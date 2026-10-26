---
id: "https://developer.sankhya.com.br/reference/get_v1-financeiros-tipos-pagamento-codigotipopagamento"
titulo: "Tipo de Pagamento específico"
url: "https://developer.sankhya.com.br/reference/get_v1-financeiros-tipos-pagamento-codigotipopagamento"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Tipo de Pagamento específico

Retorna um Tipo de Pagamento específico com base no parâmetro enviado na requisição.

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
    "/v1/financeiros/tipos-pagamento/{codigoTipoPagamento}": {
      "get": {
        "tags": [
          "Financeiros Cadastros"
        ],
        "summary": "Tipo de Pagamento específico",
        "description": "Retorna um Tipo de Pagamento específico com base no parâmetro enviado na requisição.",
        "parameters": [
          {
            "name": "codigoTipoPagamento",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código do Tipo de Pagamento para retorno"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados do Tipo de Pagamento retornados com sucesso.",
            "content": {
              "application/json": {
                "schema": {
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
