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

# Puerto por defecto para uso local (Render lo sobreescribe con su propia
# variable de entorno PORT en producción)
ENV PORT=5000
EXPOSE 5000

# Usamos gunicorn (servidor de producción) en vez del servidor de desarrollo
# de Flask. Escucha en el puerto indicado por la variable PORT, que Render
# asigna automáticamente al desplegar.
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT} app:app"]
