import math

print("Olá! Bem vindo ao programa de aritmética, siga as instruções a seguir para ler análises de diferentes relações entre elementos a e b")
a = int(input("Insira um número inteiro para representar o elemento A: "))
b = int(input("Insira um número inteiro para representar o elemento B: "))
soma = a + b
diferenca = a - b
produto = a * b
quociente = a // b
resto = a % b
log = (math.log10(a))
potencia = a**b
print(f"a + b = {soma}")
print(f"a - b = {diferenca}")
print(f"a * b = {produto}")
print(f"a / b = {quociente}")
print(f"Resto de a / b = {resto}")
print(f"Log de base 10 de a = {log}")
print(f"a ^ b = {potencia}")
