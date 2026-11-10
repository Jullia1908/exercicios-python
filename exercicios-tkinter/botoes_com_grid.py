import tkinter as tk

def botao1_clicado():
    label1.config(text="Botão 1 foi clicado!")

def botao2_clicado():
    label2.config(text="Botão 2 foi clicado!")

def botao3_clicado():
    label3.config(text="Botão 3 foi clicado!")


janela = tk.Tk()
janela.title("Exemplo com Grid")


label1 = tk.Label(janela, text="Label 1")
label2 = tk.Label(janela, text="Label 2")
label3 = tk.Label(janela, text="Label 3")


botao1 = tk.Button(janela, text="Botão 1", command=botao1_clicado, bg="blue", fg="white", padx=10, pady=5)
botao2 = tk.Button(janela, text="Botão 2", command=botao2_clicado, bg="green", fg="white", padx=10, pady=5)
botao3 = tk.Button(janela, text="Botão 3", command=botao3_clicado, bg="red", fg="white", padx=10, pady=5)


label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
botao1.grid(row=0, column=1)
botao2.grid(row=1, column=1)
botao3.grid(row=2, column=1)


janela.mainloop()
