import cv2
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt

rnc = load_model('C:/Users/MegaTecnologia/Desktop/PulmonIA/PulmonIA.h5')

img_ori = cv2.imread('C:/Users/MegaTecnologia/Desktop/PulmonIA/Neumonia_imagenes/entrenamiento/NEUMONIA/person438_bacteria_1893.jpeg')  #se tiene que modificar con boton 

img_ori = cv2.cvtColor(img_ori, cv2.COLOR_BGR2RGB)
img = cv2.resize(img_ori, (150, 150), interpolation=cv2.INTER_CUBIC)
imagen_a_probar = np.reshape(img,(1,150, 150, 3))
resultado = rnc.predict(imagen_a_probar)
if(resultado == 0):
  print('El paciente TIENE neumonia')
else:
  print('El paciente NO TIENE neumonia')
plt.imshow(img)
plt.show()