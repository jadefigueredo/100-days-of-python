# Encontre o valoor mais alto em uma lista

def alto_valor(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        lista = sorted(lista)
        return (alto_valor(lista[-1:]))
        

    
print(alto_valor([15, 28, 67, 22, 85, 107, 45, 17]))