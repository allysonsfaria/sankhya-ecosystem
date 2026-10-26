---
id: "https://developer.sankhya.com.br/reference/get_loadrecords"
titulo: "Consultas com loadRecords (para vários registros)"
url: "https://developer.sankhya.com.br/reference/get_loadrecords"
atualizado_em: "2026-05-13T15:12:48.000Z"
---

# Consultas com loadRecords (para vários registros)

<h1>Regras de negócio</h1> A API possui um serviço genérico para aplicar consultas em todas as Entidades disponíveis no ERP: <b>CRUDServiceProvider.loadRecords</b>. Por definição, uma entidade mapeia uma tabela que está no banco de dados, vejamos a seguir alguns exemplos de Entidade:<br /> <b>•</b> Entidade Produtos mapena a tabela TGFPRO<br /> <b>•</b> Entidade Parceiros mapeia a tabela TGFPAR<br />

<br /> <h3>Exemplo de uso:</h3>
<ul>
  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>
  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>
</ul>
<b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json
<br />Vejamos a seguir a estrutura completa de uma requisição do serviço loadRecords:

    {
        "serviceName": "CRUDServiceProvider.loadRecords",
        "requestBody": {
            "dataSet": {
                "rootEntity": "Produto",
                "ignoreCalculatedFields": "true",
                "useFileBasedPagination": "true",
                "includePresentationFields": "N",
                "tryJoinedFields": "true",
                "modifiedSince": "2024-04-16T12:59:59",
                "offsetPage": "0",
                "criteria": {
                    "expression": {
                      "$": "CODPROD IN ( ?, ? ) AND DESCRPROD LIKE '%?%'"
                    },
                    "parameter": [
                        {
                            "$": "1",
                            "type": "I"
                        },
                        {
                            "$": "2",
                            "type": "I"
                        },
                        {
                            "$": "QUEIJO",
                            "type": "S"
                        }
                    ]
                },
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
                    }
                ]
            }
        }
    }

Agora, vamos detalhar as propriedades utilizadas:<br /> <ul>
  <li>serviceName: nome do serviço e por padrão, sempre será: CRUDServiceProvider.loadRecords
rootEntity: nome da entidade a ser consultada.</li>
  <li>modifiedSince: faz referência a funcionalidade de logAlteracoesTabelas (<a href="https://developer.sankhya.com.br/reference/get_logalteracoestabelas">clique aqui</a> para mais detalhes sobre o recurso de LogAlteracoesTabelas). Quando esta funcionalidade está habilitada, é possível trazer apenas registros que tiveram alteração a partir de uma determinada data/hora. Vale ressaltar que este parâmetro é opcional, e ao enviar valores o serviço irá considerar “apenas” registros contidos no logAlteracoesTabelas. Caso não tenha informações logadas no sistema, o retorno do serviço será vazio (ZERO registros).</li>
  <li>ignoreCalculatedFields: quando configurado como `true`, os campos calculados são ignorados e apenas os campos persistidos em banco são retornados, reduzindo o volume de processamento e aumentando a performance da consulta. O valor padrão é false, ou seja, por padrão os campos calculados são incluídos no resultado.</li>
  <li>useFileBasedPagination: este atributo habilita a paginação baseada em disco. O padrão é utilizar memória do servidor para fazer paginações. É indicado para consultas com grande volume de dados (superior a 1000 páginas). Quando configurado como `true`, o processamento passa a ser realizado em disco, garantindo maior estabilidade e performance em cenários massivos. O valor padrão é false, mantendo a paginação tradicional para consultas comuns.</li>
  <li>offsetPage: indica a página a ser retornada. A página tem início em 0 (zero) e novas requisições devem ser realizadas, incrementando este valor, sempre que o retorno indicar mais registros através do parametro "hasMoreResult" com valor "true".</li>
  <li>criteria -> expression: condição da consulta. Sempre que houver "parâmetros" variáveis, deve ser utilizado os parâmetros (parameter) para indicar os valores para critério da consulta.</li>
  <li>criteria -> parameter: deve ser informado os valores para os parâmetros utilizados na consulta (clique aqui para mais detalhes sobre o recurso de critérios nos filtros).</li>
  <li>entity: são indicados os campos a serem retornados na consulta. Os campos estão disponíveis no <a href="https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados">Dicionário de Dados</a> para identificar quais campos serão necessários em cada entidade consultada. Esta propriedade também permite obter informações de entidades com ligação direta ao registro consultado. Ex.: para buscar um parceiro, através do CODBAI é possível trazer na consulta o nome do bairro. Isso se aplica a qualquer informação com ligação similar a esta (cidade, endereço, perfil, etc.). Clique aqui e para mais detalhes sobre "join" de dados nas consultas.</li>
</ul>
<br />Vejamos agora um exemplo de consulta de parceiros do tipo "Cliente" realizado na entidade "Parceiro":

    {
        "serviceName": "CRUDServiceProvider.loadRecords",
        "requestBody": {
            "dataSet": {
                "rootEntity": "Parceiro",
                "ignoreCalculatedFields": "true",
                "useFileBasedPagination": "true",
                "includePresentationFields": "N",
                "tryJoinedFields": "true",
                "offsetPage": "0",
                "criteria": {
                    "expression": {
                      "$": "CLIENTE = ?"
                    },
                    "parameter": [
                        {
                            "$": "S",
                            "type": "S"
                        }
                    ]
                },
                "entity": [
                    {
                        "path": "",
                        "fieldset": {
                            "list": "CODPARC, NOMEPARC, NUMEND, COMPLEMENTO, CEP"
                        }
                    },
                    {
                        "path": "Endereco",
                        "fieldset": {
                            "list":"CODEND, TIPO, NOMEEND"
                        }
                    },
                    {
                        "path": "Bairro",
                        "fieldset": {
                            "list": "CODBAI, NOMEBAI"
                        }
                    },
                    {
                        "path": "Cidade",
                        "fieldset": {
                            "list": "CODCID, NOMECID, UF"
                        }
                    }
                ]
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
    "/loadRecords": {
      "get": {
        "tags": [
          "Como consultar dados?"
        ],
        "summary": "Consultas com loadRecords (para vários registros)",
        "description": "<h1>Regras de negócio</h1> A API possui um serviço genérico para aplicar consultas em todas as Entidades disponíveis no ERP: <b>CRUDServiceProvider.loadRecords</b>. Por definição, uma entidade mapeia uma tabela que está no banco de dados, vejamos a seguir alguns exemplos de Entidade:<br /> <b>•</b> Entidade Produtos mapena a tabela TGFPRO<br /> <b>•</b> Entidade Parceiros mapeia a tabela TGFPAR<br />\n\n<br /> <h3>Exemplo de uso:</h3>\n<ul>\n  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>\n  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>\n</ul>\n<b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json\n<br />Vejamos a seguir a estrutura completa de uma requisição do serviço loadRecords:\n\n    {\n        \"serviceName\": \"CRUDServiceProvider.loadRecords\",\n        \"requestBody\": {\n            \"dataSet\": {\n                \"rootEntity\": \"Produto\",\n                \"ignoreCalculatedFields\": \"true\",\n                \"useFileBasedPagination\": \"true\",\n                \"includePresentationFields\": \"N\",\n                \"tryJoinedFields\": \"true\",\n                \"modifiedSince\": \"2024-04-16T12:59:59\",\n                \"offsetPage\": \"0\",\n                \"criteria\": {\n                    \"expression\": {\n                      \"$\": \"CODPROD IN ( ?, ? ) AND DESCRPROD LIKE '%?%'\"\n                    },\n                    \"parameter\": [\n                        {\n                            \"$\": \"1\",\n                            \"type\": \"I\"\n                        },\n                        {\n                            \"$\": \"2\",\n                            \"type\": \"I\"\n                        },\n                        {\n                            \"$\": \"QUEIJO\",\n                            \"type\": \"S\"\n                        }\n                    ]\n                },\n                \"entity\": [\n                    {\n                        \"path\": \"\",\n                        \"fieldset\": {\n                            \"list\": \"CODPROD, DESCRPROD\"\n                        }\n                    },\n                    {\n                        \"path\": \"GrupoProduto\",\n                        \"fieldset\": {\n                            \"list\": \"CODGRUPOPROD, DESCRGRUPOPROD\"\n                        }\n                    }\n                ]\n            }\n        }\n    }\n\nAgora, vamos detalhar as propriedades utilizadas:<br /> <ul>\n  <li>serviceName: nome do serviço e por padrão, sempre será: CRUDServiceProvider.loadRecords\nrootEntity: nome da entidade a ser consultada.</li>\n  <li>modifiedSince: faz referência a funcionalidade de logAlteracoesTabelas (<a href=\"https://developer.sankhya.com.br/reference/get_logalteracoestabelas\">clique aqui</a> para mais detalhes sobre o recurso de LogAlteracoesTabelas). Quando esta funcionalidade está habilitada, é possível trazer apenas registros que tiveram alteração a partir de uma determinada data/hora. Vale ressaltar que este parâmetro é opcional, e ao enviar valores o serviço irá considerar “apenas” registros contidos no logAlteracoesTabelas. Caso não tenha informações logadas no sistema, o retorno do serviço será vazio (ZERO registros).</li>\n  <li>ignoreCalculatedFields: quando configurado como `true`, os campos calculados são ignorados e apenas os campos persistidos em banco são retornados, reduzindo o volume de processamento e aumentando a performance da consulta. O valor padrão é false, ou seja, por padrão os campos calculados são incluídos no resultado.</li>\n  <li>useFileBasedPagination: este atributo habilita a paginação baseada em disco. O padrão é utilizar memória do servidor para fazer paginações. É indicado para consultas com grande volume de dados (superior a 1000 páginas). Quando configurado como `true`, o processamento passa a ser realizado em disco, garantindo maior estabilidade e performance em cenários massivos. O valor padrão é false, mantendo a paginação tradicional para consultas comuns.</li>\n  <li>offsetPage: indica a página a ser retornada. A página tem início em 0 (zero) e novas requisições devem ser realizadas, incrementando este valor, sempre que o retorno indicar mais registros através do parametro \"hasMoreResult\" com valor \"true\".</li>\n  <li>criteria -> expression: condição da consulta. Sempre que houver \"parâmetros\" variáveis, deve ser utilizado os parâmetros (parameter) para indicar os valores para critério da consulta.</li>\n  <li>criteria -> parameter: deve ser informado os valores para os parâmetros utilizados na consulta (clique aqui para mais detalhes sobre o recurso de critérios nos filtros).</li>\n  <li>entity: são indicados os campos a serem retornados na consulta. Os campos estão disponíveis no <a href=\"https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados\">Dicionário de Dados</a> para identificar quais campos serão necessários em cada entidade consultada. Esta propriedade também permite obter informações de entidades com ligação direta ao registro consultado. Ex.: para buscar um parceiro, através do CODBAI é possível trazer na consulta o nome do bairro. Isso se aplica a qualquer informação com ligação similar a esta (cidade, endereço, perfil, etc.). Clique aqui e para mais detalhes sobre \"join\" de dados nas consultas.</li>\n</ul>\n<br />Vejamos agora um exemplo de consulta de parceiros do tipo \"Cliente\" realizado na entidade \"Parceiro\":\n\n    {\n        \"serviceName\": \"CRUDServiceProvider.loadRecords\",\n        \"requestBody\": {\n            \"dataSet\": {\n                \"rootEntity\": \"Parceiro\",\n                \"ignoreCalculatedFields\": \"true\",\n                \"useFileBasedPagination\": \"true\",\n                \"includePresentationFields\": \"N\",\n                \"tryJoinedFields\": \"true\",\n                \"offsetPage\": \"0\",\n                \"criteria\": {\n                    \"expression\": {\n                      \"$\": \"CLIENTE = ?\"\n                    },\n                    \"parameter\": [\n                        {\n                            \"$\": \"S\",\n                            \"type\": \"S\"\n                        }\n                    ]\n                },\n                \"entity\": [\n                    {\n                        \"path\": \"\",\n                        \"fieldset\": {\n                            \"list\": \"CODPARC, NOMEPARC, NUMEND, COMPLEMENTO, CEP\"\n                        }\n                    },\n                    {\n                        \"path\": \"Endereco\",\n                        \"fieldset\": {\n                            \"list\":\"CODEND, TIPO, NOMEEND\"\n                        }\n                    },\n                    {\n                        \"path\": \"Bairro\",\n                        \"fieldset\": {\n                            \"list\": \"CODBAI, NOMEBAI\"\n                        }\n                    },\n                    {\n                        \"path\": \"Cidade\",\n                        \"fieldset\": {\n                            \"list\": \"CODCID, NOMECID, UF\"\n                        }\n                    }\n                ]\n            }\n        }\n    }",
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
