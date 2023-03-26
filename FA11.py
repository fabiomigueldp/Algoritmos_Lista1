import math

print("Bem vindo à calculadora de distância entre pontos na superfície terrestre, para calcula a distância entre dois pontos siga as instruções a seguir:")

lat1 = float(input("Insira a látitude do ponto 1: "))
lon1 = float(input("insira a longitude do ponto 1: "))
lat2 = float(input("Insira a látitude do ponto 2: "))
lon2 = float(input("Insira a longitude do ponto 2: "))

haversine = 6371.01 * math.acos(math.sin(lat1)*math.sin(lat2)+math.cos(lat1)*math.cos(lat2)*math.cos(lon1-lon2))
#A Fórmula de Haversine está incorreta.
print(f"A distância entre os pontos inseridos, é de {haversine}km.")
print("teste")