function filtrarProductos() {
  var textoBuscado = document.querySelector('.buscar').value.toLowerCase();
  var productos = document.querySelectorAll('.item');

  for (var i = 0; i < productos.length; i++) {
    var nombreProducto = productos[i].querySelector('.titulo-item').textContent.toLowerCase();
    var coincideExactamente = nombreProducto === textoBuscado;
    var contieneTexto = nombreProducto.includes(textoBuscado);

    if (coincideExactamente || contieneTexto || textoBuscado === '') {
      productos[i].style.display = 'block';
    } else {
      productos[i].style.display = 'none';
    }
  }
}

document.querySelector('.buscar').addEventListener('input', filtrarProductos);
