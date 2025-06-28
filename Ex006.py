#Desafio: Caixa Eletrônico Simples
#Crie um programa que:
#Mostra um menu com as opções:
#1 - Ver saldo
#2 - Depositar
#3 - Sacar
#0 - Sair
#Usa um while para repetir o menu até o usuário escolher a opção 0.
#Comece com saldo = 0. Toda vez que o usuário:
#Depositar: adicione ao saldo
#Sacar: subtraia do saldo somente se houver saldo suficiente
#Exiba mensagens adequadas como "Saldo insuficiente", "Depósito realizado", etc.

print(" ====Menu====")
print(" 1 - Ver saldo \n 2 - Depositar \n 3 - Sacar \n 0 - Sair ")

saldo = 0.0
while True:
    opção = input("Digite uma opção: ")
    if opção == "1":
        print (" Seu saldo é de R$ {} .".format(saldo))
    elif opção == "2":
        deposito = float(input("Quanto você poderia de depositar? "))
        saldo += deposito # '' += '' é o mesmo que '' saldo = saldo + saque'' so que mais curto
    elif opção == "3":
        saque = float(input("Quanto você gostaria de sacar? "))
        if saque > saldo:
            print ("Saque maior que saldo!")
        else:
            saque - saldo
            print ("Saque efetuado com sucesso!")
    elif opção == "0":
        print ("Você escolheu sair")
        break
    else:
        print ("Opção inválida!")
