from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

#interfaz gráfica. V0.3

"""
FALTA AGREGAR:
-funcionalidad de los botones -> Funcionalidad de analizar img
-Ajustar cuadro de img
"""

# Cargar el modelo de la red neuronal convolucional pre-entrenada
model = tf.keras.models.load_model("PulmonIA.h5")

def analizar_imagen():
    imagen = filedialog.askopenfilename()
    image = Image.open(imagen).resize((150, 150))
    
    # Preprocesamiento de la imagen
    imagen_array = np.array(image)
    imagen_array = imagen_array / 255.0
    imagen_array = np.expand_dims(imagen_array, axis=0)
    
    # Realizar la predicción con el modelo
    prediccion = model.predict(imagen_array)
    
    # Obtener el resultado de la predicción
    if prediccion[0][0] > 0.5:
        resultado = "El paciente podría tener neumonía"
    else:
        resultado = "El paciente no tiene neumonía"
    
    messagebox.showinfo("Resultado", resultado)
    
    
root = Tk()

root.title('PulmonIA')
root.configure(bg= "deep sky blue")


#CENTRALIZADO DE VENTANA
# Obtiene el ancho y la altura de la pantalla
ancho_pantalla = root.winfo_screenwidth()
altura_pantalla = root.winfo_screenheight()
#Ajusta el ancho y alto de la ventana
ancho_ventana = 800
altura_ventana = 550
# Calcula las coordenadas x e y para centrar la ventana
x = (ancho_pantalla - ancho_ventana) // 2
y = (altura_pantalla - altura_ventana) // 2
root.geometry(f"{ancho_ventana}x{altura_ventana}+{x}+{y}")

Label(root, text="RADIOGRAFÍA DE TÓRAX", pady=10, bg="deep sky blue", font=("Ebrima", 12, "bold")).pack(pady=5)

mostrar_image = Label(root, bg="deep sky blue")
mostrar_image.pack()

#150 x 150 imagenes que recibe la red 

# Cuadro blanco para mostrar la imagen
#cuadro_blanco = Label(root, bg="white", width=30, height=18)
#cuadro_blanco.pack()

# Función para cargar y analizar la imagen seleccionada
def agregar_imagen():
   imagen = filedialog.askopenfilename()
   image = Image.open(imagen).resize((250, 300))
   image_tk = ImageTk.PhotoImage(image)
   mostrar_image.configure(image=image_tk)
   mostrar_image.image = image_tk
   #cuadro_blanco.destroy()
   btn_agregar_imagen.destroy()  # Eliminar el botón después de utilizarlo
  
   
# Función para salir de la aplicación
def salir():
    root.destroy()   
    
    
#botones 
btn_agregar_imagen = Button(root, text="Agregar imagen", command=agregar_imagen, width=17)
btn_agregar_imagen.configure(font=("Ebrima", 11, "bold"))
btn_agregar_imagen.pack(pady=150) #Margen

analizar_button = Button(root, text="Analizar imagen", command=analizar_imagen, width=15, state=DISABLED)
analizar_button.configure(font=("Ebrima", 11, "bold"))
analizar_button.pack(pady=10)

btn_salir = Button(root, text="Salir", command=salir, width=10)
btn_salir.configure(font=("Ebrima", 11, "bold"))
btn_salir.pack(side="bottom", anchor="se", pady=5, padx=20) #Margen 

root.mainloop()