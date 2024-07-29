import os
import csv
from tkinter import *
from tkinter import messagebox, filedialog, ttk
import tkinter
from ConexionDB import ConexionDB
from datetime import datetime

class Aplicacion(Frame):
  def init(self, master=None):
    super().init(master)
    self.master = master
    self.master.configure(bg='#2C3E50')
    icon_path = os.path.join(os.path.dirname(file), 'sindicato.ico')
    self.master.iconbitmap(icon_path)
    self.create_widgets()
    self.basededatos = ConexionDB()
    self.pack(fill=X, expand=False)
    def create_widgets(self):
    # Crear el primer frame (arriba) para búsqueda y botones
    self.frame1 = Frame(self, bg='#2C3E50')
    self.frame1.place(x=0, y=0, width=1920, height=100)

    self.label1 = Label(self.frame1, text="Buscar Legajo:", bg='#2C3E50', fg='white', font=('Arial', 12))
    self.label1.pack(side="left", padx=5)

    self.entry_legajo = Entry(self.frame1, bg='darkgray', fg='black', font=('Arial', 12))
    self.entry_legajo.pack(side="left", padx=5)

    self.boton_buscar = Button(self.frame1, text="Buscar", command=self.buscar_nombre, bg='gray', fg='white', font=('Arial', 12))
    self.boton_buscar.pack(side="left", padx=5)

    self.boton_guardar = Button(self.frame1, text="Guardar", command=self.guardar_cambios, bg='gray', fg='white', font=('Arial', 12))
    self.boton_guardar.pack(side="left", padx=5)

    self.boton_listar = Button(self.frame1, text="Listar Bajas", command=self.listar_bajas, bg='gray', fg='white', font=('Arial', 12))
    self.boton_listar.pack(side="left", padx=5)

    self.boton_exportar = Button(self.frame1, text="Exportar CSV", command=self.exportar_csv, bg='gray', fg='white', font=('Arial', 12))
    self.boton_exportar.pack(side="left", padx=5)

    # Crear el segundo frame (izquierda) para entradas de datos
    self.frame2 = Frame(self, bg='#2C3E50')
    self.frame2.place(x=0, y=100, width=1000, height=1080)

    self.variables = {key: StringVar() for key in [
        'LEGAJO', 'APELLIDO_Y_NOMBRE', 'DIRECCION', 'LOCALIDAD', 'CP', 
        'FECHA_INGRESO', 'ANTIGUEDAD', 'FECHA_DE_NACIMIENTO', 'EDAD', 
        'DNI', 'NRO', 'CAT', 'OFICINA', 'NOMBRE_OFICINA', 'SECRETARIA', 
        'SINDICATO', 'SEPELIO', 'MUTUAL', 'SOLO_4', 'COSEGURO', 
        'SEGURO', 'PUESTO', 'SEXO', 'ESTUDIO', 'NRO_DE_AFILIADO', 
        'FECHA_DE_AFILIACION', 'CAMPO_EXTRA', 'FECHA_EXTRA'
    ]}

    labels = list(self.variables.keys())
    entries = list(self.variables.values())
    num_fields = len(labels)

    for i in range(num_fields):
        column = 0 if i < num_fields / 2 else 2
        row = i if i < num_fields / 2 else i - num_fields // 2
        Label(self.frame2, text=labels[i], bg='#2C3E50', fg='white', font=('Arial', 12)).grid(row=row, column=column, padx=10, pady=5, sticky="e")
        Entry(self.frame2, textvariable=entries[i], font=('Arial', 12), bg='darkgray', fg='black', width=24).grid(row=row, column=column+1, padx=10, pady=5, sticky="w")

    # Crear el tercer frame (derecha) para el Treeview
    self.frame3 = Frame(self, bg='#2C3E50')
    self.frame3.place(x=1000, y=100, width=800, height=1000)
    self.frame4 = Frame (self, bg='#2C3E50')     
    self.frame4.place(x=1800, y=100, width=1000, height=1080
    self.tree = ttk.Treeview(self.frame3, columns=('LEGAJO', 'FECHA_EXTRA', 'APELLIDO_Y_NOMBRE'), show='headings')
    self.tree.heading('LEGAJO', text='LEGAJO')
    self.tree.heading('FECHA_EXTRA', text='FECHA EXTRA')
    self.tree.heading('APELLIDO_Y_NOMBRE', text='APELLIDO Y NOMBRE')

    self.tree.column('LEGAJO', width=300)
    self.tree.column('FECHA_EXTRA', width=100)
    self.tree.column('APELLIDO_Y_NOMBRE', width=300)

    self.tree.pack(fill=BOTH, expand=True)

  def buscar_nombre(self):
        legajo = self.entry_legajo.get()
        for var in self.variables.values():
            var.set("")
        try:
            resultados = self.basededatos.buscar_legajo(legajo)
            if resultados:
                for key, value in zip(self.variables.keys(), resultados[0].values()):
                    self.variables[key].set(value)
            else:
                self.show_message("No se encontraron resultados.")
        except Exception as e:
            self.show_message(f"Error al buscar: {e}")

def guardar_cambios(self):
        valores = {key: var.get() for key, var in self.variables.items()}
        
        # Depuración: Verificar los valores obtenidos
        print("Valores a guardar:", valores)
        
        # Convertir 'None' a None para SQL
        valores = {key: (None if value == 'None' else value) for key, value in valores.items()}
        
        try:
            self.basededatos.actualizar_legajo(valores)
            self.show_message("Cambios guardados correctamente.")
        except Exception as e:
            self.show_message(f"Error al guardar cambios: {e}")
            print("Error al guardar cambios:", e)  # Depuración: Imprimir error

    def listar_bajas(self):
        try:
            resultados = self.basededatos.obtener_bajas()
            bajas_filtradas = [r for r in resultados if r['FECHA_EXTRA'] is not None and r['SINDICATO']]
            
            if bajas_filtradas:
                self.tree.delete(*self.tree.get_children())  # Limpiar Treeview antes de llenarlo de nuevo
                self.bajas = []  # Limpiar lista de bajas antes de llenarla de nuevo

                for b in bajas_filtradas:
                    legajo = b['LEGAJO']
                    fecha_extra = b['FECHA_EXTRA']
                    apellido_y_nombre = b['APELLIDO_Y_NOMBRE']
                    self.bajas.append({'LEGAJO': legajo, 'FECHA_EXTRA': fecha_extra, 'APELLIDO_Y_NOMBRE': apellido_y_nombre})
                    self.tree.insert('', 'end', values=(legajo, fecha_extra, apellido_y_nombre))

                self.show_message("Bajas listadas correctamente.")
            else:
                self.show_message("No se encontraron bajas.")
        except Exception as e:
            self.show_message(f"Error al listar bajas: {e}")

  def exportar_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Archivos CSV", "*.csv")])
        if file_path:
            try:
                with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=['LEGAJO', 'FECHA_EXTRA', 'APELLIDO_Y_NOMBRE'])
                    writer.writeheader()
                    writer.writerows(self.bajas)
                
                self.show_message(f"Datos exportados correctamente a {file_path}.")
            except Exception as e:
                self.show_message(f"Error al exportar datos: {e}")

  def show_message(self, message):
        messagebox.showinfo("Información", message)
                  
  
