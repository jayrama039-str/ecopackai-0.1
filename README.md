# EcoPackAI – AI-Powered Sustainable Packaging Recommendation System

## Project Overview
EcoPackAI is an AI-powered web application that recommends eco-friendly packaging materials for different products.  
The system helps industries reduce environmental impact and cost by selecting optimal sustainable packaging solutions.

---

## Problem Statement
Traditional packaging relies heavily on non-biodegradable materials, increasing pollution and cost.  
Businesses lack intelligent systems to choose sustainable alternatives efficiently.

---

## Solution
EcoPackAI uses Machine Learning models to:
- Predict packaging cost
- Estimate CO₂ impact
- Recommend best eco-friendly material

---

## Features
-  Material Recommendation System
-  Cost Prediction
-  CO₂ Impact Prediction
-  Sustainability Score
-  BI Dashboard (charts & analytics)
-  User-friendly Web Interface

---

## Project Architecture
Frontend → Flask Backend → ML Models → PostgreSQL Database

---

##  Technologies Used
- Python
- Flask
- PostgreSQL
- HTML, CSS, Bootstrap
- JavaScript
- Scikit-learn
- XGBoost
- Matplotlib / Plotly

---

## Dataset Details
The dataset includes:
- Material Type
- Strength
- Weight Capacity
- Biodegradability Score
- CO₂ Emission Score
- Recyclability %

Product dataset includes:
- Product Category (Electronics, Food, etc.)
- Weight
- Fragility

---

##  Modules Implemented

###  Module 1: Data Collection
Collected eco-friendly packaging material dataset and product dataset.

###  Module 2: Data Cleaning & Feature Engineering
- Handled missing values
- Normalized data
- Created:
  - CO₂ Impact Index
  - Cost Efficiency Score
  - Suitability Score

### Module 3: ML Dataset Preparation
- Train-Test Split
- Feature Selection
- Data Scaling

### Module 4: ML Models
- Random Forest Regressor → Cost Prediction
- XGBoost Regressor → CO₂ Prediction

---

##  Model Performance

### 🔹 Random Forest (Cost Prediction)
- RMSE: 4.18
- MAE: 3.05
- R² Score: 0.91

### 🔹 XGBoost (CO₂ Prediction)
- RMSE: 2.73
- MAE: 2.08
- R² Score: 0.93

---

##  Backend (Flask API)
- Handles user input
- Sends data to ML model
- Returns recommended packaging material

---

##  Frontend
- Built using HTML, CSS, Bootstrap
- User input form
- Displays recommendations

---

##  Dashboard
- CO₂ Reduction %
- Cost Savings
- Material comparison charts

---

##  Deployment
- Platform: Render / Heroku
- Database: PostgreSQL Cloud

---

##  Example Output

Input:
Product: Electronics  
Weight: 1.5 kg  

Output:
Recommended Material: Recycled Cardboard  
Predicted Cost: ₹42  
CO₂ Impact: Low  

---

##  Project Structure
ecopackai/ │ ├── app.py ├── database/ ├── ml_model/ ├── static/ ├── templates/ ├── requirements.txt ├── runtime.txt └── README.md

---

##  Future Improvements
- Add more datasets
- Improve model accuracy
- Real-time industry integration
- Mobile app version
- 

---

##  Author
Jayanth  
B.Tech Student  

---

## Acknowledgement
Springboard Internship Program for guidance and mentorship.
