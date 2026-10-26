---
id: "https://developer.sankhya.com.br/reference/get_v1-usuarios-codigousuario"
titulo: "Usuário específico"
url: "https://developer.sankhya.com.br/reference/get_v1-usuarios-codigousuario"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Usuário específico

Retorna um Usuário específico com base no parâmetro enviado na requisição.

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
    "/v1/usuarios/{codigoUsuario}": {
      "get": {
        "tags": [
          "Cadastros Básicos"
        ],
        "summary": "Usuário específico",
        "description": "Retorna um Usuário específico com base no parâmetro enviado na requisição.",
        "parameters": [
          {
            "name": "codigoUsuario",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código do Usuário para retorno"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados do Usuário retornados com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Usuario"
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
      "Usuario": {
        "type": "object",
        "properties": {
          "codigoUsuario": {
            "type": "integer",
            "description": "Código identificador único do usuário.",
            "example": 123
          },
          "nome": {
            "type": "string",
            "description": "Nome completo do usuário.",
            "example": "João da Silva"
          },
          "caixa": {
            "type": "boolean",
            "description": "Indica se o usuário é um caixa. `true` para Sim, `false` para Não.",
            "example": true
          },
          "codigoEmpresa": {
            "type": "integer",
            "description": "Código da empresa.",
            "example": 1
          },
          "nomeEmpresa": {
            "type": "string",
            "description": "Razão social da empresa.",
            "example": "Tech Solutions LTDA"
          },
          "codigoVendedor": {
            "type": "integer",
            "description": "Código do vendedor.",
            "example": 1
          },
          "nomeVendedor": {
            "type": "string",
            "description": "Nome do Vendedor.",
            "example": "JOAO.SILVA"
          },
          "email": {
            "type": "string",
            "format": "email",
            "description": "Endereço de email do usuário.",
            "example": "usuario@empresa.com.br"
          },
          "cpf": {
            "type": "string",
            "description": "CPF do usuário.",
            "example": "12345678900"
          },
          "rg": {
            "type": "string",
            "description": "RG (Registro Geral) do usuário.",
            "example": "MG-12.345.678"
          },
          "dataLimiteAcesso": {
            "type": "string",
            "format": "date",
            "description": "Data limite para o usuário acessar o sistema.",
            "example": "16/05/2025"
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
