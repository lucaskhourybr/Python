# @title Exercício 012 - Estrutura de decisão aninhada com elif
# Crie um programa que pede um número ao usuário e retorna se ele é positivo , negativo ou zero.

print("Inicio do programa \n")
print("Bem vindo ao nosso programa , irei verificar se o valor inserido é positivo , negativo ou zero.\n")

valor = float(input("Digite um número \n"))

if valor == 0:
    print(f"O valor inserido foi {valor} , logo ele é ZERO \n")


elif valor > 0:
    print(f"O valor inserido foi {valor} , logo ele é POSITIVO \n")

else:

    print(f"O valor inserido foi {valor} , logo ele é NEGATIVO \n") 


print(f"|-------------------------------------------------|")
print(f"|---------------Fim programa ---------------------|")
print(f"|---------Denvolvido por LucasKhoury--------------|")
print(f"|-------------------------------------------------|")
