# 🐾 VFa–PetShop  
Sistema de gestión para una tienda de mascotas desarrollado con **Django**, **SQLite**, **Bootstrap** y **Python**. Incluye módulos para administración, visualización de productos, gestión de clientes, compras, inventario y autenticación.

---

## 📌 Tecnologías utilizadas

- **Python 3.x**
- **Django 4.x** (o versión definida en `Requeriments.txt`)
- **SQLite3**
- **Bootstrap 4/5**
- **HTML / CSS / JavaScript**
- **Django Admin**
- **Entorno virtual (venv)**

---

## 📁 Estructura del proyecto

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/V1xIN/VFa--PetShop-dj.git
cd VFa--PetShop-dj

2. Crear entorno virtual

Windows

python -m venv venv
venv\Scripts\activate

Linux/Mac

python3 -m venv venv
source venv/bin/activate

3. Instalar dependencias
pip install -r Requeriments.txt

4. Aplicar migraciones
python manage.py migrate


Si deseas reiniciar la base y crear una nueva:

del db.sqlite3       # Windows
rm db.sqlite3        # Linux/Mac
python manage.py migrate

5. Crear un superusuario
python manage.py createsuperuser

6. Ejecutar el servidor
python manage.py runserver


Abrir en el navegador:

http://127.0.0.1:8000/

http://127.0.0.1:8000/admin/
