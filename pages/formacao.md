---
layout: page
title: Formação
description: Some description.
permalink: /formacao/
ok: ok
menu: true
---

<img itemprop="image" class="img-rounded" src="http://pacceqx.github.io\assets\img\icons\read.svg" alt="Your Name" style="width: 160px;">
<h2 style="text-align: center;">FORMAÇÃO</h2>
<style type="text/css" media="screen">
@font-face {
  font-family: 'Josefin Sans';
  font-style: normal;
  font-weight: 400;
  src: local('Josefin Sans Regular'), local('JosefinSans-Regular'), url(https://fonts.gstatic.com/s/josefinsans/v14/Qw3aZQNVED7rKGKxtqIqX5EUDXx9.ttf) format('truetype');
}
@font-face {
  font-family: 'Josefin Sans';
  font-style: normal;
  font-weight: 700;
  src: local('Josefin Sans Bold'), local('JosefinSans-Bold'), url(https://fonts.gstatic.com/s/josefinsans/v14/Qw3FZQNVED7rKGKxtqIqX5Ectllte10k.ttf) format('truetype');
}
.container { 
  overflow-Y: hidden;
  display:flex;
  flex-flow: row wrap;
  justify-content:space-between; 
  margin-left: 300px;
}

</style>
<script>
    function calcular() {
	    var fomulario = document.getElementById("formulario");
		var pg1 = formulario.pg1.value;
		var pg2 = formulario.pg2.value;
		soma = parseInt (pg1) + parseInt (pg2); 
		alert ("Soma" + soma);
    }


</script>


<div class="container">  
<form id="formulario">
<fieldset><br>
    <label for="pergunta">Pergunta 1</label><br>
        <input type="radio" id="pg1" name="pg1" value="5">
        <label for="pg1">Opção 1</label><br>
        <input type="radio" id="pg1" name="pg1" value="3">
        <label for="pg1">Opção 2</label><br>
        <input type="radio" id="other" name="pg1" value="2">
        <label for="other">Opção 3</label><br><br>
    <label for="pergunta">Pergunta 2</label><br>
        <input type="radio" id="pg2" name="pg2" value="5">
        <label for="pg2">Opção 1</label><br>
        <input type="radio" id="pg2" name="pg2" value="3">
        <label for="pg2">Opção 2</label><br>
        <input type="radio" id="other" name="pg2" value="2">
        <label for="other">Opção 3</label><br><br>
	<a href="#" onclick="calcular();">calcular</a>
</fieldset>
</form>
    </div>
   
