# 🎡 Ejercicio: Ruleta de Probabilidades con Boletos

## Descripción

Este ejercicio simula una **ruleta de probabilidades** para rifas. Cada participante ha comprado una cantidad de boletos, y su **probabilidad de ganar** es proporcional a los boletos que compró en relación al total.

El giro de la ruleta se simula generando un número aleatorio entre 0 y 1. Luego se usa ese número para seleccionar un ganador con base en su rango de probabilidad acumulada.

---

## Objetivo

Escribe un programa en **C++** que:

1. Tenga dos arreglos:
   - `string nombres[]`: nombres de los participantes.
   - `int boletos[]`: cantidad de boletos que compró cada uno.
2. Calcule la **probabilidad** de cada participante.
3. Use un ciclo `for` para recorrer los participantes y comparando sus probabilidades con un número aleatorio `r` entre 0 y 1.
4. Cuando `r` sea menor que la probabilidad del participante, este es el ganador.
6. Muestra el número generado y el nombre del ganador.

---

## Requisitos

- Usar `rand()` y `RAND_MAX` para obtener un número entre 0 y 1.
- Usar un ciclo `for` para calcular la probabilidad acumulada.
- Comparar el valor aleatorio `r` con la probabilidad acumulada hasta encontrar el ganador.

---

## Recomendaciones

- Usar `srand(time(0))` al inicio del programa para garantizar números aleatorios.
- Imprimir las probabilidades de cada participante para propósitos de depuración.
- Usar variables `float` o `double` para las probabilidades.
- Comentar el código para mayor claridad.


