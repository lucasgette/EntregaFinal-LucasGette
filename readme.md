# RaveReviews sitio web

## Configuración

En primer lugar, será necesario clonar el repositorio:

```sh
$ git clone https://github.com/lucasgette/Entrega-LucasGette.git
$ cd Entrega-LucasGette

```

Crear y activar un ambiente virtual en el cual instalaremos los paquetes necesarios para el proyecto:

```sh
$ py -m venv venv
$ . venv/scripts/activate
```

Estando activado el entorno virtual creado, instalar los paquetes necesarios a partir de requirements.txt:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` en la terminal nos indicará que está operando en el entorno virtual que hemos creado y denominado venv


Una vez que `pip` haya descargado e instalado los paquetes, podemos hacer correr el servidor:
```sh
(venv)$ python manage.py runserver
```

Luego, podremos navegar desde `http://127.0.0.1:8000/`.


## Navegar el sitio y conocer sus funcionalidades

El sitio cuenta con una página de inicio, en la que podemos ver 3 tarjetas con las 3 secciones principales del sitio:
* Peliculas
* Series
* Libros

Además, el sitio cuenta con una barra de navegación que permanece inalterada en todas las secciones, y nos permitirá navegar facilmente por todo el sitio.

En cada una de esas secciones, podemos:
* Observar un listado de los elemento registrados (ya sea peliculas, series, o libros)
* Cargar a través de un formulario, un nuevo elemento a registrar, el cual se agregará al listado y a la correspondiente base de datos.
* Acceder a través del boton "Buscar películas/series/libros" (según corresponda), a un buscador de los elementos en cuestión.
* Los buscadores permiten encontrar elementos según su nombre.


## Acceso al panel de administración

El sitio cuenta con un panel de administración, que nos permitirá acceder a nuestras bases de datos, y en ellas crear nuevos elementos, observar los elementos creados, modificarlos, borrarlos (CRUD).



Para ingresar al panel, con la totalidad de los permisos disponibles, previamente debemos crear un superusuario. Para ello, ingresar el siguiente código:

```sh
py manage.py createsuperuser
```

Y posteriormente ingresar el nombre de usuario y la contraseña a establecer. Una vez creado el superusuario, se puede ingresar al panel de navegación a través `http://127.0.0.1:8000/admin/`. El superusuario puede realizar cualquier tipo de tareas en el panel de administración, incluido crear nuevos usuarios y definir sus permisos.



Por defecto, se encuentra creado un usuario llamado staff, con algunas funcionalidades específicas limitadas (puede crear, actualizar y modificar elementos). 

usuario: staff
contraseña: interno123

## Funcionalidades en desarrollo

* Acceso al sitio con usuario y contraseña
* Cada usuario podrá registrar sus propias películas, series o libros
* Para cada elemento creado, el usuario podrá realizar puntuaciones y escribir una reseña del mismo (review)
* Cada usuario podrá editar, ver o eliminar sus propias reseñas.
* Los usuarios podrán buscar a otros usuarios y leer las reseñas que estos hayan escrito.