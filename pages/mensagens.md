---
layout: page
title: Pacce a Mensagem
description: Some description.
permalink: /mensagens/
ok: ok
menu: true
---

<img itemprop="image" class="img-rounded" src="http://pacceqx.github.io\assets\img\icons\read.svg" alt="Your Name" style="width: 160px;">
<h2 style="text-align: center;">PACCE A MENSAGEM</h2>
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
#msg{
  height: 300px; 
  width: 300px;
  text-align: justify;  
  margin-left: auto;
  margin-right: auto;
  font-family: 'Josefin Sans';
}
#titulo{
  font-weight:bold;
}
ul {
list-style-type: none;
}
li{
  margin:none;
}
</style>



<div class="container">  
        {% for mensagens in site.mensagens %}
      <div id="msg">
          <ul>
              <li><p id="titulo">De:</p>{{ mensagens.de  }}</li>
              <li><p id="titulo">Para:</p>{{ mensagens.para }}</li>
              <li id="titulo">Mensagem:</li><li>{{ mensagens.msg }}</li>
          </ul>
      </div>  
      {% endfor %}
    </div>
   