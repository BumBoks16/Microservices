from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    amqp_url: str
    postgres_url: str
    is_local: bool =False

    model_config = SettingsConfigDict(env_file='.env')

print("Loading environment variables...")
settings = Settings()

print("AMQP URL:", settings.amqp_url)
print("PostgreSQL URL:", settings.postgres_url)
