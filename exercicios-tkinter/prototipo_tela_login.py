import tkinter as tk

def clique():
    texto = ("Seja bem vindo de volta!")
    print (texto)
    
janela = tk.Tk()

janela.title("Minha primeira tela em Tkinter")

janela.geometry("400x300")

label_nome = tk.Label(janela, text="Nome de Usuário")
label_nome.grid(row=3, column=1)

nome = tk.Entry(janela)
nome.grid(row=3,column=2)

label_senha = tk.Label(janela, text="Senha")
label_senha.grid(row=4, column=1)

senha = tk.Entry(janela, show='*')
senha.grid(row=4, column=2)


botao = tk.Button(janela, text="Login", command=clique)
botao.grid(row=5, column=2, columnspan=2)

janela.mainloop()
