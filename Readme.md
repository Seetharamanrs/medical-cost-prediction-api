# Medical Cost Prediction 
## Project Overview
    This project is an end-to-end Machine Learning application that predicts individual medical insurance costs based on personal and health-related attributes.
    The model is trained on historical data and deployed as a REST API, allowing real-time predictions from anywhere.

## Objectives
- Predict medical insurance charges using regression models
- Perform Exploratory Data Analysis (EDA) to understand key factors
- Identify feature importance affecting medical costs
- Build and compare multiple regression models
- Deploy the model using a Flask API on AWS

## Dataset

The dataset includes the following features:

- age: Age of the individual
- sex: Gender (male/female)
- bmi: Body Mass Index
- children: Number of dependents
- smoker: Smoking status (yes/no)
- region: Residential region
- charges: Medical cost (target variable)

## Exploratory Data Analysis (EDA)
Key insights from data analysis:

- Smoking has the strongest impact on medical costs
- Medical charges increase with age
- Higher BMI is associated with higher costs
- Smokers with high BMI incur significantly higher expenses

## Key Insights
- Smoking status has the strongest impact on medical costs
- Charges increase with age and BMI
- Smokers with higher BMI incur significantly higher expenses
## Preprocessing
- Applied one-hot encoding for categorical variables
- Ensured all features are numeric for model compatibility

## Model Performance

|Model	          |MAE	|   MSE	  |R² Score|
|-----------------|-----|---------|--------|
|Linear Regression|	4181|	33.59M|	0.78   |
|Ridge Regression |	4193|	33.64M|	0.78   |
|Lasso Regression |	4181|	33.59M|	0.78   |
|Random Forest    | 2560|	20.66M|	0.87   |

## Feature Importance

Top contributing features:

- Smoking status (most significant)
- BMI
- Age

## API Development

The model is deployed using Flask with the following endpoint:

🔹 POST /predict

Request Example:
```
{
  "age": 30,
  "sex": "male",
  "bmi": 25,
  "children": 1,
  "smoker": "no",
  "region": "southeast"
}

Response:
{
  "prediction": 12345.67
}
```
## Deployment
- Deployed on AWS EC2
- Configured security groups for external access
- API accessible via public IP
## Testing

Tested with multiple scenarios:

- Low-risk individuals (non-smokers)
- High-risk individuals (smokers)
- High BMI and older age cases

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Flask
- Joblib
- AWS EC2
## Key Learnings
- Implemented End-to-end ML workflow (EDA → Modeling → Deployment)
- Handling categorical data using encoding techniques
- Model comparison and evaluation
- Building and deploying REST APIs
- Real-world testing and debugging

## - Author

Seetharaman R
