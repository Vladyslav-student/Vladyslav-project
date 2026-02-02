# PROYECTO: Gestor de Notas - Entrega Final (POO + Herencia)
import json
import logging

# --- CONFIGURACIÓN DE LOGGING ---
logging.basicConfig(filename='registro.log', level=logging.INFO)

# ==========================================
# 1. CLASES DE DATOS (MODELO)
# ==========================================

class Persona:
    """
    Clase Padre (Base). 
    Representa a cualquier persona con un nombre.
    """
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Persona: {self.nombre}"

class Alumno(Persona):
    """
    Clase Hija (Derivada).
    Hereda de Persona y añade la gestión de notas.
    """
    def __init__(self, nombre, notas=None):
        # Llamamos al constructor del padre (Persona) para asignar el nombre
        super().__init__(nombre)
        
        # Asignamos las notas (si no hay, lista vacía)
        if notas is None:
            self.notas = []
        else:
            self.notas = notas

    def agregar_nota(self, nota):
        """Método encapsulado para añadir notas."""
        self.notas.append(nota)

    def calcular_media(self):
        """Método encapsulado para calcular la propia media."""
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        return 0.0

    def to_dict(self):
        """
        Convierte el Objeto a Diccionario para poder guardarlo en JSON.
        (Los objetos no se guardan solos en JSON).
        """
        return {
            "nombre": self.nombre,
            "notas": self.notas
        }

    def __str__(self):
        """Representación en texto del alumno."""
        return f"{self.nombre} - Notas: {self.notas}"

# ==========================================
# 2. CLASE DE CONTROL (GESTOR)
# ==========================================

class GestorNotas:
    """
    Clase que maneja toda la lógica del programa (CRUD).
    Sustituye a las funciones sueltas y al diccionario global.
    """
    def __init__(self):
        self.archivo_json = "notas_clase.json"
        self.mis_alumnos = {} # Diccionario de OBJETOS Alumno
        self.cargar_datos()   # Carga automática al iniciar

    def cargar_datos(self):
        try:
            with open(self.archivo_json, "r", encoding='utf-8') as archivo:
                datos_cargados = json.load(archivo)
                
                # RECONSTRUCCIÓN: Convertimos el JSON (diccionarios) a Objetos Alumno
                self.mis_alumnos = {}
                for nombre_clave, datos in datos_cargados.items():
                    # Creamos el objeto Alumno usando los datos leídos
                    alumno_obj = Alumno(datos["nombre"], datos["notas"])
                    self.mis_alumnos[nombre_clave] = alumno_obj
                    
            print(">> Datos cargados correctamente.")
            logging.info("Inicio: Datos cargados desde JSON.")
        except (FileNotFoundError, json.JSONDecodeError):
            print(">> Base de datos nueva/vacía.")
            logging.info("Inicio: Base de datos nueva.")
            self.mis_alumnos = {}

    def guardar_datos(self):
        try:
            # SERIALIZACIÓN: Convertimos los objetos Alumno a diccionarios simples
            datos_para_guardar = {}
            for nombre, obj_alumno in self.mis_alumnos.items():
                datos_para_guardar[nombre] = obj_alumno.to_dict()

            with open(self.archivo_json, "w", encoding='utf-8') as archivo:
                json.dump(datos_para_guardar, archivo, indent=4)
            print("Datos guardados en JSON.")
            logging.info("Guardado exitoso.")
        except Exception as e:
            print(f"Error al guardar: {e}")
            logging.error(f"Fallo al guardar: {e}")

    def insertar_alumno(self):
        nombre = input("Nombre del nuevo alumno: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return

        if nombre not in self.mis_alumnos:
            # INSTANCIAMOS LA CLASE ALUMNO
            nuevo_alumno = Alumno(nombre)
            self.mis_alumnos[nombre] = nuevo_alumno
            print(f"Alumno '{nombre}' registrado.")
            logging.info(f"Alumno creado: {nombre}")
        else:
            print("Ese alumno ya existe.")

    def modificar_notas(self):
        nombre = input("Nombre del alumno: ").strip()
        if nombre in self.mis_alumnos:
            try:
                nota = float(input(f"Introduce nota para {nombre}: "))
                if 0 <= nota <= 10:
                    # Usamos el MÉTODO del objeto
                    self.mis_alumnos[nombre].agregar_nota(nota)
                    print("Nota guardada.")
                    logging.info(f"Nota {nota} añadida a {nombre}.")
                else:
                    print("Nota debe ser entre 0 y 10.")
            except ValueError:
                print("Error: Introduce un número.")
        else:
            print("Alumno no encontrado.")

    def buscar_alumno(self):
        nombre = input("¿A quién buscas?: ").strip()
        if nombre in self.mis_alumnos:
            # Recuperamos el objeto
            alumno = self.mis_alumnos[nombre]
            print(f"--- Ficha de {alumno.nombre} ---")
            print(f"Notas: {alumno.notas}")
            
            # Usamos el método de la clase para calcular la media
            media = alumno.calcular_media()
            if media > 0 or alumno.notas:
                print(f"Media: {media:.2f}")
            else:
                print("Media: Sin notas")
            logging.info(f"Consultado: {nombre}")
        else:
            print("Alumno no encontrado.")

    def eliminar_alumno(self):
        nombre = input("Nombre a eliminar: ").strip()
        if nombre in self.mis_alumnos:
            del self.mis_alumnos[nombre]
            print("Eliminado.")
            logging.info(f"Eliminado: {nombre}")
        else:
            print("No existe.")

    def mostrar_clase(self):
        if not self.mis_alumnos:
            print("No hay alumnos.")
            return
        
        print("--- CLASE COMPLETA ---")
        for alumno in self.mis_alumnos.values():
            media = alumno.calcular_media()
            nota_str = f"{media:.2f}" if alumno.notas else "Sin notas"
            print(f"{alumno.nombre} - Notas: {alumno.notas} - Media: {nota_str}")

    def iniciar(self):
        """Bucle principal del menú"""
        while True:
            print("\n1. Insertar | 2. Nota | 3. Buscar | 4. Borrar | 5. Ver Todo | 6. Salir")
            opcion = input("Opción: ")
            
            if opcion == "1": self.insertar_alumno()
            elif opcion == "2": self.modificar_notas()
            elif opcion == "3": self.buscar_alumno()
            elif opcion == "4": self.eliminar_alumno()
            elif opcion == "5": self.mostrar_clase()
            elif opcion == "6":
                self.guardar_datos()
                print("Adios.")
                break
            else:
                print("Opción no válida")

# ==========================================
# 3. EJECUCIÓN DEL PROGRAMA
# ==========================================

# Todo el programa se resume en estas dos líneas:
# Creamos el gestor y lo iniciamos.
if __name__ == "__main__":
    app = GestorNotas()
    app.iniciar()