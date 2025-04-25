# Pilha de chamada com fatorial e erro de recursão
#Exercício 3.2: O que acontece com a pilha quando a cursão recursiva fica executando infinitamente?
# R: A pilha de alcança a quantidade máxima de execuções e o programa é encerrado

# def fat(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fat(x -1)
    
# print(fat(0))




#Pilha de chamada com fatorial corrigida

def fat(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fat(x -1)
    
print(fat(12))
