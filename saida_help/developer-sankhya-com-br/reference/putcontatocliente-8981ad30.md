---
id: "https://developer.sankhya.com.br/reference/putcontatocliente"
titulo: "Atualizar contato do cliente"
url: "https://developer.sankhya.com.br/reference/putcontatocliente"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Atualizar contato do cliente

Permite atualizar um contato de um cliente previamente cadastrado


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
      "name": "Clientes",
      "description": "Cadastrar, atualizar e retornar clientes disponíveis no SankhyaOm"
    }
  ],
  "paths": {
    "/v1/parceiros/clientes/{codigoCliente}/contatos/{codigoContato}": {
      "put": {
        "tags": [
          "Clientes"
        ],
        "summary": "Atualizar contato do cliente",
        "description": "Permite atualizar um contato de um cliente previamente cadastrado\n",
        "operationId": "putContatoCliente",
        "parameters": [
          {
            "name": "codigoCliente",
            "in": "path",
            "description": "Informe neste atributo o \"código do cliente\" desejado\n",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int64",
              "example": 4599
            }
          },
          {
            "name": "codigoContato",
            "in": "path",
            "description": "Informe neste atributo o \"código do contato do cliente\" desejado\n",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int64",
              "example": 4
            }
          }
        ],
        "requestBody": {
          "description": "descrever o request...\n",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/contatoPostPut"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Operação bem sucedida. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/codigoContato"
                }
              }
            }
          },
          "400": {
            "description": "Informações Inválidas. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Clientes_e_Estoqueretorno400"
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
                  "$ref": "#/components/schemas/Clientes_e_Estoqueretorno404"
                }
              }
            }
          },
          "409": {
            "description": "Conflito na operação. Geralmente ocorre quando o cadastro já existe. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/codigoContato"
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
              "write:clientes",
              "read:clientes"
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
      "contato": {
        "allOf": [
          {
            "$ref": "#/components/schemas/Clientes_e_Estoqueendereco"
          }
        ],
        "type": "object",
        "properties": {
          "nome": {
            "description": "Informe o nome do contato do parceiro\n",
            "type": "string",
            "example": "Maria Roberta"
          },
          "email": {
            "type": "string",
            "example": "contato@provedor.com.br"
          },
          "telefoneDdd": {
            "type": "string",
            "example": "34"
          },
          "telefoneNumero": {
            "type": "string",
            "example": "912349966"
          }
        }
      },
      "Clientes_e_Estoqueendereco": {
        "type": "object",
        "required": [
          "bairro",
          "cep",
          "cidade",
          "codigoIbge",
          "logradouro",
          "numero",
          "uf"
        ],
        "properties": {
          "logradouro": {
            "type": "string",
            "example": "Rua Maria Roberta"
          },
          "numero": {
            "type": "string",
            "format": "int64",
            "example": 10
          },
          "complemento": {
            "type": "string",
            "example": "Apto 104"
          },
          "bairro": {
            "type": "string",
            "example": "Centro"
          },
          "cidade": {
            "type": "string",
            "example": "Uberlândia"
          },
          "codigoIbge": {
            "type": "string",
            "example": 11155566
          },
          "uf": {
            "type": "string",
            "example": "MG"
          },
          "cep": {
            "type": "string",
            "example": 38400000
          }
        }
      },
      "contatoPostPut": {
        "allOf": [
          {
            "$ref": "#/components/schemas/contato"
          },
          {
            "type": "object",
            "required": [
              "nome"
            ]
          }
        ]
      },
      "codigoCliente": {
        "type": "object",
        "properties": {
          "codigoCliente": {
            "type": "integer",
            "description": "Insira o código do cliente.Esse código é facilmente retornado pelo serviço: GET /v1/parceiros/clientes",
            "example": 8115
          }
        }
      },
      "codigoContato": {
        "type": "object",
        "allOf": [
          {
            "$ref": "#/components/schemas/codigoCliente"
          }
        ],
        "properties": {
          "codigoContato": {
            "type": "integer",
            "description": "Insira o código do contato do respectivo cliente. Esse código é facilmente retornado pelo serviço: GET /v1/parceiros/clientes/{codigoCliente}/contatos",
            "example": 2
          }
        }
      },
      "Clientes_e_Estoqueretorno400": {
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
            "$ref": "#/components/schemas/Clientes_e_EstoqueretornoErro"
          }
        }
      },
      "Clientes_e_Estoqueretorno404": {
        "type": "object",
        "properties": {
          "statusCode": {
            "type": "integer",
            "format": "int32",
            "example": 404
          },
          "error": {
            "$ref": "#/components/schemas/Clientes_e_EstoqueretornoErro"
          }
        }
      },
      "Clientes_e_EstoqueretornoErro": {
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
