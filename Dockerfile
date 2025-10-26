# Imagen base de Python
FROM python:3.11-slim

# Configuraciones básicas para que Python no genere archivos extra
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# Carpeta donde se trabajará dentro del contenedor
WORKDIR /app

# Copiar el archivo con las dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar todo el resto del proyecto dentro del contenedor
COPY . .

# Indicar el puerto que se usará
EXPOSE 8000

# Comando para iniciar la aplicación FastAPI
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]
