###Atividade 3
Salario = float(input("Digite o seu salário: "))

ir = Salario * 0.11
inss = Salario * 0.08
sindicato = Salario * 0.05
salario_liq = Salario - ir - inss - sindicato

print(f"Salário Bruto: R$ {Salario}")
print(f"IR (11%): R$ {ir}")
print(f"INSS (8%): R$ {inss}")
print(f"Salário Líquido: R$ {salario_liq}")