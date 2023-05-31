from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

#interfaz gráfica. V0.5

# Cargar el modelo de la red neuronal convolucional pre-entrenada
model = tf.keras.models.load_model("PulmonIA.h5")

# Variable para almacenar la imagen seleccionada
imagen_seleccionada = None

def analizar_imagen():
    if imagen_seleccionada is None:
        messagebox.showwarning("Advertencia", "Por favor, primero seleccione una imagen.")
        return
    
    # Preprocesamiento de la imagen
    imagen = Image.open(imagen_seleccionada).convert("RGB").resize((150, 150))
    imagen_array = np.array(imagen)
    imagen_array = imagen_array / 255.0
    imagen_array = np.expand_dims(imagen_array, axis=0)
    
    # Realizar la predicción con el modelo
    prediccion = model.predict(imagen_array)
    
    # Obtener el resultado de la predicción
    if prediccion[0][0] < 0.5:
        resultado = "El paciente podría tener neumonía."
    else:
        resultado = "El paciente no tiene neumonía."
    
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

# Función para cargar y analizar la imagen seleccionada
def agregar_imagen():
   global imagen_seleccionada
   imagen_seleccionada = filedialog.askopenfilename()
   image = Image.open(imagen_seleccionada).resize((250, 300))
   image_tk = ImageTk.PhotoImage(image)
   mostrar_image.configure(image=image_tk)
   mostrar_image.image = image_tk
   analizar_button.configure(state=NORMAL)
   btn_agregar_imagen.config(text="Volver a añadir imagen") #Renombra el botón "Agregar imagen"
   
   
# Función para salir de la aplicación
def salir():
    root.destroy()   
    
    
#botones 
btn_agregar_imagen = Button(root, text="Agregar imagen", width=25, command=agregar_imagen)
btn_agregar_imagen.configure(font=("Ebrima", 11, "bold"))
btn_agregar_imagen.pack(pady=15) #Margen

analizar_button = Button(root, text="Analizar imagen", command=analizar_imagen, width=25, state=DISABLED)
analizar_button.configure(font=("Ebrima", 11, "bold"))
analizar_button.pack(pady=10)

btn_salir = Button(root, text="Salir", command=salir, width=10)
btn_salir.configure(font=("Ebrima", 11, "bold"))
btn_salir.pack(side="bottom", anchor="se", pady=5, padx=20) #Margen 

root.mainloop()