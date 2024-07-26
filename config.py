from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False
    )

    bot_token: str
    admin_ids: frozenset[int] = frozenset({33, 979871718})
    
settings = Settings()