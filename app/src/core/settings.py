from pydantic import BaseSettings


class Settings(BaseSettings):
    EVKSCONFIGFILE: str
    PARAMSCONFIGFILE: str


# FIXME env_ setting
env_ = "/home/mgarcia/Projects/TempDevicesControl/temp-devices-manager/.env"
settings = Settings(_env_file=env_)
