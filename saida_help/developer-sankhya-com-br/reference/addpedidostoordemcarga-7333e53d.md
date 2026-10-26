---
id: "https://developer.sankhya.com.br/reference/addpedidostoordemcarga"
titulo: "Adicionar Pedidos à Ordem de Carga (Lista)"
url: "https://developer.sankhya.com.br/reference/addpedidostoordemcarga"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Adicionar Pedidos à Ordem de Carga (Lista)


Adiciona um pedido a uma Ordem de Carga existente.



**Regras para atualização de ordem de carga no pedido:**

* A Ordem de Carga deve estar com a situação Aberta.

* O pedido não pode estar totalmente faturado.

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
      "put": {
        "tags": [
          "Logística"
        ],
        "summary": "Adicionar Pedidos à Ordem de Carga (Lista)",
        "description": "\nAdiciona um pedido a uma Ordem de Carga existente.\n\n\n\n**Regras para atualização de ordem de carga no pedido:**\n\n* A Ordem de Carga deve estar com a situação Aberta.\n\n* O pedido não pode estar totalmente faturado.",
        "operationId": "addPedidosToOrdemCarga",
        "responses": {
          "201": {
            "description": "Todos os pedidos foram adicionados com sucesso."
          },
          "400": {
            "description": "O pedido não pôde ser processado devido a dados inválidos ou violação das regras de negócio."
          },
          "404": {
            "description": "Ordem de Carga ou Empresa não encontrada."
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
