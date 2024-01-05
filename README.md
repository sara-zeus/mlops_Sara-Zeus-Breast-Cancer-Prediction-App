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

## Installation

1. Clone the repository.
2. Install the necessary dependencies using `pip install -r requirements.txt`.

---

- app
  ├── app.py
  └── requirements.txt

- assets
  └── style.css

- data
  └── data.csv

- images
  ├── body_logo.png
  └── heart_logo.png

- mlops_examples
  ├── Data_Ingestion_Pipeline.py
  ├── Data_Preprocessing_Pipeline.py
  ├── Model_Evaluation_Pipeline.py
  ├── Model_Training_Pipeline.py
  ├── tempCodeRunnerFile.py
  └── trained_model.pkl

- model
  ├── main.py
  ├── model.pkl
  └── scaler.pkl

- pipelines
  ├── __pycache__
  ├── deployment_pipeline.py
  └── training_pipelines.py

- src
  ├── __pycache__
  │   ├── data_cleaning.cpython-38.pyc
  │   ├── evaluation.cpython-38.pyc
  │   └── model_dev.cpython-38.pyc
  ├── data_cleaning.py
  ├── evaluation.py
  ├── model_dev.py

- steps
  ├── __pycache__
  ├── clean_data.py
  ├── config.py
  ├── evaluation.py
  ├── ingest_data.py
  ├── model_train.py
  ├── README.md
  ├── __init__.py
  ├── run_deployment.py
  └── run_pipeline.py



