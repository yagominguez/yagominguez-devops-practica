# models/Pedido.py

# Importamos uuid4 para los identificadores únicos
from uuid import uuid4
# Importamos datetime para poder trabajar con fechas y horas actuales
from datetime import datetime
# Importamos Dict, para usar diccionarios, y Tuple para las Tuplas. 
from typing import Dict, Tuple

# El . delante, lo pongo para importarlo del paquete de (Models), lo que es lo mismo, del mismo paquete
from .Usuario import Cliente
from .Producto import Producto

# Creamos clase Pedido
class Pedido:
    """
    Representa un pedido realizado por un cliente en la tienda online.
    """

    def __init__(self, cliente: Cliente, productos: Dict[Producto, int]) -> None:
        """
        Inicializa un pedido con su ID único, el cliente que lo hizo, los productos comprados y la fecha actual.
        """
        # Se crea un ID único para el pedido para poder identificarlo.
        self.id: str = str(uuid4())
        # Guarda el objeto del cliente que realizó la compra.
        self.cliente: Cliente = cliente
        # Guarda un diccionario con los productos y la cantidad de cada uno.
        self.productos: Dict[Producto, int] = productos
        # Guarda la fecha y hora en que se creó el pedido automáticamente.
        self.fecha: datetime = datetime.now()

    def calcular_total(self) -> float:
        """
        Calcula el precio total del pedido sumando el costo de todos los productos.
        """
        # Recorre cada producto en el pedido, multiplica el precio por la cantidad y suma todo.
        return sum(producto.precio * cantidad for producto, cantidad in self.productos.items())

    def __str__(self) -> str:
        """
        Devuelve un resumen fácil de leer del pedido para mostrar en pantalla.
        """
        # Crea una lista de texto con cada producto, su cantidad y el subtotal.
        productos_str = "\n".join(
            f"   - {producto.nombre} x {cantidad} = {producto.precio * cantidad:.2f}€"
            for producto, cantidad in self.productos.items()
        )
        # Combinamos toda la información del pedido
        return (
            f"Pedido [{self.id}]\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M:%S')}\n"    #f string para fecha y hora 
            f"Productos:\n{productos_str}\n"
            f"Total: {self.calcular_total():.2f}€"
        )