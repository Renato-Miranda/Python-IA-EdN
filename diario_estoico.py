
import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

def salvar_entrada():
    data = entry_data.get()
    fez_bem = text_fez_bem.get("1.0", tk.END).strip()
    poderia_melhor = text_poderia_melhor.get("1.0", tk.END).strip()
    controle_amanha = text_controle_amanha.get("1.0", tk.END).strip()

    if not data or not fez_bem or not poderia_melhor or not controle_amanha:
        messagebox.showwarning("Campos obrigatórios", "Por favor, preencha todos os campos.")
        return

    with open("diario_estoico.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([data, fez_bem, poderia_melhor, controle_amanha])

    messagebox.showinfo("Salvo", "Entrada salva com sucesso!")
    entry_data.delete(0, tk.END)
    text_fez_bem.delete("1.0", tk.END)
    text_poderia_melhor.delete("1.0", tk.END)
    text_controle_amanha.delete("1.0", tk.END)

root = tk.Tk()
root.title("Diário Estoico")

tk.Label(root, text="Data (AAAA-MM-DD):").grid(row=0, column=0, sticky="w")
entry_data = tk.Entry(root, width=20)
entry_data.insert(0, datetime.today().strftime('%Y-%m-%d'))
entry_data.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="O que você fez bem hoje?").grid(row=1, column=0, sticky="w")
text_fez_bem = tk.Text(root, height=4, width=50)
text_fez_bem.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="O que poderia ter feito melhor?").grid(row=2, column=0, sticky="w")
text_poderia_melhor = tk.Text(root, height=4, width=50)
text_poderia_melhor.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="O que está sob seu controle amanhã?").grid(row=3, column=0, sticky="w")
text_controle_amanha = tk.Text(root, height=4, width=50)
text_controle_amanha.grid(row=3, column=1, padx=5, pady=5)

btn_salvar = tk.Button(root, text="Salvar Entrada", command=salvar_entrada)
btn_salvar.grid(row=4, column=1, pady=10)

root.mainloop()
