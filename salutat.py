import tkinter as tk
def saludar():
    frame2.pack()
    etiqueta1["text"]=" ¡ H O L A  M U N D O ! "
    frame3.pack(side='right')
def desaludar():
    etiqueta1["text"]=""
ventana = tk.Tk()
ventana.title("Un Saludo")
""" ventana.geometry("600x200") """
ventana.wm_iconbitmap("handshake.ico")
ventana.configure(bd=10, bg="gray31", padx=50)
frame1=tk.Frame(ventana)
frame1.configure(background="red", bd=20)
frame1.pack()
frame2=tk.Frame(ventana)
boton1=tk.Button(frame1, text="Saludar", height=2, width=20, command=saludar)
boton1.pack()
etiqueta1=tk.Label(frame2)
etiqueta1.config(fg="yellow", font=("Arial", 35, "bold"), bg="gray31", pady=20)
etiqueta1.pack()
frame3=tk.Frame(ventana)
frame3.configure(width=10, height=10)
boton2=tk.Button(frame3, text="X",fg="gray38" , bg="gray25", command=desaludar)
boton2.pack()
ventana.mainloop()
