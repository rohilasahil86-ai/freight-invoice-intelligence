import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
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

#For freight cost request 
class FreightRequest(BaseModel):
    Origin_City: str
    Destination_City: str
    Distance_KM: float
    Transport_Mode: str
    Vehicle_Type: str
    Weight_KG: float
    Volume_CBM: float
    Shipment_Type: str
    Delivery_Days: int
    Vendor_Rating: float
    Vendor_Experience_Years: float

# For invoice risk request
class RiskRequest(BaseModel):
    Distance_KM: float
    Transport_Mode: str
    Vehicle_Type: str
    Weight_KG: float
    Volume_CBM: float
    Shipment_Type: str
    Delivery_Days: int
    Vendor_Rating: float
    Vendor_Experience_Years: float
    Invoice_Amount: float
    Expected_Invoice_Amount: float
    Payment_Status: str
    Payment_Delay_Days: int


# For Freightcost model post
@app.post("/predict/freight")
def predict_freight(request: FreightRequest):

    input_data = pd.DataFrame([request.model_dump()])

    prediction = freight_model.predict(input_data)

    return {
        "predicted_freight_cost": float(prediction[0])
    }

## For risk invoice 
@app.post("/predict/risk")
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