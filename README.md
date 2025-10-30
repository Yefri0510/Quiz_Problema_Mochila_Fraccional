# Algoritmo voraz — Mochila fraccionaria
## Yefri Stiven Barrero Solano - 2320392

## Tema general

Este repositorio muestra la implementación del **algoritmo voraz** para resolver la **mochila fraccionaria** (fractional knapsack). El problema consiste en maximizar el valor total que cabe en una mochila con capacidad limitada si los objetos **pueden fraccionarse** (es decir, podemos tomar parte de un objeto).

---

## Código

* **Construcción de la lista de objetos con ratio valor/peso**
  Para cada objeto se calcula `ratio = valor / peso` y se almacena junto con sus atributos (`indice`, `peso`, `valor`, `ratio`, `nombre`).
  Esta relación es la medida de “valor por kg” que guía la elección voraz.

* **Ordenación por ratio descendente**
  Los objetos se ordenan por `ratio` de mayor a menor. Esta es la fase crítica: tomamos primero lo que aporta más valor por unidad de peso.

* **Selección voraz (iteración y fraccionamiento)**
  Se recorre la lista ordenada y para cada objeto:

  * Si cabe completo en la mochila, se toma todo.
  * Si no cabe, se toma la fracción máxima posible (capacidad restante / peso del objeto) y se termina.
    Se actualizan `peso_usado`, `valor_total` y se guarda la descripción de la selección.

* **Salida**
  El código imprime los objetos ordenados (nombre, peso, valor, valor/kg) y devuelve `valor_total`, `seleccion` y `objetos` ordenados. La complejidad dominante es la ordenación: **O(n log n)**.

---

## Respuestas a las preguntas planteadas

### 1) ¿Cuál es la combinación óptima que maximiza el valor total sin exceder la capacidad de 50 kg, usando un algoritmo voraz?

Con los datos:

* Objetos: A `(peso=10, valor=60)`, B `(20, 100)`, C `(30, 120)`
* Ratios (valor/kg): A = 6.0, B = 5.0, C = 4.0
* Capacidad = 50 kg

La estrategia voraz toma primero A, luego B, y finalmente la fracción necesaria de C:

* `Todo A` → 10 kg → 60 monedas
* `Todo B` → 20 kg → 100 monedas
* `2/3 de C` → 20 kg (20/30 = 0.666...) → 80 monedas

**Resultado final:**

* **Valor total máximo:** `60 + 100 + 80 = 240` monedas
* **Peso usado:** `10 + 20 + 20 = 50` kg (capacidad completa)
* **Selección:** `Todo A`, `Todo B`, `0.667 de C` (aprox.)

> Nota: para la versión fraccionaria del problema, el algoritmo voraz basado en `valor/peso` **es óptimo**.

---

### 2) ¿Cuándo es apropiado usar un algoritmo voraz? ¿Cuáles son sus limitaciones?

**Cuándo usarlo**

* Cuando el problema satisface la **propiedad de elección voraz** (greedy-choice property) y la **subestructura óptima**: elegir la mejor opción local en cada paso lleva a una solución global óptima.
* Ejemplo clásico donde funciona y es óptimo: **mochila fraccionaria** (objetos divisibles).
* Es útil cuando se necesita una solución rápida, con buena complejidad (usualmente O(n log n) por ordenación) y cuando los ítems pueden tomarse parcialmente o cuando el problema está diseñado para admitir una estrategia voraz.

**Limitaciones**

* **No es óptimo para la mochila 0/1** (objetos indivisibles). En ese caso la elección por mejor `valor/peso` puede llevar a una solución subóptima. La mochila 0/1 requiere DP o búsqueda para garantizar optimalidad.
* El voraz falla cuando la mejor decisión local impide alcanzar la mejor solución global (problemas sin la propiedad voraz).
* No es una receta universal: muchos problemas requieren comprobar que la heurística voraz cumple las condiciones necesarias (o usarla solo como aproximación).
* Si se necesita la **solución exacta** para problemas discretos NP-completos, a menudo hay que recurrir a algoritmos más costosos (programación dinámica, branch-and-bound, etc.).

---

## Resultado concreto (ejemplo de salida)

```
OBJETOS ORDENADOS POR VALOR/KG:
-------------------------------------------------------
Objeto   Peso     Valor    Valor/kg
-------------------------------------------------------
A        10       60       6.00
B        20       100      5.00
C        30       120      4.00
-------------------------------------------------------

Capacidad de la mochila: 50 kg

SOLUCIÓN ÓPTIMA (Algoritmo Voraz):
============================================================
→ Todo A (10 kg, 60 monedas)
→ Todo B (20 kg, 100 monedas)
→ 0.667 de C (20 kg, 80.0 monedas)
============================================================
VALOR TOTAL MÁXIMO: 240 monedas de oro
PESO TOTAL USADO: 50 kg
============================================================
```

---
