---
id: "https://developer.sankhya.com.br/reference/addfechacaixapdv"
titulo: "Registra o fechamento do Caixa/PDV"
url: "https://developer.sankhya.com.br/reference/addfechacaixapdv"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Registra o fechamento do Caixa/PDV

Este serviço realiza o fechamento do Caixa/PDV que está aberto. Este processo permite enviar os valores transacionados no Caixa/PDV por "Tipo de Pagamento", isso irá apoiar no processo de Gestão de Caixa disponível no SankhyaOm.

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
    "/v1/caixa/fechamento": {
      "post": {
        "tags": [
          "Vendas Gestão de Caixa"
        ],
        "summary": "Registra o fechamento do Caixa/PDV",
        "description": "Este serviço realiza o fechamento do Caixa/PDV que está aberto. Este processo permite enviar os valores transacionados no Caixa/PDV por \"Tipo de Pagamento\", isso irá apoiar no processo de Gestão de Caixa disponível no SankhyaOm.",
        "operationId": "addFechaCaixaPDV",
        "requestBody": {
          "description": "Registra o fechamento do Caixa/PDV.",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/fecharCaixa"
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
              "write:caixa/fechamento",
              "read:caixa/fechamento"
            ]
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "fecharCaixa": {
        "type": "object",
        "required": [
          "codigoCaixa",
          "data",
          "hora"
        ],
        "properties": {
          "codigoCaixa": {
            "type": "integer",
            "description": "Identificador do Caixa/PDV que está aberto. Esta informação é retonrada ao abrir o caixa e pode ser consultada também pelo endpoint caixa/{codigoPdv}/{cpfOperador}",
            "example": 315
          },
          "data": {
            "type": "string",
            "description": "Data do fechamento do Caixa/PDV",
            "example": "26/10/2024"
          },
          "hora": {
            "type": "string",
            "description": "Hora do fechamento do Caixa/PDV",
            "example": "08:54"
          },
          "observacao": {
            "type": "string",
            "example": "Observações referente ao fechamento do Caixa/PDV"
          },
          "conferencia": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/conferenciaCaixa"
            }
          }
        }
      },
      "conferenciaCaixa": {
        "type": "object",
        "properties": {
          "subTipoPagamento": {
            "type": "string",
            "description": "Este atributo identifica o SubTipo de pagamento utilizado em todas as transações realizadas no Caixa/PDV. Cada Tipo de Pagamento (representado pelo atributo \"tipoPagamento\" nos registros financeiros do movimento) possui uma classificação específica denominada SubTipo. Esses dados devem ser enviados para auxiliar nas rotinas de gestão de caixa e controle financeiro.",
            "example": "A vista",
            "enum": [
              "A prazo",
              "A vista",
              "Cartão de crédito",
              "Cartão de débito",
              "Cheque pré-datado",
              "Crediário",
              "Financeira",
              "Parcelada",
              "PIX",
              "PIX POS",
              "Voucher",
              "Sangria",
              "Suprimento"
            ]
          },
          "valor": {
            "type": "number",
            "description": "Valor transacionado durante o período entre abertura e fechamento do caixa, utilizando o respectivo subTipoPagamento.",
            "example": 314.18
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
