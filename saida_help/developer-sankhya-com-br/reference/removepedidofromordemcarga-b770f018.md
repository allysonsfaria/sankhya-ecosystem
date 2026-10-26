---
id: "https://developer.sankhya.com.br/reference/removepedidofromordemcarga"
titulo: "Remover Pedido Específico da Ordem de Carga"
url: "https://developer.sankhya.com.br/reference/removepedidofromordemcarga"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Remover Pedido Específico da Ordem de Carga


Remove um único pedido de uma Ordem de Carga existente, identificado pelo `codigoPedido` no path.



**Regras para atualização de ordem de carga no pedido:**

* A Ordem de Carga deve estar com a situação Aberta.

* O pedido deve estar confirmado e não faturado totalmente.

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
    "/v1/logistica/empresas/{codigoEmpresa}/ordens-carga/{codigoOrdemCarga}/pedidos/{codigoPedido}/delete": {
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
          "description": "Código único do pedido (TGFCAB.NUNOTA) a ser removido.",
          "required": true,
          "schema": {
            "type": "integer",
            "format": "int64"
          }
        }
      ],
      "put": {
        "tags": [
          "Logística"
        ],
        "summary": "Remover Pedido Específico da Ordem de Carga",
        "description": "\nRemove um único pedido de uma Ordem de Carga existente, identificado pelo `codigoPedido` no path.\n\n\n\n**Regras para atualização de ordem de carga no pedido:**\n\n* A Ordem de Carga deve estar com a situação Aberta.\n\n* O pedido deve estar confirmado e não faturado totalmente.",
        "operationId": "removePedidoFromOrdemCarga",
        "responses": {
          "204": {
            "description": "Pedido removido com sucesso."
          },
          "400": {
            "description": "O pedido não pôde ser removido devido a violação das regras de negócio."
          },
          "404": {
            "description": "Ordem de Carga, Empresa ou Pedido não encontrado."
          }
        }
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
