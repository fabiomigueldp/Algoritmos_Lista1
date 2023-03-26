print("   Olá! Bem vindo ao programa de cálculo de resultados de investimentos que rendem 12%a.a")
print("pelos próximos 3 anos, com uma precisão de duas casa decimais!")
value = float(input("Insira o valor inicial de seu investimento: R$"))
a1 = float(value*1.12)
r1 = a1 - value
a2 = float(a1*1.12)
r2 = a2 - a1
a3 = float (a2*1.12)
r3 = a3 - a2
rt = a3 - value
print(f"No primeiro ano, seu investimento renderá R${r1: .2f}, o valor total de seu investimento será de R${a1: .2f}.")
print(f"No segundo ano, seu investimento renderá R${r2: .2f}, o valor total de seu investimento será de R${a2: .2f}.")
print(f"No terceiro ano, seu investimento renderá R${r3: .2f}, o valor total de seu investimento será de R${a3: .2f}.")
print(f"Passados os três anos, o seu investimento terá um rendimento total de R${rt: .2f}")
