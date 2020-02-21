from fastapi import APIRouter
from typing import Dict, List
from app.schemas import CreateAnalysisMetric
from app.crud import db_operations

router = APIRouter()

@router.post('/analysis_metric', tags=['IP ANALYSIS'], response_model=Dict)
async def submit_ip_analysis_metric(metrics: CreateAnalysisMetric):
    db_operations.insert_data(metrics)
    return {
        "metrics":metrics,
        "status": "saved"
    }

@router.get('/analysis_metric/{ip}', tags=['IP ANALYSIS'], response_model=Dict)
async def get_ip_analysis_metric(ip: str):
    result = db_operations.get_data(ip)
    return {
        "ip": result[0][0],
        "score": result[0][1],
        "country": result[0][2],
        "bots": result[0][3],
        "crypto_mining": result[0][4],
        "ip_scan": result[0][5],
        "ip_dynamic": result[0][6],
        "malware": result[0][7],
        "anonymization": result[0][8],
        "botnets_command_center": result[0][9],
        "spam": result[0][10]
    }