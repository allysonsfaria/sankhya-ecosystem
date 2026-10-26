---
id: "https://developer.sankhya.com.br/reference/post_incluimovimentos"
titulo: "Incluir Movimentos (pedidos, notas, etc)"
url: "https://developer.sankhya.com.br/reference/post_incluimovimentos"
atualizado_em: "2026-05-13T15:12:48.000Z"
---

# Incluir Movimentos (pedidos, notas, etc)

<h1>Regras de negócio</h1>
O cadastro de pedidos no sistema, permite que você registre e gerencie o que foi vendido e precisa ser faturado e entregue indicando, para qual cliente ou parceiro, quais as condições comerciais e financeiras negociadas e demais informações, proporcionando uma clara visão do que está em cada etapa do processo.<br />
<b>OBS:</b> Caso tenha alguma necessidade de configuração do ERP procure “Consultor” ou acesso o link de apoio:<br /> https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendasbr
<h3>Dependências</h3> Para realizar a inclusão do pedido, os seguintes itens são obrigatórios:<br />
<b>1) </b>Logar no sistema utilizando o Serviço de Login descrito nesta documentação em Login;<br />  <b>2) </b>Produtos/Serviços  preeviamente cadastrados e ativos;<br />  <b>3) </b>Empresas previamente cadastradas e ativas;<br /> <b>4) </b>Top's configuradas devidamente tipo de movimentação <b>\"Pedido de venda\"</b>;<br />  <b>5) </b>Tipo de negociação cadastrados seja  a vista, a prazo, parcelada, cheque.<br />  <b>6) </b>O parceiro deve estar cadastrado e ativo antes da geração do pedido.<br />
<h3>Detalhes Técnicos</h3> 
O serviço utilizado para inclusão de notas é o CACSP.IncluirNota que instancia as entidades principais para o envio de pedido, as entidades que este serviço utiliza são: <br />
<b>• CabecalhoNota;</b><br /> <b>• ItemNota.</b><br />
Os campos obrigatórios dependem estritamente da configuração de TOP,empresa, produto, etc. Portanto, neste exemplo colocamos os campos tipicamente obrigatórios em todos os casos de uso. Este exemplo não tenta exaurir as possibilidades,que são muitas, então em alguns casos a chamada a esse serviço pode resultar em mensagem de erro exigindo que outros campos sejam enviados. Apenas um pedido/nota pode ser enviado por vez. <br />
Para realizar a inclusão do pedido através do Json, os campos abaixo são obrigatórios:<br /><br /> <b>CABEÇALHO DO PEDIDO</b>

  - NUNOTA – Numero Único da nota;
  - CODPARC – Código do Parceiro;
  - DTNEG – Data de Negociação;
  - CODTIPOPER – Código do Tipo de Operação;
  - CODTIPVENDA – Tipo de Negociação;
  - CODVEND – Código do vendedor;
  - CODEMP – Código da Empresa;
  - TIPMOV – Tipo de Movimento.


<b>ITENS DO PEDIDO</b>

  - CODPROD – Código do Produto;
  - QTDNEG – Quantidade;
  - CODLOCALORIG – Código local de Origem;
  - CODVOL – Código do Volume;
  - IGNOREDESCPROMOQTD - Quando "True" garante que os valores enviados na API não serão alterados devido a algum disconto promocional vigente.

Conforme explicado  anteriormente, os campos enviados acima são obrigatórios e são os campos padrões. Os campos abaixo só serão obrigatórios se na requisição o campo \"<b><font color=red>INFORMARPRECO</font>\"</b> for igual a <b>true</b>, caso contrário  os campos abaixo não serão obrigatórios.<br/><br />  <b>• VLRUNIT</b> – Valor  Unitário;<br /> <b>• PERCDESC</b> – Percentual de desconto;<br /><br />
<b><font  color=red>IMPORTANTE</font>:</b> O atributo <b>INFORMARPRECO</b> serve para enviar o pedido com os valores já negociados e neste caso, o preço e o desconto terão que serem enviados para serem calculados. Caso o campo <b>informarPreço</b> = N então o ERP irá utilizar  valor da tabela de preços vigente no momento da inclusão do pedido.
<h3>Descritivo de Campos das Entidades</h3>
Acesse [aqui](http://swagger.sankhya.com.br/tabelas/TGFCAB.html) o dicionário de dados da tabela <b>TGFCAB</b><br />  Acesse [aqui](http://swagger.sankhya.com.br/tabelas/TGFITE.html) o dicionário de dados da tabela <b>TGFITE</b><br />
<h3>Exemplo de uso:</h3> <ul>
  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>
  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>
</ul> <b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mgecom/service.sbr?serviceName=CACSP.incluirNota&outputType=json <br /><br />
</b>Corpo de requisição</b>

    {
       "serviceName":"CACSP.incluirNota",
       "requestBody":{
          "nota":{
             "cabecalho":{
                "NUNOTA":{
                },
                "CODPARC":{
                   "$":"1"
                },
                "DTNEG":{
                   "$":"09/12/2022"
                },
                "CODTIPOPER":{
                   "$":"2000"
                },
                "CODTIPVENDA":{
                   "$":"12"
                },
                "CODVEND":{
                   "$":"0"
                },
                "CODEMP":{
                   "$":"1"
                },
                "TIPMOV":{
                   "$":"O"
                }
             },
             "itens":{
                "INFORMARPRECO":"True",
                "item":[
                      {
                       "NUNOTA":{
                      },
                      "IGNOREDESCPROMOQTD": {
                          "$": "True"
                      },
                      "CODPROD":{
                         "$":"8"
                      },
                      "QTDNEG":{
                         "$":"1"
                      },
                      "CODLOCALORIG":{
                         "$":"0"
                      },
                      "CODVOL":{
                         "$":"UN"
                      },
                      "PERCDESC": {
                        "$": "0"
                      },
                     "VLRUNIT": {
                        "$": "1.75"
                      }
                   }               
                ]
             }
          }
       }
    }


<b>Retorno:</b><br />


    {
        "serviceName": "CACSP.incluirNota",
        "status": "1",
        "pendingPrinting": "false",
        "transactionId": "1484EE05236C4B33DE6355DAA8443EFF",
        "responseBody": {
            "pk": {
                "NUNOTA": {
                    "$": "740"
                }
            }
        }
    }

<b><font color=red>IMPORTANTE</font>:</b> Este é apenas um exemplo de requisição baseado em um ambiente de teste. Todos os atributos devem ser revistos e ajustados considernado o ambiente do seu caso de uso.


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
    "/IncluiMovimentos": {
      "post": {
        "tags": [
          "Serviços Especialistas"
        ],
        "summary": "Incluir Movimentos (pedidos, notas, etc)",
        "description": "<h1>Regras de negócio</h1>\nO cadastro de pedidos no sistema, permite que você registre e gerencie o que foi vendido e precisa ser faturado e entregue indicando, para qual cliente ou parceiro, quais as condições comerciais e financeiras negociadas e demais informações, proporcionando uma clara visão do que está em cada etapa do processo.<br />\n<b>OBS:</b> Caso tenha alguma necessidade de configuração do ERP procure “Consultor” ou acesso o link de apoio:<br /> https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendasbr\n<h3>Dependências</h3> Para realizar a inclusão do pedido, os seguintes itens são obrigatórios:<br />\n<b>1) </b>Logar no sistema utilizando o Serviço de Login descrito nesta documentação em Login;<br />  <b>2) </b>Produtos/Serviços  preeviamente cadastrados e ativos;<br />  <b>3) </b>Empresas previamente cadastradas e ativas;<br /> <b>4) </b>Top's configuradas devidamente tipo de movimentação <b>\\\"Pedido de venda\\\"</b>;<br />  <b>5) </b>Tipo de negociação cadastrados seja  a vista, a prazo, parcelada, cheque.<br />  <b>6) </b>O parceiro deve estar cadastrado e ativo antes da geração do pedido.<br />\n<h3>Detalhes Técnicos</h3> \nO serviço utilizado para inclusão de notas é o CACSP.IncluirNota que instancia as entidades principais para o envio de pedido, as entidades que este serviço utiliza são: <br />\n<b>• CabecalhoNota;</b><br /> <b>• ItemNota.</b><br />\nOs campos obrigatórios dependem estritamente da configuração de TOP,empresa, produto, etc. Portanto, neste exemplo colocamos os campos tipicamente obrigatórios em todos os casos de uso. Este exemplo não tenta exaurir as possibilidades,que são muitas, então em alguns casos a chamada a esse serviço pode resultar em mensagem de erro exigindo que outros campos sejam enviados. Apenas um pedido/nota pode ser enviado por vez. <br />\nPara realizar a inclusão do pedido através do Json, os campos abaixo são obrigatórios:<br /><br /> <b>CABEÇALHO DO PEDIDO</b>\n\n  - NUNOTA – Numero Único da nota;\n  - CODPARC – Código do Parceiro;\n  - DTNEG – Data de Negociação;\n  - CODTIPOPER – Código do Tipo de Operação;\n  - CODTIPVENDA – Tipo de Negociação;\n  - CODVEND – Código do vendedor;\n  - CODEMP – Código da Empresa;\n  - TIPMOV – Tipo de Movimento.\n\n\n<b>ITENS DO PEDIDO</b>\n\n  - CODPROD – Código do Produto;\n  - QTDNEG – Quantidade;\n  - CODLOCALORIG – Código local de Origem;\n  - CODVOL – Código do Volume;\n  - IGNOREDESCPROMOQTD - Quando \"True\" garante que os valores enviados na API não serão alterados devido a algum disconto promocional vigente.\n\nConforme explicado  anteriormente, os campos enviados acima são obrigatórios e são os campos padrões. Os campos abaixo só serão obrigatórios se na requisição o campo \\\"<b><font color=red>INFORMARPRECO</font>\\\"</b> for igual a <b>true</b>, caso contrário  os campos abaixo não serão obrigatórios.<br/><br />  <b>• VLRUNIT</b> – Valor  Unitário;<br /> <b>• PERCDESC</b> – Percentual de desconto;<br /><br />\n<b><font  color=red>IMPORTANTE</font>:</b> O atributo <b>INFORMARPRECO</b> serve para enviar o pedido com os valores já negociados e neste caso, o preço e o desconto terão que serem enviados para serem calculados. Caso o campo <b>informarPreço</b> = N então o ERP irá utilizar  valor da tabela de preços vigente no momento da inclusão do pedido.\n<h3>Descritivo de Campos das Entidades</h3>\nAcesse [aqui](http://swagger.sankhya.com.br/tabelas/TGFCAB.html) o dicionário de dados da tabela <b>TGFCAB</b><br />  Acesse [aqui](http://swagger.sankhya.com.br/tabelas/TGFITE.html) o dicionário de dados da tabela <b>TGFITE</b><br />\n<h3>Exemplo de uso:</h3> <ul>\n  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>\n  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>\n</ul> <b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mgecom/service.sbr?serviceName=CACSP.incluirNota&outputType=json <br /><br />\n</b>Corpo de requisição</b>\n\n    {\n       \"serviceName\":\"CACSP.incluirNota\",\n       \"requestBody\":{\n          \"nota\":{\n             \"cabecalho\":{\n                \"NUNOTA\":{\n                },\n                \"CODPARC\":{\n                   \"$\":\"1\"\n                },\n                \"DTNEG\":{\n                   \"$\":\"09/12/2022\"\n                },\n                \"CODTIPOPER\":{\n                   \"$\":\"2000\"\n                },\n                \"CODTIPVENDA\":{\n                   \"$\":\"12\"\n                },\n                \"CODVEND\":{\n                   \"$\":\"0\"\n                },\n                \"CODEMP\":{\n                   \"$\":\"1\"\n                },\n                \"TIPMOV\":{\n                   \"$\":\"O\"\n                }\n             },\n             \"itens\":{\n                \"INFORMARPRECO\":\"True\",\n                \"item\":[\n                      {\n                       \"NUNOTA\":{\n                      },\n                      \"IGNOREDESCPROMOQTD\": {\n                          \"$\": \"True\"\n                      },\n                      \"CODPROD\":{\n                         \"$\":\"8\"\n                      },\n                      \"QTDNEG\":{\n                         \"$\":\"1\"\n                      },\n                      \"CODLOCALORIG\":{\n                         \"$\":\"0\"\n                      },\n                      \"CODVOL\":{\n                         \"$\":\"UN\"\n                      },\n                      \"PERCDESC\": {\n                        \"$\": \"0\"\n                      },\n                     \"VLRUNIT\": {\n                        \"$\": \"1.75\"\n                      }\n                   }               \n                ]\n             }\n          }\n       }\n    }\n\n\n<b>Retorno:</b><br />\n\n\n    {\n        \"serviceName\": \"CACSP.incluirNota\",\n        \"status\": \"1\",\n        \"pendingPrinting\": \"false\",\n        \"transactionId\": \"1484EE05236C4B33DE6355DAA8443EFF\",\n        \"responseBody\": {\n            \"pk\": {\n                \"NUNOTA\": {\n                    \"$\": \"740\"\n                }\n            }\n        }\n    }\n\n<b><font color=red>IMPORTANTE</font>:</b> Este é apenas um exemplo de requisição baseado em um ambiente de teste. Todos os atributos devem ser revistos e ajustados considernado o ambiente do seu caso de uso.\n",
        "responses": {
          "201": {
            "description": "Inclusão de pedidos realizada com sucesso!"
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
