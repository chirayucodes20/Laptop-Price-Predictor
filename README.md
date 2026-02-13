<div align="center">

  <h1>💻 Laptop Price Predictor</h1>
  
  <p>
    An end-to-end Machine Learning web application that predicts the price of laptops based on their specifications. 
    Built with <b>Python</b>, <b>Scikit-Learn</b>, and deployed using <b>Streamlit</b>.
  </p>

  <p>
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python" />
    </a>
    <a href="https://streamlit.io/">
      <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B" alt="Streamlit" />
    </a>
    <a href="https://scikit-learn.org/">
      <img src="https://img.shields.io/badge/Sklearn-ML-orange" alt="Sklearn" />
    </a>
    <img src="https://img.shields.io/badge/Accuracy-81%25-success" alt="Accuracy" />
    <img src="https://img.shields.io/badge/Status-Active-green" alt="Status" />
  </p>
  
  <h4>
    <a href="#-demo">View Demo</a>
    <span> | </span>
    <a href="#-installation">Installation</a>
    <span> | </span>
    <a href="#-technologies-used">Tech Stack</a>
  </h4>
</div>

<br />

## 📋 Table of Contents

- [Overview](#-overview)
- [Project Demo](#-demo)
- [Key Features](#-key-features)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Future Scope](#-future-scope)
- [Author](#-author)

---

## 🧐 Overview

Buying a laptop can be confusing due to the vast number of specifications and price variations. This project aims to solve this problem by providing a fair price estimate for a laptop based on its configuration. 

The model is trained on a dataset of **1,300+ laptops** and uses the **Random Forest / Linear Regression** algorithm to predict prices with high accuracy. The web interface allows users to select brand, RAM, storage, CPU, and other features to get an instant price prediction.

---

## 🎥 Demo

> *Place a screenshot of your Streamlit App here. It makes the repo look 10x better!*
> *Example: `![App Screenshot](screenshot.png)`*

*(You can add a GIF here showing the user selecting options and getting a price)*

---

## ✨ Key Features

- **🎯 High Accuracy:** Achieved an R2 Score of **0.81** using optimized regression models.
- **⚡ Real-time Prediction:** Get instant price estimates as you tweak specifications.
- **🎨 Interactive UI:** Clean and responsive interface built with Streamlit.
- **🧹 Data Cleaning:** Handled messy data (removing 'GB', 'kg', processing CPU/GPU names).
- **🔄 Robust Pipeline:** Implemented Sklearn Pipelines for seamless data preprocessing (OneHotEncoding) and prediction.

---

## 🛠 Technologies Used

| Category | Technologies |
| :--- | :--- |
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) |
| **Frontend** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) |
| **Machine Learning** | ![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) |
| **Deployment** | ![Streamlit Cloud](https://img.shields.io/badge/Streamlit_Cloud-FF4B4B?style=flat&logo=streamlit&logoColor=white) |

---

## 🚀 Installation

Follow these steps to run the project locally on your machine.

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Laptop-Price-Predictor.git](https://github.com/YOUR_USERNAME/Laptop-Price-Predictor.git)
   cd Laptop-Price-Predictor
Create a Virtual Environment (Optional but Recommended)

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies

Bash
pip install -r requirements.txt
Run the App

Bash
streamlit run app.py
📂 Project Structure
Bash
Laptop-Price-Predictor/
├── .git/
├── __pycache__/
├── .gitignore
├── app.py               # Main Streamlit Application
├── laptop_data.csv      # Raw Dataset
├── model.pkl            # Trained Model File
├── df.pkl               # Processed DataFrame
├── Laptop_Price_Prediction.ipynb  # Jupyter Notebook (Analysis & Training)
├── requirements.txt     # List of dependencies
└── README.md            # Project Documentation
