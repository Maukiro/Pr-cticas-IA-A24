import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np


# Cargar datos desde un archivo CSV
data = pd.read_csv(r'C:\Users\mauri\Documents\7MO SEMESTRE\INTELIGENCIA ARTIFICIAL\Practica 9\iris.csv')


# Columnas 'sepal.length', 'sepal.width', 'petal.length', 'petal.width'
# Etiqueta/clase en una columna llamada 'variety'
X = data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
y = data['variety'].values


# Dividir los datos en entrenamiento (70) y prueba (30) de manera estratificada
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)


# Verificar que las proporciones de las clases son similares
unique, counts_train = np.unique(y_train, return_counts=True)
unique, counts_test = np.unique(y_test, return_counts=True)
print("Proporciones en el conjunto de entrenamiento:", counts_train / len(y_train))
print("Proporciones en el conjunto de prueba:", counts_test / len(y_test))


# Crear DataFrames para los conjuntos de entrenamiento y prueba
train_df = pd.DataFrame(X_train, columns=['sepal.length', 'sepal.width', 'petal.length', 'petal.width'])
train_df['variety'] = y_train


test_df = pd.DataFrame(X_test, columns=['sepal.length', 'sepal.width', 'petal.length', 'petal.width'])
test_df['variety'] = y_test


# Guardar los DataFrames en archivos CSV
train_df.to_csv('train_data.csv', index=False)
test_df.to_csv('test_data.csv', index=False)


print("Conjuntos de entrenamiento y prueba guardados en 'train_data.csv' y 'test_data.csv' respectivamente.")
