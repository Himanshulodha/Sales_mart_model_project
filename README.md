# 📊 Sales Mart Prediction

A Flask-based web application that predicts grocery item sales using machine learning. This tool helps store managers and supply chain teams make data-driven decisions about stock and inventory levels by forecasting future sales with high accuracy.

## 🔍 Project Overview
This project focuses on forecasting individual grocery item sales using a machine learning model trained on historical data. The application is deployed using Flask and provides a user-friendly interface for real-time predictions.

## 🧠 Features
📈 Sales Forecasting: Predicts future sales quantity for specific grocery items.
🧮 85%+ Accuracy: Model performance validated with strong predictive accuracy.
📊 Data Visualization: Includes insights through graphs (Matplotlib & Seaborn).
🧰 Web Integration: Flask-powered frontend for easy user interaction.

## 🛠️ Tech Stack
Languages: Python
Frameworks: Flask
Libraries: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn
IDE: VS Code

## 🚀 How to Run
### Clone the repository
git clone https://github.com/Himanshulodha/Sales_mart_model_project.git
cd Sales_mart_model_project

### Install dependencies
pip install -r requirements.txt

### Run the Flask app
python app.py

### Open in browser
Navigate to http://127.0.0.1:5000 to use the web application.

## 📁 Project Structure
Sales_mart_model_project/
│
├── app.py                # Flask application
├── model.pkl             # Trained ML model
├── templates/
│   └── index.html        # HTML frontend
├── static/
│   └── style.css         # Styling (optional)
├── data/
│   └── sales_data.csv    # Dataset used
└── README.md             # Project documentation
