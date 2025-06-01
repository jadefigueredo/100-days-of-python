#1 crie uma fila contendo todas as pessoas que devem ser verificadas
    # criar uma tabela hash para mapear os amigos e vizinhos 
#2 Retirar uma pessoa da fila
    # utilizar deque()
#3 Confira se essa pessoa é um vendedor de mangas
    # a pessoa será um vendedor de manga se o seu nome terminar com "m"
    # criar uma função para verificar se os nomes na tabela contem a letra "m"
#4 caso a fila esteja vazia, não existem vendedores de manga na rede


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
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        print(f"Fila atual: {list(fila_de_pesquisa)}")
        if pessoa_e_vendedor(pessoa):
            print(pessoa + " é um vendedor de manga!")  
            return True
        else:
            fila_de_pesquisa += grafo[pessoa]
    return False

print(verifica_fila())
    

    

# while fila_de_pesquisa:
#     pessoa = fila_de_pesquisa.popleft()
#     if pessoa_e_vendedor(pessoa):
#         print (pessoa + "é um vendedor de manga")
#         return True
#     else:
#         return 

# print(grafo)