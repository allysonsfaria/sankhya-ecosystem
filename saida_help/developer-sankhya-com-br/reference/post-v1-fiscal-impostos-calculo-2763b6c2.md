---
id: "https://developer.sankhya.com.br/reference/post_v1-fiscal-impostos-calculo"
titulo: "Calcular Impostos em Vendas"
url: "https://developer.sankhya.com.br/reference/post_v1-fiscal-impostos-calculo"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Calcular Impostos em Vendas

Este endpoint calcula os impostos incidentes sobre uma operação de venda. Com base nos dados fornecidos, como empresa, cliente, produtos e despesas acessórias, a API retorna os valores calculados, incluindo base de cálculo, alíquotas e valores de impostos.

É importante ressaltar que toda a parametrização tributária deve ser previamente configurada no SankhyaOm, pois o endpoint não realiza essa configuração, apenas aplica as regras já definidas no SankhyaOm.

 Serviço está disponível no SankhyaOm a partir da versão 4.31.

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "API Sankhya",
    "description": "API de Integrações com Gateway Sankhya.\n\nOs endpoints aqui documentados estão todos baseados no EasyAPI, seguindo padrão Rest e documentação padrão OpenAPI/Swagger.\n\nPara utilizar todos os serviços, é necessário realizar o login conforme descrito na documentação.\n",
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
  "security": [
    {
      "Bearer": []
    }
  ],
  "tags": [
    {
      "name": "Fiscal",
      "description": "Breve descrição sobre o respectivo contexto"
    }
  ],
  "paths": {
    "/v1/fiscal/impostos/calculo": {
      "post": {
        "tags": [
          "Fiscal"
        ],
        "summary": "Calcular Impostos em Vendas",
        "description": "Este endpoint calcula os impostos incidentes sobre uma operação de venda. Com base nos dados fornecidos, como empresa, cliente, produtos e despesas acessórias, a API retorna os valores calculados, incluindo base de cálculo, alíquotas e valores de impostos.\n\nÉ importante ressaltar que toda a parametrização tributária deve ser previamente configurada no SankhyaOm, pois o endpoint não realiza essa configuração, apenas aplica as regras já definidas no SankhyaOm.\n\n Serviço está disponível no SankhyaOm a partir da versão 4.31.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/NegociacaoRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Impostos calculados com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NegociacaoResponse"
                }
              }
            }
          },
          "400": {
            "description": "Informações Inválidas. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Calculo_Impostosretorno400"
                }
              }
            }
          },
          "401": {
            "description": "Não autenticado. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "403": {
            "description": "Autenticação inválida. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "404": {
            "description": "Dados não encontrados. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Calculo_Impostosretorno404"
                }
              }
            }
          },
          "500": {
            "description": "Erro interno no servidor. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "501": {
            "description": "Não implementado. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "502": {
            "description": "Retorno inválido do servidor. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "503": {
            "description": "Serviço indisponível no momento. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "504": {
            "description": "Tempo de execução excedido. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          }
        },
        "security": [
          {
            "Bearer": [
              "write:impostos",
              "read:impostos"
            ]
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "retorno40X_50X": {
        "type": "object",
        "properties": {
          "fieldSet": {
            "type": "string"
          },
          "paginate": {
            "type": "string"
          },
          "mensagem": {
            "$ref": "#/components/schemas/error"
          }
        }
      },
      "error": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "string"
          },
          "descricao": {
            "type": "string"
          }
        }
      },
      "NegociacaoRequest": {
        "type": "object",
        "properties": {
          "notaModelo": {
            "type": "integer",
            "description": "Este atributo é utilizado para preparar a inclusão do movimento no SankhyaOm, permitindo que o serviço obtenha informações essenciais, como empresa, tipo de operação, natureza, entre outros. Para saber mais como configurar um Modelo de Nota, [clique aqui](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047012513-Config-Modelo-de-Notas)\n",
            "example": 123
          },
          "codigoCliente": {
            "type": "integer",
            "description": "Para realizar o cálculo de impostos, informe neste atributo o \"código do cliente\" disponível no SankhyaOm. Esse código é facilmente acessível através da nossa API, na entidade \"Parceiro\" (CODPARC). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)\n",
            "example": 54321
          },
          "codigoEmpresa": {
            "type": "integer",
            "description": "Este atributo é opcional e caso não seja enviado, a API irá assumir a empresa configurada na Nota Modelo. Para mudar a empresa contida na Nota Modelo, informe neste atributo o \"código da empresa\" disponível no SankhyaOm. Esse código é facilmente acessível através da nossa API, na entidade \"Empresa\" (CODEMP). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 45
          },
          "codigoTipoOperacao": {
            "type": "integer",
            "description": "Este atributo é opcional e caso não seja enviado, a API irá assumir o Tipo de Operação configurada na Nota Modelo. Para utilizar um Tipo de Operação diferente do que está configurado na Nota Modelo, informe neste atributo o \"código do tipo de operação\" disponível no SankhyaOm. Esse código é facilmente acessível através da nossa API, na entidade \"TipoOperacao\" (CODTIPOPER). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)\n",
            "example": 45
          },
          "finalidadeOperacao": {
            "type": "integer",
            "description": "Informe neste atributo a \"finalidade da operação\" disponível no SankhyaOm. Esse código é facilmente acessível através da nossa API, na entidade \"FinalidadeOperacao\" (NUFOP). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)\n",
            "example": 2
          },
          "despesasAcessorias": {
            "$ref": "#/components/schemas/DespesasAcessorias"
          },
          "produtos": {
            "type": "array",
            "description": "Lista de produtos para realizar o cálculo de impostos",
            "items": {
              "$ref": "#/components/schemas/Produto"
            }
          }
        },
        "required": [
          "notaModelo",
          "codigoCliente",
          "produtos"
        ]
      },
      "DespesasAcessorias": {
        "type": "object",
        "description": "Despesas adicionais relacionadas à negociação, como frete, seguro e outras despesas.\nA API não irá tratar de forma separada valores de destaque, juros e embalagem de forma separada, com isso, estas despesas serão  enquadradas como \"outros\" e receberão a tratativa de \"destaque\".\n",
        "properties": {
          "frete": {
            "type": "number",
            "format": "double",
            "description": "Valor do frete associado à negociação.\n",
            "example": 100
          },
          "seguro": {
            "type": "number",
            "format": "double",
            "description": "Valor do seguro aplicado à negociação.\n",
            "example": 50
          },
          "outras": {
            "type": "number",
            "format": "double",
            "description": "Outras despesas acessórias da negociação (ex.: embalagem, juros, destaque, etc.).\n",
            "example": 30
          }
        }
      },
      "Produto": {
        "type": "object",
        "properties": {
          "codigoProduto": {
            "type": "integer",
            "description": "Para registrar os produtos utilizados da negociação, informe neste atributo o \"código do produto\" disponível no SankhyaOm. Esse código é facilmente acessível através da nossa API, na entidade \"Produto\" (CODPROD). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)\n",
            "example": 1
          },
          "unidade": {
            "type": "string",
            "description": "Unidade de medida utilizada na negociação do produto\n",
            "example": "UN"
          },
          "quantidade": {
            "type": "integer",
            "description": "Quantidade negociada do produto\n",
            "example": 10
          },
          "valorUnitario": {
            "type": "number",
            "format": "double",
            "description": "Preço unitário do produto\n",
            "example": 50
          },
          "valorDesconto": {
            "type": "number",
            "format": "double",
            "description": "Valor de desconto aplicado no produto\n",
            "example": 0
          }
        },
        "required": [
          "codigoProduto",
          "unidade",
          "quantidade",
          "valorUnitario"
        ]
      },
      "NegociacaoResponse": {
        "type": "object",
        "properties": {
          "produtos": {
            "type": "array",
            "description": "Lista de produtos com os respectivos impostos calculados.\n",
            "items": {
              "$ref": "#/components/schemas/ProdutoImposto"
            }
          }
        }
      },
      "ProdutoImposto": {
        "type": "object",
        "properties": {
          "codigoProduto": {
            "type": "integer",
            "description": "Para registrar os produtos utilizados da negociação, informe neste atributo o \"código do produto\" disponível no SankhyaOm. Esse código é facilmente acessível através da nossa API, na entidade \"Produto\" (CODPROD). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)\n",
            "example": 1
          },
          "origemProduto": {
            "type": "integer",
            "description": "Origem do Produto. Os valores retornados aqui são com base no manual da Nota Fiscal Eletrônica (anexo I).\n\nSeguem valores aceitos:\n  - 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8; \n  - 1 - Estrangeira - Importação direta, exceto a indicada no código 6;\n  - 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7;\n  - 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%;\n  - 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes;\n  - 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%;\n  - 6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX e gás natural;\n  - 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante lista CAMEX e gás natural.\n  - 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%;\n",
            "enum": [
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8
            ],
            "example": 1
          },
          "unidade": {
            "type": "string",
            "description": "Unidade de medida utilizada na negociação do produto.\n",
            "example": "UN"
          },
          "quantidade": {
            "type": "integer",
            "description": "Quantidade negociada do produto\n",
            "example": 10
          },
          "valorUnitario": {
            "type": "number",
            "format": "double",
            "description": "Preço unitário do produto\n",
            "example": 50
          },
          "valorDesconto": {
            "type": "number",
            "format": "double",
            "description": "Valor de desconto aplicado no produto\n",
            "example": 0
          },
          "valorTotal": {
            "type": "number",
            "format": "double",
            "description": "Valor total do produto considerando a quantidade negociada\n",
            "example": 500
          },
          "despesasAcessorias": {
            "type": "number",
            "format": "double",
            "description": "Despesas acessórias alocadas para o produto específico\n",
            "example": 50
          },
          "impostos": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Calculo_ImpostosImpostos"
            }
          }
        }
      },
      "Calculo_ImpostosImpostos": {
        "type": "object",
        "description": "Detalhamento dos impostos calculados para o produto\n",
        "properties": {
          "tipo": {
            "type": "string",
            "description": "Tipo do imposto. Os valores previstos neste atributo são:\n  - icms\n  - st\n  - ipi\n  - irpj\n  - cpp\n  - iss\n  - inss\n  - pis\n  - cofins\n  - irf\n  - cssl\n  - ibsuf\n  - ibsmun\n  - cbs\n  - is\n  - ibsmono\n  - cbsmono\n  - outros\n",
            "enum": [
              "icms",
              "st",
              "ipi",
              "irpj",
              "cpp",
              "iss",
              "inss",
              "pis",
              "cofins",
              "irf",
              "cssl",
              "ibsuf",
              "ibsmun",
              "cbs",
              "is",
              "ibsmono",
              "cbsmono",
              "outros"
            ],
            "example": "st"
          },
          "cst": {
            "type": "string",
            "description": "Código de Situação Tributária. Os valores retornados aqui são com base no manual da Nota Fiscal Eletrônica (anexo I).\n",
            "example": "00"
          },
          "modalidadeBaseCalculo": {
            "type": "integer",
            "description": "Código da Modalidade de Base de Cálculo. Os valores retornados aqui são com base no manual da Nota Fiscal Eletrônica (anexo I).\n\nValores previstos para ICMS:\n  - 0 - Margem Valor Agregado (%)\n  - 1 - Pauta (Valor)\n  - 2 - Preço Tabelado Máx. (valor)\n  - 3 - Valor da operação\n\n  \nValores previstos para ST:\n  - 0 - Preço tabelado ou máximo sugerido\n  - 1 - Lista Negativa (valor)\n  - 2 - Lista Positiva (valor)\n  - 3 - Lista Neutra (valor)\n  - 4 - Margem Valor Agregado (%)\n  - 5 - Pauta (valor)\n",
            "enum": [
              0,
              1,
              2,
              3,
              4,
              5
            ],
            "example": 1
          },
          "valorOperacao": {
            "type": "number",
            "format": "double",
            "description": "Valor envaido na requisição para realizar o cálculo.\n",
            "example": 150
          },
          "aliquota": {
            "type": "number",
            "format": "double",
            "description": "Aliquota do imposto\n",
            "example": 18
          },
          "valorBase": {
            "type": "number",
            "format": "double",
            "description": "Valor da base de cálculo com reduções caso existam\n",
            "example": 145
          },
          "valorImposto": {
            "type": "number",
            "format": "double",
            "description": "Valor do imposto calculado",
            "example": 26.1
          },
          "percentualFCP": {
            "type": "number",
            "format": "double",
            "description": "Percentual do Fundo de Combate a Pobreza (FCP).\n",
            "example": 0
          },
          "valorFCP": {
            "type": "number",
            "format": "double",
            "description": "Valor do Fundo de Combate a Pobreza (FCP).\n",
            "example": 0
          },
          "valorDesoneracao": {
            "type": "number",
            "format": "double",
            "description": "Valor do imposto calculado",
            "example": 3.31
          },
          "motivoDesoneracao": {
            "type": "integer",
            "description": "Lista de motivos da desoneração de impostos para ICMS e ST. Segue relação de valores para ICMS:\n  - 1 - Táxi\n  - 2 - Deficiente Físico\n  - 3 - Produtor Agropecuário\n  - 4 - Frotista/Locadora\n  - 5 - Diplomático/Consular\n  - 6 - Utilitários e Motocicletas da Amazônia Ocidental e Áreas de Livre Comércio\n  - 7 - SUFRAMA\n  - 8 - Venda a Órgãos Públicos\n  - 9 - Outros\n  - 16 - Olimpíadas Rio 2016\n  - 90 - Solicitado pelo Fisco\n  \nSegue relação de valores exclusivos para ST:\n  - 9 - Outros\n  - 3 - Uso na agropecuária\n  - 12 - Fomento agropecuário\n",
            "enum": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              12,
              16,
              90
            ],
            "example": 4
          },
          "indicadorRepasseDesoneracao": {
            "type": "integer",
            "description": "Indica se o valor do ICMS desonerado deduz do valor do item. Seguem valores aceitos:\n  - 0 - Valor do ICMS desonerado não deduz do valor do item  / total da NF-e\n  - 1 - Valor do ICMS desonerado deduz do valor do item / total da NF-e\n",
            "enum": [
              0,
              1
            ],
            "example": 1
          }
        }
      },
      "Calculo_Impostosretorno400": {
        "type": "object",
        "properties": {
          "statusCode": {
            "type": "integer",
            "format": "int32",
            "example": 400
          },
          "error": {
            "type": "string"
          },
          "mensagem": {
            "$ref": "#/components/schemas/Calculo_ImpostosretornoErro"
          }
        }
      },
      "Calculo_Impostosretorno404": {
        "type": "object",
        "properties": {
          "statusCode": {
            "type": "integer",
            "format": "int32",
            "example": 404
          },
          "error": {
            "$ref": "#/components/schemas/Calculo_ImpostosretornoErro"
          }
        }
      },
      "Calculo_ImpostosretornoErro": {
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "example": "INVALID_REQUEST"
          },
          "message": {
            "type": "string",
            "example": "Ocorreu algum erro inesperado!"
          },
          "details": {
            "type": "string",
            "example": "O produto [6] enviado não existe."
          },
          "help": {
            "type": "string",
            "example": "https://api.sankhya.com.br/api/docs/?ERROR_CODE=INVALID_REQUEST"
          }
        }
      }
    },
    "securitySchemes": {
      "Bearer": {
        "type": "apiKey",
        "name": "Authorization",
        "in": "header",
        "description": "Insira o token com o prefixo 'Bearer: ' ex. \"Bearer abcde12345\"."
      }
    }
  }
}
```
