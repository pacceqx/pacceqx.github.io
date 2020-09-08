---
layout: 
title: Presença da formação
description: Some description.
permalink: /enviar/
---

<img itemprop="image" class="img-rounded" src="http://pacceqx.github.io\assets\img\icons\read.svg" alt="Your Name" style="width: 160px;">
<h2 style="text-align: center;">Presença da formação</h2>
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
  margin: 0 auto;
}
.container3{ 
  margin: 0 auto;
}
#msg{
  height: 350px; 
  width: 290px;
  text-align: justify;  
  font-family: 'Josefin Sans';;
  background: #00afefff;
  margin-bottom: 5px;
}
#titulo{
  font-weight:bold;
}
ul {
list-style-type: none;
}
li{
  margin-left: -50px;
  margin-top: -20px;
}
.contact-form3 {
    font-family: 'Titillium Web', 'Helvetica Neue', Helvetica, sans-serif;
    font-weight: 700;
    font-style: normal;
    width: 310px;
    margin-left: -10px
}
.contact-form3 fieldset {
    border: none;
    font-weight: normal
}
.contact-form3 input[type="text"],
.contact-form3 input[type="para"],
.contact-form3 textarea {
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
.contact-form3 input[type="text"].has-error,
.contact-form3 input[type="para"].has-error,
.contact-form3 span {
    display: block;
    font-size: .875rem;
    color: #00afefff;
    padding-bottom: .625rem
}
.contact-form3 button[type="submit"] {
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
.contact-form3 button[type="submit"]:hover {
    background: rgb(43, 190, 243)
}
@media only screen and (min-width:37.5rem) {
    .contact-form3 button[type="submit"] {
        padding: 1.188rem 2.438rem 1.125rem 2.438rem
    }
}
.contact-form3 [v-cloak] {
    display: none
}
</style>

{% if site.email %}


<div class="container">  
        <div class="container2">
        <div id="form3" class="contact-form3">
            <form accept-charset="UTF-8" method="POST" action="https://formspree.io/{{ site.email }}"  ref="contact">
            <fieldset>
                <input type="hidden" name="_subject" value="New contact!" />
                <input type="hidden" name="_next" value="{{ site.url }}/contact/message-sent/" />
                <h3>Formação </h3>
                <input type="hidden" name="_language" value="{{ site.language }}" />
        <h5 >Nome:</h5><br>
                <input type="text" name="nome" placeholder="Seu nome ">
        <h5 >1. Escreva um pouco, com suas palavras, sobre o que você entende / aprendeu sobre proatividade.</h5><br>
                 <textarea name="pergunta1" onkeyup="adjust_textarea(this)" placeholder="Sua mensagem" ></textarea>
        <h5 >2. Sabemos que nem sempre o questionário será 100% fiel, há casos e casos. Mas, com base no que você respondeu, em que aspectos você avistou que pode melhorar? (Cite exemplos no projeto, na faculdade, no dia a dia, o que você julgar importante)</h5><br>
                 <textarea name="pergunta2" onkeyup="adjust_textarea(this)" placeholder="Sua mensagem" ></textarea>
        <h5 >3. O pacce ajudou você de alguma maneira no aspecto proativo? Se sim, conta pra gente.</h5><br>
                   <textarea name="pergunta3" onkeyup="adjust_textarea(this)" placeholder="Sua mensagem" ></textarea>
        <h5 >4. Há alguma história sobre proatividade que você gostaria de contar para contribuir com nosso diálogo? (Pode ser real ou que você viu em algum filme, por exemplo).</h5><br>
                  <textarea name="pergunta4" onkeyup="adjust_textarea(this)" placeholder="Sua mensagem" ></textarea>
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

   </div>
