from pydantic import BaseModel, Field

class IrisFeatures(BaseModel):
    """
    Schema for input data of Iris model
    """
    sepal_length: float = Field(..., example=5.1, description="Sepal length")
    sepal_width: float = Field(..., example = 3.5, description="Sepal width")
    petal_length: float = Field(..., example=1.4, description="Petal length")
    petal_width: float = Field(..., example=0.2, description="Petal width")

    class Config:
        # Provide complete example for IrisFeatures object 
        schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width" : 3.5,
                "petal_length" : 1.4,
                "petal_width" : 0.2
            }
        }

class PredictResponse(BaseModel):
    """
    Schema for output data (prediction)
    """
    predicted_class: str = Field(..., example="setosa", description="Class predicted")
    prediction_index: int = Field(..., example = 0, description="Index of class predicted")

class PredictResponseV2(PredictResponse):
    """
    Schema for output data (prediction) - Version 2
    Include confidence score and execution time
    """
    confidence_score: float = Field(..., example=0.98, description="Confidence score of model when predicted (from 0.0 to 1.0)")
    execution_time: float = Field(..., example=5.2, description="Execution time of model when predict(ms)")