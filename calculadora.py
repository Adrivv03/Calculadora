from suma import sumar
from resta import restar
from multiplicacion import multiplicar
from division import dividir
def calculadora():
    print(""" 
          Opciones:
          0 - Salir
          1 - Suma
          2 - Resta
          3 - Multiplicación
          4 - División
          
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
        elif opcion == 2:
            a = int(input("Primer número: "))
            b = int(input("Segundo número: "))
            print(f"Resultado de la resta: {restar(a, b)}")
        elif opcion == 3:
            a = int(input("Primer número: "))
            b = int(input("Segundo número: "))
            print(f"Resultado de la multiplicación: {multiplicar(a, b)}")
        elif opcion == 4:
            a = int(input("Primer número: "))
            b = int(input("Segundo número: "))
            if b == 0:
                raise ValueError("No se puede dividir entre 0")
            print(f"Resultado de la división: {dividir(a, b)}")
if __name__ == "__main__":
    calculadora()