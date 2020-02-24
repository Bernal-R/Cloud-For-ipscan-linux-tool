from fastapi import FastAPI
from .routers import analysis_metrics
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title='API Microservice',
    description='A Python-based microservice that expose an web interface to capture ip analysis metrics', 
    version='1.0.0', 
    openapi_url='/api/openapi.json',
    docs_url='/api/docs',
    redoc_url=None
)

app.include_router(analysis_metrics.router, prefix='/api/v1')

origins = [
    "http://localhost:31000",
    "http://localhost:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)