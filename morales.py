import math

def suma_numeros():
    cantidad_morales = int(input("Ingrese la cantidad de números a sumar: "))
    numeros_morales = [float(input(f"Ingrese el número Morales #{i + 1}: ")) for i in range(cantidad_morales)]
    resultado_morales = sum(numeros_morales)
    print(f"La suma de los números Morales es: {resultado_morales}\n")

def producto_numeros():
    cantidad_morales = int(input("Ingrese la cantidad de números a multiplicar: "))
    numeros_morales = [float(input(f"Ingrese el número Morales #{i + 1}: ")) for i in range(cantidad_morales)]
    resultado_morales = 1
    for num_morales in numeros_morales:
        resultado_morales *= num_morales
    print(f"El producto de los números Morales es: {resultado_morales}\n")

def division_numeros():
    num1_morales = float(input("Ingrese el primer número Morales: "))
    num2_morales = float(input("Ingrese el segundo número Morales (distinto de cero): "))
    resultado_morales = num1_morales / num2_morales
    print(f"La división de {num1_morales} entre {num2_morales} es: {resultado_morales}\n")

def calcular_factorial():
    n_morales = int(input("Ingrese un número Morales para calcular su factorial: "))
    resultado_morales = math.factorial(n_morales)
    print(f"El factorial de {n_morales} es: {resultado_morales}\n")

def tablas_multiplicar():
    num_tabla_morales = int(input("Ingrese el número Morales para mostrar su tabla de multiplicar (1 al 10): "))
    for i_morales in range(1, 11):
        print(f"{num_tabla_morales} x {i_morales} = {num_tabla_morales * i_morales}")
    print()

def cuadrado_y_cubo():
    numero_morales = float(input("Ingrese un número Morales para calcular su cuadrado y cubo: "))
    cuadrado_morales = numero_morales ** 2
    cubo_morales = numero_morales ** 3
    print(f"El cuadrado de {numero_morales} es: {cuadrado_morales}")
    print(f"El cubo de {numero_morales} es: {cubo_morales}\n")

def promedio_numeros():
    numeros_morales = []
    while True:
        num_morales = float(input("Ingrese un número Morales (-1 para dejar de ingresar): "))
        if num_morales == -1:
            break
        numeros_morales.append(num_morales)
    if numeros_morales:
        promedio_morales = sum(numeros_morales) / len(numeros_morales)
        print(f"El promedio de los números Morales es: {promedio_morales}\n")
    else:
        print("No se ingresaron números Morales.\n")

def valores_maximo_minimo():
    cantidad_morales = int(input("Ingrese la cantidad de números Morales a comparar: "))
    numeros_morales = [float(input(f"Ingrese el número Morales #{i + 1}: ")) for i in range(cantidad_morales)]
    maximo_morales = max(numeros_morales)
    minimo_morales = min(numeros_morales)
    print(f"El valor máximo Morales es: {maximo_morales}")
    print(f"El valor mínimo Morales es: {minimo_morales}")
    print(f"Se introdujeron en total {cantidad_morales} números Morales.\n")

def menu():
    while True:
        print("Menú de opciones Morales:")
        print("1. Suma de números Morales")
        print("2. Producto de números Morales")
        print("3. División de números Morales")
        print("4. Calcular factorial Morales")
        print("5. Tablas de multiplicar Morales")
        print("6. Cuadrado y cubo de un número Morales")
        print("7. Promedio de números Morales")
        print("8. Valores máximo y mínimo Morales")
        print("0. Salir")

        opcion_morales = input("Seleccione una opción Morales: ")

        if opcion_morales == '1':
            suma_numeros()
        elif opcion_morales == '2':
            producto_numeros()
        elif opcion_morales == '3':
            division_numeros()
        elif opcion_morales == '4':
            calcular_factorial()
        elif opcion_morales == '5':
            tablas_multiplicar()
        elif opcion_morales == '6':
            cuadrado_y_cubo()
        elif opcion_morales == '7':
            promedio_numeros()
        elif opcion_morales == '8':
            valores_maximo_minimo()
        elif opcion_morales == '0':
            print("Saliendo del programa Morales. ¡Hasta luego Morales!")
            break
        else:
            print("Opción no válida Morales. Inténtelo de nuevo Morales.\n")

if __name__ == "__main__":
    menu()
