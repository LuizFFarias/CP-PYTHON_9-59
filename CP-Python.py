agenda = {}

# Função para mostrar a lista de contatos na agenda.
def mostrar_contatos(agenda):
    print("Contatos:")
    for nome, dados in agenda.items():
            print(f"Nome: {nome}")
            
            if 'telefone' in dados:
                print(f"Telefone: {dados['telefone']}")
            else:
                print("Telefone: N/A")
            
            if 'email' in dados:
                print(f"E-mail: {dados['email']}")
            else:
                print("E-mail: N/A")

            if 'telefones' in dados:
                print('Telefones:')
                for telefone in dados['telefones']:
                    print(telefone)

            print('-' * 20)


# Função para adicionar contatos na array de contatos
def adicionar_contato(nome, telefone, email):
    while True:

        if nome == "":
            print("Digite um nome válido!")
        elif    len(telefone) < 11: 
            print("Digite um número válido!")
        elif email == "":
            print("Digite um e-mail válido!")
        else:    
            agenda [nome] = {'telefone': telefone,
                            'email': email}
            print('Contato adicionado.')
            break


# Função para remover um contato da agenda 
def remover_contato(nome):
    if nome in agenda:
        del agenda[nome]
        print(f"Contato {nome} removido com sucesso.")
    else:
        print(f"Contato {nome} não encontrado na agenda.")


#Função para inserir telefones
def inserirTelefone(nome):
    while True:
        telefone = input('Digite seu telefone: ')
        if telefone == '0':
            print('Inserir telefones encerrado')
            break

        if nome in agenda:
            if 'telefones' not in agenda[nome]:
                agenda[nome]['telefones'] = []
            agenda[nome]['telefones'].append(telefone)
            print('Telefone adicionado')
        else:
            print('Contato não encontrado')
        
        
#Função para remover telefone de um contato  
def remover_telefone(nome, telefone):
    if nome in agenda:
        if 'telefones' in agenda[nome] and telefone in agenda[nome]['telefones']:
            agenda[nome]['telefones'].remove(telefone)
            print(f"Telefone {telefone} removido do contato {nome}.")
        elif 'telefone' in agenda[nome] and agenda[nome]['telefone'] == telefone:
            del agenda[nome]['telefone']
            print(f"Telefone {telefone} removido do contato {nome}.")
        else:
            print(f"Telefone {telefone} não encontrado no contato {nome}.")
    else:
        print(f"Contato {nome} não encontrado na agenda.")


#Função para alterar e-mail.
def alterar_email(nome, novo_email):
    if nome in agenda:
        agenda[nome]['email'] = novo_email
        print(f"Email de {nome} alterado para {novo_email}.")
    else:
        print(f"Contato {nome} não encontrado na agenda.")
        

# Função para exibir o menu de opções
def menu(agenda):
    """Exibe o menu da agenda e permite que o usuário escolha uma opção"""
    while True:
        print("\nMenu:")
        print("1. Mostrar Contatos")
        print("2. Adicionar Contatos")
        print("3. Remover Contatos")
        print("4. Inserir Telefone")
        print("5. Remover Telefone")
        print("6. Alterar E-mail")
        print("7. Finalizar")
        
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
           mostrar_contatos(agenda)
        elif escolha == "2":
            nome  = input("Digite o nome do novo contato: ")
            telefone = input("Digite o número de telefone: ")
            email = input("Digite o e-mail: ")
            adicionar_contato(nome, telefone, email)
        elif escolha == "3":
            nome  = input("Digite o nome do contato a ser removido: ")
            remover_contato(nome)
        elif escolha == "4":
            nome = input("Digite o nome do contato: ")
            inserirTelefone(nome)
        elif escolha == "5":
            nome  = input("Digite o nome do contato: ")
            telefone = input("Digite o número de telefone a ser removido: ")
            remover_telefone(nome, telefone)
        elif escolha == "6":
            nome  = input("Digite o nome do contato: ")
            novo_email = input("Digite o novo e-mail: ")
            alterar_email(nome, novo_email)
        elif escolha == "7":
            print("Encerrando o Programa...")
            break
        else:
            print("Opção Inválida. Tente Novamente...")
            
menu(agenda)