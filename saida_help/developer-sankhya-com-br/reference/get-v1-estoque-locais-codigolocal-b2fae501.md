---
id: "https://developer.sankhya.com.br/reference/get_v1-estoque-locais-codigolocal"
titulo: "Local de Estoque específico"
url: "https://developer.sankhya.com.br/reference/get_v1-estoque-locais-codigolocal"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Local de Estoque específico

Retorna um Local de Estoque específico com base no parâmetro enviado na requisição.

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
      "name": "Estoque",
      "description": "Retorna estoque de produto existente no SankhyaOm"
    }
  ],
  "paths": {
    "/v1/estoque/locais/{codigoLocal}": {
      "get": {
        "tags": [
          "Estoque"
        ],
        "summary": "Local de Estoque específico",
        "description": "Retorna um Local de Estoque específico com base no parâmetro enviado na requisição.",
        "parameters": [
          {
            "name": "codigoLocal",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código do Local de Estoque para retorno"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados do Local de Estoque retornado com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/LocalEstoque"
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
      "LocalEstoque": {
        "type": "object",
        "properties": {
          "codigoLocal": {
            "type": "integer",
            "example": 101,
            "description": "Código identificador único do local de estoque."
          },
          "codigoLocalPai": {
            "type": "integer",
            "example": 100,
            "description": "Código do local de estoque pai, utilizado em estruturas hierárquicas."
          },
          "descricaoLocal": {
            "type": "string",
            "example": "Almoxarifado Central",
            "description": "Descrição do local de estoque."
          },
          "grau": {
            "type": "integer",
            "example": 2,
            "description": "Grau hierárquico do local de estoque."
          },
          "analitico": {
            "type": "boolean",
            "example": true,
            "description": "Indica se o local de estoque é analítico (não pode ter filhos).\n"
          },
          "ativo": {
            "type": "boolean",
            "example": true,
            "description": "Indica se o local de estoque está ativo.\n"
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
