import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6372.8  # Raio da Terra em km

    # Converter graus decimais para radianos
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)

    # Aplicar a fórmula de Haversine
    a = math.sin(dLat/2)**2 + math.sin(dLon/2)**2 * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.asin(math.sqrt(a))

    # Calcular a distância em km
    distance = R * c
    return distance

# solicita as coordenadas do ponto A
lat1 = float(input("Insira a latitude do ponto A: "))
lon1 = float(input("Insira a longitude do ponto A: "))

# solicita as coordenadas do ponto B
lat2 = float(input("Insira a latitude do ponto B: "))
lon2 = float(input("Insira a longitude do ponto B: "))

# calcula a distância
dist = haversine(lat1, lon1, lat2, lon2)

# imprime a distância em km
print(f"A distância entre os pontos A e B é de {dist:.2f} km.")