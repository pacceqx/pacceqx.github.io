---
layout: page
title: Conteúdos
description: Some description.
permalink: /conteudo/
menu: true
---

<?php
 $cod = $_POST['{{ celula.cod }}'];
 echo {{ celula.cod }};
?>
<img itemprop="image" class="img-rounded" src="http://pacceqx.github.io\assets\img\icons\read.svg" alt="Your Name" style="width: 160px;">
<h2 style="text-align: center; ">CONTEÚDO</h2>
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
  margin-left: -50px;
}
#celula{
  height: 500px; 
  width: 250px;
  text-align: center;
  margin-left: auto;
  margin-right: auto;
  font-family: 'Josefin Sans';
}
ul {
list-style-type: none;
}
</style>



<div class="container">  
{% assign conteudo = site.conteudo | where: "cod", page.conteudo | first %}
        {% for conteudo in site.conteudo %}
      <div id="celula">
          <ul>
              <li><img  src="{{ conteudo.photo }}" ></li>
          </ul>
      </div>  
      {% endfor %}
    </div>
   
