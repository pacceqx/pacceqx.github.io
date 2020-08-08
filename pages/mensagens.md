---
layout: page
title: Pacce a Mensagem
description: Some description.
permalink: /mensagens/
ok: ok
menu: true
---

<img itemprop="image" class="img-rounded" src="http://pacceqx.github.io\assets\img\icons\read.svg" alt="Your Name" style="width: 160px;">
<h2 style="text-align: center;">PACCE a Mensagem</h2>
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
.container{ 
  overflow-Y: hidden;
  display:flex;
  flex-flow: row wrap;
  justify-content:space-between; 
}
#msg{
  height: 340px; 
  width: 280px;
  text-align: justify;  
  font-family: 'Josefin Sans';;
  background-color: grey;
	border-radius: 10px;
}
#titulo{
  font-weight:bold;
}
ul {
list-style-type: none;
}
.contact-form2 {
    font-family: 'Titillium Web', 'Helvetica Neue', Helvetica, sans-serif;
    font-weight: 700;
    font-style: normal;
    width: 300px;
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
    font-size: 1.125rem;
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

{% if site.email %}
<style type="text/css" media="screen">
  .container2 {
  }
</style>

<div class="container">  
<div class="container2">
  <div id="form2" class="contact-form2">
    <form accept-charset="UTF-8" method="POST" action="https://formspree.io/{{ site.email }}"  ref="contact">
      <fieldset>
        <input type="hidden" name="_subject" value="New contact!" />
        <input type="hidden" name="_next" value="{{ site.url }}/contact/message-sent/" />
        <h3> Mensagem</h3>
        <input type="hidden" name="_language" value="{{ site.language }}" />
        <input type="text" name="de" placeholder="Seu nome ou pseudônimo">
        <span v-cloak>${ errors.first('de') }</span>
        <input type="text" name="para" placeholder="Para quem vai sua mensagem">
        <span  v-cloak>${ errors.first('para') }</span>
        <textarea name="message" onkeyup="adjust_textarea(this)" placeholder="Sua menssagem" ></textarea>
        <span  v-cloak>${ errors.first('message') }</span>
        <button type="submit">Enviar</button>
      </fieldset>
    </form>
  </div>

</div>

<script type="text/javascript">
function adjust_textarea(h) {
    h.style.height = "100px";
    h.style.height = (h.scrollHeight)+"px";
}
</script>

<script src="https://unpkg.com/vue@2.4.2"></script>
<script src="https://unpkg.com/vee-validate@2.0.0-rc.8"></script>
<script type="text/javascript">
Vue.use(VeeValidate);
new Vue({
  el: '#form2',
  delimiters: ['${', '}'],
  methods: {
    validateBeforeSubmit: function () {
      this.$validator.validateAll();
      if (!this.errors.any()) {
        this.$refs.contact.submit();
      }
    }
  }
});
</script>

{% else %}

<script>window.location = "{% if site.url == '' and site.baseurl == '' %}/{% else %}{{ site.url }}{{ site.baseurl }}{% endif %}";</script>

{% endif %}
        {% for mensagens in site.mensagens %}
      <div id="msg">
        <b>De:</b> {{ mensagens.de  }}<br>
             Para:</b> {{ mensagens.para }}<br>
                Mensagem:<br>
              {{ mensagens.msg }}
      </div>  
      {% endfor %}
    </div>
   
