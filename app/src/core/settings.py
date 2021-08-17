from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    DRIVERSCONFIGFILE: str
    OPERATIONCONFIGFILE: str


# FIXME env_ setting
_env = os.environ.get("PROJ_TDM") + "/.env"
settings = Settings(_env)
