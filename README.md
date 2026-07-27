# Sistema de Gestión de Inventario (MVC)

Este repositorio contiene el proyecto final para el sistema de gestión de inventario, desarrollado en Python bajo el patrón de arquitectura Modelo-Vista-Controlador (MVC) y utilizando MySQL como sistema de gestión de base de datos.

##  Tecnologías Utilizadas
* **Lenguaje:** Python
* **Interfaz Gráfica:** Tkinter / ttk
* **Base de Datos:** MySQL
* **Gestor Local:** XAMPP / phpMyAdmin

## Estructura del Proyecto
* `app.py`: Archivo ejecutable principal del sistema.
* `modul.py`: Manejo de la conexión a la base de datos MySQL y consultas SQL (Modelo).
* `vista.py`: Definición de las pantallas, tablas y formularios con Tkinter (Vista).
* `controlador.py`: Validaciones y comunicación entre el Modelo y la Vista (Controlador).
* `sistema_gestion.sql`: Script ejecutable para importar la base de datos y sus tablas.

##  Instrucciones de Ejecución
1. Importar la base de datos `sistema_gestion.sql` en phpMyAdmin.
2. Iniciar el servicio de MySQL desde XAMPP.
3. Ejecutar el archivo principal desde la terminal:
   ```bash
   python app.py
