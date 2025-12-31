from fastapi import FastAPI
from src.api.endpoint.router import api_router

app = FastAPI(title='Previsão preço de carro')
app.include_router(api_router)

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
    