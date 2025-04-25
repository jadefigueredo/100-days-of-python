Compreensões de Lista (List Comprehensions)
Vamos aprender sobre compreensões de lista! Você pode ler sobre isso aqui:

Dada três inteiros x, y e z representando os limites para os eixos i, j e k, e um inteiro n, você deve imprimir uma lista de todas as possíveis coordenadas (i, j, k) em que a soma de i + j + k não é igual a n. Cada valor de i, j, k pode variar de 0 até o respectivo limite (incluindo o limite).

Formato de entrada:
Três inteiros x, y, z e um inteiro n, cada um em uma linha separada.

Restrições:
0
≤
𝑥
,
𝑦
,
𝑧
≤
100
0≤x,y,z≤100

0
≤
𝑛
≤
𝑥
+
𝑦
+
𝑧
0≤n≤x+y+z

Formato de saída:
Liste em ordem crescente todas as coordenadas possíveis (i, j, k) que satisfazem as condições acima, como uma lista de listas.

Exemplo de entrada:
1
1
1
2
Exemplo de saída:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
Explicação:
Todos os possíveis valores de (i, j, k) de acordo com os limites dados são:

(0, 0, 0)

(0, 0, 1)

(0, 1, 0)

(0, 1, 1)

(1, 0, 0)

(1, 0, 1)

(1, 1, 0)

(1, 1, 1)

Removendo aqueles em que a soma i + j + k = 2, sobra a lista de saída.