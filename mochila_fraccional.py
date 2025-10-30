def mochila_fraccional(pesos, valores, capacidad):
    # Crear lista de objetos con su ratio valor/peso
    objetos = []
    for i in range(len(pesos)):
        ratio = valores[i] / pesos[i]
        objetos.append({
            'indice': i,
            'peso': pesos[i],
            'valor': valores[i],
            'ratio': ratio,
            'nombre': chr(65 + i)  # A, B, C...
        })

    # Ordenar por ratio (valor/peso) descendente
    objetos.sort(key=lambda x: x['ratio'], reverse=True)

    valor_total = 0
    peso_usado = 0
    seleccion = []  # Guardar qué se tomó y cuánto

    print("OBJETOS ORDENADOS POR VALOR/KG:")
    print("-" * 55)
    print(f"{'Objeto':<8} {'Peso':<8} {'Valor':<8} {'Valor/kg':<10}")
    print("-" * 55)
    for obj in objetos:
        print(f"{obj['nombre']:<8} {obj['peso']:<8} {obj['valor']:<8} {obj['ratio']:<10.2f}")
    print("-" * 55)
    print(f"\nCapacidad de la mochila: {capacidad} kg\n")

    # Aplicar algoritmo voraz
    for obj in objetos:
        if peso_usado >= capacidad:
            break

        peso_disponible = capacidad - peso_usado

        if obj['peso'] <= peso_disponible:
            # Tomar todo el objeto
            fraccion = 1.0
            peso_tomado = obj['peso']
            valor_tomado = obj['valor']
        else:
            # Tomar fracción
            fraccion = peso_disponible / obj['peso']
            peso_tomado = peso_disponible
            valor_tomado = fraccion * obj['valor']

        # Actualizar totales
        peso_usado += peso_tomado
        valor_total += valor_tomado

        # Guardar selección
        if fraccion == 1.0:
            seleccion.append(f"Todo {obj['nombre']} ({obj['peso']} kg, {obj['valor']} monedas)")
        else:
            seleccion.append(f"{fraccion:.3f} de {obj['nombre']} ({peso_tomado} kg, {valor_tomado} monedas)")

    return valor_total, seleccion, objetos

pesos = [10, 20, 30]        # A, B, C
valores = [60, 100, 120]
capacidad = 50

valor_optimo, seleccion, objetos_ordenados = mochila_fraccional(pesos, valores, capacidad)

print("SOLUCIÓN ÓPTIMA (Algoritmo Voraz):")
print("=" * 60)
for item in seleccion:
    print("→", item)
print("=" * 60)
print(f"VALOR TOTAL MÁXIMO: {valor_optimo} monedas de oro")
print(f"PESO TOTAL USADO: {capacidad} kg")
print("=" * 60)