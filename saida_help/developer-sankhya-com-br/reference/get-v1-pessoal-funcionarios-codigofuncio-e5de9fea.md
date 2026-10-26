---
id: "https://developer.sankhya.com.br/reference/get_v1-pessoal-funcionarios-codigofuncionario-empresas-codigoempresa-atrasos"
titulo: "Lista de registros de Atrasos de um determinado funcionário e empresa."
url: "https://developer.sankhya.com.br/reference/get_v1-pessoal-funcionarios-codigofuncionario-empresas-codigoempresa-atrasos"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Lista de registros de Atrasos de um determinado funcionário e empresa.

Retorna uma lista de Registros de Atrasos, com paginação, cadastradas no SankhyaOM. 

 Versão mínima do módulo pessoal: **5.53.0**

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
      "name": "HCM Funcionários",
      "description": "Cadastros relacionados a Funcionários no SankhyaOm"
    }
  ],
  "paths": {
    "/v1/pessoal/funcionarios/{codigoFuncionario}/empresas/{codigoEmpresa}/atrasos": {
      "get": {
        "tags": [
          "HCM Funcionários"
        ],
        "summary": "Lista de registros de Atrasos de um determinado funcionário e empresa.",
        "description": "Retorna uma lista de Registros de Atrasos, com paginação, cadastradas no SankhyaOM. \n\n Versão mínima do módulo pessoal: **5.53.0**",
        "parameters": [
          {
            "name": "codigoFuncionario",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código do Funcionário"
          },
          {
            "name": "codigoEmpresa",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código da Empresa"
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
            "description": "Lista de Registros de Atrasos retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Atraso"
                  }
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Atrasosretorno400"
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
      "Atrasosretorno400": {
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
                "example": "O parâmetro 'codigoEmpresa' é obrigatório quando 'codigoFuncionario' é informado."
              }
            }
          }
        }
      },
      "Atraso": {
        "type": "object",
        "properties": {
          "dataAtraso": {
            "type": "string",
            "description": "Data que ocorreu o atraso ou saída antecipada.",
            "example": "10/03/2025 16:03:12"
          },
          "minutos": {
            "type": "integer",
            "description": "Quantidade de minutos de atrasos.",
            "example": 8
          },
          "perdeDsr": {
            "type": "boolean",
            "description": "Indica se houve perda de DSR(Descanso Semanal Remunerado).",
            "example": true
          },
          "empresa": {
            "type": "object",
            "description": "Informações da empresa.",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código da empresa.",
                "example": 252515
              },
              "nome": {
                "type": "string",
                "description": "Nome da empresa.",
                "example": "SANKHYA."
              }
            }
          },
          "funcionario": {
            "type": "object",
            "description": "Informações do funcionário.",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código do funcionário.",
                "example": 252515
              },
              "nome": {
                "type": "string",
                "description": "Nome do funcionário.",
                "example": "Pedro José Souza."
              }
            }
          },
          "dataAlteracao": {
            "type": "string",
            "description": "Data da última alteração.",
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
