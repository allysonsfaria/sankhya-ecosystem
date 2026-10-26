---
id: "https://developer.sankhya.com.br/reference/getpedidosbyordemcarga"
titulo: "Consultar Pedidos da Ordem de Carga (Lista)"
url: "https://developer.sankhya.com.br/reference/getpedidosbyordemcarga"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Consultar Pedidos da Ordem de Carga (Lista)

Retorna a lista de pedidos atualmente associados a uma Ordem de Carga específica.

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
      "name": "Logística",
      "description": "Cadastros básicos relacionados a motorista, transportadora, ordens de carga, veículos, no Sankhya Om"
    }
  ],
  "paths": {
    "/v1/logistica/empresas/{codigoEmpresa}/ordens-carga/{codigoOrdemCarga}/pedidos/{codigoPedido}": {
      "parameters": [
        {
          "name": "codigoEmpresa",
          "in": "path",
          "description": "Código da empresa.",
          "required": true,
          "schema": {
            "type": "integer",
            "format": "int64"
          }
        },
        {
          "name": "codigoOrdemCarga",
          "in": "path",
          "description": "Código único da Ordem de Carga.",
          "required": true,
          "schema": {
            "type": "integer",
            "format": "int64"
          }
        },
        {
          "name": "codigoPedido",
          "in": "path",
          "description": "Código único do pedido.",
          "required": true,
          "schema": {
            "type": "integer",
            "format": "int64"
          }
        }
      ],
      "get": {
        "tags": [
          "Logística"
        ],
        "summary": "Consultar Pedidos da Ordem de Carga (Lista)",
        "description": "Retorna a lista de pedidos atualmente associados a uma Ordem de Carga específica.",
        "operationId": "getPedidosByOrdemCarga",
        "responses": {
          "200": {
            "description": "Lista de pedidos retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PedidoResponse"
                }
              }
            }
          },
          "404": {
            "description": "Ordem de Carga ou Empresa não encontrada."
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PedidoBase": {
        "type": "object",
        "properties": {
          "codigoPedido": {
            "type": "integer",
            "description": "Código único do pedido (TGFCAB.NUNOTA).",
            "example": 10565
          },
          "numeroPedido": {
            "type": "integer",
            "description": "Número da nota/pedido (TGFCAB.NUMNOTA).",
            "example": 45
          },
          "serie": {
            "type": "string",
            "description": "Série do pedido.",
            "example": "SN"
          },
          "cnpjEmpresa": {
            "type": "string",
            "description": "CNPJ da empresa faturadora.",
            "example": "12345678000199"
          }
        }
      },
      "PedidoResponse": {
        "type": "object",
        "properties": {
          "pedidos": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PedidoBase"
            }
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
