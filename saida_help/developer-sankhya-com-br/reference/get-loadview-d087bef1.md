---
id: "https://developer.sankhya.com.br/reference/get_loadview"
titulo: "Consultas com loadView (não tem paginação)"
url: "https://developer.sankhya.com.br/reference/get_loadview"
atualizado_em: "2026-05-13T15:12:48.000Z"
---

# Consultas com loadView (não tem paginação)

A API disponibiliza o serviço loadView (CRUDServiceProvider.loadView) para realizar consulta em VIEWs.<br /> Existem algumas considerações importantes que devem ser levadas em consideração antes de sua utilização. Seguem:  <ul>
  <li>O serviço não possui paginação nativa, portanto, a paginação deve ser feita pelo integrador que realiza a requisição.</li>
  <li>Caso a view não seja performática, é indicado a utilização de mecanismos de indexação para que a performance seja adequada, como Materialized Views (fique atento com as regras de atualização dos dados desse tipo de objeto).</li>
  <li>Para um volume muito grande de dados, pode ser utilizado um indicador de linha para criar a paginação de maneira mais simples. Segue um exemplo para ORACLE e SQL Server:</li>
</ul>
<b>Oracle</b>

    CREATE VIEW VW_ITENS_PEDIDO 
    AS
    SELECT T.* 
    FROM (
        SELECT ROWNUM AS LINHA
        , PRO.CODPROD
        , PRO.DESCRPROD
        , ITE.NUNOTA
        , ITE.SEQUENCIA
        , ITE.QTDNEG
        , ITE.VLRUNIT
        , ITE.VLRTOT
        FROM TGFITE ITE
        INNER JOIN TGFPRO PRO ON PRO.CODPROD = ITE.CODPROD
    ) T

<b>SQL Server</b>

    CREATE VIEW VW_ITENS_PEDIDO 
    AS
    SELECT T.* 
    FROM (
        SELECT ROW_NUMBER() OVER(ORDER BY NUNOTA, SEQUENCIA) AS LINHA
        , PRO.CODPROD
        , PRO.DESCRPROD
        , ITE.NUNOTA
        , ITE.SEQUENCIA
        , ITE.QTDNEG
        , ITE.VLRUNIT
        , ITE.VLRTOT
        FROM TGFITE ITE
        INNER JOIN TGFPRO PRO ON PRO.CODPROD = ITE.CODPROD
    ) T


Nos exemplos acima foi utilizado a TGFITE que detém um grande volume de dados, na maioria das vezes.<br /> Segue exemplo de utilização do serviço com a VIEW criada no exemplo acima:
<h3>Exemplo de uso</h3> <ul>
  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>
  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>
</ul> <b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mge/service.sbr?serviceName=CRUDServiceProvider.loadView&outputType=json
<br /><br /><b>Corpo de requisição</b>

    {
        "serviceName": "CRUDServiceProvider.loadView",
        "requestBody": {
            "query": {
                "viewName": "VW_ITENS_PEDIDO",
                "where": {
                    "$": "LINHA BETWEEN 15000 AND 15499"
                },
                "fields": {
                    "field": {
                        "$": "CODPROD, DESCRPROD, NUNOTA, SEQUENCIA, QTDNEG, VLRUNIT, VLRTOT"
                    }
                }
            }
        }
    }

<br />A requisição acima retorna 500 registros, considerando linhas de 15.000 a 15.499.


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
    "/loadView": {
      "get": {
        "tags": [
          "Como consultar dados?"
        ],
        "summary": "Consultas com loadView (não tem paginação)",
        "description": "A API disponibiliza o serviço loadView (CRUDServiceProvider.loadView) para realizar consulta em VIEWs.<br /> Existem algumas considerações importantes que devem ser levadas em consideração antes de sua utilização. Seguem:  <ul>\n  <li>O serviço não possui paginação nativa, portanto, a paginação deve ser feita pelo integrador que realiza a requisição.</li>\n  <li>Caso a view não seja performática, é indicado a utilização de mecanismos de indexação para que a performance seja adequada, como Materialized Views (fique atento com as regras de atualização dos dados desse tipo de objeto).</li>\n  <li>Para um volume muito grande de dados, pode ser utilizado um indicador de linha para criar a paginação de maneira mais simples. Segue um exemplo para ORACLE e SQL Server:</li>\n</ul>\n<b>Oracle</b>\n\n    CREATE VIEW VW_ITENS_PEDIDO \n    AS\n    SELECT T.* \n    FROM (\n        SELECT ROWNUM AS LINHA\n        , PRO.CODPROD\n        , PRO.DESCRPROD\n        , ITE.NUNOTA\n        , ITE.SEQUENCIA\n        , ITE.QTDNEG\n        , ITE.VLRUNIT\n        , ITE.VLRTOT\n        FROM TGFITE ITE\n        INNER JOIN TGFPRO PRO ON PRO.CODPROD = ITE.CODPROD\n    ) T\n\n<b>SQL Server</b>\n\n    CREATE VIEW VW_ITENS_PEDIDO \n    AS\n    SELECT T.* \n    FROM (\n        SELECT ROW_NUMBER() OVER(ORDER BY NUNOTA, SEQUENCIA) AS LINHA\n        , PRO.CODPROD\n        , PRO.DESCRPROD\n        , ITE.NUNOTA\n        , ITE.SEQUENCIA\n        , ITE.QTDNEG\n        , ITE.VLRUNIT\n        , ITE.VLRTOT\n        FROM TGFITE ITE\n        INNER JOIN TGFPRO PRO ON PRO.CODPROD = ITE.CODPROD\n    ) T\n\n\nNos exemplos acima foi utilizado a TGFITE que detém um grande volume de dados, na maioria das vezes.<br /> Segue exemplo de utilização do serviço com a VIEW criada no exemplo acima:\n<h3>Exemplo de uso</h3> <ul>\n  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>\n  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>\n</ul> <b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mge/service.sbr?serviceName=CRUDServiceProvider.loadView&outputType=json\n<br /><br /><b>Corpo de requisição</b>\n\n    {\n        \"serviceName\": \"CRUDServiceProvider.loadView\",\n        \"requestBody\": {\n            \"query\": {\n                \"viewName\": \"VW_ITENS_PEDIDO\",\n                \"where\": {\n                    \"$\": \"LINHA BETWEEN 15000 AND 15499\"\n                },\n                \"fields\": {\n                    \"field\": {\n                        \"$\": \"CODPROD, DESCRPROD, NUNOTA, SEQUENCIA, QTDNEG, VLRUNIT, VLRTOT\"\n                    }\n                }\n            }\n        }\n    }\n\n<br />A requisição acima retorna 500 registros, considerando linhas de 15.000 a 15.499.\n",
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
