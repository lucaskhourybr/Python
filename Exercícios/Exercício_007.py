# @title Estrutura de decisão aninhada
# Exemplo de estrutura de decisão aninhada
# Formatação de casas decimais
# Crie um programa que calcule o valor que sera pago pelo serviço cobrado em minutos , considerando que 
# Se for menor que 200 minutos ira pagar R$0.20 , menor que 400 minutos R$0.18 , maior que 400 ou qualquer valor R$0.15 

print("Inicio do programa \n")

minutos = int(input("Quantos minutos voce usou nesse mês? \n"))


if minutos <= 200:  

  preco = 0.20
  print(f"Você vai pagar este mês , consido o minuto á R${preco}, o valor R$ {minutos * preco:.2f}.")
  
else:
  if minutos < 400:
    preco = 0.18
    print(f"Você vai pagar este mês , consido o minuto á R${preco}, o valor R$ {minutos * preco:.2f}.")

  else:
    preco = 0.15
    print(f"Você vai pagar este mês , consido o minuto á R${preco}, o valor R$ {minutos * preco:.2f}.")
