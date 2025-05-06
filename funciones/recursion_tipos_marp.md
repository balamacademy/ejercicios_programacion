---
marp: true
theme: default
class: lead
paginate: true
---

# 🌀 Recursión en C++

Explicación de los tipos de recursión:  
- Simple  
- Múltiple  
- Externa (Indirecta)

---

## 🔁 ¿Qué es la recursión?

La **recursión** es una técnica en la que una función se llama a sí misma para resolver un problema dividiéndolo en subproblemas más simples.

Requiere:
- Caso base (condición de parada)
- Llamada recursiva

---

## 🔹 Recursión Simple

Una función se llama a sí misma **una sola vez** en su cuerpo.

### 📌 Ejemplo:
```cpp
void cuentaAtras(int n) {
    if (n == 0) return;
    cout << n << endl;
    cuentaAtras(n - 1);
}
```

Llama a `cuentaAtras(n-1)` hasta llegar a 0.

---

## 🔷 Recursión Múltiple

Una función se llama a sí misma **más de una vez** en su cuerpo.

### 📌 Ejemplo:
```cpp
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

Llama a sí misma dos veces: `fibonacci(n-1)` y `fibonacci(n-2)`.

---

## 🔁 Recursión Externa (Indirecta)

Una función **A** llama a otra función **B**, y **B** llama de vuelta a **A**.

### 📌 Ejemplo:
```cpp
void par(int n);
void impar(int n);

void par(int n) {
    if (n == 0) {
        cout << "Es par" << endl;
        return;
    }
    impar(n - 1);
}

void impar(int n) {
    if (n == 0) {
        cout << "Es impar" << endl;
        return;
    }
    par(n - 1);
}
```

---

## 🧠 Conclusión

- Usa recursión cuando un problema se puede descomponer naturalmente en subproblemas.
- Siempre define un **caso base** para evitar recursión infinita.
- Puedes encontrar recursión simple, múltiple e indirecta en algoritmos matemáticos, recorridos, juegos, etc.

---

## 📚 ¿Dudas o preguntas?

¡Es hora de practicar algunos ejercicios con recursión!
