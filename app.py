import os

restaurantes = [{'nome':'Ponte Furada', 'categoria':'Japonesa', 'ativo': False},
                {'nome':'Show King', 'categoria':'Hamburguer', 'ativo': False},
                {'nome':'POP', 'categoria':'Pizaa', 'ativo': True}]

def exibir_nome_do_programa():
      print("""

      ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
      ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
      ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
      ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
      ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
      ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░

            """)

def exibir_opcoes():
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Ativar restaurante')
      print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando aplicativo')

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
     print('Opção inválida!\n')
     voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurantes = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurantes}: ')
    dados_do_restaurante = {'nome':nome_do_restaurantes, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurantes} foi cadastrado!')
    voltar_ao_menu()
     
def listar_restaurante():
    exibir_subtitulo('Listar restaurantes ')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} {categoria} {ativo} ')

    voltar_ao_menu()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()  
    escolher_opcao()

if __name__ == '__main__':
    main()