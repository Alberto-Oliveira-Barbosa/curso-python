"""
Variáveis 
Apelidos para algo que é salvo na memória do computador

Iniciar com letras, pode conter numeros, separa por _, letras minusculas
"""

nome = 'Carlos'
idade = 30
altura = 1.73
peso = 99
maior_idade = idade > 18


print( 'Nome ',nome)
print('Idade ',idade)
print('É maior de idade? ',maior_idade)

# é possível fazer contas com as variáveis 
print(nome,'tem', idade, 'anos de idade e seu IMC é: ' , peso / (altura**2))