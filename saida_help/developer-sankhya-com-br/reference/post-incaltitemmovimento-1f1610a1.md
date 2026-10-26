---
id: "https://developer.sankhya.com.br/reference/post_incaltitemmovimento"
titulo: "Incluir e Alterar Itens de Movimentos"
url: "https://developer.sankhya.com.br/reference/post_incaltitemmovimento"
atualizado_em: "2026-05-13T15:12:48.000Z"
---

# Incluir e Alterar Itens de Movimentos

"<h1>Regras de negócio</h1> O objetivo é incluir no ERP um <b>pedido de venda</b> ou <b>pedido de compra</b> negociado, por exemplo em 01/01 para ser entregue em até 31/12, durante esse prazo de negociação, ocorrem algumas variações do preço na quantidade dos itens, assim como itens excluídos e incluídos na negociação, por isso existe a necessidade de manter um <b>pedido de venda</b> faturado parcialmente e que poderá sofrer manutenções/alterações.<br />\nPara realizar configuração no sistema com o <b><u>tipo de operação - Top</u></b> e habilitar algumas marcações \"Permitir Alteração após confirmar\" e \"Permite alterar itens após faturar parcialmente\" e \"Gravar histórico de alterações do pedido\" que possibilita a alteração do <b>pedido de compra</b> ou <b>pedido de venda</b>, faturado parcialmente no sistema.<br />\n<b>OBS:</b> Caso tenha alguma necessidade de configuração do ERP procure “Consultor” ou acesso o link de apoio:<br /> https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109773-Altera%C3%A7%C3%A3o-de-Pedidos-Parcialmente-Faturados#prefer%C3%AAncias<br />\n<h3>Dependências</h3> Para realizar a inclusão ou alteração de itens no pedido, os seguintes itens são obrigatórios:<br />\n<b>1) </b>Logar no sistema utilizando o Serviço de Login descrito nesta documentação em Login; <br /> <b>2) </b>Produtos/Serviços  preeviamente cadastrados e ativos;<br /> <b>3) </b>Empresas previamente cadastradas e ativas;<br /> <b>4) </b>Top's configuradas devidamente tipo de movimentação <b>\"Pedido de venda\"</b>;<br /> <b>5) </b>Tipo de operação(TOP) utilizado no pedido deve estar configurada para permitir a alteração do <b>\"pedido\"</b> após a <b>\"confirmação\"</b> do mesmo. <br />\n<h3>Detalhes Técnicos</h3> O serviço utilizado para inclusão e alteração de itens no pedido  é o <b>CACSP.incluirAlterarItemNota</b> que instancia as entidades principais para o envio de item no pedido, as entidades que este serviço utiliza são: <br />\n  <b>• CabecalhoNota;</b>\n  <b>• ItemNota.</b><br />\n  Os campos obrigatórios dependem estritamente da configuração de TOP,empresa, produto, etc. Portanto, neste exemplo colocamos os campos tipicamente obrigatórios em todos os casos de uso. Este exemplo não tenta exaurir as possibilidades,que são muitas, então em alguns casos a chamada a esse serviço pode resultar em mensagem de erro exigindo que outros campos sejam enviados. <br />\n  Apenas um item pedido/nota pode ser enviado por vez. <br />\n  Para realizar a inclusão do item no pedido através do Json, os campos abaixo são obrigatórios:<br /><br />
<b>CABEÇALHO DO PEDIDO</b><br />

  - CODPROD – Código do Produto;
  - QTDNEG – Quantidade;
  - CODLOCALORIG – Código local de Origem;
  - CODVOL – Código do Volume;
  - SEQUENCIA - Sequência do item no pedido;
  - VLRUNIT - Valor Unitário;
  - VLRTOT - Valor total do item(QTDNEG x VLRUNIT);
  - VLRDESC - Valor do Desconto;
  - PERCDESC - Percentual de Desconto.


<h3></h3> Para realizar a alteração de itens do pedido basta informar o número da SEQUÊNCIA do item a ser alterado pelo JSON, segue exemplo:

    "SEQUENCIA":{
      "$":"10"
    }

<h3>Descritivo de Campos das Entidades</h3>
Acesse [aqui](http://swagger.sankhya.com.br/tabelas/TGFCAB.html) o dicionário de dados da tabela <b>TGFCAB</b><br />  Acesse [aqui](http://swagger.sankhya.com.br/tabelas/TGFITE.html) o dicionário de dados da tabela <b>TGFITE</b><br />

<h3>Exemplo de uso:</h3> <ul>
  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>
  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>
</ul> <b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mgecom/service.sbr?serviceName=CACSP.incluirAlterarItemNota&outputType=json<br />
<b>Corpo de Requisição Padrão para Inclusão:</b>

    {
       "serviceName":"CACSP.incluirAlterarItemNota",
       "requestBody":{
          "nota":{
             "NUNOTA":"7468",
             "itens":{
                "item":{
                   "CODPROD":{
                      "$":"129"
                   },
                   "NUNOTA":{
                      "$":"7468"
                   },
                   "SEQUENCIA":{
                      "$":""
                   },
                   "QTDNEG":{
                      "$":"10"
                   },
                   "VLRUNIT":{
                      "$":"10"
                   },
                   "VLRTOT":{
                      "$":"432.38"
                   },
                   "CODVOL":{
                      "$":"UN"
                   },
                   "VLRDESC":{
                      "$":"0"
                   },
                   "PERCDESC":{
                      "$":"0"
                   }
                }
             }
          }
       }
    }


<b>Corpo de Requisição Padrão para Alteração:</b>

    {
       "serviceName":"CACSP.incluirAlterarItemNota",
       "requestBody":{
          "nota":{
             "NUNOTA":"7468",
             "itens":{
                "item":{
                   "CODPROD":{
                      "$":"129"
                   },
                   "NUNOTA":{
                      "$":"7468"
                   },
                   "SEQUENCIA":{
                      "$":"10"
                   },
                   "QTDNEG":{
                      "$":"8"
                   },
                   "VLRUNIT":{
                      "$":"10"
                   },
                   "VLRTOT":{
                      "$":"432.38"
                   },
                   "CODVOL":{
                      "$":"UN"
                   },
                   "VLRDESC":{
                      "$":"0"
                   },
                   "PERCDESC":{
                      "$":"0"
                   }
                }
             }
          }
       }
    }



<b>Retorno:</b><br />

    {
        "serviceName": "CACSP.incluirAlterarItemNota",
        "status": "1",
        "pendingPrinting": "false",
        "transactionId": "46457EBA87743376561485A6021C8D8A",
        "responseBody": {
            "pk": {
                "NUNOTA": {
                    "$": "7468"
                },
                "SEQUENCIA": {
                    "$": "8"
                }
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
    "/IncAltItemMovimento": {
      "post": {
        "tags": [
          "Serviços Especialistas"
        ],
        "summary": "Incluir e Alterar Itens de Movimentos",
        "description": "\"<h1>Regras de negócio</h1> O objetivo é incluir no ERP um <b>pedido de venda</b> ou <b>pedido de compra</b> negociado, por exemplo em 01/01 para ser entregue em até 31/12, durante esse prazo de negociação, ocorrem algumas variações do preço na quantidade dos itens, assim como itens excluídos e incluídos na negociação, por isso existe a necessidade de manter um <b>pedido de venda</b> faturado parcialmente e que poderá sofrer manutenções/alterações.<br />\\nPara realizar configuração no sistema com o <b><u>tipo de operação - Top</u></b> e habilitar algumas marcações \\\"Permitir Alteração após confirmar\\\" e \\\"Permite alterar itens após faturar parcialmente\\\" e \\\"Gravar histórico de alterações do pedido\\\" que possibilita a alteração do <b>pedido de compra</b> ou <b>pedido de venda</b>, faturado parcialmente no sistema.<br />\\n<b>OBS:</b> Caso tenha alguma necessidade de configuração do ERP procure “Consultor” ou acesso o link de apoio:<br /> https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109773-Altera%C3%A7%C3%A3o-de-Pedidos-Parcialmente-Faturados#prefer%C3%AAncias<br />\\n<h3>Dependências</h3> Para realizar a inclusão ou alteração de itens no pedido, os seguintes itens são obrigatórios:<br />\\n<b>1) </b>Logar no sistema utilizando o Serviço de Login descrito nesta documentação em Login; <br /> <b>2) </b>Produtos/Serviços  preeviamente cadastrados e ativos;<br /> <b>3) </b>Empresas previamente cadastradas e ativas;<br /> <b>4) </b>Top's configuradas devidamente tipo de movimentação <b>\\\"Pedido de venda\\\"</b>;<br /> <b>5) </b>Tipo de operação(TOP) utilizado no pedido deve estar configurada para permitir a alteração do <b>\\\"pedido\\\"</b> após a <b>\\\"confirmação\\\"</b> do mesmo. <br />\\n<h3>Detalhes Técnicos</h3> O serviço utilizado para inclusão e alteração de itens no pedido  é o <b>CACSP.incluirAlterarItemNota</b> que instancia as entidades principais para o envio de item no pedido, as entidades que este serviço utiliza são: <br />\\n  <b>• CabecalhoNota;</b>\\n  <b>• ItemNota.</b><br />\\n  Os campos obrigatórios dependem estritamente da configuração de TOP,empresa, produto, etc. Portanto, neste exemplo colocamos os campos tipicamente obrigatórios em todos os casos de uso. Este exemplo não tenta exaurir as possibilidades,que são muitas, então em alguns casos a chamada a esse serviço pode resultar em mensagem de erro exigindo que outros campos sejam enviados. <br />\\n  Apenas um item pedido/nota pode ser enviado por vez. <br />\\n  Para realizar a inclusão do item no pedido através do Json, os campos abaixo são obrigatórios:<br /><br />\n<b>CABEÇALHO DO PEDIDO</b><br />\n\n  - CODPROD – Código do Produto;\n  - QTDNEG – Quantidade;\n  - CODLOCALORIG – Código local de Origem;\n  - CODVOL – Código do Volume;\n  - SEQUENCIA - Sequência do item no pedido;\n  - VLRUNIT - Valor Unitário;\n  - VLRTOT - Valor total do item(QTDNEG x VLRUNIT);\n  - VLRDESC - Valor do Desconto;\n  - PERCDESC - Percentual de Desconto.\n\n\n<h3></h3> Para realizar a alteração de itens do pedido basta informar o número da SEQUÊNCIA do item a ser alterado pelo JSON, segue exemplo:\n\n    \"SEQUENCIA\":{\n      \"$\":\"10\"\n    }\n\n<h3>Descritivo de Campos das Entidades</h3>\nAcesse [aqui](http://swagger.sankhya.com.br/tabelas/TGFCAB.html) o dicionário de dados da tabela <b>TGFCAB</b><br />  Acesse [aqui](http://swagger.sankhya.com.br/tabelas/TGFITE.html) o dicionário de dados da tabela <b>TGFITE</b><br />\n\n<h3>Exemplo de uso:</h3> <ul>\n  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>\n  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>\n</ul> <b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mgecom/service.sbr?serviceName=CACSP.incluirAlterarItemNota&outputType=json<br />\n<b>Corpo de Requisição Padrão para Inclusão:</b>\n\n    {\n       \"serviceName\":\"CACSP.incluirAlterarItemNota\",\n       \"requestBody\":{\n          \"nota\":{\n             \"NUNOTA\":\"7468\",\n             \"itens\":{\n                \"item\":{\n                   \"CODPROD\":{\n                      \"$\":\"129\"\n                   },\n                   \"NUNOTA\":{\n                      \"$\":\"7468\"\n                   },\n                   \"SEQUENCIA\":{\n                      \"$\":\"\"\n                   },\n                   \"QTDNEG\":{\n                      \"$\":\"10\"\n                   },\n                   \"VLRUNIT\":{\n                      \"$\":\"10\"\n                   },\n                   \"VLRTOT\":{\n                      \"$\":\"432.38\"\n                   },\n                   \"CODVOL\":{\n                      \"$\":\"UN\"\n                   },\n                   \"VLRDESC\":{\n                      \"$\":\"0\"\n                   },\n                   \"PERCDESC\":{\n                      \"$\":\"0\"\n                   }\n                }\n             }\n          }\n       }\n    }\n\n\n<b>Corpo de Requisição Padrão para Alteração:</b>\n\n    {\n       \"serviceName\":\"CACSP.incluirAlterarItemNota\",\n       \"requestBody\":{\n          \"nota\":{\n             \"NUNOTA\":\"7468\",\n             \"itens\":{\n                \"item\":{\n                   \"CODPROD\":{\n                      \"$\":\"129\"\n                   },\n                   \"NUNOTA\":{\n                      \"$\":\"7468\"\n                   },\n                   \"SEQUENCIA\":{\n                      \"$\":\"10\"\n                   },\n                   \"QTDNEG\":{\n                      \"$\":\"8\"\n                   },\n                   \"VLRUNIT\":{\n                      \"$\":\"10\"\n                   },\n                   \"VLRTOT\":{\n                      \"$\":\"432.38\"\n                   },\n                   \"CODVOL\":{\n                      \"$\":\"UN\"\n                   },\n                   \"VLRDESC\":{\n                      \"$\":\"0\"\n                   },\n                   \"PERCDESC\":{\n                      \"$\":\"0\"\n                   }\n                }\n             }\n          }\n       }\n    }\n\n\n\n<b>Retorno:</b><br />\n\n    {\n        \"serviceName\": \"CACSP.incluirAlterarItemNota\",\n        \"status\": \"1\",\n        \"pendingPrinting\": \"false\",\n        \"transactionId\": \"46457EBA87743376561485A6021C8D8A\",\n        \"responseBody\": {\n            \"pk\": {\n                \"NUNOTA\": {\n                    \"$\": \"7468\"\n                },\n                \"SEQUENCIA\": {\n                    \"$\": \"8\"\n                }\n            }\n        }\n    }\n",
        "responses": {
          "201": {
            "description": "Inclusão / Alteração de itens realizada com sucesso!"
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
