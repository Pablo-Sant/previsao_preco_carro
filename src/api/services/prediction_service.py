from src.api.schemas.car import Car
from src.ml.preprocessing import simplificar_cores
from src.ml.pipeline.prediction_pipeline import PredictionPipeline
from src.api.exceptions.feature_enginnering import FeatureEngineeringError
class PredictionService:
    
    @staticmethod
    def predict(dto: Car):
        
        # passar pelo validations do damain
        
        data = dto.model_dump() # transformando em dicionário
        
        color_int = data.pop('color_int') # retira feature que será transformada
        color_ext = data.pop('color_ext') # retira feature que será transformada
        
        colors = simplificar_cores(color_int, color_ext) # recebe features transformadas em forma de dict
        
        if not colors:
            raise FeatureEngineeringError
        
        data.update(colors) # coloca essas as features trasnformadas no dict
        
        price = PredictionPipeline.predict(data=data)
        
        return {'price': price}

        # passar por normalização e encoder
        
        # passar por predição
        

        