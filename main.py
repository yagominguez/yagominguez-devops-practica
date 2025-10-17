# main.py

#Importo las Clases de los modelos de Usuario, Producto y Pedido, para poder crear instancias. 
from Models.Usuario import Cliente, Administrador
from Models.Producto import ProductoElectronico, ProductoRopa
from Models.Pedido import Pedido
from Services.Tienda_service import TiendaService

def main():
    """
    Esta es la función principal del sistema de tienda_online.
    """
    print(" Inicializando la tienda online ")
    tienda_service = TiendaService()

    #1. Se registran tres clientes (al menos) y un administrador (yo)
    print("\n Registrando usuarios ")
    cliente1 = Cliente("Carlos", "Carlos@email.com", "Rúa do Príncipe, 15, Vigo")
    cliente2 = Cliente("Ana", "ana@email.com", "Rúa de Policarpo Sanz, 20, Vigo")
    cliente3 = Cliente("Luis", "luis@email.com", "Avenida de Camelias, 50, Vigo")
    admin1 = Administrador("Admin_Yago", "admin.yago@email.com")

    # Se utiliza el método 'registrar_usuario' del servicio para añadir los usuarios
    tienda_service.registrar_usuario(cliente1)
    tienda_service.registrar_usuario(cliente2)
    tienda_service.registrar_usuario(cliente3)
    tienda_service.registrar_usuario(admin1)

    #Se muestra en consola los usuarios que se registran
    print("Usuarios registrados:")
    tienda_service.listar_usuarios()

    #2. Se Crean 5 productos de diferentes categorías y se añaden al inventario
    print("\n Creando y añadiendo productos al inventario ")
    ps5 = ProductoElectronico("PlayStation 5", 549.99, 10, 24)
    airpods = ProductoElectronico("AirPods Pro", 279.00, 50, 12)
    iphone = ProductoElectronico("iPhone 15 Pro", 1199.00, 25, 24)
    camiseta_armani = ProductoRopa("Camiseta Armani", 75.50, 20, "L", "Negro")
    sudadera_polo = ProductoRopa("Sudadera Polo", 99.99, 15, "M", "Azul")
    
    #Se añaden los productos al inventario 
    tienda_service.anadir_producto_a_inventario(ps5)
    tienda_service.anadir_producto_a_inventario(airpods)
    tienda_service.anadir_producto_a_inventario(iphone)
    tienda_service.anadir_producto_a_inventario(camiseta_armani)
    tienda_service.anadir_producto_a_inventario(sudadera_polo)

    #3. Listar los productos para comprobar el inventario
    # Se lista el inventario para verificar que se ha llenado correctamente.
    print("\n Inventario de productos actual ")
    tienda_service.listar_productos()

    #4. Simular pedidos
    # Se simulan 3 pedidos con productos definidos manualmente, además de la cantidad (también de forma manual) sin ser aleatorios.
    print("\n Simulando pedidos ")
    
    # Primer pedido de Carlos
    print("\nRealizando pedido 1 para Carlos")
    pedido1_productos = {ps5: 1, airpods: 1, camiseta_armani: 1}
    tienda_service.realizar_pedido(cliente1.id, pedido1_productos)
    
    # Segundo pedido de Ana
    print("\nRealizando pedido 2 para Ana")
    pedido2_productos = {iphone: 1, sudadera_polo: 1}
    tienda_service.realizar_pedido(cliente2.id, pedido2_productos)
    
    # Tercer pedido de Luis
    print("\nRealizando pedido 3 para Luis")
    pedido3_productos = {ps5: 1, iphone: 1, airpods: 1}
    tienda_service.realizar_pedido(cliente3.id, pedido3_productos)
    
    #5. Se comprueba el stock actualizado
    #Se vuelve a listar el inventario para ver los cambios después y variaciones de los pedidos.
    print("\n Inventario de productos después de los pedidos ")
    tienda_service.listar_productos()

    #6. Se comprueba el historial de pedidos de los clientes
    #Se muestra el historial de cada cliente
    print(f"\n Historial de pedidos de {cliente1.nombre} ")
    tienda_service.listar_pedidos_usuario(cliente1.id)

    print(f"\n Historial de pedidos de {cliente2.nombre} ")
    tienda_service.listar_pedidos_usuario(cliente2.id)

    print(f"\n Historial de pedidos de {cliente3.nombre} ")
    tienda_service.listar_pedidos_usuario(cliente3.id)
    
#Para que la función 'main' se ejecute solo cuando el script se inicie directamente.    
if __name__ == "__main__":
    main()
    