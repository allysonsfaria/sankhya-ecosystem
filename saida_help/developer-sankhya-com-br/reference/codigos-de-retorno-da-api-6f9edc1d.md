---
id: "https://developer.sankhya.com.br/reference/códigos-de-retorno-da-api"
titulo: "Códigos de Retorno da API"
url: "https://developer.sankhya.com.br/reference/códigos-de-retorno-da-api"
atualizado_em: "2025-11-10T23:39:03.000Z"
---

# Códigos de Retorno da API

Nesta seção, são listados os principais códigos de retorno da API Sankhya, acompanhados de suas mensagens correspondentes para referência. Além disso, são fornecidas orientações detalhadas sobre como lidar com cada situação, de acordo com o código retornado. O objetivo é facilitar a identificação e resolução de problemas durante o uso da API.

> 🚧 Atenção
>
> **Mensagens de erro, retornadas com "Status Code" 200, estão relacionadas a regras de negócio do SankhyaOm.**
>
> Para identificar o motivo do retorno, clique [aqui](https://ajuda.sankhya.com.br/), faça uma pesquisa utilizando o código do erro desejado como critério e veja detalhes em nossa página de ajuda.

<HTMLBlock>{`
<table cellpadding="0" cellspacing="0" dir="ltr">
	<tbody>
		<tr>
			<td><strong>Status Code</strong></td>
			<td><strong>Code Gateway</strong></td>
			<td><strong>Mensagem</strong></td>
			<td><strong>Tratativa</strong></td>
		</tr>
		<tr>
			<td>200</td>
			<td>-</td>
			<td>Mensagens com c&oacute;digo de erro iniciando com [CORE_E<strong>xxxxx</strong>] (onde&nbsp;<strong>xxxxx</strong> &eacute; um n&uacute;mero interiro que varia de acordo com a regra no SankhyaOm) retornadas pela requisi&ccedil;&atilde;o.</td>
			<td>Essas mensagens est&atilde;o relacionadas a regras de neg&oacute;cio do SankhyaOm. Para identificar o motivo do retorno, clique <a href="https://ajuda.sankhya.com.br/" target="_blank">aqui</a>, fa&ccedil;a uma pesquisa utilizando o c&oacute;digo do erro desejado como crit&eacute;rio e veja detalhes em nossa p&aacute;gina de ajuda.</td>
		</tr>
		<tr>
			<td>400</td>
			<td>GTW2500</td>
			<td>Erro inesperado na requisicao.</td>
			<td>Verifique a estrutura da requi&ccedil;&atilde;o e tente novamente.</td>
		</tr>
		<tr>
			<td>400</td>
			<td>GTW2509</td>
			<td>O atributo offsetPage &eacute; obrigat&oacute;rio para este tipo de consulta.</td>
			<td>Utilize o atributo offsetPage para a pagina&ccedil;&atilde;o. Clique <a href="https://developer.sankhya.com.br/reference/get_loadrecords">aqui</a> e veja os atributos necess&aacute;rios para realizar uma consulta.</td>
		</tr>
		<tr>
			<td>400</td>
			<td>GTW2508</td>
			<td>Erro na comunicacao com o servico de autenticacao.</td>
			<td>Erro de comunica&ccedil;&atilde;o interna do gateway com os servi&ccedil;os de autentica&ccedil;&atilde;o. Tente realizar a requisi&ccedil;&atilde;o novamente em alguns instantes.</td>
		</tr>
		<tr>
			<td>400</td>
			<td>GTW3003</td>
			<td>Erro na comunica&ccedil;&atilde;o com o Console.</td>
			<td>Erro de comunica&ccedil;&atilde;o interna do gateway. Tente realizar a requisi&ccedil;&atilde;o novamente em alguns instantes.</td>
		</tr>
		<tr>
			<td>400</td>
			<td>GTW3407</td>
			<td>N&atilde;o foi possivel realizar login no erp.</td>
			<td>Verifique se o ambiente do SankhyaOM est&aacute; dispon&iacute;vel.&nbsp;Clique <a href="https://developer.sankhya.com.br/reference/configurando-acessos-iniciais-integra%C3%A7%C3%A3o#inclus%C3%A3o-de-ip%C2%B4s-no-firewall-devido-chamada-do-gateway">aqui</a> e veja os requisitos necess&aacute;rios para acessar o ambiente do SankhyaOm via gateway.</td>
		</tr>
		<tr>
			<td>400</td>
			<td>GTW3500</td>
			<td>Erro na comunica&ccedil;&atilde;o com o SankhyaID.</td>
			<td>N&atilde;o foi poss&iacute;vel realizar login com as credencias (SankhyaID) enviadas. Clique <a href="https://login.sankhya.com.br/" target="_blank">aqui</a> e valide as credencias de acesso.</td>
		</tr>
		<tr>
			<td>401</td>
			<td>GTW2510</td>
			<td>O Header Authorization &eacute; obrigat&oacute;rio para esta requisi&ccedil;&atilde;o.</td>
			<td>Adicione ao Header o BearerToken. Clique <a href="https://developer.sankhya.com.br/reference/requisi%C3%A7%C3%B5es-via-gateway#realizando-requisi%C3%A7%C3%B5es">aqui</a> e veja os requisitos necess&aacute;rios para realizar uma requisi&ccedil;&atilde;o.</td>
		</tr>
		<tr>
			<td>401</td>
			<td>GTW2511</td>
			<td>Header Authorization fora do padr&atilde;o. N&atilde;o come&ccedil;a com &#39;Bearer &#39; ou n&atilde;o cont&eacute;m o JWT.</td>
			<td>Adicione ao Header o BearerToken. Clique <a href="https://developer.sankhya.com.br/reference/requisi%C3%A7%C3%B5es-via-gateway#realizando-requisi%C3%A7%C3%B5es">aqui</a> e veja os requisitos necess&aacute;rios para realizar uma requisi&ccedil;&atilde;o.</td>
		</tr>
		<tr>
			<td>401</td>
			<td>GTW3501</td>
			<td>Usuario Invalido.</td>
			<td>Verifique as credenciais (SankhyaID) para login.&nbsp;Clique <a href="https://developer.sankhya.com.br/reference/post_login">aqui</a> e veja os requisitos necess&aacute;rios para realizar uma requisi&ccedil;&atilde;o de login.</td>
		</tr>
		<tr>
			<td>401</td>
			<td>GTW3502</td>
			<td>Password Invalido.</td>
			<td>Verifique as credenciais (SankhyaID) para login.&nbsp;Clique <a href="https://developer.sankhya.com.br/reference/post_login">aqui</a> e veja os requisitos necess&aacute;rios para realizar uma requisi&ccedil;&atilde;o de login.</td>
		</tr>
		<tr>
			<td>401</td>
			<td>GTW3503</td>
			<td>Excedido o tempo m&aacute;ximo da Requisi&ccedil;&atilde;o do Gateway Sankhya.</td>
			<td>Verifique se o ambiente do SankhyaOM est&aacute; dispon&iacute;vel.&nbsp;Clique <a href="https://developer.sankhya.com.br/reference/configurando-acessos-iniciais-integra%C3%A7%C3%A3o#inclus%C3%A3o-de-ip%C2%B4s-no-firewall-devido-chamada-do-gateway">aqui</a> e veja os requisitos necess&aacute;rios para acessar o ambiente do SankhyaOm via gateway.</td>
		</tr>
		<tr>
			<td>403</td>
			<td>GTW3403</td>
			<td>Bearer Token inv&aacute;lido ou Expirado.</td>
			<td>Fa&ccedil;a login, atualize o&nbsp;BearerToken e tente novamente.&nbsp;Clique <a href="https://developer.sankhya.com.br/reference/post_login">aqui</a> e veja os requisitos necess&aacute;rios para realizar uma requisi&ccedil;&atilde;o de login.</td>
		</tr>
		<tr>
			<td>403</td>
			<td>4405</td>
			<td>Token e Appkey nao associados.</td>
			<td>Verifique as credenciais (Appkey, Token e URL utilizados - combine corretamente as credenciais para acesso de acordo com o ambiente PRODUÇÃO ou SANDBOX) para login.&nbsp;Clique <a href="https://developer.sankhya.com.br/reference/post_login">aqui</a> e veja os requisitos necess&aacute;rios para realizar uma requisi&ccedil;&atilde;o de login.</td>
		</tr>
		<tr>
			<td>403</td>
			<td>4303</td>
			<td>Token invalido ou inativado.</td>
			<td>Verifique as credenciais (Appkey, Token e URL utilizados - combine corretamente as credenciais para acesso de acordo com o ambiente PRODUÇÃO ou SANDBOX) para login.&nbsp;Clique <a href="https://developer.sankhya.com.br/reference/post_login">aqui</a> e veja os requisitos necess&aacute;rios para realizar uma requisi&ccedil;&atilde;o de login.</td>
		</tr>
		<tr>
			<td>500</td>
			<td>-</td>
			<td>Erro interno do servidor</td>
			<td>Retorno padr&atilde;o do servidor.</td>
		</tr>
		<tr>
			<td>501</td>
			<td>-</td>
			<td>Not Implemented</td>
			<td>Retorno padr&atilde;o do servidor.</td>
		</tr>
		<tr>
			<td>502</td>
			<td>-</td>
			<td>Bad Gateway</td>
			<td>Retorno padr&atilde;o do servidor.</td>
		</tr>
		<tr>
			<td>503</td>
			<td>-</td>
			<td>Servi&ccedil;o Indispon&iacute;vel</td>
			<td>Retorno padr&atilde;o do servidor.</td>
		</tr>
		<tr>
			<td>504</td>
			<td>-</td>
			<td>Gateway Timeout</td>
			<td>Quando a requisi&ccedil;&atilde;o ultrapassa 2 minutos de processamento. Geralmente ocorre quando o SankhyaOm demora para processar a requisi&ccedil;&atilde;o.</td>
		</tr>
	</tbody>
</table>
`}</HTMLBlock>

<br />

## Links Úteis

<HTMLBlock>{`
<p style="text-align:left"><a href="https://ajuda.sankhya.com.br/hc/pt-br/articles/360050259413-Sankhya-ID" target="_blank">SankhyaID</a> | <a href="https://developer.sankhya.com.br/reference/api-de-integra%C3%A7%C3%B5es-sankhya">Documenta&ccedil;&atilde;o da API</a> | <a href="https://ajuda.sankhya.com.br/hc/pt-br/articles/10007620733463-Configura%C3%A7%C3%B5es-Gateway" target="_blank">Libera&ccedil;&atilde;o de Ambientes/Gerar Token</a> |<br /> <a href="https://developer.sankhya.com.br/reference/mapeamento-de-servi%C3%A7o">Como Mapear Servi&ccedil;os</a>
<a href="https://developer.sankhya.com.br/reference/boas-pr%C3%A1ticas-para-integra%C3%A7%C3%A3o">Boas Pr&aacute;ticas de Integra&ccedil;&atilde;o</a> | <a href="https://status-gateway.sankhya.com.br/" target="_blank">Status do Gateway</a> | <a href="https://developer.sankhya.com.br/docs/tech-academy-sankhya" target="_blank">Artigos Sankhya</a> | <br /> <a href="https://community.sankhya.com.br/developers" target="_blank">Comunidade para D&uacute;vidas</a></p>
`}</HTMLBlock>
