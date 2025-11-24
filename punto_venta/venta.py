from producto import producto
from cliente import Clientes

class venta: 
    def __init__(self, cliente: Clientes):
        self.cliente = cliente 
        self.productos: list[producto] =[]

    def agregar_producto(self, producto: producto) -> None:
        self.productos.append(producto)

    def total(self) -> float:
        return sum(p.precio for p in self.productos)
    