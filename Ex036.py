#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, 
# o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print ("Bem vindo ao empréstimos bancáros!")
casa = float(input("Informe o valor do imóvel: "))
salário = float(input("Informe o seu salário bruto: "))
anos_financiamento = int(input("E com quantos anos você pretende pagar? "))

prestação = casa / (anos_financiamento * 12)

if prestação > salário * 0.3:
    print ("A prestação do financiamento excede os 30% do salário bruto. Empréstimo NEGADO!!")
else:
    print("Emprestimo APROVADO!")
    print(f"A prestação será de R$ {prestação:.2f}")

