from fastapi import APIRouter
from src.api.endpoint import predict
from src.api.endpoint import health_check

api_router = APIRouter()

api_router.include_router(health_check.router)
api_router.include_router(predict.router)
