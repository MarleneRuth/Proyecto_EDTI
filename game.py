import random
import os
#TEST ONLY
def iniciar_juego():
    tablero = [[0] * 4 for _ in range(4)]
    agregar_nuevo(tablero)
    agregar_nuevo(tablero)
    return tablero

def agregar_nuevo(tablero):
    celdas_vacias = [(r, c) for r in range(4) for c in range(4) if tablero[r][c] == 0]
    if celdas_vacias:
        r, c = random.choice(celdas_vacias)
        tablero[r][c] = 2 if random.random() < 0.9 else 4

def imprimir_tablero(tablero):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- JUEGO 2048 (Usa: W, A, S, D + Enter) ---")
    for fila in tablero:
        print(f"[{ ' '.join([str(n) if n != 0 else '.' for n in fila]).center(15) }]")

def comprimir(fila):
    nueva_fila = [n for n in fila if n != 0]
    for i in range(len(nueva_fila) - 1):
        if nueva_fila[i] == nueva_fila[i+1]:
            nueva_fila[i] *= 2
            nueva_fila[i+1] = 0
    nueva_fila = [n for n in nueva_fila if n != 0]
    return nueva_fila + [0] * (4 - len(nueva_fila))

def mover(tablero, direccion):
    # W: arriba, S: abajo, A: izquierda, D: derecha
    for i in range(4):
        if direccion in 'AD': # Movimiento Horizontal
            fila = tablero[i]
            if direccion == 'D': fila = fila[::-1]
            nueva = comprimir(fila)
            if direccion == 'D': nueva = nueva[::-1]
            tablero[i] = nueva
        else: # Movimiento Vertical
            columna = [tablero[r][i] for r in range(4)]
            if direccion == 'S': columna = columna[::-1]
            nueva = comprimir(columna)
            if direccion == 'S': nueva = nueva[::-1]
            for r in range(4): tablero[r][i] = nueva[r]

def principal():
    tablero = iniciar_juego()
    while True:
        imprimir_tablero(tablero)
        movimiento = input("Mover: ").upper()
        if movimiento in ['W', 'A', 'S', 'D']:
            copia = [f[:] for f in tablero]
            mover(tablero, movimiento)
            if tablero != copia:
                agregar_nuevo(tablero)
        elif movimiento == 'Q': break

principal()