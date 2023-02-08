#1

'''num = []

for _ in range (5):
    num.append(float(input("Digite um número:")))

maior = num[0]
for i in range(1,5):
    if maior < num[i]:
        maior = num[i]
    
print("O maior é:", maior)'''

#2

'''num = []

for _ in range (5):
    num.append(float(input("Digite um número:")))

soma = 0
for i in range(5):
    soma += num[i]

media = soma/5

print("Soma:", soma)
print("Média:", media)'''

#3

'''for x in range(1,51,2):
    print(x)'''

#4

'''import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

for x in range(num1+1, num2, 1):
    print (x)'''

#5

'''for x in range(0,11,1):
    print("2 x", x, "=", 2*x)'''

#6

'''for x in range(2,10,1):
    for y in range (0,11,1):
        print(x,"x", y, "=", x*y)'''