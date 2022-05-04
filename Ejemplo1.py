import xlrd
import pandas as pd
import numpy  as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error,r2_score
data=pd.read_excel('BI_Alumnos07.xlsx')
datax=data[['Altura']]
x=np.array(datax)
y=data['Peso'].values
regL=linear_model.LinearRegression()
regL.fit(x,y)
y_pred=regL.predict(x)
print('Coeficiente R:',regL.coef_)
print('Error cuadrado medio %.2f '% mean_squared_error(y,y_pred))
print('Puntaje de varianza: %.2f '% r2_score(y,y_pred))
predPeso=regL.predict([[180]])
print('Prediccion de Peso: ',int(predPeso))