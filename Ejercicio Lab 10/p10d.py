import numpy as np
import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

def nivelCorrectitud(test_labels,answers):
    correctos = 0
    for i in range(len(answers)):
        if(answers[i] == test_labels[i]):
            correctos+=1
    
    correctos/=len(answers)
    return correctos


data = pd.read_csv("diabetes.csv",sep = ',')
tuvieron = data[data["Outcome"]==1]
salvados = data[data["Outcome"]==0]
print(len(tuvieron))
print(len(salvados))
#diabetes = data[["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]]
#resultados = data[["Outcome"]]
#diabetes = diabetes.to_numpy()
#resultados = resultados.to_numpy()
#print(diabetes)
#print(resultados)
#X_train,X_test,y_train,y_test = train_test_split(diabetes,resultados,test_size=0.30,random_state = 123)
escalador = MinMaxScaler()
datos = data[["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]]
clases = data[["Outcome"]]
clases = clases.to_numpy()
clases = clases.ravel()
"""
X_train,X_test,y_train,y_test = train_test_split(datos,clases,test_size=0.30,random_state = 123)
print(X_train)
print(X_test)

data = escalador.fit_transform(data)
clasificador = KNeighborsClassifier(n_neighbors = 13)
clasificador.fit(datos,clases)

checando = []
for cosa in X_test:
    print(cosa)
    #actual = escalador.transform([cosa])
"""
escalador = MinMaxScaler()
datos = escalador.fit_transform(datos)
clasificador = KNeighborsClassifier(n_neighbors=5)
print(datos)
print(clases)
X_train,X_test,y_train,y_test = train_test_split(datos,clases,test_size=0.20,random_state = 123)
clasificador.fit(X_train,y_train)

print(X_test)
salidas = clasificador.predict(X_test)
print(y_test)
print(salidas)
print(nivelCorrectitud(salidas,y_test))