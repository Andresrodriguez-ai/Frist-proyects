import tkinter as tk

def convertir():
    valor = float(entrada_valor.get())
    uo = combo_unidades_origen.get()
    ud = combo_unidades_destino.get()

    if uo == "Euros" and ud == "Dólares":
        resultado = valor * 1.1159513
    elif uo == "Metros" and ud == "Pulgadas":
        resultado = valor * 39.37
    elif uo == "Euros" and ud == "Franco Suizo":
        resultado = valor * 0.95
    else:
        resultado = valor
    
    label_resultado.config(text="Resultado: " + str(resultado))


ventana = tk.Tk()
ventana.title("Conversor")

entrada_valor = tk.Entry(ventana)
entrada_valor.pack()

unidades_origen = ["Metros", "Euros"]
combo_unidades_origen = tk.StringVar(ventana)
combo_unidades_origen.set(unidades_origen[0])

menu_unidades_origen = tk.OptionMenu(ventana, combo_unidades_origen, *unidades_origen)
menu_unidades_origen.pack()

unidades_destino = ["Dólares", "Pulgadas", "Franco Suizo"]
combo_unidades_destino = tk.StringVar(ventana)
combo_unidades_destino.set(unidades_destino[0])

menu_unidades_destino = tk.OptionMenu(ventana, combo_unidades_destino, *unidades_destino)
menu_unidades_destino.pack()


boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.pack()

label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack()

ventana.mainloop()