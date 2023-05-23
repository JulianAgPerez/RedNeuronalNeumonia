from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

#Primera interfaz gráfica. 

"""
FALTA AGREGAR:
-configuraciones de  ancho, largo y aparicion de la ventana (completo)
-funcionalidad de los botones -> Funcionalidad Salir (completo)
-Segunda ventana
    -Sus botones
    -Su funcionalidad. 
    -Cuadro donde se pueda arrastrar una imagen/al hacer click deje agregar una imagen
"""

root = Tk()

root.title('PulmonIA')
root.geometry("700x500")
root.configure(bg= "powder blue")

Label(root, text="Radiografía").pack

mostrar_image = Label(root, bg="powder blue")
mostrar_image.pack(pady=20)

#150 x 150 imagenes que recibe la red 
 
# Función para cargar y analizar la imagen seleccionada
def agregar_imagen():
   imagen = filedialog.askopenfilename()
   image = Image.open(imagen).resize((200, 300))
   image_tk = ImageTk.PhotoImage(image)
   mostrar_image.configure(image=image_tk)
   mostrar_image.image = image_tk
   btn_agregar_imagen.destroy()  # Eliminar el botón después de utilizarlo
   
# Función para salir de la aplicación
def salir():
    root.destroy()   
    
#botones 
btn_agregar_imagen = Button(root, text="Agregar imagen", command=agregar_imagen, width=17)
btn_agregar_imagen.configure(font=("Ebrima", 10))
btn_agregar_imagen.pack(pady=20) #Margen

btn_salir = Button(root, text="Salir", command=salir, width=10)
btn_salir.configure(font=("Ebrima", 10))
btn_salir.pack(side="bottom", anchor="se", pady=17, padx=20) #Margen 

root.mainloop()