# import uvicorn
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"temperature": 12.4}


# def start():
#     """Launched with `poetry run start` at root level"""
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


# if __name__ == "__main__":
#     start()
# # poetry run python main.py
import uvicorn
from app_factory import app_factory

app = app_factory()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
