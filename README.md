# Tienda Online - Práctica 2.2

Una aplicación de tienda online desarrollada en Python que simula la gestión de usuarios, productos y pedidos, contenerizada en Docker

# Autor: Yago Mínguez Estévez

## Características
- Gestión de clientes y administradores
- Inventario de productos (electrónicos y ropa)
- Sistema de pedidos
- Actualización automática de stock

## Docker 
```bash

## Construcción de la Imagen

Para construir la imagen Docker de la aplicación:

```bash
docker build -t tienda-online .

## Ejecutar
docker run tienda-online
