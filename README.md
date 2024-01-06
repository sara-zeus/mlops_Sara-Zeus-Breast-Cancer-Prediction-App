# Sara-Zeus Breast Cancer Prediction App :stethoscope: :cherry_blossom: <br> Empowering Precision, Embracing Hope


***


![Sara-Zeus Breast App](https://github.com/sara-zeus/Sara-Zeus-Breast-Cancer-Prediction-App/blob/main/images/body_logo.png)




## Objective
This repository hosts the code for a specialized Breast Cancer Prediction App and MLOps workflows and Deployment Mechanisms tailored for cytology labs. By harnessing machine learning techniques and utilizing the [Wisconsin Breast Cancer Dataset from Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data), my project aims to develop a predictive tool for identifying breast tumor malignancy. 
 - :reminder_ribbon: [App Link](https://sara-zeus-breast-cancer-prediction-app.streamlit.app)
- Specifically designed for lab technicians, the app interprets cellular morphological features extracted from fine needle aspirate (FNA) samples.
- Derived from digitized images of FNA samples from breast masses, the app's analysis centers on Cellular Morphological Features. It serves as a valuable tool for laboratory technicians, aiding in the prediction of breast cancer based on tissue samples.

## Why MLOps? 
- For the Capstone Project after creating the App, I decided to take it a step further and explore MLOps because building a machine learning model isn't the end game. MLOps—Machine Learning Operations—is vital for reproducibility and success in a production environment. MLOps ensures scalability, collaboration, and reproducibility throughout the machine learning lifecycle.
- MLOps streamlines the complex machine learning lifecycle, so for this project I decided to use using [ZenML](https://www.zenml.io) with the use pipelines, coordinating tasks from data ingest to model deployment using [MLflow](https://mlflow.org).
- This practice promotes collaboration among various teams, including Data Engineering, Data Science, and ML Engineering, necessitating strict operational standards to synchronize processes.

## Benefits of MLOps include:
- Efficiency: Faster model development, high-quality ML models, and swift deployment.
- Scalability: Management of numerous models, facilitating continuous integration and deployment.
- Risk Reduction: Enables regulatory compliance, drift-check, and faster response to requests, ensuring transparency and policy adherence. 
<p align="center">
  <img src="images/mlops.jpg" alt="MLOps" width="700" height="500">
</p>

## Why MLOps Matters

**Building a machine learning model isn't the end game. MLOps—Machine Learning Operations—is vital for reproducibility and success in a production environment. MLOps ensures scalability, collaboration, and reproducibility throughout the machine learning lifecycle. The GIF below explains it well!**

![Alt Text](https://media.giphy.com/media/DYMk2THiOU0akjDCQ9/giphy.gif)

 
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


***

**Creating a machine learning model is only 20% of the work! The rest is explained in the image below:** ![MLOps](images/ml.png)

***

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
├── model                    <- EDA and ML model 
│   ├── main.py                   <- Source code
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
***
## 🪜 Lets look at the code
***

**My training pipeline:** 

Steps inside the training pipeline:

- 📥 ingest_data: This step will ingest the data and create a DataFrame.
- 🔍 clean_data: This step will clean the data and remove the unwanted columns.
- 🤖 train_model: This step will train the model and save the model using MLflow autologging.
- 📊 evaluation: This step will evaluate the model and save the metrics. 


**And finally, my deployment pipeline that creates a continuous deployment workflow:** 
- 🚀 Deployment Pipeline 

## Challenges I Encountered in MLOps:

- One of the primary challenges I faced revolves around the scarcity of comprehensive resources dedicated to instructing proficient MLOps practices. Given the nascent nature of this field, not all industry professionals possess the requisite skills and knowledge in this domain.

- Additionally, I encountered difficulties in resolving certain bugs within the deployment pipeline, an ongoing area of focus in my current work.



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
