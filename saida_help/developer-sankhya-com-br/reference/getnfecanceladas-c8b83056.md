---
id: "https://developer.sankhya.com.br/reference/getnfecanceladas"
titulo: "Consultar Notas Fiscais Canceladas"
url: "https://developer.sankhya.com.br/reference/getnfecanceladas"
atualizado_em: "2026-10-22T11:38:21.000Z"
---

# Consultar Notas Fiscais Canceladas

Retorna lista paginada de Notas Fiscais modelo 55 (venda) que possuem cancelamento registrado.

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
      "name": "Vendas NF-e",
      "description": "Consulta Nota Fiscal Eletrônica modelo 55"
    }
  ],
  "paths": {
    "/v1/vendas/nfe/canceladas": {
      "get": {
        "tags": [
          "Vendas NF-e"
        ],
        "summary": "Consultar Notas Fiscais Canceladas",
        "description": "Retorna lista paginada de Notas Fiscais modelo 55 (venda) que possuem cancelamento registrado.",
        "operationId": "getNfeCanceladas",
        "security": [
          {
            "VendasNFeCanceladasBearer": []
          }
        ],
        "parameters": [
          {
            "$ref": "#/components/parameters/VendasNFeCanceladasPageParam"
          },
          {
            "$ref": "#/components/parameters/VendasNFeCanceladasModifiedSinceParam"
          },
          {
            "$ref": "#/components/parameters/VendasNFeCanceladasCodigoEmpresaParam"
          },
          {
            "$ref": "#/components/parameters/VendasNFeCanceladasCodigoNotaParam"
          },
          {
            "$ref": "#/components/parameters/NumeroNotaParam"
          },
          {
            "$ref": "#/components/parameters/VendasNFeCanceladasSerieNotaParam"
          },
          {
            "$ref": "#/components/parameters/VendasNFeCanceladasCodigoClienteParam"
          },
          {
            "$ref": "#/components/parameters/DataCancelamentoInicioParam"
          },
          {
            "$ref": "#/components/parameters/DataCancelamentoFinalParam"
          }
        ],
        "responses": {
          "200": {
            "description": "Sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RespostaPaginadaNfeCancelada"
                }
              }
            }
          },
          "400": {
            "description": "Erro na requisição.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/VendasNFeCanceladasRetornoErro"
                }
              }
            }
          },
          "401": {
            "description": "Não autorizado."
          },
          "500": {
            "description": "Erro interno."
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "RespostaPaginadaNfeCancelada": {
        "type": "object",
        "properties": {
          "metadados": {
            "$ref": "#/components/schemas/VendasNFeCanceladasMetadados"
          },
          "registros": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/RetornoNfeCancelada"
            }
          }
        }
      },
      "VendasNFeCanceladasMetadados": {
        "type": "object",
        "properties": {
          "paginaAtual": {
            "type": "integer",
            "example": 1
          },
          "totalRegistros": {
            "type": "integer",
            "example": 42
          }
        }
      },
      "RetornoNfeCancelada": {
        "type": "object",
        "properties": {
          "codigoNota": {
            "type": "integer",
            "format": "int64",
            "description": "Código interno da Nota Fiscal (NUNOTA).",
            "example": 12540
          },
          "numeroNota": {
            "type": "integer",
            "format": "int64",
            "description": "Número da Nota Fiscal (NUMNOTA).",
            "example": 254100
          },
          "serieNota": {
            "type": "string",
            "description": "Série da Nota Fiscal.",
            "example": "1"
          },
          "modelo": {
            "type": "string",
            "description": "Modelo do documento fiscal. Sempre `55` neste endpoint.",
            "example": "55"
          },
          "codigoEmpresa": {
            "type": "integer",
            "example": 1
          },
          "nomeEmpresa": {
            "type": "string",
            "example": "Sankhya Gestão de Negócios Matriz"
          },
          "codigoCliente": {
            "type": "integer",
            "example": 20500
          },
          "nomeCliente": {
            "type": "string",
            "example": "Tech Solutions Comercio e Servicos LTDA"
          },
          "chaveNFe": {
            "type": "string",
            "example": "35240612345678000199550010000125401002541002"
          },
          "status": {
            "type": "string",
            "description": "Status fixo indicando que a nota está cancelada.",
            "example": "cancelada"
          },
          "valorTotal": {
            "type": "number",
            "format": "double",
            "example": 5450
          },
          "dataEmissao": {
            "type": "string",
            "description": "Data de emissão/negociação da nota no formato DD-MM-YYYY.",
            "example": "15-06-2024"
          },
          "dataHoraAlteracao": {
            "type": "string",
            "format": "date-time",
            "description": "Data/hora da última alteração da nota.",
            "example": "2024-06-15T14:45:30Z"
          },
          "dataCancelamento": {
            "type": "string",
            "nullable": true,
            "description": "Data do cancelamento (TGFCAN.DTCANC) no formato DD/MM/YYYY. `null` se o registro de cancelamento não for encontrado.",
            "example": "16/06/2024"
          },
          "protocoloCancelamento": {
            "type": "string",
            "nullable": true,
            "description": "Número do protocolo de cancelamento na SEFAZ (TGFCAN.NUMPROTOCCAN).",
            "example": "135240008899774"
          },
          "motivoCancelamento": {
            "type": "string",
            "nullable": true,
            "description": "Justificativa informada para o cancelamento (TGFCAN.MOTCANCEL).",
            "example": "Erro de digitação no pedido"
          },
          "cnpjCpfEmitente": {
            "type": "string",
            "nullable": true,
            "description": "CNPJ/CPF da Empresa emitente (TSIEMP.CGC).",
            "example": "12345678000199"
          },
          "camposNaoMapeados": {
            "type": "object",
            "description": "Campos retornados pelo ERP sem mapeamento direto no contrato.",
            "additionalProperties": true
          },
          "camposAdicionais": {
            "type": "object",
            "description": "Campos adicionais (AD_) da entidade CabecalhoNota.",
            "additionalProperties": true
          }
        }
      },
      "VendasNFeCanceladasRetornoErro": {
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "example": "INVALID_REQUEST"
          },
          "message": {
            "type": "string",
            "example": "Erro na requisição"
          },
          "details": {
            "type": "string",
            "example": "O código da empresa não foi informado."
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
      },
      "VendasNFeCanceladasBearer": {
        "type": "apiKey",
        "name": "Authorization",
        "in": "header",
        "description": "Insira o token com o prefixo Bearer"
      }
    },
    "parameters": {
      "NumeroNotaParam": {
        "name": "numeroNota",
        "in": "query",
        "description": "Número da Nota Fiscal (NUMNOTA).",
        "required": false,
        "schema": {
          "type": "integer",
          "format": "int64",
          "example": 254100
        }
      },
      "VendasNFeCanceladasPageParam": {
        "name": "page",
        "in": "query",
        "description": "Número da página desejada.",
        "required": true,
        "schema": {
          "type": "integer",
          "format": "int64",
          "example": 1,
          "minimum": 1
        }
      },
      "VendasNFeCanceladasModifiedSinceParam": {
        "name": "modifiedSince",
        "in": "query",
        "description": "Retorna apenas registros alterados após esta data/hora (YYYY-MM-DDTHH:MM:SS).",
        "required": false,
        "schema": {
          "type": "string",
          "format": "date-time",
          "example": "2025-01-28T16:24:00Z"
        }
      },
      "VendasNFeCanceladasCodigoEmpresaParam": {
        "name": "codigoEmpresa",
        "in": "query",
        "description": "Código da Empresa.",
        "required": true,
        "schema": {
          "type": "integer",
          "example": 1
        }
      },
      "VendasNFeCanceladasCodigoNotaParam": {
        "name": "codigoNota",
        "in": "query",
        "description": "Código interno da Nota Fiscal (NUNOTA).",
        "required": false,
        "schema": {
          "type": "integer",
          "format": "int64",
          "example": 12540
        }
      },
      "VendasNFeCanceladasSerieNotaParam": {
        "name": "serieNota",
        "in": "query",
        "description": "Série da Nota Fiscal (SERIENOTA).",
        "required": false,
        "schema": {
          "type": "string",
          "example": "1"
        }
      },
      "VendasNFeCanceladasCodigoClienteParam": {
        "name": "codigoCliente",
        "in": "query",
        "description": "Código do Cliente (Parceiro).",
        "required": false,
        "schema": {
          "type": "integer"
        }
      },
      "DataCancelamentoInicioParam": {
        "name": "dataCancelamentoInicio",
        "in": "query",
        "description": "Data inicial de cancelamento no formato DD-MM-YYYY.",
        "required": false,
        "schema": {
          "type": "string",
          "example": "10-02-2025"
        }
      },
      "DataCancelamentoFinalParam": {
        "name": "dataCancelamentoFinal",
        "in": "query",
        "description": "Data final de cancelamento no formato DD-MM-YYYY.",
        "required": false,
        "schema": {
          "type": "string",
          "example": "20-02-2025"
        }
      }
    }
  }
}
```
