from fastapi import FastAPI
from .routers import analysis_metrics

app = FastAPI(
    title='API Microservice 2',
    description='A Python-based microservice that expose an web interface to capture ip analysis metrics', 
    version='1.0.0', 
    openapi_url='/api/openapi.json',
    docs_url='/api/docs',
    redoc_url=None
)

app.include_router(analysis_metrics.router, prefix='/api/v1')
