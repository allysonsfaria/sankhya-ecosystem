---
id: "https://developer.sankhya.com.br/reference/get_v1-vendedores"
titulo: "Lista de Vendedores"
url: "https://developer.sankhya.com.br/reference/get_v1-vendedores"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Lista de Vendedores

Retorna uma lista de Vendedores, com paginação, cadastrados no SankhyaOM.

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
    "/v1/vendedores": {
      "get": {
        "tags": [
          "Cadastros Básicos"
        ],
        "summary": "Lista de Vendedores",
        "description": "Retorna uma lista de Vendedores, com paginação, cadastrados no SankhyaOM.",
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
            "description": "Data e hora da última modificação. Quando esse parâmetro é enviado, o serviço retorna apenas os registros que foram modificados a partir da data e hora informadas. Vale ressaltar que este recurso é condicionada a utilização do [Log de Alterações no SankhyaOm](https://developer.sankhya.com.br/reference/get_logalteracoestabelas) no ambiente do cliente. O formato deve ser o seguinte: DD/MM/AAAA HH:MM",
            "required": false,
            "schema": {
              "type": "string",
              "example": "07/10/2025 10:38"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Lista de Vendedores retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "vendedores": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/Vendedor"
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
      "Vendedor": {
        "type": "object",
        "properties": {
          "codigoVendedor": {
            "type": "integer",
            "description": "Código do vendedor.",
            "example": 101
          },
          "nome": {
            "type": "string",
            "description": "Nome do vendedor.",
            "example": "joaodasilva"
          },
          "ativo": {
            "type": "boolean",
            "description": "Indica se o vendedor está ativo. `true` para Sim, `false` para Não.",
            "example": true
          },
          "tipo": {
            "type": "integer",
            "enum": [
              1,
              2,
              3,
              4,
              5,
              6,
              7
            ],
            "description": "Tipo do vendedor:\n  - 1 - Comprador\n  - 2 - Executante\n  - 3 - Gerente\n  - 4 - Vendedor\n  - 5 - Supervisor\n  - 6 - Técnico\n  - 7 - Representante",
            "example": 4
          },
          "comissaoGerencia": {
            "type": "number",
            "format": "float",
            "description": "Percentual de comissão da gerência.",
            "example": 2.5
          },
          "comissaoVenda": {
            "type": "number",
            "format": "float",
            "description": "Percentual de comissão por venda.",
            "example": 5.75
          },
          "email": {
            "type": "string",
            "format": "email",
            "description": "Endereço de e-mail do vendedor.",
            "example": "vendedor@email.com"
          },
          "codigoEmpresa": {
            "type": "integer",
            "description": "Código da empresa.",
            "example": 1
          },
          "nomeEmpresa": {
            "type": "string",
            "description": "Nome da empresa.",
            "example": "Tech Company"
          },
          "codigoParceiro": {
            "type": "integer",
            "description": "Código do parceiro.",
            "example": 456
          },
          "nomeParceiro": {
            "type": "string",
            "description": "Nome do parceiro.",
            "example": "Josefina Andrade"
          },
          "codigoFuncionario": {
            "type": "integer",
            "description": "Código do funcionário.",
            "example": 789
          },
          "nomeFuncionario": {
            "type": "string",
            "description": "Nome do funcionário.",
            "example": "Emanuel Oliveira"
          },
          "codigoGerente": {
            "type": "integer",
            "description": "Código do gerente responsável.",
            "example": 321
          },
          "nomeGerente": {
            "type": "string",
            "description": "Nome do gerente responsável.",
            "example": "Evandro Rocha"
          },
          "codigoCentroResultado": {
            "type": "integer",
            "description": "Código do centro de resultado.",
            "example": 12
          },
          "nomeCentroResultado": {
            "type": "string",
            "description": "Nome do centro de resultado.",
            "example": "Vendas"
          },
          "codigoRegiao": {
            "type": "integer",
            "description": "Código da região de atuação.",
            "example": 5
          },
          "nomeRegiao": {
            "type": "string",
            "description": "Nome da região de atuação.",
            "example": "Zona Norte"
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
