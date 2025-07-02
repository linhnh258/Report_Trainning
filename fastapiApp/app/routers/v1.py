from fastapi import APIRouter, HTTPException
from ..model_schemas import IrisFeatures, PredictResponse
from ..ml.model import predictor

router = APIRouter(
    prefix="/v1",
    tags=["Predictions V1"]
)

@router.post("/predict", response_model=PredictResponse)
def predict_iris_v1(features: IrisFeatures):
    if predictor.model is None: 
        raise HTTPException(status_code=503, detail="Model invalid")
    try:
        prediction_index, predicted_class, _ = predictor.predict(features)

        return PredictResponse(
            predicted_class=predicted_class,
            prediction_index=prediction_index
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))