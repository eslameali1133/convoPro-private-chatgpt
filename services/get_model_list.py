import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings

settings = Settings()


def get_ollama_models_list():
    models_list = settings.OLLAMA_MODELS  # str data type from .env file
    ollama_models = [model.strip() for model in models_list.split(",") if model.strip()]
    return ollama_models


# Example usage
# check_ollama_models = get_ollama_models_list()
# print(type(check_ollama_models))   
# print(check_ollama_models)        