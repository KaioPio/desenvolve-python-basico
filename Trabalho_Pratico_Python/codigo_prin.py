import csv

# Gerenciamento de arquivos

def carregar_usuarios(arquivo):
    usuarios = []
    try:
        with open(arquivo, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for linha in reader:
                usuarios.append(linha)
    except FileNotFoundError:
        print("Arquivo de usuários não encentrado.")
    return usuarios

def carregar_produtos(arquivo):
    produtos = []
    try:
        with open(arquivo, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for linha in reader:
                linha['preco'] = float(linha['preco'])
                linha['quantidade'] = int(linha['quantidade'])
    except FileNotFoundError:
        print("Arquivo de produtos não encontrato.")  
    return produtos  

def salvar_usuarios(arquivo, usuarios):
    with open(arquivo, mode='w',newline='', encoding='utf-8') as f:
        campos = ['id', 'nome', 'login', 'senha', 'tipo']
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for u in usuarios:
            writer.writerow(u)

def  salvar_produtos(arquivo, produtos):
    with open(arquivo, mode='w', newline='', encoding='utf-8') as f:
        campos = ['id', 'nome', 'preco', 'quantidade']
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for p in produtos:
            writer.writerow(p)

# Função de login

def login(usuarios):
    print("\n 🔐 Login")
    login = input("Login: ")
    senha = input("Senha: ")
    for usuario in usuarios:
        if usuario['login'] == login and usuario['senha'] == senha:
            print(f"\n ✅Bem Vindo, {usuario['nome']} ({usuario['tipo']})")
            return usuario
    print("❌ Login Inválido")
    return None    

# Crud Usuarios

def criar_usuario(usuarios):
    print("\n👤 Criar novo usuário")
    novo = {
        'id': str(len(usuarios)+1),
        'nome': input("Nome: "),
        'login': input("Login: "),
        'senha': input("Senha: "),
        'tipo': input("Tipo (gerente, funcionario, cliente): ")
    }
    usuarios.append(novo)
    print("✅ Usuário criado com sucesso!")

def listar_usuarios(usuarios):
    print("\n📋 Lista de Usuários:")
    for u in usuarios:
        print(f"{u['id']} - {u['nome']} ({u['tipo']})")

def atualizar_usuario(usuarios):
    listar_usuarios(usuarios)
    id = input("ID do usuário para atualizar: ")
    for u in usuarios:
        if u['id'] == id:
            u['nome'] = input("Novo nome: ") or u['nome']
            u['senha'] = input("Nova senha: ") or u['senha']
            u['tipo'] = input("Novo tipo: ") or u['tipo']
            print("✅ Usuário atualizado!")
            return
    print("❌ Usuário não encontrado.")

def excluir_usuario(usuarios):
    listar_usuarios(usuarios)
    id = input("ID do usuário para excluir: ")
    for u in usuarios:
        if u['id'] == id:
            usuarios.remove(u)
            print("🗑️ Usuário excluído!")
            return
    print("❌ Usuário não encontrado.")

# Crud para produtos

def criar_produto(produtos):
    print("\n➕ Adicionar Produto")
    novo = {
        'id': str(len(produtos)+101),
        'nome': input("Nome: "),
        'preco': float(input("Preço: ")),
        'quantidade': int(input("Quantidade: "))
    }
    produtos.append(novo)
    print("✅ Produto adicionado!")

def listar_produtos(produtos):
    print("\n📦 Lista de Produtos:")
    for p in produtos:
        print(f"{p['id']} - {p['nome']} - R${p['preco']:.2f} - {p['quantidade']} unidades")

def atualizar_produto(produtos):
    listar_produtos(produtos)
    id = input("ID do produto para atualizar: ")
    for p in produtos:
        if p['id'] == id:
            p['nome'] = input("Novo nome: ") or p['nome']
            p['preco'] = float(input("Novo preço: ") or p['preco'])
            p['quantidade'] = int(input("Nova quantidade: ") or p['quantidade'])
            print("✅ Produto atualizado!")
            return
    print("❌ Produto não encontrado.")

def excluir_produto(produtos):
    listar_produtos(produtos)
    id = input("ID do produto para excluir: ")
    for p in produtos:
        if p['id'] == id:
            produtos.remove(p)
            print("🗑️ Produto excluído!")
            return
    print("❌ Produto não encontrado.")

def buscar_produto(produtos):
    nome = input("🔍 Nome do produto: ").lower()
    encontrados = [p for p in produtos if nome in p['nome'].lower()]
    for p in encontrados:
        print(f"{p['id']} - {p['nome']} - R${p['preco']:.2f} - {p['quantidade']} unidades")

def ordenar_por_nome(produtos):
    ordenados = sorted(produtos, key=lambda x: x['nome'].lower())
    for p in ordenados:
        print(f"{p['nome']} - R${p['preco']:.2f}")

def ordenar_por_preco(produtos):
    ordenados = sorted(produtos, key=lambda x: x['preco'])
    for p in ordenados:
        print(f"{p['nome']} - R${p['preco']:.2f}")

# Menu de usuarios


def menu(usuario, usuarios, produtos, arq_usuarios, arq_produtos):
    tipo = usuario['tipo']
    while True:
        print("\n📋 Menu")
        if tipo == 'gerente':
            print("1. CRUD Usuários")
            print("2. CRUD Produtos")
            print("3. Buscar Produto")
            print("4. Ordenar Produtos")
            print("0. Sair")
        elif tipo == 'funcionario':
            print("1. Listar Produtos")
            print("2. Atualizar Produto")
            print("3. Buscar Produto")
            print("0. Sair")
        elif tipo == 'cliente':
            print("1. Listar Produtos")
            print("2. Buscar Produto")
            print("0. Sair")
        else:
            print("Tipo de usuário desconhecido.")
            break

        opcao = input("Escolha: ")

        if opcao == '0':
            salvar_usuarios(arq_usuarios, usuarios)
            salvar_produtos(arq_produtos, produtos)
            print("👋 Saindo...")
            break

        if tipo == 'gerente':
            if opcao == '1':
                print("\n🔧 CRUD Usuários")
                print("a. Criar")
                print("b. Listar")
                print("c. Atualizar")
                print("d. Excluir")
                acao = input("Escolha: ")
                if acao == 'a': criar_usuario(usuarios)
                elif acao == 'b': listar_usuarios(usuarios)
                elif acao == 'c': atualizar_usuario(usuarios)
                elif acao == 'd': excluir_usuario(usuarios)
            elif opcao == '2':
                print("\n🔧 CRUD Produtos")
                print("a. Criar")
                print("b. Listar")
                print("c. Atualizar")
                print("d. Excluir")
                acao = input("Escolha: ")
                if acao == 'a': criar_produto(produtos)
                elif acao == 'b': listar_produtos(produtos)
                elif acao == 'c': atualizar_produto(produtos)
                elif acao == 'd': excluir_produto(produtos)
            elif opcao == '3': buscar_produto(produtos)
            elif opcao == '4':
                print("a. Por nome")
                print("b. Por preço")
                acao = input("Escolha: ")
                if acao == 'a': ordenar_por_nome(produtos)
                elif acao == 'b': ordenar_por_preco(produtos)
        elif tipo == 'funcionario':
            if opcao == '1': listar_produtos(produtos)
            elif opcao == '2': atualizar_produto(produtos)
            elif opcao == '3': buscar_produto(produtos)
        elif tipo == 'cliente':
            if opcao == '1': listar_produtos(produtos)
            elif opcao == '2': buscar_produto(produtos)

# execução 
def main():
    arq_usuarios = 'usuarios.csv'
    arq_produtos = 'produtos.csv'
    usuarios = carregar_usuarios(arq_usuarios)
    produtos = carregar_produtos(arq_produtos)
    usuario_logado = login(usuarios)
    if usuario_logado:
        menu(usuario_logado, usuarios, produtos, arq_usuarios, arq_produtos)

main()
