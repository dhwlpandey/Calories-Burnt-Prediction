from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import pandas as pd
import matplotlib.pyplot as plt
import math

def evaluate_models(model,X_test,y_test):
    pred=model.predict(X_test)
    mae=mean_absolute_error(y_test,pred)
    rmse=math.sqrt(mean_squared_error(y_test,pred))
    r2=r2_score(y_test,pred)
    with open('outputs/metrics.txt','w') as f:
        f.write(f'MAE:{mae}\nRMSE:{rmse}\nR2:{r2}')
    pd.DataFrame({'Actual':y_test,'Predicted':pred}).to_csv('outputs/predictions.csv',index=False)
    plt.scatter(y_test,pred)
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.savefig('outputs/graphs/actual_vs_predicted.png')
