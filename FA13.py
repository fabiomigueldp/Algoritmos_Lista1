print("Bem vindo ao programa de cálculo da área de um triângulo, para calcula a área de um triângulo, siga as instruções a seguir:")

# Definindo a funções da área do triângulo

def area_triangulo(b, h):
    at = (b*h)/2
    return at

# Solicita os dados do comprimento da base e da altura do triângulo

b = float(input("Insira o comprimento da base do triângulo em uma unidade X: "))

h = float(input("Insira a altura desse mesmo triângulo em uma unidade X: "))

# Calcula a área do triângulo

area = area_triangulo(b, h)

# Imprime a área do triângulo

print(f"A área do triângulo com uma base que mede {b}X e uma altura {h}X, é de {area: .2f}X.")