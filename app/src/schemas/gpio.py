from typing import Optional
from pydantic import BaseModel


class BaseGpioSetter(BaseModel):
    evk_name: str
    value: bool


class AppTemperatureSetter(BaseGpioSetter):
    user_name: str


class BaseGpioGetter(BaseModel):
    evk_name: str


class AppGpioGetter(BaseGpioGetter):
    user_name: Optional[str]
