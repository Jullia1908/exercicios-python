import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo de Texto")
janela.geometry("400x300")


label_resultado = tk.Label(janela, text="")
label_resultado.pack()

caixa_texto = tk.Text(janela, height=10, width=40, bg="lightyellow", fg="black")
caixa_texto.pack()

def clique():
    texto = caixa_texto.get("1.0", "end")  
    label_resultado.config(text=texto)  

botao = tk.Button(janela, text="Salvar", command=clique)
botao.pack()

janela.mainloop()
