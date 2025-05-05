# Mapeie cada letra para um número primo:
# a = 2
# b = 3
# c = 5
# d = 7
# e = 11
# e assim por diante. Para uma string a função hash é a soma de todos os caracteres-modulo ao quadrado, conforme o tamanho da hash
# se o tamanho de sua hash for 10, por exemplo, e a string for "bag", o índice será (3 + 2 + 17) % 10 = 22 % 10 = 2
# para cada um desses exemplos, qual função hash forncerá uma boa distribuição? Consiere o tamanho da tabela hash tenha dez espaços

# Etapas do Problema:
# Gerar os 26 primeiros números primos (para associar às 26 letras do alfabeto).

def gerar_primos(n):
    lista_primos = []
    num = 2
    while len(lista_primos) < n:
        for i in lista_primos: 
            if num % i == 0:
                break
        else:
            lista_primos.append(num)
        num += 1
    return lista_primos      

# Mapear cada letra do alfabeto (de 'a' a 'z') para um primo, mantendo a ordem.

import string
def mapeamento():
    primos = gerar_primos(26)
    alpha = list(string.ascii_lowercase)
    dicionario = {}
    for letra, p in zip(alpha, primos):
        dicionario[letra] = p
    return dicionario    
        
# Criar uma função que recebe uma string, soma os valores primos correspondentes às letras e retorna soma % tamanho_tabela.
# Testar essa função para verificar a distribuição dos índices em uma tabela de tamanho 10.


def recebe_string(tamanho_tabela):
    input_usuario = input('').lower()
    mapa = mapeamento()
    soma = 0
    for letra in input_usuario:
        if letra in mapa:
            soma += mapa[letra]
    return soma % tamanho_tabela      

print(recebe_string(10))


