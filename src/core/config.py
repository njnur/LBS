from typing import List
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Basic application configuration
    APP_NAME: str = "Location-Based Service API"
    APP_VERSION: str = "1.0.0"
    DEBUG_MODE: bool = True

    # Database configurations
    MONGODB_URL: str = Field('mongodb://localhost:27017', env='MONGODB_URL')
    MONGODB_DB_NAME: str = Field('lbs', env='MONGODB_DB_NAME')

    # Security and authentication settings
    SECRET_KEY: str = Field('oB^uh%Cj!#axk0FeWL07syBz317wCc8s$dNcHcw!vs1*#avo6E^', env='SECRET_KEY')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(60*24, env='ACCESS_TOKEN_EXPIRE_MINUTES')

    # CORS configuration
    ALLOWED_HOSTS: List[str] = ["*"]

    # Additional settings can be added here

    class Config:
        # Configuration file path (if used)
        env_file = ".env"

        # This option tells the Pydantic model to read the environment variables
        env_file_encoding = 'utf-8'
        case_sensitive = True


# Instantiate the Settings
settings = Settings()
