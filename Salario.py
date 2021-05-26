salario = int(input("Qual o seu salário mensal ? "))
if salario <= 280: #salários até R$ 280,00 (incluindo) : aumento de 20%
         aumento = salario * 0.2 
         new_sala = salario + aumento
         percentual = "20%"
elif salario > 280 and salario <= 700: #salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
         aumento = salario * 0.15
         new_sala = salario + aumento
         percentual = "15%"
elif salario >= 700  and salario <= 1500: #salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        aumento = salario * 0.1
        new_sala = salario + aumento
        percentual = "10%"
elif salario > 1500: #salários de R$ 1500,00 em diante : aumento de 5%
        aumento = salario * 0.05
        new_sala = salario + aumento
        percentual = "5%"
print("Salário informado = ", salario, "percentual a soma", percentual)
print("Aumento = ", aumento)
print ("O seu salario mudou para:", new_sala)
