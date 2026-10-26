---
id: "https://developer.sankhya.com.br/reference/get_loadrecord"
titulo: "Consultas com loadRecord (para registro único)"
url: "https://developer.sankhya.com.br/reference/get_loadrecord"
atualizado_em: "2026-05-13T15:12:48.000Z"
---

# Consultas com loadRecord (para registro único)

<h1>Regras de negócio</h1> A API possui um serviço genérico para aplicar consultas em todas as Entidades disponíveis no ERP: <b>CRUDServiceProvider.loadRecord</b> com o objetivo de obter 1 registro. O escopo da requisição é mais simples que <b>CRUDServiceProvider.loadRecord</b> e exige apenas o envio dos critérios por meio da tag "rows".

<br /> <h3>Exemplo de uso:</h3>
<ul>
  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>
  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>
</ul>
<b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecord&outputType=json
<br />Vejamos a seguir a estrutura completa de uma requisição do serviço loadRecords:

    {
       "serviceName": "CRUDServiceProvider.loadRecord",
       "requestBody": {
          "dataSet": {
             "rootEntity": "Produto",
             "entity": [
                {
                   "path": "",
                   "fieldset": {
                      "list": "CODPROD, DESCRPROD"
                   }
                },
                {
                   "path": "GrupoProduto",
                   "fieldset": {
                      "list": "CODGRUPOPROD, DESCRGRUPOPROD"
                   }
                },
                {
                   "path": "AliquotaIPI",
                   "fieldset": {
                      "list": "CODIPI, PERCENTUAL"
                   }
                }
             ],
             "rows": {
                "row": {
                   "CODPROD": {
                      "$": "4"
                   }
                }
             }
          }
       }
    }

O retorno para esta requisição é:<br />

    {
        "serviceName": "CRUDServiceProvider.loadRecord",
        "status": "1",
        "pendingPrinting": "false",
        "transactionId": "2B265FCF92393625B097EDE09B031295",
        "responseBody": {
            "entities": {
                "total": "1",
                "entity": {
                    "GrupoProduto_CODGRUPOPROD": {
                        "$": "10401"
                    },
                    "AliquotaIPI_PERCENTUAL": {
                        "$": "3"
                    },
                    "GrupoProduto_DESCRGRUPOPROD": {
                        "$": "REVENDA DE PRODUTO IMPORTADO"
                    },
                    "_rmd": {
                        "CODPROD": {
                            "$": "{\"decVlr\":2,\"decQtd\":0,\"controle\":{\"tipoContEst\":\"N\",\"listaContEst\":[\"\"],\"usaMascara\":false}}",
                            "provider": "PRODUTORMP"
                        }
                    },
                    "DESCRPROD": {
                        "$": "AGUA TONICA "
                    },
                    "CODPROD": {
                        "$": "4"
                    },
                    "AliquotaIPI_CODIPI": {
                        "$": "2"
                    }
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
      "name": "Como consultar dados?",
      "description": "Realizando consultas utilizando loadRecords"
    }
  ],
  "paths": {
    "/loadRecord": {
      "get": {
        "tags": [
          "Como consultar dados?"
        ],
        "summary": "Consultas com loadRecord (para registro único)",
        "description": "<h1>Regras de negócio</h1> A API possui um serviço genérico para aplicar consultas em todas as Entidades disponíveis no ERP: <b>CRUDServiceProvider.loadRecord</b> com o objetivo de obter 1 registro. O escopo da requisição é mais simples que <b>CRUDServiceProvider.loadRecord</b> e exige apenas o envio dos critérios por meio da tag \"rows\".\n\n<br /> <h3>Exemplo de uso:</h3>\n<ul>\n  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>\n  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>\n</ul>\n<b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecord&outputType=json\n<br />Vejamos a seguir a estrutura completa de uma requisição do serviço loadRecords:\n\n    {\n       \"serviceName\": \"CRUDServiceProvider.loadRecord\",\n       \"requestBody\": {\n          \"dataSet\": {\n             \"rootEntity\": \"Produto\",\n             \"entity\": [\n                {\n                   \"path\": \"\",\n                   \"fieldset\": {\n                      \"list\": \"CODPROD, DESCRPROD\"\n                   }\n                },\n                {\n                   \"path\": \"GrupoProduto\",\n                   \"fieldset\": {\n                      \"list\": \"CODGRUPOPROD, DESCRGRUPOPROD\"\n                   }\n                },\n                {\n                   \"path\": \"AliquotaIPI\",\n                   \"fieldset\": {\n                      \"list\": \"CODIPI, PERCENTUAL\"\n                   }\n                }\n             ],\n             \"rows\": {\n                \"row\": {\n                   \"CODPROD\": {\n                      \"$\": \"4\"\n                   }\n                }\n             }\n          }\n       }\n    }\n\nO retorno para esta requisição é:<br />\n\n    {\n        \"serviceName\": \"CRUDServiceProvider.loadRecord\",\n        \"status\": \"1\",\n        \"pendingPrinting\": \"false\",\n        \"transactionId\": \"2B265FCF92393625B097EDE09B031295\",\n        \"responseBody\": {\n            \"entities\": {\n                \"total\": \"1\",\n                \"entity\": {\n                    \"GrupoProduto_CODGRUPOPROD\": {\n                        \"$\": \"10401\"\n                    },\n                    \"AliquotaIPI_PERCENTUAL\": {\n                        \"$\": \"3\"\n                    },\n                    \"GrupoProduto_DESCRGRUPOPROD\": {\n                        \"$\": \"REVENDA DE PRODUTO IMPORTADO\"\n                    },\n                    \"_rmd\": {\n                        \"CODPROD\": {\n                            \"$\": \"{\\\"decVlr\\\":2,\\\"decQtd\\\":0,\\\"controle\\\":{\\\"tipoContEst\\\":\\\"N\\\",\\\"listaContEst\\\":[\\\"\\\"],\\\"usaMascara\\\":false}}\",\n                            \"provider\": \"PRODUTORMP\"\n                        }\n                    },\n                    \"DESCRPROD\": {\n                        \"$\": \"AGUA TONICA \"\n                    },\n                    \"CODPROD\": {\n                        \"$\": \"4\"\n                    },\n                    \"AliquotaIPI_CODIPI\": {\n                        \"$\": \"2\"\n                    }\n                }\n            }\n        }\n    }",
        "responses": {
          "201": {
            "description": "Consulta efetuada com sucesso"
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
