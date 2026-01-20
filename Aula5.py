import pandas as pd
import numpy as np
import matplotlib as plt

#Lista de nomes com A, C, J
nomes = ['Alice','João','Ana','José','Carlos','Janaína','Caio','Cristiane']

nomes_com_a = []
nomes_com_c = []
nomes_com_j = []
for nome in nomes:
    if nome.startswith('A'):
        nomes_com_a.append(nome)
    elif nome.startswith('C'):
        nomes_com_c.append(nome)
    elif nome.startswith('J'):
        nomes_com_j.append(nome)

print('Nomes com A:',(nomes_com_a))
print('Nomes com C:',(nomes_com_c))
print('Nomes com J:',(nomes_com_j))

#Lista de menores e maiores de idade
idades = [17,18,25,43,15,29,36,50]
maiores_de_idade = []
menores_de_idade = []

for idade in idades:
    if idade>18:
        maiores_de_idade.append(idade)
    else:
        menores_de_idade.append(idade)

print('Maiores de idade:',(maiores_de_idade))
print('Menores de idade:',(menores_de_idade))

#Contagens de salarios
salarios = [2000,5000,1500,2100,5000,1500,2000]
contagem = {} #dicionario vazio

for salario in salarios:
    if salario in contagem:
        contagem[salario] = contagem[salario] +1
    else:
        contagem[salario] = 1

print('Contagem de salarios:',(contagem))

#Contagem de categorias
categorias = ['A','B','C','C','A','C','B','B','A']
contagem_categorias = {}

for categoria in categorias:
    if categoria in contagem_categorias:
        contagem_categorias[categoria] = contagem_categorias[categoria] +1
    else:
        contagem_categorias[categoria] = 1

print('Contagem de categorias:',(contagem_categorias))

#Números divisíveis por 5
numero = 1
while numero <= 10:
    if numero %5 == 0:
        print(f'Número {numero} é divisível por 5')
    numero += 1

#Números pares e ímpares
numero = 1
while numero < 20:
    if numero %2 == 0:
        print(f'Número {numero} é par')
    else:
        print('Número', numero, 'é ímpar') 
    numero += 1
