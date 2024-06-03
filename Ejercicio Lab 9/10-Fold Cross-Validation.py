import pandas as pd
from sklearn.model_selection import StratifiedKFold
import numpy as np

# Cargar datos desde un archivo CSV
data = pd.read_csv(r'C:\Users\Mauricio\Documents\7 SEMESTRE\INTELIGENCIA ARTIFICIAL\Ejercicio Lab 9\diabetes.csv')
# Imprimir los nombres de las columnas para verificar
print(data.columns)
# Separar características y etiquetas utilizando los nombres exactos de las columnas
X = data[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
          'BMI', 'DiabetesPedigreeFunction', 'Age']].values
y = data['Outcome'].values

# Configurar StratifiedKFold con 10 folds
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

# Lista para almacenar los índices de cada fold
fold_indices = list(skf.split(X, y))

# Verificar que las proporciones de las clases son similares en cada fold
for i, (train_index, test_index) in enumerate(fold_indices):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    unique_train, counts_train = np.unique(y_train, return_counts=True)
    unique_test, counts_test = np.unique(y_test, return_counts=True)
    
    print(f"Fold {i+1}")
    print("Proporciones en el conjunto de entrenamiento:", counts_train / len(y_train))
    print("Proporciones en el conjunto de prueba:", counts_test / len(y_test))
    print()

# Crear DataFrames para cada fold y guardarlos en archivos CSV
for fold, (train_index, test_index) in enumerate(fold_indices):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    train_df = pd.DataFrame(X_train, columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
                                              'BMI', 'DiabetesPedigreeFunction', 'Age'])
    train_df['Wine'] = y_train

    test_df = pd.DataFrame(X_test, columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
                                            'BMI', 'DiabetesPedigreeFunction', 'Age'])
    test_df['Wine'] = y_test

    train_df.to_csv(f'train_data_fold_{fold+1}.csv', index=False)
    test_df.to_csv(f'test_data_fold_{fold+1}.csv', index=False)

print("Conjuntos de entrenamiento y prueba para cada fold guardados en archivos CSV.")