from typing import List

from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from api import router
from api.home.home import home_router


def init_routers(app_: FastAPI) -> None:
    app_.include_router(home_router)
    app_.include_router(router)


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
    ]
    return middleware


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Sample APIr",
        description="",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        dependencies=[],
        # middleware=make_middleware(),
    )
    init_routers(app_=app_)
    return app_


app = create_app()
