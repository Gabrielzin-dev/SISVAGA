import tkinter as tk
from tkinter import messagebox
import sqlite3

#========================================
# 1. Conexão com o banco de dados
#========================================
conexao = sqlite3.connect("pagamento.db")
cursos = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS titulos (
    id INTEGER PRIMARY KEY AUTOINCREMENT.
    tipo TEXT,
    descricao TEXT,
    beneficiario TEXT,
    data TEXT,
    valor TEXT,
    status TEXT
    )
    """)

#========================================
# 2. Função para cadstrar título
#========================================
def cadastrar():
    tipo = entrada_tipo.get()
    descricao = entrada_descricao.get()
    beneficiario = entrada_beneficiario.get()
    data = entrada_data.get()
    valor = entrada_valor.get()
    status = entrada_status.get()
    cursor.execute("""
    INSERT INTO titulos(tipo, descricao, beneficiario, data, valor, status)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (tipo, descricao, beneficiario, data, valor, status))
    conexao.comit()
    messagebox.showinfo("Sucesso", "Título cadastro com sucesso!")
  
# ================================================  
    # 3. Função para listar títulos
# ================================================
def listar():
    cursor.execute("SELECT * FROM titulos")
    registros = cursor.fetchall()
    texto_lista.delete("1.0", tk.END)  # Limpa antes de mostrar
    for r in registros:
        texto_lista.insert(tk.END, f"{r}\n")

# ================================================
# 4. Função para atualizar status
# ================================================
def atualizar():
    id_titulo = entrada_id.get()
    novo_status = entrada_status.get()
    cursor.execute("UPDATE titulos SET status = ? WHERE id = ?", (novo_status, id_titulo))
    conexao.commit()
    messagebox.showinfo("Sucesso", "Status atualizado com sucesso!")