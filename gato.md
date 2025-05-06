## Juego del Gato (Tres en Línea)

Desarrolla un programa que permita jugar al clásico **juego del gato (tres en línea)** entre dos jugadores, usando una matriz de 3x3 como tablero.

### Requisitos del juego:

- El programa debe usar una **matriz de enteros de 3x3** para representar el tablero.
- Cada jugador debe ingresar un número del **0 al 8**, correspondiente a una celda del tablero. El número se convierte en una posición de fila y columna.
- Un jugador juega con el símbolo **X** y otro con el símbolo **O**.
- Se deben utilizar funciones para:
  - Mostrar el tablero actual en pantalla.
  - Verificar si un jugador ha ganado, comprobando filas, columnas y diagonales.
  - Verificar si el tablero está completamente lleno.
- El juego debe continuar hasta que:
  - Un jugador gane, o
  - El tablero esté lleno (empate).
- Al final, el programa debe mostrar el tablero final y un mensaje indicando si ganó el **jugador 1**, el **jugador 2** o si hubo un **empate**.
- La pantalla debe limpiarse en cada turno para mostrar solo la versión actual del tablero.

### Consideraciones:

- Utiliza valores enteros para representar las jugadas: uno de los jugadores puede usar **1** y el otro **-1**, mientras que las casillas vacías se representan con **0**.
- La conversión del número de celda a fila y columna debe realizarse mediante una operación aritmética.
- No es necesario validar si la celda ya está ocupada, aunque se puede agregar como mejora opcional.
