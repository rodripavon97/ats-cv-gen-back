# CV Generator API

Este proyecto es una API construida con FastAPI para la generación de CVs y autenticación de usuarios. La base de datos utilizada es PostgreSQL, y se encuentra dockerizada para facilitar su despliegue.

## Requisitos

- Docker y Docker Compose
- Python 3.12

## Instalación y ejecución

1. Clona el repositorio:

   ```bash
   git clone <repo-url>
   cd cv-generator
   ```

2. Crea un archivo `.env` basado en el archivo de ejemplo (En caso):
> **¡Importante!** Si estás haciendo con Docker salta este paso.

   ```bash
   cp .env.example .env
   ```

   Ajusta las variable de entorno según tu configuración.
   DATABASE_URL=postgresql://postgres:admin@postgres_db:5432/mydatabase

3. Construye y levanta los contenedores:

   ```bash
   docker-compose up --build
   ```

4. Para detener los contenedores, usa:
   ```bash
   docker-compose down
   ```

## Acceso a la API

Una vez que la aplicación esté en ejecución, puedes acceder a la documentación de la API en:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Acceso a la base de datos

Para conectarte a la base de datos PostgreSQL dentro del contenedor, usa el siguiente comando:

```bash
 docker exec -it postgres_db psql -U postgres -d mydatabase
```

También puedes conectarte desde tu máquina local usando herramientas como DBeaver o pgAdmin con la siguiente configuración:

- Host: `localhost`
- Puerto: `5432`
- Usuario: `postgres`
- Contraseña: `admin`
- Base de datos: `mydatabase`
  

## Migraciones de base de datos

Este proyecto utiliza Alembic para la gestión de migraciones de la base de datos de forma síncrona.

### Crear una nueva migración

Para generar una nueva migración automáticamente según los modelos de SQLAlchemy:

```bash
docker exec -it fastapi_app alembic revision --autogenerate -m "descripcion de la migracion"
```

### Aplicar migraciones

Para aplicar las migraciones a la base de datos:

```bash
docker exec -it fastapi_app alembic upgrade head
```

### Revertir migraciones

Para deshacer la última migración:

```bash
docker exec -it fastapi_app alembic downgrade -1
```

## .gitkeep
No eliminar este archivo, se encarga de mantener la carpeta versions vacia.

## Autor

Desarrollado por SharedIt - 2025.
