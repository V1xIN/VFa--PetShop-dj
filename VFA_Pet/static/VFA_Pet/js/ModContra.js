$(document).ready(function(){
    $("#formMod_Contra").submit(function(c){
        
        var Nusuario = $("#nameU").val().trim();
        var clave = $("#clave").val().trim();
        var Newclave = $("#new_clave").val().trim();
        var rep_Newclave = $("#rep_new_clave").val().trim();

        let letras = /^[a-zA-Z]+$/;
        let msjMostrar = "";
        let enviar = false;
        let valClave= /(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/


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


        if(!valClave.test(Newclave)){
            msjMostrar = msjMostrar + "La Contraseña nueva debe tener al menos un número o carácter especial y al menos una letra minúscula<br>";
            enviar = true;

        }
        

       
        if( Newclave.length < 8 || Newclave.length > 12){
            msjMostrar = msjMostrar + "La Contraseña nueva debe tener entre 8 y 12 caracteres<br>";
            enviar = true;
        } 
        

        if(clave == Newclave){
            msjMostrar += "La Contraseña nueva no puede ser igual a la anterior<br>";
            enviar = true;
        }

        if(rep_Newclave == Newclave){
            return true
        }else{
            msjMostrar += "Las contraseñas nuevas deben ser iguales"
            enviar = true;
        }







         if(enviar){
            c.preventDefault();
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