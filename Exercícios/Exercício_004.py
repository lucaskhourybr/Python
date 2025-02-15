# @title Estruturas de Decisão
# Crie duas variaveis nota1 e nota2 e atribua valores numeros a ela.
# Verifique se a media das notas e maior ou igual a 7
# imprima aprovado ou reprovado de acordo com a condição


print("Programa para verificar a média do aluno e se ele esta aprovado.\n")


nota1 = float(input("Digite a nota 1 : \n")) 
nota2 = float(input("Digite a nota 2 : \n"))

media = (nota1 + nota2)/2


print(f"Você digitou que a nota 01 é {nota1} e a nota2 é {nota2} \n ")
print(f"Logo sua média é {media} \n ")

if (media == 10):
    print("Parabéns , você foi aprovado com a nota MÁXIMA \n")

if (media >= 7 and media < 10):
    print("Então Parabéns , você foi aprovado \n")

if (media  >= 1 and media < 7):
    print("Então Infelizmente, Você foi reprovado \n")

if (media < 1):
    print("Ai você não entendeu nada da matéria , estude mais \n")



print(f" |-------------------------------------------------|")
print(f" |---------------Fim programa ---------------------|")
print(f" |---------Denvolvido por LucasKhoury--------------|")
print(f" |-------------------------------------------------|")
