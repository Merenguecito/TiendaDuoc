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
				icon				: 'static/Images/logo.png',
				body				: mensaje,
				requireInteraction	: false
			}
		);
		
		notificacion.onclick = function(){
			window.open(url);
			//alert('click me');
		}
	}
}



setTimeout(function()
//setInterval(function()
{
	var titulo	= "Mi primera notificación";
	var mensaje	= "Holaaaa, soy una notificación :). Click me!!!";
	var url		= "https://google.cl"; //"/admin";
	notificar(titulo, mensaje, url);
	
}, 3000)