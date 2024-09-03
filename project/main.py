from fastapi import FastAPI
import api

app = FastAPI()

app.include_router(api.app)