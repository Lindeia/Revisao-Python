# Perguntar o valor total da compra
# O cliente informa os valores que está pagando (pode ser em partes)
# Enquanto o valor pago for menor que o valor da compra, continuar pedindo mais dinheiro
# Quando o total pago for igual ou maior, exibir:
# "Pagamento finalizado sem troco" se for exato
# "Troco a ser devolvido: R$ x" se sobrar dinheiro
# O pagamento só pode ser feito de uma vez (ou seja, valor pago tem que ser ≥ valor da compra na primeira tentativa).
# Se o valor for menor, mostrar mensagem de erro e pedir novamente.
# Quando o valor for suficiente, finalizar e mostrar o troco (se houver).


print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Bem vindo ao supermercado Low Code")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

valor_da_compra = (float(input("Informe o valor da sua compra: R$  ")))
valor_pago = 0

while valor_pago < valor_da_compra:
    pagamento = float(input("Informe o valor a ser pago: R$ "))
    valor_pago += pagamento
    print (" Pagamento parcial efetuado! Saldo insuficiente! Você digitou o valor R$ {} e sua compra foi de R$ {}. Faltam R$ {} ".format(valor_da_compra, valor_pago, valor_da_compra - valor_pago))

if valor_pago == valor_da_compra:
    print("Pagamento finalizado sem troco.")
else:
    troco = valor_pago - valor_da_compra
    print(f"Pagamento finalizado. Troco a ser devolvido: R$ {troco:.2f}")

