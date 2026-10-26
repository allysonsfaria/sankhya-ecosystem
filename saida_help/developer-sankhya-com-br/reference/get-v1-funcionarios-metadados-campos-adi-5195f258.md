---
id: "https://developer.sankhya.com.br/reference/get_v1-funcionarios-metadados-campos-adicionais"
titulo: "Listar metadados dos campos adicionais disponíveis para a Requisição de Admissão"
url: "https://developer.sankhya.com.br/reference/get_v1-funcionarios-metadados-campos-adicionais"
atualizado_em: "2026-08-18T12:42:37.000Z"
---

# Listar metadados dos campos adicionais disponíveis para a Requisição de Admissão

Este endpoint retorna o catálogo de campos adicionais (personalizados) cadastrados na entidade Funcionário e válidos para uso na Requisição de Admissão — nome, tipo de dado, obrigatoriedade, tamanho máximo e opções válidas (para campos de lista). Use este endpoint para descobrir programaticamente quais campos podem ser enviados no array `camposAdicionais` do endpoint `POST /v2/funcionarios/admissao`, e em qual formato, sem precisar consultar manualmente o Dicionário de Dados.

Apenas campos ativos e com prefixo `AD_` são retornados. Campos dos tipos Hora, Binário e Texto Longo (CLOB) — incluindo as variações Arquivo, Múltiplo Arquivo e Texto com Formatação HTML — não são suportados no fluxo de admissão e não aparecem na resposta.

Caso o cliente não possua nenhum campo adicional cadastrado, a resposta é `200` com `camposAdicionais` vazio e `totalCampos` igual a `0`.


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
    "/v1/funcionarios/metadados-campos-adicionais": {
      "get": {
        "summary": "Listar metadados dos campos adicionais disponíveis para a Requisição de Admissão",
        "tags": [
          "HCM Cadastros"
        ],
        "description": "Este endpoint retorna o catálogo de campos adicionais (personalizados) cadastrados na entidade Funcionário e válidos para uso na Requisição de Admissão — nome, tipo de dado, obrigatoriedade, tamanho máximo e opções válidas (para campos de lista). Use este endpoint para descobrir programaticamente quais campos podem ser enviados no array `camposAdicionais` do endpoint `POST /v2/funcionarios/admissao`, e em qual formato, sem precisar consultar manualmente o Dicionário de Dados.\n\nApenas campos ativos e com prefixo `AD_` são retornados. Campos dos tipos Hora, Binário e Texto Longo (CLOB) — incluindo as variações Arquivo, Múltiplo Arquivo e Texto com Formatação HTML — não são suportados no fluxo de admissão e não aparecem na resposta.\n\nCaso o cliente não possua nenhum campo adicional cadastrado, a resposta é `200` com `camposAdicionais` vazio e `totalCampos` igual a `0`.\n",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "required": false,
            "description": "Número da página de resultados. Começa em 1. Valores menores que 1 são tratados como 1.",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "default": 1
            },
            "example": 1
          },
          {
            "name": "pageSize",
            "in": "query",
            "required": false,
            "description": "Quantidade de campos adicionais retornados por página. Valores menores que 1 são tratados como o padrão (50).",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "default": 50
            },
            "example": 50
          }
        ],
        "responses": {
          "200": {
            "description": "Lista de campos adicionais retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MetadadosCamposAdicionaisResponse"
                }
              }
            }
          },
          "401": {
            "description": "Não autenticado. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "500": {
            "description": "Erro interno no servidor. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "retorno40X_50X": {
        "type": "object",
        "properties": {
          "fieldSet": {
            "type": "string"
          },
          "paginate": {
            "type": "string"
          },
          "mensagem": {
            "$ref": "#/components/schemas/error"
          }
        }
      },
      "error": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "string"
          },
          "descricao": {
            "type": "string"
          }
        }
      },
      "CampoAdicionalMetadado": {
        "title": "Metadado de Campo Adicional",
        "type": "object",
        "description": "Metadado de um campo adicional (personalizado) cadastrado na entidade Funcionário e disponível para uso na Requisição de Admissão. Retornado pelo endpoint `GET /v1/funcionarios/metadados-campos-adicionais`.",
        "properties": {
          "nomeCampo": {
            "type": "string",
            "description": "Nome exato do campo adicional, conforme cadastrado no Dicionário de Dados. É o valor a ser usado em `nomeCampo` no array `camposAdicionais` do `POST /v2/funcionarios/admissao`.",
            "example": "AD_APELIDO"
          },
          "descricao": {
            "type": "string",
            "description": "Descrição legível do campo, conforme cadastrada no Dicionário de Dados.",
            "example": "Apelido do funcionário"
          },
          "tipo": {
            "type": "string",
            "description": "Tipo de dado do campo e o formato esperado em `valor` ao enviar este campo no `POST /v2/funcionarios/admissao`:\n\n| Valor | Significado | Formato esperado em `valor` no POST |\n|---|---|---|\n| `TEXTO` | Texto | string |\n| `INTEIRO` | Número Inteiro | number, sem casas decimais |\n| `DECIMAL` | Número Decimal | number |\n| `DATA` | Data | string, formato ISO 8601 (YYYY-MM-DD) |\n| `DATA_HORA` | Data e Hora | string, formato ISO 8601 (YYYY-MM-DD) |\n| `CHECKBOX` | Checkbox | boolean |\n| `LISTA_OPCOES` | Lista de Opções | string, com o valor de uma das opções em `opcoes` (não a descrição) |\n",
            "enum": [
              "TEXTO",
              "INTEIRO",
              "DECIMAL",
              "DATA",
              "DATA_HORA",
              "CHECKBOX",
              "LISTA_OPCOES"
            ],
            "example": "TEXTO"
          },
          "obrigatorio": {
            "type": "boolean",
            "description": "Indica se o campo é obrigatório, conforme configurado no Dicionário de Dados. Atenção: o `POST /v2/funcionarios/admissao` não bloqueia a requisição por falta deste campo mesmo quando `obrigatorio` é `true` — a requisição é criada normalmente (200) e fica pendente para complementação posterior.",
            "example": false
          },
          "tamanhoMaximo": {
            "type": "integer",
            "description": "Tamanho máximo permitido para o valor do campo, conforme configurado no Dicionário de Dados.",
            "example": 50
          },
          "opcoes": {
            "type": "array",
            "description": "Lista de opções válidas para o campo. Presente apenas para campos do tipo Lista de Opções (`tipo` = `L`); array vazio para os demais tipos.",
            "items": {
              "type": "object",
              "properties": {
                "valor": {
                  "type": "string",
                  "description": "Valor da opção. É este valor (não a descrição) que deve ser enviado em `valor` no `POST /v2/funcionarios/admissao`.",
                  "example": "A"
                },
                "descricao": {
                  "type": "string",
                  "description": "Descrição legível da opção.",
                  "example": "Admitido"
                }
              }
            }
          }
        }
      },
      "MetadadosCamposAdicionaisResponse": {
        "title": "Metadados de Campos Adicionais",
        "type": "object",
        "properties": {
          "camposAdicionais": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CampoAdicionalMetadado"
            }
          },
          "totalCampos": {
            "type": "integer",
            "description": "Total de campos adicionais disponíveis, considerando todas as páginas (não apenas a página atual).",
            "example": 1
          },
          "page": {
            "type": "integer",
            "description": "Página atual retornada.",
            "example": 1
          },
          "pageSize": {
            "type": "integer",
            "description": "Quantidade de itens por página utilizada nesta resposta.",
            "example": 50
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
