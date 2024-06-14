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
    '''Essa  função é responsavel por declarar as opções de funcionalidades'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')

def voltar_ao_menu_principal():
    '''Essa  função é responsavel por reniciar a aplicação'''
    input('Digite uma tecla para voltar ao menu principal! ')
    main()
        

def finalizar_app():
    '''Essa  função é responsavel por finalizar a aplicação'''
    os.system('cls')
    print('Finalizando o app\n')     
    
def opcao_invalida():
    '''Essa  função é responsavel no tratamento dos erros'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()
 
def exibir_subtitulo(texto):
    '''Essa  função é responsavel por exibir sub titulos nas funcionalidade'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha) 
    print()    
    
def cadastrar_novo_restaurante():
    '''Essa  função é responsavel por cadastrar um novo restaurante'''
    exibir_subtitulo('Cadastro de novos Reataurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    
    categoria = input(f'Digite o nome da categoria do resturante: {nome_do_restaurante}')
    
    dados_do_restaurante={'nome' :nome_do_restaurante, 'categoria':categoria, 'ativo': False}
    
    restaurantes.append(dados_do_restaurante)
    
    print(f'O restaurante {nome_do_restaurante} foi cadastro com sucesso!')
    voltar_ao_menu_principal()
        
def alternar_estado_ativo():
    '''Essa  função é responsavel por alterar o status do restaurante'''
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
            print('O restaurante não foi encontrado.')
        
    voltar_ao_menu_principal()

        
def listar_restaurantes():
    '''Essa  função é responsavel por listar os restaurantes cadastrados'''
    exibir_subtitulo('Listando os restaurantes')
    
    print(f'{'Nome do restaurante'.ljust(21)} | {'categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'.{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()
    
    
        
def escolher_opcao():
    '''Essa  função é responsavel pela escolha da opção''' 
    try:   
        opcao_escolhida = int (input('Escolha uma opção: '))
        
        if opcao_escolhida == 1 :
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2 :
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_ativo()
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
    

