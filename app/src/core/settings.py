from pydantic import BaseSettings


class Settings(BaseSettings):
    DRIVERSCONFIGFILE: str
    OPERATIONCONFIGFILE: str
    LOGSPATH: str


settings = Settings()
