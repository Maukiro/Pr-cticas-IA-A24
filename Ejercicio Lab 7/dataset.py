import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import radviz

df = pd.read_csv('bezdekIris.data', header=None)

#print(df)
#print(pd.DataFrame.to_numpy(df))

dataset = pd.DataFrame(pd.DataFrame.to_numpy(df), columns=["sepal_length","sepal_width","petal_length","petal_width","species"])

print ("Promedio longitud del sepal", dataset['sepal_length'].sum()/dataset['sepal_length'].size)
print ("Promedio anchura del sepal", dataset['sepal_width'].sum()/dataset['sepal_width'].size)
print ("Promedio longitud del petal", dataset['petal_length'].sum()/dataset['petal_length'].size)
print ("Promedio anchura del petal", dataset['petal_width'].sum()/dataset['petal_width'].size)

print ("Varianza longitud del sepal", dataset['sepal_length'].var())
print ("Varianza anchura del sepal", dataset['sepal_width'].var())
print ("Varianza longitud del petal", dataset['petal_length'].var())
print ("Varianza anchura del petal", dataset['petal_width'].var())

print ("Desviación Estandar longitud del sepal", dataset['sepal_length'].std())
print ("Desviación Estandar anchura del sepal", dataset['sepal_width'].std())
print ("Desviación Estandar longitud del petal", dataset['petal_length'].std())
print ("Desviación Estandar anchura del petal", dataset['petal_width'].std())

a = dataset['sepal_length'].to_numpy()
b = dataset['sepal_width'].to_numpy()
c = dataset['petal_length'].to_numpy()
d = dataset['petal_width'].to_numpy()

print ("--- Mismo Procedimiento con Matrices de Numpy---")

print ("Promedio longitud del sepal", a.sum()/a.size)
print ("Promedio anchura del sepal", b.sum()/b.size)
print ("Promedio longitud del petal", c.sum()/c.size)
print ("Promedio anchura del petal", d.sum()/d.size)

print ("Varianza longitud del sepal", np.var(a))
print ("Varianza anchura del sepal", np.var(b))
print ("Varianza longitud del petal", np.var(c))
print ("Varianza anchura del petal", np.var(d))

print ("Desviación Estandar longitud del sepal", np.std(a))
print ("Desviación Estandar anchura del sepal", np.std(b))
print ("Desviación Estandar longitud del petal", np.std(c))
print ("Desviación Estandar anchura del petal", np.std(d))

plt.figure(figsize=(10, 6))

plt.scatter(dataset['sepal_length'], dataset['sepal_width'], c=pd.factorize(dataset['species'])[0], cmap='viridis')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Sepal Length vs Sepal Width')
plt.colorbar(label='Species')
plt.show()