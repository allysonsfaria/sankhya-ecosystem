---
id: "https://developer.sankhya.com.br/reference/get_v1-volumes-produtos-codigovolume"
titulo: "Volume específico"
url: "https://developer.sankhya.com.br/reference/get_v1-volumes-produtos-codigovolume"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Volume específico

Retorna um Volume específico com base no parâmetro enviado na requisição.

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
      "name": "Produtos",
      "description": "Cadastros Relacionados a Produtos"
    }
  ],
  "paths": {
    "/v1/volumes-produtos/{codigoVolume}": {
      "get": {
        "tags": [
          "Produtos"
        ],
        "summary": "Volume específico",
        "description": "Retorna um Volume específico com base no parâmetro enviado na requisição.",
        "parameters": [
          {
            "name": "codigoVolume",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Código do Volume para retorno"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados do Volume retornados com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Volume"
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
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Volume": {
        "type": "object",
        "properties": {
          "codigoVolume": {
            "type": "string",
            "description": "Sigla da unidade de volume.",
            "example": "KG"
          },
          "nome": {
            "type": "string",
            "description": "Descrição completa da unidade de volume.",
            "example": "Quilograma"
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
