function ocultarTodosLosRestaurantes() {
  var restaurantes = document.getElementsByClassName('restaurante');
  for (var i = 0; i < restaurantes.length; i++) {
    ocultarRestaurante(restaurantes[i]);
  }
}

function ocultarRestaurante(restaurante) {
  restaurante.style.display = 'none';
}

function mostrarRestaurante(restaurante) {
  restaurante.style.display = 'inline-block';
}

function filtrarRestaurantes() {
  var textoBuscado = document.getElementById('inputBuscar').value.toLowerCase();
  var restaurantes = document.getElementsByClassName('restaurante');

  if (textoBuscado === '') {
    ocultarTodosLosRestaurantes();
    return;
  }

  for (var i = 0; i < restaurantes.length; i++) {
    var restauranteNombre = restaurantes[i].textContent.toLowerCase();
    var coincideExactamente = restauranteNombre === textoBuscado;
    var contieneTexto = restauranteNombre.includes(textoBuscado);

    if (coincideExactamente || contieneTexto) {
      mostrarRestaurante(restaurantes[i]);
    } else {
      ocultarRestaurante(restaurantes[i]);
    }
  }
  console.log('El botón se ha hecho clic'); // Verificar si se ha ejecutado la función al hacer clic en el botón
}

document.getElementById('btnBuscar').addEventListener('click', filtrarRestaurantes);
