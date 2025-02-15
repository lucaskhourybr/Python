# @title Exercício 008 - Estrutura de decisão com if apenas
# Crie um programa que escolha a categoria do produto e traga o preço dela.
# Categoria 1 = R$10 , 2 = R$18 , 3 = R$23 , 4 = R$26 e 5 = R$31

print("Inicio do programa \n")
print("Bem vindo ao nosso programa , irei mostrar as categorias que temos escolha uma.\n")
print("1 - Categoria 1 | 2 - Categoria 2 | 3 - Categoria 3 | 4 - Categoria 4 | 5 - Categoria 5 \n")
categoria = int(input("Digite o número da categoria \n"))

if categoria == 1:
    preco = 10
    print(f"O valor da categoria categoria 1 é de R${preco} \n")

if categoria == 2:
    preco = 18
    print(f"O valor da categoria categoria 2 é de R${preco} \n")    

if categoria == 3:
    preco = 23
    print(f"O valor da categoria categoria 3 é de R${preco} \n")

if categoria == 4:
    preco = 26
    print(f"O valor da categoria categoria 4 é de R${preco} \n")

if categoria == 5:
    preco = 31
    print(f"O valor da categoria categoria 5 é de R${preco} \n")

if categoria != 1 and categoria != 2 and categoria != 3 and categoria != 4 and categoria != 5:
    print("Categoria não encontrada \n")

print(f"|-------------------------------------------------|")
print(f"|---------------Fim programa ---------------------|")
print(f"|---------Denvolvido por LucasKhoury--------------|")
print(f"|-------------------------------------------------|")
