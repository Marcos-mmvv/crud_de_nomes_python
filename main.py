#Lista de opções
def menu ():
    print(f'{'-'*30} MENU {'-'*30}\n')
    print('1 - Adicionar um nome a lista: ')
    print('2 - Listar o conteúdo da lista: ')
    print('3 - Digite o nome que deseja localizar: ')
    print('4 - Atualizar a lista: ')
    print('5 - Digite o nome que deseja deletar da lista:')
    print('6 - sair ')
    print()

import os

lista = []

#Inicio do loop
while True:
    menu()
    escolha = input('Escolha a opção desejada: ')
        
    if escolha == '1':
        nome = input('Insira o nome: ').capitalize()
        lista.append(nome)
        lista.sort()
        print('Opção inválida')
      
    elif escolha == '2':
        for nome in range(len(lista)):
            print()
            print(f'{nome +1}º - {lista[nome]}')
            
    elif escolha == '3':
        nome = input('Insira o nome que deseja localizar: ').capitalize()
        if nome in lista:
            print()
            print(f'O nome {nome} foi localizado na lista.')
            
    elif escolha == '4':
        novo_nome = input('Insira o novo nome: ').capitalize()
        lista.append(novo_nome)
        lista.sort()
        if novo_nome in lista:
                print()
                print(f'O nome {novo_nome} foi inserido na lista com sucesso.')
                
    elif escolha == '5':
        deletar = input('Digite o nome a ser deletado: ')
        if deletar in lista:
            try:
                lista.remove(deletar)
                print(f'O nome {deletar} foi excluído com sucesso.')
                print()
                print(f'{'-'*10} LISTA ATUALIZADA {'-'*10}')

            except:
                print('Não foi possível deletar! ')
            for novo_nome in range(len(lista)):
                print(f'{novo_nome +1 }º - {lista[novo_nome]}')
                
    elif escolha =='6':
        os.system('cls')
        break
        
    else:
        escolha == ''
        print('Opção inválida ')
        continue