from cliente import Clientes
from producto import producto
from venta import venta
from tienda import Tienda

# Crear cliente 
cliente1 = Clientes("luis", "luis@mail.com", 1000)

# Crear productos
p1 = producto("teclado", 250)
p2 = producto("mouse", 150)

# Crear venta y agregar productos 
venta1 = venta(cliente1)
venta1.agregar_producto(p1)
venta1.agregar_producto(p2)

# Crear tienda y registrar venta
tienda = Tienda("techstore")
tienda.registrar_venta(venta1)

# Mostrar resultado
print(cliente1.mostrar_info())
print(f"total de la venta: ${venta1.total():.2f}")
print(f"ventas registradas: {len(tienda.ventas)}")
