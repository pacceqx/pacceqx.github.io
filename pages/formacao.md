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
  border:none;
  overflow-Y: hidden;
  display:flex;
  flex-flow: row wrap;
  justify-content:space-between; 
  margin-left: 100px;
}

</style>
<script>
    function calcular() {
	    var fomulario = document.getElementById("formulario");
		var pg1  = formulario.pg1.value;
    var pg2  = formulario.pg2.value;
    var pg3  = formulario.pg3.value;
    var pg4  = formulario.pg4.value;
    var pg5  = formulario.pg5.value;
    var pg6  = formulario.pg6.value;
    var pg7  = formulario.pg7.value;
    var pg8  = formulario.pg8.value;
    var pg9  = formulario.pg9.value;
    var pg10 = formulario.pg10.value;
    var pg11 = formulario.pg11.value;
    var pg12 = formulario.pg12.value;
    var pg13 = formulario.pg13.value;
    var pg14 = formulario.pg14.value;
    var pg15 = formulario.pg15.value;
    var pg16 = formulario.pg16.value;
    var pg17 = formulario.pg17.value;
    var pg18 = formulario.pg18.value;
    var pg19 = formulario.pg19.value;
    var pg20 = formulario.pg20.value;
    
		soma =  parseInt (pg1) 
          + parseInt (pg2)
          + parseInt (pg3)
          + parseInt (pg4)
          + parseInt (pg5)
          + parseInt (pg6)
          + parseInt (pg7)
          + parseInt (pg8)
          + parseInt (pg9)
          + parseInt (pg10)
          + parseInt (pg11)
          + parseInt (pg12)
          + parseInt (pg13)
          + parseInt (pg14)
          + parseInt (pg15)
          + parseInt (pg16)
          + parseInt (pg17)
          + parseInt (pg18)
          + parseInt (pg19)
          + parseInt (pg20); 

      if((soma => 20) && (soma <= 40)){
        	alert ("SEU RESULTADO FOI: " + soma + " PONTOS \n  Sua PROATIVIDADE é um pouco baixa e, possivelmente, isso esteja se refletindo em alguns aspectos do seu cotidiano. Tomar consciência desta necessidade é o primeiro passo; o segundo é desenvolver um plano de ação. Converse um pouco mais consigo mesmo, e esteja aberto a receber mais feedback das pessoas.Seja mais observador do comportamento dos outros, especialmente daqueles que você considera muito bons nesta competência. Se precisar de ajuda, conta com a gente, pacceiro! \n Acesse o link para receber presença pela formação-->");
      }else if((soma > 40) && (soma <= 60)){
          alert ("SEU RESULTADO FOI: " + soma + " PONTOS \n Sua PROATIVIDADE é mediana. Você precisa desenvolvê-la um pouco mais, procurando melhorar naqueles aspectos em que sente mais dificuldade. Converse um pouco mais consigo mesmo, e esteja aberto a receber mais feedback das pessoas. Se precisar de ajuda, conta com a gente, pacceiro! \n Acesse o link para receber presença pela formação-->");
      }
      else if((soma > 60) && (soma <= 80)){
          alert ("SEU RESULTADO FOI:" + soma + " PONTOS \n Sua PROATIVIDADE é desenvolvida , mas você precisa estimular este comportamento nas pessoas, através de exemplos pessoais e da criação de um ambiente de abertura e confiança para sua equipe. Se precisar de ajuda, conta com a gente, pacceiro! \n Acesse o link para receber presença pela formação-->" );
      }
      else if(soma > 80){
          alert ("SEU RESULTADO FOI: " + soma + " PONTOS \n Sua PROATIVIDADE é bastante alta. Você é uma pessoa PROATIVA e estimula este comportamento nos outros, através de seu exemplo pessoal e criando um ambiente favorável à iniciativa de sua equipe. Parabéns, pacceiro! \n Acesse o link para receber presença pela formação-->" );
      } else{
        alert ("Você não fez a formação toda. Tente novamente. " + soma);
      }
	
    }


</script>


<div class="container">  
<form id="formulario">
<fieldset><br>
<br><br><label for="pergunta">1 - Você percebeu que ainda não teve nenhuma interação marcada pra essa semana. O que você faz?</label><br>
        <input type="radio" id="pg1" name="pg1" value="5">
        <label >Crio uma interação do zero</label><br>
        <input type="radio" id="pg1" name="pg1" value="4">
        <label >Marco uma interação com algum jogo online.</label><br>
        <input type="radio" id="pg1" name="pg1" value="3">
        <label >Mando uma indireta pro amigo marcar.</label><br>
        <input type="radio" id="pg1" name="pg1" value="2">
        <label >Pergunto pra Gabi se ela vai marcar alguma.</label><br>
        <input type="radio" id="pg1" name="pg1" value="1">
        <label >Deixo pra lá, afinal, a responsabilidade não é minha.</label><br>
<br><br><label for="pergunta">2 - Você vê um erro de digitação na arte que foi postada no instagram recentemente. O que faz?</label><br>
        <input type="radio" id="pg2" name="pg2" value="5">
        <label >Fala com quem fez a arte diretamente (se você souber)</label><br>
        <input type="radio" id="pg2" name="pg2" value="4">
        <label >Avisa pra Isa, afinal ela coordena a comunicação</label><br>
        <input type="radio" id="pg2" name="pg2" value="3">
        <label >Fala com a Lorena e vê se aquilo é certo ou errado</label><br>
        <input type="radio" id="pg2" name="pg2" value="2">
        <label >Manda mensagem no grupo geral com um print do erro</label><br>
        <input type="radio" id="pg2" name="pg2" value="1">
        <label >Deixa pra lá, isso já aconteceu antes.</label><br>
<br><br><label for="pergunta">3 -Vocês estão assistindo um filme online em uma interação e a internet da pessoa que está transmitindo está ruim e travando muito. O que você faz?</label><br>
        <input type="radio" id="pg3" name="pg3" value="5">
        <label >Pergunta se pode tentar transmitir do seu pc para todos. </label><br>
        <input type="radio" id="pg3" name="pg3" value="4">
        <label >Pergunta se alguém pode transmitir e testar se melhora.</label><br>
        <input type="radio" id="pg3" name="pg3" value="3">
        <label >Fala que é melhor remarcar para outro dia.</label><br>
        <input type="radio" id="pg3" name="pg3" value="2">
        <label >Deixa travando mesmo, não foi você que marcou a interação.</label><br>
        <input type="radio" id="pg3" name="pg3" value="1">
        <label >Comenta com outras pessoas que a interação foi muito ruim, porque travou muito.</label><br>
<br><br><label for="pergunta">4 - O pacce vai transmitir uma live, sobre um assunto “x”. O que você faz?</label><br>
        <input type="radio" id="pg4" name="pg4" value="5">
        <label >Você já compartilha com seu amigos, chamando pra assistir, comentando que vai ser legal.</label><br>
        <input type="radio" id="pg4" name="pg4" value="4">
        <label >Não compartilha, mas assiste a live e fica comentando no chat, pro pessoal interagir.</label><br>
        <input type="radio" id="pg4" name="pg4" value="3">
        <label >Espera a Kassiane pedir pra todo mundo compartilhar.</label><br>
        <input type="radio" id="pg4" name="pg4" value="2">
        <label >Não compartilha em lugar nenhum, porque você sabe que a Kassiane já compartilha em todos os lugares</label><br>
        <input type="radio" id="pg4" name="pg4" value="1">
        <label >Não preciso compartilhar, a comunicação serve pra isso</label><br>
<br><br><label for="pergunta">5 - A atividade da formação foi muito complicada de ser feita. O que você faz?</label><br>
        <input type="radio" id="pg5" name="pg5" value="5">
        <label >Fala com a Késsia para sugerir uma outra atividade</label><br>
        <input type="radio" id="pg5" name="pg5" value="4">
        <label >Fala no grupo que está com dificuldade de fazer a atividade</label><br>
        <input type="radio" id="pg5" name="pg5" value="3">
        <label >Não faz a atividade, mas se justifica com a Késsia do motivo.</label><br>
        <input type="radio" id="pg5" name="pg5" value="2">
        <label >Deixa pra lá, a reposição serve pra isso</label><br>
        <input type="radio" id="pg5" name="pg5" value="1">
        <label >Que formação? Tem formação?</label><br>
<br><br><label for="pergunta">6 - Você está na reunião semanal e percebe que o microfone da Kassiane não está funcionando bem. O que você faz?</label><br>
        <input type="radio" id="pg6" name="pg6" value="5">
        <label >Liga o microfone pra avisar pra ela.</label><br>
        <input type="radio" id="pg6" name="pg6" value="4">
        <label >Avisa no chat e espera que ela olhe</label><br>
        <input type="radio" id="pg6" name="pg6" value="3">
        <label >Espera que alguém avise</label><br>
        <input type="radio" id="pg6" name="pg6" value="2">
        <label >Não vou avisar, uma hora ela vai perceber</label><br>
        <input type="radio" id="pg6" name="pg6" value="1">
        <label >Só quero que a reunião acabe logo</label><br>
<br><br><label for="pergunta">7 - Vou organizar um evento. O que eu faço?</label><br>
        <input type="radio" id="pg7" name="pg7" value="5">
        <label >Falo logo com a Comunicação e pergunto o que preciso para fazer acontecer</label><br>
        <input type="radio" id="pg7" name="pg7" value="4">
        <label >Faço uns materiais de divulgação e peço feedback a uns amigos</label><br>
        <input type="radio" id="pg7" name="pg7" value="3">
        <label >Faço tudo sozinho e já saio compartilhando com os amigos</label><br>
        <input type="radio" id="pg7" name="pg7" value="2">
        <label >Deixo a Comunicação fazer toda a divulgação, já que é trabalho deles</label><br>
        <input type="radio" id="pg7" name="pg7" value="1">
        <label >Só anuncio e espero que tudo dê certo no dia</label><br>
<br><br><label for="pergunta">8 - Recebo mensagem dizendo ser hora da Reunião Individual. O que faço?</label><br>
        <input type="radio" id="pg8" name="pg8" value="5">
        <label >Respondo na hora e explico detalhadamente tudo o que tá acontecendo</label><br>
        <input type="radio" id="pg8" name="pg8" value="4">
        <label >Respondo que estou ocupada(o), mas que assim que estiver livre mando as respostas</label><br>
        <input type="radio" id="pg8" name="pg8" value="3">
        <label >Demoro muito pra responder, mas explico tudo o que tá acontecendo</label><br>
        <input type="radio" id="pg8" name="pg8" value="2">
        <label >Quando der, eu visualizo e respondo, mas de forma super sucinta</label><br>
        <input type="radio" id="pg8" name="pg8" value="1">
        <label >Deixo pra lá, todo mês tem reunião individual mesmo...</label><br>  
<br><br><label for="pergunta">9 - Você vê que não vai conseguir cumprir as horas semanais</label><br>
        <input type="radio" id="pg9" name="pg9" value="5">
        <label >Tento fazer algo a mais para cumprir as horas (crio uma interação, penso em algum campeonato, gravo algum vídeo de conteúdo pro canal, etc)</label><br>
        <input type="radio" id="pg9" name="pg9" value="4">
        <label >Pergunto pra Kassi se tem mais alguma coisa pra fazer</label><br>
        <input type="radio" id="pg9" name="pg9" value="3">
        <label >Pergunto se alguém precisa de ajuda com seus projetos, para completar as horas</label><br>
        <input type="radio" id="pg9" name="pg9" value="2">
        <label >Falo com a Kassi e justifica, e diz que irá compensar na semana seguinte</label><br>
        <input type="radio" id="pg9" name="pg9" value="1">
        <label >Deixo pra lá...</label><br>
<br><br><label for="pergunta">10 - Você vai fazer um evento na célula. O que você faz?</label><br>
        <input type="radio" id="pg10" name="pg10" value="5">
        <label >Planejo direitinho tudo que quero fazer e peço ajuda da Comunicação na parte da arte e divulgação</label><br>
        <input type="radio" id="pg10" name="pg10" value="4">
        <label >Divulgo no grupo da célula, já tá bom demais</label><br>
        <input type="radio" id="pg10" name="pg10" value="3">
        <label >Aviso para a Comunicação fazer as coisas em cima da hora</label><br>
        <input type="radio" id="pg10" name="pg10" value="2">
        <label >Não vou me preocupar com divulgação, já que no último evento algumas pessoas participaram</label><br>
        <input type="radio" id="pg10" name="pg10" value="1">
        <label >Acho melhor não divulgar. Menos pessoas, menos problemas</label><br>  
<br><br><label for="pergunta">11 - Kassiane avisa que as frequências da célula precisam ser entregues no final do mês. O que você faz?</label><br>
        <input type="radio" id="pg11" name="pg11" value="5">
        <label >Criei meu documento no início da célula, sempre atualizo a cada semana</label><br>
        <input type="radio" id="pg11" name="pg11" value="4">
        <label >Crio logo meu documento e faço, pra não esquecer depois</label><br>
        <input type="radio" id="pg11" name="pg11" value="3">
        <label >Deixo pra depois, ainda tem um mês todo pra fazer</label><br>
        <input type="radio" id="pg11" name="pg11" value="2">
        <label >No dia de entregar vou no grupo e peço o arquivo da planilha de frequência editável</label><br>
        <input type="radio" id="pg11" name="pg11" value="1">
        <label >Perco o prazo e espero a Kassiane cobrar de novo</label><br> 
<br><br><label for="pergunta">12 - Esqueceu / perdeu a noção do tempo para fazer Planejamento e Feedback. O que você faz?</label><br>
        <input type="radio" id="pg12" name="pg12" value="5">
        <label >Aviso pra Kassi que não consegui fazer a tempo e envio ainda de madrugada.</label><br>
        <input type="radio" id="pg12" name="pg12" value="4">
        <label >Mando mensagem para a Kassi e pergunto se posso entregar no dia seguinte</label><br>
        <input type="radio" id="pg12" name="pg12" value="3">
        <label >Sempre entrego atrasado, a Kassi já se acostumou</label><br>
        <input type="radio" id="pg12" name="pg12" value="2">
        <label >Eu sempre entrego, esquecer uma vez não faz mal</label><br>
        <input type="radio" id="pg12" name="pg12" value="1">
        <label >Não vou enviar, nem sei pra que serve</label><br>
<br><br><label for="pergunta">13 - Surgiu um desentendimento entre você e outro bolsista e você se sentiu ofendido. O que faz?</label><br>
        <input type="radio" id="pg13" name="pg13" value="5">
        <label >Falo com a pessoa em particular pra não virar uma bola de neve</label><br>
        <input type="radio" id="pg13" name="pg13" value="4">
        <label >Falo logo com a Kassi e desabafo o acontecido</label><br>
        <input type="radio" id="pg13" name="pg13" value="3">
        <label >Espero a reunião individual para falar sobre o assunto</label><br>
        <input type="radio" id="pg13" name="pg13" value="2">
        <label >Espero a pessoa falar comigo, afinal, foi ela que me ofendeu</label><br>
        <input type="radio" id="pg13" name="pg13" value="1">
        <label >Falo na frente de todos na reunião geral</label><br>
<br><br><label for="pergunta">14 - Alguém aparece pedindo informação sobre as coisas do PACCE. Como você age?</label><br>
        <input type="radio" id="pg14" name="pg14" value="5">
        <label >Me prontifico a responder, buscando informações</label><br>
        <input type="radio" id="pg14" name="pg14" value="4">
        <label >Mando o contato de uma pessoa do PACCE</label><br>
        <input type="radio" id="pg14" name="pg14" value="3">
        <label >Digo que estou ocupado e respondo quando der</label><br>
        <input type="radio" id="pg14" name="pg14" value="2">
        <label >Só respondo se for algo relacionado ao que eu faço</label><br>
        <input type="radio" id="pg14" name="pg14" value="1">
        <label >Falo que não conheço o projeto e pronto</label><br> 
<br><br><label for="pergunta">15 - Vi que um bolsista está passando por um sério problema familiar. O que faço?</label><br>
        <input type="radio" id="pg15" name="pg15" value="5">
        <label >Pergunto se posso ajudar nas suas atividades da semana</label><br>
        <input type="radio" id="pg15" name="pg15" value="4">
        <label >Falo pra Kassi, ela pode saber como agir nessa situação</label><br>
        <input type="radio" id="pg15" name="pg15" value="3">
        <label >Espero que alguém do grupo perceba e tome alguma atitude</label><br>
        <input type="radio" id="pg15" name="pg15" value="2">
        <label >Já já isso passa, qualquer coisa ele recupera depois</label><br>
        <input type="radio" id="pg15" name="pg15" value="1">
        <label >Cada um com seus problemas...</label><br>  
<br><br><label for="pergunta">16 - Estava nas redes sociais e vi um post falando mal do PACCE. Como devo agir?</label><br>
        <input type="radio" id="pg16" name="pg16" value="5">
        <label >Chamo a pessoa no privado para conversar e tentar resolver o desentendimento</label><br>
        <input type="radio" id="pg16" name="pg16" value="4">
        <label >Encaminho a publicação para a Gestão, eles podem resolver isso de uma boa maneira</label><br>
        <input type="radio" id="pg16" name="pg16" value="3">
        <label >Tiro um print e mando no grupo</label><br>
        <input type="radio" id="pg16" name="pg16" value="2">
        <label >Cada um fala o que quiser, deixa quieto</label><br>
        <input type="radio" id="pg16" name="pg16" value="1">
        <label >Finjo que nem vi</label><br>    
<br><br><label for="pergunta">17 - Estou em equipe da formação com pessoas que não colaboram. O que eu faço?</label><br>
        <input type="radio" id="pg17" name="pg17" value="5">
        <label >Insisto em incluir o pessoal o máximo possível</label><br>
        <input type="radio" id="pg17" name="pg17" value="4">
        <label >Faço a formação mesmo assim, é só uma semana</label><br>
        <input type="radio" id="pg17" name="pg17" value="3">
        <label >Falo com a Késsia com antecedência e explico a situação</label><br>
        <input type="radio" id="pg17" name="pg17" value="2">
        <label >Nem tento, vou direto pra reposição</label><br>
        <input type="radio" id="pg17" name="pg17" value="1">
        <label >Não faço formações em equipe</label><br>       
<br><br><label for="pergunta">18 - Você sabe que em uma semana não estará disponível para as atividades. O que você faz?</label><br>
        <input type="radio" id="pg18" name="pg18" value="5">
        <label >Falo com a Kassi, a Késsia e a Gabi explicando que estarei ausente</label><br>
        <input type="radio" id="pg18" name="pg18" value="4">
        <label >Coloco no planejamento que estarei ausente</label><br>
        <input type="radio" id="pg18" name="pg18" value="3">
        <label >Na semana seguinte, eu coloco no feedback que não pude participar das atividades</label><br>
        <input type="radio" id="pg18" name="pg18" value="2">
        <label >Espero alguém falar comigo e eu explico a situação</label><br>
        <input type="radio" id="pg18" name="pg18" value="1">
        <label >É só uma semana, ninguém vai notar</label><br> 
<br><br><label for="pergunta">19 - Você viu no site que está faltando uma notícia de um evento que já aconteceu. O que você faz?</label><br>
        <input type="radio" id="pg19" name="pg19" value="5">
        <label >Falo com alguém da comunicação</label><br>
        <input type="radio" id="pg19" name="pg19" value="4">
        <label >Pergunto no grupo por que a notícia não foi pro site ainda</label><br>
        <input type="radio" id="pg19" name="pg19" value="3">
        <label >Espero até o pessoal da comunicação colocar</label><br>
        <input type="radio" id="pg19" name="pg19" value="2">
        <label >Mando uma indireta no grupo</label><br>
        <input type="radio" id="pg19" name="pg19" value="1">
        <label >Deixo pra lá, o trabalho não é meu mesmo</label><br>
<br><br><label for="pergunta">20 - Alguém vai no grupo e pergunta quem está livre para um teste de live. Se você estiver livre, o que você faz?</label><br>
        <input type="radio" id="pg20" name="pg20" value="5">
        <label >Vou para o teste na hora, é bom que ajudo a galera</label><br>
        <input type="radio" id="pg20" name="pg20" value="4">
        <label >Vou, mas não passo muito tempo</label><br>
        <input type="radio" id="pg20" name="pg20" value="3">
        <label >Entro na live, mas não falo nada</label><br>
        <input type="radio" id="pg20" name="pg20" value="2">
        <label >Nem vale como interação, não tem pra que eu ir</label><br>
        <input type="radio" id="pg20" name="pg20" value="1">
        <label >Acho que isso é trabalho dos organizadores</label><br>                      
	<a href="#" onclick="calcular();">calcular</a>
</fieldset>
</form>
    </div>
   
