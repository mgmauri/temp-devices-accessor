from fastapi import HTTPException
from fastapi import status


EvkNameNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Could not find evk name",
)
