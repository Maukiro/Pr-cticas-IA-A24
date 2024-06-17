import numpy as np
import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn import datasets
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

TradSalidas = datasets.load_iris().target_names
Etiquetas = datasets.load_iris().feature_names
iris = datasets.load_iris().data
realClassification = datasets.load_iris().target

escalador = MinMaxScaler()
datos = escalador.fit_transform(iris)
clasificador = KNeighborsClassifier(n_neighbors = 30)
clasificador.fit(iris,realClassification)

salidas = cross_validate(clasificador,datos,realClassification,cv = 10,scoring = 'accuracy')
x = salidas['test_score'].mean()
print(x)