---
id: "https://developer.sankhya.com.br/reference/get_v1-financeiros-moedas-codigomoeda-cotacoes"
titulo: "Lista de Cotações de Moedas"
url: "https://developer.sankhya.com.br/reference/get_v1-financeiros-moedas-codigomoeda-cotacoes"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Lista de Cotações de Moedas

Retorna uma lista de cotações da moeda enviada no contexto, com paginação, cadastradas no SankhyaOM.


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
    "/v1/financeiros/moedas/{codigoMoeda}/cotacoes": {
      "get": {
        "tags": [
          "Financeiros Cadastros"
        ],
        "summary": "Lista de Cotações de Moedas",
        "description": "Retorna uma lista de cotações da moeda enviada no contexto, com paginação, cadastradas no SankhyaOM.\n",
        "parameters": [
          {
            "name": "codigoMoeda",
            "in": "path",
            "description": "Código da Moeda",
            "required": true,
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "dataCotacao",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "example": "16/06/2025"
            },
            "description": "Data da cotação desejada."
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
            "description": "Lista de cotações retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Cotacao"
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
    "schemas": {
      "Cotacao": {
        "type": "object",
        "properties": {
          "dataCotacao": {
            "type": "string",
            "description": "Data da cotação",
            "example": "16/06/2025"
          },
          "valor": {
            "type": "number",
            "description": "Valor da Cotação",
            "example": 5.87
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
