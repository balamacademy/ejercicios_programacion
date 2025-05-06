---
marp: false
theme: default
paginate: true
class: lead
backgroundColor: #ffffff
---

# 🕹️ Proyecto: Juego del Gato (Tres en Línea)

### Programación Estructurada en C++

---

## 🎯 Objetivo

Desarrollar un juego interactivo en C++ para dos jugadores, usando:

- Matrices bidimensionales (`3x3`)
- Funciones
- Lógica de control y flujo

---

## 🧠 ¿Cómo funciona?

- Dos jugadores se turnan para marcar celdas (0 a 8).
- El primero en alinear 3 símbolos (X u O) gana.
- Si se llenan todas las celdas sin ganador: empate.

---

## 🔧 Requisitos del programa

✅ Usar una **matriz 3x3 de enteros**  
✅ Utilizar funciones para:
- Mostrar el tablero
- Verificar si hay ganador
- Verificar si el tablero está lleno

✅ Representar el tablero como:
- `0` = celda vacía
- `-1` = jugador 1 (X)
- `1` = jugador 2 (O)

✅ Limpieza de pantalla con `system("cls")`  
✅ Alternancia automática de turnos

---

## 📄 Entrega

- Nombre del archivo: `gato.cpp`
- Sin bibliotecas externas (solo `<iostream>` y `<stdlib.h>`)
- No usar arreglos adicionales

---

## ✅ Evaluación (13 puntos)

| Criterio | Puntos |
|---------|--------|
| Archivo y compilación correcta | 2 |
| Funciones implementadas | 2 |
| Turnos y lógica de victoria | 4 |
| Tablero y detección de empate | 2 |
| Interfaz clara + limpieza pantalla | 3 |

**Extra:**  
✔️ Validar si la celda ya está ocupada (+1)  
✔️ Mejorar diseño del tablero e interfaz (+1)

---

## 🎉 ¡A jugar!

> Usa lo aprendido sobre funciones, condicionales y estructuras para crear un juego completamente funcional.

**¡Diviértete programando!**
