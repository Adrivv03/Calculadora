from suma import sumar
def calculadora():
    print(""" 
          Opciones:
          0 - Salir
          1 - Suma
""")
    while True:
        opcion = int(input("Introduzca la opcion que quiera: "))
        if opcion == 0:
            print("Saliendo de calculadora...")
            break
        if opcion == 1:
            a = int(input("Introduzca el primer numero: "))
            b = int(input("Introduzca el segundo número: "))
            print(f"El resultado de la suma de {a} + {b} es: {sumar(a, b)}")

if __name__ == "__main__":
    calculadora()