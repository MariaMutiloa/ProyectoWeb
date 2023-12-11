function filtrarProductos() {
    var textoBuscado = document.querySelector('.buscar').value.toLowerCase();
    var productos = document.querySelectorAll('.item');
  
    for (var i = 0; i < productos.length; i++) {
      var nombreProducto = productos[i].querySelector('.titulo-item').textContent.toLowerCase();
      var coincideExactamente = nombreProducto === textoBuscado;
      var contieneTexto = nombreProducto.includes(textoBuscado);
  
      if (textoBuscado === '' || coincideExactamente || contieneTexto) {
        productos[i].style.display = 'block';
      } else {
        productos[i].style.display = 'none';
      }
    }
  }
  
  document.getElementById('btnBuscar').addEventListener('click', function() {
    console.log('Se ha hecho clic en el botón de búsqueda');
    filtrarProductos();
  });
  