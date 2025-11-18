from collections import Counter, OrderedDict

# 1. Diccionario con las listas de compras y registrados
datos_clientes = {
    "compras": [
        "Marco", "Jorge", "Ivonne", "Lucia", "Liliana", "Carlos",
        "Mariana", "Lucia", "Sebas", "Baruc", "Carlos", "Sofia"
    ],
    "registrados": ["Ana", "Pedro", "Maria", "Lucia", "Miguel", "Carlos"]
}

# Acceso a las listas dentro del diccionario
compras = datos_clientes["compras"]
registrados = datos_clientes["registrados"]

# 2. Filtrar clientes nuevos (no registrados)
clientes_nuevos = list(set(compras) - set(registrados))

# 3. Eliminar duplicados y mantener el orden
clientes_unicos = list(OrderedDict.fromkeys(compras))

# 4. Contar cuántas veces aparece cada cliente
conteo_compras = Counter(compras)

# 5. Crear resumen personalizado (solo clientes frecuentes)
resumen_frecuentes = {
    cliente: f"Ha comprado {veces} veces"
    for cliente, veces in conteo_compras.items()
    if veces > 1
}

# Formato final de salida
print("=== CLIENTES NUEVOS NO REGISTRADOS ===")
print(clientes_nuevos)

print("\n=== CLIENTES UNICOS (SIN DUPLICADOS) ===")
print(clientes_unicos)

print("\n=== CLIENTES FRECUENTES (MAS DE 1 COMPRA) ===")
for cliente, mensaje in resumen_frecuentes.items():
    print(f"{cliente}: {mensaje}")