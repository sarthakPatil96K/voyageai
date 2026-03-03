from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from app.api.routes import router
from app.config import settings

from fastapi.middleware.cors import CORSMiddleware

 
def create_app() -> FastAPI:
    app = FastAPI(
        title="VoyageAI",
        version="1.0.0"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)
    return app


app = create_app()
