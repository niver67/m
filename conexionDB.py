import os
from tkinter import messagebox
from mysql.connector import connect, Error

class ConexionDB:
def init(self):
try:
self.conexion = connect(
host='localhost',
database='basededatos',
user='root',
password='03579'
)
self.cursor = self.conexion.cursor(dictionary=True)
except Error as error:
messagebox.showerror("Error de Conexión", f"Error al conectar a la base de datos: {error}")

def insertar_legajo(self, *values):
    query = """
        INSERT INTO sindicato (
            LEGAJO, APELLIDO_Y_NOMBRE, DIRECCION, LOCALIDAD, CP, FECHA_INGRESO, ANTIGUEDAD, FECHA_DE_NACIMIENTO,
            EDAD, DNI, NRO, CAT, OFICINA, NOMBRE_OFICINA, SECRETARIA, SINDICATO, SEPELIO, MUTUAL, SOLO_4,
            COSEGURO, SEGURO, PUESTO, SEXO, ESTUDIO, NRO_DE_AFILIADO, FECHA_DE_AFILIACION, CAMPO_EXTRA, FECHA_EXTRA
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    try:
        self.cursor.execute(query, values)
        self.conexion.commit()
        messagebox.showinfo("Insertar Legajo", "Datos insertados correctamente.")
    except Error as error:
        messagebox.showerror("Error de Conexión", f"Error al conectar a la base de datos: {error}")
messagebox.showerror("Error de Conexión", f"Error al conectar a la base de datos: {error}")
def insertar_legajo(self, *values):
    query = """
        INSERT INTO sindicato (
            LEGAJO, APELLIDO_Y_NOMBRE, DIRECCION, LOCALIDAD, CP, FECHA_INGRESO, ANTIGUEDAD, FECHA_DE_NACIMIENTO,
            EDAD, DNI, NRO, CAT, OFICINA, NOMBRE_OFICINA, SECRETARIA, SINDICATO, SEPELIO, MUTUAL, SOLO_4,
            COSEGURO, SEGURO, PUESTO, SEXO, ESTUDIO, NRO_DE_AFILIADO, FECHA_DE_AFILIACION, CAMPO_EXTRA, FECHA_EXTRA
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    try:
        self.cursor.execute(query, values)
        self.conexion.commit()
        messagebox.showinfo("Insertar Legajo", "Datos insertados correctamente.")
    except Error as error:
        messagebox.showerror("Error al Insertar", f"Error al insertar datos: {error}")

def buscar_legajo(self, valor):
    query = "SELECT * FROM sindicato WHERE LEGAJO = %s"
    try:
        self.cursor.execute(query, (valor,))
        return self.cursor.fetchall()
    except Error as error:
        messagebox.showerror("Error al Buscar", f"Error al buscar legajo: {error}")
        return []

def mostrar_legajo(self):
    query = "SELECT * FROM sindicato"
    try:
        self.cursor.execute(query)
        return self.cursor.fetchall()
    except Error as error:
        messagebox.showerror("Error al Mostrar", f"Error al mostrar legajos: {error}")
        return []

def actualizar_legajo(self, valores):
    query = """
        UPDATE sindicato SET 
            APELLIDO_Y_NOMBRE = %s, 
            DIRECCION = %s, 
            LOCALIDAD = %s, 
            CP = %s, 
            FECHA_INGRESO = %s, 
            ANTIGUEDAD = %s, 
            FECHA_DE_NACIMIENTO = %s, 
            EDAD = %s, 
            DNI = %s, 
            NRO = %s, 
            CAT = %s, 
            OFICINA = %s, 
            NOMBRE_OFICINA = %s, 
            SECRETARIA = %s, 
            SINDICATO = %s, 
            SEPELIO = %s, 
            MUTUAL = %s,    
            SOLO_4 = %s, 
            COSEGURO = %s, 
            SEGURO = %s, 
            PUESTO = %s, 
            SEXO = %s, 
            ESTUDIO = %s, 
            NRO_DE_AFILIADO = %s, 
            FECHA_DE_AFILIACION = %s, 
            CAMPO_EXTRA = %s, 
            FECHA_EXTRA = %s
        WHERE LEGAJO = %s
    """
    try:
        # Reemplazar valores nulos por None
        values = [
            valores['APELLIDO_Y_NOMBRE'], 
            valores['DIRECCION'], 
            valores['LOCALIDAD'], 
            valores['CP'], 
            valores['FECHA_INGRESO'], 
            valores['ANTIGUEDAD'], 
            valores['FECHA_DE_NACIMIENTO'], 
            valores['EDAD'], 
            valores['DNI'], 
            valores['NRO'], 
            valores['CAT'], 
            valores['OFICINA'], 
            valores['NOMBRE_OFICINA'], 
            valores['SECRETARIA'], 
            valores['SINDICATO'], 
            valores['SEPELIO'], 
            valores['MUTUAL'], 
            valores['SOLO_4'], 
            valores['COSEGURO'], 
            valores['SEGURO'], 
            valores['PUESTO'],
            valores['SEXO'], 
            valores['ESTUDIO'], 
                None if valores['NRO_DE_AFILIADO'] == 'None' else valores['NRO_DE_AFILIADO'], 
                None if valores['FECHA_DE_AFILIACION'] == 'None' else valores['FECHA_DE_AFILIACION'], 
                None if valores['CAMPO_EXTRA'] == 'None' else valores['CAMPO_EXTRA'], 
                None if valores['FECHA_EXTRA'] == 'None' else valores['FECHA_EXTRA'], 
                valores['LEGAJO']
            ]

            # Imprimir los valores para depuración
            print("Valores para la consulta de actualización:", values)

            # Ejecutar la consulta
            self.cursor.execute(query, values)
            self.conexion.commit()
            messagebox.showinfo("Actualizar Legajo", "Datos actualizados correctamente.")
        except Error as error:
            messagebox.showerror("Error al Actualizar", f"Error al actualizar datos: {error}")
            print("Error al actualizar datos:", error)  # Depuración: Imprimir error

    def obtener_bajas(self):
        query = "SELECT * FROM sindicato WHERE FECHA_EXTRA IS NOT NULL"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as error:
            messagebox.showerror("Error al Obtener Bajas", f"Error al obtener bajas: {error}")
            return []

    def cerrar_conexion(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conexion:
                self.conexion.close()
        except Error as error:
            messagebox.showerror("Error al Cerrar", f"Error al cerrar la conexión: {error}")


