# RaveReviews sitio web

## Miembros del grupo

El trabajo fue realizado en forma individual, siendo elaborado en su totalidad por mì (Lucas Gette).





## Configuración

En primer lugar, será necesario clonar el repositorio:

```sh
$ git clone https://github.com/lucasgette/EntregaFinal-LucasGette
$ cd EntregaFinal-LucasGette

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

El sitio cuenta con una página de inicio (home), con un mensaje de bienvenida al sitio. Para navegar por la página, el sitio cuenta con una barra de navegación, que nos permite acceder a sus diferentes secciones, las cuales incluyen:

* Inicio de sesión

En caso de contar con un usuario creado, a través del formulario de login se podrá iniciar sesión

* Registro 

Permite crear nuevos usuarios. Se trata de usuarios con permisos limitados. No tendrán acceso al panel de administración (para ello se deberá crear un superusuario)

* Mi perfil

En esta sección podemos ver nuestros datos de usuario. Para el caso del E-mail, la información no se mostrará a otros usuarios (permanece oculta). Podremos además editar nuestro perfil, agregar nombre, apellido, un avatar, descripción y sitio web.  En caso de que no se haya cargado un avatar, se asigna una imagen por defecto. En caso de no haber agregado una descipción o sitio web, este campo no aparecerá en el perfil.

Además, nos permitirá visualizar los posteos realizados.

* Buscador de usuarios

Permite buscar otros usuarios en base a su nombre de usuario. De esta forma, podemos acceder a su perfil, donde podremos ver sus datos (con excepción del email), y los posteos realizados por esta persona (y ver sus detalles).


* Buscador de posts

Permite buscar posteos realizados por cualquier persona, utilizando como criterio de búsqueda el título del post. En caso de haber coincidencias, devuelve un listado con las mismas, y un link de acceso a los detalles del post.

* Listado de todos los posts

Nos permite visualizar la lista de todos los posteos realizados, ya sea propios como ajenos. Para el caso de los post ajenos únicamente permite ver los detalles. Para los post propios permite además editarlos.

* Listado de posts propios

Nos permite visualizar la lista de todos los posteos realizado por nosotros mismos, con un acceso a sus detalles y permitiendo además borrarlos y editarlos.


* Creación de nuevos post

Permite crear un nuevo post, que incluirá un título, subtitulo, cuerpo (que se podrá crear con un editor de texto enriquecido), author, calificación (para calificar la película sobre la cual se está haciendo la publicación), y una imagen (la cual es opcional). Además, cada post contará con una fecha de creación (establecida cuando se crea el post) y de modificación (la ultima fecha en que fue modificado.)

* Edición de post:

Permite editar el título, subtitulo, cuerpo, calificación e imagen del post. Al editar un post, se generará una nueva fecha de modificación.

* Detalles del post

Permite visualizar para cada post su fecha de creación, fecha de modificación, autor, titulo, subtitulo, cuerpo, imagen, y además los comentarios realizados sobre cada post. En la parte inferior además habrá un formulario para que el usuario loggeado pueda publicar comentarios.



## Acceso al panel de administración

El sitio cuenta con un panel de administración, que nos permitirá acceder a nuestras bases de datos, y en ellas crear nuevos elementos, observar los elementos creados, modificarlos, borrarlos (CRUD).



Para ingresar al panel, con la totalidad de los permisos disponibles, previamente debemos crear un superusuario. Para ello, ingresar el siguiente código:

```sh
py manage.py createsuperuser
```

Y posteriormente ingresar el nombre de usuario y la contraseña a establecer. Una vez creado el superusuario, se puede ingresar al panel de navegación a través `http://127.0.0.1:8000/admin/`. El superusuario puede realizar cualquier tipo de tareas en el panel de administración, incluido crear nuevos usuarios y definir sus permisos.



Por defecto, y a efectos de la demostración del funcionamiento del sitio, se ha creado un super usuario, que ya cuenta con un perfil propio y un posteo realizado. 

usuario: admin
contraseña: admin123
