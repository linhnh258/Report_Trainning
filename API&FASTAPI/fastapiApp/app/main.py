from fastapi import FastAPI
from contextlib import asynccontextmanager

from .routers import v1, v2

@asynccontextmanager
async def lifespan(app: FastAPI):
    print ("----- Starting application -----")
    yield
    print ("----- Stopping -----")

app = FastAPI(
    title="Iris Model Prediction API",
    description="Model API for predict Iris Flowers, by Random Forest",
    version="2.0.0",
    lifespan=lifespan
)

@app.get("/", tags=["General"])
def read_root():
    return{"message": "Welcome to Model Prediction API"}

app.include_router(v1.router)
app.include_router(v2.router)