# Tienda Online - Práctica 2.2

Aplicación Python de tienda online contenerizada con Docker.
La aplicación simula una tienda online completa que incluye:
Gestión de usuarios, Inventario de productos, Sistema completo de pedidos, Actualización automática del stock
Se divide en: 
Carpeta 'Models/': Contiene las clases Usuario, Producto y Pedido
Carpeta 'Services/': Contiene la lógica principal del negocio
Archivo 'main.py': Es el punto de entrada principal de la aplicación

Incluye archivos de configuración:
Dockerfile: Configuración para contenerizar la aplicación
dockerignore: Archivos que Docker debe ignorar al construir la imagen
gitignore: Archivos que Git debe ignorar en el control de versiones
requirements.txt: Dependencias de Python necesarias

# Construir imagen

Docker build -t tienda-online .


## Docker
```bash
# Construir imagen
docker build -t tienda-online .

# Ejecutar
docker run tienda-online
