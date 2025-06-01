
# 🗓️ Dia 07 - Capítulo 6: Pesquisa em largura

## 📚 Livro consultado:
- Compreendendo Algoritmos - Capítulo 6

## 🧠 Assuntos estudados:
- Grafo
- Estrutura de dados deque
- Enqueue e Dequeue
- Pesquisa em largura

## ✍️ Anotações e Reflexões:

Sempre ir adicionando print a print dentro do código para ir debugando e entendendo o que está acontecendo por *debaixo dos panos* me ajuda. Além disso, estar em contato com código diariamente no meu outro projeto pessoal tem me ajudado a desbloquear os problemas com mais rapidez.
Notei uma melhoria na parte de resolução e decomposição de problemas.

## 🛠️ Atividades práticas:


## 🌱 Aprendizados do dia:

#### Lista de falhas de lógica que enfrentei durante a resolução e fui refatorando

1. Confusão sobre o Parâmetro da Função

Enquanto fazia o código criei uma função sem parâmetro, mas precisava verificar pessoa específica. Isso fezm com que o código verificasse todas as pessoas em vez da pessoa atual da fila. 
Lição: Lembrar de sempre definir claramente o que a função deve receber como entrada.

2. Sobrescrita de Variável e loop desnecessário

Fiz um  `for nome in grafo` e acabei sobrescrevendo o parâmetro `nome`. Além disso, usei um `for` para verificar uma pessoa específica. A função ignorava o parâmetro recebido e o código tava verboso e mais complexo do que o necessário
Lição: Evitar reutilizar nomes de parâmetros. Acessar diretamente itens específicos sem loop.

4. Chamada de Função Incorreta

Chamei `pessoa_e_vendedor()` sem passar argumento e a função não sabia qual pessoa verificar.
Lição: Sempre verificar se estou passando os argumentos necessários.

5. Variável Errada no Print Final

Problema: Usei `pessoa` (que sempre seria a primeira) em vez da `pessoa` encontrada, o que fez com que o código mostrasse sempre a mesma pessoa como vendedor.
Lição: Pensar em QUAL variável realmente contém o valor desejado.

Padrão Geral dos Erros:

- Falta de clareza sobre o que cada função deveria fazer
- Não testei cada parte separadamente
- Misturar responsabilidades (verificar todas vs verificar uma)
    