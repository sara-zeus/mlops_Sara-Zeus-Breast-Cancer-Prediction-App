# Sara-Zeus Breast Cancer Prediction App :stethoscope: :cherry_blossom: 
**Empowering Precision, Embracing Hope** 
![Sara-Zeus Breast App](https://github.com/sara-zeus/Sara-Zeus-Breast-Cancer-Prediction-App/blob/main/images/body_logo.png)




## Objective
This repository hosts the code for a specialized Breast Cancer Prediction App tailored for cytology labs. By harnessing machine learning techniques and utilizing the [Wisconsin Breast Cancer Dataset from Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data), my project aims to develop a predictive tool for identifying breast tumor malignancy. 
 - :reminder_ribbon: [App Link](https://sara-zeus-breast-cancer-prediction-app.streamlit.app)
- Specifically designed for lab technicians, the app interprets cellular morphological features extracted from fine needle aspirate (FNA) samples.
- I decided to take this project a step further and implement MLOps, which stands for Machine Learning Operations. MLOps is a core function of Machine Learning engineering, aimed at streamlining the process of deploying machine learning models to production and subsequently maintaining and monitoring them. It involves collaboration among data scientists, DevOps engineers, and IT professionals. 
![MLOps](images/mlops.jpg)

## Functionality
- **Data Input:** Users have the flexibility to input data manually or connect their devices for a streamlined analysis.
- **Visualization:** The app provides a radar chart illustrating critical cellular characteristics.
- **Prediction:** It offers predictions regarding tumor classification as benign or malignant.

## Features
Derived from digitized images of FNA samples from breast masses, the app's analysis centers on Cellular Morphological Features. It serves as a valuable tool for laboratory technicians, aiding in the prediction of breast cancer based on tissue samples.

## Dataset
The underlying machine learning model is trained on the [Wisconsin Breast Cancer Dataset from Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data), enhancing accuracy and reliability.


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

## The Streamlit App
To run the Streamlit App, run the following command: 

```python
streamlit run app/app.py

```



