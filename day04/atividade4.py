import random

def tenta_acerto():
    acerto = 0
    erro = 0
    n = random.randint(1, 10)
    
    for tentativa in range(3):
        x = int(input("Escolha um número entre 1 e 10: "))
        if x == n:
            acerto += 1
            print("você acertou!")
            break
        else:
            erro +=1
            print("você errou!")
        
tenta_acerto()
