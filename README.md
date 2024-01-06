# Sara-Zeus Breast Cancer Prediction App :stethoscope: :cherry_blossom: <br> Empowering Precision, Embracing Hope


***


![Sara-Zeus Breast App](https://github.com/sara-zeus/Sara-Zeus-Breast-Cancer-Prediction-App/blob/main/images/body_logo.png)




## Objective
This repository hosts the code for a specialized Breast Cancer Prediction App tailored for cytology labs. By harnessing machine learning techniques and utilizing the [Wisconsin Breast Cancer Dataset from Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data), my project aims to develop a predictive tool for identifying breast tumor malignancy. 
 - :reminder_ribbon: [App Link](https://sara-zeus-breast-cancer-prediction-app.streamlit.app)
- Specifically designed for lab technicians, the app interprets cellular morphological features extracted from fine needle aspirate (FNA) samples.
- Derived from digitized images of FNA samples from breast masses, the app's analysis centers on Cellular Morphological Features. It serves as a valuable tool for laboratory technicians, aiding in the prediction of breast cancer based on tissue samples.

## Why MLOps? 
- For the Capstone Project, I decided to take it a step further and explore MLOps because building a machine learning model isn't the end game. MLOps—Machine Learning Operations—is vital for reproducibility and success in a production environment. MLOps ensures scalability, collaboration, and reproducibility throughout the machine learning lifecycle.
- MLOps streamlines the complex machine learning lifecycle, so for this project I decided to use using [ZenML](https://www.zenml.io) with the use pipelines, coordinating tasks from data ingest to model deployment using [MLflow](https://mlflow.org).
- This practice promotes collaboration among various teams, including Data Engineering, Data Science, and ML Engineering, necessitating strict operational standards to synchronize processes.

## Benefits of MLOps include:
- Efficiency: Faster model development, high-quality ML models, and swift deployment.
- Scalability: Management of numerous models, facilitating continuous integration and deployment.
- Risk Reduction: Enables regulatory compliance, drift-check, and faster response to requests, ensuring transparency and policy adherence. 
<p align="center">
  <img src="images/mlops.jpg" alt="MLOps" width="700" height="500">
</p>

# Why MLOps Matters
***
**Building a machine learning model isn't the end game. MLOps—Machine Learning Operations—is vital for reproducibility and success in a production environment. MLOps ensures scalability, collaboration, and reproducibility throughout the machine learning lifecycle. The GIF below explains it well!**

<div style="text-align:center;">
  <img src="https://media.giphy.com/media/DYMk2THiOU0akjDCQ9/giphy.gif" width="300" height="300">
</div>
 
 
## MLOps: Solving Problems and Best Practices

MLOps addresses issues like versioning, monitoring model performance, and efficient feature generation. It ensures consistency, prevents degradation, and streamlines feature creation, allowing data scientists to focus on refining models.

## Skills for MLOps

For successful MLOps, teams need skills in problem articulation, data collection, preparation, model creation, pipeline development, deployment, and real-world monitoring.

## Key Components of MLOps

MLOps comprises various components, including a feature store for efficient feature storage, data versioning for reproducibility, ML metadata for comprehensive logging, and model serving and monitoring for performance checks.

## Model Management and CI/CD in MLOps

Model versioning, registry, serving, monitoring, retraining, and continuous integration/deployment are essential aspects ensuring models perform optimally and adapt to changing data.

## Implementing MLOps

Creating an MLOps system or using pipeline orchestration tools like MLflow, Sacred, and ModelDB streamlines workflows and automates processes.

## Best Practices in MLOps

Collaborative tools, starting simple, quick launches, automated testing, and model deployment are key practices ensuring success in MLOps.

Creating a machine learning model is only 20% of the work! The rest is explained in the image below: ![MLOps](images/ml.png)


## Project Structure


```sql


├── app                      <- Folder For All The Streamlit App Code  
│   ├── app.py                    <- my streamlit app 
│   ├── requirements.txt          <- list of all dependencies 
│
├── assets                   <- Supplementary Resources
│   ├── style.css                 <- styling code
│  
├── data                     <- Data Folder 
│   ├── data.csv                  <- data source
│   
├── images                   <- Images Used in the Project 
│   ├── body_logo.png             <- application logo   
│   ├── heart_logo.png            <- heart logo 
│ 
├── model                    <- Source code
│   ├── main.py                   <- the main 
│   ├── model.pkl                 <- serialized model file
│   ├── scaler.pkl                <- serialized scaler file
│
├── pipelines                <- Pipeline Orchestrators 
│   ├── deployment_pipeline.py    <- automated deployment orchestrator 
│   └── training_pipelines.py     <- model training orchestrator
│   
├── src                      <- Source Code 
│   ├── data_cleaning.py          <- code for data cleaning 
│   ├── evaluation.py             <- code for evaluation 
│   └── model_dev.py              <- code for model development 
│ 
├── steps                    <- Aatomic Aomponents Of ZenML Pipelines 
│   ├── clean_data.py             <- data cleaning step                   
│   ├── config.py                 <- configuration settings  
│   ├── evaluation.py             <- evaluation step         
│   ├── ingest_data.py            <- data ingestion step 
│   └── model_train.py            <- model training step            
│ 
├── __init__.py              <- Package Initializer
├── run_deployment.py        <- Deployment Script
├── run_pipeline.py          <- Pipeline Executor            
└── README.md                <- Project Documentation



```
## 🚀 Lets look at the code 
***

These are my training pipelines: 

- Data Ingestion Pipeline** 📥: Responsible for gathering and importing raw data from various sources into the system or data processing workflow. Involves data collection, extraction, and initial processing tasks.

- Data Preprocessing Pipeline** 🔍: Focuses on cleaning, transforming, and preparing raw data for analysis or model training. Includes data cleaning, normalization, feature engineering, and handling missing values.

- Model Training Pipeline** 🤖: Dedicated to training machine learning or statistical models using prepared data. Involves selecting algorithms, training models, tuning hyperparameters, and validating performance.

- Model Evaluation Pipeline** 📊: Assesses trained models' performance and effectiveness. Involves evaluating against specific metrics, conducting cross-validation, and generating reports or visualizations.

- Deployment Pipeline** 🚀: Handles deploying trained and evaluated models into production or operational environments. Includes model packaging, integration, testing, and making models accessible for usage.


And finally, my deployment pipeline that creates a continuous deployment workflow: 
- Deployment Pipeline: 🚀





## The Streamlit App 
To run the Streamlit App, run the following command: 

```python
streamlit run app/app.py

```

## To Run the Pipelines: 

```python
python run_pipeline.py

```
```python
python run_deployment.py
```
