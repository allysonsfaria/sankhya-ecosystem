---
id: "https://developer.sankhya.com.br/reference/get_v1-produtos-codigoproduto-volumes"
titulo: "Volumes de um respectivo Produto"
url: "https://developer.sankhya.com.br/reference/get_v1-produtos-codigoproduto-volumes"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Volumes de um respectivo Produto

Retorna uma lista de Volumes de um respectivo Produto, com paginação, cadastrados no SankhyaOM.

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
    "/v1/produtos/{codigoProduto}/volumes": {
      "get": {
        "tags": [
          "Produtos"
        ],
        "summary": "Volumes de um respectivo Produto",
        "description": "Retorna uma lista de Volumes de um respectivo Produto, com paginação, cadastrados no SankhyaOM.",
        "parameters": [
          {
            "name": "codigoProduto",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer"
            },
            "description": "Código do Produto para o contexto de volumes do produto."
          },
          {
            "name": "page",
            "in": "query",
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Número da página, iniciando sempre por ZERO (0)."
          }
        ],
        "responses": {
          "200": {
            "description": "Lista de Volumes de um respectivo Produto retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "volumesProduto": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/VolumesProduto"
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
        }
      }
    }
  },
  "components": {
    "schemas": {
      "VolumesProduto": {
        "type": "object",
        "properties": {
          "unidade": {
            "type": "string",
            "description": "Unidade de medida do volume alternativo.",
            "example": "CX"
          },
          "controle": {
            "type": "string",
            "description": "Valor de controle associado ao volume alternativo (geralmente utilizado para identificação ou agrupamento interno).",
            "example": "Lote2025"
          },
          "operacao": {
            "type": "integer",
            "description": "Tipo de operação para o volume alternativo. \n  - 1 - Multiplica \n  - 2 - Divide",
            "example": 1
          },
          "multiplicadorValor": {
            "type": "number",
            "format": "float",
            "description": "Fator utilizado como multiplicador para valor do volume alternativo.",
            "example": 1.5
          },
          "quantidade": {
            "type": "number",
            "format": "float",
            "description": "Quantidade referente ao volume alternativo.",
            "example": 10
          },
          "codigoBarra": {
            "type": "string",
            "description": "Código de barras associado ao volume alternativo do produto.",
            "example": "7891234567890"
          },
          "ativo": {
            "type": "boolean",
            "description": "Indica se o volume alternativo está ativo.",
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
