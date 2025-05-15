# ARREGLOS

1. Rellene un array con los 100 primeros números enteros y los muestre en pantalla en orden ascendente. - Nombre de archivo: `arreglos_1.cpp`

1. Rellene un array con los 100 primeros números enteros y los muestre en pantalla en orden descendente. - Nombre de archivo: `arreglos_2.cpp`

1. Rellene un array con los números primos comprendidos entre 1 y 100 y los muestre en pantalla en orden ascendente. - Nombre de archivo: `arreglos_3.cpp`

1. Rellene un array con los números pares comprendidos entre 1 y 100 y los muestre en pantalla en orden ascendente. - Nombre de archivo: `arreglos_4.cpp`

1. Que lea 5 números por teclado, los copie a otro array multiplicados por 2 y muestre el segundo array. - Nombre de archivo: `arreglos_5.cpp`

1. Lea 10 números por teclado, los almacene en un array y muestre la suma, resta, multiplicación y división de todos. - Nombre de archivo: `arreglos_6.cpp`

1. Cree un arreglo de 10 posiciones de numeros enteros. Pida al usuario los 10 numeros pero este valor siempre se ingresa en la posición 0, recorriendo los demás valores.  - Nombre de archivo: `arreglos_7.cpp`
    Ejemplo
    ```
    - A = [ 0, 0, 0, 0]
    - Usuario 1
    - A = [ 1, 0, 0, 0]
    - Usuario 2
    - A = [ 2, 1, 0, 0]
    - Usuario 6
    - A = [ 6, 2, 1, 0]
    - Usuario 3
    - A = [ 3, 6, 2, 1]
    ```

1. Cree un arreglo de 10 posiciones de numeros enteros. Pida al usuario los 10 numeros pero este valor siempre se ingresa en la posición 9, recorriendo los demás valores.  - Nombre de archivo: `arreglos_8.cpp`
    Ejemplo
    ```
    - A = [ 0, 0, 0, 0]
    - Usuario 1
    - A = [ 0, 0, 0, 1]
    - Usuario 2
    - A = [ 0, 0, 1, 2]
    - Usuario 6
    - A = [ 0, 1, 2, 6]
    - Usuario 3
    - A = [ 1, 2, 6, 3]
    ```

1. Cree un arreglo de 10 posiciones de numeros enteros. Llenelo con los valores del 1 al 10, consideré que el cero representa una casilla vacia. Pidale al usuario cuantos numeros quiere eliminar, y eliminelos inciando en el indice 0, recorra todos los valores hacia adelante.  - Nombre de archivo: `arreglos_9.cpp`

    Ejemplo
    ```
    - A = [ 1, 2, 3, 4]
    - Usuario 3
    - A = [ 4, 0, 0, 0]
    ```


1. Haga un programa que cree 2 arreglos de 5 valores y pida estos valores al usuario. Y finalmente imprima la suma de estos dos arreglos:  - Nombre de archivo: `arreglos_10.cpp`
    ```
    A    = [1, 4, 2,  6,  8]
    B    = [1, 2, 3,  4,  6]
    SUMA = [2, 6, 5, 10, 14]
    ```

1. Haga un programa que cree 2 arreglos de 3 valores y pida estos valores al usuario. Y finalmente realice el producto punto de estos arreglos.  - Nombre de archivo: `arreglos_11.cpp`
    ```
    A    = [1, 4, 2]

    B    = [1, 2, 3]

    A dot B = 1 * 1 + 4 * 2 + 2 * 3 = 1 + 8 + 6 = 15
    ```

1. Haga un programa que resuelva la siguiente ecuación, que recibe un vector de dos valores: Nombre de archivo: `arreglos_12.cpp`

    **$$ f(\vec{x}) = (x_1-10)^3+(x_2-20)^3 $$**

    x = (14.09500000000000064, 0.8429607892154795668) donde f(x) = −6961.81387558015.

1. Haga un programa que resuelva la siguiente ecuación, que recibe un vector de trece valores: Nombre de archivo: `arreglos_13.cpp`

    **$$ f(\vec{x}) = 5\sum_{i=1}^{4}x_i - 5\sum_{i=1}^{4}x^2_i - \sum_{i=5}^{13}x_i $$**

    x = (1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 1) donde f(x) = −15

1. Haga un programa que resuelva la siguiente ecuación, que recibe un vector de siete valores: Nombre de archivo: `arreglos_14.cpp`

    **$$ f(\vec{x}) = (x_1-10)^2 + 5(x_2-12)^2 + x_3^4 + 3(x_4-11)^2 + 10x^6_5 + 7x_6^2 + x_7^4 - 4x_6x_7 - 10x_6 - 8x_7$$**

    x = (2.33049935147405174, 1.95137236847114592, −0.477541399510615805, 4.36572624923625874, −0.624486959100388983, 1.03813099410962173, 1.5942266780671519) donde f(x) = 680.630057374402

1. Haga un programa que resuelva la siguiente ecuación, que recibe un vector de veinte valores: Nombre de archivo: `arreglos_15.cpp`

    $$ f(\vec{x}) = - \left| \dfrac{  \sum_{i=1}^{n} \cos^2(x_i) - 2 \prod_{i=1}^{n}\cos^2(x_i)  }{ \sqrt{\sum_{i=1}^{n}ix^2_i}  } \right|$$

    
    x = (3.16246061572185, 3.12833142812967, 3.09479212988791, 3.06145059523469, 3.02792915885555, 2.99382606701730, 2.95866871765285, 2.92184227312450, 0.49482511456933, 0.48835711005490, 0.48231642711865, 0.47664475092742, 0.47129550835493, 0.46623099264167, 0.46142004984199, 0.45683664767217, 0.45245876903267, 0.44826762241853, 0.44424700958760, 0.44038285956317), donde f(x) = −0.80361910412559


1. Cree dos arreglos uno con dimensión (posiciones) 4 y otro con dimensión 6. Ambos arreglos tendran valores ordenados de menor a mayo.

    Cree un nuevo arreglo de dimensión 10, en este arreglo mezcle ambos arreglos siempre colocando el menor primero. Este arreglo debe quedar con todos los valores arreglados. Nombre de archivo: `arreglos_16.cpp`

    Se le daran ejemplos para probarlo.
    ```
    Ejemplo 1
    - A = [ 2, 5, 7, 8]
    - B = [ 1, 4, 6, 9, 10, 11]
    - R = [ 1, 2, 4, 5, 6, 7, 8, 9, 10, 11]
    
    Ejemplo 2
    - A = [ 1, 7, 12, 15]
    - B = [ 3, 4, 6, 8, 9, 13]
    - R = [ 1, 3, 4, 6, 7, 8, 9, 12, 13, 15]
    ```

# MATRICES

1. Crear una matriz de 5x5 , llenarla con números consecutivos, y luego imprimala en pantalla de la siguiente forma: - Nombre de archivo: `matriz_1.cpp`
    ```
    1,  2,  3,  4,  5
    6,  7,  8,  9, 10
    11, 12, 13, 14, 15
    16, 17, 18, 19, 20
    21, 22, 23, 24, 25
    ```
    

1. La matriz anterior ahora imprimala inciando del valor mas alto. NOTA: Debe ser la misma matriz llenada del 1 al 25 inciando el 1 en la posición [0, 0]. - Nombre de archivo: `matriz_2.cpp`

    ```
    25, 24, 23, 22, 21
    20, 19, 18, 17, 16
    15, 14, 13, 12, 11
    10,  9,  8,  7,  6
    5,  4,  3,  2,  1
    ```
    

1.  Crear una matriz de 5x5 , llenarla con números consecutivos, y luego imprimala en pantalla de la siguiente forma: - Nombre de archivo: `matriz_3.cpp`
    ```
    1,  2,  3,  4,  5
    6,  7,  8,  9, 10
    11, 12, 13, 14, 15
    16, 17, 18, 19, 20
    21, 22, 23, 24, 25
    ```
    Y luego imprime la suma de cada una de las filas.
    ```
    Fila 1: 15
    Fila 2: 40
    Fila 3: 65
    Fila 4: 90
    Fila 5: 115
    ```
    
1. Crear una matriz de 5x5 , llenarla con números consecutivos, y luego imprimala en pantalla de la siguiente forma: - Nombre de archivo: `matriz_4.cpp`
    ```
    1,  2,  3,  4,  5
    6,  7,  8,  9, 10
    11, 12, 13, 14, 15
    16, 17, 18, 19, 20
    21, 22, 23, 24, 25
    ```
    Y luego imprime la suma de cada una de las columnas.
    ```
    Columna 1: 55
    Columna 2: 60
    Columna 3: 65
    Columna 4: 70
    Columna 5: 75
    ```
## Algebra lineal

1. **Matriz Identidad:**
   - Descripción: Crea una matriz identidad de tamaño n.
   - Nombre de archivo: `matriz_identidad.cpp`
   - Ejemplo:
     ```
      Entrada: 4
     
      Salida:
      - Se ve así:
      1 0 0 0
      0 1 0 0
      0 0 1 0
      0 0 0 1
     ```

2. **Suma de escalar y matriz**
   - Descripción: Realiza la suma de un escalar a una matriz
   - Nombre de archivo: `suma_escalar_matrices.cpp`
   - Ejemplo:
     ```
     Entrada: 2, 1, 2, 3, 4, 10
     Matriz A:
     1  2
     3  4
     
     Escalar: 10
     
     Salida:
     - Se ve así:
     11 12
     13 14
     ```
1. **Suma de Matrices:**
   - Descripción: Realiza la suma de dos matrices de igual tamaño.
   - Nombre de archivo: `suma_matrices.cpp`
   - Ejemplo:
     ```
     Entrada: 2, 1, 2, 3, 4, 5, 6, 7, 8
     Matriz A:
     1  2
     3  4
     
     Matriz B:
     5  6
     7  8
     
     Salida:
     - Se ve así:
     6 8
     10 12
     ```

1. **Producto escalar y Matrices:**
   - Descripción: Calcula el producto de un escalar y una matrices.
   - Nombre de archivo: `producto_escalar_matrices.cpp`
   - Ejemplo:
     
     ```
     Entrada: 2, 1, 2, 3, 5
     Matriz A:
     1  2
     3  4
     
     Escalar: 5
     
     Salida:
     - Se ve así:
     5 10
     15 20
     ```

1. **Producto de Matrices:**
   - Descripción: Calcula el producto de dos matrices compatibles.
   - Nombre de archivo: `producto_matrices.cpp`
   - Ejemplo:
     
     ```
     Entrada: 2, 1, 2, 3, 4, 5, 6, 7, 8
     Matriz A:
     1  2
     3  4
     
     Matriz B:
     5  6
     7  8
     
     Salida:
     - Se ve así:
     19 22
     43 50
     ```

1. **Matriz Transpuesta:**
   - Descripción: Encuentra la transpuesta de una matriz dada.
   - Nombre de archivo: `transpuesta_matriz.cpp`
   - Ejemplo:
     ```
     Entrada: 2, 3, 1, 2, 3, 4, 5, 6
     Matriz original:
     1 2 3
     4 5 6
     
     Salida:
     - Se ve así:
     
     1 4
     2 5
     3 6
     ```

1. **Diagonal Principal y Secundaria:**
   - Descripción: Calcula la suma de los elementos de la diagonal principal y secundaria de una matriz cuadrada.
   - Nombre de archivo: `diagonal_matriz.cpp`
   - Ejemplo:
     ```
     Entrada: 3, 1, 2, 3, 4, 5, 6, 7, 8, 9
     1  2  3
     4  5  6
     7  8  9
     ```
1. **Matriz mágica**
   Una matriz mágica es una matriz cuadrada que tiene como propiedad especial que la suma de las filas, columnas y diagonales es igual. Por ejemplo
    ```
     2  7  6
     9  5  1
     4  3  8
     ```
    y las sumas son 15.
   Haga un programa que pida al usario ingresar los valores de una matriz y este verifique si es mágica o no. Si es mágica se debe mostrar la suma, el usuario ingresa el tamaño de la matriz hasta un máximo de 10.
    - Nombre de archivo: `matriz_magica.cpp`