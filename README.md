# 📦 Freight & Invoice Intelligence System

An end-to-end **Machine Learning application** for logistics businesses that helps predict **freight costs** and identify **invoice risk levels**.

The project combines **Machine Learning, Logistic reg, XGBoost, SQL, FastAPI and Streamlit** into a complete business-oriented prediction system.

---

## 🚀 Live Demo

### 🖥️ Streamlit Application
https://freight-invoice-intelligence-4.streamlit.app/

### ⚡ FastAPI Backend
https://freight-invoice-intelligence.onrender.com/

### 📚 API Documentation
https://freight-invoice-intelligence.onrender.com/docs

---

## 💼 Business Problem

Logistics companies handle a large number of shipments, vendors and invoices.

Two important business problems are:

### 📦 1. Freight Cost Prediction

Freight costs can vary depending on:

- Distance
- Transport mode
- Vehicle type
- Shipment weight
- Shipment volume
- Shipment type
- Delivery time
- Vendor performance

Accurately estimating freight cost can help businesses with **cost planning, budgeting and shipment decisions**.

### ⚠️ 2. Invoice Risk Detection

Logistics businesses may process a large number of invoices.

Some invoices may contain characteristics that require additional verification, such as:

- Higher invoice amount than expected
- Payment delays
- Vendor-related factors
- Shipment-related factors

Manually reviewing every invoice can be time-consuming.

This system helps identify invoices that may require **additional manual review**.

---

## 🎯 Project Objectives

The system has two major objectives:

### 📦 Freight Cost Prediction

Predict the expected freight cost of a shipment using shipment, transportation and vendor-related information.

### ⚠️ Invoice Risk Prediction

Classify an invoice into:

- 🔴 High Risk
- 🟡 Medium Risk
- 🟢 Low Risk

The system also provides the probability associated with each risk level.

---

# 🧠 Machine Learning Approach

## 📦 Freight Cost Prediction

Freight cost prediction is treated as a **Regression problem** because the target variable is a continuous numerical value.

### Features Used

#### 🔢 Numerical Features

- Distance_KM
- Weight_KG
- Volume_CBM
- Delivery_Days
- Vendor_Rating
- Vendor_Experience_Years

#### 🔤 Categorical Features

- Origin_City
- Destination_City
- Transport_Mode
- Vehicle_Type
- Shipment_Type

### Models

The project uses:

- 📊 Linear Regression as a baseline model
- 🚀 XGBoost for the main regression approach

The baseline model provides a simple reference point, while XGBoost is used to capture more complex relationships between shipment characteristics and freight cost.

---

## ⚠️ Invoice Risk Prediction

Invoice risk prediction is treated as a **Classification problem**.

The model predicts:

- 🔴 High Risk
- 🟡 Medium Risk
- 🟢 Low Risk

The API also returns class probabilities so that the application can show the probability associated with each risk level.

---

---

# 📊 Model Performance

## 📦 Freight Cost Prediction

The final freight cost model uses **tuned XGBoost Regressor**.

| Metric | Score |
|---|---:|
| MAE | 2,440.56 |
| RMSE | 4,674.26 |
| R² Score | **0.9512** |

The tuned XGBoost model achieved an **R² score of 0.9512** on the test dataset.

---

## ⚠️ Invoice Risk Prediction

For invoice risk classification, **Logistic Regression** was selected as the final model.

Although the XGBoost classifier achieved higher overall accuracy (89.3%), its recall for the High-risk class was only 5%.

Therefore, Logistic Regression with `class_weight="balanced"` was selected because it achieved better High-risk recall of **51%**, which is more important for identifying invoices that may require manual review.

| Metric | Score |
|---|---:|
| Accuracy | **78.56%** |
| High Risk Recall | **51%** |
| Medium Risk Recall | 35% |
| Low Risk Recall | 88% |
| Macro F1-Score | 0.49 |
| Weighted F1-Score | 0.80 |


# 🔍 Data Analysis & Preprocessing

The project includes:

- Exploratory Data Analysis
- Missing-value analysis
- Numerical feature analysis
- Categorical feature analysis
- Feature preprocessing
- Encoding of categorical variables
- Model training and evaluation

### 🛠️ Libraries Used

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost

---

---

# 💼 LinkedIn

Connect with me on LinkedIn:

🔗 **LinkedIn Profile:**  
https://www.linkedin.com/in/sahil-rohilla-7436a635a/

---

# 🗄️ SQL Analysis

SQL is used for **business-oriented analysis** of the logistics data.

The analysis focuses on areas such as:

- 📦 Shipment analysis
- 💰 Freight cost analysis
- 🚚 Vendor performance
- 📊 Business-level aggregations
- ⚠️ Invoice-related analysis

SQL helps convert raw logistics data into useful business insights before and alongside the Machine Learning workflow.

---

# ⚡ FastAPI Backend

FastAPI is used as the backend API layer between the frontend application and the Machine Learning models.

## 📦 Freight Prediction API

```text
POST /predict/freight