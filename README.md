
# 🚀 Network Security Threat Detection – End-to-End MLOps Project

An automated **Network Intrusion Detection System (NIDS)** built using **MLOps**, **ELT pipelines**, **ML model training**, **CI/CD**, and **cloud deployment**.
This project detects malicious network activities using machine learning, ensuring a fully scalable and production-ready architecture.

---

## 📌 **Project Overview**

This project implements a **complete end-to-end MLOps pipeline** for identifying network security threats from raw network logs. It follows a real-world architecture starting from **data ingestion → ELT → transformation → model training → evaluation → deployment → monitoring**.

The project is production-focused and automates the entire lifecycle of the ML model using:

* **Airflow** (workflow orchestration)
* **DVC** (data versioning)
* **MLflow** (experiment tracking & model registry)
* **Docker** (container deployment)
* **AWS S3 ** (cloud storage)

It is inspired by the **MLOps Bootcamp** project by *Krish Naik*.

---

## 🎯 **Features**

### 🔹 **1. Automated ELT Pipeline**

* Extracts raw network traffic logs (CSV/JSON/Parquet)
* Loads data into a cloud storage bucket
* Transforms using Pandas/PySpark
* Validates schema & quality

### 🔹 **2. Modular ML Pipeline**

Includes multiple reusable components:

* Data Ingestion
* Data Validation
* Data Transformation
* Model Training
* Model Evaluation
* Model Deployment

Each component uses **config entities**, **artifact entities**, and **custom exception handling**.

### 🔹 **3. MLOps Tools Integration**

* **MLflow** → tracks metrics, hyperparameters, model versions
* **DVC** → versions datasets & pipelines
* **Airflow** → schedules daily/weekly ETL & model retraining
* **Docker** → deploy the inference API as a container
* **GitHub Actions** → CI/CD pipeline

### 🔹 **4. Network Threat Detection Model**

ML algorithms used:

* Random Forest
* XGBoost
* LightGBM
* Logistic Regression

Metrics used:

* Accuracy
* Precision / Recall
* F1-score
* ROC-AUC

### 🔹 **5. Deployment**

The model is deployed using:

* **Docker image**
* Optional cloud deployment (AWS EC2 / Elastic Beanstalk / GCP VM)

---

## 🏗️ **Project Architecture**

```
network-security-mlops/
│
├── airflow/                      # Airflow DAGs for pipeline orchestration
├── notebooks/                    # Jupyter notebooks for analysis and experiments
├── networksecurity/              # Core project package
│   ├── components/               # Pipeline components
│   ├── config/                   # Config entities
│   ├── entity/                   # Artifact & config entity classes
│   ├── exception/                # Custom exception handling
│   ├── logger/                   # Central logging system
│   └── pipeline/                 # Training & prediction pipeline
│
├── artifacts/                    # Saved artifacts (data, models, reports)
├── saved_models/                 # Final deployed model
├── main.py                       # Main entry script to start training
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

---

## 🛠️ **Tech Stack**

### **Programming & ML**

* Python
* Scikit-Learn
* Pandas / Numpy
* PySpark (optional)

### **MLOps & DevOps**

* **Airflow**
* **MLflow**
* **DVC**
* **Docker**
* **GitHub Actions**
* **Cloud (AWS)**

### **Deployment**

* Docker Compose

---

## ⚙️ **How It Works (Pipeline Flow)**

### Step 1️⃣ — Data Ingestion

Loads raw network logs from:

* Public datasets (e.g., NSL-KDD, CICIDS2017)

### Step 2️⃣ — Data Validation

* Schema validation
* Missing/outlier detection
* Stats report generation

### Step 3️⃣ — Data Transformation

* Encoding
* Normalization
* Feature engineering
* Train-test split

### Step 4️⃣ — Model Training

Trains multiple ML models → selects best model via evaluation metrics.

### Step 5️⃣ — Model Evaluation

Automatically compares:

* New model
* Previously deployed model

If new model is better → it gets deployed.

### Step 6️⃣ — Model Deployment

Deploys using FastAPI + Docker.

### Step 7️⃣ — Monitoring

Pipeline tracked via:

* MLflow UI
* Airflow DAG monitoring
* Log system

---

## 🧪 **Running the Project**

### **1. Clone the repo**

```bash
git clone https://github.com/yourusername/network-security-mlops.git
cd network-security-mlops
```

### **2. Create virtual environment**

```bash
python -m venv venv
venv/Scripts/activate
```

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

### **4. Run full ML pipeline**

```bash
python main.py
```

### **5. Start Airflow**

```bash
airflow standalone
```

### **6. Start FastAPI server**

```bash
uvicorn app:app --reload
```

---

## 📊 **Model Performance (Example)**

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 98.2% |
| Precision | 97.6% |
| Recall    | 98.9% |
| F1-Score  | 98.2% |

---

## 📦 **Deployment (Optional)**

### **Docker**

```bash
docker build -t networksecurity-api .
docker run -p 8000:8000 networksecurity-api
```

### **Cloud Options**

* AWS EC2
* AWS Elastic Beanstalk
* GCP Compute Engine
* Docker Hub + Kubernetes

---

## 📁 **Dataset**

You can use:

* Custom network logs

---

## 🤝 **Contributing**

Pull requests are welcome.
Follow PEP8 and MLOps best practices.

---

## 📜 **License**

MIT License © 2025

---

If you want, I can also generate:

✅ **Badges for GitHub**
✅ **Flow diagram (ASCII or Mermaid)**
✅ **CI/CD workflow YAML**
✅ **Architecture diagram**

Just tell me!
