---
id: "https://developer.sankhya.com.br/reference/post_faturamovimento"
titulo: "Faturamento de Movimentos"
url: "https://developer.sankhya.com.br/reference/post_faturamovimento"
atualizado_em: "2026-05-13T15:12:48.000Z"
---

# Faturamento de Movimentos

<h1>Regras de negócio</h1> 
Para finalizar uma venda, o pedido de vendas precisa ser faturado, ou seja, transformado em nota fiscal ou Ordem de Entrega.<br />
O conceito prático de faturamento, consiste em transformar um pedido de venda em uma nota fiscal de Venda; porém, na passagem de um orçamento para um pedido de venda, pode-se entender que também houve um faturamento, mas não com as mesmas validações mencionadas acima.<br />
<b>Vale ressaltar que, os comportamentos citados, poderão variar de acordo com o processo de cada empresa.</b><br />
<b>OBS:</b> Caso tenha alguma necessidade de configuração do ERP procure “Consultor” ou acesso o link de apoio:<br /> https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas#faturamento-comofazer<br />
<h3>Dependências</h3> Para realizar o faturamento do pedido, os seguintes itens são obrigatórios:<br />
<b>1) </b>Logar no sistema utilizando o Serviço de Login descrito nesta documentação em Login; <br />  <b>2) </b>O pedido deve estar confirmado no ERP Sankhya-Om;<br />  <b>3) </b>É obrigatório informar o número único do pedido.<br />  <b>4) </b>É obrigatório configurar o tipo de operação(TOP) para atender a requisição de faturamento vindo do json<br />  <b>5) </b>É obrigatório informar o tipo de operação(TOP) de faturamento para a nota fiscal.<br />
<b>OBS:</b> O faturamento pelo json passa pelas mesmas regras definidas e configuradas nas TOPs do ERP.<br /> 
<h3>Detalhes Técnicos</h3>
O serviço utilizado para o faturamento de pedidos é o SelecaoDocumentoSP.faturar que utiliza a entidade CabecalhoNota que por sua vez instancia a tabela TGFCAB.<br />
Para realizar o faturamento do pedido o campo abaixo é obrigatório:<br /><br /> <b>• NUNOTA</b> – Numero Único da nota;<br /><br />
Ao realizar o faturamento deve-se passar no campo <b>NUNOTA</b> o número do pedido que deseja faturar.<br />
Após o serviço executar o faturamento no ERP ele retorna o NUNOTA da nota fiscal gerada. ( Lembrando que o <b>NUNOTA</b> não é o número da nota e sim apenas a chave (PK) interna que identifica o documento na tabela TGFCAB ).<br />
Para obter os dados da nota fiscal gerada, deve-se fazer chamada ao serviço de consulta de <b>pedidos/notas</b> passando como parâmetro o NUNOTA da nota fiscal que foi retornado durante a chamada do serviço de faturamento.<br />
Assim conseguirá obter todas as informações da nota fiscal que foi gerada no faturamento.<br />\n  Importante: A nota faturada fica ligada com o pedido pela tabela <b>TGFVAR</b> ( ver serviço de consulta de \"Ligação Nota x Pedido\" )<br /><br /><br />
<b>Opções de Faturamento (atributo: tipoFaturamento):</b>
  - Faturamento normal (FaturamentoNormal): Faturamento da nota independente dos itens, ao utilizar esta opção o faturamento é realizado juntamente com a quantidade total de itens na nota.

        ...
        "notas": {
          "codTipOper": 167,
          "dtFaturamento": "04/02/2021",
          "tipoFaturamento": "FaturamentoNormal",
          "dataValidada": true,
          "notasComMoeda": {
          
          },         
          "nota": [
            {
              "$": 7434
            }
          ],
          "faturarTodosItens": true
        }
        ...
        
  - Faturamento por Item e por quantidade: Faturamento por item, permite selecionar o item que será faturado e a sua quantidade, permitindo assim, faturar parcialmente um pedido ou um item.
  
        ...
        "nota": [
          {
            "NUNOTA": "7432",
            "itens": {
              "item": [
                {
                  "QTDFAT": 2,
                  "$": 1
                }
              ],
              "faturarTodosItens": false,
            }
          }
        ],
        ...
  
  
  - Faturamento por Estoque: Para realizar o faturamento por estoque o parâmetro <b>FATEST-RESERV</b> deverá estar desligado no ERP.
  
        ...
        "notas": {
          "codTipOper": 167,
          "dtFaturamento": "04/02/2021",
          "serie": "",
          "dtSaida": "04/02/2021",
          "hrSaida": "",
          "tipoFaturamento": "FaturamentoEstoque",
          "dataValidada": true,
          "notasComMoeda": {
          
          },         
          "nota": [
            {
              "$": 7434
            }
          ],
          "faturarTodosItens": true
        }
        ...
  
  - Faturamento por Estoque deixando pendente: Faturar pelo estoque deixando pendente, serve para atender os itens que possuem estoque, sendo assim, os itens que não possuem estoque ficam como pendentes para serem atendidos posteriormente em um novo faturamento. Para realizar o faturamento por estoque o parâmetro <b>FATEST-RESERV</b> deverá estar desligado no ERP.
  
        ...
        "notas": {
          "codTipOper": 167,
          "dtFaturamento": "04/02/2021",
          "serie": "",
          "dtSaida": "04/02/2021",
          "hrSaida": "",
          "tipoFaturamento": "FaturamentoEstoqueDeixandoPendente",
          "dataValidada": true,
          "notasComMoeda": {
          
          },         
          "nota": [
            {
              "$": 7439
            }
          ],
          "faturarTodosItens": true
        }
        ...
  
  - Faturamento Direto:

        ...
        "notas": {
          "codTipOper": 28600,
          "dtFaturamento": "27/07/2021",
          "tipoFaturamento": "FaturamentoDireto",
          "dataValidada": true,
          "serie": "1",
          "tipoFaturamento": "FaturamentoDireto",
          "notasComMoeda": {
          
          },         
          "nota": [
            {
              "$": 7439
            }
          ],
          "faturarTodosItens": true
        }
        ...


OBSERVAÇÃO: Nota-se que que nas opções de por estoque a tag <b>tipoFaturamento</b> é alterada para <b>\"FaturamentoEstoque\"</b> ou <b>\"FaturamentoEstoqueDeixandoPendente\"</b> nos demais tag fica com a opção <b>FaturamentoNormal</b>. <br />
<h3>Descritivo de Campos das Entidades</h3>
Acesse [aqui](http://swagger.sankhya.com.br/tabelas/TGFCAB.html) o dicionário de dados da tabela <b>TGFCAB</b><br /> 



<h3>Exemplo de uso:</h3>
<b>URL de chamada</b>: <ul>
  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>
  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>
</ul> <b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mgecom/service.sbr?serviceName=SelecaoDocumentoSP.faturar&outputType=json<br />
<b>Corpo de requisição</b>

    {
       "serviceName":"SelecaoDocumentoSP.faturar",
       "requestBody":{
          "notas":{
             "codTipOper":167,
             "dtFaturamento":"04/02/2021",
             "tipoFaturamento":"FaturamentoNormal",
             "dataValidada":true,
             "notasComMoeda":{
                
             },
             "nota":[
                {
                   "$":7434
                }
             ],
             "codLocalDestino":"",
             "faturarTodosItens":true,
             "umaNotaParaCada":"false",
             "ehWizardFaturamento":true,
             "dtFixaVenc":"",
             "ehPedidoWeb":false,
             "nfeDevolucaoViaRecusa":false
          }
       }
    }


<b>Retorno:</b><br />

    {
        "serviceName": "SelecaoDocumentoSP.faturar",
        "status": "1",
        "pendingPrinting": "false",
        "transactionId": "C688DB3E5193312092DC853D04B7BBE2",
        "responseBody": {
            "codUsuLogado": {
                "$": "0"
            },
            "notas": {
                "tipMov": "V",
                "nota": {
                    "$": "7435"
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
    "/FaturaMovimento": {
      "post": {
        "tags": [
          "Serviços Especialistas"
        ],
        "summary": "Faturamento de Movimentos",
        "description": "<h1>Regras de negócio</h1> \nPara finalizar uma venda, o pedido de vendas precisa ser faturado, ou seja, transformado em nota fiscal ou Ordem de Entrega.<br />\nO conceito prático de faturamento, consiste em transformar um pedido de venda em uma nota fiscal de Venda; porém, na passagem de um orçamento para um pedido de venda, pode-se entender que também houve um faturamento, mas não com as mesmas validações mencionadas acima.<br />\n<b>Vale ressaltar que, os comportamentos citados, poderão variar de acordo com o processo de cada empresa.</b><br />\n<b>OBS:</b> Caso tenha alguma necessidade de configuração do ERP procure “Consultor” ou acesso o link de apoio:<br /> https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas#faturamento-comofazer<br />\n<h3>Dependências</h3> Para realizar o faturamento do pedido, os seguintes itens são obrigatórios:<br />\n<b>1) </b>Logar no sistema utilizando o Serviço de Login descrito nesta documentação em Login; <br />  <b>2) </b>O pedido deve estar confirmado no ERP Sankhya-Om;<br />  <b>3) </b>É obrigatório informar o número único do pedido.<br />  <b>4) </b>É obrigatório configurar o tipo de operação(TOP) para atender a requisição de faturamento vindo do json<br />  <b>5) </b>É obrigatório informar o tipo de operação(TOP) de faturamento para a nota fiscal.<br />\n<b>OBS:</b> O faturamento pelo json passa pelas mesmas regras definidas e configuradas nas TOPs do ERP.<br /> \n<h3>Detalhes Técnicos</h3>\nO serviço utilizado para o faturamento de pedidos é o SelecaoDocumentoSP.faturar que utiliza a entidade CabecalhoNota que por sua vez instancia a tabela TGFCAB.<br />\nPara realizar o faturamento do pedido o campo abaixo é obrigatório:<br /><br /> <b>• NUNOTA</b> – Numero Único da nota;<br /><br />\nAo realizar o faturamento deve-se passar no campo <b>NUNOTA</b> o número do pedido que deseja faturar.<br />\nApós o serviço executar o faturamento no ERP ele retorna o NUNOTA da nota fiscal gerada. ( Lembrando que o <b>NUNOTA</b> não é o número da nota e sim apenas a chave (PK) interna que identifica o documento na tabela TGFCAB ).<br />\nPara obter os dados da nota fiscal gerada, deve-se fazer chamada ao serviço de consulta de <b>pedidos/notas</b> passando como parâmetro o NUNOTA da nota fiscal que foi retornado durante a chamada do serviço de faturamento.<br />\nAssim conseguirá obter todas as informações da nota fiscal que foi gerada no faturamento.<br />\\n  Importante: A nota faturada fica ligada com o pedido pela tabela <b>TGFVAR</b> ( ver serviço de consulta de \\\"Ligação Nota x Pedido\\\" )<br /><br /><br />\n<b>Opções de Faturamento (atributo: tipoFaturamento):</b>\n  - Faturamento normal (FaturamentoNormal): Faturamento da nota independente dos itens, ao utilizar esta opção o faturamento é realizado juntamente com a quantidade total de itens na nota.\n\n        ...\n        \"notas\": {\n          \"codTipOper\": 167,\n          \"dtFaturamento\": \"04/02/2021\",\n          \"tipoFaturamento\": \"FaturamentoNormal\",\n          \"dataValidada\": true,\n          \"notasComMoeda\": {\n          \n          },         \n          \"nota\": [\n            {\n              \"$\": 7434\n            }\n          ],\n          \"faturarTodosItens\": true\n        }\n        ...\n        \n  - Faturamento por Item e por quantidade: Faturamento por item, permite selecionar o item que será faturado e a sua quantidade, permitindo assim, faturar parcialmente um pedido ou um item.\n  \n        ...\n        \"nota\": [\n          {\n            \"NUNOTA\": \"7432\",\n            \"itens\": {\n              \"item\": [\n                {\n                  \"QTDFAT\": 2,\n                  \"$\": 1\n                }\n              ],\n              \"faturarTodosItens\": false,\n            }\n          }\n        ],\n        ...\n  \n  \n  - Faturamento por Estoque: Para realizar o faturamento por estoque o parâmetro <b>FATEST-RESERV</b> deverá estar desligado no ERP.\n  \n        ...\n        \"notas\": {\n          \"codTipOper\": 167,\n          \"dtFaturamento\": \"04/02/2021\",\n          \"serie\": \"\",\n          \"dtSaida\": \"04/02/2021\",\n          \"hrSaida\": \"\",\n          \"tipoFaturamento\": \"FaturamentoEstoque\",\n          \"dataValidada\": true,\n          \"notasComMoeda\": {\n          \n          },         \n          \"nota\": [\n            {\n              \"$\": 7434\n            }\n          ],\n          \"faturarTodosItens\": true\n        }\n        ...\n  \n  - Faturamento por Estoque deixando pendente: Faturar pelo estoque deixando pendente, serve para atender os itens que possuem estoque, sendo assim, os itens que não possuem estoque ficam como pendentes para serem atendidos posteriormente em um novo faturamento. Para realizar o faturamento por estoque o parâmetro <b>FATEST-RESERV</b> deverá estar desligado no ERP.\n  \n        ...\n        \"notas\": {\n          \"codTipOper\": 167,\n          \"dtFaturamento\": \"04/02/2021\",\n          \"serie\": \"\",\n          \"dtSaida\": \"04/02/2021\",\n          \"hrSaida\": \"\",\n          \"tipoFaturamento\": \"FaturamentoEstoqueDeixandoPendente\",\n          \"dataValidada\": true,\n          \"notasComMoeda\": {\n          \n          },         \n          \"nota\": [\n            {\n              \"$\": 7439\n            }\n          ],\n          \"faturarTodosItens\": true\n        }\n        ...\n  \n  - Faturamento Direto:\n\n        ...\n        \"notas\": {\n          \"codTipOper\": 28600,\n          \"dtFaturamento\": \"27/07/2021\",\n          \"tipoFaturamento\": \"FaturamentoDireto\",\n          \"dataValidada\": true,\n          \"serie\": \"1\",\n          \"tipoFaturamento\": \"FaturamentoDireto\",\n          \"notasComMoeda\": {\n          \n          },         \n          \"nota\": [\n            {\n              \"$\": 7439\n            }\n          ],\n          \"faturarTodosItens\": true\n        }\n        ...\n\n\nOBSERVAÇÃO: Nota-se que que nas opções de por estoque a tag <b>tipoFaturamento</b> é alterada para <b>\\\"FaturamentoEstoque\\\"</b> ou <b>\\\"FaturamentoEstoqueDeixandoPendente\\\"</b> nos demais tag fica com a opção <b>FaturamentoNormal</b>. <br />\n<h3>Descritivo de Campos das Entidades</h3>\nAcesse [aqui](http://swagger.sankhya.com.br/tabelas/TGFCAB.html) o dicionário de dados da tabela <b>TGFCAB</b><br /> \n\n\n\n<h3>Exemplo de uso:</h3>\n<b>URL de chamada</b>: <ul>\n  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>\n  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>\n</ul> <b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mgecom/service.sbr?serviceName=SelecaoDocumentoSP.faturar&outputType=json<br />\n<b>Corpo de requisição</b>\n\n    {\n       \"serviceName\":\"SelecaoDocumentoSP.faturar\",\n       \"requestBody\":{\n          \"notas\":{\n             \"codTipOper\":167,\n             \"dtFaturamento\":\"04/02/2021\",\n             \"tipoFaturamento\":\"FaturamentoNormal\",\n             \"dataValidada\":true,\n             \"notasComMoeda\":{\n                \n             },\n             \"nota\":[\n                {\n                   \"$\":7434\n                }\n             ],\n             \"codLocalDestino\":\"\",\n             \"faturarTodosItens\":true,\n             \"umaNotaParaCada\":\"false\",\n             \"ehWizardFaturamento\":true,\n             \"dtFixaVenc\":\"\",\n             \"ehPedidoWeb\":false,\n             \"nfeDevolucaoViaRecusa\":false\n          }\n       }\n    }\n\n\n<b>Retorno:</b><br />\n\n    {\n        \"serviceName\": \"SelecaoDocumentoSP.faturar\",\n        \"status\": \"1\",\n        \"pendingPrinting\": \"false\",\n        \"transactionId\": \"C688DB3E5193312092DC853D04B7BBE2\",\n        \"responseBody\": {\n            \"codUsuLogado\": {\n                \"$\": \"0\"\n            },\n            \"notas\": {\n                \"tipMov\": \"V\",\n                \"nota\": {\n                    \"$\": \"7435\"\n                }\n            }\n        }\n    }\n",
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
