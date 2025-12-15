# PROYECTO: Gestor de Notas
# La idea es hacer un pqueño programa para que los profesores puedan gestionar las notas de sus alumnos.
# El programa permitirá añadir alumnos, asignarles notas, ver las notas y calcular la media, y guardar los datos en archivos de texto separados entre aprobados y suspensos.(Parte final del proyecto).
# Primera Entrega de la estructura basica del programa.


#  Gestor de Notas (Corregido)
mis_alumnos = {}

def insertar_alumno():
    """
    Crea un nuevo alumno en el diccionario si no existe.
    """
    nombre = input("Escribe el nombre del nuevo alumno: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    if nombre not in mis_alumnos:
        mis_alumnos[nombre] = []
        print(f"Alumno '{nombre}' registrado correctamente.")
    else:
        print("Ese alumno ya existe.")

def modificar_notas():
    """
    Busca un alumno existente y permite añadirle una nota.
    Incluye control de errores para evitar que el programa falle si se escriben letras.
    """
    nombre = input("Nombre del alumno a calificar: ").strip()
    
    if nombre in mis_alumnos:
        try:
            nota = float(input(f"Introduce la nota para {nombre}: "))
            if 0 <= nota <= 10: # Opcional: validar rango lógico de nota
                mis_alumnos[nombre].append(nota)
                print(f"Nota {nota} añadida a {nombre}.")
            else:
                print("Por favor, introduce una nota entre 0 y 10.")
        except ValueError:
            print("ERROR: Debes introducir un número (ej: 7.5), no letras.")
    else:
        print("El alumno no existe. Usa la opción de insertar primero.")

def buscar_alumno():
    """
    Busca un alumno en concreto y muestra sus notas y media.
    Controla el error de división por cero si no tiene notas.
    """
    nombre = input("¿A quién buscas?: ").strip()
    
    if nombre in mis_alumnos:
        notas = mis_alumnos[nombre]
        print(f"--- Ficha de {nombre} ---")
        print(f"Notas: {notas}")
        
        # Control de DivisionError
        if len(notas) > 0:
            media = sum(notas) / len(notas)
            print(f"Media: {media:.2f}")
        else:
            print("Media: N/A (No tiene notas registradas)")
    else:
        print("Alumno no encontrado.")

def eliminar_alumno():
    """
    Elimina a un alumno del diccionario dado su nombre.
    """
    nombre = input("Nombre del alumno a eliminar: ").strip()
    
    if nombre in mis_alumnos:
        del mis_alumnos[nombre]
        print(f"Alumno '{nombre}' eliminado correctamente.")
    else:
        print("No se puede eliminar: El alumno no existe.")

def mostrar_clase():
    """
    Muestra la lista completa de alumnos, sus notas y sus medias.
    """
    if len(mis_alumnos) == 0:
        print("No hay alumnos registrados.")
        return

    print("--- LISTA DE CLASE ---")
    for nombre, notas in mis_alumnos.items():
        # Control de DivisionError
        if len(notas) > 0:
            promedio = sum(notas) / len(notas)
            media_str = f"{promedio:.2f}"
        else:
            media_str = "Sin notas"
            
        print(f"{nombre} - Notas: {notas} - Media: {media_str}")

def guardar_en_archivo():
    """
    Guarda los datos actuales en un archivo de texto y finaliza el guardado.
    """
    try:
        archivo = open("notas_guardadas.txt", "w")
        for alumno, notas in mis_alumnos.items():
            archivo.write(f"{alumno},{notas}\n")
        archivo.close()
        print("Datos guardados exitosamente en 'notas_guardadas.txt'.")
    except Exception as e:
        print(f"Hubo un error al guardar: {e}")

# --- MENÚ PRINCIPAL ---
while True:
    print("\n--- GESTOR DE NOTAS ---")
    print("1. Insertar Alumno (Crear)")
    print("2. Modificar Nota (Añadir nota)")
    print("3. Buscar Alumno (Consultar uno)")
    print("4. Eliminar Alumno (Borrar)")
    print("5. Ver Clase (Mostrar todos)")
    print("6. Guardar y Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        insertar_alumno()
    elif opcion == "2":
        modificar_notas()
    elif opcion == "3":
        buscar_alumno()
    elif opcion == "4":
        eliminar_alumno()
    elif opcion == "5":
        mostrar_clase()
    elif opcion == "6":
        guardar_en_archivo()
        print("¡Hasta luego!")
        break # El break está aquí, dentro de la opción de salida.
    else:
        print("Opción incorrecta. Por favor, elige del 1 al 6.")