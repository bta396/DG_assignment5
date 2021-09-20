import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def regression_test():
    X=pd.read_excel('Linear_X.xlsx')
    y=pd.read_excel('Linear_Y.xlsx')

    X=X.values
    y=y.values

    model=LinearRegression()

    model.fit(X,y)

    X_test = np.array(2)
    X_test = X_test.reshape((1,-1))

    return model.predict(X_test)


