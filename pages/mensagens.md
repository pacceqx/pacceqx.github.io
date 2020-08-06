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
.container { 
  overflow-Y: hidden;
  display:flex;
  flex-flow: row wrap;
  justify-content:space-between; 
  margin-left: -50px;
}
#msg{
  height: 500px; 
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
   
