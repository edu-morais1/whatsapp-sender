import logging
from supabase_client import get_contacts
from zapi_client import send_message

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


def get_first_name(full_name: str) -> str:
    parts = full_name.strip().split()
    return parts[0] if parts else ""


def is_valid_phone(phone: str) -> bool:
    digits = "".join(char for char in phone if char.isdigit())
    return len(digits) >= 10


def main():
    logger.info("Iniciando envio de mensagens...")

    contacts = get_contacts(limit=3)

    if not contacts:
        logger.warning("Nenhum contato encontrado no banco de dados.")
        return

    logger.info(f"{len(contacts)} contato(s) encontrado(s).")

    for contact in contacts:
        name = contact.get("nome")
        phone = contact.get("telefone")

        first_name = get_first_name(name) if name else ""

        if not first_name:
            logger.warning(f"Contato com nome inválido ignorado: {contact}")
            continue
        if not phone or not is_valid_phone(phone):
            logger.warning(f"Contato com telefone inválido ignorado: {contact}")
            continue

        message = f"Olá, {first_name} tudo bem com você?"

        success = send_message(phone=phone, message=message)

        if success:
            logger.info(f"Mensagem enviada para {name} ({phone}).")
        else:
            logger.error(f"Falha ao enviar mensagem para {name} ({phone}).")

    logger.info("Processo finalizado.")


if __name__ == "__main__":
    main()
