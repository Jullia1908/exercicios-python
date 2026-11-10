import tkinter as tk

def calcular_imc():
    peso = float(peso_entry.get())
    altura = float(altura_entry.get())

    imc = peso / (altura ** 2)

    print (imc)
    
janela = tk.Tk()

janela.title("Minha primeira tela em Tkinter")

janela.geometry("400x300")

label_texto = tk.Label(janela, text='Calcule seu IMC')
label_texto.place(x=100, y=15)

label_peso = tk.Label(janela, text="Peso")
label_peso.place(x=50, y=50)
peso_entry = tk.Entry(janela)
peso_entry.place(x=100, y=50)

label_altura = tk.Label(janela, text="Altura")
label_altura.place(x=50, y=100)
altura_entry = tk.Entry(janela)
altura_entry.place(x=100, y=100)


botao = tk.Button(janela, text="Calcular", command=calcular_imc)
botao.place(x=150, y=150)

janela.mainloop()
