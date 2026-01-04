from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get('/', status_code=200)
def check():
    
    return RedirectResponse(url='/docs')