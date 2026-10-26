---
id: "https://developer.sankhya.com.br/reference/getprecoproduto"
titulo: "Obter preços vinculados a um produto independente da tabela de preço"
url: "https://developer.sankhya.com.br/reference/getprecoproduto"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Obter preços vinculados a um produto independente da tabela de preço

Este serviço retorna os preços do produto enviado no contexto, bem como as tabelas de preços nele relacionado. Vale ressaltar que cada produto x tabela de preços pode possuir mais de um preço, pois o produto pode ter volume alternativo, variação de preço por local de armazenamento e também preço variado por controle (ex.: sabor, cor, tamanho, etc.). Este serviço retorna até 50 registros por página.

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
    "/v1/precos/produto/{codigoProduto}": {
      "get": {
        "tags": [
          "Preços"
        ],
        "summary": "Obter preços vinculados a um produto independente da tabela de preço",
        "description": "Este serviço retorna os preços do produto enviado no contexto, bem como as tabelas de preços nele relacionado. Vale ressaltar que cada produto x tabela de preços pode possuir mais de um preço, pois o produto pode ter volume alternativo, variação de preço por local de armazenamento e também preço variado por controle (ex.: sabor, cor, tamanho, etc.). Este serviço retorna até 50 registros por página.",
        "operationId": "getPrecoProduto",
        "parameters": [
          {
            "name": "codigoProduto",
            "in": "path",
            "description": "Informe neste atributo o \"código do produto\" disponível no SankhyaOm. Esse código é facilmente acessível através da nossa API, na entidade \"Produto\" (CODPROD). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int64",
              "example": 4599
            }
          },
          {
            "name": "pagina",
            "in": "query",
            "description": "Número da página para consulta. Cada página retorna até 50 registros. O valor mínimo requerido é 1 e caso exista mais registros o atributo \"temMaisRegistros\" estará com valor igual à \"true\" e o número da pagina poderá ser incrementado para exibir os demais registros.",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int64",
              "example": 1
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Operação bem sucedida. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retornoPrecosProdutoTabela"
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
              "write:/v1/precos/produto",
              "read:/v1/precos/produto"
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
      "precosProdutoTabela": {
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
              "codigoTabela": {
                "description": "Informe neste atributo o \"código da tabela de preços\" disponível no SankhyaOm. Esse código é facilmente acessível através da nossa API, na entidade \"TabelaPreco\" (CODTAB). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
                "type": "number",
                "example": 10
              },
              "valor": {
                "type": "number",
                "example": 458.49
              }
            }
          }
        ]
      },
      "paginacao": {
        "type": "object",
        "properties": {
          "page": {
            "type": "integer",
            "format": "int32",
            "example": 2
          },
          "numeroRegistros": {
            "type": "integer",
            "format": "int32",
            "example": 50
          },
          "temMaisRegistros": {
            "type": "boolean",
            "example": true
          }
        }
      },
      "retornoPrecosProdutoTabela": {
        "allOf": [
          {
            "$ref": "#/components/schemas/retornoMovimento"
          },
          {
            "$ref": "#/components/schemas/paginacao"
          },
          {
            "type": "object",
            "properties": {
              "precos": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/precosProdutoTabela"
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
