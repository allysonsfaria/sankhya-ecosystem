---
id: "https://developer.sankhya.com.br/reference/requisições-via-gateway"
titulo: "Requisições via Gateway"
url: "https://developer.sankhya.com.br/reference/requisições-via-gateway"
atualizado_em: "2025-11-10T23:39:00.000Z"
---

# Requisições via Gateway

## Realizando requisições

A documentação da API Sankhya a seguir, visa demonstrar os serviços disponíveis para cada objetivo/entidade.

Tem-se aqui a explicação da regra de negócio das entidades, demonstração de uso dos serviços e detalhamento dos campos e opções disponíveis para cada entidade.

O método PUT não é utilizado em nossa API por já ser contemplado pelo método POST que pode ser utilizado para inclusão ou atualização de dados. Caso a PK (Primary Key) enviada já exista na tabela será feito UPDATE, se não existir será feito INSERT na tabela correspondente.

Exemplo de URL de requisição em **Produção**:\
A URL de requisição possui sempre o mesmo padrão, independente do serviço a ser utilizado.

**URL padrão:**

<HTMLBlock>{`
<b>https://api.sankhya.com.br/gateway/v1/<font color="red">[modulo]/</font>service.sbr?serviceName=<font color="red">[nomedoserviço]</font>&outputType=json</font></b>
`}</HTMLBlock>

## Módulos Utilizados

Abaixo são apresentados os principais módulos para uso.

* MGE: O Módulo é utilizado para consulta e gravação de dados de cadastros em geral.

Exemplos de Serviços utilizados no MGE:

* DatasetSP.loadRecords
* CRUDServiceProvider.saveRecord
* CRUDServiceProvider.loadRecords
* DbExplorerSP.executeQuery

**URL padrão MGE**

<HTMLBlock>{`
<b>https://api.sankhya.com.br/gateway/v1/<font color="red">mge/</font>service.sbr?serviceName=<font color="red">[nomedoserviço]</font>&outputType=json</font></b>
`}</HTMLBlock>

* MGECOM: O Módulo Comercial é utilizado para consulta e gravação de movimentações como por exemplo consulta de pedido e criação de pedido de compra, venda entre outros.

Exemplos de Serviços utilizados no MGECOM:

* CACSP.IncluirNota
* CACSP.incluirAlterarItemNota
* CACSP.excluirItemNota
* CACSP.cancelarNota
* SelecaoDocumentoSP.faturar

**URL padrão MGECOM**

<HTMLBlock>{`
<b>https://api.sankhya.com.br/gateway/v1/<font color="red">mgecom/</font>service.sbr?serviceName=<font color="red">CACSP.IncluirNota</font>&outputType=json</font></b>
`}</HTMLBlock>

Ressalta-se que os serviços mencionados acima são específicos de cada módulo, ou seja, o serviço disponibilizado no módulo MGECOM é **EXCLUSIVO** deste módulo, portanto não funcionará se caso o módulo setado na URL seja o MGE, assim como os serviços do módulo MGE são **EXCLUSIVOS** e não funcionarão no módulo MGECOM.

> 🚧 Atenção
>
> Para utilização de todos os serviços, é necessário e obrigatório que seja feito o login conforme descritivo e orientação na documentação.

## Como montar as requisições no Postman

Nos passos a seguir, tem-se um exemplo de chamada para iniciar o novo método de requisição via Gateway.

> 🚧 Atenção
>
> Todos os exemplos abaixo se referem ao ambiente de homologação, o Playground da Sankhya. Para utilização em Produção, deve-se somente mudar a URL de apontamento.

**1 - Primeiro Passo:**

* A - Antes de realizar qualquer chamada ao Gateway, é necessário obter um bearerToken, que será enviado em todas as requisições após a autenticação. Consulte a documentação do endpoint [authenticate](https://developer.sankhya.com.br/reference/post_authenticate) para obter o bearerToken e utilizá-lo nas próximas transações com o Gateway.
* B - Após a chamada, recebemos o BearerToken.

<Image title="3.png" alt={953} align="center" border={true} src="https://files.readme.io/87ebc1a-3.png">
  BearerToken gerado no login.
</Image>

**2 - Segundo Passo:**

* A - Após receber o bearerToken, como exemplo acima, vamos chamar um serviço de Consulta de Preço de Produtos.\
  Devemos preencher primeiramente o Autorization com o beartoken gerado na requisição de login.

<Image title="4.png" alt={650} align="center" className="border" border={true} src="https://files.readme.io/58aa9d0-4.png" />

* B - Após preencher o Autorization, usamos como exemplo de body da requisição, passando os parâmetros de critérios, nome do serviço, etc.

Observação: Pode ser consultado esse detalhe de chamada no link abaixo: <https://developer.sankhya.com.br/reference/get_tabelapreco>

<Image title="5.png" alt={833} align="center" border={true} src="https://files.readme.io/5c766cf-image_1.png">
  Exemplo de requisição para Consulta de Preços de Produtos.
</Image>

* C - Após preenchido o body e autorization, fazemos a chamada do serviço. Recebendo essa resposta.

![](https://files.readme.io/4986f87-6.png "6.png")

<br />

## Links Úteis

<HTMLBlock>{`
<p style="text-align:left"><a href="https://ajuda.sankhya.com.br/hc/pt-br/articles/360050259413-Sankhya-ID" target="_blank">SankhyaID</a> | <a href="https://developer.sankhya.com.br/reference/api-de-integra%C3%A7%C3%B5es-sankhya">Documenta&ccedil;&atilde;o da API</a> | <a href="https://ajuda.sankhya.com.br/hc/pt-br/articles/10007620733463-Configura%C3%A7%C3%B5es-Gateway" target="_blank">Libera&ccedil;&atilde;o de Ambientes/Gerar Token</a> |<br /> <a href="https://developer.sankhya.com.br/reference/mapeamento-de-servi%C3%A7o">Como Mapear Servi&ccedil;os</a>
<a href="https://developer.sankhya.com.br/reference/boas-pr%C3%A1ticas-para-integra%C3%A7%C3%A3o">Boas Pr&aacute;ticas de Integra&ccedil;&atilde;o</a> | <a href="https://status-gateway.sankhya.com.br/" target="_blank">Status do Gateway</a> | <a href="https://developer.sankhya.com.br/docs/tech-academy-sankhya" target="_blank">Artigos Sankhya</a> | <br /> <a href="https://community.sankhya.com.br/developers" target="_blank">Comunidade para D&uacute;vidas</a></p>
`}</HTMLBlock>
