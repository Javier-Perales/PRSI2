import random
from collections import deque
from PIL import Image, ImageDraw


# ============================================================
# CONFIGURACIÓN
# ============================================================

ANCHO = 480
ALTO = 360

MURO = 8
PASILLO = 32

COLUMNAS = 12
FILAS = 9

COLOR_FONDO = "white"
COLOR_MURO = "black"
COLOR_SALIDA = "#00C853"

ARCHIVO_PNG = "laberinto_scratch.png"
ARCHIVO_SVG = "laberinto_scratch.svg"


# ============================================================
# REPRESENTACIÓN DEL LABERINTO
# ============================================================

# Cada celda guarda las paredes que conserva:
# N = norte
# S = sur
# E = este
# O = oeste

laberinto = []

for fila in range(FILAS):
    nueva_fila = []

    for columna in range(COLUMNAS):
        nueva_fila.append({
            "N": True,
            "S": True,
            "E": True,
            "O": True
        })

    laberinto.append(nueva_fila)


# ============================================================
# CELDA INICIAL
# ============================================================

# En una cuadrícula 8x6 no existe una única celda central.
# Elegimos una de las cuatro centrales.

inicio_col = COLUMNAS // 2 - 1
inicio_fila = FILAS // 2 - 1

INICIO = (inicio_col, inicio_fila)


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def vecinos_no_visitados(col, fila, visitadas):
    vecinos = []

    if fila > 0 and (col, fila - 1) not in visitadas:
        vecinos.append(("N", col, fila - 1))

    if fila < FILAS - 1 and (col, fila + 1) not in visitadas:
        vecinos.append(("S", col, fila + 1))

    if col > 0 and (col - 1, fila) not in visitadas:
        vecinos.append(("O", col - 1, fila))

    if col < COLUMNAS - 1 and (col + 1, fila) not in visitadas:
        vecinos.append(("E", col + 1, fila))

    return vecinos


def eliminar_pared(col1, fila1, col2, fila2, direccion):

    if direccion == "N":
        laberinto[fila1][col1]["N"] = False
        laberinto[fila2][col2]["S"] = False

    elif direccion == "S":
        laberinto[fila1][col1]["S"] = False
        laberinto[fila2][col2]["N"] = False

    elif direccion == "O":
        laberinto[fila1][col1]["O"] = False
        laberinto[fila2][col2]["E"] = False

    elif direccion == "E":
        laberinto[fila1][col1]["E"] = False
        laberinto[fila2][col2]["O"] = False


# ============================================================
# GENERACIÓN DEL LABERINTO
# Algoritmo Recursive Backtracker / DFS
# ============================================================

def generar_laberinto():

    visitadas = set()

    pila = [INICIO]
    visitadas.add(INICIO)

    while pila:

        col, fila = pila[-1]

        vecinos = vecinos_no_visitados(
            col,
            fila,
            visitadas
        )

        if vecinos:

            direccion, nueva_col, nueva_fila = random.choice(vecinos)

            eliminar_pared(
                col,
                fila,
                nueva_col,
                nueva_fila,
                direccion
            )

            visitadas.add((nueva_col, nueva_fila))

            pila.append((nueva_col, nueva_fila))

        else:
            pila.pop()


# ============================================================
# BUSCAR LA SALIDA MÁS LEJANA
# ============================================================

def vecinos_accesibles(col, fila):

    vecinos = []

    celda = laberinto[fila][col]

    if not celda["N"]:
        vecinos.append((col, fila - 1))

    if not celda["S"]:
        vecinos.append((col, fila + 1))

    if not celda["O"]:
        vecinos.append((col - 1, fila))

    if not celda["E"]:
        vecinos.append((col + 1, fila))

    return vecinos


def buscar_salida():

    cola = deque()

    cola.append((INICIO, 0))

    visitadas = {INICIO}

    candidatos = []

    while cola:

        (col, fila), distancia = cola.popleft()

        # ¿Está esta celda en el borde?

        if (
            col == 0
            or col == COLUMNAS - 1
            or fila == 0
            or fila == FILAS - 1
        ):
            candidatos.append(
                (distancia, col, fila)
            )

        for vecino in vecinos_accesibles(col, fila):

            if vecino not in visitadas:

                visitadas.add(vecino)

                cola.append(
                    (vecino, distancia + 1)
                )

    # Ordenamos de mayor a menor distancia
    candidatos.sort(reverse=True)

    # Escogemos aleatoriamente entre los 3 más lejanos.
    # Así el laberinto cambia ligeramente en cada ejecución.

    mejores = candidatos[:3]

    distancia, col, fila = random.choice(mejores)

    # Decidimos por qué pared exterior saldrá

    posibilidades = []

    if fila == 0:
        posibilidades.append("N")

    if fila == FILAS - 1:
        posibilidades.append("S")

    if col == 0:
        posibilidades.append("O")

    if col == COLUMNAS - 1:
        posibilidades.append("E")

    direccion = random.choice(posibilidades)

    return col, fila, direccion, distancia


# ============================================================
# CÁLCULO DE LA POSICIÓN DEL LABERINTO
# ============================================================

ANCHO_LABERINTO = (
    COLUMNAS * PASILLO
    + (COLUMNAS + 1) * MURO
)

ALTO_LABERINTO = (
    FILAS * PASILLO
    + (FILAS + 1) * MURO
)


OFFSET_X = (ANCHO - ANCHO_LABERINTO) // 2
OFFSET_Y = (ALTO - ALTO_LABERINTO) // 2


def posicion_celda(col, fila):

    x = OFFSET_X + MURO + col * (PASILLO + MURO)

    y = OFFSET_Y + MURO + fila * (PASILLO + MURO)

    return x, y


# ============================================================
# GENERAR IMAGEN PNG
# ============================================================

def generar_png(salida):

    imagen = Image.new(
        "RGB",
        (ANCHO, ALTO),
        COLOR_FONDO
    )

    dibujo = ImageDraw.Draw(imagen)

    # --------------------------------------------------------
    # Dibujar paredes
    # --------------------------------------------------------

    for fila in range(FILAS):

        for col in range(COLUMNAS):

            x, y = posicion_celda(col, fila)

            celda = laberinto[fila][col]

            # Norte

            if celda["N"]:
                dibujo.rectangle(
                    [
                        x - MURO,
                        y - MURO,
                        x + PASILLO + MURO - 1,
                        y - 1
                    ],
                    fill=COLOR_MURO
                )

            # Sur

            if celda["S"]:
                dibujo.rectangle(
                    [
                        x - MURO,
                        y + PASILLO,
                        x + PASILLO + MURO - 1,
                        y + PASILLO + MURO - 1
                    ],
                    fill=COLOR_MURO
                )

            # Oeste

            if celda["O"]:
                dibujo.rectangle(
                    [
                        x - MURO,
                        y - MURO,
                        x - 1,
                        y + PASILLO + MURO - 1
                    ],
                    fill=COLOR_MURO
                )

            # Este

            if celda["E"]:
                dibujo.rectangle(
                    [
                        x + PASILLO,
                        y - MURO,
                        x + PASILLO + MURO - 1,
                        y + PASILLO + MURO - 1
                    ],
                    fill=COLOR_MURO
                )

    # --------------------------------------------------------
    # Abrir y colorear salida
    # --------------------------------------------------------

    col, fila, direccion, distancia = salida

    x, y = posicion_celda(col, fila)

    if direccion == "N":

        dibujo.rectangle(
            [
                x,
                OFFSET_Y,
                x + PASILLO - 1,
                OFFSET_Y + MURO - 1
            ],
            fill=COLOR_SALIDA
        )

    elif direccion == "S":

        dibujo.rectangle(
            [
                x,
                ALTO - OFFSET_Y - MURO,
                x + PASILLO - 1,
                ALTO - OFFSET_Y - 1
            ],
            fill=COLOR_SALIDA
        )

    elif direccion == "O":

        dibujo.rectangle(
            [
                OFFSET_X,
                y,
                OFFSET_X + MURO - 1,
                y + PASILLO - 1
            ],
            fill=COLOR_SALIDA
        )

    elif direccion == "E":

        dibujo.rectangle(
            [
                ANCHO - OFFSET_X - MURO,
                y,
                ANCHO - OFFSET_X - 1,
                y + PASILLO - 1
            ],
            fill=COLOR_SALIDA
        )

    imagen.save(ARCHIVO_PNG)

    print(
        f"PNG generado: {ARCHIVO_PNG}"
    )


# ============================================================
# GENERAR SVG
# ============================================================

def generar_svg(salida):

    elementos = []

    elementos.append(
        f'''
<svg
    xmlns="http://www.w3.org/2000/svg"
    width="{ANCHO}"
    height="{ALTO}"
    viewBox="0 0 {ANCHO} {ALTO}">
'''
    )

    elementos.append(
        f'<rect width="{ANCHO}" height="{ALTO}" fill="{COLOR_FONDO}"/>'
    )

    # --------------------------------------------------------
    # Paredes
    # --------------------------------------------------------

    for fila in range(FILAS):

        for col in range(COLUMNAS):

            x, y = posicion_celda(col, fila)

            celda = laberinto[fila][col]

            if celda["N"]:
                elementos.append(
                    f'<rect x="{x-MURO}" y="{y-MURO}" '
                    f'width="{PASILLO + 2*MURO}" '
                    f'height="{MURO}" '
                    f'fill="{COLOR_MURO}"/>'
                )

            if celda["S"]:
                elementos.append(
                    f'<rect x="{x-MURO}" y="{y+PASILLO}" '
                    f'width="{PASILLO + 2*MURO}" '
                    f'height="{MURO}" '
                    f'fill="{COLOR_MURO}"/>'
                )

            if celda["O"]:
                elementos.append(
                    f'<rect x="{x-MURO}" y="{y-MURO}" '
                    f'width="{MURO}" '
                    f'height="{PASILLO + 2*MURO}" '
                    f'fill="{COLOR_MURO}"/>'
                )

            if celda["E"]:
                elementos.append(
                    f'<rect x="{x+PASILLO}" y="{y-MURO}" '
                    f'width="{MURO}" '
                    f'height="{PASILLO + 2*MURO}" '
                    f'fill="{COLOR_MURO}"/>'
                )

    # --------------------------------------------------------
    # Salida
    # --------------------------------------------------------

    col, fila, direccion, distancia = salida

    x, y = posicion_celda(col, fila)

    if direccion == "N":

        salida_x = x
        salida_y = OFFSET_Y
        salida_w = PASILLO
        salida_h = MURO

    elif direccion == "S":

        salida_x = x
        salida_y = ALTO - OFFSET_Y - MURO
        salida_w = PASILLO
        salida_h = MURO

    elif direccion == "O":

        salida_x = OFFSET_X
        salida_y = y
        salida_w = MURO
        salida_h = PASILLO

    else:

        salida_x = ANCHO - OFFSET_X - MURO
        salida_y = y
        salida_w = MURO
        salida_h = PASILLO

    elementos.append(
        f'''
<rect
    x="{salida_x}"
    y="{salida_y}"
    width="{salida_w}"
    height="{salida_h}"
    fill="{COLOR_SALIDA}"
/>
'''
    )

    elementos.append("</svg>")

    with open(
        ARCHIVO_SVG,
        "w",
        encoding="utf-8"
    ) as archivo:

        archivo.write("\n".join(elementos))

    print(
        f"SVG generado: {ARCHIVO_SVG}"
    )


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

generar_laberinto()

salida = buscar_salida()

generar_png(salida)

generar_svg(salida)


print()
print("Laberinto generado correctamente.")
print(f"Tamaño: {ANCHO} x {ALTO} px")
print(f"Pasillo: {PASILLO} px")
print(f"Muro: {MURO} px")
print(f"Rejilla: {COLUMNAS} x {FILAS}")
print(f"Inicio: {INICIO}")

print(
    "Salida:",
    salida[0],
    salida[1],
    salida[2]
)

print(
    "Distancia desde el inicio:",
    salida[3],
    "celdas"
)