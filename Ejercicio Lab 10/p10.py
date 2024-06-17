import numpy as np
from sklearn.model_selection import cross_validate
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def distancia(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def euclidean_classifier(train_data, train_labels, test_point):
    distances = [distancia(train_point, test_point) for train_point in train_data]
    nearest_neighbor_index = np.argmin(distances)
    return train_labels[nearest_neighbor_index]

def nivelCorrectitud(test_labels,answers):
    correctos = 0
    for i in range(len(answers)):
        if(answers[i] == test_labels[i]):
            correctos+=1
    
    correctos/=len(answers)
    return correctos


iris = datasets.load_iris().data
realClassification = datasets.load_iris().target

X_train,X_test,y_train,y_test = train_test_split(iris,realClassification,test_size=0.3,random_state = 123)
print(X_train)
print("X prueba")
print(X_test)
print("Y entreno")
print(y_train)
print("y prueba")
print(y_test)

resultados_test = []
for test_point in X_test:
    resultados_test.append(euclidean_classifier(X_train, y_train, test_point))

resultados_test = np.array(resultados_test)
print(resultados_test)

print(nivelCorrectitud(y_test,resultados_test))
