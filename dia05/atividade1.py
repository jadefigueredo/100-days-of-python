# você deve somar todos os números e retornar o valor total. Isto é simples de ser feito com um loop.
# def soma(lista):
#     total = 0
#     for x in lista:
#         total+= x
#     return total


# print(soma([1, 2, 3, 4]))

# Mas como isso poderia ser feito com uma função recursiva?

def soma(lista):
    total = 0
    if lista == []:
        return total
    else:
        return lista[0] + soma(lista[1:])
        
print(soma([2, 4, 6]))