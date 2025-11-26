# models/Usuario.py

# Importo la función uuid4 del módulo 'uuid' para así generar identificadores únicos.
from uuid import uuid4

# Se crean las clases Usuario y administrador
class Usuario:
    """
    Clase base que representa a un usuario de la tienda online.
    """

    def __init__(self, nombre: str, email: str) -> None:
        """
        Inicializa un nuevo usuario. Por supuesto, con un ID único y sus propios datos.
        """
        self.id: str = str(uuid4())
        self.nombre: str = nombre
        self.email: str = email

    def is_admin(self) -> bool:
        """
        Se indica si el usuario es administrador.
        """
        # Un usuario normal no es admin.
        return False

    def __str__(self) -> str:
        """
        Devuelve una representación en texto del usuario.
        """
        # Muestra el ID, nombre y email del usuario.
        return f"[{self.id}] Usuario: {self.nombre} - Email: {self.email}"

# Se crea la clase Cliente
class Cliente(Usuario):
    """
    Es la clase que representa a un cliente de la tienda con dirección postal.
    Hereda de la clase padre 'Usuario'.
    """

    def __init__(self, nombre: str, email: str, direccion_postal: str) -> None:
        
        # Inicializa un cliente
        # Se llama al constructor de la clase padre (Usuario) para usar su ID, nombre y email.
        # uso super como función para ayudar con la herencia de las clases
        super().__init__(nombre, email)
        self.direccion_postal: str = direccion_postal

    def __str__(self) -> str:
        # Muestrar los datos del cliente, incluyendo su dirección postal.
        return (
            f"[{self.id}] Cliente: {self.nombre} - Email: {self.email} - "
            f"Dirección: {self.direccion_postal}"
        )

# Se crea la clase admin
class Administrador(Usuario):
    """
    Clase que representa a un administrador.
    Hereda de la clase padre 'Usuario'.
    """

    def __init__(self, nombre: str, email: str) -> None:
        """
        Inicializa un administrador.
        Se llama al constructor de Usuario para usar su ID, nombre y email.
        """
        super().__init__(nombre, email)

    def is_admin(self) -> bool:
        """
        El administrador siempre devuelve 'True'. Lo que indica que es siempre un Admin.
        """
        # Sobrescribe el método de la clase padre.
        return True

    def __str__(self) -> str:
        # Muestra que el usuario es un administrador.
        return f"[{self.id}] Administrador: {self.nombre} - Email: {self.email}"