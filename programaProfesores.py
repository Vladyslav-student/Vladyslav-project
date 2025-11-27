# PROYECTO: Gestor de Notas
# La idea es hacer un pqueño programa para que los profesores puedan gestionar las notas de sus alumnos.
# El programa permitirá añadir alumnos, asignarles notas, ver las notas y calcular la media, y guardar los datos en archivos de texto separados entre aprobados y suspensos.(Parte final del proyecto).
# Primera Entrega de la estructura basica del programa.
mis_alumnos = {}

def guardar_en_archivo():
    archivo = open("notas_guardadas.txt", "w")
    
    for alumno in mis_alumnos:
        notas = mis_alumnos[alumno]
        archivo.write(f"{alumno},{notas}\n")
    
    archivo.close()
    print("Datos guardados en notas_guardadas.txt")

def agregar_alumno():
    nombre = input("Escribe el nombre del alumno: ")

    if nombre not in mis_alumnos:
        mis_alumnos[nombre] = []
        print("Alumno nuevo registrado.")

    nota = float(input(f"Introduce la nota de {nombre}: "))

    mis_alumnos[nombre].append(nota)
    print("Nota añadida.")

def ver_clase():
    print("--- LISTA DE CLASE ---")
    for nombre in mis_alumnos:
        notas = mis_alumnos[nombre]
        
        suma = sum(notas)
        cantidad = len(notas)
        promedio = suma / cantidad
        
        print(f"{nombre} - Notas: {notas} - Media: {promedio}")

# --- MENU PRINCIPAL ---
while True:
    print("\n1. Poner notas")
    print("2. Ver resultados")
    print("3. Guardar y Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        agregar_alumno()
    elif opcion == "2":
        if len(mis_alumnos) > 0:
            ver_clase()
        else:
            print("Todavía no hay alumnos.")
    elif opcion == "3":
        guardar_en_archivo()
        break
        print("Opción incorrecta")