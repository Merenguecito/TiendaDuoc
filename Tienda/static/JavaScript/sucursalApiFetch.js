// uso de fetch

function apiFetch()
{
	const formulario = new FormData();
	formulario.append('txtId', document.getElementsByClassName("txtId")[0].value)

	fetch("/sucursalAjaxResponse",
	{ 
		method 	: "POST",
		body	: formulario
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
}