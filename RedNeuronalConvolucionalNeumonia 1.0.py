
import os  # Libreria que permite manipular archivos y directorios, acceso a variables de entorno, ejecución de comandos del sistema
import cv2  # Libreria que proporciona una amplia gama de funciones y herramientas para procesamiento de imágenes y visión por computadora
import h5py  # Libreria que permite guardar la red neuronal ya entrenada para luego utilizarla
import keras  # Libreria para agilizar la creacion de redes neuronales
import numpy as np  # Libreria que permite trabajar con matrices multidimensionales y realizar cálculos numéricos eficientes
from keras.preprocessing.image import ImageDataGenerator  # Modulo de Keras que permite cargar imágenes desde el disco y aplicarles diversas transformaciones en tiempo real
from keras import models  # Modulo de Keras que permite manipular y crear modelos de redes neuronaler
from keras.models import load_model  # Modulo de Keras que permite importar un modelo ya entrenado para utilizarlo
from keras import layers  # Modulo de Keras que permite crear y manipular las capas de una red neuronal

# Definir las rutas donde estan las imagenes
ruta_entrenamiento='C:/Users/MegaTecnologia/Desktop/PulmonIA/Neumonia_imagenes/entrenamiento'  # Ruta de las imagenes de entrenamiento
ruta_validacion ='C:/Users/MegaTecnologia/Desktop/PulmonIA/Neumonia_imagenes/validacion'  # Ruta de las imagenes de validacion
ruta_test ='C:/Users/MegaTecnologia/Desktop/PulmonIA/Neumonia_imagenes/test'  # Ruta de las imagenes de prueba

# Red neuronal convolucional
cnn = models.Sequential()  # Se crea una red secuencial para luego agregarle las capas

# Capas convolucionales y de pooling
cnn.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(150, 150, 3)))  # Se utilizan 32 filtros de imagen para la capa y un kernel de convolucion de 3x3, se utiliza acivacion ReLU y utiliza imagenes de entrada RGB
cnn.add(layers.MaxPooling2D(pool_size = (2, 2)))  # Esta capa hace down sampling a la imagen en una ventana de tamaño 2x2
cnn.add(layers.Conv2D(32, (3, 3), activation="relu"))  # Se utilizan 32 filtros de imagen para la capa y un kernel de convolucion de 3x3, se utiliza acivacion ReLU y utiliza imagenes de entrada RGB
cnn.add(layers.MaxPooling2D(pool_size = (2, 2)))  # Esta capa hace down sampling a la imagen en una ventana de tamaño 2x2
cnn.add(layers.Conv2D(32, (3, 3), activation="relu"))  # Se utilizan 32 filtros de imagen para la capa y un kernel de convolucion de 3x3, se utiliza acivacion ReLU y utiliza imagenes de entrada RGB
cnn.add(layers.MaxPooling2D(pool_size = (2, 2)))  # Esta capa hace down sampling a la imagen en una ventana de tamaño 2x2
cnn.add(layers.Flatten())  # convierte el mapas de características en un vector unidimensional para que las capas densamente conectadas lo utilicen como datos

# Capas densamente conectadas
cnn.add(layers.Dense(activation = 'relu', units = 128))  # Se añade una capa denda con 128 nodos(neuronas) con activacion ReLU
cnn.add(layers.Dense(activation = 'sigmoid', units = 1))  # Al ser un problema binario se utiliza 1 sola neurona con activacion sigmoid que se encarga de comprimir los valores de salida en un rango de 0 a 1 para realizar una clasificación binaria

# Compilar el modelo neuronal
cnn.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])  # Se utiliza el algoritmo de optimización adam, función de pérdida de entropía cruzada binaria y como metrica para evaluar el rendimiento se usa la precision

# Preprocesamiento de las imagenes
train_datagen = ImageDataGenerator(rescale = 1./255,   #Se generan imagenes imperfectas aplicandoles zoom, rotandolas y distorcionandolas para aumentar el desempeño a la hora de reconocer las radiografias
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
# Normalización de imagenes
test_datagen = ImageDataGenerator(rescale = 1./255)  # Normalización de los valores de píxeles dividiéndolos por 255 para asegura que los valores de entrada estén en un rango adecuado  para ser procesados por el modelo durante la prueba.

# Generación de los conjuntos de entrenamiento, validación y prueba
training_set = train_datagen.flow_from_directory(ruta_entrenamiento,   
                                                 target_size = (150, 150),  #Se homogeniza el tamaño de las imagenes a 150x150 pixeles
                                                 batch_size = 20,  #Se toman lotes de a 20 imagenes
                                                 class_mode = 'binary')  #binary porque este es un problema binario

validation_generator = test_datagen.flow_from_directory(ruta_validacion,  
                                                        target_size =(150, 150),  #Se homogeniza el tamaño de las imagenes a 150x150 pixeles
                                                        batch_size = 20,  #Se toman lotes de a 20 imagenes
                                                        class_mode = 'binary')  #binary porque este es un problema binario

test_set = test_datagen.flow_from_directory(ruta_test,
                                            target_size = (150, 150),  #Se homogeniza el tamaño de las imagenes a 150x150 pixeles
                                            batch_size = 20,  #Se toman lotes de a 20 imagenes
                                            class_mode = 'binary')  #binary porque este es un problema binario

cnn_model = cnn.fit(training_set,
                    steps_per_epoch=100,  # La red se entrena en 100 pasos por epoca
                    epochs=30,  # en un total de 30 epocas
                    validation_data=validation_generator,
                    validation_steps=50)  # Se toman 50 lotes de datos del generador de validación para evaluar el modelo en cada época.
 #Se espera 97% de exactitud aprox
                 
ruta_archivo = 'C:/Users/MegaTecnologia/Desktop/PulmonIA' + '/PulmonIA.h5'
cnn.save(ruta_archivo) # Se guarda la red neuronal ya entrenada en un archivo .h5 para luego ser utilazada

# Predicción sobre una imagen de prueba(cambiar por la radiografia que ingrese el usuario) 

#img_ori = cv2.imread('/content/Neumonia_Dataset/test/NORMAL/IM-0011-0001-0002.jpeg')
img_ori = cv2.imread('C:/Users/MegaTecnologia/Desktop/PulmonIA/Neumonia_imagenes/entrenamiento/NORMAL/NORMAL2-IM-0414-0001.jpeg')  #se tiene que modificar con boton 

img_ori = cv2.cvtColor(img_ori, cv2.COLOR_BGR2RGB)
img = cv2.resize(img_ori, (150, 150), interpolation=cv2.INTER_CUBIC)
imagen_a_probar = np.reshape(img,(1,150, 150, 3))
predictions = cnn.predict(imagen_a_probar)
if(predictions == 0):
  print('El paciente TIENE neumonia')
else:
  print('El paciente NO TIENE neumonia')
