# Ejercicios condicionales simples

1. **Mayor de edad**
   -  Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad (18 o más) o no.
   - Nombre de archivo: `mayordeedad.cpp`
   - Ejemplo:
     ```
     Entrada: 18
     Salida: Eres Mayor
     ```
     ```
     Entrada: 15
     Salida: No eres Mayor
     ```
1. **División Exacta**
   -  Escriba un programa que pida dos números enteros y que calcule su división, y diga si la división es exacta o no.
   - Nombre de archivo: `divisionexacta.cpp`
   - Ejemplo:
     ```
     Entrada: 10, 5
     Salida: La division es exacta
     ```
     ```
     Entrada: 21, 4
     Salida: La division NO es exacta
     ```

1. **Par Impar**
   -  Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
   - Nombre de archivo: `parimpar.cpp`
   - Ejemplo:
     ```
     Entrada: 80
     Salida: Numero par
     ```
     ```
     Entrada: 21
     Salida: Numero impar
     ```

1. **Años Faltantes**
   - Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.
   - Nombre de archivo: `agnosfaltantes.cpp`
   - Ejemplo:
     ```
     Entrada: 2025, 2000
     Salida: Han pasado 25 agnos
     ```
     ```
     Entrada: 2025, 2035
     Salida: Faltan 10 agnos
     ```

1. **Bisiesto**
   - Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
   - Nombre de archivo: `bisiesto.cpp`
   - Ejemplo:
     ```
     Entrada: 2024
     Salida: Es bisiesto
     ```
     ```
     Entrada: 2025
     Salida: No es bisiesto
     ```

# Ejercicios condicionales Multiples

1. **Mes**
   - Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente. NOTA: Los nombres de los meses con mayuscula inicial y sin acentos.
   - Nombre de archivo: `mes.cpp`
   - Ejemplo:
     ```
     Entrada: 12
     Salida: Diciembre
     ```
     ```
     Entrada: 13
     Salida: No es existe
     ```

1. **Día**
   - Se desea diseñar un algoritmo que escriba los nombres de los días de la semana en función del valor de una variable DIA introducida por teclado. Si introducimos otro número nos da un error. NOTA: Los nombres de los días con mayuscula inicial y sin acentos.
   - Nombre de archivo: `dia.cpp`
   - Ejemplo:
     ```
     Entrada: 1
     Salida: Lunes
     ```
     ```
     Entrada: 7
     Salida: Domingo
     ```

1. **Día de la semana dado un número de día del mes**
    - Dado un número de día de un mes: decir el día de la semana, suponiendo que el día 1 de dicho mes fue lunes
    - Nombre de archivo: `diados.cpp`
    - Ejemplo:
      ```
      Entrada: 1
      Salida: Lunes
      ```
      ```
      Entrada: 2
      Salida: Martes
      ```
      ```
      Entrada: 18
      Salida: Jueves
      ```

1. **Día de la semana para cualquier inicio de mes**
    - Preguntar qué día de la semana fue el día 1 del mes actual (Usar numeros para el día de la semana 0-Domingo 6-Sabado) y calcular que día de la semana es hoy.
    - Nombre de archivo: `diatres.cpp`
    - Ejemplo:
      ```
      Entrada: 1, 18
      Salida: Jueves
      ```
      ```
      Entrada: 6, 13
      Salida: Jueves
      ```
      ```
      Entrada: 2, 14
      Salida: Lunes
      ```

1. **Calificaciones Alfabeticas**
   - Se desea convertir las calificaciones alfabéticas A, B, C, D, E y F a calificaciones numéricas 9, 8, 7, 6, 5 y 4 respectivamente.
   - Nombre de archivo: `calificacionesalfa.cpp`
   - Ejemplo:
     ```
     Entrada: A
     Salida: 9
     ```
     ```
     Entrada: E
     Salida: 5
     ```

1. **Mayor de tres números**
    - Diseñar un algoritmo que lea tres números A, B, C y visualice en pantalla el valor del más grande. Se
 supone que los tres valores son diferentes.
    - Nombre de archivo: `mayordetres.cpp`
   - Ejemplo:
     ```
     Entrada: 19, 21, 33
     Salida: 33
     ```
     ```
     Entrada: 17 7 9
     Salida: 17
     ```
     ```
     Entrada: 6 27 9
     Salida: 27
     ```

1. **Sala de juegos**
   - Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, $10.
   - Nombre de archivo: `saladejuegos.cpp`
   - Ejemplo:
     ```
     Entrada: 4
     Salida: ¡¡Gratis!!
     ```
     ```
     Entrada: 15
     Salida: Paga $5
     ```
     ```
     Entrada: 45
     Salida: Paga $10
     ```
1. **IVA**
   - Se trata de escribir el algoritmo que permita emitir la factura correspondiente a una compra de un artículo determinado, del que se adquieren una o varias unidades. El IVA a aplicar es del 15% y si el precio bruto (precio venta más IVA) es mayor de 1000, se debe realizar un descuento del 5%.
   - Nombre de archivo: `iva.cpp`
   - Ejemplo:
     ```
     Entrada: 5, 100
     Salida: Pagar $575
     ```
     ```
     Entrada: 4, 300
     Salida: Pagar $1311
     ```
1. **Dado**
    -  Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en texto (dato cadena) de la cara opuesta al resultado obtenido.
        - Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
        - Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”
    - Nombre de archivo: `dado.cpp`
    - Ejemplo:
      ```
      Entrada: 1
      Salida: Seis
      ```
      ```
      Entrada: 4
      Salida: Tres
      ```

1. **Triangulos**
    - Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
        - Sí se cumple Pitágoras entonces es triángulo rectángulo
        - Sí sólo dos lados del triángulo son iguales entonces es isósceles.
        - Sí los 3 lados son iguales entonces es equilátero.
        - Sí no se cumple ninguna de las condiciones anteriores, es escaleno.
    - Nombre de archivo: `dado.cpp`
    - Ejemplo:
      ```
      Entrada: 7, 7, 4
      Salida:  Isosceles
      ```
      ```
      Entrada: 4, 4, 5
      Salida: Equilatero
      ```
  
1. **Nomina**
    -  11. Se desea obtener la nómina semanal —salario neto— de los empleados de una empresa cuyo trabajo se paga por horas y del modo siguiente: 
          - las horas inferiores o iguales a 35 horas (normales) se pagan a una tarifa determinada que se debe introducir por teclado al igual que el número de horas y el nombre del trabajador,
          - las horas superiores a 35 se pagarán como extras a 1.5 horas normales,
          - los impuestos a deducir a los trabajadores varían en función de su sueldo mensual: — sueldo <=2.000, libre de impuestos, — de 2000 a 4200 al 20%, — mayor a 4200, al 30%.
    - Nombre de archivo: `nomina.cpp`
    - Ejemplo:
      ```
      Entrada: 50, 10, Juan
      Salida: 500
      ```
      ```
      Entrada: 50, 40, Pedro
      Salida: 2400
      ```
      ```
      Entrada: 50, 50, Hugo
      Salida: 5250
      ```
1. **Pizzería**
    - La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
        - Ingredientes vegetarianos: Pimiento y tofu.
        - Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

      Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva
    - Nombre de archivo: `pizzeria.cpp`
    - Ejemplo:
      ```
      Entrada: 1, 2
      Salida: Su pizza es Vegetariana y lleva Tofu, Mozarrela y Tomate
      ```
      ```
      Entrada: 2, 4
      Salida: Su pizza no es Vegetariana y lleva Salmon, Mozarrela y Tomate
      ```

      **NOTA**
      Lo conveniente por el momento es usar numeros como entradas o solo caracteres, para este ejercicio si coloque los mensajes necesarios para guiar al usuario. Mostrar un menú como:
      ```
      Introduzca el número de su elección:
        1. Vegetariano
        2. No Vegetariano
        1
      Seleccione Ingrediente
        1. Pimiento
        2. Tofu
        2
      Su pizza es Vegetariana y lleva Tofu, Mozarrela y Tomate
      ```