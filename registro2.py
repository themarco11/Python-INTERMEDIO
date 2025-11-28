def validar_datos(nombre, edad, correo):
    print("Iniciando validación de datos...")

    try:
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un texto.")
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")

        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un número entero.")
        if edad <= 0:
            raise TypeError("La edad debe ser mayor que cero.")
        if edad > 90:
            raise TypeError("La edad no puede ser mayor de 110 años.")

        if "@" not in correo:
            raise TypeError("El correo debe contener '@'.")

        print("Validación completada.")
        print("Datos registrados correctamente.")

    except Exception as e:
        print("Error:", e)

    finally:
        print("Proceso terminado.\n")


print("=== REGISTRO DE USUARIO ===")

# Bucle para registrar varias personas
while True:
    try:
        nombre = input("Ingresa tu nombre: ")
        edad = int(input("Ingresa tu edad: "))
        correo = input("Ingresa tu correo: ")

        validar_datos(nombre, edad, correo)

    except TypeError:
        print("La edad debe ser un número entero.")

    # Preguntar si desea registrar otra persona
    repetir = input("¿Deseas registrar otra persona? (si/no): ").lower()
    if repetir != "si":
        print("Registro finalizado.")
