from typing import Optional
from pydantic import BaseModel


class BaseTemperatureSetter(BaseModel):
    evk_name: str
    temperature: float


class AppTemperatureSetter(BaseTemperatureSetter):
    user_name: Optional[str]


class BaseTemperatureGetter(BaseModel):
    evk_name: str


class AppTemperatureGetter(BaseModel):
    user_name: Optional[str]
