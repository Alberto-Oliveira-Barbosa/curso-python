"""
Criar variáveis para nome (str), idade (int), altura (float) e peso de uma pessoa
Criar variável com o ano atual (int)
Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
Exibir um texto com todos os valores na tela usando F-Strings
"""

nome = 'João'
idade = 35
altura = 1.73
peso = 80
ano_atual= 2022
nascimento = 2022 - idade
imc = peso / (altura ** 2)

print(
    f"""
    {nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.
    O IMC de {nome} é {imc:.2f}.
    {nome} nasceu em {nascimento}.
    """)