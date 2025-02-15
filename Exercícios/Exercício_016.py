# @title Exercício 016 - Estrutura de decisão aninhada com elif
# Faça um programa que verifica se uma lera é vogal ou consoante

print("Inicio do programa \n")
print("Bem vindo ao nosso programa , para verificação se a letra é vogal ou consoante.\n")

letra = (input("Digite uma letra \n")).lower()  #.lower é uma função para deixar a letra minuscula


if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
   print(f"A letra inserida foi {letra} , logo é uma VOGAL ! \n")

else:
   print(f"A letra inserida foi {letra} , logo é uma CONSOANTE !\n")
