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
}
#celula{
  height: 500px; 
  width: 250px;
  margin-left: auto;
  margin-right: auto;
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
   
