#Exercício 1

import sys
'''

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

if num1 > num2:
    print(num1)
else:
    print(num2)
'''
#Exercício 2

'''
num = int(input("Digite um número:"))

if num>=0:
    print("É positivo")
else:
    print("É negativo")

'''

#Exercício 3

'''
idade = int(input("Digite sua idade:"))

if idade>= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
'''

#Exercício 4

'''
num1 = int(input("Digite um número:"))
num2 = int(input("Digite um número:"))
num3 = int(input("Digite um número:"))

if num1>=num2 and num1>=num3:
    print("O maior é:", num1)
elif num2>=num1 and num2>=num3:
    print("O maior é:", num2)
else:
    print("O maior é:", num3)
'''

#Exercício 5

'''
dia = int(input("Digite um número:"))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("Valor inválido")
'''
#Exercício 6

'''
ano = int(input("Digite um ano:"))

if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("É bissexto")
else:
    print("Não é bissexto")

'''

#Exercício 7

'''
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite um segunda nota:"))

media = (nota1+nota2)/2

if media == 10:
    print("Aprovada com distinção")
elif media >= 7:
        print("Aprovada")
else:
    print("Reprovada")

'''

#8 IF

'''
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
num3 = float(sys.argv[3])

if num1 > num2:
    if num1 > num3:
        if num2 > num3:
            print(num1, num2, num3)
        elif num1 > num2:
            if num1 > num3:
                if num3 > num2:
                    print(num1, num3, num2)
                elif num2 > num1:
                    if num2 > num3:
                        if num1 > num3:
                            print(num2, num1, num3)
                        elif num2 > num1: 
                            if num2 > num3:
                                if num3 > num1:
                                    print(num2, num3, num1)
                                elif num3 > num1:
                                    if num3 > num2:
                                        if num1 > num2:
                                            print(num3, num1, num2)
                                        else:
                                            print(num3, num2, num1)
'''

#8 FOR

'''
numeros = []

numeros.append(float(sys.argv[1]))
numeros.append(float(sys.argv[2]))
numeros.append(float(sys.argv[3]))

maior = numeros[0]
meio = 0
menor = numeros[0]

for i in range(3):
    if maior < numeros[i]:
        maior = numeros[i]
    if menor > numeros[i]:
        menor = numeros[i]

for i in range(3):
    if numeros[i] != maior and numeros[i] != menor:
        meio = numeros[i]

print(maior, meio, menor)

'''

#9 IF

'''
print("Responda com sim ou não")
p1 = input("\nFalou com a vítima no dia do crime? ")
p2 = input("\nEsteve no local do crime? ")
p3 = input("\nMora perto da vítima? ")
p4 = input("\nDevia dinheiro para a vítima? ")
p5 = input("\nJá trabalhou com a vítima? ")

total = 0

if p1 == "sim":
    total += 1
if p2 == "sim":
    total += 1
if p3 == "sim":
    total += 1
if p4 == "sim":
    total += 1
if p5 == "sim":
    total += 1

if total == 2:
    print("\nClassificação: Suspeita")
elif total > 2 and total < 5:
    print("\nClassificação: Cúmplice")
elif total == 5:
    print("\nClassificação: Assassina")
else:
    print("\nClassificação: Inocente")

'''
#9 FOR

'''
print("Responda com sim ou não")
respostas = []
respostas.append(input("\nFalou com a vítima no dia do crime? "))
respostas.append(input("\nEsteve no local do crime? "))
respostas.append(input("\nMora perto da vítima? "))
respostas.append(input("\nDevia dinheiro para a vítima? "))
respostas.append(input("\nJá trabalhou com a vítima? "))

total = 0

for i in respostas:
    if i == "sim":
        total += 1

if total == 2:
    print("\nClassificação: Suspeita")
elif total > 2 and total < 5:
    print("\nClassificação: Cúmplice")
elif total == 5:
    print("\nClassificação: Assassina")
else:
    print("\nClassificação: Inocente")

'''