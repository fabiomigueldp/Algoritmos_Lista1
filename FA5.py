print("Bem vindo ao programa de reciclagem, para resgatar seus créditos, siga as seguintes instruções:")
pequenos = float(input("insira o número de recipientes de até 1 litro de volume que serão reciclados: "))
grandes = float(input("insira o número de recipientes com volume maior do que 1 litro que serão reciclados: "))
valorpequenos = pequenos * 0.10
valorgrandes = grandes * 0.25
credit = valorpequenos + valorgrandes
print(f"Você recebeu R${credit:.2f} em cŕeditos por sua reciclagem!")