import tkinter as tk
from tkinter import messagebox

# Definir variáveis globais para os campos de cadastro de produtos e a área de exibição
entry_quantidade = None
entry_nome_produto = None
entry_preco = None
text_produtos_cadastrados = None

def fazer_login():
    # Obter valores dos campos de entrada
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    # Verificar as credenciais (substitua esta lógica pela sua autenticação real)
    if usuario == "usuario" and senha == "senha":
        messagebox.showinfo("Login", "Login bem-sucedido!")
        exibir_menu_principal()
    else:
        messagebox.showerror("Login", "Credenciais inválidas. Tente novamente.")

def cadastrar_produto():
    # Obter valores dos campos de cadastro de produtos
    quantidade = entry_quantidade.get()
    nome_produto = entry_nome_produto.get()
    preco = entry_preco.get()

    # Adicionar produto à área de exibição
    produto_info = f"Quantidade: {quantidade}, Nome: {nome_produto}, Preço: {preco}\n"
    text_produtos_cadastrados.config(state=tk.NORMAL)  # Tornar o Text widget editável
    text_produtos_cadastrados.insert(tk.END, produto_info)
    text_produtos_cadastrados.config(state=tk.DISABLED)  # Tornar o Text widget não editável

    # Limpar campos de cadastro de produtos
    entry_quantidade.delete(0, tk.END)
    entry_nome_produto.delete(0, tk.END)
    entry_preco.delete(0, tk.END)

def exibir_menu_principal():
    # Destruir os widgets de login
    label_usuario.destroy()
    entry_usuario.destroy()
    label_senha.destroy()
    entry_senha.destroy()
    botao_login.destroy()

    # Criar novos widgets para o menu principal
    label_menu = tk.Label(janela, text="Menu Principal")
    label_menu.pack()

    # Campos de cadastro de produtos
    global entry_quantidade, entry_nome_produto, entry_preco

    label_quantidade = tk.Label(janela, text="Quantidade:")
    label_quantidade.pack()

    entry_quantidade = tk.Entry(janela)
    entry_quantidade.pack()

    label_nome_produto = tk.Label(janela, text="Nome do Produto:")
    label_nome_produto.pack()

    entry_nome_produto = tk.Entry(janela)
    entry_nome_produto.pack()

    label_preco = tk.Label(janela, text="Preço:")
    label_preco.pack()

    entry_preco = tk.Entry(janela)
    entry_preco.pack()

    # Botão para cadastrar produto
    botao_cadastrar_produto = tk.Button(janela, text="Cadastrar Produto", command=cadastrar_produto)
    botao_cadastrar_produto.pack()

    # Área de exibição para produtos cadastrados
    global text_produtos_cadastrados
    label_produtos_cadastrados = tk.Label(janela, text="Produtos Cadastrados")
    label_produtos_cadastrados.pack()

    text_produtos_cadastrados = tk.Text(janela, height=10, width=40, state=tk.DISABLED)
    text_produtos_cadastrados.pack()

# Criar a janela principal
janela = tk.Tk()
janela.title("Sistema de Login")

# Desativar redimensionamento da janela
janela.resizable(False, False)

# Criar rótulos e campos de entrada para login
label_usuario = tk.Label(janela, text="Usuário:")
label_usuario.pack()

entry_usuario = tk.Entry(janela)
entry_usuario.pack()

label_senha = tk.Label(janela, text="Senha:")
label_senha.pack()

entry_senha = tk.Entry(janela, show="*")
entry_senha.pack()

# Botão de login
botao_login = tk.Button(janela, text="Login", command=fazer_login)
botao_login.pack()

# Iniciar o loop principal da janela
janela.mainloop()
