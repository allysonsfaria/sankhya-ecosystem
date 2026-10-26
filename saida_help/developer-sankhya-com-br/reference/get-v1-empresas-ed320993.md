---
id: "https://developer.sankhya.com.br/reference/get_v1-empresas"
titulo: "Lista de Empresas"
url: "https://developer.sankhya.com.br/reference/get_v1-empresas"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Lista de Empresas

Retorna uma lista de Empresas, com paginação, cadastradas no SankhyaOM.

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
    "/v1/empresas": {
      "get": {
        "tags": [
          "Cadastros Básicos"
        ],
        "summary": "Lista de Empresas",
        "description": "Retorna uma lista de Empresas, com paginação, cadastradas no SankhyaOM.",
        "parameters": [
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
            "description": "Lista de Empresas retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "empresas": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/Empresa1"
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
      "Empresa1": {
        "type": "object",
        "properties": {
          "codigoEmpresa": {
            "type": "integer",
            "description": "Código identificador da empresa",
            "example": 123
          },
          "nomeFantasia": {
            "type": "string",
            "description": "Nome fantasia da empresa",
            "example": "Tech Solutions"
          },
          "razaoSocial": {
            "type": "string",
            "description": "Razão social da empresa",
            "example": "Tech Solutions LTDA"
          },
          "razaoAbreviada": {
            "type": "string",
            "description": "Razão social abreviada",
            "example": "Tech Sol"
          },
          "cnpjCpf": {
            "type": "string",
            "description": "CNPJ ou CPF da empresa",
            "example": "12.345.678/0001-90"
          },
          "inscricaoEstadual": {
            "type": "string",
            "description": "Inscrição estadual da empresa",
            "example": "123456789"
          },
          "inscricaoMunicipal": {
            "type": "string",
            "description": "Inscrição municipal da empresa",
            "example": "987654321"
          },
          "telefone": {
            "type": "string",
            "description": "Telefone de contato da empresa",
            "example": "11 912345678"
          },
          "email": {
            "type": "string",
            "description": "Endereço de e-mail da empresa",
            "example": "contato@techsolutions.com"
          },
          "homepage": {
            "type": "string",
            "description": "Site institucional da empresa",
            "example": "https://www.techsolutions.com"
          },
          "codigoLogradouro": {
            "type": "integer",
            "description": "Código do Logradouro",
            "example": 123
          },
          "nomeLogradouro": {
            "type": "string",
            "description": "Nome do Logradouro",
            "example": "Rua José da Silva"
          },
          "numero": {
            "type": "string",
            "description": "Número do endereço da empresa",
            "example": "100A"
          },
          "complemento": {
            "type": "string",
            "description": "Complemento do endereço",
            "example": "Sala 201"
          },
          "codigoBairro": {
            "type": "integer",
            "description": "Código do Bairro",
            "example": 789
          },
          "nomeBairro": {
            "type": "string",
            "description": "Nome do Bairro",
            "example": "Centro"
          },
          "codigoCidade": {
            "type": "integer",
            "description": "Código da Cidade",
            "example": 1234
          },
          "nomeCidade": {
            "type": "string",
            "description": "Nome da Cidade",
            "example": "Uberlândia"
          },
          "cep": {
            "type": "string",
            "description": "CEP do endereço da empresa",
            "example": "01234567"
          },
          "codigoEmpresaMatriz": {
            "type": "integer",
            "description": "Código da empresa matriz (caso aplicável)",
            "example": 1
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
