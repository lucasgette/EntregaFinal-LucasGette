const hamburguesa = document.querySelector('.hamburguesa')
const nav = document.querySelector('.lista-enlaces');

const tdImagen = document.querySelector('.new-post-form-table')

if(tdImagen) {
    const labelEliminarImagen = tdImagen.children[0].children[3].children[1].children[2]
    const casillaImagen = document.getElementById('blog_image-clear_id')
    labelEliminarImagen.outerHTML = '<p style="text-align:center"><label style="color:red" for="blog_image-clear_id">Tilda la casilla para eliminar la imagen actual</label></p><br>'
    casillaImagen.outerHTML= '<input style="margin-top:25px" type=\"checkbox\" name=\"blog_image-clear\" id=\"blog_image-clear_id\">'

}


hamburguesa.addEventListener('click', openNav)

function openNav() {
    // Para la pelotudez de la cruz
    console.log('HI')
    hamburguesa.classList.toggle('active'); 

    const nav = document.querySelector('.lista-enlaces');
    nav.classList.toggle("open");

    if(nav.classList.contains("open")) {
        nav.style.maxHeight = nav.scrollHeight + "px"

        if(listaControles.classList.contains('open')) {
            profileControl()
        }
    }

    else {
        nav.removeAttribute("style");
    }
}



const fotoPerfil = document.querySelector('.perfil-logo')

fotoPerfil.addEventListener('click', profileControl)


const listaControles = document.querySelector('.control-usuario');

function profileControl() { 
        
    listaControles.classList.toggle("open");

    if(listaControles.classList.contains("open")) {
        listaControles.style.maxHeight = listaControles.scrollHeight + "px" 
        
        if(nav.classList.contains("open")) {
            console.log('ABIERTOOOOO')
            openNav()
        }
    }

    else {
        listaControles.removeAttribute("style");
    }

}