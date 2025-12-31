from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

ARTIFACTS_DIR = PROJECT_ROOT / 'src' / 'ml' / 'artifacts'

MODEL_PATH = ARTIFACTS_DIR / 'model.pkl'
PREPROCESSOR_PATH = ARTIFACTS_DIR / 'preprocessor.pkl'
