---
id: "https://developer.sankhya.com.br/reference/buscarrecomendacoesperfilcliente"
titulo: "Consulta por Perfil do cliente"
url: "https://developer.sankhya.com.br/reference/buscarrecomendacoesperfilcliente"
atualizado_em: "2026-06-22T19:53:08.000Z"
---

# Consulta por Perfil do cliente

Recebe o código do parceiro via query param e retorna recomendações de produtos baseadas no perfil de compra do agrupador ao qual o parceiro pertence. Quando não há agrupador vigente ou não há ranking calculado, retorna `temRecomendacao` false com o motivo da ausência.

Versão mínima do SankhyaOm: **4.36**

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
      "name": "Sugestões de Vendas",
      "description": "Recomendações de produtos complementares baseadas em análise de cesta de itens"
    }
  ],
  "paths": {
    "/v1/vendas/recomendacoes/perfil-cliente": {
      "get": {
        "tags": [
          "Sugestões de Vendas"
        ],
        "summary": "Consulta por Perfil do cliente",
        "description": "Recebe o código do parceiro via query param e retorna recomendações de produtos baseadas no perfil de compra do agrupador ao qual o parceiro pertence. Quando não há agrupador vigente ou não há ranking calculado, retorna `temRecomendacao` false com o motivo da ausência.\n\nVersão mínima do SankhyaOm: **4.36**",
        "operationId": "buscarRecomendacoesPerfilCliente",
        "parameters": [
          {
            "name": "codigoParceiro",
            "in": "query",
            "required": true,
            "description": "Código do parceiro (TGFPAR.CODPARC)",
            "schema": {
              "type": "integer",
              "format": "int64"
            },
            "example": 123
          }
        ],
        "responses": {
          "200": {
            "description": "Operação bem sucedida",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retornoPerfilCliente"
                },
                "examples": {
                  "comRecomendacao": {
                    "summary": "Parceiro com recomendações disponíveis",
                    "value": {
                      "codigoParceiro": 123,
                      "nivelAgrupador": "CNAE",
                      "valorAgrupador": "4711-3/02",
                      "identificadorExecucao": 42,
                      "temRecomendacao": true,
                      "motivoAusencia": null,
                      "itensRecomendados": [
                        {
                          "codigoProduto": 2001,
                          "controle": " ",
                          "descricaoProduto": "PRODUTO RECOMENDADO",
                          "rank": 1,
                          "frequencia": 0.85,
                          "cobertura": 0.6,
                          "volume": 120
                        }
                      ]
                    }
                  },
                  "semRecomendacao": {
                    "summary": "Parceiro sem agrupador vigente",
                    "value": {
                      "codigoParceiro": 999,
                      "nivelAgrupador": null,
                      "valorAgrupador": null,
                      "identificadorExecucao": null,
                      "temRecomendacao": false,
                      "motivoAusencia": "PARCEIRO_SEM_AGRUPADOR",
                      "itensRecomendados": []
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Informações Inválidas. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SugestoesVendasretorno400"
                }
              }
            }
          },
          "401": {
            "description": "Não autenticado. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "403": {
            "description": "Autenticação inválida. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "500": {
            "description": "Erro interno no servidor. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
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
      "SugestoesVendasretorno400": {
        "type": "object",
        "properties": {
          "statusCode": {
            "type": "integer",
            "format": "int32",
            "example": 400
          },
          "error": {
            "type": "string"
          },
          "mensagem": {
            "$ref": "#/components/schemas/SugestoesVendasretornoErro"
          }
        }
      },
      "SugestoesVendasretornoErro": {
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "example": "INVALID_REQUEST"
          },
          "message": {
            "type": "string",
            "example": "Ocorreu algum erro inesperado!"
          },
          "details": {
            "type": "string",
            "example": "O parâmetro 'codigoProduto' é obrigatório e deve conter ao menos um valor."
          },
          "help": {
            "type": "string",
            "example": "https://api.sankhya.com.br/api/docs/?ERROR_CODE=INVALID_REQUEST"
          }
        }
      },
      "retornoPerfilCliente": {
        "type": "object",
        "properties": {
          "codigoParceiro": {
            "type": "integer",
            "format": "int64",
            "description": "Código do parceiro consultado",
            "example": 123
          },
          "nivelAgrupador": {
            "type": "string",
            "nullable": true,
            "description": "Nível do agrupador vigente do parceiro (ex. 'CNAE', 'SEGMENTO')",
            "example": "CNAE"
          },
          "valorAgrupador": {
            "type": "string",
            "nullable": true,
            "description": "Valor do agrupador vigente (ex. o código CNAE do parceiro)",
            "example": "4711-3/02"
          },
          "identificadorExecucao": {
            "type": "integer",
            "format": "int64",
            "nullable": true,
            "description": "Identificador da execução de pré-processamento que originou o ranking utilizado",
            "example": 42
          },
          "temRecomendacao": {
            "type": "boolean",
            "description": "Indica se há recomendações disponíveis para o parceiro",
            "example": true
          },
          "motivoAusencia": {
            "type": "string",
            "nullable": true,
            "description": "Motivo pelo qual não há recomendações. Presente apenas quando `temRecomendacao` é false. Valores possíveis: PARCEIRO_SEM_AGRUPADOR, SEM_RANKING_VIGENTE.",
            "example": null
          },
          "itensRecomendados": {
            "type": "array",
            "description": "Lista de produtos recomendados para o perfil do parceiro, ordenados por rank ASC",
            "items": {
              "$ref": "#/components/schemas/itemRecomendadoPerfilCliente"
            }
          }
        }
      },
      "itemRecomendadoPerfilCliente": {
        "type": "object",
        "properties": {
          "codigoProduto": {
            "type": "integer",
            "format": "int64",
            "description": "Código do produto recomendado (TGFPRO.CODPROD)",
            "example": 2001
          },
          "controle": {
            "type": "string",
            "description": "Controle de grade/lote do produto recomendado. Valor ' ' (espaço) indica produto sem controle de grade.",
            "example": " "
          },
          "descricaoProduto": {
            "type": "string",
            "description": "Descrição do produto recomendado (TGFPRO.DESCRPROD)",
            "example": "PRODUTO RECOMENDADO"
          },
          "rank": {
            "type": "integer",
            "description": "Posição do produto no ranking do perfil (1-indexed)",
            "example": 1
          },
          "frequencia": {
            "type": "number",
            "format": "double",
            "description": "Frequência relativa de compra do produto pelo perfil (0.0 a 1.0). Proporção de clientes do agrupador que compraram este produto.",
            "example": 0.85
          },
          "cobertura": {
            "type": "number",
            "format": "double",
            "description": "Cobertura do produto no perfil (0.0 a 1.0). Proporção do volume total do perfil representada por este produto.",
            "example": 0.6
          },
          "volume": {
            "type": "number",
            "format": "double",
            "description": "Volume total comprado do produto pelo perfil no período de análise",
            "example": 120
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
