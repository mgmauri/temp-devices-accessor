
from fastapi import HTTPException
from fastapi import status


EvkNameNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Could not find evk name",
)

TemperatureOutOfRange = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE,
    detail="Set temperature out of range"
)
