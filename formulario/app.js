function getData()
{
    var nombre=document.getElementById("nombre").value;
    var edad=document.getElementById("edad").value;
    alert("Tu nombre es : "+nombre+ " y tienes " +edad+ " años");  
}
var elemento = document.getElementById("condiciones");
console.log(" Elemento: " + elemento.value + "\n Seleccionado: " + elemento.checked);
 
elemento = document.getElementById("privacidad");
console.log(" Elemento: " + elemento.value + "\n Seleccionado: " + elemento.checked);

 // Obtener la referencia a la lista
 var lista = document.getElementById("opciones");
 // Obtener el índice de la opción que se ha seleccionado
 var indiceSeleccionado = lista.selectedIndex;
 // Con el índice y el array "options", obtener la opción seleccionada
 var opcionSeleccionada = lista.options[indiceSeleccionado];
 // Obtener el valor y el texto de la opción seleccionada
 var textoSeleccionado = opcionSeleccionada.text;
 var valorSeleccionado = opcionSeleccionada.value;
 console.log("Opción seleccionada: " + textoSeleccionado + "\n Valor de la opción: " + valorSeleccionado);
 
 var lista = document.getElementById("opciones");
 // Obtener el valor de la opción seleccionada
 var valorSeleccionado = lista.options[lista.selectedIndex].value;
 // Obtener el texto que muestra la opción seleccionada
 var valorSeleccionado = lista.options[lista.selectedIndex].text;
  