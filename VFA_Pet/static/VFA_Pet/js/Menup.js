$(document).ready(function(){
    $("#formP").submit(function(p){
        
        var Nusuario = $("#correo").val().trim();
        var clave = $("#clave").val().trim();

        let msjMostrar = "";
        let enviar = false;
        let valClave= /(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/
        let email = /^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$/;

        if(!email.test(Nusuario)){
            msjMostrar = msjMostrar + "El Correo no es valido<br>";
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
            msjMostrar += "El  nombre de usuario no puede ser igual a la contraseña<br>";
            enviar = true;
        }
        
        if(enviar){
            p.preventDefault();
            $("#warnings").html(msjMostrar);
        }
        else{
            $("#warnings").html("Sesion correcta");
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