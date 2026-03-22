# 🧠 Topic Classification Project (SRIP)

## 📌 Overview

This project focuses on building a **text classification model from scratch** to predict the **TOPIC** of a given text (**DATA**).
The dataset contains **10 million rows (~4GB)**, making it a large-scale machine learning problem.

---

## 🚀 Features

* Efficient handling of large dataset using **batch processing (PyArrow)**
* Text preprocessing and cleaning
* Feature extraction using **TF-IDF**
* Multiple model experiments:

  * Logistic Regression
  * Naive Bayes
  * SVM
* Final optimized model with best performance

---

## 📂 Project Structure

```
project/
│── src/
│   ├── train.py
│   ├── inference.py
│   ├── model.py
│   └── utils.py
│── experiments/
│── final_models/
│   └── final_model.pkl
│── report.pdf
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone <your-repo-link>
cd project
```

### 2️⃣ Create virtual environment (recommended)

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## 🏋️ Training the Model

```
cd src
python train.py
```

👉 The model will be saved in:

```
final_models/final_model.pkl
```

---

## 🔮 Inference (Prediction)

```
python inference.py
```

Example:

```
Input: "AI is transforming the world"
Output: Technology
```

---

## 🧠 Approach

### 🔹 Data Processing

* Batch loading using PyArrow (100K rows at a time)
* Text cleaning (lowercase, remove special characters)

### 🔹 Feature Engineering

* TF-IDF Vectorization
* N-grams (unigrams + bigrams)

### 🔹 Model Selection

* Compared Logistic Regression, Naive Bayes, SVM
* Selected **Logistic Regression** for best performance

---

## 📊 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score

---

## 🧪 Experiments

All experiments, logs, and configurations are stored in the `experiments/` folder.

---

## ⚠️ Constraints

* No pretrained models used
* Model built from scratch
* Efficient processing for large dataset

---

## 💡 Future Improvements

* Use deep learning models (from scratch)
* Better feature engineering
* Hyperparameter tuning

---

## 👨‍💻 Author

Your Name JAY THAKAR

---

## ⭐ Note

This project is part of the **SRIP Task - Topic Classification** and demonstrates efficient handling of large-scale NLP problems.
