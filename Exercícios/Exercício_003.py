# @title Operadores Relacionais
# ==                    ------> igual
# > , >= , < , <=       ------>  menor, menor igual , maior ,maior igual
# !=                    ------> diferente
# &&                    ------> And (E)
# ||                    ------> Or  (ou)
# !                     ------> not (não)

print("Inicio do programa \n")
print("Bem vindo ao nosso programa , você devera inserir 2 números quando solicitado e ele ira dizer aonde este número se aplica.\n")
valor1 = int(input("Digite o número do valor 1 \n"))
valor2 = int(input("Digite o número do valor 2 \n"))

igualdade = (valor1 == valor2) # Valor 1 é igual a Valor 2 ?
print(f"{valor1} é igual a {valor2} ?")
print(igualdade,"\n")

menor = (valor1 < valor2)  # Valor 1 é menor que o Valor 2 ?
print(f"{valor1} é menor que {valor2} ?")
print(menor,"\n")

maior = (valor1 > valor2) # Valor 1 é maior que o Valor 2 ?
print(f"{valor1} é maior que {valor2} ?")
print(maior,"\n")

menorigual = (valor1 <= valor2) # Valor 1 é menor ou igual que o Valor 2 ?
print(f"{valor1} é menor ou igual a {valor2} ?")
print(menorigual,"\n")

maiorigual = (valor1 >= valor2)  # Valor 1 é maior ou igual que o Valor 2 ?
print(f"{valor1} é maior ou igual a {valor2} ?")
print(maiorigual,"\n") 

diferente = (valor1 != valor2)  # Valor 1 é diferente do Valor 2 ?
print(f"{valor1} é diferente de {valor2} ?")
print(diferente,"\n")


print(f"|-------------------------------------------------|")
print(f"|---------------Fim programa ---------------------|")
print(f"|---------Denvolvido por LucasKhoury--------------|")
print(f"|-------------------------------------------------|")
