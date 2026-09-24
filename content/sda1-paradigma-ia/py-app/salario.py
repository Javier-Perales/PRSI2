horas=0.0
precio_hora=2.75
salario_bruto=0.0
retencion=0.0
salario_neto=0.0
horas= float(input("Ingrese la cantidad de horas trabajadas: "))
retención= float(input("Ingrese el porcentaje de retención que se aplica: "))
salario_bruto=horas*precio_hora
salario_neto=salario_bruto-(salario_bruto*retención/100)
print("El salario bruto es: ", salario_bruto, "€")
print("El salario neto es: ", salario_neto, "€")
print("Impuestos pagados: ", salario_bruto-salario_neto, " €")