from pydantic import BaseModel, Field, conint, confloat

class HeartFeatures(BaseModel):
    age: conint(ge=0) = Field(..., example=63, description="Age in years")
    sex: conint(ge=0, le=1) = Field(..., example=1, description="1 = male, 0 = female")
    cp: conint(ge=0, le=3) = Field(..., example=3, description="Chest pain type (0-3)")
    trestbps: conint(ge=0) = Field(..., example=145, description="Resting blood pressure (mm Hg)")
    chol: conint(ge=0) = Field(..., example=233, description="Serum cholestoral (mg/dl)")
    fbs: conint(ge=0, le=1) = Field(..., example=1, description="Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)")
    restecg: conint(ge=0, le=2) = Field(..., example=2, description="Resting electrocardiographic results (0-2)")
    thalach: conint(ge=0) = Field(..., example=150, description="Maximum heart rate achieved")
    exang: conint(ge=0, le=1) = Field(..., example=0, description="Exercise induced angina (1 = yes; 0 = no)")
    oldpeak: confloat(ge=0) = Field(..., example=2.3, description="ST depression induced by exercise relative to rest")
    slope: conint(ge=0, le=2) = Field(..., example=0, description="Slope of the peak exercise ST segment (0-2)")
    ca: conint(ge=0, le=4) = Field(..., example=0, description="Number of major vessels colored by flourosopy (0-4)")
    thal: conint(ge=0, le=3) = Field(..., example=1, description="Thalassemia (0 = unknown, 1 = normal, 2 = fixed defect, 3 = reversible defect)")

    # Pydantic v2 config
    model_config = {"from_attributes": True}


class PredictionResponse(BaseModel):
    prediction: int = Field(..., example=1, description="Predicted presence of heart disease (1 = yes, 0 = no)")
    probability: float = Field(..., example=0.85, description="Prediction probability")