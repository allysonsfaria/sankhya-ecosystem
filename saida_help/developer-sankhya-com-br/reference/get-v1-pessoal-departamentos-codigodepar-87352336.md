---
id: "https://developer.sankhya.com.br/reference/get_v1-pessoal-departamentos-codigodepartamento"
titulo: "Departamento específico"
url: "https://developer.sankhya.com.br/reference/get_v1-pessoal-departamentos-codigodepartamento"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Departamento específico

Retorna um Departamento específico com base no parâmetro enviado na requisição. 

 Versão mínima do módulo pessoal: **5.48.0**

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
      "name": "HCM Cadastros",
      "description": "Cadastros Básicos relacionados a Pessoal no SankhyaOm"
    }
  ],
  "paths": {
    "/v1/pessoal/departamentos/{codigoDepartamento}": {
      "get": {
        "tags": [
          "HCM Cadastros"
        ],
        "summary": "Departamento específico",
        "description": "Retorna um Departamento específico com base no parâmetro enviado na requisição. \n\n Versão mínima do módulo pessoal: **5.48.0**",
        "parameters": [
          {
            "name": "codigoDepartamento",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código do Departamento"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados do Departamento retornado com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Departamento"
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Departamentoretorno400"
                }
              }
            }
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
      "Departamentoretorno400": {
        "type": "object",
        "properties": {
          "statusCode": {
            "type": "integer",
            "format": "int32",
            "example": 400
          },
          "error": {
            "type": "object",
            "properties": {
              "code": {
                "type": "string",
                "example": "BAD_REQUEST"
              },
              "message": {
                "type": "string",
                "example": "Ocorreu algum erro inesperado!"
              },
              "details": {
                "type": "string",
                "example": "O parâmetro de paginação 'pageSize' deve ser um número inteiro positivo."
              }
            }
          }
        }
      },
      "Departamento": {
        "type": "object",
        "properties": {
          "codigoDepartamento": {
            "type": "integer",
            "description": "Código do departamento",
            "example": 101
          },
          "nome": {
            "type": "string",
            "description": "Nome atribuído ao Departamento",
            "example": "Departamento pessoal."
          },
          "ativo": {
            "type": "boolean",
            "description": "Indica se o departamento está ativo (valor original S/N)",
            "example": true
          },
          "endereco": {
            "type": "object",
            "description": "Informações de endereço do departamento.",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código do Endereço do Departamento.",
                "example": 252515
              },
              "descricao": {
                "type": "string",
                "description": "Descrição atribuída ao endereço",
                "example": "Rua andorinhas."
              },
              "numero": {
                "type": "string",
                "description": "Número do logradouro",
                "example": "200"
              },
              "complemento": {
                "type": "string",
                "description": "Complemento do endereço",
                "example": "apto 906."
              }
            }
          },
          "centroResultado": {
            "type": "object",
            "description": "Informações sobre o centro de resultado associado ao departamento.",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código do centro de resultado associado ao departamento.",
                "example": 252515
              },
              "descricao": {
                "type": "string",
                "description": "Descrição do centro de resultado associado ao departamento.",
                "example": "Centro de resultado xpto."
              }
            }
          },
          "registroFiscal": {
            "type": "object",
            "description": "Informações de registro fiscal vinculado ao departamento.",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código de registro fiscal vinculado ao departamento.",
                "example": 252515
              },
              "descricao": {
                "type": "string",
                "description": "Descrição de registro fiscal vinculado ao departamento.",
                "example": "Registro fiscal xpto."
              }
            }
          },
          "parceiro": {
            "type": "object",
            "description": "Informações do parceiro vinculado ao departamento em caso de tomadores de serviço.",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código do parceiro vinculado ao departamento em caso de tomadores de serviço.",
                "example": 252515
              },
              "nome": {
                "type": "string",
                "description": "Nome do parceiro vinculado ao departamento",
                "example": "Parceiro empresarial."
              }
            }
          },
          "lotacao": {
            "type": "object",
            "description": "Informações de Tipo de lotação.",
            "properties": {
              "tipo": {
                "type": "integer",
                "description": "Tipo de lotação conforme tabela 10 - Tipos de Lotação Tributária, da versão S-1.3 do eSocial.",
                "example": 4
              },
              "descricao": {
                "type": "string",
                "description": "Descrição da lotação atribuída ao departamento",
                "example": "Pessoa Jurídica Tomadora de Serviços prestados mediante cessão de mão de obra, exceto contratante de cooperativa, nos termos da lei 8.212/1991."
              }
            }
          },
          "dataAlteracao": {
            "type": "string",
            "description": "Data da última alteração",
            "example": "10/03/2022 16:03:12"
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
