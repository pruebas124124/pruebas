# Usar una imagen base ligera de Python
FROM python:3.10-slim
# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app
# Copiar primero requirements.txt para aprovechar la caché
COPY requirements.txt .
# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt
# Copiar el resto de la aplicación
COPY app.py .
# Declarar el puerto que usa la aplicación (documentación)
EXPOSE 5000
# Comando para ejecutar la aplicación
CMD ["python", "app.py"]