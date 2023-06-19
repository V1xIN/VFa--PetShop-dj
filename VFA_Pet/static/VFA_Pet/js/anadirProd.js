$(document).ready(function(){
    $("#formP").submit(function(p){

        var codprod = $("#cod_producto").val().trim();
        var nomprod = $("#Nombrep").val().trim();
        var stock = $("#Stock").val().trim();
        var descripcion = $("#Descripcion").val().trim();
        var foto = $("#Foto").val().trim();
        var precio = $("#Precio").val().trim();
    
        let msjMostrar = "";
        let numeros = /^[0-9]+$/;
        let letras = /^[a-zA-Z]+$/;
        let imageRegex = /([^\s]+(?=\.(jpg|gif|png))\.\2)/gm;
    
        if(!numeros.test(codprod)){
            msjMostrar = msjMostrar + "El codigo solo debe contener numeros<br>";
            enviar = true;
        }
        if(!letras.test(nomprod)){
            msjMostrar = msjMostrar + "El nombre solo debe contener letras<br>";
            enviar = true;
        }
        if(nomprod.length < 4 || nomprod.length > 12){
            msjMostrar = msjMostrar + "El Producto debe tener entre 4 y 12 caracteres<br>";
            enviar = true;
        }
        if(!numeros.test(stock)){
            msjMostrar = msjMostrar + "El stock solo debe contener numeros<br>";
             enviar = true;
        }
    
        if(descripcion.length < 6 || descripcion.length > 20){

            msjMostrar = msjMostrar + "El Producto debe tener entre 6 y 100 caracteres<br>";
            enviar = true;
        }

        if(!imageRegex.test(foto)){
            msjMostrar = msjMostrar + "Archivo no valido<br>";
            enviar = true;
        }
        if(!numeros.test(precio)){
            msjMostrar = msjMostrar + "El precio solo debe contener numeros<br>";
            enviar = true;
        }




        if(enviar){
            p.preventDefault();
            $("#warnings").html(msjMostrar);
        }
        else{
            $("#warnings").html("Producto correcto correcta");
        }
    });


    

});