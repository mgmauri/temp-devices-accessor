from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    EVKSCONFIGFILE: str
    PARAMSCONFIGFILE: str


# FIXME env_ setting
env_ = os.environ["PROJ_TDM"] + "/.env"
settings = Settings(_env_file=env_)
