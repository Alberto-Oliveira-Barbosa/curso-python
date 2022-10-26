"""
formatação de strings
"""

nome = 'Carlos'
idade = 30
altura = 1.73
peso = 99
maior_idade = idade > 18
imc = peso / (altura**2)

print( 'Nome ',nome)
print('Idade ',idade)
print('É maior de idade? ',maior_idade)

print('Usando F-strings')
print(f'{nome} tem {idade} anos de idade e seu IMC é: {imc:.2f}')

print('Usando format')
print('{} tem {} anos de idade e seu IMC é: {:.2f}'.format(nome,idade,imc))

# possível passar mais de uma vez o mesmo parâmetro com a sua posição
print('Usando posição')
print('Seu nome é {0}? \n {0} tem {1} anos de idade e seu IMC é: {2:.2f}'.format(nome,idade,imc))

print('Nomeando parâmetros')
print('{n} tem {i} anos de idade e seu IMC é: {im:.2f}'.format(n=nome,i=idade,im=imc))
