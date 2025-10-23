from resta import restar

def calculadora():
    print("""
    Opciones:
    0 - Salir
    2 - Resta
    """)

    while True:
        opcion = int(input("Introduzca la opción: "))
        if opcion == 0:
            print("Saliendo...")
            break
        elif opcion == 2:
            a = int(input("Primer número: "))
            b = int(input("Segundo número: "))
            print(f"Resultado de la resta: {restar(a, b)}")

if __name__ == "__main__":
    calculadora()