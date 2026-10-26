---
id: "https://developer.sankhya.com.br/reference/getprecocontexto"
titulo: "Obter preços de produtos de forma contextualizada"
url: "https://developer.sankhya.com.br/reference/getprecocontexto"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Obter preços de produtos de forma contextualizada

Este serviço retorna os preços dos produtos de forma contextualizada, levando em conta as condições específicas de uma negociação. O preço pode variar com base em diversos fatores, como forma de pagamento, localização do cliente, vendedor responsável pela negociação, entre outros. A consulta permite até 50 produtos por solicitação.

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
      "name": "Preços",
      "description": "Breve descrição sobre o respectivo contexto"
    }
  ],
  "paths": {
    "/v1/precos/contextualizado": {
      "post": {
        "tags": [
          "Preços"
        ],
        "summary": "Obter preços de produtos de forma contextualizada",
        "description": "Este serviço retorna os preços dos produtos de forma contextualizada, levando em conta as condições específicas de uma negociação. O preço pode variar com base em diversos fatores, como forma de pagamento, localização do cliente, vendedor responsável pela negociação, entre outros. A consulta permite até 50 produtos por solicitação.",
        "operationId": "getPrecoContexto",
        "requestBody": {
          "description": "Obter preços de produtos de forma contextualizada",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/produtoPrecosContextoPost"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Operação bem sucedida. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retornoPreco"
                }
              }
            }
          },
          "400": {
            "description": "Informações Inválidas. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno400"
                }
              }
            }
          },
          "401": {
            "description": "Não autenticado. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "403": {
            "description": "Autenticação inválida. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "404": {
            "description": "Dados não encontrados. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno404"
                }
              }
            }
          },
          "500": {
            "description": "Erro interno no servidor. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "501": {
            "description": "Não implementado. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "502": {
            "description": "Retorno inválido do servidor. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "503": {
            "description": "Serviço indisponível no momento. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "504": {
            "description": "Tempo de execução excedido. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
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
              "write:/v1/precos/contextualizado",
              "read:/v1/precos/contextualizado"
            ]
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "retornoMovimento": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "format": "int32"
          },
          "tipo": {
            "type": "string"
          },
          "mensagem": {
            "type": "string"
          }
        }
      },
      "retorno400": {
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
            "$ref": "#/components/schemas/retornoErro"
          }
        }
      },
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
      "retorno404": {
        "type": "object",
        "properties": {
          "statusCode": {
            "type": "integer",
            "format": "int32",
            "example": 404
          },
          "error": {
            "$ref": "#/components/schemas/Requisicao_de_Servicos_TomadosretornoErro"
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
      "retornoErro": {
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
            "example": "O produto [9554] enviado não existe."
          },
          "help": {
            "type": "string",
            "example": "https://api.sankhya.com.br/api/docs/?ERROR_CODE=INVALID_REQUEST"
          }
        }
      },
      "produtoPrecosContextoPost": {
        "type": "object",
        "required": [
          "codigoEmpresa",
          "codigoCliente",
          "codigoVendedor",
          "codigoTipoOperacao",
          "codigoTipoNegociacao",
          "data"
        ],
        "properties": {
          "codigoEmpresa": {
            "type": "integer",
            "description": "Insira o código da Empresa utilizado na negociação. Esse código é facilmente acessível através da nossa API, na entidade \"Empresa\" (CODEMP). Obtenha essa informação e mantenha seus registros sempre atualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 1
          },
          "codigoCliente": {
            "type": "integer",
            "description": "Insira o código do cliente utilizado na negociação. Esse código é facilmente acessível através da nossa API, na entidade \"Parceiro\" (CODPARC). Obtenha essa informação e mantenha seus registros sempre atualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 9541
          },
          "codigoVendedor": {
            "type": "integer",
            "description": "Insira o código do vendedor responsável pela negociação. Esse código é facilmente acessível através da nossa API, na entidade \"Vendedor\" (CODVEND). Obtenha essa informação e mantenha seus registros sempre atualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 11
          },
          "codigoTipoOperacao": {
            "type": "integer",
            "description": "Insira o código do Tipo de Operação utilizado na negociação. Esse código é facilmente acessível através da nossa API, na entidade \"TipoOperacao\" (CODTIPOPER). Obtenha essa informação e mantenha seus registros sempre atualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 1001
          },
          "codigoTipoNegociacao": {
            "type": "integer",
            "description": "Insira o código do Tipo de Negociação utilizado na negociação. Esse código é facilmente acessível através da nossa API, na entidade \"TipoNegociacao\" (CODTIPVENDA). Obtenha essa informação e mantenha seus registros sempre atualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 10
          },
          "dataNegociacao": {
            "type": "string",
            "description": "Data da negociação",
            "example": "16/10/2024"
          },
          "simularInclusao": {
            "type": "boolean",
            "description": "Quando definido como \"true\", este atributo realiza uma simulação da inclusão da negociação, item por item. Trata-se de uma operação com baixa performance e deve ser utilizada apenas quando o cliente possui preços personalizados que diferem do padrão fornecido pelo SankhyaOm.",
            "example": true
          },
          "produtos": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/precosProdutoContextoPost"
            }
          }
        }
      },
      "precosProdutoContextoPost": {
        "allOf": [
          {
            "$ref": "#/components/schemas/produtoPreco"
          },
          {
            "type": "object",
            "required": [
              "codigoProduto",
              "codigoLocalEstoque",
              "controle",
              "unidade",
              "quantidade"
            ],
            "properties": {
              "quantidade": {
                "type": "number",
                "example": 5
              }
            }
          }
        ]
      },
      "produtoModelo": {
        "type": "object",
        "properties": {
          "codigoProduto": {
            "type": "integer",
            "description": "Informe neste atributo o \"código do produto\" disponível no SankhyaOm. Esse código é facilmente acessível através da nossa API, na entidade \"Produto\" (CODPROD). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 9145
          },
          "codigoLocalEstoque": {
            "type": "integer",
            "description": "Código do Local de Estoque para o produto desejado. Quando este atributo é informado, o serviço retornará apenas os preços definidos para o local especificado. Caso não seja enviado, o serviço retornará todos os preços disponíveis para o produto, independentemente do local. Necessário quando existe controle de preços por local de estoque. Essa informação deve ser obtida previamente pela entidade \"Estoque\" (CODLOCAL). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 0
          },
          "controle": {
            "type": "string",
            "description": "Insira neste campo o \"controle\" correspondente. Quando este atributo é informado, o serviço retornará apenas os preços definidos para o controle especificado. Caso não seja enviado, o serviço retornará todos os preços disponíveis para o produto, independentemente do controle. No SankhyaOm, o controle é essencial para a gestão de estoque/preços e pode incluir características como voltagem, sabor, tamanho, cor, entre outros. Por exemplo, para um produto controlado por cor, o valor \"verde\" seria uma informação esperada. Certifique-se de obter esses dados previamente através das entidades \"Produto\" ou \"Estoque\". Veja como funciona controle adicional de estoque em nossa ajuda [clicando aqui](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": "Verde"
          },
          "unidade": {
            "type": "string",
            "description": "Informe neste atributo a \"unidade de medida\" disponível no SankhyaOm. Quando este atributo é informado, o serviço retornará apenas os preços definidos para a unidade especificada. Caso não seja enviado, o serviço retornará todos os preços disponíveis para o produto, independentemente da unidade. Essa informação é facilmente acessível através da nossa API, na entidade \"Produto\" ou \"UnidadeAlternativa\" (CODVOL). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": "UN"
          }
        }
      },
      "produtoPreco": {
        "allOf": [
          {
            "$ref": "#/components/schemas/produtoModelo"
          }
        ],
        "type": "object",
        "required": [
          "codigoProduto"
        ]
      },
      "precosProduto": {
        "allOf": [
          {
            "$ref": "#/components/schemas/produtoPreco"
          },
          {
            "type": "object",
            "required": [
              "valor"
            ],
            "properties": {
              "valor": {
                "type": "number",
                "example": 458.49
              }
            }
          }
        ]
      },
      "retornoPreco": {
        "allOf": [
          {
            "$ref": "#/components/schemas/retornoMovimento"
          },
          {
            "type": "object",
            "properties": {
              "precos": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/precosProduto"
                }
              }
            }
          }
        ]
      },
      "Requisicao_de_Servicos_TomadosretornoErro": {
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
            "example": "O bairro [6] enviado não existe."
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
