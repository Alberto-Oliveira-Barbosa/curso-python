"""
Tipos de dados primitivos
str - Strings - Textos
int - Inteiro - 12345 -10 -15
float - real/Ponto flutuante - 10.22 11.78
bool - booleano/lógico - True/False
"""

# verifica o tipo de dado
print('texto',type('texto'))
print(1234, type(1234))
print(10.56, type(10.56))
print(True, type(True))
print(10 == 10, type(10==10))


# type casting - CONVERSÃO DE TIPOS

print('10', type('10'), type(int('10')))
print('10.50', type('10.50'), type(float('10.50')))
print(bool(0)) # 0 convertido para bool é lido como False
print(bool(1)) # 1 convertido para bool é lido como True

