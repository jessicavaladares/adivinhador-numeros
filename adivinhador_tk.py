import tkinter as tk
from tkinter import ttk
import random

def verificar_chute():
    try:
        chute = int(entrada.get())
        if chute < 1 or chute > 100:
            resultado["text"] = "Digite um número entre 1 e 100!"
            return # Sai da função para não continuar comparando
        if chute > numero_secreto:
            resultado["text"] = "Seu chute é MAIOR!"
        elif chute < numero_secreto:
            resultado["text"] = "Seu chute é MENOR!"
        else:
            resultado["text"] = f"ACERTOU! O número era {numero_secreto}"
            botao_verificar["state"] = tk.DISABLED
            entrada["state"] = tk.DISABLED
    except ValueError:
        resultado["text"] = "Digite um número válido!"

def reiniciar_jogo():
    global numero_secreto
    numero_secreto = random.randint(1, 100)
    resultado["text"] = ""
    entrada.delete(0, tk.END)
    entrada["state"] = tk.NORMAL
    botao_verificar["state"] = tk.NORMAL
    entrada.focus()

numero_secreto = random.randint(1, 100)

janela = tk.Tk()
janela.title("Adivinhe o Número")
janela.configure(bg="#191970")
janela.resizable(False, False) # Impede redimensionamento da janela

estilo = ttk.Style()
estilo.configure("TLabel", font=("Arial", 14), background="#6A5ACD", foreground="#DCDCDC")
estilo.configure("TButton", font=("Arial", 10), background="#111111", foreground="Black", padding=(10, 5))
estilo.configure("TEntry", font=("Arial", 10), width=10)

instrucao = ttk.Label(janela, text="Adivinhe um número\nentre 1 e 100:")
instrucao.grid(row=0, column=0, columnspan=2, pady=(10, 5))

entrada = ttk.Entry(janela)
entrada.grid(row=1, column=0, columnspan=2, pady=5)
entrada.bind("<Return>", lambda event=None: verificar_chute())
entrada.focus() # Coloca o cursor automaticamente no campo de entrada

botao_verificar = ttk.Button(janela, text="Verificar", command=verificar_chute)
botao_verificar.grid(row=2, column=0, columnspan=2, pady=10)

resultado = ttk.Label(janela, text="")
resultado.grid(row=3, column=0, columnspan=2, pady=(0, 10))

botao_reiniciar = ttk.Button(janela, text="Reiniciar", command=reiniciar_jogo)
botao_reiniciar.grid(row=4, column=0, columnspan=2, pady=(0, 10))


janela.mainloop()