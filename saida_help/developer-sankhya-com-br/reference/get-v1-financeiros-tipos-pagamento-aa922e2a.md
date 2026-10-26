---
id: "https://developer.sankhya.com.br/reference/get_v1-financeiros-tipos-pagamento"
titulo: "Lista de Tipos de Pagamentos"
url: "https://developer.sankhya.com.br/reference/get_v1-financeiros-tipos-pagamento"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Lista de Tipos de Pagamentos

Retorna a lista de Tipos de Pagamento (Tipos de Títulos), com paginação, cadastradas no SankhyaOM.

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
      "name": "Financeiros Cadastros",
      "description": "Breve descrição sobre o respectivo contexto"
    }
  ],
  "paths": {
    "/v1/financeiros/tipos-pagamento": {
      "get": {
        "tags": [
          "Financeiros Cadastros"
        ],
        "summary": "Lista de Tipos de Pagamentos",
        "description": "Retorna a lista de Tipos de Pagamento (Tipos de Títulos), com paginação, cadastradas no SankhyaOM.",
        "parameters": [
          {
            "name": "subTipoPagamento",
            "in": "query",
            "description": "Sub Tipo do Pagamento:\n  - 1  -  A vista\n  - 2  -  A prazo\n  - 3  -  Parcelada\n  - 4  -  Cheque pré-datado\n  - 5  -  Crediário\n  - 6  -  Financeira\n  - 7  -  Cartão de crédito\n  - 8  -  Cartão de débito\n  - 9  -  Voucher\n  - 10 - PIX\n  - 11 - PIX POS\n",
            "required": false,
            "schema": {
              "type": "integer",
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
                10,
                11
              ]
            }
          },
          {
            "name": "page",
            "in": "query",
            "schema": {
              "type": "integer",
              "default": 1
            },
            "description": "Número da página para paginação dos resultados. O valor mínimo é 1. Quando não informado, será considerada a página 1."
          },
          {
            "name": "modifiedSince",
            "in": "query",
            "schema": {
              "type": "string",
              "example": "07/10/2025 10:38"
            },
            "description": "Data e hora da última modificação. Quando este parâmetro é enviado, o serviço retornará apenas os registros que foram modificados a partir da data e hora informadas. Vale ressaltar que este recurso é condicionada a utilização do [Log de Alterações no SankhyaOm](https://developer.sankhya.com.br/reference/get_logalteracoestabelas) no ambiente do cliente. O formato deve ser o seguinte: DD/MM/AAAA HH:MM"
          }
        ],
        "responses": {
          "200": {
            "description": "Lista de Tipos de Pagamentos retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "codigoTipoPagamento": {
                        "type": "integer",
                        "description": "Tipo do Pagamento",
                        "example": 20
                      },
                      "nome": {
                        "type": "string",
                        "description": "Descrição do Pagamento.",
                        "example": "Dinheiro"
                      },
                      "ativo": {
                        "type": "boolean",
                        "description": "Indica que o Tipo de Pagamento está ativo",
                        "example": true
                      },
                      "subTipoPagamento": {
                        "type": "integer",
                        "description": "Sub Tipo do Pagamento:\n- 1 - A vista\n- 2 - A prazo\n- 3 - Parcelada\n- 4 - Cheque pré-datado\n- 5 - Crediário\n- 6 - Financeira\n- 7 - Cartão de crédito\n- 8 - Cartão de débito\n- 9 - Voucher\n- 10 - PIX\n- 11 - PIX POS\n",
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
                          10,
                          11
                        ],
                        "example": 1
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida."
          },
          "401": {
            "description": "Não autorizado."
          },
          "403": {
            "description": "Acesso proibido."
          },
          "404": {
            "description": "Recurso não encontrado."
          },
          "500": {
            "description": "Erro interno do servidor."
          },
          "501": {
            "description": "Não implementado."
          },
          "502": {
            "description": "Erro de gateway."
          },
          "503": {
            "description": "Serviço indisponível."
          },
          "504": {
            "description": "Tempo limite excedido."
          }
        },
        "security": [
          {
            "Bearer": [
              "write:financeiro",
              "read:financeiro"
            ]
          }
        ]
      }
    }
  },
  "components": {
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
