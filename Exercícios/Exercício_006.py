# @title Teste de Condição
# Verifique se o número é divisivel por 3 e por 5, 

print("Inicio do programa /n")

numero = int(input("Digite o número"))

# Atenção o Python precisa estar alinhado o if com o else e a condição fica deslocada
#Exemplo:
#if função:
#   print("true") --> atente que o print esta deslocado a direita do if
#else:
#   print("false") --> atente que o print esta deslocado a direita do else

if numero % 3 == 0 and numero % 5 == 0:  

  print(f"O número {numero} é divisível por 3 e 5")

else:

  print(f"O número {numero} não é divisível por 3 e 5")
