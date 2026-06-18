import logging
from supabase import create_client, Client
from config import Config

logger = logging.getLogger(__name__)


def get_supabase_client() -> Client:
    Config.validate()
    return create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)


def get_contacts(limit: int = 3) -> list[dict]:
    try:
        client = get_supabase_client()
        response = (
            client.table(Config.SUPABASE_TABLE)
            .select("nome, telefone")
            .limit(limit)
            .execute()
        )
        return response.data or []
    except Exception as e:
        logger.error(f"Erro ao buscar contatos no Supabase: {e}")
        return []
