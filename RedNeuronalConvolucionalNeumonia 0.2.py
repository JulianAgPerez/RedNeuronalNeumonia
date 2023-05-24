
import os
import cv2
import keras
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras import models
from keras import layers
import matplotlib.pyplot as plt

# Definir las rutas donde estan las imagenes
ruta_entrenamiento= 'ruta de la carpeta entrenamiento'
ruta_validacion = 'ruta de la carpeta validacion'
ruta_test = 'ruta de la carpeta test'

# Red neuronal convolucional
cnn = models.Sequential()

# Capas convolucionales y de pooling
cnn.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(150, 150, 3)))
cnn.add(layers.MaxPooling2D(pool_size = (2, 2)))
cnn.add(layers.Conv2D(32, (3, 3), activation="relu"))
cnn.add(layers.MaxPooling2D(pool_size = (2, 2)))
cnn.add(layers.Conv2D(32, (3, 3), activation="relu"))
cnn.add(layers.MaxPooling2D(pool_size = (2, 2)))   
cnn.add(layers.Flatten())

# Capas densamente conectadas
cnn.add(layers.Dense(activation = 'relu', units = 128))
cnn.add(layers.Dense(activation = 'sigmoid', units = 1)) # Al ser un problema binario se utiliza 1 sola neurona

# Compilar el modelo neuronal
cnn.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Preprocesamiento de las imagenes
train_datagen = ImageDataGenerator(rescale = 1./255,   #Se generan imagenes imperfectas para aumentar el desempeño a la hora de reconocer las radiografias
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
# Normalización de imagenes
test_datagen = ImageDataGenerator(rescale = 1./255)

# Generación de los conjuntos de entrenamiento, validación y prueba
training_set = train_datagen.flow_from_directory(ruta_entrenamiento,   
                                                 target_size = (150, 150),  #Se homogeniza el tamaño de las imagenes a 150x150 pixeles
                                                 batch_size = 20,  #Se toman lotes de a 20 imagenes
                                                 class_mode = 'binary')  #binary porque este es un problema binario

validation_generator = test_datagen.flow_from_directory(ruta_validacion,
                                                        target_size =(150, 150),
                                                        batch_size = 20,
                                                        class_mode = 'binary')

test_set = test_datagen.flow_from_directory(ruta_test,
                                            target_size = (150, 150),
                                            batch_size = 20,
                                            class_mode = 'binary')

cnn_model = cnn.fit(training_set,
                    steps_per_epoch=100,   #Se espera 97% de exactitud aprox
                    epochs=30,
                    validation_data=validation_generator,
                    validation_steps=50)

# Predicción sobre una imagen de prueba(cambiar por la radiografia que ingrese el usuario) 

#img_ori = cv2.imread('/content/Neumonia_Dataset/test/NORMAL/IM-0011-0001-0002.jpeg')
img_ori = cv2.imread('/content/Neumonia_Dataset/test/PNEUMONIA/person119_bacteria_566.jpeg')  #se tiene que modificar con boton 

img_ori = cv2.cvtColor(img_ori, cv2.COLOR_BGR2RGB)
img = cv2.resize(img_ori, (150, 150), interpolation=cv2.INTER_CUBIC)
imagen_a_probar = np.reshape(img,(1,150, 150, 3))
predictions = cnn.predict(imagen_a_probar)
if(predictions == 0):
  print('Persona sin neumonia')
else:
  print('Persona con neumonia')
plt.imshow(img)
plt.show()