FROM python:3.11

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    ca-certificates \
    unixodbc-dev

# Agregar repositorio de Microsoft sin verificación de firma
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Instalar ODBC Driver 17 (sin verificación GPG)
RUN apt-get update --allow-insecure-repositories && \
    ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated msodbcsql17

# Copiar código
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Exponer puerto
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]