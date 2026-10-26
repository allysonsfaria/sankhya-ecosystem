---
id: "https://developer.sankhya.com.br/reference/postordemcarga"
titulo: "Incluir uma nova Ordem de Carga"
url: "https://developer.sankhya.com.br/reference/postordemcarga"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Incluir uma nova Ordem de Carga

Permite incluir uma nova Ordem de Carga no ERP.

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
    "/v1/logistica/ordens-carga": {
      "post": {
        "tags": [
          "Logística"
        ],
        "summary": "Incluir uma nova Ordem de Carga",
        "description": "Permite incluir uma nova Ordem de Carga no ERP.",
        "operationId": "postOrdemCarga",
        "requestBody": {
          "description": "Dados da Ordem de Carga para inclusão.",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ordemCargaPost"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Operação bem sucedida. Retorna a Ordem de Carga criada.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ordemCargaResponse"
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
          "403": {
            "description": "Acesso proibido."
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
      "ordemCarga": {
        "type": "object",
        "description": "Representa uma Ordem de Carga no sistema.",
        "properties": {
          "codigoOrdemCarga": {
            "type": "integer",
            "description": "Código de identificação da Ordem de Carga.",
            "example": 901
          },
          "codigoEmpresa": {
            "type": "integer",
            "description": "Código da empresa da ordem de carga.",
            "example": 1
          },
          "codigoRoteirizador": {
            "type": "string",
            "description": "Id da rota planejada na ferramenta de roteirização.",
            "example": 123456
          },
          "nomeEmpresa": {
            "type": "string",
            "description": "Nome da empresa da ordem de carga.",
            "example": "Empresa Matriz Ltda.",
            "readOnly": true
          },
          "dataInicio": {
            "type": "string",
            "description": "Data de início da operação.",
            "example": "12/09/2025"
          },
          "dataPrevistaSaida": {
            "type": "string",
            "description": "Data prevista para a saída do veículo.",
            "example": "13/09/2025"
          },
          "horaSaida": {
            "type": "string",
            "description": "Hora prevista para a saída.",
            "example": "14:30"
          },
          "codigoVeiculo": {
            "type": "integer",
            "description": "Código do veículo alocado para a carga.",
            "example": 205
          },
          "codigoRegiao": {
            "type": "integer",
            "description": "Código da região de destino da ordem de carga.",
            "example": 10
          },
          "nomeRegiao": {
            "type": "string",
            "description": "Nome da região de destino.",
            "example": "TRIÂNGULO MINEIRO",
            "readOnly": true
          },
          "codigoTransportadora": {
            "type": "integer",
            "description": "Código do parceiro Transportadora.",
            "example": 432
          },
          "nomeTransportadora": {
            "type": "string",
            "description": "Nome da transportadora.",
            "example": "Transportadora Rápida S.A.",
            "readOnly": true
          },
          "codigoMotorista": {
            "type": "integer",
            "description": "Código do parceiro Motorista.",
            "example": 8115
          },
          "nomeMotorista": {
            "type": "string",
            "description": "Nome do motorista.",
            "example": "José da Silva",
            "readOnly": true
          },
          "roteiro": {
            "type": "string",
            "description": "Descrição detalhada do roteiro a ser seguido.",
            "example": "Seguir pela BR-050 até Uberlândia, depois BR-365..."
          },
          "tipo": {
            "type": "integer",
            "description": "Define o tipo da Ordem de Carga. 1: Ambos, 2: Entrada, 3: Saída.",
            "enum": [
              1,
              2,
              3
            ],
            "example": 3
          },
          "situacao": {
            "type": "integer",
            "description": "Situação atual da Ordem de Carga. 1: Aberta, 2: Fechada.",
            "enum": [
              1,
              2
            ],
            "example": 1
          },
          "pesoMaximo": {
            "type": "number",
            "format": "float",
            "description": "Peso máximo suportado pela carga em Kg.",
            "example": 25000.5
          },
          "metroCubicoMaximo": {
            "type": "number",
            "format": "float",
            "description": "Volume máximo suportado pela carga em m³.",
            "example": 88.7
          },
          "observacoes": {
            "type": "string",
            "description": "Observações gerais sobre a ordem de carga.",
            "example": "Carga frágil, manusear com cuidado."
          }
        }
      },
      "ordemCargaPost": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ordemCarga"
          },
          {
            "type": "object",
            "required": [
              "codigoEmpresa",
              "tipo",
              "situacao"
            ]
          }
        ]
      },
      "ordemCargaResponse": {
        "allOf": [
          {
            "type": "object",
            "properties": {
              "ordemCarga": {
                "$ref": "#/components/schemas/ordemCarga"
              }
            }
          }
        ]
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
