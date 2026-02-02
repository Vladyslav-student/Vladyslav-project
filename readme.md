# 📘 Sistema de Gestión Académica y Calificación de Alumnos v1.0

> **Documentación Técnica del Proyecto**
>
> Este documento detalla la arquitectura, lógica y funcionalidad del "Gestor de Notas", una solución de software CLI (Interfaz de Línea de Comandos) desarrollada para optimizar la administración docente.

---

## 📑 Tabla de Contenidos

1. [Introducción y Objetivos](#1-introducción-y-objetivos)
2. [Requisitos del Sistema](#2-requisitos-del-sistema)
3. [Arquitectura de Software](#3-arquitectura-de-software)
    * [Estructura de Datos](#31-estructura-de-datos)


---

## 1. Introducción y Objetivos

El objetivo principal de este proyecto es digitalizar el cuaderno de notas tradicional del profesorado. El sistema permite realizar operaciones **CRUD** (Create, Read, Update, Delete) sobre los registros de los alumnos, garantizando la integridad de los datos y proporcionando cálculos estadísticos automáticos (media aritmética) en tiempo real.

**Puntos Clave:**
* Eliminación de errores de cálculo manual.
* Centralización de la información.
* Capacidad de exportación de datos (Persistencia).

---

## 2. Requisitos del Sistema

Para ejecutar este software, se requiere un entorno compatible con la interpretación de Python.

* **Sistema Operativo:** Multiplataforma (Windows, macOS, Linux).
* **Intérprete:** Python 3.6 o superior.
* **Librerías:** No requiere librerías externas (`pip install` no es necesario). Utiliza únicamente la librería estándar.

---

## 3. Arquitectura de Software

El programa sigue un paradigma de **Programación Estructurada** y utiliza un bucle principal (`Main Loop`) para la interacción con el usuario.

### 3.1 Estructura de Datos

La base de datos en memoria (`RAM`) se gestiona mediante un **Diccionario de Python** (`dict`). Esta estructura fue seleccionada por su eficiencia en tiempos de acceso y búsqueda.

* **Variable Global:** `mis_alumnos`
* **Formato:** `Clave (String) : Valor (List<Float>)`

**Diagrama lógico de la estructura:**
```text
mis_alumnos = {
    "Alumno A": [Nota1, Nota2, ...],  # Lista dinámica
    "Alumno B": [],                   # Lista vacía inicial
    ...
}

### 3.2 Almacenamiento y Persistencia (JSON)

Para cumplir con los requisitos de la entrega 2, se ha implementado el uso del formato **JSON** (JavaScript Object Notation) para el almacenamiento de datos. A diferencia de los archivos de texto plano, JSON permite guardar la estructura del diccionario (`clave: valor`) de forma nativa.

* **Archivo de destino:** `notas_clase.json`
* **Carga de datos:** Se ejecuta automáticamente mediante la función `cargar_datos()` al iniciar el script. Si el archivo no existe, el programa inicia con una base de datos vacía sin generar errores.
* **Guardado de datos:** Se realiza manualmente al seleccionar la opción "Guardar y Salir", serializando el diccionario en memoria y escribiéndolo en el disco.

### 3.3 Sistema de Registro (Logging)

Se ha integrado el módulo `logging` de Python para generar un historial de auditoría de la aplicación. Esto permite rastrear el funcionamiento del programa y detectar errores sin necesidad de estar mirando la consola constantemente.

* **Archivo de registro:** `registro.log`
* **Configuración:** Nivel `INFO`.
* **Eventos registrados:**
    * Inicio de sesión y carga de datos.
    * Creación y eliminación de alumnos.
    * Asignación de notas (éxito y error de tipo).
    * Cierre de sesión.

---

## 4. Documentación de Funciones

A continuación se detalla la lógica técnica de los módulos implementados:

* **`cargar_datos()`**: Gestiona la persistencia inicial. Utiliza un bloque `try-except` para manejar `FileNotFoundError` (primera ejecución) y `JSONDecodeError` (archivo corrupto), asegurando la estabilidad del sistema.
* **`insertar_alumno()`**: Solicita un nombre, lo limpia de espacios con `.strip()` y valida que no exista previamente en el diccionario `mis_alumnos`. Genera entradas de log tipo `INFO` o `WARNING`.
* **`modificar_notas()`**: Permite añadir calificaciones flotantes. Incluye validación de rango (0-10) y control de excepciones `ValueError` para evitar bloqueos si se introduce texto.
* **`buscar_alumno()`**: Recupera la lista de notas de un alumno específico y calcula su media aritmética en tiempo real.
* **`eliminar_alumno()`**: Elimina el registro completo (clave y valor) del diccionario global.
* **`mostrar_clase()`**: Recorre todo el diccionario para mostrar un resumen global del estado de la clase. Protege el cálculo de la media contra la división por cero si un alumno no tiene notas.
* **`guardar_en_archivo()`**: Utiliza `json.dump()` con el parámetro `indent=4` para escribir los datos en el archivo `.json` de forma legible y estructurada.

---

## 5. Instrucciones de Uso

1.  **Ejecución:** Abrir la terminal en la carpeta del proyecto y ejecutar:
    ```bash
    python gestor_notas.py
    ```
2.  **Archivos:** Al ejecutar el programa, se generará o actualizará automáticamente el archivo `registro.log`.
3.  **Operación:** Utilizar el menú numérico (1-6) para realizar las gestiones necesarias.
4.  **Guardado:** Es imprescindible seleccionar la **Opción 6 (Guardar y Salir)** para que los cambios realizados en memoria se escriban permanentemente en el archivo `notas_clase.json`.
