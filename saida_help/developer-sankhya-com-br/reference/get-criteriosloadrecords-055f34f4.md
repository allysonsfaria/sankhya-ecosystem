---
id: "https://developer.sankhya.com.br/reference/get_criteriosloadrecords"
titulo: "Critérios em Consultas loadRecords"
url: "https://developer.sankhya.com.br/reference/get_criteriosloadrecords"
atualizado_em: "2026-05-13T15:12:48.000Z"
---

# Critérios em Consultas loadRecords

Quando temos parâmetros variáveis, como é o caso da expressão aqui usada, devemos colocar um '?' onde o valor do parâmetro será injetado. Para cada '?' na expressão devemos ter um elemento 'parameter'. Os possíveis valores para o atributo 'type' são: <ul>
  <li>D = Data sem horário</li>
  <li>H = Data com horário (no seguinte formato: DD/MM/AAAA HH:MM:SS)</li>
  <li>F = Número decimal (decimal separado por '.')</li>
  <li>I = Número inteiro</li>
  <li>S = Texto</li>
</ul> <br />IMPORTANTE: Sempre usar parâmetro para critérios do tipo data, pois colocar a data direto no SQL pode não funcionar corretamente devido ao charset, formato e tipo do banco de dados.

<h3>Segue exemplo utilizando filtro com parâmetros</h3>
<ul>
  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>
  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>
</ul>
<b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json <br /><br />

<b>Corpo de requisição</b>


    {
        "serviceName": "CRUDServiceProvider.loadRecords",
        "requestBody": {
            "dataSet": {
                "rootEntity": "Produto",
                "includePresentationFields": "N",
                "tryJoinedFields":"true",
                "offsetPage": "0",
                "criteria": {
                    "expression": {
                      "$": "CODPROD IN ( ?, ? )"
                    },
                    "parameter":
                        [
                            {
                                "$": "1",
                                "type": "I"
                            },
                            {
                                "$": "2",
                                "type": "I"
                            }
                        ]
                },
                "entity": {
                    "fieldset": {
                        "list": "CODPROD, DESCRPROD"
                    }
                }
            }
        }
    }

<br />Este exemplo retorna os produtos com código 1 e 2. A seguir um exemplo de utilização com cada tipo de parâmetro, focando na tag “criteria” onde a mudança é necessária:
<br />Aplicando filtro com número inteiro:

    ...
                "criteria": {
                    "expression": {
                      "$": "NUNOTA = ?"
                    },
                    "parameter": [
                        {
                            "$": "9120",
                            "type": "I"
                        }
                    ]
                },
    ...

<br />Aplicando filtro com número inteiro utilizando IN:

    ...
                "criteria": {
                    "expression": {
                      "$": "NUNOTA IN (?, ?, ?)"
                    },
                    "parameter": [
                        {
                            "$": "9120",
                            "type": "I"
                        },
                        {
                            "$": "9141",
                            "type": "I"
                        },
                        {
                            "$": "9159",
                            "type": "I"
                        }
                    ]
                },
    ...

<br />Aplicando filtro com data e hora:

    ...
                "criteria": {
                    "expression": {
                      "$": "DTFATUR >= ?"
                    },
                    "parameter": [
                        {
                            "$": "20/05/2022 09:31:43",
                            "type": "H"
                        }
                    ]
                },
    ...

<br />Aplicando filtro entre datas:

    ...
                "criteria": {
                    "expression": {
                      "$": "DHBAIXA IS NULL AND DTVENC BETWEEN ? AND ?"
                    },
                    "parameter": [
                        {
                            "$": "01/05/2022",
                            "type": "D"
                        },
                        {
                            "$": "31/05/2022",
                            "type": "D"
                        }
                    ]
                },
    ...

<br />Aplicando filtro com texto:

    ...
                "criteria": {
                    "expression": {
                      "$": "USOPROD = ? AND DESCRPROD LIKE '%?%'"
                    },
                    "parameter": [
                        {
                            "$": "V",
                            "type": "S"
                        },
                        {
                            "$": "CHEVE",
                            "type": "S"
                        }
                    ]
                },
    ...

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
    "/CriteriosLoadRecords": {
      "get": {
        "tags": [
          "Como consultar dados?"
        ],
        "summary": "Critérios em Consultas loadRecords",
        "description": "Quando temos parâmetros variáveis, como é o caso da expressão aqui usada, devemos colocar um '?' onde o valor do parâmetro será injetado. Para cada '?' na expressão devemos ter um elemento 'parameter'. Os possíveis valores para o atributo 'type' são: <ul>\n  <li>D = Data sem horário</li>\n  <li>H = Data com horário (no seguinte formato: DD/MM/AAAA HH:MM:SS)</li>\n  <li>F = Número decimal (decimal separado por '.')</li>\n  <li>I = Número inteiro</li>\n  <li>S = Texto</li>\n</ul> <br />IMPORTANTE: Sempre usar parâmetro para critérios do tipo data, pois colocar a data direto no SQL pode não funcionar corretamente devido ao charset, formato e tipo do banco de dados.\n\n<h3>Segue exemplo utilizando filtro com parâmetros</h3>\n<ul>\n  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>\n  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>\n</ul>\n<b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json <br /><br />\n\n<b>Corpo de requisição</b>\n\n\n    {\n        \"serviceName\": \"CRUDServiceProvider.loadRecords\",\n        \"requestBody\": {\n            \"dataSet\": {\n                \"rootEntity\": \"Produto\",\n                \"includePresentationFields\": \"N\",\n                \"tryJoinedFields\":\"true\",\n                \"offsetPage\": \"0\",\n                \"criteria\": {\n                    \"expression\": {\n                      \"$\": \"CODPROD IN ( ?, ? )\"\n                    },\n                    \"parameter\":\n                        [\n                            {\n                                \"$\": \"1\",\n                                \"type\": \"I\"\n                            },\n                            {\n                                \"$\": \"2\",\n                                \"type\": \"I\"\n                            }\n                        ]\n                },\n                \"entity\": {\n                    \"fieldset\": {\n                        \"list\": \"CODPROD, DESCRPROD\"\n                    }\n                }\n            }\n        }\n    }\n\n<br />Este exemplo retorna os produtos com código 1 e 2. A seguir um exemplo de utilização com cada tipo de parâmetro, focando na tag “criteria” onde a mudança é necessária:\n<br />Aplicando filtro com número inteiro:\n\n    ...\n                \"criteria\": {\n                    \"expression\": {\n                      \"$\": \"NUNOTA = ?\"\n                    },\n                    \"parameter\": [\n                        {\n                            \"$\": \"9120\",\n                            \"type\": \"I\"\n                        }\n                    ]\n                },\n    ...\n\n<br />Aplicando filtro com número inteiro utilizando IN:\n\n    ...\n                \"criteria\": {\n                    \"expression\": {\n                      \"$\": \"NUNOTA IN (?, ?, ?)\"\n                    },\n                    \"parameter\": [\n                        {\n                            \"$\": \"9120\",\n                            \"type\": \"I\"\n                        },\n                        {\n                            \"$\": \"9141\",\n                            \"type\": \"I\"\n                        },\n                        {\n                            \"$\": \"9159\",\n                            \"type\": \"I\"\n                        }\n                    ]\n                },\n    ...\n\n<br />Aplicando filtro com data e hora:\n\n    ...\n                \"criteria\": {\n                    \"expression\": {\n                      \"$\": \"DTFATUR >= ?\"\n                    },\n                    \"parameter\": [\n                        {\n                            \"$\": \"20/05/2022 09:31:43\",\n                            \"type\": \"H\"\n                        }\n                    ]\n                },\n    ...\n\n<br />Aplicando filtro entre datas:\n\n    ...\n                \"criteria\": {\n                    \"expression\": {\n                      \"$\": \"DHBAIXA IS NULL AND DTVENC BETWEEN ? AND ?\"\n                    },\n                    \"parameter\": [\n                        {\n                            \"$\": \"01/05/2022\",\n                            \"type\": \"D\"\n                        },\n                        {\n                            \"$\": \"31/05/2022\",\n                            \"type\": \"D\"\n                        }\n                    ]\n                },\n    ...\n\n<br />Aplicando filtro com texto:\n\n    ...\n                \"criteria\": {\n                    \"expression\": {\n                      \"$\": \"USOPROD = ? AND DESCRPROD LIKE '%?%'\"\n                    },\n                    \"parameter\": [\n                        {\n                            \"$\": \"V\",\n                            \"type\": \"S\"\n                        },\n                        {\n                            \"$\": \"CHEVE\",\n                            \"type\": \"S\"\n                        }\n                    ]\n                },\n    ...",
        "responses": {
          "201": {
            "description": "Cadastro efetuado com sucesso"
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
