import joblib
import pandas as pd
def predict(sample):
    model=joblib.load('models/best_model.pkl')
    return model.predict(pd.DataFrame([sample]))[0]
