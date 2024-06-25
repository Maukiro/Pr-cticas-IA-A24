#importación de librerías
#cada una de las librerías tiene incorporado la función a importar de cada libraría
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn import linear_model
import numpy as np

def precision(reales, calculados):
    correctos = 0
    for i in range(len(reales)):
        if(reales[i]==calculados[i]):
            correctos+=1
    return correctos/len(reales)

#Se carga el dataset
dataset = datasets.load_iris()
#impresión de todo el dataset
print(dataset)
print('\n informacion del dataset: \n')
print(dataset.keys() )

#se guarda el dato de los datasets y las etiquetas de salida
x = dataset.data
y = dataset.target

#se dividen los casos a pruebas y entrenamiento con un ratio de 0.2 para pruebas / totales
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
#se imprime la entrada de cada elemento de entrenamiento
print('\n cosas del x_train \n')
print(x_train)
print('\n fin de las cosas del xtrain\n')

#Se imprimen las etiquetas de los elementos de entrenamiento
print('cosas del y_train \n')
print(y_train)
print('\n fin de las cosas del ytrain\n')

#se imprimen los valores de cada elemento de prueba
print('cosas del x_test \n')
print(x_test)
print('\n fin de las cosas del xtest\n')

#se imprimen las etiquetas de cada elemento de prueba
print('cosas del y_test \n')
print(y_test)
print('\n fin de las cosas del ytest\n')

escala = StandardScaler()
#se hace el escalamiento de los casos de entrenamiento
#x_train = escala.fit_transform(x_train)
#se hace el escalamiento de los casos de prueba
#x_test = escala.transform(x_test)

#impresion de los nuevos valores de entrenamiento
print('cosas del x_train despues de usar el scaler \n')
print(x_train)
print('\n fin de las cosas del xtrain\n')

print('cosas del x_test despues de usar el scaler \n')
print(x_test)
print('\n fin de las cosas del xtest\n')

# parte de naive bayes 
algoritmo=linear_model.BayesianRidge()
algoritmo.fit(x_train, y_train)
y_pred= algoritmo.predict(x_test)


#Analisis de las matrices 
print(y_test)
realy = []
for elemento in y_pred:
    realy.append(int(round(elemento,0)))
print(realy)
y_pred = np.array(realy)
matriz =confusion_matrix(y_test,y_pred)
print('matriz de confusion: ')
print(matriz)

#calculo del modelo

precision =precision(y_test, y_pred)

print('precision del modelo: \n')
print(precision)