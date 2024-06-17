import numpy as np
import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn import datasets

def nivelCorrectitud(test_labels,answers):
    correctos = 0
    for i in range(len(answers)):
        if(answers[i] == test_labels[i]):
            correctos+=1
    
    correctos/=len(answers)
    return correctos

datos = datasets.load_wine().data
clases = datasets.load_wine().target

escalador = MinMaxScaler()
datos = escalador.fit_transform(datos)
clasificador = KNeighborsClassifier(n_neighbors=1)

X_train,X_test,y_train,y_test = train_test_split(datos,clases,test_size=0.30,random_state = 123)
clasificador.fit(X_train,y_train)

salidas = clasificador.predict(X_test)

matriz = confusion_matrix(y_test,salidas)

print(nivelCorrectitud(salidas,y_test))

print(matriz)