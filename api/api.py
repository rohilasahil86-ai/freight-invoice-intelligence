import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib

app = FastAPI(
    title="Freight & Invoice Intelligence API",
    description="API for freight cost and invoice risk prediction",
    version="1.0.0"
)

# Load ML model
freight_model = joblib.load("model/freight_cost_model.pkl")


#  load the ml invoice model
risk_model = joblib.load("model/invoice_risk_model.pkl")

# For freight cost request
class FreightRequest(BaseModel):
    Origin_City: str
    Destination_City: str
    Distance_KM: float = Field(gt=0)
    Transport_Mode: str
    Vehicle_Type: str
    Weight_KG: float = Field(gt=0)
    Volume_CBM: float = Field(gt=0)
    Shipment_Type: str
    Delivery_Days: int = Field(ge=0)
    Vendor_Rating: float = Field(ge=0, le=5)
    Vendor_Experience_Years: float = Field(ge=0)


# For invoice risk request
class RiskRequest(BaseModel):
    Distance_KM: float = Field(gt=0)
    Transport_Mode: str
    Vehicle_Type: str
    Weight_KG: float = Field(gt=0)
    Volume_CBM: float = Field(gt=0)
    Shipment_Type: str
    Delivery_Days: int = Field(ge=0)
    Vendor_Rating: float = Field(ge=0, le=5)
    Vendor_Experience_Years: float = Field(ge=0)
    Invoice_Amount: float = Field(gt=0)
    Expected_Invoice_Amount: float = Field(gt=0)
    Payment_Status: str
    Payment_Delay_Days: int = Field(ge=0)


# Response model for freight prediction
class FreightResponse(BaseModel):
    predicted_freight_cost: float


# Response model for invoice risk prediction
class RiskResponse(BaseModel):
    predicted_risk: str
    risk_probabilities: dict[str, float]


# For Freightcost model post
@app.post("/predict/freight", response_model=FreightResponse)
def predict_freight(request: FreightRequest):

    input_data = pd.DataFrame([request.model_dump()])

    prediction = freight_model.predict(input_data)

    return {
        "predicted_freight_cost": float(prediction[0])
    }

## For risk invoice 
@app.post("/predict/risk", response_model=RiskResponse)
def predict_risk(request: RiskRequest):

    input_data = pd.DataFrame([request.model_dump()])

    prediction = risk_model.predict(input_data)[0]

    probabilities = risk_model.predict_proba(input_data)[0]

    classes = risk_model.classes_

    risk_probabilities = {
        str(classes[i]): float(probabilities[i])
        for i in range(len(classes))
    }

    return {
        "predicted_risk": str(prediction),
        "risk_probabilities": risk_probabilities
    }


@app.get("/")
def home():
    return {
        "message": "Freight & Invoice Intelligence API is running"
    }