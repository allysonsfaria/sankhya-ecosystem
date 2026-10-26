---
id: "https://developer.sankhya.com.br/reference/get_v1-logradouros"
titulo: "Lista de Logradouros"
url: "https://developer.sankhya.com.br/reference/get_v1-logradouros"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Lista de Logradouros

Retorna uma lista de Logradouros, com paginação, cadastradas no SankhyaOM.

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
    "/v1/logradouros": {
      "get": {
        "tags": [
          "Cadastros Básicos"
        ],
        "summary": "Lista de Logradouros",
        "description": "Retorna uma lista de Logradouros, com paginação, cadastradas no SankhyaOM.",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Número da página, iniciando sempre por ZERO (0)."
          },
          {
            "name": "modifiedSince",
            "in": "query",
            "schema": {
              "type": "string",
              "example": "07/10/2025 10:38"
            },
            "description": "Data e hora da última modificação. Quando esse parâmetro é enviado, o serviço retorna apenas os registros que foram modificados a partir da data e hora informadas. Vale ressaltar que este recurso é condicionada a utilização do [Log de Alterações no SankhyaOm](https://developer.sankhya.com.br/reference/get_logalteracoestabelas) no ambiente do cliente. O formato deve ser o seguinte: DD/MM/AAAA HH:MM"
          }
        ],
        "responses": {
          "200": {
            "description": "Lista de Logradouros retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Logradouro"
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
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Logradouro": {
        "type": "object",
        "properties": {
          "codigoLogradouro": {
            "type": "integer",
            "description": "Código identificador do logradouro.",
            "example": 101
          },
          "nome": {
            "type": "string",
            "description": "Nome do endereço.",
            "example": "ESPIRITO SANTO"
          },
          "tipo": {
            "type": "string",
            "description": "Tipo genérico associado ao endereço.",
            "example": "Rua"
          },
          "descricaoCorreio": {
            "type": "string",
            "description": "Nome do endereço conforme correio.",
            "example": "Rua das Flores"
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
