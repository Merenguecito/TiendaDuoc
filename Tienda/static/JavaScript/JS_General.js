
/* Set the width of the side navigation to 250px and the left margin of the page content to 250px */
function openNav() {
	document.getElementById("mySidenav").style.width = "400px";
	document.getElementById("main").style.marginRight = "370px";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
	document.getElementById("mySidenav").style.width = "0";
	document.getElementById("main").style.marginRight = "0";
}

 

function openUser() {
  document.getElementById("myUser").style.width = "400px";
	document.getElementById("main").style.marginRight = "370px";
  
  }

  /* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
  function closeUser() {
    document.getElementById("myUser").style.width = "0";
	  document.getElementById("main").style.marginRight = "0";
  
  }

/*function saludo(){
	alert("Wena Choro 2");
}*/



/*Restricciónes*/
$(function()
{
	let numeros = '1234567890';
	let letras  = 'qwertyuiopasdfghjklñzxcvbnm' +
				'QWERTYUIOPASDFGHJKLÑZXCVBNM' +
				'ÁÉÍÓÚáéíóú- ';	

	
	$('.txtRun').keypress(function(e)
	{
		let caracter = String.fromCharCode(e.which);
		if(numeros.indexOf(caracter) < 0)
			return false;
	})

	$('.txtNombre').keypress(function(e)
	{
		let caracter = String.fromCharCode(e.which);
		if(letras.indexOf(caracter) < 0)
			return false;
	})
	
	$('.btnEnviar').click(function()
	{
		let texto = "";
		texto = $('.txtCodigo').val();
		
		if(texto == '')
		{
			alert('No especificó el código');
			$('.txtCodigo').focus();
			return;
		}
		
		texto = $('.txtDescripcion').val();		
		if(texto == '')
		{
			alert('No especificó la descripción');
			$('.txtDescripcion').focus();
			return;
		}
		
		if($('.txtPrecioCosto').val() == '')
		{
			alert('No especificó precio costo');
			$('.txtPrecioCosto').focus();
			return;
		}
		
		if($('.txtPrecioVenta').val() == '')
		{
			alert('No especificó precio de venta');
			$('.txtPrecioVenta').focus();
			return;
		}
		
		alert("Los datos enviados son: \n" +
				$('.txtCodigo').val() + '\n' +
				$('.txtDescripcion').val() + '\n' +
				$('.txtPrecioVenta').val() + '\n' +
				$('.txtPrecioCosto').val()
				)
		let clave = /^[a-zA-Z0-9]{6,20}+$/
		let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,4})+$/
		if(!emailRegex.test($('.txtEmail').val()))
		{
			alert('Correo no válido');
		}
		
	});
	
})

/*
          // Example starter JavaScript for disabling form submissions if there are invalid fields
          (function() {
            'use strict';
            window.addEventListener('load', function() {
              // Fetch all the forms we want to apply custom Bootstrap validation styles to
              var forms = document.getElementsByClassName('needs-validation');
              // Loop over them and prevent submission
              var validation = Array.prototype.filter.call(forms, function(form) {
                form.addEventListener('submit', function(event) {
                  if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                  }
                  form.classList.add('was-validated');
                }, false);
              });
            }, false);
		  })();
		  */