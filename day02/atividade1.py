frase = input('Digite uma frase e eu lhe direi quantas vezes a letra escolhida aparece na frase: ')
letra = input('Digite uma letra: ')
contagem = 0


for i in frase:
    if i == letra:
        contagem += 1
print(f'A letra "{letra}" aparece {contagem} vezes na frase "{frase}".')
