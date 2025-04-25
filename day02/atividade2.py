frase = input('').lower()
letras = []

for caractere in frase:
    if caractere.isalpha():
        letras.append(caractere)
for caractere in letras:
    print(f"A letra '{caractere}' aparece {letras.count(caractere)} vezes")