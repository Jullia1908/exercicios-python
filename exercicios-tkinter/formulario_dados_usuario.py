import tkinter as tk

def clique():
    texto = ("Nome: {} \nE-mail: {} \nGênero: {}" .format (nome.get(), email.get(), genero.get()))
    label_resultado.config(text=texto)
    
janela = tk.Tk()

janela.title("Minha primeira tela em Tkinter")

janela.geometry("400x300")

label = tk.Label(janela, text="Nome")
label.pack()
nome = tk.Entry(janela)
nome.pack()

label = tk.Label(janela, text="E-mail")
label.pack()
email = tk.Entry(janela)
email.pack()

genero = tk.StringVar()

label_genero = tk.Label(janela, text="Gênero")
label_genero.pack()
feminino = tk.Radiobutton(janela, text="Feminino", variable=genero, value="Feminino")
masculino = tk.Radiobutton(janela, text="Masculino", variable=genero, value="Masculino")

feminino.pack()
masculino.pack()


botao = tk.Button(janela, text="Clique aqui", command=clique)
botao.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()

