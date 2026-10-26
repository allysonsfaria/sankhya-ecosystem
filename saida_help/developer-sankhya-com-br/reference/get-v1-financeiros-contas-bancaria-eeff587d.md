---
id: "https://developer.sankhya.com.br/reference/get_v1-financeiros-contas-bancaria"
titulo: "Lista de Contas Bancárias"
url: "https://developer.sankhya.com.br/reference/get_v1-financeiros-contas-bancaria"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Lista de Contas Bancárias

Retorna uma lista de Conta Bancária, com paginação, cadastradas no SankhyaOM.

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
    "/v1/financeiros/contas-bancaria": {
      "get": {
        "tags": [
          "Financeiros Cadastros"
        ],
        "summary": "Lista de Contas Bancárias",
        "description": "Retorna uma lista de Conta Bancária, com paginação, cadastradas no SankhyaOM.",
        "parameters": [
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
            "description": "Lista de Contas Bancárias retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/ContaBancaria"
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
