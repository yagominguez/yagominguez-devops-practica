# services/Tienda_service.py

from typing import Dict, List
from Models.Usuario import Usuario, Cliente
from Models.Producto import Producto
from Models.Pedido import Pedido

# Creamos la clase TiendaService
class TiendaService:
    """
    Clase que gestiona el cerebro de la tienda online.
    """

    def __init__(self) -> None:
        # Aquí se guardan los datos principales de la tienda.
        # usuarios guarda a los clientes y admins con sus IDs.
        self.usuarios: Dict[str, Usuario] = {}
        # inventario guarda los productos de la tienda.
        self.inventario: Dict[str, Producto] = {}
        # 'pedidos' guarda todos los pedidos realizados.
        self.pedidos: List[Pedido] = []

    def registrar_usuario(self, usuario: Usuario) -> None:
        """
        Se registra un usuario en la tienda.
        """
        # Se comprueba si el usuario ya existe para evitar duplicados.
        if usuario.id in self.usuarios:
            print(f"Error: El usuario con ID {usuario.id} ya está registrado.")
        else:
            # Si no existe, se añade al diccionario de usuarios.
            self.usuarios[usuario.id] = usuario
            print(f"Usuario '{usuario.nombre}' registrado con éxito.")

    def anadir_producto_a_inventario(self, producto: Producto) -> None:
        """
        Añade un producto al inventario de la tienda.
        """
        # Se comprueba si el producto ya existe en el inventario.
        if producto.id in self.inventario:
            print(f"Error: El producto con ID {producto.id} ya está en el inventario.")
        else:
            # Si no existe, se añade al diccionario de inventario.
            self.inventario[producto.id] = producto
            print(f"Producto '{producto.nombre}' añadido al inventario.")

    def realizar_pedido(self, cliente_id: str, productos_solicitados: Dict[Producto, int]) -> None:
        """
        Procesa un nuevo pedido.
        """
        # Se comprueba si el cliente existe y si es realmente un Cliente (no un Admin).
        if cliente_id not in self.usuarios or not isinstance(self.usuarios[cliente_id], Cliente):
            print("Error: Cliente no encontrado o ID no válido.")
            return

        # Se recorre la lista de productos para verificar si hay stock suficiente.
        for producto, cantidad in productos_solicitados.items():
            if not producto.hay_stock(cantidad):
                print(f"Error: No hay suficiente stock para el producto '{producto.nombre}'.")
                return

        # Si el stock es suficiente, se actualiza el stock y creamos el pedido.
        for producto, cantidad in productos_solicitados.items():
            producto.actualizar_stock(-cantidad)

        # Se busca el objeto del cliente usando su ID.
        cliente = self.usuarios[cliente_id]
        # Se crea una nueva instancia de pedido con el cliente y los productos.
        nuevo_pedido = Pedido(cliente, productos_solicitados)
        # Se agrega el pedido nuevo a la lista general de pedidos de la tienda.
        self.pedidos.append(nuevo_pedido)
        # Mostrar la realización del pedido y sus detalles.
        print("Pedido realizado con éxito.")
        print(nuevo_pedido)

    def listar_usuarios(self) -> None:
        """
        Lista todos los usuarios registrados.
        """
        # Se verifica si hay usuarios para evitar un error.
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return
        # Se recorre el diccionario de usuarios y se imprime cada uno.
        for usuario in self.usuarios.values():
            print(usuario)

    def listar_productos(self) -> None:
        """
        Lista todos los productos en el inventario.
        """
        # Se verifica si el inventario está vacío.
        if not self.inventario:
            print("El inventario está vacío.")
            return
        # Se recorre el diccionario de productos y se imprime cada uno.
        for producto in self.inventario.values():
            print(producto)

    def listar_pedidos_usuario(self, cliente_id: str) -> None:
        """
        Lista todos los pedidos realizados por un cliente específico.
        """
        # Se filtran los pedidos para encontrar los del cliente, y se ordenan por fecha.
        pedidos_cliente = sorted(
            [p for p in self.pedidos if p.cliente.id == cliente_id],
            key=lambda p: p.fecha,
            reverse=True
        )

        # Se comprueba si el cliente tiene pedidos.
        if not pedidos_cliente:
            print("El cliente no tiene pedidos registrados.")
            return

        # Se imprime cada pedido del cliente.
        for pedido in pedidos_cliente:
            print(pedido)