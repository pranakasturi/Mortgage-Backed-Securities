# Machine Learning App for Mortgage Backed Securities

This repository contains a Dockerized Flask application that leverages various machine learning models (Logistic Regression, XGBoost and Gradient Boosting) to predict the probability of default for Mortgage Backed Securities (MBS). The application exposes an API endpoint for making predictions and integrates Streamlit Web App.

## Overview
This project applies Machine Learning and Data Analytics techniques to analyze and predict prepayment risk, default probability, and loss severity in Mortgage-Backed Securities (MBS) using Freddie Mac's loan performance data.

## Data Source

•	Freddie Mac Single-Family Loan Performance Data (Last 5 Years)

•	Covers 53.8 million mortgages with credit performance, loss details, and monthly loan status.

## Repository Structure
<pre>
Mortgage-Backed-Securities/
├── app_streamlit.py
├── predict_utils.py
├── models/
│   ├── logistic_regression_model.pkl
│   ├── xgboost_model.pkl
│   ├── gradient_boosting_model.pkl
├── Dockerfile
├── .dockerignore
├── requirements.txt

</pre>
---
## Technologies Used

* **Python:** The primary programming language.
* **Flask:** A micro web framework for building the API.
* **Scikit-learn:** A comprehensive library for machine learning algorithms (Logistic Regression, Gradient Boosting).
* **XGBoost:** A gradient boosting library known for its performance and scalability.
* **Pandas:** A powerful library for data manipulation and analysis.
* **NumPy:** A fundamental package for numerical computation.
* **Docker:** A platform for containerizing applications.
* **Streamlit:** A web app for predicting mortgage default risk using multiple machine learning models

## Project Pipeline
1.	Data Preprocessing – Cleaning, feature engineering, and encoding.
2.	Exploratory Data Analysis – Trend analysis and visualization.
3.	Machine Learning Models:
    o	Prepayment Risk Prediction (XGBoost)
    o	Default Probability Classification (Logistic Regression)
    o	Loss Severity Estimation (Gradient Boosting)
4.	Model Evaluation & Optimization – Using AUC-ROC, RMSE, and Hyperparameter Tuning.
5.	Deployment – Streamlit App.

## Getting Started

Follow these steps to set up and run the application:

### Prerequisites

* **Docker:** Ensure you have Docker installed on your system. You can find installation instructions for your operating system on the official Docker website: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
* **Docker Compose (Optional):** If you intend to use the `docker-compose.yml` file, ensure you have Docker Compose installed: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)
* **Python 3.x:** While the application will run inside a Docker container, having Python installed can be helpful for local development or inspection.

### Installation and Running with Docker

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/pranakasturi/Mortgage-Backed-Securities.git
    cd Mortgage-Backed-Securities
    ```

2.  **Build the Docker image:**
    Navigate to the `docker` directory and build the Docker image using the Dockerfile:
    ```bash
    cd app
    docker build -t streamlit-mortgage-app .
    cd ..
    ```

3.  **Run the Docker container:**
    ```bash
    docker run -p 8501:8501 streamlit-mortgage-app
    ```

#### Accessing the Application
Once the Docker container is running, you can access the Flask API at http://localhost:8501

## API Endpoints

The application exposes the following API endpoint:
•	/predict (POST): 
o	Description: Accepts JSON data representing the features of an MBS and returns the predicted probability of default.
o	Request Body (JSON): The JSON payload should contain the features required by the trained machine learning models. The specific features will depend on the data used for training. Example: 

```
JSON
{
  "credit_score": 200,
  "ocltv": 23.3,
  "dti": 26.5,
  "originali_upb" : 80000,
  "original_interest_rate": 5
}
```
Note: Ensure the feature names and data types in your request match the expectations of the trained models.
o	Response (JSON): 
```
JSON
{
  "logistic_regression": 1,
  "xgboost": 1,
  "gradient_boosting": 1,
}
```
The model field indicates which model was used for the prediction (this might be configurable or a default). 

## Training the Models
This repository focuses on the deployment of pre-trained models. The process of training these models (data loading, preprocessing, feature engineering, model training, and saving) is typically done in separate notebooks.

To use this application with your own data, you will need to:
1.	Train the desired machine learning models (Logistic Regression, XGBoost, Gradient Boosting, LDA) on your MBS dataset.
2.	Save the trained models in a format that can be loaded by the Flask application (e.g., using pickle or model-specific saving methods).
3.	Update the application code (app/models/) to load your trained models and ensure the feature processing aligns with how the models were trained.

## Further Development
Potential areas for further development include:
•	Model Persistence: Implement robust mechanisms for loading and managing different versions of trained models.

•	Authentication and Authorization: Secure the API endpoints.

•	Integration with Monitoring Tools: Provide example configurations for integrating with other monitoring and alerting tools.

•	A/B Testing: Implement the ability to A/B test different models.

•	CI/CD Pipeline: Set up a continuous integration and continuous deployment pipeline for automated builds and deployments.

## Contributing
Contributions to this project are welcome. Please feel free to submit pull requests or open issues for bug fixes, feature requests, or improvements.





