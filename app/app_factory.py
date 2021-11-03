from fastapi import FastAPI


def app_factory():
    # configure_logger()
    app = FastAPI(
        title="Lab Temperature Devices Manager",
    )
    from src.api.api_v1.api import api_router

    app.include_router(api_router)
    return app
