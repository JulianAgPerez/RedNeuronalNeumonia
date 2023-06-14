"# RedNeuronalNeumonia" 
"# RedNeuronalNeumonia" 
Nombre: PulmonIA

# Link de descarga del proyecto (también está en GitHub)
https://drive.google.com/file/d/1duNEs6qza1fJpH3atPhz0QBF--dFXdkN/view

# Descarga de PIL (Python Imaging Library) en Ubuntu para el uso de la interfaz gráfica:

1- Abrir la terminal

2- Si PIL no está instalado, ejecute los siguientes comandos:        
sudo apt update  
sudo apt install python3-pip

3- Y por último:     
pip3 install pillow

# Descarga/instalacion de librerias externas
-Para Ubuntu; Colocar los siguientes comandos en la consola/terminal

pip install tkinter
pip install Pillow
pip install keras
pip install numpy

# Instrucciones para abrir y usar el programa
1- Desde la consola, acceder a la carpeta del proyecto (o abrir la terminal en la misma)

2- Una vez ubicado dentro de la carpeta del proyecto, colocar el siguiente comando

python3 PulmonIA1.1.4.py

3- Agregar la radiografía a evaluar tras clickear en el boton "Agregar imagen"

4- Clickear en el boton de "Analizar imagen" para obtener el resultado del analisis

# 24/05/23
Al día de la fecha se cuenta con el código de la red neuronal convolucional, los datos de entrenamiento y una primera muestra de la interfaz gráfica que dispone de la posibilidad de subir una imagen desde el almacenamiento de la computadora para que luego sea analizada por la red.
Nos encontramos con el problema de que la máquina virtual de Linux no nos toma la gpu, lo que representa un problema mayor al realizar el entrenamiento de la red y su posterior conexión con la interfaz gráfica de usuario. Se procede con cautela. 
Como información extra, nos gustaría agregar que se decidió el nombre de nuestra aplicación: PulmonIA.
Es esencial aprovechar los beneficios de la tecnología para mejorar la atención médica y el diagnóstico de enfermedades. En este contexto, nuestro objetivo sigue siendo el mismo: desarrollar y aplicar una red neuronal convolucional para la detección de la neumonía. 

# 03/06/23
Es de nuestro agrado informar que hemos logrado realizar el entrenamiento de la red y su conexión con la interfaz gráfica de usuario.
A dia de hoy tenemos el proyecto funcionando sujeto a pequeñas modificaciones de la GUI por lo que su funcionamiento está garantizado, hemos llegado a la estimacion de que tiene un 96% de efectividad de detección, por lo que sin dudas puede ser un muy buen complemento para un profesional de la salud.

# 13/6/23
Buen dia/tarde/noche, hemos tenido un pequeño contratiempo al intentar crear un ejecutable, debido a que no encontramos una solucion optamos por correr el programa desde la consola, anunciando así que finalmente hemos logrado terminar de manera oficial el proyecto.