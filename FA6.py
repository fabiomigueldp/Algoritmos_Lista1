print("     Olá! Bem vindo ao programa ineficiente de calculo da conta do almoço, para calcular o valor do seu")
print("almoço de forma ineficiente, siga as seguintes instruções:")
suco = float(input("Insira o valor do custo de seu suco: "))
main = float(input("Insira o valor do custo de seu prato principal: "))
sobremesa = float(input("Insira o valor do custo de sua sobremesa: "))
totalsc = suco + main + sobremesa
total = (suco + main + sobremesa) * 1.1
print(f"Ótimo! sua refeição lhe custará R${totalsc: .2f}, com o acréscimo de 10% da taxa de serviço, o(a) Sr(a) deve R${total: .2f}.")