$(document).ready(function(){
    $("#formRe").submit(function(r){
        r.preventDefault();
        var Nusuario = $("#nameU").val().trim();
        var Respuesta = $("#Respuesta").val().trim();

        let msjMostrar = "";
        let enviar = false;
        let letras = /^[a-zA-Z]+$/;
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
            $("#warnings").html("Datos Correctos!!");
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




