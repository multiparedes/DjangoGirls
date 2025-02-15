# Django Girls Tutorial 🚀

Este repositorio contiene el código resultante de completar el tutorial oficial de Django Girls y su extensión.

## 📖 Sobre el Tutorial
El tutorial de Django Girls es una excelente introducción al desarrollo web con Django. A lo largo de él, se construye una aplicación web desde cero, aprendiendo sobre:

- Configuración de Django y su entorno
- Modelos, vistas y plantillas
- Despliegue de la aplicación en la nube
- Extensiones adicionales como pruebas y más funcionalidades

## 🛠️ Instalación y Uso

### 1️⃣ Clonar el Repositorio
```sh
git clone https://github.com/multiparedes/DjangoGirls.git
cd djangogirls
```
### 2️⃣ Crear un Entorno Virtual
```sh
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```
### 3️⃣ Instalar Dependencias
```sh
pip install -r requirements.txt
```

### 4️⃣ Crear un Superusuario
```sh
python manage.py createsuperuser
```
Sigue las instrucciones en la terminal para establecer un nombre de usuario, correo electrónico y contraseña.
Luego, accede al panel en http://127.0.0.1:8000/admin/ e inicia sesión con las credenciales creadas.


### 5️⃣ Aplicar Migraciones y Ejecutar el Servidor
```sh
python manage.py migrate
python manage.py runserver
```

Accede a http://127.0.0.1:8000/ en tu navegador.

## 🚀 Despliegue
Si deseas desplegar la aplicación en un servicio como Render o PythonAnywhere, puedes seguir las instrucciones del tutorial para deplegar en PythonAnywhere.

Accede a https://multiparedes.pythonanywhere.com/ para ver la versión completa del proyecto


## ✨ Mejoras y Extensiones

Tras completar el tutorial base, se implementaron las siguientes mejoras:

- 📌 Funcionalidades extra desde el tutorial de extensiones
- 🎨 Mejoras en el diseño con CSS

## 🔗 Enlaces Útiles

- 📘 [Tutorial oficial de Django Girls](https://tutorial.djangogirls.org/es/django_installation/)
- 🚀 [Extensiones del tutorial](https://tutorial-extensions.djangogirls.org/es/)
- 🌐 [Documentación oficial de Django](https://docs.djangoproject.com/es/5.1/)

Made with ❤️ by [Martí Paredes Salom](https://www.linkedin.com/in/martiparedessalom/)