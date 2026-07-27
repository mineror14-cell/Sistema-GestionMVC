import tkinter as tk
from tkinter import ttk


class ProductoView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión de Productos (MVC)")
        self.geometry("750x500")
        self.controller = None

        # Formulario
        frame_form = ttk.LabelFrame(self, text=" Datos del Producto ", padding=10)
        frame_form.pack(fill="x", padx=10, pady=5)

        ttk.Label(frame_form, text="Código:").grid(row=0, column=0, padx=5, pady=5)
        self.txt_codigo = ttk.Entry(frame_form)
        self.txt_codigo.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=2, padx=5, pady=5)
        self.txt_nombre = ttk.Entry(frame_form)
        self.txt_nombre.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_form, text="Precio:").grid(row=1, column=0, padx=5, pady=5)
        self.txt_precio = ttk.Entry(frame_form)
        self.txt_precio.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Stock:").grid(row=1, column=2, padx=5, pady=5)
        self.txt_stock = ttk.Entry(frame_form)
        self.txt_stock.grid(row=1, column=3, padx=5, pady=5)

        # Botones
        frame_btn = ttk.Frame(self, padding=5)
        frame_btn.pack(fill="x", padx=10)

        self.btn_guardar = ttk.Button(frame_btn, text="Guardar Producto", command=self.on_guardar)
        self.btn_guardar.pack(side="left", padx=5)

        self.btn_eliminar = ttk.Button(frame_btn, text="Eliminar Seleccionado", command=self.on_eliminar)
        self.btn_eliminar.pack(side="left", padx=5)

        # Tabla (Treeview)
        frame_tabla = ttk.LabelFrame(self, text=" Inventario ", padding=10)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=5)

        self.tabla = ttk.Treeview(frame_tabla, columns=("ID", "Código", "Nombre", "Precio", "Stock"), show="headings")
        for col in ("ID", "Código", "Nombre", "Precio", "Stock"):
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100)
        self.tabla.pack(fill="both", expand=True)

    def set_controller(self, controller):
        self.controller = controller

    def on_guardar(self):
        if self.controller:
            self.controller.guardar_producto()

    def on_eliminar(self):
        if self.controller:
            self.controller.eliminar_producto()

    def mostrar_productos(self, lista):
        for row in self.tabla.get_children():
            self.tabla.delete(row)
        for item in lista:
            precio_formateado = f"${item['precio']:.2f}"
            self.tabla.insert("", "end", values=(item["id"], item["codigo"], item["nombre"], precio_formateado, item["stock"]))

    def limpiar_formulario(self):
        self.txt_codigo.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_precio.delete(0, tk.END)
        self.txt_stock.delete(0, tk.END)