$(function () {

    $('.divListado').hide(); // show();

    $('.btnGrabar').click(function () {
            $.post("/sucursalAjaxResponse",
                    {
                            btnGrabar: 1,
                            txtId: $('.txtId').val(),
                            txtNombre: $('.txtNombre').val(),
                            txtDireccion: $('.txtDireccion').val(),
                            txtTelefono: $('.txtTelefono').val(),
                            txtEncargado: $('.txtEncargado').val()
                    },
                    function (data) {
                            alert(data['mensaje'])
                            limpiar();
                            $('.txtId').val();
                            $('.txtId').focus();
                    }
            )
                    .fail(function () {
                            alert('Error en la comunicación');
                    })

            return false;
    })
    $('.btnListar').click(function () {
            $('.tblBody').html('');
            $.post("/sucursalAjaxResponse",
                    {
                            btnListar: 1

                    },
                    function (data) {
                            for (reg in data) {
                                    $('.tblBody').append('<tr>' +
                                            '<td>' + data[reg]["id"] + '</td>' +
                                            '<td>' + data[reg]["nombre"] + '</td>' +
                                            '<td>' + data[reg]["modelo"] + '</td>' +
                                            '<td>' + data[reg]["precio_venta"] + '</td>' +
                                            '<td>' + data[reg]["precio_compra"] + '</td>' +
                                            '<td>' + data[reg]["stock"] + '</td>' +
                                            '<td>' + data[reg]["categoria"] + '</td>' +
                                            '<td>' + data[reg]["marca"] + '</td>' +
                                            '</tr>'
                                    );
                            }

                            $('.divListado').show();
                    }
            )
                    .fail(function () {
                            alert('Error en la comunicación');
                    })

            return false;
    })
        $('.btnBuscar').click(function () {
                $('.tblBody').html('');
                if($("txtBuscaCodigo").val()==" ")
                {
                        alert("Ingrese un código");
                }
                else
                {
                        $.post("/sucursalAjaxResponse",
                        {
                                btnBuscar: 1,
                                txtId : $(".txtBuscaCodigo").val()
                        },
                        function (data) {
                                $('.txtBuscaCodigo').val(data["id"])
                                $('.txtNombre').val(data["nombre"])
                        })
                        .fail(function () {
                                alert('Error en la comunicaciónes');
                        })
                }
                return false;
        })



    $('.btnLimpiar').click(function () {
            limpiar();
            $('.txtId').val('');
            $('.txtId').focus();
            $('.divListado').hide();
            $('.tblBody').html('');
            return false;
    })
    function limpiar() {
            $('.txtNombre').val('');
            $('.txtDireccion').val('');
            $('.txtTelefono').val('');
            $('.txtEncargado').val('');











            /*###### manifest.json
            
            {
                    "name"                                : "Carrito de compras",
                    "short_name"                : "CdC",
                    "Description"                : "Super carrito de compras online",
                    "background_color"        : "#454545",
                    "orientation"                : "portrait",
                    "display"                        : "standalone",
                    "start_url"                        : "../../sucursalApiFetch",
                    "scope"                                : "sucursalApiFetch",
                    "lang"                                : "es-CL",
                    "icon"                                : [        {
                                                                            "src"        : "../images/logo64.ico",
                                                                            "sizes"        : "64x64",
                                                                            "type"        : "images/ico"
                                                            "type"        : "images/ico"
                                                                    }]
            }
            
            #### notificaciones.js
            // notificaciones
            document.addEventListener('DOMContentLoaded', function()
            {
                    if(Notification.permission != 'granted')
                            Notification.requestPermission();
            })
            
            function notificar(titulo, mensaje, url)
            {
                    if(Notification.permission != 'granted')
                            Notification.requestPermission();
                    else
                    {// hay permiso para las notificaciones
                            var notificacion = new Notification(
                                    titulo,
                                    {
                                            icon                                : 'static/Images/logo.png',
                                            body                                : mensaje,
                                            requireInteraction        : false
                                    }
                            );
                            
                            notificacion.onclick = function(){
                                    //window.open(url);
                                    //alert('click me');
                            }
                    }
            }
            
            
            
            setTimeout(function()
            //setInterval(function()
            {
                    var titulo        = "Mi primera notificación";
                    var mensaje        = "Holaaaa, soy una notificación :). Click me!!!";
                    var url                = "https://google.cl"; //"/admin";
                    notificar(titulo, mensaje, url);
                    
            }, 1000)
            
            
            #### sucursalApiFetch.js
            
            // uso de fetch
            
            function apiFetch()
            {
                    const formulario = new FormData();
                    formulario.append('txtId', document.getElementsByClassName("txtId")[0].value)
            
                    fetch("/sucursalAjaxResponse",
                    { 
                            method         : "POST",
                            body        : formulario
                    })
                    .then(function(response)
                    {
                            return response.json();
                    })
                    .then(function(data)
                    {
                            document.getElementsByClassName("txtNombre")[0].value = data["nombre"];
                            document.getElementsByClassName("txtDireccion")[0].value = data["direccion"];
                            document.getElementsByClassName("txtTelefono")[0].value = data["telefono"];
                            document.getElementsByClassName("txtEncargado")[0].value = data["encargado"];
                    })
                    .catch(function(err)
                    {
                            alert('Error en la comunicación');
                    })
            }*/



    }
});