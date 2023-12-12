if(document.readyState == 'loading'){
    document.addEventListener('DOMContentLoaded', ready)
}else{
    ready();
}

function ready() {
    var botonPagar = document.querySelector('.btn-pagar');
    botonPagar.style.display = 'none';
    console.log("Botón de pagar seleccionado:", document.getElementsByClassName('btn-pagar')[0]);
    document.getElementsByClassName('btn-pagar')[0].addEventListener('click', pagarClicked);

    var botonesEliminarItem = document.getElementsByClassName('btn-eliminar');
    for (var i = 0; i < botonesEliminarItem.length; i++) {
        var button = botonesEliminarItem[i];
        button.addEventListener('click', eliminarItemCarrito);
    }

    var botonesSumarCantidad = document.getElementsByClassName('sumar-cantidad');
    for (var i = 0; i < botonesSumarCantidad.length; i++) {
        var button = botonesSumarCantidad[i];
        button.addEventListener('click', sumarCantidad);
    }

    var botonesRestarCantidad = document.getElementsByClassName('restar-cantidad');
    for (var i = 0; i < botonesRestarCantidad.length; i++) {
        var button = botonesRestarCantidad[i];
        button.addEventListener('click', restarCantidad);
    }

    var botonesAgregarAlCarrito = document.getElementsByClassName('boton-item');
    for (var i = 0; i < botonesAgregarAlCarrito.length; i++) {
        var button = botonesAgregarAlCarrito[i];
        button.addEventListener('click', agregarAlCarritoClicked);
    }

    document.getElementsByClassName('btn-pagar')[0].addEventListener('click', pagarClicked);
}

var botonPagar = document.getElementsByClassName('btn-pagar')[0];
botonPagar.style.display = 'block'

function pagarClicked() {
    var direccion = prompt('Por favor, ingresa tu dirección de entrega:');
    if (direccion !== null && direccion !== '') {
    alert('Gracias por comprar');

    var total = parseFloat(document.getElementsByClassName('carrito-precio-total')[0].innerText.replace('€', '').replace(',', '.'));
    var username = currentUser;

    var restaurante = idRestaurante;
    var carritoItems = document.getElementsByClassName('carrito-item');
    var productos = [];
    for (var i = 0; i < carritoItems.length; i++) {
        var item = carritoItems[i];
        var titulo = item.getElementsByClassName('carrito-item-titulo')[0].innerText;
        var precio = parseFloat(item.getElementsByClassName('carrito-item-precio')[0].innerText.replace('€', '').replace(',', '.'));
        var cantidad = parseInt(item.getElementsByClassName('carrito-item-cantidad')[0].value);
     
        var producto = {
            titulo: titulo,
            precio: precio,
            cantidad: cantidad
        };
        productos.push(producto);
    }

    var productosJSON = JSON.stringify(productos);
    
$.ajax({
    url: '/pedidos/guardar',
    type: 'POST',
    data: {
        importePedido: total,
        username: username,
        id_restaurante: restaurante,
        productos: productosJSON  
    },
    error: function(jqXHR, textStatus, errorThrown) {
        console.log("Error:", textStatus, errorThrown);
    },
    success: function(data) {

        console.log(data);

        var carritoContenedor = document.querySelector('.carrito-items');
        while (carritoContenedor.firstChild) {
            carritoContenedor.removeChild(carritoContenedor.firstChild);
    }
    actualizarTotalCarrito();
    }
});
} else {
    alert('Por favor, ingresa una dirección válida para realizar el pedido.');
}
}
    

  
function agregarAlCarritoClicked(event){
    console.log("Botón 'Añadir al carrito' clickeado");
    var button = event.target;
    var item = button.parentElement;
    var titulo = item.getElementsByClassName('titulo-item')[0].innerText;
    var precio = item.getElementsByClassName('precio-item')[0].innerText;
    var imagenSrc = item.getElementsByClassName('img-item')[0].src;
    console.log(imagenSrc);

    agregarItemAlCarrito(titulo, precio, imagenSrc);

    hacerVisibleCarrito();
}


// Mostramos el botón de pagar si hay productos en el carrito
function hacerVisibleCarrito() {
    carritoVisible = true;
    var carrito = document.getElementsByClassName('carrito')[0];
    carrito.style.marginRight = '0';
    carrito.style.opacity = '1';

    var elementosCarrito = document.getElementsByClassName('carrito-item');
    var hayProductos = elementosCarrito.length > 0;

    botonPagar.style.display = hayProductos ? 'block' : 'none'; 
}


function agregarItemAlCarrito(titulo, precio, imagenSrc){
    var item = document.createElement('div');
    item.classList.add = ('item');
    var itemsCarrito = document.getElementsByClassName('carrito-items')[0];

    var nombresItemsCarrito = itemsCarrito.getElementsByClassName('carrito-item-titulo');
    for(var i=0;i < nombresItemsCarrito.length;i++){
        if(nombresItemsCarrito[i].innerText==titulo){
            alert("El item ya se encuentra en el carrito");
            return;
        }
    }

    var itemCarritoContenido = `
        <div class="carrito-item">
            <img src="${imagenSrc}" width="80px" alt="">
            <div class="carrito-item-detalles">
                <span class="carrito-item-titulo">${titulo}</span>
                <div class="selector-cantidad">
                    <input type="text" value="1" class="carrito-item-cantidad" disabled>
                    <br>
                    <button class="btn-sumar-cantidad">+</button>
                    <button class="btn-restar-cantidad">-</button>
                </div>
                <span class="carrito-item-precio">${precio}</span>
            </div>
            <button class="btn-eliminar">Eliminar</button>
            </button>
        </div>
    `
    item.innerHTML = itemCarritoContenido;
    itemsCarrito.append(item);

     item.getElementsByClassName('btn-eliminar')[0].addEventListener('click', eliminarItemCarrito);

    var botonSumarCantidad = item.getElementsByClassName('btn-sumar-cantidad')[0];
    botonSumarCantidad.addEventListener('click',sumarCantidad);

    var botonRestarCantidad = item.getElementsByClassName('btn-restar-cantidad')[0];
    botonRestarCantidad.addEventListener('click',restarCantidad);

    actualizarTotalCarrito();
}


function sumarCantidad(event){
    var buttonClicked = event.target;
    var selector = buttonClicked.parentElement;
    console.log(selector.getElementsByClassName('carrito-item-cantidad')[0].value);
    var cantidadActual = selector.getElementsByClassName('carrito-item-cantidad')[0].value;
    cantidadActual++;
    selector.getElementsByClassName('carrito-item-cantidad')[0].value = cantidadActual;
    actualizarTotalCarrito();
}

function restarCantidad(event){
    var buttonClicked = event.target;
    var selector = buttonClicked.parentElement;
    console.log(selector.getElementsByClassName('carrito-item-cantidad')[0].value);
    var cantidadActual = selector.getElementsByClassName('carrito-item-cantidad')[0].value;
    cantidadActual--;
    if(cantidadActual>=1){
        selector.getElementsByClassName('carrito-item-cantidad')[0].value = cantidadActual;
        actualizarTotalCarrito();
    }
}

function eliminarItemCarrito(event) {
    var buttonClicked = event.target;
    buttonClicked.parentElement.parentElement.remove();
  
    // Verificamos si quedan productos en el carrito
    var carritoItems = document.getElementsByClassName('carrito-item');
    var hayProductos = carritoItems.length > 0;
  
    if (!hayProductos) {
      botonPagar.style.display = 'none';
    }
  
    actualizarTotalCarrito();
  }

  function actualizarTotalCarrito() {
    var carritoContenedor = document.querySelector('.carrito-items');
    var carritoItems = carritoContenedor.getElementsByClassName('carrito-item');
    var total = 0;

    for (var i = 0; i < carritoItems.length; i++) {
        var item = carritoItems[i];
        var precioElemento = parseFloat(item.querySelector('.carrito-item-precio').innerText.replace('€', '').replace(',', '.')); // Convertimos el precio a un número flotante

        var cantidadItem = item.querySelector('.carrito-item-cantidad');
        var cantidad = cantidadItem.value;

        total += precioElemento * parseInt(cantidad);
    }

    total = Math.round(total * 100) / 100;

    document.querySelector('.carrito-precio-total').innerText = total.toLocaleString("es", { style: 'currency', currency: 'EUR' });

    var botonPagar = document.querySelector('.btn-pagar');
    botonPagar.style.display = carritoItems.length > 0 ? 'block' : 'none'; 
}


