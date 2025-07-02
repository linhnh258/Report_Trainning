import joblib
import os
import pandas as pd
from ..model_schemas import IrisFeatures

class ModelPredictor:
    def __init__(self):
        base_dir = os.path.dirname(__file__)
        model_path = os.path.join(base_dir, "trained_models/random_forest_iris.joblib")
        class_name_path = os.path.join(base_dir, "trained_models/class_names.joblib")

        try:
            self.model = joblib.load(model_path)
            self.class_names = joblib.load(class_name_path)
            print("Succesful for load model and class_names")
        except FileNotFoundError:
            print("Error: No such file")
            self.model = None
            self.class_names = []
    
    def predict(self, features: IrisFeatures) -> (int, str, float):
        """
        Predict base on input feature
        """
        if not self.model:
            raise RuntimeError("Model is not loaded. Cannot predict!")
        
        input_data = pd.DataFrame([features.dict()])
        prediction_index = self.model.predict(input_data)[0]

        probabilities = self.model.predict_proba(input_data)[0]
        confidence = probabilities[prediction_index]

        predicted_class_name = self.class_names[prediction_index]

        return int(prediction_index), predicted_class_name, float(confidence)

predictor = ModelPredictor()