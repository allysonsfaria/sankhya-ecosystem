---
id: "https://developer.sankhya.com.br/reference/addabrecaixapdv"
titulo: "Registra a abertura do Caixa/PDV"
url: "https://developer.sankhya.com.br/reference/addabrecaixapdv"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Registra a abertura do Caixa/PDV

Este endpoint permite realizar a abertura de um Caixa/PDV no SankhyaOm. Para que o processo ocorra corretamente, o operador deve estar previamente vinculado ao cadastro do PDV no SankhyaOm. 

É importante observar que o SankhyaOm não permite mais de um "Caixa Aberto" simultaneamente para o mesmo PDV, isso para garantir a integridade da operação.

Ao abrir o Caixa/PDV, a API retornará o identificador codigoCaixa, que representa o "Caixa Aberto" para o período em questão. Esse codigoCaixa deve ser utilizado para realizar o fechamento do caixa e vincular todos os movimentos de venda ao respectivo "Caixa Aberto", garantindo a correta rastreabilidade das operações.

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
      "name": "Vendas Gestão de Caixa",
      "description": "Gestão de Caixa (NFC-e e CF-e/SAT)"
    }
  ],
  "paths": {
    "/v1/caixa/abertura": {
      "post": {
        "tags": [
          "Vendas Gestão de Caixa"
        ],
        "summary": "Registra a abertura do Caixa/PDV",
        "description": "Este endpoint permite realizar a abertura de um Caixa/PDV no SankhyaOm. Para que o processo ocorra corretamente, o operador deve estar previamente vinculado ao cadastro do PDV no SankhyaOm. \n\nÉ importante observar que o SankhyaOm não permite mais de um \"Caixa Aberto\" simultaneamente para o mesmo PDV, isso para garantir a integridade da operação.\n\nAo abrir o Caixa/PDV, a API retornará o identificador codigoCaixa, que representa o \"Caixa Aberto\" para o período em questão. Esse codigoCaixa deve ser utilizado para realizar o fechamento do caixa e vincular todos os movimentos de venda ao respectivo \"Caixa Aberto\", garantindo a correta rastreabilidade das operações.",
        "operationId": "addAbreCaixaPDV",
        "requestBody": {
          "description": "Registra a abertura do Caixa/PDV.",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/abrirCaixa"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Operação bem sucedida",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retornoCaixaAberto"
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
              "write:caixa/abertura",
              "read:caixa/abertura"
            ]
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "abrirCaixa": {
        "type": "object",
        "required": [
          "codigoPdv",
          "cpfOperador",
          "data",
          "hora"
        ],
        "properties": {
          "codigoPdv": {
            "type": "integer",
            "description": "Código do PDV a ser aberto. Esse código é acessível através da nossa API, na entidade \"CadastroPDV\" (codigoPdv). Obtenha essa informação mantenha seus registros sempre atualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 11
          },
          "cpfOperador": {
            "type": "string",
            "description": "Insira o CPF do operador de Caixa/PDV para localizar o Operador do Caixa vinculado ao PDV. Com essa informação, a API identifica o operador responsável no PDV e o vincula ao movimento. Para mais detalhes sobre o cadastro de usuários, [clique aqui](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios)",
            "example": "15975325800"
          },
          "data": {
            "type": "string",
            "description": "Data da abertura do Caixa/PDV",
            "example": "26/10/2024"
          },
          "hora": {
            "type": "string",
            "description": "Hora da abertura do Caixa/PDV",
            "example": "08:54"
          },
          "observacao": {
            "type": "string",
            "example": "Observações referente a abertura do Caixa/PDV"
          }
        }
      },
      "retornoCaixaAberto": {
        "type": "object",
        "properties": {
          "codigoCaixa": {
            "type": "integer",
            "description": "Identificador do Caixa/PDV aberto.",
            "example": 315
          },
          "data": {
            "type": "string",
            "description": "Data da abertura do Caixa/PDV",
            "example": "26/10/2024"
          },
          "hora": {
            "type": "string",
            "description": "Hora da abertura do Caixa/PDV",
            "example": "08:54"
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
