from modul import ProductoModel
from vista import ProductoView
from controlador import ProductoController

if __name__ == "__main__":
    model = ProductoModel()
    view = ProductoView()
    controller = ProductoController(model, view)
    view.mainloop()