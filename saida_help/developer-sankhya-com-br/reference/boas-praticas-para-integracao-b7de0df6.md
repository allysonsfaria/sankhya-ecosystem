---
id: "https://developer.sankhya.com.br/reference/boas-práticas-para-integração"
titulo: "Boas Práticas para Integração"
url: "https://developer.sankhya.com.br/reference/boas-práticas-para-integração"
atualizado_em: "2025-11-10T23:39:02.000Z"
---

# Boas Práticas para Integração

<HTMLBlock>{`
<p>Para desenvolver uma integra&ccedil;&atilde;o eficaz com nossa API, &eacute; crucial considerar algumas premissas importantes. Considerando o uso da API Gateway, uma camada que direciona todas as requisi&ccedil;&otilde;es, estas s&atilde;o prontamente encaminhadas para a infraestrutura do cliente, que assume a responsabilidade pelo processamento completo.</p>

<p>Considerando as limita&ccedil;&otilde;es fundamentais da API Gateway:</p>

<ul>
	<li>Volume de requisi&ccedil;&otilde;es: at&eacute; 1.000 por minuto (em ambiente de produ&ccedil;&atilde;o e em ambiente de sandobox).</li>
	<li>Tamanho m&aacute;ximo da requisi&ccedil;&atilde;o: 10MB.</li>
	<li>Tempo de processamento na infraestrutura do cliente: at&eacute; 2 minutos.</li>
</ul>

<p>A&nbsp;seguir, destacamos pontos cruciais aos quais o desenvolvedor da integração deve ficar sempre atento:</p>

<ul>
	<li>Para garantir a conformidade, &eacute; essencial realizar todas as integra&ccedil;&otilde;es usando a API Gateway como o padr&atilde;o de troca de informa&ccedil;&otilde;es. Integra&ccedil;&otilde;es via Banco de Dados ou o uso direto da antiga API conectada ao SankhyaOm do cliente est&atilde;o em desacordo com as diretrizes (v&aacute;lido apenas para clientes Sankhya a partir de 01/02/2023).</li>
	<li>Ao utilizar o&nbsp;servi&ccedil;o para recuperar dados (<a href="https://developer.sankhya.com.br/reference/get_loadrecords">loadRecords</a>), esteja atento &agrave; possibilidade de lentid&atilde;o. Se encontrar essa situa&ccedil;&atilde;o, revise os campos marcados como &quot;calculados&quot; na entidade, por meio da tela <a href="https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados" target="_blank">Dicion&aacute;rio de Dados</a>. Express&otilde;es personalizadas mal otimizadas podem causar lentid&atilde;o e, consequentemente, timeouts na API.</li>
	<li>Incluir ou atualizar registros (<a href="https://developer.sankhya.com.br/reference/post_salve">salve</a>) tamb&eacute;m pode causar lentid&atilde;o na aplica&ccedil;&atilde;o do cliente ao enviar m&uacute;ltiplos registros por requisi&ccedil;&atilde;o. Isso geralmente ocorre devido a objetos de banco de dados, personalizados, na&nbsp;tabela&nbsp;que representa a entidade utilizada na requisi&ccedil;&atilde;o via API. Recomenda-se reduzir o volume de registros enviados e tamb&eacute;m revisar esses objetos de banco de dados personalizados para otimizar o desempenho.</li>
	<li>Como mencionado anteriormente, todo o processamento da requisi&ccedil;&atilde;o ocorre na infraestrutura do cliente. Isso implica que se a infraestrutura do cliente (seja na infraestrutura interna ou em um datacenter externo) n&atilde;o estiver alinhada com as cargas de requisi&ccedil;&otilde;es, a performance pode ser comprometida, levando a timeout&nbsp;na API.</li>
	<li>O servi&ccedil;o <a href="https://developer.sankhya.com.br/reference/post_pedidos">incluirNota</a> &eacute; amplamente utilizado na API, mas em certas circunst&acirc;ncias, pode resultar em timeout. Considere todos os pontos mencionados anteriormente ao analisar isso, e avalie tamb&eacute;m a quantidade de itens na requisi&ccedil;&atilde;o. Um grande volume de itens pode levar a timeout. Se isso acontecer, &eacute; recomend&aacute;vel negociar um n&uacute;mero menor de itens (por exemplo, 20 itens, mas avalie caso a caso, pois pode variar) e utilizar o servi&ccedil;o de inclus&atilde;o/altera&ccedil;&atilde;o de itens da nota (<a href="https://developer.sankhya.com.br/reference/post_incaltitempedido">incluirAlterarItemNota</a>) para adicionar os itens restantes.</li>
	<li>A obten&ccedil;&atilde;o de dados usando servi&ccedil;os sem pagina&ccedil;&atilde;o, como o <a href="https://developer.sankhya.com.br/reference/get_loadview">loadView</a>, pode resultar em timeouts. &Eacute; crucial estabelecer crit&eacute;rios seguros para evitar grandes volumes de dados, garantindo assim uma integra&ccedil;&atilde;o com desempenho adequado. Para dicas e exemplos sobre como aprimorar a performance ao utilizar o <a href="https://developer.sankhya.com.br/reference/get_loadview">loadView</a>, consulte nosso guia clicando <a href="https://developer.sankhya.com.br/reference/get_loadview">aqui</a>.</li>
</ul>

<p>Respeitar os limites de taxa de solicita&ccedil;&atilde;o &eacute; essencial para evitar sobrecarga nos servidores da API e do cliente, prevenindo quedas de desempenho e interrup&ccedil;&otilde;es no servi&ccedil;o. Ignorar esses limites pode resultar em bloqueio de acesso tempor&aacute;rio, afetando negativamente a funcionalidade da integra&ccedil;&atilde;o constru&iacute;da pelo desenvolvedor. Ao aderir &agrave;s regras, o desenvolvedor da integração garante&nbsp;uma experi&ecirc;ncia mais est&aacute;vel de uso das API&#39;s, promovendo a confiabilidade da aplica&ccedil;&atilde;o e a manuten&ccedil;&atilde;o de uma boa reputa&ccedil;&atilde;o como desenvolvedor de integrações.</p>
`}</HTMLBlock>

<br />

## Links Úteis

<HTMLBlock>{`
<p style="text-align:left"><a href="https://ajuda.sankhya.com.br/hc/pt-br/articles/360050259413-Sankhya-ID" target="_blank">SankhyaID</a> | <a href="https://developer.sankhya.com.br/reference/api-de-integra%C3%A7%C3%B5es-sankhya">Documenta&ccedil;&atilde;o da API</a> | <a href="https://ajuda.sankhya.com.br/hc/pt-br/articles/10007620733463-Configura%C3%A7%C3%B5es-Gateway" target="_blank">Libera&ccedil;&atilde;o de Ambientes/Gerar Token</a> |<br /> <a href="https://developer.sankhya.com.br/reference/mapeamento-de-servi%C3%A7o">Como Mapear Servi&ccedil;os</a>
<a href="https://developer.sankhya.com.br/reference/boas-pr%C3%A1ticas-para-integra%C3%A7%C3%A3o">Boas Pr&aacute;ticas de Integra&ccedil;&atilde;o</a> | <a href="https://status-gateway.sankhya.com.br/" target="_blank">Status do Gateway</a> | <a href="https://developer.sankhya.com.br/docs/tech-academy-sankhya" target="_blank">Artigos Sankhya</a> | <br /> <a href="https://community.sankhya.com.br/developers" target="_blank">Comunidade para D&uacute;vidas</a></p>
`}</HTMLBlock>
