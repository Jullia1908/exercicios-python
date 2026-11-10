import tkinter as tk

def confirmar():
    opcoes_selecionadas = []

    if var1.get():
        opcoes_selecionadas.append("Receber Novidades")
    if var2.get():
        opcoes_selecionadas.append("Aceitar Termos")
    if var3.get():
        opcoes_selecionadas.append("Ativar Notificações")

    texto_resultado = ", ".join(opcoes_selecionadas)
    if not texto_resultado:
        texto_resultado = "Nenhuma opção selecionada"

    label_resultado.config(text=texto_resultado)

janela = tk.Tk()
janela.title("Selecione as opções")

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

chk1 = tk.Checkbutton(janela, text="Receber Novidades", variable=var1)
chk2 = tk.Checkbutton(janela, text="Aceitar Termos", variable=var2)
chk3 = tk.Checkbutton(janela, text="Ativar Notificações", variable=var3)

chk1.pack()
chk2.pack()
chk3.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

botao_confirmar = tk.Button(janela, text="Confirmar", command=confirmar)
botao_confirmar.pack()

janela.mainloop()
