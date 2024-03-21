async function visualizarFoto(evento) {
  const files = evento.target.files;
  const archivo = files[0];
  let filename = archivo.name;
  let extension = filename.split(".").pop();
  extension = extension.tolowerCase();
  if (extension !== "jpg") {
    evento.target.value = "";
    swal.fire("Seleccionar", "La imagen debe ser en formato JPG", "warning");
  } else {
    const objectURL = URL.createObjectURL(archivo);
    imagenProducto.setAttribute("src", objectURL);
  }
}

//ventana emergente de confirmacion para eliminar producto.

document.addEventListener('DOMContentLoaded', function () {
  const deleteIcons = document.querySelectorAll('.delete-icon');
  deleteIcons.forEach(icon => {
      icon.addEventListener('click', function (event) {
          event.preventDefault(); // Evitar el comportamiento predeterminado del enlace

          const productId = this.getAttribute('data-id');

          // ventana emergente
          Swal.fire({
              title: '¿Estás seguro de querer eliminar este producto?',
              icon: 'warning',
              showCancelButton: true,
              confirmButtonText: 'Sí',
              cancelButtonText: 'Cancelar'
          }).then((result) => {
              if (result.isConfirmed) {
                  window.location.href = '/eliminarProducto/' + productId;
              }
          });
      });
  });
});

//ventana emergente de confirmacion para editar producto.

document.addEventListener('DOMContentLoaded', function () {
  const editIcons = document.querySelectorAll('.edit-icon');
  editIcons.forEach(icon => {
      icon.addEventListener('click', function (event) {
          event.preventDefault(); // Evitar el comportamiento predeterminado del enlace

          const productId = this.getAttribute('data-id');

          // Mostrar la ventana de confirmación
          Swal.fire({
              title: '¿Estás seguro de querer editar este producto?',
              icon: 'warning',
              showCancelButton: true,
              confirmButtonText: 'Sí',
              cancelButtonText: 'Cancelar'
          }).then((result) => {
              // Si se hace clic en "Sí", redirigir para editar el producto
              if (result.isConfirmed) {
                  window.location.href = '/editarProducto/' + productId;
              }
          });
      });
  });
});


function cancelarRegistro() {
  window.location.href = '/iniciarSesion';
}

function visualizarFoto(event) {
  imagenProducto = document.getElementById('imagenProducto');
  
  if (event.target.files && event.target.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
          // Actualizar la fuente de la imagen con los datos del archivo seleccionado
          imagenProducto.src = e.target.result;
      }

      // Leer el archivo como una URL de datos
      reader.readAsDataURL(event.target.files[0]);
  } else {
      // Si no se seleccionó ningún archivo, establecer la fuente de la imagen como vacía
      imagenProducto.src = '';
  }
}