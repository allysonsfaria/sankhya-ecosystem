---
id: "https://developer.sankhya.com.br/reference/get_v1-pessoal-funcionarios"
titulo: "Lista os funcionários modificados"
url: "https://developer.sankhya.com.br/reference/get_v1-pessoal-funcionarios"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Lista os funcionários modificados

Retorna uma lista de funcionários, com paginação, cadastrados no SankhyaOM. Permite filtrar por situação e/ou empresa. 

 Versão mínima do módulo pessoal: **5.76.0**

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
    "/v1/pessoal/funcionarios": {
      "get": {
        "summary": "Lista os funcionários modificados",
        "tags": [
          "HCM Funcionários"
        ],
        "description": "Retorna uma lista de funcionários, com paginação, cadastrados no SankhyaOM. Permite filtrar por situação e/ou empresa. \n\n Versão mínima do módulo pessoal: **5.76.0**",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "required": false,
            "schema": {
              "type": "integer",
              "minimum": 0
            },
            "description": "Página de resultados a ser exibida (paginação)."
          },
          {
            "name": "modifiedSince",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "format": "date-time",
              "example": "2023-01-01T00:00:00"
            },
            "description": "Data hora da ultima modificação. Quando este parametro é enviado, o serviço retorana apenas registros que tiveram modificação deste da data/hora enviada. Vale ressaltar que este recurso é condicionada a utilização do [Log de Alterações no SankhyaOm](https://developer.sankhya.com.br/reference/get_logalteracoestabelas) no ambiente do cliente. O formato deve ser o seguinte: AAAA-MM-DDTHH:MM:SS"
          },
          {
            "name": "situacao",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "enum": [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9"
              ],
              "example": "1"
            },
            "description": "Filtro opcional. Código da situação do funcionário: \n- 0 - Demitido \n- 1 - Atividade normal \n- 2 - Afastado sem remuneração \n- 3 - Afastado por acidente de trabalho \n- 4 - Afastado para serviço militar \n- 5 - Afastado por licença maternidade \n- 6 - Afastado por doença acima de 15 dias \n- 7 - Outros \n- 8 - Transferido \n- 9 - Aposentadoria por invalidez"
          },
          {
            "name": "codigoEmpresa",
            "in": "query",
            "required": false,
            "schema": {
              "type": "integer",
              "example": 2
            },
            "description": "Filtro opcional. Código da empresa para filtrar os funcionários."
          }
        ],
        "responses": {
          "200": {
            "description": "Lista de funcionários retornada com sucesso",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListaFuncionariosComPaginacao"
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Funcionariosretorno400"
                }
              }
            }
          },
          "500": {
            "description": "Erro interno no servidor"
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Funcionariosretorno400": {
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
      "CodigoFuncionario": {
        "type": "object",
        "properties": {
          "codigoEmpresa": {
            "type": "integer",
            "example": 1
          },
          "codigoFuncionario": {
            "type": "integer",
            "example": 33
          },
          "nome": {
            "type": "string",
            "example": "João da Silva"
          },
          "nomeMae": {
            "type": "string",
            "example": "Maria da Silva"
          },
          "email": {
            "type": "string",
            "example": "exemplo@exemplo.com.br"
          },
          "situacao": {
            "type": "string",
            "enum": [
              "0",
              "1",
              "2",
              "3",
              "4",
              "5",
              "6",
              "7",
              "8",
              "9"
            ],
            "description": "Situação do funcionário: \n- 0 - Demitido \n- 1 - Atividade normal \n- 2 - Afastado sem remuneração \n- 3 - Afastado por acidente de trabalho \n- 4 - Afastado para serviço militar \n- 5 - Afastado por licença maternidade \n- 6 - Afastado por doença acima de 15 dias \n- 7 - Outros \n- 8 - Transferido \n- 9 - Aposentadoria por invalidez",
            "example": "1"
          }
        }
      },
      "Pagination": {
        "type": "object",
        "properties": {
          "page": {
            "type": "string",
            "description": "Número da página atual"
          },
          "offset": {
            "type": "string",
            "description": "Quantidade de registros a serem desconsiderados no início. Geralmente usado para controle de navegação."
          },
          "total": {
            "type": "string",
            "description": "Quantidade total de registros encontrados."
          },
          "hasMore": {
            "type": "string",
            "description": "Indica se há mais páginas para serem consultadas"
          }
        }
      },
      "ListaFuncionariosComPaginacao": {
        "type": "object",
        "properties": {
          "codigos": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CodigoFuncionario"
            }
          },
          "pagination": {
            "$ref": "#/components/schemas/Pagination"
          }
        },
        "example": {
          "codigos": [
            {
              "codigoEmpresa": 1,
              "codigoFuncionario": 1,
              "nome": "Maria da Silva",
              "nomeMae": "Joana da Silva",
              "email": "exemplo@exemplo.com.br",
              "situacao": "1"
            },
            {
              "codigoEmpresa": 2,
              "codigoFuncionario": 2,
              "nome": "Joao Santos",
              "nomeMae": "Maria dos Santos",
              "email": "exemplo@exemplo.com.br",
              "situacao": "0"
            }
          ],
          "pagination": {
            "page": "0",
            "offset": "0",
            "total": "2",
            "hasMore": "false"
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
