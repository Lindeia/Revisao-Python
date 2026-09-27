# EX071 - Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS considere que o caixa possui cédulas de R$100, R$50, R$20, R$10 e R$5 e R$2.

#Para deixar o visual bonito
print('=' * 30)
print('{:^30}'.format('Linna Banks'))
print('=' * 30)

#Inserção de dados
valor = int(input('Qual valor você gostaria de sacar? R$ '))
total = valor
cédula = 100
TotalCed = 0

#Se o usuário digitar valor inválido 1 ou 3 que são ''impossíveis'' de sacar/sair
while valor != 0 and (valor == 1 or valor == 3):
    print('Valor inválido para saque.')
    valor = int(input('Digite outro valor ou 0 para sair: R$ '))

if valor == 0:
    print('Operação cancelada.')
else:
    total = valor
    cédula = 100
    TotalCed = 0

#Inicio do código
    while True:
        if total >= cédula:
            total -= cédula
            TotalCed += 1
        else:
            if TotalCed > 0:
                print (f'Total de {TotalCed} cédulas de R$: {cédula}')
            if cédula == 100:
                cédula = 50
            elif cédula == 50:
                cédula = 20
            elif cédula == 20:
                cédula = 10
            elif cédula == 10:
                cédula = 5
                if total % 2 == 0:
                    cédula = 2
            TotalCed = 0
            if total == 0:
                break


print('=' * 30)
print ('Volte sempre ao Linna Banks!!')
