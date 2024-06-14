import os

restaurantes = [{'nome': 'R1', 'categoria': 'Japonesa', 'ativo' : False},
                {'nome': 'R2', 'categoria': 'Mineira', 'ativo' : True},
                {'nome': 'R3', 'categoria': 'Churrascaria', 'ativo' : True}
               ]

def exibir_nome_do_programa():
    print("""     
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcaoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal! ')
    main()
        

def finalizar_app():
    os.system('cls')
    print('Finalizando o app\n')     
    
def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()
 
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto) 
    print()    
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos Reataurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    
    categoria = input(f'Digite o nome da categoria do resturante: {nome_do_restaurante}')
    
    dados_do_restaurante={'nome' :nome_do_restaurante, 'categoria':categoria, 'ativo': False}
    
    restaurantes.append(dados_do_restaurante)
    
    print(f'O restaurante {nome_do_restaurante} foi cadastro com sucesso!')
    voltar_ao_menu_principal()
        
def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'.{nome_restaurante} | {categoria} | {ativo}')
    
    voltar_ao_menu_principal()
    
    
        
def escolher_opcao(): 
    try:   
        opcao_escolhida = int (input('Escolha uma opção: '))
        
        if opcao_escolhida == 1 :
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2 :
            listar_restaurantes()
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
    exibir_opcaoes()
    escolher_opcao()
        
if __name__ == '__main__' :
    main()        
    

