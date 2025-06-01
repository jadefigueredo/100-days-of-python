# 🗓️ Dia 08 - Continuação do capítulo 06

## 📚 Livro consultado:
- Compreendendo Algoritmos - Capítulo 06 - Pesquisa em largura

## 🧠 Assuntos estudados:
- Grafos e ordenações topológicas;
- Árvore;
- Filas;
- Caminho mínimo

## 📝 Resumo:
- A pesquisa em largura diz se existe um caminho de A para B;
- Se esse caminho existir a pesquisa em largura consegue trazer o caminho mínimo.
- Se o problema é do tipo: "Encontre o menos X", é bom tentar modelar o problema utilizando grafo e usa a pesquisa em largura para resolver.
- Filas são FIFO (Primeiro a entrar, primeiro a sair).
- Pilhas são LIFO (Último a entrar, primeiro a sair).
- Para que a pesquisa seja em largura é preciso verificar as pessoas na ordem em que elas foram adicionadas à lista de pesquisa. Portanto a lista de pesquisa deve ser uma fila: caso contrário, não se obtém o caminho mínimo.
- Cada vez que eu precisar verificar alguém/algo, é importante não fazer duas verificações pra não acabar num loop infinito.

## ✍️ Anotações e Reflexões:
- Precisei relembrar alguns assuntos.
    - Sintaxe de listas em dicionários - coloquei números fora das aspas dentro da lista de dicionários
    - Iteração com `.items()` - Havia esquecido que retornava tuplas e errei na resposta da atividade 2.
    - Acesso a elementos de tuplas - `sequencia[0]` para chave, `sequencia[1]` para valor para valor.
    - Método `.index()` - para encontrar posição de elementos em listas.
    - Fluxo de controle - diferença entre `return` dentro e fora do loop.

## 🌱 Aprendizados do dia:
- Confusão com sintaxe - números fora de aspas, `sequencia[:]` e `sequencia[1]`.
- Conflito de variáveis - usei a mesma string como parâmetro e variável do loop.
- Lógica de validação - decidi trabalhar com nomes ao invés de `números/posições`.
- Return prematuro - fiz um return que parava na primeira verificação ao invés vez de testar todas as listas.
- Estrutura de dados -  diferenciação na extração dos dados: tuplas, listas e dicionários.

    