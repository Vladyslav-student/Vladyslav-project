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
    * [Diseño Modular](#32-diseño-modular)
4. [Documentación Técnica de Funciones (API)](#4-documentación-técnica-de-funciones-api)
5. [Estrategia de Manejo de Errores y Robustez](#5-estrategia-de-manejo-de-errores-y-robustez)
6. [Persistencia y Almacenamiento](#6-persistencia-y-almacenamiento)
7. [Guía de Usuario (Workflow)](#7-guía-de-usuario-workflow)
8. [Hoja de Ruta (Próximos Pasos)](#8-hoja-de-ruta-próximos-pasos)

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