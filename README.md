![image](https://github.com/user-attachments/assets/8d2b3543-98ce-4935-9dac-d8184457bbbd)# 💳 Credit Card Fraud Detection

This project aims to develop a Machine Learning model that detects fraudulent credit card transactions using real-world data. It is submitted as part of the GrowthLink Data Science Internship Assignment.

## 📌 Objective

To build a classification model that accurately detects fraudulent transactions from a highly imbalanced dataset, with a focus on minimizing false negatives and maximizing recall.

## 📁 Dataset

- Source: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- The dataset contains **284,807** transactions, with only **492** frauds.
- Features are anonymized using PCA, with the exception of `Time` and `Amount`.

## ⚙️ Tech Stack & Tools

- Python
- Pandas, NumPy
- Scikit-Learn
- Matplotlib, Seaborn
- Jupyter Notebook (or VS Code)

## 🧠 ML Approach

1. **Data Preprocessing**:
   - Removed duplicates and handled outliers.
   - Scaled `Amount` using `StandardScaler`.
   - Addressed class imbalance using **SMOTE (Synthetic Minority Oversampling Technique)**.

2. **Modeling**:
   - Trained multiple models (Logistic Regression, Random Forest, etc.).
   - Chose the best model based on **Recall**, **F1 Score**, and **ROC AUC**.

3. **Evaluation Metrics**:
   - Accuracy isn't enough due to imbalance. So:
     - Precision
     - Recall
     - F1-Score
     - Confusion Matrix
     - ROC-AUC Curve

##  Results

Metric	 |Class 0 (Legit) |	Class 1 (Fraud) |	Macro Avg |	Weighted Avg
Precision|   1.00	        |       1.00	    |      1.00 |  1.00
Recall	 |   1.00	        |       1.00	    |      1.00	|  1.00
F1-Score |   1.00	        |       1.00	    |      1.00	|  1.00
Accuracy |    -	          |        -	      |       -   |  100%
Support	 |  56,750	      |     56,976	    |   113,726	| 113,726

> High **recall** ensures that most fraudulent transactions are correctly detected.

## 🖥️ How to Run This Project

1. **Clone the Repository**

"git clone https://github.com/ShaikJasmin11/credit-card-fraud-detection.git"
"cd credit-card-fraud-detection"

2. **Install Dependencies**

"pip install -r requirements.txt"

3. **Run the Jupyter Notebook**

"jupyter notebook"

Open the .ipynb file and run all cells.

# Folder Structure

credit-card-fraud-detection
 ┣ data
    ┣ creditcard.csv
 ┣ notebooks
    ┣ fraud_detection.ipynb
 ┣ requirements.txt
 ┣ README.md
 ┗ plots_and_outputs
     ┗ predicted label.png
     ┗ ROC curve.png

# Future Improvements

Use deep learning (ANNs or Autoencoders).

Add transaction location & merchant behavior.

Real-time fraud detection pipeline.

# Author
Shaik Jasmin
GitHub: @ShaikJasmin11
