from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    EVKSCONFIGFILE: str
    PARAMSCONFIGFILE: str


# FIXME env_ setting
_env = os.environ.get("PROJ_TDM") + "/.env"
settings = Settings(_env)
