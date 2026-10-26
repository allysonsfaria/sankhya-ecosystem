---
id: "https://developer.sankhya.com.br/reference/getnotasordemcarga"
titulo: "Consultar as Notas Fiscais de uma Ordem de Carga"
url: "https://developer.sankhya.com.br/reference/getnotasordemcarga"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Consultar as Notas Fiscais de uma Ordem de Carga

Retorna, de forma paginada, as Notas Fiscais e seus respectivos itens vinculados a uma Ordem de Carga específica.

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
      "name": "Logística",
      "description": "Cadastros básicos relacionados a motorista, transportadora, ordens de carga, veículos, no Sankhya Om"
    }
  ],
  "paths": {
    "/v1/logistica/empresas/{codigoEmpresa}/ordens-carga/{codigoOrdemCarga}/notas": {
      "get": {
        "tags": [
          "Logística"
        ],
        "summary": "Consultar as Notas Fiscais de uma Ordem de Carga",
        "description": "Retorna, de forma paginada, as Notas Fiscais e seus respectivos itens vinculados a uma Ordem de Carga específica.",
        "operationId": "getNotasOrdemCarga",
        "parameters": [
          {
            "name": "codigoEmpresa",
            "in": "path",
            "description": "Código da empresa à qual a Ordem de Carga pertence.",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int64"
            }
          },
          {
            "name": "codigoOrdemCarga",
            "in": "path",
            "description": "Código da Ordem de Carga cujas Notas Fiscais serão consultadas.",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int64"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Operação bem sucedida.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/notasOrdemCargaResponse"
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
          "404": {
            "description": "Ordem de Carga não encontrada."
          },
          "500": {
            "description": "Erro interno do servidor."
          }
        },
        "security": [
          {
            "Bearer": []
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "notasOrdemCargaResponse": {
        "type": "object",
        "description": "Retorno paginado das Notas Fiscais vinculadas a uma Ordem de Carga.",
        "properties": {
          "paginacao": {
            "$ref": "#/components/schemas/paginacaoNotasOrdemCarga"
          },
          "notasFiscais": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/notaFiscalOrdemCarga"
            }
          }
        }
      },
      "paginacaoNotasOrdemCarga": {
        "type": "object",
        "description": "Informações de paginação do retorno de Notas Fiscais da Ordem de Carga.",
        "properties": {
          "paginaAtual": {
            "type": "integer",
            "description": "Número da página atual.",
            "example": 1
          },
          "alvoNotasPorPagina": {
            "type": "integer",
            "description": "Quantidade alvo de Notas Fiscais por página.",
            "example": 50
          },
          "alvoItensPorPagina": {
            "type": "integer",
            "description": "Quantidade alvo de itens por página.",
            "example": 500
          },
          "totalNotasNestaPagina": {
            "type": "integer",
            "description": "Total de Notas Fiscais retornadas nesta página.",
            "example": 10
          },
          "totalItensNestaPagina": {
            "type": "integer",
            "description": "Total de itens retornados nesta página.",
            "example": 120
          },
          "totalPaginas": {
            "type": "integer",
            "description": "Total de páginas disponíveis para a consulta.",
            "example": 3
          },
          "totalNotasGeral": {
            "type": "integer",
            "description": "Total geral de Notas Fiscais vinculadas à Ordem de Carga.",
            "example": 28
          },
          "motivoQuebraPagina": {
            "type": "string",
            "description": "Motivo pelo qual a página foi encerrada (ex.: limite de notas ou itens atingido).",
            "example": "LIMITE_NOTAS"
          }
        }
      },
      "notaFiscalOrdemCarga": {
        "type": "object",
        "description": "Dados de uma Nota Fiscal vinculada à Ordem de Carga.",
        "properties": {
          "nunota": {
            "type": "integer",
            "description": "Número único da Nota Fiscal no ERP.",
            "example": 123456
          },
          "serie": {
            "type": "string",
            "description": "Série da Nota Fiscal.",
            "example": "1"
          },
          "dataNegocia": {
            "type": "string",
            "description": "Data de negociação da Nota Fiscal (formato DD/MM/AAAA).",
            "example": "12/09/2025"
          },
          "valor": {
            "type": "number",
            "format": "float",
            "description": "Valor total da Nota Fiscal.",
            "example": 15230.75
          },
          "peso": {
            "type": "number",
            "format": "float",
            "description": "Peso total da Nota Fiscal em Kg.",
            "example": 1250.5
          },
          "volumes": {
            "type": "integer",
            "description": "Quantidade de volumes da Nota Fiscal.",
            "example": 10
          },
          "m3": {
            "type": "string",
            "description": "Volume total em metros cúbicos (m³).",
            "example": "2.35"
          },
          "tipoOperacao": {
            "type": "string",
            "description": "Tipo de operação da Nota Fiscal.",
            "example": "VENDA"
          },
          "observacao": {
            "type": "string",
            "description": "Observações da Nota Fiscal.",
            "example": "Entrega urgente"
          },
          "tipoMovimento": {
            "type": "string",
            "description": "Tipo de movimento associado à Nota Fiscal.",
            "example": "S"
          },
          "parceiro": {
            "$ref": "#/components/schemas/parceiroNotaFiscal"
          },
          "itens": {
            "type": "array",
            "description": "Itens da Nota Fiscal.",
            "items": {
              "$ref": "#/components/schemas/itemNotaFiscal"
            }
          }
        }
      },
      "parceiroNotaFiscal": {
        "type": "object",
        "description": "Dados do parceiro (destinatário/remetente) da Nota Fiscal.",
        "properties": {
          "codigo": {
            "type": "integer",
            "description": "Código do parceiro no ERP.",
            "example": 1001
          },
          "nome": {
            "type": "string",
            "description": "Nome/razão social do parceiro.",
            "example": "Cliente Exemplo Ltda."
          },
          "documento": {
            "type": "string",
            "description": "CPF ou CNPJ do parceiro.",
            "example": "12.345.678/0001-90"
          },
          "endereco": {
            "type": "string",
            "description": "Logradouro do parceiro.",
            "example": "Rua das Flores, 123"
          },
          "complemento": {
            "type": "string",
            "description": "Complemento do endereço.",
            "example": "Sala 45"
          },
          "bairro": {
            "type": "string",
            "description": "Bairro do endereço.",
            "example": "Centro"
          },
          "cidade": {
            "type": "string",
            "description": "Cidade do endereço.",
            "example": "Uberlândia"
          },
          "estado": {
            "type": "string",
            "description": "Sigla da unidade federativa (UF).",
            "example": "MG"
          },
          "cep": {
            "type": "string",
            "description": "CEP do endereço.",
            "example": "38400-000"
          },
          "latitude": {
            "type": "number",
            "format": "double",
            "description": "Latitude do endereço.",
            "example": -18.9186
          },
          "longitude": {
            "type": "number",
            "format": "double",
            "description": "Longitude do endereço.",
            "example": -48.2772
          }
        }
      },
      "itemNotaFiscal": {
        "type": "object",
        "description": "Dados de um item da Nota Fiscal.",
        "properties": {
          "sequencia": {
            "type": "integer",
            "description": "Número de sequência do item na Nota Fiscal.",
            "example": 1
          },
          "codigoProduto": {
            "type": "integer",
            "description": "Código do produto.",
            "example": 5001
          },
          "descricaoProduto": {
            "type": "string",
            "description": "Descrição do produto.",
            "example": "Caixa Papelão 30x20x15"
          },
          "quantidade": {
            "type": "number",
            "format": "float",
            "description": "Quantidade do produto no item.",
            "example": 100
          },
          "valorUnitario": {
            "type": "number",
            "format": "float",
            "description": "Valor unitário do produto.",
            "example": 12.5
          },
          "valorTotal": {
            "type": "number",
            "format": "float",
            "description": "Valor total do item (quantidade x valor unitário).",
            "example": 1250
          },
          "unidade": {
            "type": "string",
            "description": "Unidade de medida do item.",
            "example": "UN"
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
