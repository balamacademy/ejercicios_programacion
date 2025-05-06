# 🧠 Ejercicio: Adivina el número secreto (Juego de las Cartas Binarias)

## Descripción

Un clásico juego de lógica permite adivinar un número secreto entre 1 y 63 preguntando únicamente si el número aparece en un conjunto de 6 cartas. Este juego se basa en el sistema binario y es ideal para practicar estructuras de control, arreglos y lógica condicional.

Cada carta contiene ciertos números del 1 al 63. Si un número aparece en una carta, se debe responder "sí"; de lo contrario, "no". A partir de las respuestas, se puede deducir el número original **sumando los valores correspondientes a cada carta con respuesta "sí"**.

---

## Las Cartas

A continuación se muestran las 6 cartas utilizadas en el juego. Cada carta contiene los números cuyo valor binario tiene un `1` en una posición específica (de derecha a izquierda).

### Carta 1 (valor 1 - bit 0)

```
1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31
33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63
```

### Carta 2 (valor 2 - bit 1)

```
2  3  6  7 10 11 14 15 18 19 22 23 26 27 30 31
34 35 38 39 42 43 46 47 50 51 54 55 58 59 62 63
```

### Carta 3 (valor 4 - bit 2)

```
4  5  6  7 12 13 14 15 20 21 22 23 28 29 30 31
36 37 38 39 44 45 46 47 52 53 54 55 60 61 62 63
```

### Carta 4 (valor 8 - bit 3)

```
8  9 10 11 12 13 14 15 24 25 26 27 28 29 30 31
40 41 42 43 44 45 46 47 56 57 58 59 60 61 62 63
```

### Carta 5 (valor 16 - bit 4)

```
16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63
```

### Carta 6 (valor 32 - bit 5)

```
32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63
```

---

## Objetivo

Escribe un programa en **C++** que:

1. Pregunte al usuario si su número secreto está en cada una de las 6 cartas (`s` para sí, `n` para no).
2. Calcule el número secreto basándose en las respuestas.
3. Muestre el número que el usuario estaba pensando.

---

## Requisitos

- Usa un arreglo de 6 valores correspondientes a las cartas: `{1, 2, 4, 8, 16, 32}`.
- Usa un ciclo para recorrer las cartas y solicitar una respuesta del usuario.
- Si el usuario responde `'s'`, suma el valor correspondiente.
- Al final, muestra el número adivinado.

---

## Ejemplo de ejecución

```
¿Tu número está en la carta 1? (s/n): s
¿Tu número está en la carta 2? (s/n): n
¿Tu número está en la carta 3? (s/n): s
¿Tu número está en la carta 4? (s/n): s
¿Tu número está en la carta 5? (s/n): n
¿Tu número está en la carta 6? (s/n): s

Tu número es: 45
```

---

## Recomendaciones

- Usa `cin` y `cout` para entrada y salida.
- Usa validación opcional para aceptar únicamente `'s'` o `'n'`.
- Comenta tu código para mejorar su comprensión.
- Puedes imprimir las cartas como parte del programa o asumir que el usuario las tiene frente a él.
