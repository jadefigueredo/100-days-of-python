# recursao 
class Item:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.itens = []

    def e_uma_caixa(self):
        return self.tipo == "caixa"

    def e_uma_chave(self):
        return self.tipo == "chave"

    def adicionar(self, item):
        if self.e_uma_caixa():
            self.itens.append(item)
            
    def __iter__(self):
        return iter(self.itens)

def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item)
        elif item.e_uma_chave():
            print(("achei a chave!"))
            return True
    return False
        
                    
caixa_principal = Item("caixa principal", "caixa")
caixa_secundaria = Item("caixa secundária", "caixa")
caixa_terciaria = Item("caixa três", "caixa")
chave = Item("molho de chaves", "chave da casa")
casaco = Item("casaco", "roupa")

caixa_terciaria.adicionar(caixa_secundaria)
caixa_principal.adicionar(casaco)
caixa_principal.adicionar(chave)
caixa_secundaria.adicionar(caixa_principal)


print(procure_pela_chave(caixa_principal))