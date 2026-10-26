---
id: "https://developer.sankhya.com.br/reference/api-de-integrações-sankhya"
titulo: "API de Serviços Gateway"
url: "https://developer.sankhya.com.br/reference/api-de-integrações-sankhya"
atualizado_em: "2025-11-10T23:38:54.000Z"
---

# API de Serviços Gateway

## Requisitos para Integração

<HTMLBlock>{`
<p>Na era da interconectividade, a integra&ccedil;&atilde;o de sistemas &eacute; um pilar essencial para a efici&ecirc;ncia empresarial. Destacaremos aqui os requisitos essenciais para integrar uma solu&ccedil;&atilde;o aditicional &agrave; plataforma de gest&atilde;o Sankhya com sucesso. Ser&aacute; apresentado desde a conformidade com padr&otilde;es estabelecidos&nbsp;at&eacute; a mitiga&ccedil;&atilde;o de riscos, exploraremos como adotar uma abordagem padronizada pode simplificar processos, promover a escalabilidade e garantir a seguran&ccedil;a dos dados. Descubra as vantagens ineg&aacute;veis e os perigos potenciais de ignorar esses princ&iacute;pios fundamentais de integra&ccedil;&atilde;o.</p>

<p>Mas, quais s&atilde;o os requisitos essenciais para a integra&ccedil;&atilde;o com a Plataforma Sankhya? O processo de integra&ccedil;&atilde;o &eacute; composto por autentica&ccedil;&atilde;o e requisi&ccedil;&otilde;es autorizadas, facilitadas atrav&eacute;s de nossa API Gateway. A imagem a seguir oferece uma ilustra&ccedil;&atilde;o clara do funcionamento desse processo.</p>

<p><img alt="Fluxo de Integração com a Plataforma de Gestão Sankhya" height="470" src="https://files.readme.io/918c48f-api_gt.gif" width="744" /></p>

<p>&nbsp;</p>

<p>Para integrar com a plataforma de gest&atilde;o SankhyaOm, &eacute; imprescind&iacute;vel utilizar a API Gateway, respons&aacute;vel por encaminhar todas as requisi&ccedil;&otilde;es para as respectivas plataformas de gest&atilde;o SankhyaOm.&nbsp;Mas quais s&atilde;o os pr&eacute;-requisitos para realizar essa integra&ccedil;&atilde;o? Vamos explorar os pontos fundamentais para o primeiro acesso que &eacute; a&nbsp;autentica&ccedil;&atilde;o do acesso. Aqui est&atilde;o os requisitos essenciais para autenticar e fazer requisi&ccedil;&otilde;es usando a API Gateway:</p>

<ul>
	<li>AppKey: A AppKey (Chave de Aplica&ccedil;&atilde;o) &eacute; &uacute;nica e identifica a aplica&ccedil;&atilde;o integrada e o&nbsp;parceiro integrador em todas as transa&ccedil;&otilde;es realizadas via API Gateway.&nbsp;&Eacute; crucial observar que a AppKey &eacute; estritamente exclusiva e intransfer&iacute;vel, portanto, n&atilde;o deve ser compartilhada com terceiros.</li>
	<li>SankhyaID: O SankhyaID &eacute; uma maneira segura de fazer login no ecossistema Sankhya (SankhyaOm, Universidade, Portal do Cliente, entre outros), consistindo em um e-mail v&aacute;lido e uma senha. O parceiro integrador deve criar um SankhyaID para autentica&ccedil;&atilde;o via API Gateway.</li>
	<li>Token: O cliente deve conceder acesso ao parceiro integrador atrav&eacute;s do SankhyaOm. Essa concess&atilde;o de acesso implica em autorizar a aplica&ccedil;&atilde;o do parceiro, gerando assim um token. Esse token &eacute; a chave que conecta a aplica&ccedil;&atilde;o do parceiro integrador &agrave; Plataforma de Gest&atilde;o SankhyaOm utilizada pelo cliente.</li>
	<li>Camada de Autoriza&ccedil;&atilde;o: Toda transa&ccedil;&atilde;o realizada atrav&eacute;s da API Gateway passa por uma camada de autoriza&ccedil;&atilde;o integrada &agrave; plataforma de gest&atilde;o SankhyaOm. Para implementar essa camada, durante a cria&ccedil;&atilde;o do token, &eacute; necess&aacute;rio vincular um usu&aacute;rio existente no SankhyaOm. As permiss&otilde;es de acesso concedidas &agrave; aplica&ccedil;&atilde;o do parceiro integrador na plataforma SankhyaOm est&atilde;o ligadas a esse usu&aacute;rio utilizado na cria&ccedil;&atilde;o do token. Isso significa que, para liberar ou restringir acessos &agrave; aplica&ccedil;&atilde;o do parceiro integrador, basta configurar as permiss&otilde;es desse usu&aacute;rio.</li>
</ul>

<p>Para que este fluxo de integra&ccedil;&atilde;o seja poss&iacute;vel, &eacute; crucial que o acesso ao SankhyaOm do cliente esteja autorizado para a API Gateway, independentemente da localiza&ccedil;&atilde;o da infraestrutura utilizada para fornecer o SankhyaOm, seja ela interna ou externa.</p>

<p>A imagem a seguir exemplifica o funcionamento pr&aacute;tico do processo:</p>

<p><img alt="" height="256" src="https://files.readme.io/f03ee6f-Cenario_2.jpg" width="954" /></p>

<p>Com isso, torna-se vi&aacute;vel efetuar requisi&ccedil;&otilde;es para obter e enviar dados &agrave; plataforma de gest&atilde;o SankhyaOm, fazendo uso da API Gateway, o meio recomendado e oficial pela Sankhya. Agora, vamos analisar de forma clara os principais benef&iacute;cios de realizar integra&ccedil;&otilde;es dessa maneira:</p>

<ul>
	<li>Seguran&ccedil;a e compliance nas integra&ccedil;&otilde;es externas: Atrav&eacute;s da aplica&ccedil;&atilde;o de libera&ccedil;&otilde;es de acesso e camadas de autoriza&ccedil;&atilde;o com acessos espec&iacute;ficos, as integra&ccedil;&otilde;es utilizando a API Gateway garantem maior seguran&ccedil;a da informa&ccedil;&atilde;o.</li>
	<li>Simplifica&ccedil;&atilde;o das integra&ccedil;&otilde;es de parceiros com a plataforma: Por meio de um portal dedicado &agrave; documenta&ccedil;&atilde;o das APIs e aprimoramentos em servi&ccedil;os especializados, os parceiros integradores contam com um suporte mais robusto para desenvolver suas integra&ccedil;&otilde;es.</li>
	<li>Integra&ccedil;&otilde;es escal&aacute;veis: Com o crescimento substancial da API Gateway, nossos parceiros e clientes t&ecirc;m acesso a um ecossistema robusto com amplas possibilidades. De um lado, nossos clientes se beneficiam de diversas oportunidades para aprimorar seus processos e impulsionar o crescimento de seus resultados. Por outro lado, os parceiros integradores t&ecirc;m &agrave; disposi&ccedil;&atilde;o uma base de clientes que podem aproveitar plenamente suas solu&ccedil;&otilde;es, totalmente integradas com a plataforma de gest&atilde;o SankhyaOm.</li>
</ul>

<p>Agora que examinamos os pr&eacute;-requisitos e vantagens de usar a API Gateway para integra&ccedil;&otilde;es, vamos agora explorar as desvantagens de n&atilde;o adot&aacute;-la como o padr&atilde;o de integra&ccedil;&atilde;o.</p>
<p>&nbsp;</p>
`}</HTMLBlock>

## Formas de integração inadequadas

<HTMLBlock>{`
<p>Vamos abordar a integra&ccedil;&atilde;o direta com o Banco de Dados. Este tipo de integra&ccedil;&atilde;o ocorre quando sistemas de terceiros acessam diretamente o banco de dados.&nbsp;Isso implica em n&atilde;o utilizar as regras de neg&oacute;cio existentes no ERP para acessar, incluir, modificar ou excluir dados. Um exemplo pr&aacute;tico &eacute; o processo de inclus&atilde;o de um pedido de venda, no qual diversas configura&ccedil;&otilde;es da empresa impactam esse lan&ccedil;amento. Ao realizar essa inclus&atilde;o diretamente no Banco de Dados, essas regras podem ser ignoradas. Al&eacute;m disso, essa abordagem torna todas as informa&ccedil;&otilde;es do banco de dados, como folha de pagamento, faturamento e fluxo de caixa, totalmente acess&iacute;veis.</p>

<p>Dito isso, apresentamos de forma simples e objetiva as principais formas de integra&ccedil;&atilde;o n&atilde;o aceitas e fora de compliance:</p>

<ul>
	<li>Conex&atilde;o direta com banco de dados;</li>
	<li>Uso de APIs diretamente, sem a utiliza&ccedil;&atilde;o de API Gateway;</li>
	<li>Qualquer outra forma de integra&ccedil;&atilde;o que n&atilde;o utilize o API Gateway.</li>
</ul>

<p>&nbsp;</p>
`}</HTMLBlock>

## Conclusão

<HTMLBlock>{`
<p>Exploramos os requisitos e procedimentos essenciais para integrar uma solu&ccedil;&atilde;o &agrave; plataforma de gest&atilde;o Sankhya, desde a autentica&ccedil;&atilde;o at&eacute; a camada de autoriza&ccedil;&atilde;o na API Gateway, enfatizando a import&acirc;ncia de padr&otilde;es e seguran&ccedil;a. Destacamos os benef&iacute;cios da integra&ccedil;&atilde;o via API Gateway, como a seguran&ccedil;a e a simplifica&ccedil;&atilde;o do processo para parceiros e clientes, al&eacute;m da escalabilidade. Tamb&eacute;m discutimos as desvantagens da integra&ccedil;&atilde;o fora do padr&atilde;o API Gateway, como a integra&ccedil;&atilde;o direta com o banco de dados, ressaltando a falta de ades&atilde;o &agrave;s regras de neg&oacute;cio do ERP e a exposi&ccedil;&atilde;o de informa&ccedil;&otilde;es sens&iacute;veis. Em resumo, agora temos uma vis&atilde;o abrangente dos requisitos e implica&ccedil;&otilde;es das integra&ccedil;&otilde;es, enfatizando a import&acirc;ncia de adotar a API Gateway como padr&atilde;o.</p>
`}</HTMLBlock>

## Links Úteis

<HTMLBlock>{`
<p style="text-align:left"><a href="https://go.sankhya.com.br/developers/" target="_blank">Credenciamento do Desenvolvedor</a> | <a href="https://ajuda.sankhya.com.br/hc/pt-br/articles/360050259413-Sankhya-ID" target="_blank">SankhyaID</a> | <a href="https://developer.sankhya.com.br/reference/api-de-integra%C3%A7%C3%B5es-sankhya">Documenta&ccedil;&atilde;o da API</a> | <a href="https://ajuda.sankhya.com.br/hc/pt-br/articles/10007620733463-Configura%C3%A7%C3%B5es-Gateway" target="_blank">Libera&ccedil;&atilde;o de Ambientes/Gerar Token</a> |<br /> <a href="https://developer.sankhya.com.br/reference/mapeamento-de-servi%C3%A7o">Como Mapear Servi&ccedil;os</a>
<a href="https://developer.sankhya.com.br/reference/boas-pr%C3%A1ticas-para-integra%C3%A7%C3%A3o">Boas Pr&aacute;ticas de Integra&ccedil;&atilde;o</a> | <a href="https://status-gateway.sankhya.com.br/" target="_blank">Status do Gateway</a> | <a href="https://developer.sankhya.com.br/docs/tech-academy-sankhya" target="_blank">Artigos Sankhya</a> | <br /> <a href="https://community.sankhya.com.br/developers" target="_blank">Comunidade para D&uacute;vidas</a></p>
`}</HTMLBlock>

## Status do Gateway

Para verificar se o Gateway está disponível e estável acesse o status através do botão abaixo:

![](https://files.readme.io/b0764f5-status.jpg)

<HTMLBlock>{`
<div class="center">
 <a class="button_background button_size"
                    href="https://status-gateway.sankhya.com.br/"target= "_blank"
                    rel="noopener noreferrer">Status
                    </a>
</div>

<style>
    
   .center {
       display: flex;
       justify-content: center;
       align-items: center;
       height: 100px;
   }
  
   .button_size {
       background-color: #4CAF50;
  		 border: none;
  		 color: white;
 			 padding: 15px 32px;
  		 text-align: center;
       text-decoration: none !important;
       display: inline-block;
       font-size: 16px;
       margin: 4px 2px;
       cursor: pointer;
       box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);

    }

    .button_background {
        background-color: #66cc66;
        color: #fff !important;
    }

</style>
`}</HTMLBlock>

## Dúvidas frequentes

Ainda tem dúvidas de como funciona a API de Serviços? Consulte no botão abaixo a nossa FAQ  com as Perguntas Frequentes e confira se já existe uma resposta para sua pergunta.

<HTMLBlock>{`
<div class="center">
 <a class="button_background button_size"
                    href="https://developer.sankhya.com.br/reference/faq-1"target= "_blank"
                    rel="noopener noreferrer">Consulte nosso FAQ</a>
</div>

<style>
    
   .center {
       display: flex;
       justify-content: center;
       align-items: center;
       height: 100px;
   }
  
   .button_size {
       background-color: #4CAF50;
  		 border: none;
  		 color: white;
 			 padding: 15px 32px;
  		 text-align: center;
       text-decoration: none !important;
       display: inline-block;
       font-size: 16px;
       margin: 4px 2px;
       cursor: pointer;
       box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);

    }

    .button_background {
        background-color: #66cc66;
        color: #fff !important;
    }

</style>
`}</HTMLBlock>

## Como tirar dúvidas?

Para tirar dúvidas e compartilhar informações, use a [Comunidade Sankhya Developers](https://community.sankhya.com.br/developers).
