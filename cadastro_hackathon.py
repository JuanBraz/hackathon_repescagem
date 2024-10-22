# Criar um Dicionário para o decorrer do código
lista_usuario = {}

while True:
    #Criar um menu com as opções de cadastro para o usuário
    print()
    print(30*'*', 'Menu', 30*'*')
    print('1. Cadastrar usuário.')
    print('2. Listar usuário.')
    print('3. Editar usuário.')
    print('4. Excluir usuário.')
    print('5. Sair')
    print(66*'*')
    print()
    opcao = input('Digite a opção desejada: ')

    # Cadastrar o usuário
    if opcao == '1':
        nome = input('Digite o nome que deseja cadastrar: ').upper()
        idade = int(input('Digite a idade que deseja cadastrar: '))

        if nome in lista_usuario:
            print('Usuario já existente!')
        else:
            lista_usuario[nome] = {'nome' : nome, 'idade' : idade}
            print(f'Usuário {nome} cadastrado com sucesso!')
    
    # Listar Usuário
    elif opcao == '2':
        if lista_usuario:
            for nome , dados in lista_usuario.items():
                print(f'Nome: {dados['nome']}, Idade: {dados['idade']}')
        else:
            print('Nenhum usuário encontrado!')
    
    # Editar Usuario
    elif opcao == '3':
        nome = input('Digite o nome que deseja editar: ').upper()
        if nome in lista_usuario:
            idade = int(input('Digite uma nova idade: '))
            lista_usuario[nome] = {'nome' : nome,'idade' : idade}
            print(f'Usuário {nome} editado com sucesso!')

    # Excluir Usuario
    elif opcao == '4':
        remover = input('Digite o nome que deseja remover: ')
        if remover in lista_usuario:
            del lista_usuario[remover]
            print('Usuário removido com sucesso!')
        else:
            print('Usuário não econtrado')

    # Saida do Sistema usando o break para encerrar o laço de repetição
    elif opcao == '5':
        print('Saindo do Sistema!')
        break
    else:
        print('Digite uma opcao válida: ')