=====================================
 VFA PetShop - Proyecto Django
=====================================

Descripción:
------------
Aplicación web para la gestión de una tienda de mascotas,
desarrollada en Django 4.2.1 con Django REST Framework
y base de datos Oracle.

=====================================
 Requisitos previos
=====================================
- Python 3.10 o superior
- Oracle Database (o acceso a una instancia)
- Oracle Instant Client (para cx_Oracle)
- pip y virtualenv instalados

=====================================
 Instalación
=====================================

1. Clonar el repositorio:
   git clone https://github.com/V1xIN/VFa--PetShop-dj.git
   cd VFa--PetShop-dj

2. Crear un entorno virtual:
   python -m venv venv
   venv\Scripts\activate   (Windows)
   source venv/bin/activate   (Linux/Mac)

3. Instalar dependencias:
   pip install -r requirements.txt

4. Configurar base de datos Oracle en settings.py:
   ENGINE:   django.db.backends.oracle
   NAME:     127.0.0.1:1521/orcl
   USER:     vfadb
   PASSWORD: 12345678

   *Cambiar estos valores según tu instancia de Oracle.*

=====================================
 Crear usuario Oracle (opcional)
=====================================
Si necesitas crear un usuario para Django, puedes ejecutar el siguiente script SQL
como administrador en tu Oracle (por ejemplo, usando SQL*Plus o SQL Developer):

------------------------------------------------------
-- conectar como administrador
-- sqlplus sys/tu_password@127.0.0.1:1521/orcl AS SYSDBA

CREATE USER vfadb IDENTIFIED BY 12345678
DEFAULT TABLESPACE users
TEMPORARY TABLESPACE temp
QUOTA UNLIMITED ON users;

GRANT CONNECT, RESOURCE TO vfadb;
GRANT CREATE SESSION, CREATE TABLE, CREATE VIEW, CREATE SEQUENCE, CREATE TRIGGER TO vfadb;
GRANT CREATE PROCEDURE, ALTER SESSION TO vfadb;

-- probar conexión:
-- sqlplus vfadb/12345678@127.0.0.1:1521/orcl
------------------------------------------------------

=====================================
 Migraciones y ejecución
=====================================

1. Aplicar migraciones:
   python manage.py migrate

2. Crear superusuario (opcional):
   python manage.py createsuperuser

3. Ejecutar el servidor:
   python manage.py runserver

   Acceder en el navegador a:
   http://127.0.0.1:8000/

=====================================
 Aplicaciones incluidas
=====================================
- VFA_Pet    (lógica principal del sistema)
- rest_VfaPet (API REST con Django REST Framework)

=====================================
 Contribución
=====================================
1. Fork del repositorio
2. Crear nueva rama: git checkout -b feature/nueva-funcionalidad
3. Hacer commit: git commit -m "Descripción"
4. Push a la rama: git push origin feature/nueva-funcionalidad
5. Crear Pull Request