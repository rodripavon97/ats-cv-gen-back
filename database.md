# Documentación Database

## Descripción General

  **Nombre base de datos:**
  **Base de Datos** (PostgreSQL)
  **Propósito:** Guardar los inputs de los CVs de cada usuario

## Tablas

  Nombre de la tabla: **app_user**
  Propósito: Almacena **datos básicos del usuario**, como nombre, apellido, email y contraseña
  **Campos/Columnas:** id (PK), first_name (text), last_name (text), email (text), password_hash (text), created_at (timestamptz), updated_at (timestamptz). Todo NOT NULL

  Nombre de la tabla: **cv**
  Propósito: Almacena **datos del CV**. Está **vinculada a la tabla app_user** y tiene otras tablas vinculadas a ella.
  **Campos/Columnas:** id (PK), app_user_id (FK), telephone (int), role (varchar-30), summary (text), created_at (timestamptz), updated_at (timestamptz). Todo NOT NULL

  Nombre de la tabla: **experience**
  Propósito: Almacena **datos de la experiencia**. Está **vinculada a la tabla cv**.
  **Campos/Columnas:** id (PK), cv_id (FK), role (varchar-30), company (text), start_date (date), end_date (date), description (text), created_at (timestamptz), updated_at (timestamptz). Todo NOT NULL, excepto end_date

  Nombre de la tabla: **skill*
  Propósito: Almacena **datos de las habilidades**. Está **vinculada a la tabla cv**.
  **Campos/Columnas:** id (PK), cv_id (FK), title (varchar-10), level (text["basic", "intermediate", "advanced"]), created_at (timestamptz), updated_at (timestamptz). Todo NOT NULL, excepto title, level
