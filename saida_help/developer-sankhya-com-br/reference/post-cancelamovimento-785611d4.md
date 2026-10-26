---
id: "https://developer.sankhya.com.br/reference/post_cancelamovimento"
titulo: "Cancelamento de Movimentos"
url: "https://developer.sankhya.com.br/reference/post_cancelamovimento"
atualizado_em: "2026-05-13T15:12:48.000Z"
---

# Cancelamento de Movimentos

<h1>Regras de negócio</h1>
Para realizar o cancelamento de pedidos no ERP será necessário efetuar criação de um filtro para acessar os títulos que precisam ser cancelados e efetuar o preenchimento dos dados necessários para efetuar o cancelamento.No ERP a partir do momento que é cancelada uma nota fiscal, não é mais possível reverter este processo, sendo necessário lançar a nota fiscal novamente.<br />
<b>OBS:</b> Caso tenha alguma necessidade de configuração do ERP procure “Consultor” ou acesso o link de apoio:<br />\nhttps://ajuda.sankhya.com.br/hc/pt-br/articles/360045107913-Notas-Canceladas<br />
<h3>Dependências</h3> Para realizar o cancelameno do pedido, os seguintes itens são obrigatórios:<br />
<b>1) </b>Logar no sistema utilizando o Serviço de Login descrito nesta documentação em Login; <br />  <b>2) </b>O pedido deve estar confirmado no ERP Sankhya-Om;<br />  <b>3) </b>É obrigatório informar o número único da nota<br /> <b>4) </b>É obrigatorio informar a justificativa de cancelamento</b>.<br />
<h3>Detalhes Técnicos</h3>
O serviço utilizado para cancelamento de notas é o CACSP.cancelarNota que utiliza a entidade  CabecalhoNota que por sua vez instancia a tabela TGFCAB.<br />
Para usar serviços de módulos auxiliares, como é o caso do mgecom devemos enviar um parâmetro adicional na URL, cujo nome é mgeSession e o valor será o ID adquirido no serviço de autenticação. Isso não se aplica para serviços do módulo mge, que é o principal.<br />
Para realizar a exclusão do pedido através do Json, o campo abaixo é obrigatório:<br /><br />

  - NUNOTA – Numero Único da nota;
  
A partir do momento em que a nota é cancelada, a nota é inserida na tabela <b>TGFCAN</b> que por sua vez é instanciada pela entidade <b>\"NotaCancelada\"</b>, esta tabela é responsável por armazenar todas as notas que foram confirmadas mas por algum motivo ou divergência, foi cancelada.

<h3>Descritivo de Campos das Entidades</h3>
Acesse [aqui](http://swagger.sankhya.com.br/tabelas/TGFCAB.html) o dicionário de dados da tabela <b>TGFCAB</b><br />  Acesse [aqui](http://swagger.sankhya.com.br/tabelas/TGFCAN.html) o dicionário de dados da tabela <b>TGFCAN</b><br />
<h3>Exemplo de uso:</h3>  <ul>
  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>
  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>
</ul> <b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mgecom/service.sbr?serviceName=CACSP.cancelarNota&outputType=json <br />
<b>Corpo de requisição</b>

    {
       "serviceName":"CACSP.cancelarNota",
       "requestBody":{
          "notasCanceladas":{
             "nunota":[
                {
                   "$":"3713703"
                }
             ],
             "justificativa":"lançamento indevido",
             "validarProcessosWmsEmAndamento":"true"
          }
        }
    }


<b>Retorno:</b><br />

    {
        "serviceName": "CACSP.cancelarNota",
        "status": "1",
        "pendingPrinting": "false",
        "transactionId": "BA6F5CEB2F1ED4B27E3E66F98C4BE084",
        "responseBody": {
            "resultadoCancelamento": {
                "totalNotasCanceladas": "1"
            }
        }
    }


# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "API Sankhya - Legada",
    "description": "API de Integrações Sankhya\n\nEsta documentação apresenta os serviços disponíveis para cada objetivo e entidade. Você encontrará explicações sobre as regras de negócio, demonstrações de uso dos serviços e detalhes dos campos e opções.\n\nA API é baseada em chamadas HTTP ou HTTPS, utilizando os métodos POST e GET, com corpo no formato JSON. Qualquer sistema capaz de realizar uma chamada HTTP pode utilizar os serviços.\n\nO método PUT não é utilizado, pois as operações de inclusão ou atualização são feitas pelo método POST. Se a chave primária (PK) já existir, será feito um UPDATE; se não, um INSERT.\n\nO que é uma Entidade?\n\"Entidade\" refere-se a tudo que pode ser cadastrado, editado, consultado ou excluído no Sankhya. Por exemplo, um \"Produto\" pode ser cadastrado, editado, consultado ou excluído.\n\n**Exemplo de URL de Requisição:**\nA URL de requisição segue um padrão fixo:\n\n**URL padrão:**\nhttps://api.sankhya.com.br/gateway/v1/[modulo]/service.sbr?serviceName=[nomedoserviço]&outputType=json\n\n**Módulos Utilizados:**\n\n**MGE:**\nEste módulo é para consulta e gravação de dados de cadastros.\n\nExemplos de Serviços no MGE:\n- CRUDServiceProvider.loadRecords\n- CRUDServiceProvider.saveRecord\n- DbExplorerSP.executeQuery\n\nURL padrão MGE:\nhttps://api.sankhya.com.br/gateway/v1/mge/service.sbr?serviceName=[nomedoserviço]&outputType=json\n\n**MGECOM:**\nO módulo Comercial é para consulta e gravação de movimentações, como pedidos e compras.\n\nExemplos de Serviços no MGECOM:\n- CACSP.IncluirNota\n- CACSP.incluirAlterarItemNota\n- CACSP.excluirItemNota\n- CACSP.cancelarNota\n- SelecaoDocumentoSP.faturar\n\nURL padrão MGECOM:\nhttps://api.sankhya.com.br/gateway/v1/mgecom/service.sbr?serviceName=CACSP.IncluirNota&outputType=json\n\nImportante:\nOs serviços são específicos para cada módulo. Os serviços do módulo MGECOM são exclusivos e não funcionarão se a URL for para o módulo MGE, e vice-versa.\n\nPara utilizar todos os serviços, é necessário realizar o login conforme descrito na documentação.\n",
    "termsOfService": "https://www.sankhya.com.br/",
    "license": {
      "name": "Licença Sankhya",
      "url": "https://www.sankhya.com.br/"
    },
    "version": "1.0"
  },
  "servers": [
    {
      "url": "https://api.sankhya.com.br",
      "description": "Produção"
    },
    {
      "url": "https://api.sandbox.sankhya.com.br",
      "description": "Sandbox"
    }
  ],
  "externalDocs": {
    "description": "Saiba mais sobre a API Sankhya",
    "url": "https://developer.sankhya.com.br/reference/api-de-integra%C3%A7%C3%B5es-sankhya"
  },
  "tags": [
    {
      "name": "Serviços Especialistas",
      "description": "Serviços especialistas disponiveis no SankhyaOm"
    }
  ],
  "paths": {
    "/CancelaMovimento": {
      "post": {
        "tags": [
          "Serviços Especialistas"
        ],
        "summary": "Cancelamento de Movimentos",
        "description": "<h1>Regras de negócio</h1>\nPara realizar o cancelamento de pedidos no ERP será necessário efetuar criação de um filtro para acessar os títulos que precisam ser cancelados e efetuar o preenchimento dos dados necessários para efetuar o cancelamento.No ERP a partir do momento que é cancelada uma nota fiscal, não é mais possível reverter este processo, sendo necessário lançar a nota fiscal novamente.<br />\n<b>OBS:</b> Caso tenha alguma necessidade de configuração do ERP procure “Consultor” ou acesso o link de apoio:<br />\\nhttps://ajuda.sankhya.com.br/hc/pt-br/articles/360045107913-Notas-Canceladas<br />\n<h3>Dependências</h3> Para realizar o cancelameno do pedido, os seguintes itens são obrigatórios:<br />\n<b>1) </b>Logar no sistema utilizando o Serviço de Login descrito nesta documentação em Login; <br />  <b>2) </b>O pedido deve estar confirmado no ERP Sankhya-Om;<br />  <b>3) </b>É obrigatório informar o número único da nota<br /> <b>4) </b>É obrigatorio informar a justificativa de cancelamento</b>.<br />\n<h3>Detalhes Técnicos</h3>\nO serviço utilizado para cancelamento de notas é o CACSP.cancelarNota que utiliza a entidade  CabecalhoNota que por sua vez instancia a tabela TGFCAB.<br />\nPara usar serviços de módulos auxiliares, como é o caso do mgecom devemos enviar um parâmetro adicional na URL, cujo nome é mgeSession e o valor será o ID adquirido no serviço de autenticação. Isso não se aplica para serviços do módulo mge, que é o principal.<br />\nPara realizar a exclusão do pedido através do Json, o campo abaixo é obrigatório:<br /><br />\n\n  - NUNOTA – Numero Único da nota;\n  \nA partir do momento em que a nota é cancelada, a nota é inserida na tabela <b>TGFCAN</b> que por sua vez é instanciada pela entidade <b>\\\"NotaCancelada\\\"</b>, esta tabela é responsável por armazenar todas as notas que foram confirmadas mas por algum motivo ou divergência, foi cancelada.\n\n<h3>Descritivo de Campos das Entidades</h3>\nAcesse [aqui](http://swagger.sankhya.com.br/tabelas/TGFCAB.html) o dicionário de dados da tabela <b>TGFCAB</b><br />  Acesse [aqui](http://swagger.sankhya.com.br/tabelas/TGFCAN.html) o dicionário de dados da tabela <b>TGFCAN</b><br />\n<h3>Exemplo de uso:</h3>  <ul>\n  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>\n  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>\n</ul> <b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mgecom/service.sbr?serviceName=CACSP.cancelarNota&outputType=json <br />\n<b>Corpo de requisição</b>\n\n    {\n       \"serviceName\":\"CACSP.cancelarNota\",\n       \"requestBody\":{\n          \"notasCanceladas\":{\n             \"nunota\":[\n                {\n                   \"$\":\"3713703\"\n                }\n             ],\n             \"justificativa\":\"lançamento indevido\",\n             \"validarProcessosWmsEmAndamento\":\"true\"\n          }\n        }\n    }\n\n\n<b>Retorno:</b><br />\n\n    {\n        \"serviceName\": \"CACSP.cancelarNota\",\n        \"status\": \"1\",\n        \"pendingPrinting\": \"false\",\n        \"transactionId\": \"BA6F5CEB2F1ED4B27E3E66F98C4BE084\",\n        \"responseBody\": {\n            \"resultadoCancelamento\": {\n                \"totalNotasCanceladas\": \"1\"\n            }\n        }\n    }\n",
        "responses": {
          "201": {
            "description": "Cancelamento de pedidos realizada com sucesso!"
          },
          "400": {
            "description": "Requisição inválida"
          },
          "500": {
            "description": "Erro interno do servidor"
          }
        }
      }
    }
  }
}
```
