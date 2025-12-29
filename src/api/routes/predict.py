from fastapi import APIRouter, HTTPException
from schemas.car import Car, CarResponse
from services.prediction_service import PredictionService
from exceptions.feature_enginnering import FeatureEngineeringError

router = APIRouter()

@router.post('/predict', response_model=CarResponse, status_code=200)
def predict(payload: Car):
    
    try:
        return PredictionService.predict(payload)
    
    except FeatureEngineeringError:
        
        raise HTTPException(detail='Elementos não processados pelo feature enginnering', status_code=400)
    