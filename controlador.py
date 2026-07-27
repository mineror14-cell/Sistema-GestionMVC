from tkinter import messagebox


class ProductoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)
        self.cargar_tabla()

    def cargar_tabla(self):
        productos = self.model.obtener_productos()
        self.view.mostrar_productos(productos)

    def consultar_productos(self):
        self.cargar_tabla()
        messagebox.showinfo("Actualizado", "Inventario consultado correctamente")

    def guardar_producto(self):
        codigo = self.view.txt_codigo.get().strip()
        nombre = self.view.txt_nombre.get().strip()
        precio_str = self.view.txt_precio.get().strip()
        stock_str = self.view.txt_stock.get().strip()

        if not codigo or not nombre or not precio_str or not stock_str:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios")
            return

        try:
            precio = float(precio_str)
            stock = int(stock_str)
        except ValueError:
            messagebox.showerror("Error", "Precio y Stock deben ser números válidos")
            return

        exito = self.model.agregar_producto(codigo, nombre, precio, stock)
        if exito:
            messagebox.showinfo("Éxito", "Producto registrado correctamente")
            self.view.limpiar_formulario()
            self.cargar_tabla()
        else:
            messagebox.showerror("Error", "No se pudo guardar el producto")

    def eliminar_producto(self):
        selected = self.view.tabla.selection()
        if not selected:
            messagebox.showwarning("Atención", "Seleccione un registro de la tabla")
            return

        item = self.view.tabla.item(selected[0])
        producto_id = item["values"][0]

        if messagebox.askyesno("Confirmar", "¿Desea eliminar el producto seleccionado?"):
            if self.model.eliminar_producto(producto_id):
                messagebox.showinfo("Éxito", "Producto eliminado correctamente")
                self.cargar_tabla()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el registro")
                messagebox.showerror("Error", "No se pudo eliminar el registro")
