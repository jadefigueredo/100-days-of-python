import os
from datetime import datetime

def criar_resumo(dia):
    # Define o nome da pasta e cria a estrutura
    pasta = f"dia{dia:02d}"
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    arquivo_resumo = os.path.join(pasta, "resumo.md")

    data_atual = datetime.now().strftime("%d/%m/%Y")

    resumo = f"""
# 🗓️ Dia {dia:02d} - {input('Título da atividade: ')}

## 📚 Livro consultado:
- Compreendendo Algoritmos - Capítulo {input('Capítulo: ')}

## 🧠 Assuntos estudados:
- {input('Assuntos estudados: ')}

## ✍️ Anotações e Reflexões:
- {input('Reflexões do dia: ')}

## 🛠️ Atividades práticas:
- {input('Atividades realizadas: ')}

## 🌱 Aprendizados do dia:
- {input('Aprendizados do dia: ')}

    """

    # Cria o arquivo .md
    with open(arquivo_resumo, "w") as f:
        f.write(resumo)

    print(f"Resumo do dia {dia:02d} criado com sucesso!")

if __name__ == "__main__":
    dia = int(input("Qual o número do dia? "))
    criar_resumo(dia)
