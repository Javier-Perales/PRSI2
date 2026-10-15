import csv

with open("notas_corte.csv", mode="r", encoding="utf-8") as fichero:
    lector = csv.reader(fichero, delimiter=";")
    for nombre, siglas, carrera, nota in lector:
        print(f"{nombre:<40} {siglas:^8} {carrera[:50]:<55} {float(nota.replace(',','.')):>8.2f}")
