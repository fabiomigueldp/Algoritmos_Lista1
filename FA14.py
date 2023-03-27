import math

print("Bem vindo ao programa para calcular a área de um triângulo, dados os comprimentos de seus três lados, siga as instrtuções a seguir:")

# Definindo as funções

def ll(l1, l2, l3):
    lll = (l1+l2+l3)/2
    return lll

def area_triangulo(l, l1, l2, l3):
    at = math.sqrt(l*(l-l1)*(l-l2)*(l-l3))
    return at

# Solicita os dados de l1, l2 e l3

l1 = float(input("Insira o comprimento de l1 em uma unidade X: "))

l2 = float(input("Insira o comprimento de l2 em uma unidade X: "))

l3 = float(input("Insira o comprimento de l3 em uma unidade X: "))

# Calcula l e a área

l = ll(l1, l2, l3)

area = area_triangulo(l, l1, l2, l3)

# Imprime a área

print(f"A área do triângulo é de {area}Xˆ2")