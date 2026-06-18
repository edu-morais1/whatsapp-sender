import logging
from supabase_client import get_contacts
from zapi_client import send_message

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    logger.info("Iniciando envio de mensagens...")

    contacts = get_contacts(limit=3)
    print(contacts)
    if not contacts:
        logger.warning("Nenhum contato encontrado no banco de dados.")
        return

    logger.info(f"{len(contacts)} contato(s) encontrado(s).")

    for contact in contacts:
        name = contact.get("nome")
        phone = contact.get("telefone")

        if not name or not phone:
            logger.warning(f"Contato com dados incompletos ignorado: {contact}")
            continue

        message = f"Olá, {name} tudo bem com você?"

        success = send_message(phone=phone, message=message)

        if success:
            logger.info(f"Mensagem enviada para {name} ({phone}).")
        else:
            logger.error(f"Falha ao enviar mensagem para {name} ({phone}).")

    logger.info("Processo finalizado.")


if __name__ == "__main__":
    main()
