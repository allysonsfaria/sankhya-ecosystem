---
id: "https://developer.sankhya.com.br/reference/get_v1-financeiros-contas-bancaria-codigocontabancaria"
titulo: "Conta Bancária Específica"
url: "https://developer.sankhya.com.br/reference/get_v1-financeiros-contas-bancaria-codigocontabancaria"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Conta Bancária Específica

Retorna uma Conta Bancária específica com base no parâmetro enviado na requisição.

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
    "/v1/financeiros/contas-bancaria/{codigoContaBancaria}": {
      "get": {
        "tags": [
          "Financeiros Cadastros"
        ],
        "summary": "Conta Bancária Específica",
        "description": "Retorna uma Conta Bancária específica com base no parâmetro enviado na requisição.",
        "parameters": [
          {
            "name": "codigoContaBancaria",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código da Conta Bancária para retorno"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados da Conta Bancária retornados com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ContaBancaria"
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
      "ContaBancaria": {
        "type": "object",
        "properties": {
          "codigoContaBancaria": {
            "type": "integer",
            "description": "Código interno da conta bancária",
            "example": 1024
          },
          "descricao": {
            "type": "string",
            "description": "Descrição da conta bancária",
            "example": "Conta corrente principal"
          },
          "ativo": {
            "type": "boolean",
            "description": "Informa se a conta está ativa",
            "example": true
          },
          "tipoConta": {
            "type": "integer",
            "description": "Tipo da conta bancária:\n1 - Aplicação  \n2 - Corrente  \n3 - Adiantamento  \n4 - Empréstimo  \n5 - Caixa (PDV)  \n6 - Comissões  \n7 - Outros  \n8 - Sócios  \n9 - Caixa-Tesouraria  \n10 - Garantida\n",
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
              10
            ],
            "example": 2
          },
          "codigoBanco": {
            "type": "integer",
            "description": "Código do banco",
            "example": 341
          },
          "nomeBanco": {
            "type": "string",
            "description": "Nome do banco",
            "example": "Banco do Brasil"
          },
          "codigoAgencia": {
            "type": "string",
            "description": "Código da agência bancária",
            "example": "1234-5"
          },
          "nomeAgencia": {
            "type": "string",
            "description": "Nome da agência bancária",
            "example": "Agencia Floriano"
          },
          "contaBancaria": {
            "type": "string",
            "description": "Número da conta bancária",
            "example": "987654-3"
          },
          "codigoContaContabil": {
            "type": "integer",
            "description": "Código da conta contábil associada",
            "example": 578
          },
          "codigoEmpresa": {
            "type": "integer",
            "description": "Código da empresa",
            "example": 1
          },
          "nomeEmpresa": {
            "type": "string",
            "description": "Nome da empresa",
            "example": "TECH SOLUTIONS"
          },
          "codigoMoeda": {
            "type": "integer",
            "description": "Código da moeda vinculada",
            "example": 790
          },
          "nomeMoeda": {
            "type": "string",
            "description": "Nome da moeda vinculada",
            "example": "Real"
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
