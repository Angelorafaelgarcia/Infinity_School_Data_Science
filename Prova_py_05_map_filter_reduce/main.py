# Considere uma lista de numeros  inteiros numeros = [1,2,3,4,5,6,7,8,9,10]
# utilizando as funçoes map(), filter() e reduce(), escreva um codigo que
# execute as seguintes operacoes:
# Funcao map() para obter uma nova lista com o quadrado de cada numero da lista numeros 
# Funcao filter() para obter uma nova lista com numeros pares da lista numeros
# Funcao reduce() para obter a soma de todos os numeros da lista numeros
# Qual o resultado obtido após a execução das operações acima?

numeros = [1,2,3,4,5,6,7,8,9,10]
quadrado = list(map(lambda x: x**2,numeros))
print(quadrado)

#resposta: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numeros = [1,2,3,4,5,6,7,8,9,10]
par = list(filter(lambda x: x%2 == 0,numeros))
print(par)

#resposta: [2, 4, 6, 8, 10]

from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]
soma = reduce(lambda x,y: x+y,numeros)
print(soma)

#resposta: 55