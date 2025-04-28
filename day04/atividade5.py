#🌟 Desafio: Adivinhe o número mágico!
# Crie um programa em que:

# O computador sorteia um número entre 1 e 20.

# O jogador tem 5 tentativas para adivinhar.

# A cada tentativa, o jogo deve dizer:

# “🔼 Muito baixo!” se o número for menor que o sorteado

# “🔽 Muito alto!” se o número for maior que o sorteado

# “✅ Você acertou!” se for igual

# Se o jogador não acertar nas 5 tentativas, o jogo termina dizendo o número correto.

import random 

n = random.randint(1,10)

for tentativas in range(5):
    x = int(input("Escolha um número entre 1 e 10: "))
    if x == n:
        print("✅ Você acertou!")
    elif x < n:
        print("🔼 Muito baixo!")
    else:
        print("🔽 Muito alto!")
    