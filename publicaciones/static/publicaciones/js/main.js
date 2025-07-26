// paso 1: seleccionar los actores (selectores que vamos a usar)
const botonMenu = document.getElementById('btn-hamburguesa');
const cerrarMenu = document.getElementById('boton-cerrar-menu');
const barraResponsiva = document.getElementById('menu-overlay')

// Explicación de las dos líneas de arriba:
// 'const' crea una variable que no va a cambiar. Es como una referencia fija a nuestros actores.
// 'botonMenu' es el nombre que le damos en nuestro script al actor con id="boton-menu".
// 'document.getElementById('boton-menu')' es la orden: "Oye, documento HTML, busca el elemento con el DNI 'boton-menu' y dámelo".
// 'barraLateral' es nuestro nombre para la barra lateral.
// 'document.querySelector('.barra-lateral')' es la orden: "Oye, documento, busca el primer elemento que coincida con el selector de CSS '.barra-lateral' y dámelo".

// ================================================================================================================================================================

// paso 2: escuchar el evento click en nuestro boton
botonMenu.addEventListener('click', () =>{
   // paso 3: logica que se ejecuta cada vez que se hace click
   barraResponsiva.classList.add('activo');

});

cerrarMenu.addEventListener('click', () =>{
    barraResponsiva.classList.remove('activo');
});


// categorias
const botonCategoria = document.getElementById('a-categoria');
const categorias = document.getElementById('opciones-categorias');

botonCategoria.addEventListener('click', () => {
    categorias.classList.toggle('activo');
    botonCategoria.classList.toggle('activo');
});

// publicaciones
const abrirPublicaciones = document.getElementById('a-publicaciones');
const opcionesPublicacion = document.getElementById('opciones-publicaciones');

abrirPublicaciones.addEventListener('click', () =>{
    abrirPublicaciones.classList.toggle('activo');
    opcionesPublicacion.classList.toggle('activo');
});


// barra lateral

const abrirCategoria = document.getElementById('id-categoria-lateral');
const elementosCategoria = document.getElementById('elementos-categoria');

abrirCategoria.addEventListener('click', () =>{
    abrirCategoria.classList.toggle('activo');
    elementosCategoria.classList.toggle('activo');
});

const abrirPublicacionLateral = document.getElementById('id-publicacion-lateral');
const elementosPublicacion = document.getElementById('elementos-publicacion');

abrirPublicacionLateral.addEventListener('click', () =>{
    abrirPublicacionLateral.classList.toggle('activo');
    elementosPublicacion.classList.toggle('activo');
});