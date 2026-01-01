from fastapi import APIRouter


router = APIRouter()

@router.get('/', status_code=200)
def check():
    
    return {
        
        'status': 'ok',
        'message': 'API de predição de preço de carro online'
    }