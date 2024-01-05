# Sara-Zeus Breast Cancer Prediction App :stethoscope: :cherry_blossom: 
![Your Image Caption](https://github.com/sara-zeus/Sara-Zeus-Breast-Cancer-Prediction-App/blob/main/images/body_logo.png)




## Objective
This repository hosts the code for a specialized Breast Cancer Prediction App tailored for cytology labs. By harnessing machine learning techniques and utilizing the [Wisconsin Breast Cancer Dataset from Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data), my project aims to develop a predictive tool for identifying breast tumor malignancy. 
 - :reminder_ribbon: [App Link](https://sara-zeus-breast-cancer-prediction-app.streamlit.app)
- Specifically designed for lab technicians, the app interprets cellular morphological features extracted from fine needle aspirate (FNA) samples.

## Functionality
- **Data Input:** Users have the flexibility to input data manually or connect their devices for a streamlined analysis.
- **Visualization:** The app provides a radar chart illustrating critical cellular characteristics.
- **Prediction:** It offers predictions regarding tumor classification as benign or malignant.

## Features
Derived from digitized images of FNA samples from breast masses, the app's analysis centers on Cellular Morphological Features. It serves as a valuable tool for laboratory technicians, aiding in the prediction of breast cancer based on tissue samples.

## Dataset
The underlying machine learning model is trained on the [Wisconsin Breast Cancer Dataset from Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data), enhancing accuracy and reliability.




---

```python


├── app                      <- Folder For All The Streamlit App Code  
│   ├── app.py                    <- My Streamlit App 
│   ├── requirements.txt          <- List of all Dependencies 
│
├── assets                   <- Supplementary Resources
│   ├── style.css                  <- Styling Code
│  
├── data                     <- Data Folder 
│   ├── data.csv                   <- Data Source 
│   
├── images                   <- Images Used in the Project 
│   ├── body_logo.png              <- Application Logo   
│   ├── heart_logo.png             <- Heart Logo 
│ 
├── model                    <- Source code
│   ├── main.py                    <- The Main 
│   ├── model.pkl                  <- Serialized Model File
│   ├── scaler.pkl                 <- Serialized Scaler File
│
├── pipelines                <- Pipeline Orchestrators 
│   ├── deployment_pipeline.py     <- Automated Deployment Orchestrator 
│   └── training_pipelines.py      <- Model Training Orchestrator
│   
├── src                      <- Source Code 
│   ├── data_cleaning.py          <- code for data cleaning 
│   ├── evaluation.py             <- code for evaluation 
│   └── model_dev.py              <- code for model development 
│ 
├── steps                    <-Aatomic Aomponents Of ZenML Pipelines 
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

