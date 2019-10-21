---
layout: page
title: Pacceiros
description: Some description.
permalink: /pacceiros/
menu: true
---

<img itemprop="image" class="img-rounded" src="http://pacceqx.github.io\assets\img\icons\read.svg" alt="Your Name" style="width: 160px;">
<h2 style="text-align: center;">PACCEIROS</h2>
<style type="text/css" media="screen">
.container { 
  overflow-Y: hidden;
  display:flex;
  flex-flow: row wrap;
  justify-content:space-between; 
  font-family: 'Josefin Sans', sans-serif;
  font-size: 1px;
  margin-left: -50px;
}
#celula{
  height: 500px; 
  width: 250px;
  text-align: center;
  
}
ul {
list-style-type: none;
}
</style>



<div class="container">  
        {% for pacceiro in site.pacceiros %}
      <div id="celula">
          <ul>
              <li><img  src="{{ pacceiro.photo }}" ></li>
              <li>{{ pacceiro.display_name  }}</li>
               <li>{{ pacceiro.curso }}</li>
              <li>{{ pacceiro.funcion }}</li>
          </ul>
      </div>  
      {% endfor %}
    </div>
   
