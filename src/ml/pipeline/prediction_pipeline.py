import pandas as pd
import joblib
from src.ml.configs import MODEL_PATH, PREPROCESSOR_PATH

class PredictionPipeline:

    model = joblib.load(MODEL_PATH)
    preprocessor = joblib.load(PREPROCESSOR_PATH)

    @staticmethod
    def predict(data: dict) -> float:
        df = pd.DataFrame([data])
        x = PredictionPipeline.preprocessor.transform(df)
        pred = PredictionPipeline.model.predict(x)
        return float(pred[0])