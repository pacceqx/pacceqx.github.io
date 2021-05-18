---
layout: page
title: Pacce a Mensagem
description: Some description.
permalink: /pacceamsg/
ok: ok
menu: true
---

<img itemprop="image" class="img-rounded" src="http://pacceqx.github.io\assets\img\icons\read.svg" alt="Your Name" style="width: 160px;">
<h2 style="text-align: center;">PACCE a Mensagem</h2>
<style type="text/css" media="screen">
.container{ 
    margin-left: auto;
  overflow-Y: hidden;
  display:flex;
  flex-flow: row wrap;
  justify-content:space-between; 
}
#msg{
  height: 600px; 
  width: 350px;
  text-align: justify;  
  background: #00afefff;
  font-size: 10px;
  margin-bottom: 20px;

  
}
ul {
list-style-type: none;
}
li{
  margin-left: -50px;
  margin-top: -20px;
  font-size: 15px;
  line-height: 20px;
}
.contact-form2 {
    font-family: 'Titillium Web', 'Helvetica Neue', Helvetica, sans-serif;
    font-weight: 700;
    font-style: normal;
    width: 400px;
    margin-left: -10px
}
.contact-form2 fieldset {
    border: none;
    font-weight: normal
}
.contact-form2 input[type="text"],
.contact-form2 input[type="para"],
.contact-form2 textarea {
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    outline: none;
    display: block;
    color: #333;
    width: 100%;
    border: none;
    border-bottom: 1px solid #ddd;
    font-family: inherit;
    font-size: 15px;
    height: 50px;
}
.contact-form2 input[type="text"].has-error,
.contact-form2 input[type="para"].has-error,
.contact-form2 span {
    display: block;
    font-size: .875rem;
    color: #00afefff;
    padding-bottom: .625rem
}
.contact-form2 button[type="submit"] {
    display: block;
    padding: .875rem 2.438rem .875rem 2.438rem;
    color: #fff;
    background: #00afefff;
    font-size: 1.125rem;
    width: 100%;
    border: 1px solid #00afefff;
    border-width: 1px 1px 3px;
    cursor: pointer;
    -webkit-transition: all .3s;
    transition: all .3s;
    outline: none;
    border-radius: 10px;
}
.contact-form2 button[type="submit"]:hover {
    background: rgb(43, 190, 243)
}
@media only screen and (min-width:37.5rem) {
    .contact-form2 button[type="submit"] {
        padding: 1.188rem 2.438rem 1.125rem 2.438rem
    }
}
.contact-form2 [v-cloak] {
    display: none
}
</style>



<div class="container">  

  <div id="form2" class="contact-form2">
    <form accept-charset="UTF-8" method="POST" action="https://formspree.io/{{ site.email }}"  ref="contact">
      <fieldset>
        <input type="hidden" name="_subject" value="New contact!" />
        <input type="hidden" name="_next" value="{{ site.url }}/contact/message-sent/" />
        <h3> Envie sua Mensagem</h3>
        <input type="hidden" name="_language" value="{{ site.language }}" />
        <input type="text" name="de" placeholder="Seu nome ou pseudônimo">
        <span v-cloak>${ errors.first('de') }</span>
        <input type="text" name="para" placeholder="Para quem vai sua mensagem">
        <span  v-cloak>${ errors.first('para') }</span>
        <input type="text" name="insta" placeholder="Instagram da pessoa que vai receber a mensagem">
        <span  v-cloak>${ errors.first('insta') }</span>
        <textarea name="message" onkeyup="adjust_textarea(this)" placeholder="Sua mensagem" ></textarea>
        <span  v-cloak>${ errors.first('message') }</span>
        <button type="submit">Enviar</button>
      </fieldset>
    </form>

</div>

   
