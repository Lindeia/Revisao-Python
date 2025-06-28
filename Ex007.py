#Pedir ao usuário que crie uma senha.
#Depois, entra num loop onde o usuário deve digitar a senha corretamente para acessar o sistema.
#Se a senha estiver incorreta, mostre: "Senha incorreta. Tente novamente."
#Quando a senha for digitada corretamente, mostre: "Acesso permitido!" e finalize o programa.

senha = int(input("Crie uma senha: "))
print("Senha criada com sucesso!!")

while True:
    tentativa = int(input("Digite sua senha: "))

    if tentativa == senha:
        print("Senha digitada corretamente!")
        break
    else:
        print("Senha incorreta. Tente novamente!")
