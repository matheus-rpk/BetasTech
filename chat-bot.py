import os



def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Clique AQUI para baixar sua certidão negativa!{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} Deseja 2º via do IPTU ou pagar, digite 1 para 2º via e digite 2 para pagar .{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}Deseja cadastrar ou regularizar uma empresa ?{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}Deseja consultar ou cancelar uma nota fiscal?{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')


def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo a Devaprender.com')
    nome = 'user'
    # pedir o CPF
    cpf = input('Digite seu CPF: ')
    # pedir o e-mail
    email = input('Digite sua data de nascimento: ')
    while True:
        # Oferer o menu de opções
        resposta = input(
            f'O que gostaria de saber hoje?{os.linesep}[1] - CERTIDÃO NEGATIVA{os.linesep}[2] - IPTU{os.linesep}[3] - ALVARÁ{os.linesep}[4] - NSFA{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()
