# FastAPI Heart Disease Prediction API

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker)

A FastAPI web service that predicts the likelihood of heart disease from patient health measurements. The API loads a trained scikit-learn `RandomForestClassifier` model from `model/heart_disease_model.joblib` and exposes simple endpoints for health checks, model information, and predictions.

Live app: [https://fastapicode-hxus.onrender.com](https://fastapicode-hxus.onrender.com)

## Features

- FastAPI application with automatic Swagger/OpenAPI documentation
- Heart disease prediction using a trained scikit-learn model
- Pydantic request and response validation
- Dockerfile for containerized deployment
- Included dataset and model training script

## Project Structure

```text
FastApiCode/
|-- App/
|   |-- __init__.py
|   |-- main.py              # FastAPI app and API routes
|   `-- schemas.py           # Pydantic request/response models
|-- model/
|   |-- Model_run.py         # Model training script
|   `-- heart_disease_model.joblib
|-- heart.csv                # Heart disease dataset
|-- Requirements.txt         # Python dependencies
|-- Dockerfile               # Docker image configuration
`-- README.md
```

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/health` | Returns API health status |
| `GET` | `/info` | Returns model type and required feature names |
| `POST` | `/predict` | Predicts heart disease risk from input features |

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/iqbal-mih/FastApiCode.git
cd FastApiCode
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r Requirements.txt
```

### 4. Run the API locally

```bash
uvicorn App.main:app --reload
```

The API will be available at:

- App root: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Example Prediction Request

Send a `POST` request to `/predict`:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 63,
    "sex": 1,
    "cp": 3,
    "trestbps": 145,
    "chol": 233,
    "fbs": 1,
    "restecg": 2,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 2.3,
    "slope": 0,
    "ca": 0,
    "thal": 1
  }'
```

Example response:

```json
{
  "prediction": 1,
  "probability": 0.85
}
```

`prediction` values:

- `1`: heart disease detected
- `0`: no heart disease detected

## Input Fields

| Field | Type | Description |
| --- | --- | --- |
| `age` | integer | Age in years |
| `sex` | integer | `1` = male, `0` = female |
| `cp` | integer | Chest pain type, from `0` to `3` |
| `trestbps` | integer | Resting blood pressure in mm Hg |
| `chol` | integer | Serum cholesterol in mg/dl |
| `fbs` | integer | Fasting blood sugar over 120 mg/dl, `1` = true, `0` = false |
| `restecg` | integer | Resting electrocardiographic results, from `0` to `2` |
| `thalach` | integer | Maximum heart rate achieved |
| `exang` | integer | Exercise-induced angina, `1` = yes, `0` = no |
| `oldpeak` | float | ST depression induced by exercise relative to rest |
| `slope` | integer | Slope of the peak exercise ST segment, from `0` to `2` |
| `ca` | integer | Number of major vessels colored by fluoroscopy, from `0` to `4` |
| `thal` | integer | Thalassemia value, from `0` to `3` |

## Run with Docker

Build the image:

```bash
docker build -t fastapicode .
```

Run the container:

```bash
docker run -p 8000:8000 fastapicode
```

Then open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Model Training

The saved model is included at `model/heart_disease_model.joblib`. The training script is available at `model/Model_run.py` and uses the dataset in `heart.csv`.

To retrain the model, update the dataset path in `model/Model_run.py` if needed, then run:

```bash
python model/Model_run.py
```

## Notes

- This project is for educational/demo purposes and should not be used as a replacement for professional medical advice.
- The API returns a machine learning prediction, not a clinical diagnosis.

## Author

Mohammad Iqbal Hossain

- GitHub: [iqbal-mih](https://github.com/iqbal-mih)
