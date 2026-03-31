from pydoc import text
import tkinter as tk
from tkinter import messagebox

cadastrar = 0
listar = 0
atualizar = 0
excluir = 0
registros = []

# Recebe os dados dos campos de entrada
def listar():
    tipo = entrada_tipo.get()
    descricao = entrada_descricao.get()
    beneficiario = entrada_beneficiario.get()
    data = entrada_data.get()
    valor = entrada_valor.get()
    status = entrada_status.get()
    texto_lista.delete(1.0, tk.END)  # Limpa a área de texto antes de listar
    registros.append(tipo + "-" + descricao + "-" + beneficiario + "-" + data + "-" + valor + "-" + status)

    for r in registros:
        texto_lista.insert(tk.END, r + "\n")


# FRONTEND 
# =============================
# 6. Controle de janela principal
# =============================
janela = tk.Tk()
janela.title("Controle de Pagamento")

# Campos de entrada 
ttk.Label(janela, text="Tipo (a pagar / a receber):").grid(row=0 ,column=0)
entrada_tipo = tk.Entry(janela)
entrada_tipo.grid(row=0, column=1)

tk.Label(janela, text="Descrição:").grid(row=1, column=0)
entrada_descricao = tk.Entry(janela)
entrada_descricao.grid(row=1, column=1)

tk.Label(janela, text="Beneficiario:").grid(row=2, column=0)
entrada_beneficiario = tk.Entry(janela)
entrada_beneficiario.grid(row=2, column=1)

tk.Label(janela, text="Data (AAAA-MM-DD):").grid(row=3, column=0)
entrada_data = tk.Entry(janela)
entrada_data.grid(row=3, column=1)

tk.Label(janela, text="Valor:").grid(row=4, column=0)
entrada_valor = tk.Entry(janela)
entrada_valor.grid(row=4, column=1)

tk.Label(janela, text="Status (pendente/pago):").grid(row=5, column=0)
entrada_status = tk.Entry(janela)
entrada_status.grid(row=5, column=1)

tk.Label(janela, text="ID (Para atualizar / Excluir):").grid(row=6, column=0)
entrada_id = tk.Entry(janela)
entrada_id.grid(row=6, column=1)

# Botões de ação
tk.Button(janela, text="Cadastrar", command=cadastrar).grid(row=7, column=0)
tk.Button(janela, text="Listar", command=listar).grid(row=7, column=1)
tk.Button(janela, text="Atualizar Status", command=atualizar).grid(row=7, column=2)
tk.Button(janela, text="Excluir", command=excluir).grid(row=8, column=1)

# Área de Texto para mostrar lista
area_lista = tk.Text(janela, height=10, width=50)
texto_lista.grid(row=9, column=0, columnspan=2)


#==============================
# 7. Iniar o Programa #
#==============================

janela.mainloop()    

# ============================================================
# 8. Fechar conexão ao sair
# ============================================================
conexao.close()