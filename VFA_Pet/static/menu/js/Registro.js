$(document).ready(function(){
    $("#formRegistro").submit(function(a){
        a.preventDefault();
        var Rut = $("#rut").val().trim();
        var Nusuario = $("#nameU").val().trim();
        var Apellido = $("#Apellido").val().trim();
        var Correo = $("#correo").val().trim();
        var Telefono = $("#fono").val().trim();
        var clave = $("#clave").val().trim();
        var Respuesta = $("#Respuesta").val().trim();

        let msjMostrar = "";
        let enviar = false;
        let letras = /^[a-zA-Z]+$/;
        let valClave= /(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/
        let email = /^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$/;
        let rutt= /^[0-9]+[-|‐]{1}[0-9kK]{1}$/
        let phoneNumber = /^[0-9-()+]{3,20}/;



        if(!rutt.test(Rut)){
            msjMostrar = msjMostrar + "El Rut ingresado no es valido<br>";
            enviar = true;
        }



        if(Nusuario.length < 4 || Nusuario.length > 12){
            msjMostrar = msjMostrar + "El Usuario debe tener entre 4 y 12 caracteres<br>";
            enviar = true;
        } 
        var letra = Nusuario.charAt(0);
        if(!esMayuscula(letra)){
            msjMostrar += "El Usuario debe comenzar con mayúscla<br>";
            enviar = true;
        }
        if(!letras.test(Nusuario)){
            msjMostrar = msjMostrar + "El Usuario solo debe contener letras<br>";
            enviar = true;
        }




        if(Apellido.length < 4 || Apellido.length > 12){
            msjMostrar = msjMostrar + "El Apellido debe tener entre 4 y 12 caracteres<br>";
            enviar = true;
        } 
        var letra = Apellido.charAt(0);
        if(!esMayuscula(letra)){
            msjMostrar += "El Apellido debe comenzar con mayúscla<br>";
            enviar = true;
        }
        if(!letras.test(Apellido)){
            msjMostrar = msjMostrar + "El Apellido solo debe contener letras<br>";
            enviar = true;
        }



        if(!email.test(Correo)){
            msjMostrar = msjMostrar + "El Correo no es valido<br>";
            enviar = true;
        }

        if(!phoneNumber.test(Telefono)){
            msjMostrar = msjMostrar + "El número de teléfono ingresado no es valido<br>";
            enviar = true;
        }


        if(!valClave.test(clave)){
            msjMostrar = msjMostrar + "La Contraseña debe tener al menos un número o carácter especial y al menos una letra minúscula<br>";
            enviar = true;

        }
        if( clave.length < 8 || clave.length > 12){
            msjMostrar = msjMostrar + "La Contraseña debe tener entre 8 y 12 caracteres<br>";
            enviar = true;
        } 
        if(Nusuario == clave){
            msjMostrar += "El nombre de usuario no puede ser igual a la contraseña<br>";
            enviar = true;
        }

        if(Respuesta.length < 6 || Nusuario.length > 15){
            msjMostrar = msjMostrar + "La Respuesta debe tener entre 6 y 15 caracteres<br>";
            enviar = true;
        }
        if(!letras.test(Respuesta)){
            msjMostrar = msjMostrar + "La Respuesta solo debe contener letras<br>";
            enviar = true;
        }
    









        if(enviar){
            $("#warnings").html(msjMostrar);
        }
        else{
            $("#warnings").html("Usuario Registrado!!");
        }

    });
    function esMayuscula(letra){
        if(letra == letra.toUpperCase()){
            return true
        }
        else{
            return false
        }



    }

});