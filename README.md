# End-to-End-ML-Approach-to-Wine-Quality-Prediction-with-MLflow

## Workflows 

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py  


# How to run?

### STEPS: 

Clone the repository 

```bash
https://github.com/Pritamn11/End-to-End-ML-Approach-to-Wine-Quality-Prediction-with-MLflow
```

#### STEPS 01 - Create a virtual environment after opening the repository

```bash
python -m venv newenv
```

```bash
.\newenv\Scripts\activate
```
 
#### STEPS 01 - Install the requirements

```bash
pip install -r requirements.txt
```

```bash
# Finally run the command
python app.py
```

Now,

```bash
open up you local host and port
```

## MLflow


[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd 
- mlflow ui

## dagshub 
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/pritamnarwade11/End-to-End-ML-Approach-to-Wine-Quality-Prediction-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=pritamnarwade11 \
MLFLOW_TRACKING_PASSWORD=871b76c6a3213893886036cf5681b2454522ec97 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/pritamnarwade11/End-to-End-ML-Approach-to-Wine-Quality-Prediction-with-MLflow.mlflow 

export MLFLOW_TRACKING_USERNAME=pritamnarwade11 

export MLFLOW_TRACKING_PASSWORD=871b76c6a3213893886036cf5681b2454522ec97 

```





