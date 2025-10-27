def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

v = 1

while v == 1:
    num1 = int(input("Introduce el primer número: "))
    operacion = input("Introduce una operación (suma, resta, multiplicacion, division): ")
    num2 = int(input("Introduce el segundo número: "))

    if operacion == "suma":
        resultado = suma(num1, num2)
    elif operacion == "resta":
        resultado = resta(num1, num2)
    elif operacion == "multiplicacion":
        resultado = multiplicacion(num1, num2)
    elif operacion == "division":
        resultado = division(num1, num2)
    else:
        print(f'Operación no válida.')
        continue

    print(f'Resultado:', resultado)

    pregunta1 = input("¿Quieres realizar otra operación con el resultado actual? (Si/No): ")
    if pregunta1.lower() == "si":
        num1 = resultado
        operacion = input("Introduce una operación (suma, resta, multiplicacion, division): ")
        num2 = int(input("Introduce el segundo número: "))

        if operacion == "suma":
            resultado = suma(num1, num2)
        elif operacion == "resta":
            resultado = resta(num1, num2)
        elif operacion == "multiplicacion":
            resultado = multiplicacion(num1, num2)
        elif operacion == "division":
            resultado = division(num1, num2)
        else:
            print(f'Operación no válida.')
            continue

        print(f'Resultado:', resultado)

    respuesta = input("¿Quieres realizar una nueva operación desde cero? (Si/No): ")
    if respuesta.lower() != "si":
        v = 0