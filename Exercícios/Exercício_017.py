# @title Exercício 017 - Estrutura utilizando a palavra in
# Exemplo letra in ["a,b,c,d,e"] , in é a mesma coisa que é
# Faça um programa que verifica se uma lera é vogal ou consoante

print("Inicio do programa \n")
print("Bem vindo ao nosso programa , para verificação se a letra é vogal ou consoante.\n")

letra = (input("Digite uma letra \n")).lower()  #.lower é uma função para deixar a letra minuscula


if letra in ["a","e","i","o","u"]: # poder utilizar o in quer dizer se a letra for a e i o u é a mesma coisa
   print(f"A letra inserida foi {letra} , logo é uma VOGAL ! \n")

else:
   print(f"A letra inserida foi {letra} , logo é uma CONSOANTE !\n")
