# EX071 - Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 30)
print('{:^30}'.format('Linna Banks'))
print('=' * 30)

valor = int(input('Qual valor você gostaria de sacar? R$ '))
total = valor
cédula = 50
TotalCed = 0
while True:
    if total >= cédula:
        total -= cédula
        TotalCed += 1
    else:
        if TotalCed > 0:
            print (f'Total de {TotalCed} cédulas de R$: {cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        TotalCed = 0
        if total == 0:
            break

print('=' * 30)
print ('Volte sempre ao Linna Banks!!')
