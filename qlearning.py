
import os
from time import sleep
from random import randint

size = 6

def nuevo_estado(estado_actual, accion_aplicar):
    n_estado = estado_actual + acciones[accion_aplicar]
    if n_estado < 0:
        return n_estado+(size*size)
    elif n_estado > (size*size)-1:
        return n_estado-(size*size)
    return n_estado

def mostrarMundo(estado):
    sleep(1)
    os.system('cls')
    for i in range(0, (size*size)):
        if i%size == 0:
            print()
        if estado == i:
            print('\U0001F47E', end="") # AGENTE
        elif mundo[i] == 100:
            print('\U0001F4AF', end="") # META
        elif mundo[i] == -100:
             print('\U0001F525', end="") # MUERTE
        else:
          print('\U00002B1C', end="") # CASILLA VACIA
    print()

def printqtable(q_table):
    print('#'*43)
    print(f"E/A  | {acciones_emo[0]:^7} | {acciones_emo[1]:^7} | {acciones_emo[2]:^7} | {acciones_emo[3]:^7}")
    for indice, rewards in enumerate(q_table):
        print(indice, end="    | ")
        for reward in rewards:
            numero = f"%.2f" % reward
            print(f"{numero:>7}", end=" | ")
        print()
    print('#'*43)

mundo = [-100,   -1,  100, -100, -100, -1,
           -1,   -1, -100, -1, -100, -1,
         -100, -100,   -1, -1, -1, -1,
         -100,   -1,   -1, -1, -1, -100,
         -100,   -1, -100, -1, -100, -1,
         -100, -100,   -1, -100, -1, -1,
         ]

ARRIBA = -size
ABAJO = size
IZQ = -1
DER = 1
acciones = {
    0 : ARRIBA,
    1 : ABAJO,
    2 : IZQ,
    3 : DER
}

acciones_emo = {
    0 : '\U00002B06',
    1 : '\U00002B07',
    2 : '\U00002B05',
    3 : '\U000027A1'
}

q_table = []
for i in range((size*size)):
    q_table.append([0, 0, 0, 0])

#printqtable(q_table)

factor_aprendizaje = 0.8
razon_descuento = 0.3

episodios = 30000
for _ in range(episodios):
    estado = 25
    fin = False
    while not fin:
        #printqtable(q_table)
        if randint(1, 10) < 3:
            maximo = max(q_table[estado])
            accion = q_table[estado].index(maximo)
        else:
            accion = randint(0, 3)
        n_estado = nuevo_estado(estado, accion)
        recompensa = mundo[n_estado]
        #print(f'Estado actual: {estado}, Estado Nuevo: {n_estado}, Accion {accion}, Recompensa anterior: {mundo[estado]}, Recompensa nueva: {recompensa}')
        q_table[estado][accion] = q_table[estado][accion] + factor_aprendizaje * ( recompensa + razon_descuento * max(q_table[n_estado]) - q_table[estado][accion])
        estado = n_estado
        if estado == 2 or recompensa==-100:
            fin = True
        #input()

printqtable(q_table)

estado = 25
fin = False
while not fin:
    
    mostrarMundo(estado)
    #input()
    maximo = max(q_table[estado])
    accion = q_table[estado].index(maximo)
    n_estado = nuevo_estado(estado, accion)
    print(f'Estado actual: {estado},  Accion {acciones_emo[accion]}, Estado Nuevo: {n_estado}')
    estado = n_estado
    if estado == 2:
        fin = True
    sleep(1)

    
mostrarMundo(estado)
print(f'Estado actual: {estado},  Accion {acciones_emo[accion]}, Estado Nuevo: {n_estado}')
