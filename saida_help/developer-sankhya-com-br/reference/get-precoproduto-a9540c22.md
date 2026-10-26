---
id: "https://developer.sankhya.com.br/reference/get_precoproduto"
titulo: "Consulta de Preços"
url: "https://developer.sankhya.com.br/reference/get_precoproduto"
atualizado_em: "2026-05-13T15:12:48.000Z"
---

# Consulta de Preços

<h1>Regras de negócio</h1> 
Para realizar consulta “Tabela de Preço” no carregamento das regras/exceções da tabela de preço, o sistema irá trazer os registros de forma paginada, ou seja, os dados não irão ser carregados todos de uma vez só. O sistema irá trazer aos poucos os registros, para que você possa ir utilizando a tela enquanto as informações não são totalmente carregadas.<br />
Além disso, é possível que seja editado um registro (somente no modo formulário) enquanto os demais registros são carregados na tela. Quando estiver sendo feita a edição de um registro e o carregamento de todos os registros for concluído, o sistema irá emitir uma mensagem para  confirmação da edição.<br />
<b>OBS:</b> Caso tenha alguma necessidade de configuração do ERP procure “Consultor” ou acesso o link de apoio:<br /> https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os<br />
<h3>Dependências</h3> <b><font color=red>Não possui dependências</font></b><br /><br />
<h3>Detalhes Técnicos</h3> No endpoint ConsultaProdutosSP.consultaProdutos, não é possível informar os parâmetros codtab ou nutab, pois o serviço retorna exclusivamente os preços previamente configurados na própria consulta de produtos, desconsiderando quaisquer códigos de tabela informados na requisição.
        
<h3>Exemplo de uso:</h3> <ul>
  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>
  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>
</ul> <b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mgecom/service.sbr?serviceName=ConsultaProdutosSP.consultaProdutos&outputType=json <br />
<b>Corpo de requisição</b>

    {
        "serviceName": "ConsultaProdutosSP.consultaProdutos",
          "requestBody": {
              "filtros": {
                  "criterio": {
                      "resourceID": "br.com.sankhya.com.cons.consultaProdutos",
                      "PERCDESC": "0",
                      "CODPROD": {
                          "$": "6"
                      }
                  },
                  "isPromocao": {
                      "$": "false"
                  },
                  "isLiquidacao": {
                      "$": "false"
            }
          }
        }
      }
    }

<b>Retorno:</b><br />

    {
        "serviceName": "ConsultaProdutosSP.consultaProdutos",
          "status": "1",
          "pendingPrinting": "false",
          "transactionId": "DA7090050593CA45FA74E760480BAA0B",
          "responseBody": {
              "produtos": {
                  "maxregconsprod": {
                      "$": "0"
                  },
                  "produto": {
                      "ISPROMOCAO": "false",
                      "ISLIQUIDACAO": "false",
                      "Cadastro_COMPLDESC": {},
                      "Cadastro_CODPROD": {
                          "$": "6"
                      },
                      "Cadastro_DESCRPROD": {
                          "$": "AR CONDICIONADO YORK 18.000 BTU'S"
                      },
                      "TIPCONTEST": {
                          "$": "N"
                      },
                      "TIPLANCNOTA": {
                          "$": "A"
                      },
                      "Preço_1": {
                          "$": "0.00",
                          "PRECOBASE_Preço_1": "0"
                      },
                      "DECQTD": {
                          "$": "0"
                      },
                      "ORDEMMEDIDA": {
                          "$": "0"
                      },
                      "Estoque_1": {},
                      "DECVLR": {
                          "$": "2"
                      },
                      "CODVOL": {
                          "$": "UN"
                      },
                      "DESCRPROD": {
                          "$": "AR CONDICIONADO YORK 18.000 BTU'S"
                      },
                      "CODPROD": {
                          "$": "6"
                      },
                      "TEMIMAGEM": {
                          "$": "N"
                      },
                      "PRECOBASE": {
                          "$": "0.00"
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
      "name": "Serviços Especialistas",
      "description": "Serviços especialistas disponiveis no SankhyaOm"
    }
  ],
  "paths": {
    "/PrecoProduto": {
      "get": {
        "tags": [
          "Serviços Especialistas"
        ],
        "summary": "Consulta de Preços",
        "description": "<h1>Regras de negócio</h1> \nPara realizar consulta “Tabela de Preço” no carregamento das regras/exceções da tabela de preço, o sistema irá trazer os registros de forma paginada, ou seja, os dados não irão ser carregados todos de uma vez só. O sistema irá trazer aos poucos os registros, para que você possa ir utilizando a tela enquanto as informações não são totalmente carregadas.<br />\nAlém disso, é possível que seja editado um registro (somente no modo formulário) enquanto os demais registros são carregados na tela. Quando estiver sendo feita a edição de um registro e o carregamento de todos os registros for concluído, o sistema irá emitir uma mensagem para  confirmação da edição.<br />\n<b>OBS:</b> Caso tenha alguma necessidade de configuração do ERP procure “Consultor” ou acesso o link de apoio:<br /> https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os<br />\n<h3>Dependências</h3> <b><font color=red>Não possui dependências</font></b><br /><br />\n<h3>Detalhes Técnicos</h3> No endpoint ConsultaProdutosSP.consultaProdutos, não é possível informar os parâmetros codtab ou nutab, pois o serviço retorna exclusivamente os preços previamente configurados na própria consulta de produtos, desconsiderando quaisquer códigos de tabela informados na requisição.\n        \n<h3>Exemplo de uso:</h3> <ul>\n  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>\n  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>\n</ul> <b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mgecom/service.sbr?serviceName=ConsultaProdutosSP.consultaProdutos&outputType=json <br />\n<b>Corpo de requisição</b>\n\n    {\n        \"serviceName\": \"ConsultaProdutosSP.consultaProdutos\",\n          \"requestBody\": {\n              \"filtros\": {\n                  \"criterio\": {\n                      \"resourceID\": \"br.com.sankhya.com.cons.consultaProdutos\",\n                      \"PERCDESC\": \"0\",\n                      \"CODPROD\": {\n                          \"$\": \"6\"\n                      }\n                  },\n                  \"isPromocao\": {\n                      \"$\": \"false\"\n                  },\n                  \"isLiquidacao\": {\n                      \"$\": \"false\"\n            }\n          }\n        }\n      }\n    }\n\n<b>Retorno:</b><br />\n\n    {\n        \"serviceName\": \"ConsultaProdutosSP.consultaProdutos\",\n          \"status\": \"1\",\n          \"pendingPrinting\": \"false\",\n          \"transactionId\": \"DA7090050593CA45FA74E760480BAA0B\",\n          \"responseBody\": {\n              \"produtos\": {\n                  \"maxregconsprod\": {\n                      \"$\": \"0\"\n                  },\n                  \"produto\": {\n                      \"ISPROMOCAO\": \"false\",\n                      \"ISLIQUIDACAO\": \"false\",\n                      \"Cadastro_COMPLDESC\": {},\n                      \"Cadastro_CODPROD\": {\n                          \"$\": \"6\"\n                      },\n                      \"Cadastro_DESCRPROD\": {\n                          \"$\": \"AR CONDICIONADO YORK 18.000 BTU'S\"\n                      },\n                      \"TIPCONTEST\": {\n                          \"$\": \"N\"\n                      },\n                      \"TIPLANCNOTA\": {\n                          \"$\": \"A\"\n                      },\n                      \"Preço_1\": {\n                          \"$\": \"0.00\",\n                          \"PRECOBASE_Preço_1\": \"0\"\n                      },\n                      \"DECQTD\": {\n                          \"$\": \"0\"\n                      },\n                      \"ORDEMMEDIDA\": {\n                          \"$\": \"0\"\n                      },\n                      \"Estoque_1\": {},\n                      \"DECVLR\": {\n                          \"$\": \"2\"\n                      },\n                      \"CODVOL\": {\n                          \"$\": \"UN\"\n                      },\n                      \"DESCRPROD\": {\n                          \"$\": \"AR CONDICIONADO YORK 18.000 BTU'S\"\n                      },\n                      \"CODPROD\": {\n                          \"$\": \"6\"\n                      },\n                      \"TEMIMAGEM\": {\n                          \"$\": \"N\"\n                      },\n                      \"PRECOBASE\": {\n                          \"$\": \"0.00\"\n                    }\n                }\n            }\n        }\n    }\n",
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
