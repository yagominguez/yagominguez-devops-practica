# Tienda Online - Práctica 2.2

Esta es una aplicación desarrollada en Python que simula el funcionamiento completo de una tienda online y que ha sido contenerizada utilizando Docker para facilitar su despliegue y ejecución en cualquier entorno.
Para utilizar esta aplicación, primero debe construirse la imagen de Docker ejecutando el comando: docker build -t tienda-online .
Una vez construida la imagen, la aplicación puede ejecutarse con el comando: docker run tienda-online

El sistema simula una tienda online completa que incorpora las siguientes funcionalidades: Sistema de gestión de usuarios que diferencia entre clientes y administradores, Inventario de productos con categorías específicas para electrónica y ropa, Sistema completo de procesamiento de pedidos y un Mecanismo de actualización automática del stock tras cada compra. 

El proyecto está estructurado dentro de una carpeta src/, con los siguientes componentes principales: El archivo main.py sirve como punto de entrada principal de la aplicación, El directorio Models/ contiene las clases fundamentales: Usuario, Producto y Pedido, El directorio Services/ alberga la lógica principal del negocio, incluyendo la clase TiendaService. 

La aplicación incluye los siguientes archivos de configuración:
Dockerfile para la contenerización de la aplicación
.dockerignore para excluir archivos innecesarios en la construcción de la imagen Docker
.gitignore para el control de versiones con Git
requirements.txt qe especifica todas las dependencias de Python requeridas

Al ejecutar la aplicación mediante docker run tienda-online, se podrá observar este flujo de funcionamiento:
Registro automático de 3 clientes y 1 administrador en el sistema, Incorporación de 5 productos diferentes al inventario de la tienda, Procesamiento exitoso de 3 pedidos de ejemplo, Actualización automática de los niveles de stock tras cada transacción, Generación y visualización del historial completo de pedidos organizado por cliente. 

# Construir imagen

Docker build -t tienda-online .


## Docker
```bash
# Construir imagen
docker build -t tienda-online .

# Ejecutar
docker run tienda-online

# Descargar imagen desde Docker Hub (cuando esté disponible)
docker pull [usuario]/tienda-online:latest

# Opción 1 para el Pull: Descargar imagen desde Docker Hub
docker pull yagominguez/tienda-online:latest

# Opción 2: Construir localmente
docker build -t tienda-online .

# Ejecutar (con cualquier opción)
docker run tienda-online
