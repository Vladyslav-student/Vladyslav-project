# PROYECTO: Gestor de Notas
# La idea es hacer un pqueño programa para que los profesores puedan gestionar las notas de sus alumnos.
# El programa permitirá añadir alumnos, asignarles notas, ver las notas y calcular la media, y guardar los datos en archivos de texto separados entre aprobados y suspensos.(Parte final del proyecto).
# Primera Entrega de la estructura basica del programa.


# PROYECTO: Gestor de Notas - Entrega 2
import json
import logging

# --- CONFIGURACIÓN MÍNIMA DE LOGGING ---
# Esto crea un archivo 'registro.log' automáticamente
logging.basicConfig(filename='registro.log', level=logging.INFO)

mis_alumnos = {}

# --- FUNCIÓN PARA CARGAR DATOS (JSON) ---
def cargar_datos():
    """Intenta cargar los datos del fichero JSON al iniciar."""
    global mis_alumnos
    try:
        with open("notas_clase.json", "r", encoding='utf-8') as archivo:
            mis_alumnos = json.load(archivo)
        print(">> Datos cargados correctamente.")
        logging.info("Inicio: Datos cargados desde JSON.")
    except FileNotFoundError:
        print(">> No hay datos previos. Se inicia vacío.")
        logging.info("Inicio: No existe JSON previo. Base de datos nueva.")
        mis_alumnos = {}
    except json.JSONDecodeError:
        print(">> Error: El archivo de datos está dañado.")
        logging.error("Error: Archivo JSON corrupto o ilegible.")
        mis_alumnos = {}

# --- FUNCIONES DEL PROGRAMA ---

def insertar_alumno():
    nombre = input("Nombre del nuevo alumno: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        logging.warning("Intento de registro con nombre vacío.")
        return

    if nombre not in mis_alumnos:
        mis_alumnos[nombre] = []
        print(f"Alumno '{nombre}' registrado.")
        logging.info(f"Alumno creado: {nombre}")
    else:
        print("Ese alumno ya existe.")
        logging.warning(f"Intento de duplicado: {nombre}")

def modificar_notas():
    nombre = input("Nombre del alumno: ").strip()
    if nombre in mis_alumnos:
        try:
            nota = float(input(f"Introduce nota para {nombre}: "))
            if 0 <= nota <= 10:
                mis_alumnos[nombre].append(nota)
                print("Nota guardada.")
                logging.info(f"Nota {nota} añadida a {nombre}.")
            else:
                print("La nota debe estar entre 0 y 10.")
                logging.warning(f"Nota fuera de rango para {nombre}: {nota}")
        except ValueError:
            print("Error: Introduce un número.")
            logging.error(f"Error de tipo (no numérico) al calificar a {nombre}.")
    else:
        print("Alumno no encontrado.")
        logging.warning(f"Intento de calificar alumno inexistente: {nombre}")

def buscar_alumno():
    nombre = input("¿A quién buscas?: ").strip()
    if nombre in mis_alumnos:
        notas = mis_alumnos[nombre]
        print(f"--- {nombre} ---")
        print(f"Notas: {notas}")
        logging.info(f"Consulta de datos: {nombre}")
        
        if len(notas) > 0:
            media = sum(notas) / len(notas)
            print(f"Media: {media:.2f}")
        else:
            print("Media: Sin notas")
    else:
        print("Alumno no encontrado.")

def eliminar_alumno():
    nombre = input("Nombre a eliminar: ").strip()
    if nombre in mis_alumnos:
        del mis_alumnos[nombre]
        print("Alumno eliminado.")
        logging.info(f"Alumno eliminado: {nombre}")
    else:
        print("El alumno no existe.")

def mostrar_clase():
    if not mis_alumnos:
        print("No hay alumnos.")
        return
    
    print("--- CLASE COMPLETA ---")
    for nombre, notas in mis_alumnos.items():
        if notas:
            media = sum(notas) / len(notas)
            print(f"{nombre} - Media: {media:.2f}")
        else:
            print(f"{nombre} - Sin notas")
    logging.info("Reporte general de clase mostrado.")

def guardar_en_archivo():
    """Guarda los datos en formato JSON."""
    try:
        with open("notas_clase.json", "w", encoding='utf-8') as archivo:
            json.dump(mis_alumnos, archivo, indent=4)
        print("Datos guardados en 'notas_clase.json'.")
        logging.info("Guardado exitoso en JSON.")
    except Exception as e:
        print(f"Error al guardar: {e}")
        logging.error(f"Fallo al guardar JSON: {e}")

# --- MENÚ PRINCIPAL ---
cargar_datos() # IMPORTANTE: Cargar al principio

while True:
    print("\n1. Insertar | 2. Nota | 3. Buscar | 4. Borrar | 5. Ver Todo | 6. Salir")
    opcion = input("Opción: ")
    
    if opcion == "1": insertar_alumno()
    elif opcion == "2": modificar_notas()
    elif opcion == "3": buscar_alumno()
    elif opcion == "4": eliminar_alumno()
    elif opcion == "5": mostrar_clase()
    elif opcion == "6":
        guardar_en_archivo()
        print("Adios.")
        logging.info("Fin de sesión.")
        break
    else:
        print("Opción no válida")