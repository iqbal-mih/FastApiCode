# 🩺 FastAPI Heart Disease Prediction API

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-brightgreen?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)
![Render](https://img.shields.io/badge/Deployed%20on-Render-purple?logo=render)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A lightweight **FastAPI-based web service** for predicting heart disease using a trained machine learning model.  
This API processes patient health parameters and returns the likelihood of heart disease.

🔗 **Live Demo:** [https://fastapicode-hxus.onrender.com](https://fastapicode-hxus.onrender.com)

---

## 🚀 Features
- ⚡ RESTful API built with **FastAPI**
- 🤖 Integrated **Machine Learning model** (scikit-learn)
- 🐳 Fully **Dockerized** for easy deployment
- ✅ Input validation via **Pydantic Schemas**
- ☁️ Hosted on **Render**

---

## 📂 Project Structure
FastApiCode/
│
├── App/
│ ├── init.py
│ ├── main.py # FastAPI app entry point
│ ├── schemas.py # Pydantic models for input validation
│
├── model/
│ ├── Model_run.py # ML model training/loading script
│ ├── heart_disease_model.joblib # Trained model file
│
├── heart.csv # Dataset used for training
├── Requirements.txt # Dependencies
├── Dockerfile # Container configuration
└── README.md

yaml
Copy code

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/iqbal-mih/FastApiCode.git
cd FastApiCode
2️⃣ Install dependencies
bash
Copy code
pip install -r Requirements.txt
3️⃣ Run the API locally
bash
Copy code
uvicorn App.main:app --reload
Open your browser at:
👉 http://127.0.0.1:8000

4️⃣ Access Swagger UI
📘 http://127.0.0.1:8000/docs

🧠 Example API Request
POST /predict

json
Copy code
{
  "age": 52,
  "sex": 1,
  "cp": 0,
  "trestbps": 130,
  "chol": 230,
  "fbs": 0,
  "restecg": 1,
  "thalach": 170,
  "exang": 0,
  "oldpeak": 1.2,
  "slope": 2,
  "ca": 0,
  "thal": 2
}
Response:

json
Copy code
{
  "prediction": "Heart Disease Detected"
}
🐳 Run with Docker
bash
Copy code
docker build -t fastapicode .
docker run -d -p 8000:8000 fastapicode
📊 Dataset
The ML model was trained on the Heart Disease Dataset,
which contains key cardiovascular attributes to predict whether a patient
is likely to have heart disease or not.

💡 Future Improvements
🧩 Add automatic model retraining pipeline

🔐 Implement authentication for API access

🚀 Set up CI/CD workflow for seamless deployment

📈 Improve model accuracy with more data

👨‍💻 Author
Mohammad Iqbal Hossain
📫 GitHub Profile

⭐ If you find this project helpful, please give it a star on GitHub!

yaml
Copy code

---

Would you like me to also add a **short "Example usage in Python"** section (showing how to call your API from a script using `requests`)?  
That makes your README more developer-friendly.
