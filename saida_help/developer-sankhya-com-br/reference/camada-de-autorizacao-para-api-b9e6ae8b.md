---
id: "https://developer.sankhya.com.br/reference/camada-de-autorização-para-api"
titulo: "Camada de autorização para API"
url: "https://developer.sankhya.com.br/reference/camada-de-autorização-para-api"
atualizado_em: "2025-11-10T23:38:59.000Z"
---

# Camada de autorização para API

Com o objetivo de reforçar a segurança durante o processo de integração, foi implementada a camada de autorização para API, denominada Authorization Layer. Por meio dessa camada, o usuário responsável pelo Sankhya Om consegue definir o acesso a serviços que podem ser consultados por meio de integração via API. Em outras palavras, além da exigência de possuir um usuário de integração válido e realizar a devida autenticação, as aplicações integradas à plataforma Sankhya Om devem também obter autorização para consumir determinados serviços oferecidos pela plataforma.

Para compreender melhor o processo de ativação desse recurso, recomendamos acessar a [central de ajuda](https://ajuda.sankhya.com.br/hc/pt-br/articles/11244652964119-Camada-de-autoriza%C3%A7%C3%A3o-para-API).

A partir da tabela presente neste [link](http://swagger.sankhya.com.br/tabelas/lib_acessos_integ.html), é possível identificar quais telas precisam ser liberadas para efetuar o consumo de uma entidade específica. Como por exemplo, para realizar consultas ou cadastros na entidade "AjustesDocumentos" (TGFAJD), o usuário deve ter permissão de acesso a uma das telas vinculadas a ela, como "Cadastro Livro ICMS/IPI" ou "FUST/FUNTTEL".

<br />

## Links Úteis

<HTMLBlock>{`
<p style="text-align:left"><a href="https://ajuda.sankhya.com.br/hc/pt-br/articles/360050259413-Sankhya-ID" target="_blank">SankhyaID</a> | <a href="https://developer.sankhya.com.br/reference/api-de-integra%C3%A7%C3%B5es-sankhya">Documenta&ccedil;&atilde;o da API</a> | <a href="https://ajuda.sankhya.com.br/hc/pt-br/articles/10007620733463-Configura%C3%A7%C3%B5es-Gateway" target="_blank">Libera&ccedil;&atilde;o de Ambientes/Gerar Token</a> |<br /> <a href="https://developer.sankhya.com.br/reference/mapeamento-de-servi%C3%A7o">Como Mapear Servi&ccedil;os</a>
<a href="https://developer.sankhya.com.br/reference/boas-pr%C3%A1ticas-para-integra%C3%A7%C3%A3o">Boas Pr&aacute;ticas de Integra&ccedil;&atilde;o</a> | <a href="https://status-gateway.sankhya.com.br/" target="_blank">Status do Gateway</a> | <a href="https://developer.sankhya.com.br/docs/tech-academy-sankhya" target="_blank">Artigos Sankhya</a> | <br /> <a href="https://community.sankhya.com.br/developers" target="_blank">Comunidade para D&uacute;vidas</a></p>
`}</HTMLBlock>

##
