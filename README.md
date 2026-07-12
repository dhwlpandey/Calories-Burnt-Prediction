# 🔥 Calories Burnt Prediction using Machine Learning

A Machine Learning project that predicts the number of calories burned during physical exercise using physiological and demographic information. The project compares multiple regression algorithms, selects the best-performing model, and provides predictions through a Flask-based web application.

---

## 📌 Project Overview

Estimating calories burned during exercise is useful for fitness tracking and health monitoring. This project uses supervised machine learning algorithms to predict calories burned based on user attributes such as age, gender, weight, height, exercise duration, heart rate, and body temperature.

The project includes:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Multiple regression models
- Model evaluation and comparison
- Flask web application for real-time prediction

---

## 📂 Project Structure

```
Calories-Burnt-Prediction/
│
├── data/
│   └── calories.csv
│
├── models/
│   └── best_model.pkl
│
├── notebooks/
│   └── calories_prediction.ipynb
│
├── outputs/
│   ├── graphs/
│   │   └── actual_vs_predicted.png
│   │
│   ├── metrics.txt
│   └── predictions.csv
│
├── src/
│   ├── evaluate.py
│   ├── predict.py
│   ├── preprocess.py
│   └── train.py
│
├── templates/
│   └── index.html
│
├── UI/
│   ├── a_modern_clean_flat_vector_illustration_for_a_fitness_app._shows_diverse_people/
│   │   └── screen.png
│   │
│   ├── calories_burnt_prediction_app/
│   │   ├── code.html
│   │   └── screen.png
│   │
│   └── kinetic_analytics/
│       └── DESIGN.md
│
├── .gitignore
├── app.py
├── BurnMetrics.html
├── main.py
├── README.md
└── requirements.txt
```

---

## 📊 Dataset

**Dataset:** Calories Burnt Prediction Dataset

The dataset contains **15,000 records** and includes the following features:

| Feature | Description |
|---------|-------------|
| Gender | Male / Female |
| Age | Age of the person |
| Height | Height (cm) |
| Weight | Weight (kg) |
| Duration | Exercise duration (minutes) |
| Heart_Rate | Heart rate during exercise |
| Body_Temp | Body temperature |
| Calories | Target variable |

> **Target Variable:** Calories Burned

---

## ⚙️ Machine Learning Pipeline

1. Data Loading
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Best Model Selection
9. Model Saving
10. Web Deployment using Flask

---

## 🤖 Algorithms Used

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost

The best-performing model is automatically selected based on the highest **R² Score**.

---

## 📈 Evaluation Metrics

The models are evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

Generated evaluation results are stored in the **outputs/** directory.

---

## 🖥️ Web Application

The project includes a Flask web application where users can:

- Enter personal and exercise details
- Predict calories burned instantly
- View model performance
- Compare machine learning algorithms

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/dhwlpandey/Calories-Burnt-Prediction.git
```

Move into the project directory

```bash
cd Calories-Burnt-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the training pipeline

```bash
python main.py
```

Run the Flask application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- XGBoost
- HTML
- Tailwind CSS
- JavaScript

---

## 📷 Project Features

- Interactive prediction dashboard
- Automatic model comparison
- Real-time calorie prediction
- Data visualization
- Model evaluation
- Feature importance analysis
- Clean and responsive UI

---

## 📖 Future Improvements

- User authentication
- Workout history
- BMI calculator
- Exercise recommendations
- REST API deployment
- Cloud deployment (Render / Railway / Azure)

---

## 👨‍💻 Team Members

- Dhawal Pandey
- Dev Bhardwaj
- Vashu Saini
- Akshi

---

## 📄 License

This project was developed for educational and academic purposes.

---

## ⭐ Acknowledgements

- Kaggle for providing the dataset
- Scikit-learn
- Flask
- XGBoost