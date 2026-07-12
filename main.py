from src.preprocess import load_data
from src.train import train_models
from src.evaluate import evaluate_models

df=load_data('data/calories.csv')
best, X_test, y_test= train_models(df)
evaluate_models(best,X_test,y_test)
print('Project completed.')
