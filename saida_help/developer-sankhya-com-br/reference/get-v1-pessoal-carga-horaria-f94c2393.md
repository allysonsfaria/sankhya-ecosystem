---
id: "https://developer.sankhya.com.br/reference/get_v1-pessoal-carga-horaria"
titulo: "Registro de todas as cargas horárias"
url: "https://developer.sankhya.com.br/reference/get_v1-pessoal-carga-horaria"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Registro de todas as cargas horárias

Retorna todos os registros de cargas horárias. 

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
      "name": "HCM Cadastros",
      "description": "Cadastros Básicos relacionados a Pessoal no SankhyaOm"
    }
  ],
  "paths": {
    "/v1/pessoal/carga-horaria": {
      "get": {
        "tags": [
          "HCM Cadastros"
        ],
        "summary": "Registro de todas as cargas horárias",
        "description": "Retorna todos os registros de cargas horárias. \n\n Versão mínima do módulo pessoal: **5.53.0**",
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
            "schema": {
              "type": "string",
              "default": 0
            },
            "description": "Data hora da ultima modificação. Quando este parametro é enviado, o serviço retorana apenas registros que tiveram modificação deste da data/hora enviada. Vale ressaltar que este recurso é condicionada a utilização do [Log de Alterações no SankhyaOm](https://developer.sankhya.com.br/reference/get_logalteracoestabelas) no ambiente do cliente. O formato deve ser o seguinte: AAAA-MM-DDTHH:MM:SS"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados do Registro de Cargas Horárias retornado com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "cargasHorarias": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/CargaHorariaCargaHoraria"
                      }
                    }
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
                  "$ref": "#/components/schemas/CargaHorariaretorno400"
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
      "CargaHorariaretorno400": {
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
                "example": "O campo 'codigoEmpresa' é obrigatório."
              }
            }
          }
        }
      },
      "CargaHorariaCargaHoraria": {
        "type": "object",
        "properties": {
          "codigoCargaHoraria": {
            "type": "integer",
            "description": "Código atribuído à carga horária.",
            "example": 1
          },
          "descricao": {
            "type": "string",
            "description": "Descrição da carga horária.",
            "example": "Carga Horária Padrão"
          },
          "diaSemana": {
            "type": "integer",
            "description": "Indica sequência quando se tratar de uma carga horária por escala, ou dias da semana quando for por jornada fixa.\nDias da semana:\n - 1: Domingo\n - 2: Segunda-feira\n - 3: Terça-feira\n - 4: Quarta-feira\n - 5: Quinta-feira\n - 6: Sexta-feira\n - 7: Sábado",
            "enum": [
              1,
              2,
              3,
              4,
              5,
              6,
              7
            ],
            "example": 1
          },
          "turno": {
            "type": "integer",
            "description": "Indica qual o turno se refere o horário informado, sendo possível ter até 4 turnos por dia.",
            "example": 1
          },
          "entrada": {
            "type": "integer",
            "description": "Horário de entrada do turno.",
            "example": 900
          },
          "saida": {
            "type": "integer",
            "description": "Horário de saída do turno.",
            "example": 1800
          },
          "descansoSemanal": {
            "type": "boolean",
            "description": "Indica se o dia é de descanso semanal.",
            "example": true
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
