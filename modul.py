import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': '', 
            'database': 'sistema_gestion'
        }

    def get_connection(self):
        try:
            conn = mysql.connector.connect(**self.config)
            return conn
        except Error as e:
            print(f"Error al conectar con MySQL: {e}")
            return None


class ProductoModel:
    def __init__(self):
        self.db = DatabaseConnection()

    def obtener_productos(self):
        conn = self.db.get_connection()
        if not conn:
            print("Error: No se pudo conectar a la base de datos.")
            return []
        
        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT p.id, p.codigo, p.nombre, p.precio, p.stock, c.nombre as categoria 
                FROM productos p 
                LEFT JOIN categorias c ON p.categoria_id = c.id
            """
            cursor.execute(query)
            registros = cursor.fetchall()
            print(f" Registros encontrados en MySQL: {registros}")
            return registros
        except Error as e:
            print(f" Error al obtener productos: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def agregar_producto(self, codigo, nombre, precio, stock, categoria_id=1):
        conn = self.db.get_connection()
        if not conn:
            return False
        
        cursor = None
        try:
            cursor = conn.cursor()
            query = "INSERT INTO productos (codigo, nombre, precio, stock, categoria_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (codigo, nombre, precio, stock, categoria_id))
            conn.commit()
            return True
        except Error as e:
            print(f"Error al guardar: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def eliminar_producto(self, producto_id):
        conn = self.db.get_connection()
        if not conn:
            return False
        
        cursor = None
        try:
            cursor = conn.cursor()
            query = "DELETE FROM productos WHERE id = %s"
            cursor.execute(query, (producto_id,))
            conn.commit()
            return True
        except Error as e:
            print(f"Error al eliminar: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()
            
