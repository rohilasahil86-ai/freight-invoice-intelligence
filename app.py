import streamlit as st
import pandas as pd
import requests


st.set_page_config(
    page_title="Freight & Invoice Intelligence System",
    page_icon="📦",
    layout="wide"
)


st.title("📦 Freight & Invoice Intelligence System")

st.write("Predict freight costs and identify invoice risk levels.")


tab1, tab2 = st.tabs([
    "📦 Freight Cost Prediction",
    "⚠️ Invoice Risk Prediction"
])


# Freight cost prediction tap 1

with tab1:

    st.header("Freight Cost Prediction")

    col1, col2 = st.columns(2)

    with col1:

        origin_city = st.selectbox(
            "Origin City",
            [
                "Ahmedabad", "Bengaluru", "Chandigarh", "Chennai",
                "Delhi", "Hyderabad", "Indore", "Jaipur",
                "Kochi", "Kolkata", "Lucknow", "Mumbai",
                "Nagpur", "Pune", "Surat"
            ]
        )

        distance = st.number_input("Distance (KM)", min_value=0.0)

        vehicle_type = st.selectbox(
            "Vehicle Type",
            ["Air Cargo Express", "Air Cargo Standard", "Cargo Wagon", "Container Wagon", 
             "LCV", "Mini Truck", "Trailer", "Truck"]
             )

        volume = st.number_input("Volume (CBM)", min_value=0.0)

        delivery_days = st.number_input("Delivery Days",min_value=0,step=1)

        vendor_experience = st.number_input("Vendor Experience (Years)", min_value=0.0)


    with col2:

        destination_city = st.selectbox(
            "Destination City",
            [
                "Ahmedabad", "Bengaluru", "Chandigarh", "Chennai",
                "Delhi", "Hyderabad", "Indore", "Jaipur",
                "Kochi", "Kolkata", "Lucknow", "Mumbai",
                "Nagpur", "Pune", "Surat"
            ]
        )

        transport_mode = st.selectbox(
            "Transport Mode",
            ["Air", "Rail", "Road"]
        )

        weight = st.number_input("Weight (KG)", min_value=0.0)

        shipment_type = st.selectbox("Shipment Type", ["Bulk", "Express", "Fragile", "Standard"])

        vendor_rating = st.number_input("Vendor Rating", min_value=0.0, max_value=5.0)


        st.divider()

    if st.button(
        "Predict Freight Cost",
        key="freight_predict"
        ):

        # Input Validation
        if distance <= 0:
            st.error("Distance must be greater than 0.")

        elif weight <= 0:
            st.error("Weight must be greater than 0.")

        elif volume <= 0:
            st.error("Volume must be greater than 0.")

        elif delivery_days < 0:
            st.error("Delivery Days cannot be negative.")

        elif vendor_rating < 0 or vendor_rating > 5:
            st.error("Vendor Rating must be between 0 and 5.")

        elif vendor_experience < 0:
            st.error("Vendor Experience cannot be negative.")

        else:

            # Create input dataframe
            input_data = pd.DataFrame({
                "Origin_City": [origin_city],
                "Destination_City": [destination_city],
                "Distance_KM": [distance],
                "Transport_Mode": [transport_mode],
                "Vehicle_Type": [vehicle_type],
                "Weight_KG": [weight],
                "Volume_CBM": [volume],
                "Shipment_Type": [shipment_type],
                "Delivery_Days": [delivery_days],
                "Vendor_Rating": [vendor_rating],
                "Vendor_Experience_Years": [vendor_experience]
            })


            # connect streamlit to api
            response = requests.post(
                "https://freight-invoice-intelligence.onrender.com/predict/freight",
                json=input_data.to_dict(orient="records")[0] 
                )


            # use 
            if response.status_code == 200:
        
                result = response.json()
                st.success(f"Predicted Freight Cost: ₹{result['predicted_freight_cost']:,.2f}")

            else:
                st.error("Unable to get prediction from API.")
                

# Invoice risk predicion tab 2

with tab2:

    st.header("Invoice Risk Prediction")

    col1, col2 = st.columns(2)

    with col1:
        distance = st.number_input("Distance (KM)", min_value=0.0, key="risk_distance")

        transport_mode = st.selectbox("Transport Mode", ["Air", "Rail", "Road"], key="risk_transport")

        vehicle_type = st.selectbox(
            "Vehicle Type",
            [
                "Air Cargo Express",
                "Air Cargo Standard",
                "Cargo Wagon",
                "Container Wagon",
                "LCV",
                "Mini Truck",
                "Trailer",
                "Truck"
            ],
            key="risk_vehicle"
        )

        weight = st.number_input("Weight (KG)", min_value=0.0, key="risk_weight")

        volume = st.number_input("Volume (CBM)", min_value=0.0, key="risk_volume")

        shipment_type = st.selectbox(
            "Shipment Type",
            ["Bulk", "Express", "Fragile", "Standard"],
            key="risk_shipment"
        )

        delivery_days = st.number_input("Delivery Days", min_value=0, step=1, key="risk_delivery")

    with col2:

        vendor_rating = st.number_input("Vendor Rating", min_value=0.0, max_value=5.0, key="risk_rating")

        vendor_experience = st.number_input(
            "Vendor Experience (Years)", min_value=0.0, key="risk_experience")

        invoice_amount = st.number_input("Invoice Amount", min_value=0.0, key="risk_invoice_amount")

        expected_invoice_amount = st.number_input(
            "Expected Invoice Amount", min_value=0.0, key="risk_expected_amount")

        payment_status = st.selectbox(
            "Payment Status", ["Paid", "Pending", "Overdue"], key="risk_payment_status"
            )

        payment_delay = st.number_input("Payment Delay (Days)", min_value=0, step=1,
                                         key="risk_payment_delay")


    st.divider()


    if st.button("Predict Invoice Risk", key="risk_predict"):

        # Input Validation
        if distance <= 0:
            st.error("Distance must be greater than 0.")


        elif weight <= 0:
            st.error("Weight must be greater than 0.")


        elif volume <= 0:
            st.error("Volume must be greater than 0.")

        elif vendor_rating < 0 or vendor_rating > 5:
            st.error("Vendor Rating must be between 0 and 5.")

        elif vendor_experience < 0:
            st.error("Vendor Experience cannot be negative.")

        elif invoice_amount <= 0:
            st.error("Invoice Amount must be greater than 0.")

        elif expected_invoice_amount <= 0:
            st.error("Expected Invoice Amount must be greater than 0.")

        elif payment_delay < 0:
            st.error("Payment Delay cannot be negative.")

        else:
# Create input DataFrame
            input_data = pd.DataFrame({
                "Distance_KM": [distance],
                "Transport_Mode": [transport_mode],
                "Vehicle_Type": [vehicle_type],
                "Weight_KG": [weight],
                "Volume_CBM": [volume],
                "Shipment_Type": [shipment_type],
                "Delivery_Days": [delivery_days],
                "Vendor_Rating": [vendor_rating],
                "Vendor_Experience_Years": [vendor_experience],
                "Invoice_Amount": [invoice_amount],
                "Expected_Invoice_Amount": [expected_invoice_amount],
                "Payment_Status": [payment_status],
                "Payment_Delay_Days": [payment_delay]
            })


            #COnnect streamlit to api
            response = requests.post(
                "https://freight-invoice-intelligence.onrender.com/predict/risk",
                json=input_data.to_dict(orient="records")[0])


            # Handle api response with pydantic 
            if response.status_code == 200:

                result = response.json()
                risk = result["predicted_risk"]

                risk_probabilities = result["risk_probabilities"]


                # Risk Probability
                probability_df = pd.DataFrame({
                    "Risk Level": risk_probabilities.keys(),
                    "Probability": risk_probabilities.values()
                })

                probability_df["Probability"] = ( probability_df["Probability"] * 100).round(2)


                st.subheader("Risk Probability")

                st.dataframe(probability_df, hide_index=True)

                # Prediction Result
                st.subheader("Prediction Result")

                if risk == "High":
                    st.error("🔴 HIGH RISK")
                    st.write("Immediate review required.")

                elif risk == "Medium":
                    st.warning("🟡 MEDIUM RISK")
                    st.write("Manual verification recommended.")

                else:
                    st.success("🟢 LOW RISK")
                    st.write("No immediate action required.")

            else:
                error = response.json()
                st.error("API request failed. Please check your inputs.")
                st.write(error)