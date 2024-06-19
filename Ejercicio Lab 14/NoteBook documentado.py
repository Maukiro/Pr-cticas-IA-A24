# Importa la biblioteca principal de TensorFlow
import tensorflow as tf

# Importa módulos específicos de Keras dentro de TensorFlow
from tensorflow.keras import datasets, layers, models

# Importa la biblioteca Matplotlib para graficar
import matplotlib.pyplot as plt

# Cargar y preprocesar el conjunto de datos CIFAR-10
# CIFAR-10 es un conjunto de datos de 60,000 imágenes de 10 clases diferentes
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalizar los píxeles de la imagen (de 0 a 255) a un rango de 0 a 1
# Esto es útil para mejorar la convergencia del entrenamiento
train_images, test_images = train_images / 255.0, test_images / 255.0

# Nombres de las clases en CIFAR-10
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# Visualizar las primeras 25 imágenes del conjunto de entrenamiento
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])  # Eliminar marcas en el eje X
    plt.yticks([])  # Eliminar marcas en el eje Y
    plt.grid(False)  # No mostrar cuadrícula
    plt.imshow(train_images[i])  # Mostrar la imagen
    # Los labels de CIFAR-10 son arrays, por lo que se necesita un índice adicional
    plt.xlabel(class_names[train_labels[i][0]])  # Mostrar el nombre de la clase
plt.show()  # Mostrar la figura

# Construir el modelo utilizando la API de Keras
# Un modelo secuencial es apropiado para una pila simple de capas lineales
model = models.Sequential()

# Añadir una capa de convolución 2D con 32 filtros, un tamaño de kernel de 3x3 y ReLU como función de activación
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))

# Añadir una capa de max pooling 2D para reducir la dimensionalidad espacial (reducción de muestreo)
model.add(layers.MaxPooling2D((2, 2)))

# Añadir una segunda capa de convolución 2D con 64 filtros y un tamaño de kernel de 3x3
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Añadir otra capa de max pooling 2D
model.add(layers.MaxPooling2D((2, 2)))

# Añadir una tercera capa de convolución 2D con 64 filtros y un tamaño de kernel de 3x3
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Mostrar la arquitectura del modelo hasta este punto
model.summary()

# Aplanar la salida de las capas anteriores para que puedan ser alimentadas en una capa completamente conectada (densa)
model.add(layers.Flatten())

# Añadir una capa densa con 64 unidades y ReLU como función de activación
model.add(layers.Dense(64, activation='relu'))

# Añadir una capa densa final con 10 unidades (una por clase) sin función de activación (logits)
model.add(layers.Dense(10))

# Mostrar la arquitectura completa del modelo
model.summary()

# Compilar el modelo especificando el optimizador, la función de pérdida y las métricas
# El optimizador Adam es una buena elección general
# SparseCategoricalCrossentropy se usa para clasificación con etiquetas enteras (en lugar de one-hot)
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Entrenar el modelo usando el conjunto de datos de entrenamiento
# Validar el entrenamiento con el conjunto de datos de prueba
history = model.fit(train_images, train_labels, epochs=10,
                    validation_data=(test_images, test_labels))

# Graficar la precisión del entrenamiento y la validación a lo largo de las épocas
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])  # Limitar el rango del eje Y
plt.legend(loc='lower right')
plt.show()  # Mostrar la gráfica

# Evaluar el modelo en el conjunto de datos de prueba
# Esto da una idea del rendimiento del modelo en datos no vistos
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(test_acc)  # Imprimir la precisión en el conjunto de prueba