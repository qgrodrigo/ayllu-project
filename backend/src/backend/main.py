from fastapi import FastAPI
from backend.commoner.router import router as commoner_router

app = FastAPI()

app.include_router(commoner_router)