---
id: "https://developer.sankhya.com.br/reference/get_v1-tipos-operacao"
titulo: "Lista de Tipos de Operação"
url: "https://developer.sankhya.com.br/reference/get_v1-tipos-operacao"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Lista de Tipos de Operação

Retorna a lista de Tipos de Operação, com paginação, cadastradas no SankhyaOM.


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
      "name": "Cadastros Básicos",
      "description": "Cadastros Básicos disponíveis no SankhyaOM"
    }
  ],
  "paths": {
    "/v1/tipos-operacao": {
      "get": {
        "tags": [
          "Cadastros Básicos"
        ],
        "summary": "Lista de Tipos de Operação",
        "description": "Retorna a lista de Tipos de Operação, com paginação, cadastradas no SankhyaOM.\n",
        "parameters": [
          {
            "name": "tipoMovimento",
            "in": "query",
            "description": "Tipo de Movimento:\n  -  1: NF Depósito\n  -  2: Pedido de Devolução\n  -  3: Saídas\n  -  4: Faturamento\n  -  5: Pedido de Armazenagem\n  -  6: Movimento bancário\n  -  7: Compra\n  -  8: Devolução de venda\n  -  9: Devolução de compra\n  - 10: Produção\n  - 11: Pagamento\n  - 12: Financeiro\n  - 13: Pedido de Requisição\n  - 14: Pedido de Transferência\n  - 15: Devolução de Requisição\n  - 16: Devolução de Transf.\n  - 17: Entradas\n  - 18: Pedido de Compra\n  - 19: Pedido de Venda\n  - 20: Requisição\n  - 21: Recebimento\n  - 22: Transferência\n  - 23: Venda\n",
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
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23
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
              "default": "07/10/2025 10:38"
            },
            "description": "Data e hora da última modificação. Quando este parâmetro é enviado, o serviço retornará apenas os registros que foram modificados a partir da data e hora informadas. Vale ressaltar que este recurso é condicionada a utilização do [Log de Alterações no SankhyaOm](https://developer.sankhya.com.br/reference/get_logalteracoestabelas) no ambiente do cliente. O formato deve ser o seguinte: DD/MM/AAAA HH:MM"
          }
        ],
        "responses": {
          "200": {
            "description": "Lista de Tipos de Operação retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/TipoOperacao"
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
    "schemas": {
      "TipoOperacao": {
        "type": "object",
        "properties": {
          "codigoTipoOperacao": {
            "type": "integer",
            "description": "Código do Tipo de Operação",
            "example": 123
          },
          "nome": {
            "type": "string",
            "description": "Descrição da Tipo de Operação",
            "example": "Baixa de Financeiro"
          },
          "tipoMovimento": {
            "type": "integer",
            "description": "Código do Tipo de Movimento associado à Tipo de Operação. Valores aceitos:\n  -  1: NF Depósito\n  -  2: Pedido de Devolução\n  -  3: Saídas\n  -  4: Faturamento\n  -  5: Pedido de Armazenagem\n  -  6: Movimento bancário\n  -  7: Compra\n  -  8: Devolução de venda\n  -  9: Devolução de compra\n  - 10: Produção\n  - 11: Pagamento\n  - 12: Financeiro\n  - 13: Pedido de Requisição\n  - 14: Pedido de Transferência\n  - 15: Devolução de Requisição\n  - 16: Devolução de Transf.\n  - 17: Entradas\n  - 18: Pedido de Compra\n  - 19: Pedido de Venda\n  - 20: Requisição\n  - 21: Recebimento\n  - 22: Transferência\n  - 23: Venda\n",
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23
            ],
            "example": 12
          },
          "ativo": {
            "type": "boolean",
            "description": "Indica que o Tipo de Operação está ativo",
            "example": true
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
