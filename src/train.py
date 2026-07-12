from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score
import joblib

def train_models(df):
    X=df.drop(columns=['Calories'])
    y=df['Calories']
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    models={
        'Linear Regression':LinearRegression(),
        'Decision Tree':DecisionTreeRegressor(random_state=42),
        'Random Forest':RandomForestRegressor(random_state=42),
        'XGBoost':XGBRegressor(random_state=42,verbosity=0)
    }
    best=None
    best_score=-1
    for name,model in models.items():
        model.fit(X_train,y_train)
        score=r2_score(y_test,model.predict(X_test))
        if score>best_score:
            best_score=score
            best=model
    joblib.dump(best,'models/best_model.pkl')
    return best,X_test,y_test
