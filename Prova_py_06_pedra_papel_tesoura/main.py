import random

def escolher_usuario():
    escolha_do_usuario = str(input("Escolha entre pedra, papel ou tesoura: ")).lower()
    return escolha_do_usuario

def escolher_computador():
    lista = ['pedra', 'papel', 'tesoura']
    escolha_do_computador = random.choice(lista)
    return escolha_do_computador

def jogo (escolha_usuario, escolha_da_maquina):
    if escolha_usuario == escolha_da_maquina:
        return 'empate'
    elif escolha_usuario == 'pedra' and  escolha_da_maquina == 'tesoura':
        return 'O usuario e o vencedor'
    elif escolha_usuario == 'tesoura' and  escolha_da_maquina == 'papel':
        return 'O usuario e o vencedor'
    elif escolha_usuario == 'papel' and  escolha_da_maquina == 'pedra':
        return 'O usuario e o vencedor'
    else:
        return 'O computador é o vencedor'

usuario = escolher_usuario()
computador = escolher_computador()

print(f'A escolha do computador foi: {computador}')
print(f'A escolha do usuario foi: {usuario}')

print (jogo(usuario,computador))

