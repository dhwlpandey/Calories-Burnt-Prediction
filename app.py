import os
import io
import base64
import math
import json

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template, request, jsonify
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

try:
    from xgboost import XGBRegressor
    HAS_XGB = True
except ImportError:
    HAS_XGB = False

app = Flask(__name__)

model_store = {}   
metrics_store = {} 
best_model_name = None
feature_columns = ['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']
df_global = None   

def load_and_preprocess(path='data/calories.csv'):
    df = pd.read_csv(path)
    df['Gender'] = df['Gender'].map({'male': 0, 'female': 1, 'Male': 0, 'Female': 1})
    df = df.fillna(df.mean(numeric_only=True))
    if 'User_ID' in df.columns:
        df = df.drop(columns=['User_ID'])
    return df

def fig_to_b64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', dpi=120)
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return encoded

def train_all():
    global model_store, metrics_store, best_model_name, df_global
    df_global = load_and_preprocess()
    X = df_global[feature_columns]
    y = df_global['Calories']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    candidates = {
        'Linear Regression': LinearRegression(),
        'Decision Tree':     DecisionTreeRegressor(random_state=42),
        'Random Forest':     RandomForestRegressor(n_estimators=100, random_state=42),
    }
    if HAS_XGB:
        candidates['XGBoost'] = XGBRegressor(random_state=42, verbosity=0)

    best_r2 = -1
    for name, mdl in candidates.items():
        mdl.fit(X_train, y_train)
        preds = mdl.predict(X_test)
        mae  = mean_absolute_error(y_test, preds)
        rmse = math.sqrt(mean_squared_error(y_test, preds))
        r2   = r2_score(y_test, preds)
        model_store[name]   = mdl
        metrics_store[name] = {'mae': round(mae, 4), 'rmse': round(rmse, 4), 'r2': round(r2, 4),
                                'X_test': X_test, 'y_test': y_test, 'preds': preds}
        if r2 > best_r2:
            best_r2 = r2
            best_model_name = name

    os.makedirs('models', exist_ok=True)
    joblib.dump(model_store[best_model_name], 'models/best_model.pkl')
    print(f"[OK] Training done. Best model: {best_model_name} (R2={best_r2:.4f})")

def make_scatter_chart(model_name):
    info = metrics_store[model_name]
    fig, ax = plt.subplots(figsize=(5, 4), facecolor='#0f172a')
    ax.set_facecolor('#1e293b')
    ax.scatter(info['y_test'], info['preds'], alpha=0.55, s=18, c='#38bdf8', edgecolors='none')
    mn = min(info['y_test'].min(), info['preds'].min())
    mx = max(info['y_test'].max(), info['preds'].max())
    ax.plot([mn, mx], [mn, mx], 'r--', lw=1.5, label='Perfect fit')
    ax.set_xlabel('Actual Calories', color='#94a3b8', fontsize=9)
    ax.set_ylabel('Predicted Calories', color='#94a3b8', fontsize=9)
    ax.set_title('Actual vs Predicted', color='#e2e8f0', fontsize=10, pad=8)
    ax.tick_params(colors='#64748b', labelsize=8)
    for spine in ax.spines.values():
        spine.set_edgecolor('#334155')
    ax.legend(fontsize=8, facecolor='#1e293b', labelcolor='#94a3b8')
    return fig_to_b64(fig)

def make_r2_bar_chart():
    names  = list(metrics_store.keys())
    r2vals = [metrics_store[n]['r2'] for n in names]
    colors = ['#38bdf8' if n != best_model_name else '#34d399' for n in names]
    fig, ax = plt.subplots(figsize=(5, 4), facecolor='#0f172a')
    ax.set_facecolor('#1e293b')
    bars = ax.barh(names, r2vals, color=colors, height=0.55)
    ax.set_xlim(0, 1.05)
    ax.set_xlabel('R² Score', color='#94a3b8', fontsize=9)
    ax.set_title('Model Comparison (R²)', color='#e2e8f0', fontsize=10, pad=8)
    ax.tick_params(colors='#64748b', labelsize=8)
    for spine in ax.spines.values():
        spine.set_edgecolor('#334155')
    for bar, v in zip(bars, r2vals):
        ax.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height() / 2,
                f'{v:.4f}', va='center', color='#e2e8f0', fontsize=8)
    return fig_to_b64(fig)

def make_dist_chart():
    fig, ax = plt.subplots(figsize=(5, 4), facecolor='#0f172a')
    ax.set_facecolor('#1e293b')
    if df_global is not None:
        ax.hist(df_global['Calories'], bins=40, color='#818cf8', edgecolor='#0f172a', linewidth=0.4)
    ax.set_xlabel('Calories Burnt', color='#94a3b8', fontsize=9)
    ax.set_ylabel('Count', color='#94a3b8', fontsize=9)
    ax.set_title('Calories Distribution', color='#e2e8f0', fontsize=10, pad=8)
    ax.tick_params(colors='#64748b', labelsize=8)
    for spine in ax.spines.values():
        spine.set_edgecolor('#334155')
    return fig_to_b64(fig)

def make_feature_importance_chart():
    mdl = model_store.get(best_model_name)
    fig, ax = plt.subplots(figsize=(5, 4), facecolor='#0f172a')
    ax.set_facecolor('#1e293b')
    if hasattr(mdl, 'feature_importances_'):
        imp = mdl.feature_importances_
        idx = np.argsort(imp)
        ax.barh([feature_columns[i] for i in idx], imp[idx],
                color='#f472b6', height=0.55)
        ax.set_xlabel('Importance', color='#94a3b8', fontsize=9)
        ax.set_title('Feature Importance', color='#e2e8f0', fontsize=10, pad=8)
    else:
        ax.text(0.5, 0.5, 'Not available\nfor this model',
                ha='center', va='center', color='#94a3b8', fontsize=11,
                transform=ax.transAxes)
        ax.set_title('Feature Importance', color='#e2e8f0', fontsize=10, pad=8)
    ax.tick_params(colors='#64748b', labelsize=8)
    for spine in ax.spines.values():
        spine.set_edgecolor('#334155')
    return fig_to_b64(fig)

@app.route('/')
def index():
    summary = {name: {'r2': m['r2'], 'mae': m['mae'], 'rmse': m['rmse']}
               for name, m in metrics_store.items()}
    return render_template('index.html',
                           best_model=best_model_name,
                           summary=summary,
                           dataset_rows=len(df_global) if df_global is not None else 0,
                           feature_columns=feature_columns,
                           hero_image_url='https://www.gstatic.com/labs-code/stitch/stitch-placeholder-300x300.svg')

@app.route('/api/charts')
def api_charts():
    model_name = request.args.get('model', best_model_name)
    if model_name not in metrics_store:
        return jsonify({'error': 'unknown model'}), 400
    return jsonify({
        'scatter':    make_scatter_chart(model_name),
        'r2_bar':     make_r2_bar_chart(),
        'dist':       make_dist_chart(),
        'feat_imp':   make_feature_importance_chart(),
    })

@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json()
    try:
        sample = {
            'Gender':     int(data['gender']),
            'Age':        float(data['age']),
            'Height':     float(data['height']),
            'Weight':     float(data['weight']),
            'Duration':   float(data['duration']),
            'Heart_Rate': float(data['heart_rate']),
            'Body_Temp':  float(data['body_temp']),
        }
        mdl = model_store[best_model_name]
        df_input = pd.DataFrame([sample])[feature_columns]
        prediction = float(mdl.predict(df_input)[0])
        return jsonify({'calories': round(prediction, 2), 'model': best_model_name})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/metrics')
def api_metrics():
    return jsonify({name: {'r2': m['r2'], 'mae': m['mae'], 'rmse': m['rmse']}
                    for name, m in metrics_store.items()})

if __name__ == '__main__':
    train_all()
    app.run(debug=False, host='0.0.0.0', port=5000)
