from fastapi import APIRouter
from src.api.endpoint import predict

api_router = APIRouter()

api_router.include_router(predict.router)