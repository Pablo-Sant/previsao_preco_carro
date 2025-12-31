from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]  # src/ml

ARTIFACTS_DIR = BASE_DIR / 'artifacts'

MODEL_PATH = ARTIFACTS_DIR / 'model.pkl'
PREPROCESSOR_PATH = ARTIFACTS_DIR / 'preprocessor.pkl'
