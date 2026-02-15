import json
import logging

# --- CONFIGURACIÓN DE LOGGING ---
logging.basicConfig(filename='registro.log', level=logging.INFO)

# ==========================================
# 1. CLASES DE DATOS (MODELO)
# ==========================================

class Persona:
    """
    Representa la identidad básica.
    """
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Persona: {self.nombre}"

class Alumno(Persona):
    """
    Clase Padre (Elemento Principal).
    Representa un alumno estándar.
    """
    def __init__(self, nombre, notas=None):
        super().__init__(nombre)
        # Asignamos las notas (si no hay, lista vacía)
        if notas is None:
            self.notas = []
        else:
            self.notas = notas

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        return 0.0

    def to_dict(self):
        """Convierte a diccionario base."""
        return {
            "tipo": "Normal", # Ayuda a identificarlo en el JSON (opcional pero útil)
            "nombre": self.nombre,
            "notas": self.notas
        }

    def __str__(self):
        return f"[Alumno] {self.nombre} - Notas: {self.notas}"

class AlumnoErasmus(Alumno):
    """
    Clase Hija (Subclase Especial).
    Hereda de Alumno y añade el país de destino.
    """
    def __init__(self, nombre, notas=None, pais="Desconocido"):
        # Llamamos al constructor de Alumno para gestionar nombre y notas
        super().__init__(nombre, notas)
        self.pais = pais

    def to_dict(self):
        
        #Sobreescribimos to_dict para añadir el campo extra.
        
        data = super().to_dict()
        data["tipo"] = "Erasmus"
        data["pais"] = self.pais
        return data

    def __str__(self):
        # Representación diferente para distinguir que es Erasmus
        return f"[ERASMUS - {self.pais}] {self.nombre} - Notas: {self.notas}"

# ==========================================
# 2. CLASE DE CONTROL (GESTOR)
# ==========================================

class GestorNotas:
    def __init__(self):
        self.archivo_json = "notas_clase.json"
        self.mis_alumnos = {}
        self.cargar_datos()   

    def cargar_datos(self):
        try:
            with open(self.archivo_json, "r", encoding='utf-8') as archivo:
                datos_cargados = json.load(archivo)
                
                self.mis_alumnos = {}
                for nombre_clave, datos in datos_cargados.items():
                    # --- LÓGICA DE DETECCIÓN DE TIPO ---
                    if datos.get("tipo") == "Erasmus" or "pais" in datos:
                        # Creamos objeto Erasmus
                        pais = datos.get("pais", "Desconocido")
                        alumno_obj = AlumnoErasmus(datos["nombre"], datos["notas"], pais)
                    else:
                        # Creamos objeto Alumno normal
                        alumno_obj = Alumno(datos["nombre"], datos["notas"])
                    
                    self.mis_alumnos[nombre_clave] = alumno_obj
                    
            print(">> Datos cargados correctamente.")
            logging.info("Inicio: Datos cargados desde JSON.")

        except (FileNotFoundError, json.JSONDecodeError):
            print(">> Base de datos nueva/vacía.")
            self.mis_alumnos = {}

    def guardar_datos(self):
        try:
            datos_para_guardar = {}
            for nombre, obj_alumno in self.mis_alumnos.items():
                datos_para_guardar[nombre] = obj_alumno.to_dict()

            with open(self.archivo_json, "w", encoding='utf-8') as archivo:
                json.dump(datos_para_guardar, archivo, indent=4)
            print("Datos guardados en JSON.")
            logging.info("Guardado exitoso.")
        except Exception as e:
            print(f"Error al guardar: {e}")

    def insertar_alumno(self):
        nombre = input("Nombre del nuevo alumno: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return

        if nombre in self.mis_alumnos:
            print("Ese alumno ya existe.")
            return

        # --- ADAPTACIÓN DEL MENÚ ---
        # Preguntamos si es un caso especial
        es_erasmus = input("¿Es un alumno de beca Erasmus? (s/n): ").strip().lower()

        if es_erasmus == 's':
            pais = input("Introduce el país de destino: ").strip()
            # Instanciamos la SUBCLASE
            nuevo_alumno = AlumnoErasmus(nombre, pais=pais)
            logging.info(f"Alumno Erasmus creado: {nombre} ({pais})")
        else:
            # Instanciamos la CLASE BASE
            nuevo_alumno = Alumno(nombre)
            logging.info(f"Alumno normal creado: {nombre}")

        self.mis_alumnos[nombre] = nuevo_alumno
        print(f"Alumno registrado correctamente.")

    def modificar_notas(self):
        nombre = input("Nombre del alumno: ").strip()
        if nombre in self.mis_alumnos:
            try:
                nota = float(input(f"Introduce nota para {nombre}: "))
                if 0 <= nota <= 10:
                    self.mis_alumnos[nombre].agregar_nota(nota)
                    print("Nota guardada.")
                else:
                    print("Nota debe ser entre 0 y 10.")
            except ValueError:
                print("Error: Introduce un número.")
        else:
            print("Alumno no encontrado.")

    def buscar_alumno(self):
        nombre = input("¿A quién buscas?: ").strip()
        if nombre in self.mis_alumnos:
            alumno = self.mis_alumnos[nombre]
            
            # El print usará el __str__ correspondiente (Normal o Erasmus) automáticamente
            print(f"--- Ficha ---")
            print(alumno) 
            
            media = alumno.calcular_media()
            print(f"Media actual: {media:.2f}")
        else:
            print("Alumno no encontrado.")

    def eliminar_alumno(self):
        nombre = input("Nombre a eliminar: ").strip()
        if nombre in self.mis_alumnos:
            del self.mis_alumnos[nombre]
            print("Eliminado.")
        else:
            print("No existe.")

    def mostrar_clase(self):
        if not self.mis_alumnos:
            print("No hay alumnos.")
            return
        
        print("\n--- LISTADO DE CLASE ---")
        for alumno in self.mis_alumnos.values():
            media = alumno.calcular_media()
            print(f"{alumno} | Media: {media:.2f}")
        print("------------------------")

    def iniciar(self):
        while True:
            print("\n1. Insertar Alumno | 2. Añadir Nota | 3. Buscar | 4. Borrar | 5. Ver Todo | 6. Salir")
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
# 3. EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    app = GestorNotas()
    app.iniciar()