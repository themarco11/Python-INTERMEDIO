from venta import venta

class Tienda: 
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.ventas: list[venta] = []

    def registrar_venta(self, venta: venta) -> None:
        self.ventas.append(venta)
