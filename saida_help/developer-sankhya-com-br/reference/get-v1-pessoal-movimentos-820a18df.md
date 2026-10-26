---
id: "https://developer.sankhya.com.br/reference/get_v1-pessoal-movimentos"
titulo: "Registro de todos os movimentos"
url: "https://developer.sankhya.com.br/reference/get_v1-pessoal-movimentos"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Registro de todos os movimentos

Retorna todos os registros de movimentos. 

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
    "/v1/pessoal/movimentos": {
      "get": {
        "tags": [
          "HCM Cadastros"
        ],
        "summary": "Registro de todos os movimentos",
        "description": "Retorna todos os registros de movimentos. \n\n Versão mínima do módulo pessoal: **5.53.0**",
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
            "name": "dataInicio",
            "in": "query",
            "schema": {
              "type": "string",
              "default": ""
            },
            "description": "Data inicial limite para os movimentos. Exemplo: 01-01-2025."
          },
          {
            "name": "dataFim",
            "in": "query",
            "schema": {
              "type": "string",
              "default": ""
            },
            "description": "Data final limite para os movimentos. Exemplo: 01-12-2025."
          },
          {
            "name": "modifiedSince",
            "in": "query",
            "schema": {
              "type": "string",
              "default": ""
            },
            "description": "Data hora da ultima modificação. Quando este parametro é enviado, o serviço retorana apenas registros que tiveram modificação deste da data/hora enviada. Vale ressaltar que este recurso é condicionada a utilização do [Log de Alterações no SankhyaOm](https://developer.sankhya.com.br/reference/get_logalteracoestabelas) no ambiente do cliente. O formato deve ser o seguinte: AAAA-MM-DDTHH:MM:SS"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados do Registro de Movimentos retornado com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Movimentos"
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
                  "$ref": "#/components/schemas/Movimentosretorno400"
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
      "Movimentosretorno400": {
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
      "Movimentos": {
        "type": "object",
        "properties": {
          "empresa": {
            "type": "object",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código da empresa",
                "example": 101
              },
              "nome": {
                "type": "string",
                "description": "Nome da empresa",
                "example": "Embraer."
              }
            }
          },
          "funcionario": {
            "type": "object",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código do funcionário",
                "example": 101
              },
              "nome": {
                "type": "string",
                "description": "Nome do funcionário",
                "example": "João."
              }
            }
          },
          "referencia": {
            "type": "string",
            "description": "Referência do lançamento.",
            "example": "10/03/2022 16:03:12"
          },
          "evento": {
            "type": "object",
            "properties": {
              "tipo": {
                "type": "integer",
                "description": "Tipo de evento. Os valores aceitos são:\n - -1: Desconto\n - 0: Neutro\n - 1: Provento",
                "enum": [
                  -1,
                  0,
                  1
                ],
                "example": 1
              },
              "codigo": {
                "type": "integer",
                "description": "Código do evento (rubrica).",
                "example": 101
              },
              "descricao": {
                "type": "string",
                "description": "Descrição do evento (rubrica).",
                "example": "Salário Base."
              }
            }
          },
          "tipo": {
            "type": "string",
            "description": "Tipo. Os valores aceitos são:\n - A: Adiantamento\n - C: Rescisão Complementar\n - D: 13° Salário\n - E: Férias\n - F: Fixo\n - M: Mensal\n - O: Dissídio\n - P: Produção\n - R: Rescisão\n - T: Verbas Meses Anteriores\n - U: Participação nos Lucros\n - V: Folha Avulsa",
            "enum": [
              "A",
              "C",
              "D",
              "E",
              "F",
              "M",
              "O",
              "P",
              "R",
              "T",
              "U",
              "V"
            ],
            "example": "A"
          },
          "sequencia": {
            "type": "integer",
            "description": "Sequência de lançamento, caso haja mais de um lançamento para o mesmo evento na mesma referência.",
            "example": 1
          },
          "valor": {
            "type": "number",
            "description": "Valor do movimento.",
            "example": 22.5
          },
          "indice": {
            "type": "number",
            "description": "Índice do movimento (utilizado para os eventos que não são valor).",
            "example": 7.5
          },
          "unidade": {
            "type": "string",
            "description": "Unidade do movimento. Os valores aceitos são:\n - D: Dias\n - H: Horas\n - Q: Quantidade\n - V: Valor",
            "enum": [
              "D",
              "H",
              "Q",
              "V"
            ],
            "example": "H"
          },
          "observacao": {
            "type": "string",
            "description": "Observação inserida do lançamento do movimento.",
            "example": "Movimento lançando para fins de correção."
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
