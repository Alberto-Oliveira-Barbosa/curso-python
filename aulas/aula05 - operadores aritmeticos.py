"""
OPERADORES ARITMÉTICOS
+ --> ADIÇÃO
- --> SUBTRAÇÃO
* --> MULTIPLICAÇÃO
/--> DIVISÃO
//--> DIVISÃO INTEIRA
%--> MÓDULO
**--> EXPONENCIAÇÃO
()--> ALTERA A PRECEDÊNCIA DOS OPERADORES
"""

print('Adição ',10+10)
print('Subtração ',10-10)
print('Multiplicação ',10*10)
print('Divisão ',10/10)

print('Multiplicação com strings (faz repetição) ', 10 * "10")
print('Adição com strings (concatena os valores) ','10'+'10')
print('Divisão inteira ',10//3)
print('Potenciação ',2 ** 10)
print('Módulo (retorna o resto da divisão) ',10 % 3)
print('O python usa a precedência matemática pra calcular os valores,\
mas com o uso de parênteses é  possível alterar a ordem de execução', (10+5) * 10 )

# para mais informações sobre precedências de operadores: 
# https://docs.python.org/3/reference/expressions.html#operator-precedence
