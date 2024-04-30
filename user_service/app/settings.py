from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    amqp_url: str
    postgres_url: str

    model_config = SettingsConfigDict(env_file='.env')

print("Loading environment variables...")
settings = Settings()

print("AMQP URL:", settings.amqp_url)
print("PostgreSQL URL:", settings.postgres_url)
