import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")
    SUPABASE_TABLE: str = os.getenv("SUPABASE_TABLE", "contatos")

    ZAPI_INSTANCE_ID: str = os.getenv("ZAPI_INSTANCE_ID", "")
    ZAPI_TOKEN: str = os.getenv("ZAPI_TOKEN", "")
    ZAPI_CLIENT_TOKEN: str = os.getenv("ZAPI_CLIENT_TOKEN", "")

    @classmethod
    def validate(cls):
        required = [
            ("SUPABASE_URL", cls.SUPABASE_URL),
            ("SUPABASE_KEY", cls.SUPABASE_KEY),
            ("ZAPI_INSTANCE_ID", cls.ZAPI_INSTANCE_ID),
            ("ZAPI_TOKEN", cls.ZAPI_TOKEN),
        ]
        missing = [name for name, value in required if not value]
        if missing:
            raise EnvironmentError(
                f"Variáveis de ambiente obrigatórias não definidas: {', '.join(missing)}"
            )
