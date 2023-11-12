# Equipo: Royal Tech
Tienda online de Casa de deportes
---

### Características
- Home: Describe la página web
- store: Residen los modelos y donde cargaremos los datos de los
              productos que se mostrarán en el 'Home'
- category: Ahí se encuentra el modelo 'Category' para los distintos
            tipos de productos que se agreguen al modelo 'Product'
---

### Lenguajes
- Python(Framework: Django)
- HTML
- CSS
---

### Documentación
Para correr el proyecto:
- Clone este proyecto
- Cree un ambiente virtual donde alojará el proyecto
- Diríjase a la raíz del proyecto e instale los requerimientos con: pip install -r requirements.txt
- Revise las migraciones con un 'py manage.py makemigrations' y luego 'py manage.py migrate'
- Cree su usuario para ingresar al administrador y agregar los datos a mostrar en el 'Home'
  con 'py manage.py createsuperuser'
- Ejecute el servidor con 'py manage.py runserver'
- diríjase a: http://localhost:8000/admin/ e inicie sesión con el usuario creado, luego
  comience a cargar los datos en el modelo 'Product'.
- Una vez cargado los datos, diríjase a: http://localhost:8000/ y revise que se vean los
  productos cargados como debe ser.
