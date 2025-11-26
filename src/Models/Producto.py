# models/Producto.py

# Generar IDS para identificar a cada producto de forma única en el inventario.
from uuid import uuid4

#Crear clase Producto
class Producto:
    """
    Clase base que representa un producto genérico en la tienda online.
    """

    def __init__(self, nombre: str, precio: float, stock: int) -> None:
        """
        Inicializar un nuevo producto, con su ID único, nombre, precio y cantidad.
        """
        self.id: str = str(uuid4())
        self.nombre: str = nombre
        self.precio: float = precio #Numeros con decimales
        self.stock: int = stock

    def hay_stock(self, cantidad: int) -> bool:
        """
        Verificar si hay suficiente stock para la cantidad solicitada.
        """
        # Comprobar si el stock es igual o mayor a la cantidad que se quiere adquirir
        return self.stock >= cantidad

    def actualizar_stock(self, cantidad: int) -> None:
        """
        Actualiza el stock, sumando o restando unidades.
        """
        # Se añade la cantidad al stock. Si la cantidad es negativa, se resta. (para q el stock no baje de 0)
        if self.stock + cantidad < 0:
            raise ValueError("No hay suficiente stock para realizar esta operación.")
        # cantidad puede ser tanto positivo (para reponer), como negativo (para vender)
        self.stock += cantidad

    def __str__(self) -> str:
        """
        Devuelve una representación en texto del producto.
        """
        # Muestra el ID, nombre, precio y stock de forma legible.
        return f"[{self.id}] {self.nombre} - Precio: {self.precio:.2f}€ - Stock: {self.stock}"

#Hacer clase producto para productos electrónicos
class ProductoElectronico(Producto):
    """
    Representa un producto electrónico con meses de garantía. Hereda de la clase 'Producto'.
    """

    def __init__(self, nombre: str, precio: float, stock: int, garantia_meses: int) -> None:
        """
        Inicializa un producto electrónico, usando los datos del producto base y añadiendo la garantía.
        """
        # Llama al constructor del producto base para heredar sus atributos.
        super().__init__(nombre, precio, stock)
        self.garantia_meses: int = garantia_meses

    def __str__(self) -> str:
        # Devuelve una representación del producto, añadiendo la información de la garantía.
        return (
            f"[{self.id}] {self.nombre} (Electrónico) - "
            f"Precio: {self.precio:.2f}€ - Stock: {self.stock} - "
            f"Garantía: {self.garantia_meses} meses"
        )

#Hacer clase Producto para Ropa
class ProductoRopa(Producto):
    """
    Representa un producto de ropa con talla y color. Hereda de la clase 'Producto'.
    """

    def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str) -> None:
        """
        Inicializa un producto de ropa, usando los datos del producto base y añadiendo la talla y el color.
        """
        # Llama al constructor del producto base para heredar sus atributos.
        super().__init__(nombre, precio, stock)
        self.talla: str = talla
        self.color: str = color

    def __str__(self) -> str:
        # Devuelve una representación del producto, añadiendo la talla y el color.
        return (
            f"[{self.id}] {self.nombre} (Ropa) - "
            f"Precio: {self.precio:.2f}€ - Stock: {self.stock} - "
            f"Talla: {self.talla}, Color: {self.color}"
        )