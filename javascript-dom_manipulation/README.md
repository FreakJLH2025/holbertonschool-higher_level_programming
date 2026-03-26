JavaScript DOM Manipulation

Este proyecto contiene una serie de scripts en **JavaScript** que muestran cómo manipular el **DOM** en un navegador web.  
Cada ejercicio está vinculado a un archivo HTML de prueba y demuestra un aspecto clave de la interacción con elementos de la página.


📂 Contenido del proyecto

0-script.js
- Cambia el color del texto del elemento `<header>` a rojo (`#FF0000`).
- Uso de `document.querySelector`.

1-script.js
- Cambia el color del `<header>` a rojo cuando el usuario hace clic en el elemento con id `red_header`.
- Uso de `addEventListener('click', ...)`.

2-script.js
- Agrega la clase `red` al `<header>` cuando el usuario hace clic en el elemento con id `red_header`.
- Uso de `classList.add`.

3-script.js
- Alterna la clase del `<header>` entre `red` y `green` al hacer clic en el elemento con id `toggle_header`.
- Garantiza que el `<header>` siempre tenga exactamente una clase activa.

4-script.js
- Agrega un nuevo elemento `<li>Item</li>` a la lista con clase `my_list` cuando el usuario hace clic en el elemento con id `add_item`.
- Uso de `document.createElement` y `appendChild`.

5-script.js
- Actualiza el texto del `<header>` a **"New Header!!!"** cuando el usuario hace clic en el elemento con id `update_header`.
- Uso de `textContent`.

6-script.js
- Obtiene el nombre de un personaje de Star Wars desde la API:  
  `https://swapi-api.hbtn.io/api/people/5/?format=json`
- Muestra el nombre en el elemento con id `character`.
- Uso de la **Fetch API** y Promesas.

7-script.js
- Obtiene y lista los títulos de todas las películas de Star Wars desde la API:  
  `https://swapi-api.hbtn.io/api/films/?format=json`
- Inserta cada título como un `<li>` dentro del `<ul id="list_movies">`.

8-script.js
- Obtiene la traducción de “hello” en francés desde la API:  
  `https://hellosalut.stefanbohacek.com/?lang=fr`
- Muestra el valor en el elemento con id `hello`.
- Incluye `DOMContentLoaded` para asegurar que el DOM esté cargado antes de manipularlo.


🚀 Ejecución

1. Abre el archivo HTML correspondiente (ejemplo: `0-main.html`) en tu navegador.
2. El script enlazado (`0-script.js`) se ejecutará automáticamente y manipulará el DOM según lo especificado.


📖 Aprendizajes clave

- Selección de elementos con `document.querySelector`.
- Modificación de estilos y clases dinámicamente.
- Manejo de eventos (`click`).
- Creación y actualización de elementos en el DOM.
- Consumo de APIs externas con la **Fetch API** y manejo de Promesas.
- Diferencia entre manipulación directa del DOM y actualización basada en eventos.


✍️ Autor
Proyecto realizado como parte del programa de **Holberton School**.
