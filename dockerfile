# Usar una imagen de Python
FROM python:3.12-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar requirements.txt 
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Cambiar permisos (esto es lo que te falta)
RUN chmod +x main.py

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]