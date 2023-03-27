import math

# Definindo as funções

def area_circulo(raio):
    ac = math.pi*raio**2
    return ac

def volume_esfera(raio):
    ve = 4/3*math.pi*raio**3
    return ve 


# Solicita o raio

raio = float(input("Insira um valor para o raio em uma unidade X: "))

# Calcula a área e o volume
area = area_circulo(raio)

volume = volume_esfera(raio)

# Imprime a área e o volume

print(f"A área de uma circunferência de raio {raio} é de {area: .2f}X^2.")
print(f"O volume de uma esfera de raio {raio} é de {volume: .2f}X^3.")
