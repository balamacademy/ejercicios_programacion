
## 🐜 Hormiga de Langton

### 🎯 Descripción del Problema

Desarrolla un programa en C++ que simule el comportamiento de la **Hormiga de Langton**, un autómata celular bidimensional con reglas simples que producen un comportamiento emergente sorprendente.

---

### 📜 Reglas del Autómata

La simulación ocurre en un tablero bidimensional formado por celdas cuadradas que pueden ser de dos colores: **blanco** o **negro**.

1. La hormiga comienza en una posición del tablero, mirando hacia una de las 4 direcciones cardinales: Norte, Sur, Este u Oeste.
2. En cada paso, la hormiga sigue las siguientes reglas:
   - Si la celda actual es **blanca**:
     - Gira 90° a la **derecha**
     - Cambia la celda a **negra**
     - Avanza una celda hacia adelante
   - Si la celda actual es **negra**:
     - Gira 90° a la **izquierda**
     - Cambia la celda a **blanca**
     - Avanza una celda hacia adelante

Estas simples instrucciones dan origen a patrones caóticos al inicio, y eventualmente a una estructura repetitiva llamada "carretera".

---

### 📥 Entrada

- Tamaño del tablero (filas y columnas).
- Número de pasos de simulación.
- Posición inicial de la hormiga (fila y columna).
- Dirección inicial: N, S, E, O.

Ejemplo:
```
Ingrese filas y columnas: 11 11
Ingrese pasos: 100
Posición inicial: 5 5
Dirección inicial: N
```

---

### 🧠 Recomendaciones de Implementación

- Representa el tablero como una matriz de enteros (`0` = blanco, `1` = negro).
- Usa un conjunto de direcciones codificadas como índices:
  - `0` = Norte
  - `1` = Este
  - `2` = Sur
  - `3` = Oeste
- Usa arreglos `dx[]` y `dy[]` para simplificar los movimientos según la dirección.
- Implementa la lógica del tablero **circular**:
  - Si la hormiga se sale por un borde, reaparece por el borde opuesto (usa módulo `%` para lograrlo).
- Usa `Sleep(500)` (Windows) o `usleep(500000)` (Linux/macOS) para pausar medio segundo entre pasos.
- Limpia la pantalla en cada iteración para simular el movimiento (`system("cls")` o `system("clear")`).

---

### 🖥️ Salida esperada

El programa debe mostrar el tablero automáticamente cada 500 milisegundos, simulando el movimiento de la hormiga en tiempo real.

Usa los siguientes símbolos:
- `.` para celdas blancas
- `#` para celdas negras
- Una letra o símbolo como `^`, `v`, `<`, `>` para representar la hormiga según su orientación

Ejemplo parcial de salida durante la ejecución:

```
Paso 50:
...........
...........
.....#.....
....###....
.....^.....
...........
...........
```

---

### 📦 Entrega

- Archivo obligatorio: `langton.cpp`
- Organiza el código utilizando funciones:
  - `inicializar_tablero()`
  - `mover_hormiga()`
  - `mostrar_tablero()`
