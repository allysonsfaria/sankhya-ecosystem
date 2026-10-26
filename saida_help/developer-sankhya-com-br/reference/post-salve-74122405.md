---
id: "https://developer.sankhya.com.br/reference/post_salve"
titulo: "Incluir e Alterar Dados"
url: "https://developer.sankhya.com.br/reference/post_salve"
atualizado_em: "2026-05-13T15:12:48.000Z"
---

# Incluir e Alterar Dados

<h1>Regras de negócio</h1> 
Utilizando a API é possível realizar a inclusão, ou atualização, de dados no SankhyaOm. Para isso, utilizamos o serviço \"DatasetSP.save\". O mesmo serviço é utilizado para ambos os casos, o que vai indicar se é inclusão ou atualização é o envio da chave primária do registro ou não, ou seja, ao enviar a chave primária indica a necessidade de atualização, e caso a chave primária não seja enviada, a API entende que é necessário fazer a inclusão do registro.<br /><br />
<h3>Exemplo de uso</h3> <ul>
  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>
  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>
</ul> <b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mge/service.sbr?serviceName=DatasetSP.save&outputType=json<br /><br />
<b>Vejamos agora a estrutura base da requisição para incluir e atualizar dados via API:</b>


    {
       "serviceName":"DatasetSP.save",
       "requestBody":{
          "entityName":"NomeDaEntidade",
          "standAlone":false,
          "fields":[ "CAMPO_1",
            "CAMPO_2",
            "CAMPO_N"
          ],
          "records":[
             {
                "pk":{  // deve ser enviado apenas para situação de atualização
                   "NOME_PK":"VALOR_PK"
                },
                "values":{
                   "0": "VALOR_1",
                   "1": "VALOR_2",
                   "2": "VALOR_N"
                }
             }
          ]
       }
    }


<br /> Esta estrutura é padrão, e permite fazer inclusão, e atualização, em qualquer entidade existente no SankhyaOm. Para isso, basta indicar a Entidade (entityName), os campos (fields) e os respectivos valores (records).<br /> Veremos a seguir 2 exemplos práticos de inclusão e atualização de registros. <br /><br /><br />
<h2>Como fazer a inclusão de dados?</h2>  Agora que temos a estrutura base da requisição para incluir e atualizar dados via API, vamos apresentar um exemplo de inclusão utilizando registros com PK simples e com PK composta. Veja a seguir a inclusão de um Parceiro e seu contato.<br /><br /> <b>Exemplo para incluir parceiro:</b>


    {
       "serviceName":"DatasetSP.save",
       "requestBody":{
          "entityName":"Parceiro",
          "standAlone":false,
          "fields":[
             "CODPARC",
             "NOMEPARC",
             "ATIVO",
             "TIPPESSOA",
             "CODCID",
             "CODREG",
             "CLASSIFICMS",
             "ComplementoParc.SUGTIPNEGENTR",
             "ComplementoParc.SUGTIPNEGSAID"
          ],
          "records":[
             {
                "values":{
                   "1":"NOME DO PARCEIRO BEM AQUI",
                   "2":"S",
                   "3":"F",
                   "4":"1",
                   "5":"0",
                   "6":"C",
                   "7":"13",
                   "8":"13"
                }
             }
          ]
       }
    }

<b>Retorno:</b>

    {
        "serviceName": "DatasetSP.save",
        "status": "1",
        "pendingPrinting": "false",
        "transactionId": "EAE26797DAF8A192B2FFF990097337A7",
        "responseBody": {
            "total": "1",
            "result": [
                [
                    "4454",
                    "NOME DO PARCEIRO BEM AQUI",
                    "S",
                    "F",
                    "1",
                    "0",
                    "C",
                    "13",
                    "13"
                ]
            ]
        }
    }

<br />No retorno, a primeira linha da requisição indica o Código atribuído a este parceiro (neste exemplo 4454).<br /> Agora, vamos fazer a inclusão de múltiplos registros utilizando PK do parceiro como chave de ligação para registros de detalhe. O json a seguir inclui dois contatos para o parceiro na entidade Contato que possui PK composta (CODPARC, CODCONTATO). Segue json para incluir os contatos para o parceiro recém incluído:<br /><br />
<b>Exemplo para incluir os contatos do parceiro:</b>

    {
       "serviceName":"DatasetSP.save",
       "requestBody":{
          "entityName":"Contato",
          "standAlone":false,
          "fields":[
             "CODCONTATO",
             "ATIVO",
             "NOMECONTATO",
             "EMAIL",
             "CELULAR"
          ],
          "records":[
             {
                "foreignKey":{
                   "CODPARC":"4454"
                },
                "values":{
                   "1":"S",
                   "2":"Nome do Contato 1",
                   "4":"33  999998888"
                }
             },
             {
                "foreignKey":{
                   "CODPARC":"4454"
                },
                "values":{
                   "1":"S",
                   "2":"Nome do Contato 2",
                   "4":"33  999998888"
                }
             }
          ]
       }
    }

<b>Retorno:</b><br/>

    {
        "serviceName": "DatasetSP.save",
        "status": "1",
        "pendingPrinting": "false",
        "transactionId": "A0B2291C8ED35C5DD22E42B36B98BE97",
        "responseBody": {
            "total": "2",
            "result": [
                [
                    "1",
                    "S",
                    "NOME DO CONTATO 1",
                    "",
                    "33  999998888"
                ],
                [
                    "2",
                    "S",
                    "NOME DO CONTATO 2",
                    "",
                    "33  999998888"
                ]
            ]
        }
    }


<br />Dessa forma, com uma requisição conseguimos realizar múltiplas inclusões. Note que incluirmos o contato código 1 e 2 para o parceiro 4454.\n<br />Vale ressaltar que não é necessário enviar todos os dados (records) indicados na seção de campos (fields). O exemplo acima indica 5 campos, mas envia apenas 3 informações para realizar a inclusão do parceiro.<br /><br />
<h2>Como fazer alterações em dados?</h2>  Agora que vimos como incluir registros, vamos fazer algumas atualizações nos cadastros incluídos recentemente. Vamos atualizar o nome do parceiro e adicionar e-mails aos contatos que foram vinculados ao parceiro.<br />
Para realizar uma atualização de cadastro, basta indicar a PK forte do registro desejado. Vejamos a seguir o json para atualizar o cadastro do parceiro 4454:<br />

    {
       "serviceName":"DatasetSP.save",
       "requestBody": {
          "entityName":"Parceiro",
          "standAlone":false,
          "fields": [
             "CODPARC",
             "NOMEPARC",
             "ATIVO",
             "TIPPESSOA"
          ],
          "records":[
             {
                "pk": {
                   "CODPARC":"4454"
                },
                "values": {
                   "1":"JOSE DA SILVA XAVIER"
                }
             }
          ]
       }
    }




<b>Retorno:</b><br />

    {
        "serviceName": "DatasetSP.save",
        "status": "1",
        "pendingPrinting": "false",
        "transactionId": "E5526480FF334FF05DC6118028A60AE0",
        "responseBody": {
            "total": "1",
            "result": [
                [
                    "4454",
                    "JOSE DA SILVA XAVIER",
                    "S",
                    "F"
                ]
            ]
        }
    }


<br />Agora vamos atualizar o cadastro dos dois contatos, adicionando e-mails aos mesmos. Segue json para realizar a requisição:<br />

    {
       "serviceName":"DatasetSP.save",
       "requestBody":{
          "entityName":"Contato",
          "standAlone":false,
          "fields":[
             "CODCONTATO",
             "ATIVO",
             "NOMECONTATO",
             "EMAIL",
             "CELULAR"
          ],
          "records":[
             {
                "pk":{
                   "CODPARC":"4454",
                   "CODCONTATO":"1"
                },
                "values":{
                   "3":"financeiro@empresa.com.br"
                }
             },
             {
                "pk":{
                   "CODPARC":"4454",
                   "CODCONTATO":"2"
                },
                "values":{
                   "3":"comercial@empresa.com.br"
                }
             }
          ]
       }
    }



<b>Retorno:</b><br />

    {
        "serviceName": "DatasetSP.save",
        "status": "1",
        "pendingPrinting": "false",
        "transactionId": "42C865B17822AC52F3F58DFEA7394BE5",
        "responseBody": {
            "total": "2",
            "result": [
                [
                    "1",
                    "S",
                    "NOME DO CONTATO 1",
                    "financeiro@empresa.com.br",
                    "33  999998888"
                ],
                [
                    "2",
                    "S",
                    "NOME DO CONTATO 2",
                    "comercial@empresa.com.br",
                    "33  999998888"
                ]
            ]
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
      "name": "Como incluir/alterar dados?",
      "description": "Realizando a inclusão e alteração de dados"
    }
  ],
  "paths": {
    "/Salve": {
      "post": {
        "tags": [
          "Como incluir/alterar dados?"
        ],
        "summary": "Incluir e Alterar Dados",
        "description": "<h1>Regras de negócio</h1> \nUtilizando a API é possível realizar a inclusão, ou atualização, de dados no SankhyaOm. Para isso, utilizamos o serviço \\\"DatasetSP.save\\\". O mesmo serviço é utilizado para ambos os casos, o que vai indicar se é inclusão ou atualização é o envio da chave primária do registro ou não, ou seja, ao enviar a chave primária indica a necessidade de atualização, e caso a chave primária não seja enviada, a API entende que é necessário fazer a inclusão do registro.<br /><br />\n<h3>Exemplo de uso</h3> <ul>\n  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>\n  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>\n</ul> <b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mge/service.sbr?serviceName=DatasetSP.save&outputType=json<br /><br />\n<b>Vejamos agora a estrutura base da requisição para incluir e atualizar dados via API:</b>\n\n\n    {\n       \"serviceName\":\"DatasetSP.save\",\n       \"requestBody\":{\n          \"entityName\":\"NomeDaEntidade\",\n          \"standAlone\":false,\n          \"fields\":[ \"CAMPO_1\",\n            \"CAMPO_2\",\n            \"CAMPO_N\"\n          ],\n          \"records\":[\n             {\n                \"pk\":{  // deve ser enviado apenas para situação de atualização\n                   \"NOME_PK\":\"VALOR_PK\"\n                },\n                \"values\":{\n                   \"0\": \"VALOR_1\",\n                   \"1\": \"VALOR_2\",\n                   \"2\": \"VALOR_N\"\n                }\n             }\n          ]\n       }\n    }\n\n\n<br /> Esta estrutura é padrão, e permite fazer inclusão, e atualização, em qualquer entidade existente no SankhyaOm. Para isso, basta indicar a Entidade (entityName), os campos (fields) e os respectivos valores (records).<br /> Veremos a seguir 2 exemplos práticos de inclusão e atualização de registros. <br /><br /><br />\n<h2>Como fazer a inclusão de dados?</h2>  Agora que temos a estrutura base da requisição para incluir e atualizar dados via API, vamos apresentar um exemplo de inclusão utilizando registros com PK simples e com PK composta. Veja a seguir a inclusão de um Parceiro e seu contato.<br /><br /> <b>Exemplo para incluir parceiro:</b>\n\n\n    {\n       \"serviceName\":\"DatasetSP.save\",\n       \"requestBody\":{\n          \"entityName\":\"Parceiro\",\n          \"standAlone\":false,\n          \"fields\":[\n             \"CODPARC\",\n             \"NOMEPARC\",\n             \"ATIVO\",\n             \"TIPPESSOA\",\n             \"CODCID\",\n             \"CODREG\",\n             \"CLASSIFICMS\",\n             \"ComplementoParc.SUGTIPNEGENTR\",\n             \"ComplementoParc.SUGTIPNEGSAID\"\n          ],\n          \"records\":[\n             {\n                \"values\":{\n                   \"1\":\"NOME DO PARCEIRO BEM AQUI\",\n                   \"2\":\"S\",\n                   \"3\":\"F\",\n                   \"4\":\"1\",\n                   \"5\":\"0\",\n                   \"6\":\"C\",\n                   \"7\":\"13\",\n                   \"8\":\"13\"\n                }\n             }\n          ]\n       }\n    }\n\n<b>Retorno:</b>\n\n    {\n        \"serviceName\": \"DatasetSP.save\",\n        \"status\": \"1\",\n        \"pendingPrinting\": \"false\",\n        \"transactionId\": \"EAE26797DAF8A192B2FFF990097337A7\",\n        \"responseBody\": {\n            \"total\": \"1\",\n            \"result\": [\n                [\n                    \"4454\",\n                    \"NOME DO PARCEIRO BEM AQUI\",\n                    \"S\",\n                    \"F\",\n                    \"1\",\n                    \"0\",\n                    \"C\",\n                    \"13\",\n                    \"13\"\n                ]\n            ]\n        }\n    }\n\n<br />No retorno, a primeira linha da requisição indica o Código atribuído a este parceiro (neste exemplo 4454).<br /> Agora, vamos fazer a inclusão de múltiplos registros utilizando PK do parceiro como chave de ligação para registros de detalhe. O json a seguir inclui dois contatos para o parceiro na entidade Contato que possui PK composta (CODPARC, CODCONTATO). Segue json para incluir os contatos para o parceiro recém incluído:<br /><br />\n<b>Exemplo para incluir os contatos do parceiro:</b>\n\n    {\n       \"serviceName\":\"DatasetSP.save\",\n       \"requestBody\":{\n          \"entityName\":\"Contato\",\n          \"standAlone\":false,\n          \"fields\":[\n             \"CODCONTATO\",\n             \"ATIVO\",\n             \"NOMECONTATO\",\n             \"EMAIL\",\n             \"CELULAR\"\n          ],\n          \"records\":[\n             {\n                \"foreignKey\":{\n                   \"CODPARC\":\"4454\"\n                },\n                \"values\":{\n                   \"1\":\"S\",\n                   \"2\":\"Nome do Contato 1\",\n                   \"4\":\"33  999998888\"\n                }\n             },\n             {\n                \"foreignKey\":{\n                   \"CODPARC\":\"4454\"\n                },\n                \"values\":{\n                   \"1\":\"S\",\n                   \"2\":\"Nome do Contato 2\",\n                   \"4\":\"33  999998888\"\n                }\n             }\n          ]\n       }\n    }\n\n<b>Retorno:</b><br/>\n\n    {\n        \"serviceName\": \"DatasetSP.save\",\n        \"status\": \"1\",\n        \"pendingPrinting\": \"false\",\n        \"transactionId\": \"A0B2291C8ED35C5DD22E42B36B98BE97\",\n        \"responseBody\": {\n            \"total\": \"2\",\n            \"result\": [\n                [\n                    \"1\",\n                    \"S\",\n                    \"NOME DO CONTATO 1\",\n                    \"\",\n                    \"33  999998888\"\n                ],\n                [\n                    \"2\",\n                    \"S\",\n                    \"NOME DO CONTATO 2\",\n                    \"\",\n                    \"33  999998888\"\n                ]\n            ]\n        }\n    }\n\n\n<br />Dessa forma, com uma requisição conseguimos realizar múltiplas inclusões. Note que incluirmos o contato código 1 e 2 para o parceiro 4454.\\n<br />Vale ressaltar que não é necessário enviar todos os dados (records) indicados na seção de campos (fields). O exemplo acima indica 5 campos, mas envia apenas 3 informações para realizar a inclusão do parceiro.<br /><br />\n<h2>Como fazer alterações em dados?</h2>  Agora que vimos como incluir registros, vamos fazer algumas atualizações nos cadastros incluídos recentemente. Vamos atualizar o nome do parceiro e adicionar e-mails aos contatos que foram vinculados ao parceiro.<br />\nPara realizar uma atualização de cadastro, basta indicar a PK forte do registro desejado. Vejamos a seguir o json para atualizar o cadastro do parceiro 4454:<br />\n\n    {\n       \"serviceName\":\"DatasetSP.save\",\n       \"requestBody\": {\n          \"entityName\":\"Parceiro\",\n          \"standAlone\":false,\n          \"fields\": [\n             \"CODPARC\",\n             \"NOMEPARC\",\n             \"ATIVO\",\n             \"TIPPESSOA\"\n          ],\n          \"records\":[\n             {\n                \"pk\": {\n                   \"CODPARC\":\"4454\"\n                },\n                \"values\": {\n                   \"1\":\"JOSE DA SILVA XAVIER\"\n                }\n             }\n          ]\n       }\n    }\n\n\n\n\n<b>Retorno:</b><br />\n\n    {\n        \"serviceName\": \"DatasetSP.save\",\n        \"status\": \"1\",\n        \"pendingPrinting\": \"false\",\n        \"transactionId\": \"E5526480FF334FF05DC6118028A60AE0\",\n        \"responseBody\": {\n            \"total\": \"1\",\n            \"result\": [\n                [\n                    \"4454\",\n                    \"JOSE DA SILVA XAVIER\",\n                    \"S\",\n                    \"F\"\n                ]\n            ]\n        }\n    }\n\n\n<br />Agora vamos atualizar o cadastro dos dois contatos, adicionando e-mails aos mesmos. Segue json para realizar a requisição:<br />\n\n    {\n       \"serviceName\":\"DatasetSP.save\",\n       \"requestBody\":{\n          \"entityName\":\"Contato\",\n          \"standAlone\":false,\n          \"fields\":[\n             \"CODCONTATO\",\n             \"ATIVO\",\n             \"NOMECONTATO\",\n             \"EMAIL\",\n             \"CELULAR\"\n          ],\n          \"records\":[\n             {\n                \"pk\":{\n                   \"CODPARC\":\"4454\",\n                   \"CODCONTATO\":\"1\"\n                },\n                \"values\":{\n                   \"3\":\"financeiro@empresa.com.br\"\n                }\n             },\n             {\n                \"pk\":{\n                   \"CODPARC\":\"4454\",\n                   \"CODCONTATO\":\"2\"\n                },\n                \"values\":{\n                   \"3\":\"comercial@empresa.com.br\"\n                }\n             }\n          ]\n       }\n    }\n\n\n\n<b>Retorno:</b><br />\n\n    {\n        \"serviceName\": \"DatasetSP.save\",\n        \"status\": \"1\",\n        \"pendingPrinting\": \"false\",\n        \"transactionId\": \"42C865B17822AC52F3F58DFEA7394BE5\",\n        \"responseBody\": {\n            \"total\": \"2\",\n            \"result\": [\n                [\n                    \"1\",\n                    \"S\",\n                    \"NOME DO CONTATO 1\",\n                    \"financeiro@empresa.com.br\",\n                    \"33  999998888\"\n                ],\n                [\n                    \"2\",\n                    \"S\",\n                    \"NOME DO CONTATO 2\",\n                    \"comercial@empresa.com.br\",\n                    \"33  999998888\"\n                ]\n            ]\n        }\n    }\n",
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
