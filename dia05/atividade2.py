# Escreva uma função recursiva que conte o número de itens em uma lista

def conta_itens(lista):
    total = 0 
    if lista == []:
        return total
    else:
        return 1 + conta_itens(lista[1:])
    
print(conta_itens([2, 6, 9, 12, 14, 16, 15, 29]))