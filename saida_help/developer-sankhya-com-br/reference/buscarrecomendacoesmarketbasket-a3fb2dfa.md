---
id: "https://developer.sankhya.com.br/reference/buscarrecomendacoesmarketbasket"
titulo: "Consulta por Itens da cesta"
url: "https://developer.sankhya.com.br/reference/buscarrecomendacoesmarketbasket"
atualizado_em: "2026-06-22T19:53:08.000Z"
---

# Consulta por Itens da cesta

Recebe a cesta de produtos do cliente via query params e retorna recomendações de produtos complementares ordenadas por relevância (score DESC, codigoProduto ASC). Produtos já presentes na cesta e produtos inativos são excluídos automaticamente dos resultados. O parâmetro `codigoProduto` pode ser repetido para informar múltiplos produtos; `controle` é alinhado por posição com `codigoProduto`.

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
    "/v1/vendas/recomendacoes/market-basket": {
      "get": {
        "tags": [
          "Sugestões de Vendas"
        ],
        "summary": "Consulta por Itens da cesta",
        "description": "Recebe a cesta de produtos do cliente via query params e retorna recomendações de produtos complementares ordenadas por relevância (score DESC, codigoProduto ASC). Produtos já presentes na cesta e produtos inativos são excluídos automaticamente dos resultados. O parâmetro `codigoProduto` pode ser repetido para informar múltiplos produtos; `controle` é alinhado por posição com `codigoProduto`.\n\nVersão mínima do SankhyaOm: **4.36**",
        "operationId": "buscarRecomendacoesMarketBasket",
        "parameters": [
          {
            "name": "codigoProduto",
            "in": "query",
            "required": true,
            "description": "Código(s) de produto presentes na cesta (TGFPRO.CODPROD). Repita o parâmetro para informar múltiplos produtos. Mínimo: 1. Máximo: 200.",
            "schema": {
              "type": "array",
              "minItems": 1,
              "maxItems": 200,
              "items": {
                "type": "integer",
                "format": "int64"
              }
            },
            "style": "form",
            "explode": true,
            "example": [
              1001,
              1002
            ]
          },
          {
            "name": "controle",
            "in": "query",
            "required": false,
            "description": "Controle de grade/lote (TGFPRO.CONTROLE), alinhado por posição com `codigoProduto`. Omita o parâmetro ou envie vazio para produtos sem controle de grade.",
            "schema": {
              "type": "array",
              "items": {
                "type": "string",
                "maxLength": 17
              }
            },
            "style": "form",
            "explode": true,
            "example": [
              "",
              "ABC123"
            ]
          },
          {
            "name": "maxSuggestions",
            "in": "query",
            "required": false,
            "description": "Número máximo de sugestões a retornar no total (limite global, aplicado antes da paginação). Padrão configurável via Dynamic Config; máximo: 50.",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 50,
              "default": 5
            },
            "example": 10
          },
          {
            "name": "pageSize",
            "in": "query",
            "required": false,
            "description": "Quantidade de itens por página. Padrão: 20. Máximo: 100.",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "default": 20
            },
            "example": 20
          },
          {
            "name": "pageNumber",
            "in": "query",
            "required": false,
            "description": "Número da página desejada (1-indexed). Padrão: 1.",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "default": 1
            },
            "example": 1
          },
          {
            "name": "codigoTipoOperacao",
            "in": "query",
            "required": false,
            "description": "Código do Tipo de Operação (TGFTOP.CODTOP). Quando informado, produtos sem estoque compatível com o TOP são despriorizados nos resultados.",
            "schema": {
              "type": "integer",
              "format": "int64"
            },
            "example": 100
          },
          {
            "name": "codigoNota",
            "in": "query",
            "required": false,
            "description": "Código da nota (TGFCAB.NUNOTA). Quando informado, os itens já presentes na nota são excluídos das recomendações.",
            "schema": {
              "type": "integer",
              "format": "int64"
            },
            "example": 77
          }
        ],
        "responses": {
          "200": {
            "description": "Operação bem sucedida",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retornoSugestoesVendas"
                },
                "example": {
                  "requestId": "550e8400-e29b-41d4-a716-446655440000",
                  "identificadorExecucao": 42,
                  "itensRecomendados": [
                    {
                      "codigoProduto": 2001,
                      "controle": " ",
                      "descricaoProduto": "PRODUTO RECOMENDADO A",
                      "tituloControle": "Grade",
                      "textoSugestao": "Frequentemente comprado junto",
                      "score": 3.8,
                      "rank": 1,
                      "produtosBase": [
                        {
                          "codigoProdutoBase": 1001,
                          "controleBase": " ",
                          "descricaoProdutoBase": "PRODUTO BASE X",
                          "score": 1.5
                        },
                        {
                          "codigoProdutoBase": 1002,
                          "controleBase": "ABC123",
                          "descricaoProdutoBase": "PRODUTO BASE Y",
                          "score": 2.3
                        }
                      ]
                    },
                    {
                      "codigoProduto": 2002,
                      "controle": " ",
                      "descricaoProduto": "PRODUTO RECOMENDADO B",
                      "tituloControle": "Grade",
                      "textoSugestao": "Frequentemente comprado junto",
                      "score": 1.2,
                      "rank": 2,
                      "produtosBase": [
                        {
                          "codigoProdutoBase": 1001,
                          "controleBase": " ",
                          "descricaoProdutoBase": "PRODUTO BASE X",
                          "score": 1.2
                        }
                      ]
                    }
                  ],
                  "pagination": {
                    "pageNumber": 1,
                    "pageSize": 20,
                    "totalItems": 2,
                    "totalPages": 1
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
      "retornoSugestoesVendas": {
        "type": "object",
        "properties": {
          "requestId": {
            "type": "string",
            "format": "uuid",
            "description": "Identificador único da requisição (para rastreabilidade em logs)",
            "example": "550e8400-e29b-41d4-a716-446655440000"
          },
          "identificadorExecucao": {
            "type": "integer",
            "format": "int64",
            "description": "Identificador da execução de pré-processamento que originou as regras utilizadas",
            "example": 42
          },
          "itensRecomendados": {
            "type": "array",
            "description": "Lista de produtos recomendados, ordenados por score DESC, codigoProduto ASC. Pode ser vazia quando não há regras ativas para a cesta.",
            "items": {
              "$ref": "#/components/schemas/itemRecomendadoMarketBasket"
            }
          },
          "pagination": {
            "$ref": "#/components/schemas/SugestoesVendaspaginacao"
          }
        }
      },
      "itemRecomendadoMarketBasket": {
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
            "example": "PRODUTO RECOMENDADO A"
          },
          "tituloControle": {
            "type": "string",
            "description": "Título da grade de controle (ex. 'Grade', 'Lote')",
            "example": "Grade"
          },
          "textoSugestao": {
            "type": "string",
            "description": "Texto de apresentação da sugestão ao usuário final",
            "example": "Frequentemente comprado junto"
          },
          "score": {
            "type": "number",
            "format": "double",
            "description": "Score agregado determinístico: soma dos scores de todas as regras ativadas pelos itens da cesta.",
            "example": 3.8
          },
          "rank": {
            "type": "integer",
            "description": "Posição global do item na lista ordenada (1-indexed, não relativo à página)",
            "example": 1
          },
          "produtosBase": {
            "type": "array",
            "description": "Lista de produtos da cesta que originaram esta recomendação",
            "items": {
              "$ref": "#/components/schemas/produtoBase"
            }
          }
        }
      },
      "produtoBase": {
        "type": "object",
        "description": "Produto antecedente da cesta que originou a sugestão",
        "properties": {
          "codigoProdutoBase": {
            "type": "integer",
            "format": "int64",
            "description": "Código do produto antecedente (da cesta do cliente)",
            "example": 1001
          },
          "controleBase": {
            "type": "string",
            "description": "Controle de grade/lote do produto antecedente. Valor ' ' (espaço) indica produto sem controle de grade.",
            "example": " "
          },
          "descricaoProdutoBase": {
            "type": "string",
            "description": "Descrição do produto antecedente (TGFPRO.DESCRPROD)",
            "example": "PRODUTO BASE X"
          },
          "score": {
            "type": "number",
            "format": "double",
            "description": "Contribuição individual deste antecedente para o score do produto recomendado",
            "example": 1.5
          }
        }
      },
      "SugestoesVendaspaginacao": {
        "type": "object",
        "properties": {
          "pageNumber": {
            "type": "integer",
            "description": "Número da página retornada (1-indexed)",
            "example": 1
          },
          "pageSize": {
            "type": "integer",
            "description": "Tamanho de página solicitado",
            "example": 20
          },
          "totalItems": {
            "type": "integer",
            "description": "Total de recomendações disponíveis (limitado por maxSuggestions)",
            "example": 2
          },
          "totalPages": {
            "type": "integer",
            "description": "Total de páginas (ceil(totalItems / pageSize))",
            "example": 1
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
