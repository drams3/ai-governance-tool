from fastapi import APIRouter
from app.services.bias_detection import check_bias

router = APIRouter(prefix="/governance", tags=["AI Governance"])

@router.get("/bias_check")
def bias_check():
    """
    Simple test endpoint to check bias detection.
    """
    bias_result = check_bias()
    return {"message": "Bias check completed", "result": bias_result}
