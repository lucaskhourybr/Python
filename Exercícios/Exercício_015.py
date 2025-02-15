# @title Exercício 015 - Estrutura de decisão aninhada com elif
# Crie uma variável "horário" e atribua um valor inteiro
# Representando a hora do dia ( em formato 24 horas)
# Verifique se o horário está dentro do período:
# madrugada ( 0hrs até as 06hrs) 
# manhã ( 6hrs até as 12hrs) 
# tarde ( 12hrs até as 18hrs) 
# noite ( 18hrs até as 24hrs) 
# Exiba a mensagem 


print("Inicio do programa \n")
print("Bem vindo ao nosso programa , para verificação se o horário corresponde á madrugada, manhã, tarde ou noite.\n")

periodo = int(input("Digite um horário entre 0 até 24 \n"))

if periodo >= 0 and periodo <= 6:
   
   print(f"O horário inserido foi {periodo}hrs , logo é de MADRUGADA \n")

elif periodo > 6 and periodo <= 12:

   print(f"O horário inserido foi {periodo}hrs , logo é de MANHÂ \n")

elif periodo > 12 and periodo <= 18:

   print(f"O horário inserido foi {periodo}hrs , logo é de TARDE \n")

elif periodo > 18 and periodo <= 24:

   print(f"O horário inserido foi {periodo}hrs , logo é de NOITE \n")      
   

print(f"|-------------------------------------------------|")
print(f"|---------------Fim programa ---------------------|")
print(f"|---------Denvolvido por LucasKhoury--------------|")
print(f"|-------------------------------------------------|")
