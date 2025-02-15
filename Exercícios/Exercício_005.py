# @title Estruturas de Decisão
# Crie uma variavel salario e atribua um valor numerico a ela.
# Verifique se o salario e maior que 1000 e menor que 3700 ao mesmo tempo e exiba a mensagem correspondendete


print("Programa para verificar se o salário esta entre R$1000 e R$3700\n")


salario = float(input("Digite o valor do salário : \n")) 


print(f"Você digitou que o seu salário é R$ {salario} \n ")

if (salario >= 1000 and salario <= 3700):
    print(f"Seu salário está entre R$1000.00 e R$3700.00 \n")

else:
    print(f"Seu salário não está entre R$1000.00 e R$3700.00 \n")


print(f" |-------------------------------------------------|")
print(f" |---------------Fim programa ---------------------|")
print(f" |---------Denvolvido por LucasKhoury--------------|")
print(f" |-------------------------------------------------|")
