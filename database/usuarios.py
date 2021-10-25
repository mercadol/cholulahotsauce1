import sqlite3
from sqlite3 import Error

from .connection import create_connection


def insert_usuario(data):
    conn = create_connection()

    sql= """ INSERT INTO usuario (ID_Usuario, Correo, Nombre, Apellido, Cedula, Genero, Fecha_ingreso, Direccion, Tipo_contrato, Id_Rol, ID_Cargo)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    try:
        cur= conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(f"Error ar insert_usuario(): {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()

def get_usuarios():
    conn =create_connection()
    sql=""" SELECT * FROM Usuario """

    try:
        cur=conn.cursor()
        cur.execute(sql)
        return cur.lastrowid
    except Error as e:
        print(f"Error ar insert_usuario(): {str(e)}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
        

