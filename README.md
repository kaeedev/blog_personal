## ESP:

# Proyecto de Blog de Noticias 📰🗞️

Esta es una página web sencilla sin estilos con varias vistas y funcionalidades como logearse, registrarse y desde el admin de django crear, modificar y borrar noticias. Todo realizado con **HTML** y **Django**. El proyecto también cuenta con vistas protegidas.
Se utiliza en este proyecto una base de datos MySQL para almacenar los usuarios y las noticias

## 🎯 Objetivo del Proyecto

El objetivo de este proyecto es crear una página web con funcionalidades y con una base de datos MySQL donde guardar los datos creados y los usuarios creados.

## 👁️ Vista previa del proyecto
<img src="img/preview.jpeg" width=1200>
<img src="img/preview2.jpeg" width=1200>

## 🛠️ Estructura del Proyecto

El proyecto está organizado en varias carpetas y archivos para facilitar su mantenimiento y expansión:

Una carpeta **blog_personal** que corresponderá a la "app" principal que se encargará de manejar templates y los settings del proyecto:
- Una carpeta **templates** donde recoge todos los HTMLs del proyecto con sus vistas correspondientes para noticias, login, register, contacto...
- **admin.py**: Fichero donde registramos y personalizamos nuestros modelos para que aparezcan en el admin de Django.
- **settings.py**: Fichero que recoge todos los ajustes del proyecto para poder funcionar.
- **urls.py**: Fichero donde definimos y conectamos nuestras urls principales.

Una carpeta **blogs** que corresponderá a una "subapp" que maneja el modelo noticias:
- Una carpeta **models** donde se crean los modelos de autor, editorial y libro.
- Una carpeta **urls** donde se definen las urls de autor, editorial y libro.
- Una carpeta **views** donde creamos las vistas de noticias y las vistas detalle de noticias.
- **admin.py**: Fichero donde registramos nuestros modelos para que puedan ser utilizados en el admin.

Una carpeta **core** que corresponderá a una "subapp" que maneja sitios principales de la web como home, login...:
- Una carpeta **models** donde se crean los modelos de a.
- Una carpeta **urls** donde se definen las urls de autor, editorial y libro.
- **forms.py** donde se crean los formularios independientes para lo que se necesite, como login o register.
- **views.py**: Fichero donde creamos nuestras vistas principales del proyecto, como home, login, register, contact.. Se usa CBV.
- **admin.py**: Fichero donde registramos nuestros modelos para que puedan ser utilizados en el admin.

**requirements.txt**: Fichero que recoge los requerimientos que hacen falta para que el proyecto funcione adecuadamente. Se deberán instalar en un nuevo entorno virtual


## 🚀 Funcionalidades y uso

- **Registro**: La página cuenta con un formulario para registrar usuarios que quedarán guardados en la base de datos. Es muy importante registrarse para
  poder utilizar todas las funcionalidades del proyecto, ya que el proyecto tiene vistas protegidas y funciones protegidas, como por ejemplo, para poder ver la lista completa de noticias o ver el detalle de una debemos registrarnos.
  
- **Iniciar sesión**: Podrás logearte con tu usuario
  
- **Agregar/Modificar/Borrar noticias con CSKEditor desde el admin**: Si tienes permiso para entrar al admin, puedes crear, modificar o borrar noticias


- **Posibilidad de contacto**: El proyecto cuenta con un formulario de contacto el cual está conectado a mi correo, por lo cual se puede contactar conmigo también de esta manera


- **Vistas protegidas**: Los usuarios que no estén logeados no podrán realizar funciones como ver todas las noticias o los detalles de una. Si lo intentan se les         
  redireccionará al login

- **Uso del admin**: Si te registras, puedes utilizar el admin de django con ese usuario poniendo /admin en el enlace

- **Protección en el admin**: Se ha configurado algunas protecciones en el admin, como por ejemplo que solo el superusuario puede crear en nombre de otro autor, modificar noticias de otros autores o incluso borrarlos. Mientras que el resto de usuarios solo pueden
  ver, crear, modificar y borrar sus propias noticias


## 🛠️ Instalación y Ejecución

1. Clona este repositorio:
   ```bash
   https://github.com/kaeedev/blog_personal.git

2. Crea un entorno virtual en el proyecto para instalar las dependencias necesarias:
   ```bash
   python3 -m venv venv
   
   ```
   o
   ```bash
   python -m venv venv
   ```

3. Inicia el entorno virtual que has creado:
   ```bash
   source venv/bin/activate

4. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

5. Ejecuta el programa:
   Deberás runear un servidor local
   ```bash
   python manage.py runserver
   ```

6. Usar el admin de django si lo deseas:
   ```bash
   Añadir /admin al final del enlace del servidor local

## 📝 Licencia

Este proyecto está disponible únicamente para uso **docente** y con fines de aprendizaje.

### Condiciones:
- El código fuente de este proyecto puede ser usado, modificado y distribuido solo con fines educativos.

Si tienes alguna duda o quieres utilizar algún recurso de este proyecto, por favor contacta conmigo.

---
## ENG:

# News Blog Project 📰🗞️
This is a simple webpage without styles with various views and functionalities such as logging in, registering, and creating, editing, and deleting news through Django's admin. The project also includes protected views. It uses a MySQL database to store users and news.

## 🎯 Project Objective
The goal of this project is to create a webpage with functionalities and a MySQL database to store created data and users.

## 👁️ Project Preview
<img src="img/preview.jpeg" width=1200> 
<img src="img/preview2.jpeg" width=1200>

## 🛠️ Project Structure
The project is organized into several folders and files to facilitate maintenance and expansion:

A blog_personal folder corresponding to the main "app" that handles templates and project settings:

A templates folder containing all the HTML files of the project with their corresponding views for news, login, register, contact...
admin.py: File where we register and customize our models to appear in the Django admin.
settings.py: File that contains all the project's settings to make it work.
urls.py: File where we define and connect our main URLs.
A blogs folder corresponding to a "subapp" that handles the news model:

A models folder where the models of author, editorial, and book are created.
A urls folder where the URLs of author, editorial, and book are defined.
A views folder where we create the views for news and detailed news views.
admin.py: File where we register our models to be used in the admin.
A core folder corresponding to a "subapp" that handles main sites of the web such as home, login...:

A models folder where the models of author are created.
A urls folder where the URLs of author, editorial, and book are defined.
forms.py where independent forms are created for login or registration.
views.py: File where we create our main views, such as home, login, register, contact.. It uses CBV.
admin.py: File where we register our models to be used in the admin.
requirements.txt: A file that contains the required dependencies for the project to function correctly. They should be installed in a new virtual environment.

## 🚀 Features and Usage
Registration: The page has a registration form for users, which are saved in the database. Registration is crucial for accessing all project functionalities, as it includes protected views and features, such as viewing the full list of news or the details of a news item, which require registration.

Login: You can log in with your user account.

Add/Edit/Delete News with CSKEditor from the Admin: If you have permission to access the admin, you can create, edit, or delete news.

Contact Option: The project includes a contact form connected to my email, so users can contact me this way.

Protected Views: Users who are not logged in cannot perform actions like viewing all news or the details of a news item. If they try, they will be redirected to the login page.

Admin Usage: If you register, you can use the Django admin with that user by visiting /admin.

Admin Protection: Some protections have been set in the admin, such as only allowing superusers to create news on behalf of other authors, edit news by other authors, or delete them. Regular users can only view, create, edit, and delete their own news.

## 🛠️ Installation and Running

1. Clone this repository:
   ```bash
   https://github.com/kaeedev/blog_personal.git

2. Create a virtual environment to install the necessary dependencies:
   ```bash
   python3 -m venv venv
   
   ```
   or
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   source venv/bin/activate

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the project: You'll need to run a local server:
   Deberás runear un servidor local
   ```bash
   python manage.py runserver
   ```

6. Use the django admin if you wish:
   ```bash
   Add /admin to the end of the local server URL
   
## 📝 License

This project is available for educational and learning purposes only.

### Conditions:

The source code of this project can be used, modified, and distributed for educational purposes only.
If you have any questions or want to use any resource from this project, feel free to contact me.
