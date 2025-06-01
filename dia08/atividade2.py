# grafo de rotina matinal
# não pode tomar café da manhã antes de escovar dentes
# a partir desse grafo você pode fazer uma lista relacionando a ordem das atividades da minha rotina matinal
# A: Acordar, tomar banho, tomar café da manhã, escovar os dentes
# B: Acordar, escovar os dentes, tomar café da manhã, tomar banho
# C: Tomar banho, acordar, escovar os dentes, tomar café da manhã
# a partir desse grafo você pode fazer uma lista relacionando a ordem das atividades da minha rotina matinal
# Qunato a estas três listas, marque se elas são válidas ou inválidas
from collections import deque

def grafo_rotina():
    rotina = {
        "A": [ "Acordar", "tomar banho", "tomar café da manhã", "escovar os dentes"],
        "B": ["Acordar", "escovar os dentes", "tomar café da manhã","tomar banho"],
        "C": ["Tomar banho", "acordar", "escovar os dentes","tomar café da manhã"]
        }
    return rotina

def ordens_validas():
    lista = grafo_rotina()
    sequencia_valida = []
    for sequencia in lista.items(): # iterando sobre todos os itens do dict
        if sequencia[1][0] == "Acordar" and sequencia[1].index("tomar café da manhã") < sequencia[1].index("escovar os dentes", 1):
            sequencia_valida.append(sequencia)
            if sequencia_valida != []:
                continue
            else:
                print("Nenhuma sequência é vaálida")
        return sequencia_valida

            
print(ordens_validas())

    