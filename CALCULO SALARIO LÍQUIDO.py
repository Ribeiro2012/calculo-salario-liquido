ganho_hora = float (input("Digite quanto você ganha por hora: R$"))
horas_trab = int (input("Quantas horas trabalhadas no mês?: "))
salario_bruto = ganho_hora * horas_trab
ir = (salario_bruto / 100) * 11
inss = (salario_bruto / 100) * 8
sindicato = (salario_bruto / 100) * 5
salario_liquido = salario_bruto - ir - inss - sindicato

print (f"Salário Bruto: R${salario_bruto}")
print (f"IR (11%): R${ir}")
print (f"INSS (8%): R${inss}")
print (f"Sindicato (5%): R${sindicato}")
print (f"Salário Líquido: R${salario_liquido}")