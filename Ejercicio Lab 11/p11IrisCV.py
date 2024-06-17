import numpy as np
import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn import datasets
from sklearn.model_selection import cross_val_predict

def nivelCorrectitud(test_labels,answers):
    correctos = 0
    for i in range(len(answers)):
        if(answers[i] == test_labels[i]):
            correctos+=1
    
    correctos/=len(answers)
    return correctos

datos = datasets.load_iris().data
clases = datasets.load_iris().target

escalador = MinMaxScaler()
datos = escalador.fit_transform(datos)

clasificador = KNeighborsClassifier(n_neighbors = 1)
clasificador.fit(datos,clases)

salidas = cross_validate(clasificador,datos,clases,cv = 10,scoring = 'accuracy')
x = salidas['test_score'].mean()
print(x)
y_pred = cross_val_predict(clasificador,datos,clases,cv=10)
matriz = confusion_matrix(clases,y_pred)
print(matriz)