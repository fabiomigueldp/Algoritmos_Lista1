import math
print("Bem vindo ao programa de calculo da área de um polígono regular, siga as intruções:")

# Definindo a função

def area_polreg(n, l):
    apolreg = (n*l**2)/4*math.tan(math.pi/n)
    return apolreg

# Solicita o número de lado e comprimento destes

n = int(input("Insira o número de lados do polígono regular: "))

l = float(input("Insira o comprimento dos lados do poígono regular em uma unidade X: "))

# Calcula a área

area = area_polreg(n, l)

# Imprime a área

print(f"A área de um poígono regula de {n} lados, com cada um medindo {l}X, é de {area}X^2.")