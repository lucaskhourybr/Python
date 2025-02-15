# @title Exercício 011 - Estrutura de decisão aninhada com elif
# Crie um programa que pede a nota do aluno e informa se esta aprovado em recuperação ou reprovado.
# A regra para a aprovação é nota maior ou igual a 7 : >=7.
# Reprovação menor ou igual a 5 : <=5
# Em recuperação com nota maior que 5 e menor 7 : >5 and <7


print("Inicio do programa \n")
print("Bem vindo ao nosso programa , irei verificar se você foi APROVADO , REPROVADO ou RECUPERAÇÃO.\n")

nota = float(input("Digite a sua nota \n"))

if nota >10 or nota < 0:
    print("###### Nota inválida ##### \n")
    print("Digite um valor entre 0 á 10. \n")

elif nota >= 7:
    print(f" Você tirou {nota} , logo você está APROVADO !\n")

elif nota <= 5:

    print(f" Você tirou {nota} , logo você está REPROVADO !\n") 

elif nota > 5 and nota < 7:
    print(f" Você tirou {nota} , logo você está de RECUPERAÇÃO !\n")

print(f"|-------------------------------------------------|")
print(f"|---------------Fim programa ---------------------|")
print(f"|---------Denvolvido por LucasKhoury--------------|")
print(f"|-------------------------------------------------|")
