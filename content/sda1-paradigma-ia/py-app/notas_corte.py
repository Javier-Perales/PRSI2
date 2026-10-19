import csv

def crear_grado(grado):
    grado[3]= float(grado[3].replace(',','.'))
    return (grado)
    
def cargar_csv():
    with open("notas_corte.csv", mode="r", encoding="utf-8") as fichero:
        lector = csv.reader(fichero, delimiter=";")
        for fila in lector:
            fila[3] = float (fila[3].replace(',','.'))
            print(fila)

grados= []
cargar_csv()


opc=' '
while (opc!='0'):
    print('='*50)
    print(f"{'ORIENTADOR UNIVERSITARIO':^50}")
    print('='*50)
    print(f"{'1. Mostrar todas las titulaciones':<50}")
    print(f"{'2. Buscar por Universidad':<50}")
    print(f"{'3. Buscar por nombre de grado':<50}")
    print(f"{'4. Filtrar por nota de admisión':<50}")
    print(f"{'0. Salir':<50}")
    opc=input('Introduce opción: ')
    match opc:
        case '1': 
            print("Has pulsado la opción 1")
        case '2':
            print("Has pulsado la opción 2")
        case '3':
            print("Has pulsado la opción 3")
        case '4':
            print("Has pulsado la opción 4")
        case '0':
            print("Hasta pronto")
        case _:
            print("Opción incorrecta")
        

    





        