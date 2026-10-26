---
id: "https://developer.sankhya.com.br/reference/addrecebimentocaixapdvbaixa"
titulo: "Registra recebimento para um Caixa/PDV"
url: "https://developer.sankhya.com.br/reference/addrecebimentocaixapdvbaixa"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Registra recebimento para um Caixa/PDV

Registra recebimento para um Caixa/PDV.

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
    "/v1/caixa/recebimento/baixa": {
      "post": {
        "tags": [
          "Vendas Gestão de Caixa"
        ],
        "summary": "Registra recebimento para um Caixa/PDV",
        "description": "Registra recebimento para um Caixa/PDV.",
        "operationId": "addRecebimentoCaixaPDVbaixa",
        "requestBody": {
          "description": "Inclui um recebimento realizado em um Caixa/PDV no SankhyaOm",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/recebimentoBaixar"
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
                  "$ref": "#/components/schemas/retornoMovimento"
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
              "write:caixa/recebimento",
              "read:caixa/recebimento"
            ]
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "recebimentoModelo": {
        "type": "object",
        "properties": {
          "codigoCaixa": {
            "type": "integer",
            "description": "Identificador do Caixa/PDV que está aberto. Esta informação é retonrada ao abrir o caixa e pode ser consultada também pelo endpoint caixa/{codigoPdv}/{cpfOperador}",
            "example": 348
          },
          "dataBaixa": {
            "type": "string",
            "description": "Data da baixa do recebimento",
            "example": "26/10/2024"
          },
          "valorBaixa": {
            "type": "number",
            "description": "Valor da baixa do recebimento",
            "example": 3.4
          },
          "valorJuro": {
            "type": "number",
            "description": "Valor de juros do recebimento",
            "example": 0.02
          },
          "valorMulta": {
            "type": "number",
            "description": "Valor de multa do recebimento",
            "example": 0
          },
          "valorDesconto": {
            "type": "number",
            "description": "Valor de desconto do recebimento",
            "example": 0
          },
          "identificador": {
            "type": "string",
            "description": "Número identificador do recebívelf, pode ser o código de barras, nosso número, ou algum outra informação que seja capaz de identificar o finaceiro recebido.",
            "example": 1025469845
          },
          "observacao": {
            "type": "string",
            "example": "Observações para o recebimento"
          }
        }
      },
      "recebimentoBaixar": {
        "description": "Contrato para baixa de recebíveis que existem no SankhyaOm e que ocorreram no Caixa/PDV.",
        "allOf": [
          {
            "$ref": "#/components/schemas/recebimentoModelo"
          }
        ],
        "type": "object",
        "required": [
          "dataBaixa",
          "valorBaixa",
          "codigoFinanceiro",
          "codigoCaixa"
        ],
        "properties": {
          "codigoFinanceiro": {
            "type": "integer",
            "description": "Insira o código do Financeiro para realizar baixa. Esse código é facilmente acessível através da nossa API, na entidade \"Financeiro\" (NUFIN). Obtenha essa informação e mantenha seus registros sempre atualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 8115
          }
        }
      },
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
