import time 
from fastapi import APIRouter, HTTPException

from ..model_schemas import IrisFeatures, PredictResponseV2
from ..ml.model import predictor

router = APIRouter(
    prefix="/v2",
    tags = ["Predictions V2"]
)

@router.post("/predict", response_model = PredictResponseV2)
def predict_iris_v2(features: IrisFeatures):
    if predictor.model is None:
        raise HTTPException(
            status_code=503,
            detail = "Model invalid!"
        )
    
    try: 
        start_time = time.time()
        prediction_index, predicted_class, confidence = predictor.predict(features)
        end_time = time.time()
        execution_time_ms = (end_time - start_time)*1000

        return PredictResponseV2(
            predicted_class=predicted_class,
            prediction_index=prediction_index,
            confidence_score=confidence,
            execution_time=execution_time_ms
        )
    except Exception as e:
        print(f"ĐÃ XẢY RA LỖI: {e}") 
        raise HTTPException(status_code=500, detail = str(e))