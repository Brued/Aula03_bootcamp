# Exercício 1: Verificação de Qualidade de Dados Você está analisando um conjunto de dados de vendas
# e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. Escreva 
# um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

# quantidade = int(input("Insira a quantidade: "))
# preco = int(input(" Insiea o preço. "))

# if quantidade > 0 and preco > 0:
#     print("Valores válidos!")
# else:
#     print ("Valor inválido!")   

# Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. 
# Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'


temp = float(input ("Valor da temperatura º C: "))

if temp < 18 :
    print (f"A temperatura {temp} é baixa.")
elif  18 <= temp <= 26 :
    print(f"A temperatura {temp} é normal.")
else:
    print (f"A temperatura {temp} é alta.")

