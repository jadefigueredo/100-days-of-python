#Exemplo de caso base e caso recursivo

def regressiva(i):
    print(i)
    if i <= 1: #caso base
        return
    else:
        regressiva(i-1) # caso recursivo
        
        
print(regressiva(10))