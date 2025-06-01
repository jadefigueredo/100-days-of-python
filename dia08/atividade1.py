# Continuação do capítulo 06 - Pequisa em largura
# antes de verificar uma pessoa é importante conferir se ela ainda não foi verificada. Para fazer isso, você criará uma lista de pessoas que já foram verificadas.

from collections import deque

def lista_pessoas():
    pessoa = {
        "voce": ["alice", "bob", "claire"],
        "bob": ["anuj", "peggy"],
        "alice": ["peggy"],
        "claire": ["thom", "jonny"],
        "anuj": [],
        "peggy": [],
        "thom": [],
        "jonny": []
    }
    return pessoa

def pessoa_e_vendedor(nome):
    return nome[-1] == "m"


def verifica_fila():
    grafo = lista_pessoas()    
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    return False
