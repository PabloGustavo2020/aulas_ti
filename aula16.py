 #Gabarito
def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")
    return nome, cpf, senha

def fazer_login(usuarios):
    cpf_l = input("Digite seu CPF: ")
    senha_l = input("Digite sua senha: ")

    for usuario in usuarios:
        if cpf_l == usuario[1] and senha_l == usuario[2]:
            print("Login feito com sucesso!")
            return True
        
    print(" CF ou senha incorretos. tente novamente.")
    return False

def main():
    usuarios = []
    while True:
        print("1. Cadastrar Usuário")
        print("2. Fazer Login")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            novo_usuario = cadastrar_usuario()
            if len(novo_usuario[1])