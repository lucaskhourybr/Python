# @title Exercício 20 - Estrutura de repetição FOR aqui vamos repetir uma quantidade vezes 
# Programa super Mercado
# Criar uma variavel tolalcompra = 0
# Criar variaveis para cada produto , feijão , arroz , macarrão.
# Inicializar com os valores de cada
# solicitar o código do produto
# testar e adiconar seu valor ao total da compra
# exibir o produto

totalcompra = 0
feijao = 5.00
arroz = 10.00
macarrao = 4.00


print("Inicio do programa \n")
print("Bem vindo ao nosso SUPER MERCADO.\n")

for contador in range(3):

  print("Digite o produto que você quer comprar , escolha 3 produtos.\n")  
  produto = (input("Feijao , Macarrao ,Arroz ou Finalizar.\n")).lower()

  if produto == "feijao":
    totalcompra += feijao  # mesma coisa que totalcompra = feijao + totalcompra
    print(f"\n O valor da sua compra até agora está em R$ {totalcompra} \n")

  if produto == "macarrao":
    totalcompra += macarrao 
    print(f"\n O valor da sua compra até agora está em R$ {totalcompra} \n")

  if produto == "arroz":
    totalcompra += arroz  
    print(f"\n O valor da sua compra até agora está em R$ {totalcompra} \n")
  

print(f"\n O valor da sua compra ficou em R$ {totalcompra}\n")

print(f"|-------------------------------------------------|")
print(f"|---------------Fim programa ---------------------|")
print(f"|---------Denvolvido por LucasKhoury--------------|")
print(f"|-------------------------------------------------|")
