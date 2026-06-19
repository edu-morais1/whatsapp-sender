import logging
import requests
from config import Config

logger = logging.getLogger(__name__)

ZAPI_BASE_URL = "https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"


def send_message(phone: str, message: str) -> bool:
    """Envia uma mensagem de texto via Z-API. Retorna True se bem sucedido."""
    Config.validate()

    url = ZAPI_BASE_URL.format(
        instance_id=Config.ZAPI_INSTANCE_ID,
        token=Config.ZAPI_TOKEN,
    )

    headers = {"Content-Type": "application/json"}
    if Config.ZAPI_CLIENT_TOKEN:
        headers["Client-Token"] = Config.ZAPI_CLIENT_TOKEN

    payload = {"phone": phone, "message": message}
    response = None
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        return True
    except requests.exceptions.HTTPError as e:
        logger.error(
            f"Erro HTTP ao enviar mensagem: {e} | Resposta: {response.text if response else 'sem resposta'}"
        )
        return False
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro de conexão ao enviar mensagem: {e}")
        return False
