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
    margin: 0px auto;
    max-width: 600px;
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

   
<script type="text/javascript">
function adjust_textarea(h) {
    h.style.height = "200px";
    h.style.height = (h.scrollHeight)+"px";
}
</script>

<script src="https://unpkg.com/vue@2.4.2"></script>
<script src="https://unpkg.com/vee-validate@2.0.0-rc.8"></script>
<script type="text/javascript">
Vue.use(VeeValidate);
new Vue({
  el: '#form',
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
