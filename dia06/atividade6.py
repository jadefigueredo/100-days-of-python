# Um mapeamento do tamanho de baterias e sua devida potência. Os tamanhos são os seguintes: AA, AAA, AAAA e 9V. As potências são as seguintes: 1.5, 1.2, 0.9 e 6.
def mapeamento_baterias():
    dict = {
        'AA': 1.5,
        'AAA': 1.2,
        'AAAA': 0.9,
        '9V': 6
    }
    return dict

print(mapeamento_baterias())