from schemas.car import Car
from ml.preprocessing import simplificando_cores
from exceptions.feature_enginnering import FeatureEngineeringError
class PredictionService:
    
    @staticmethod
    def predict(dto: Car):
        
        # passar pelo validations do damain
        
        data = dto.model_dump() # transformando em dicionário
        
        color_int = data.pop('color_int') # retira feature que será transformada
        color_ext = data.pop('color_ext') # retira feature que será transformada
        
        colors = simplificando_cores(color_int, color_ext) # recebe features transformadas em forma de dict
        
        if not colors:
            raise FeatureEngineeringError
        
        data.update(colors) # coloca essas as features trasnformadas no dict
        
        
        # passar por normalização e encoder
        
        # passar por predição
        

        