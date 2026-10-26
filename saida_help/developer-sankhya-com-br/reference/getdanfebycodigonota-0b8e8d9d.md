---
id: "https://developer.sankhya.com.br/reference/getdanfebycodigonota"
titulo: "Obter PDF do DANFE"
url: "https://developer.sankhya.com.br/reference/getdanfebycodigonota"
atualizado_em: "2026-08-20T20:02:33.000Z"
---

# Obter PDF do DANFE

Retorna o arquivo PDF do DANFE de uma NF-e modelo 55 autorizada ou encerrada. O identificador `{codigoNota}` pode ser o NUNOTA (ID interno) ou a Chave de Acesso da NF-e (44 dígitos numéricos). O documento é devolvido como stream binário (`application/pdf`) com cabeçalho `Content-Disposition: attachment`.

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
    "/v1/vendas/nfe/{codigoNota}/danfe": {
      "get": {
        "tags": [
          "Vendas NF-e"
        ],
        "summary": "Obter PDF do DANFE",
        "description": "Retorna o arquivo PDF do DANFE de uma NF-e modelo 55 autorizada ou encerrada. O identificador `{codigoNota}` pode ser o NUNOTA (ID interno) ou a Chave de Acesso da NF-e (44 dígitos numéricos). O documento é devolvido como stream binário (`application/pdf`) com cabeçalho `Content-Disposition: attachment`.",
        "operationId": "getDanfeByCodigoNota",
        "security": [
          {
            "VendasNFeDanfeBearer": []
          }
        ],
        "parameters": [
          {
            "name": "codigoNota",
            "in": "path",
            "description": "Identificador da nota: NUNOTA (ID interno) ou Chave de Acesso da NF-e (44 caracteres numéricos).",
            "required": true,
            "schema": {
              "type": "string",
              "example": "10688"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "PDF do DANFE gerado/recuperado com sucesso.",
            "headers": {
              "Content-Disposition": {
                "description": "Indica o nome do arquivo para download.",
                "schema": {
                  "type": "string",
                  "example": "attachment; filename=\"DANFE-10688.pdf\""
                }
              }
            },
            "content": {
              "application/pdf": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida (ex.: identificador malformado).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/VendasNFeDanfeRetornoErro"
                }
              }
            }
          },
          "401": {
            "description": "Não autorizado (token ausente ou sessão expirada)."
          },
          "404": {
            "description": "Nota fiscal não encontrada para o identificador informado.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/VendasNFeDanfeRetornoErro"
                },
                "example": {
                  "code": "RESOURCE_NOT_FOUND",
                  "message": "Recurso solicitado não foi encontrado!",
                  "details": "Nenhum registro da entidade CabecalhoNota com o identificador informado!"
                }
              }
            }
          },
          "409": {
            "description": "Documento não é uma NF-e modelo 55 autorizada ou encerrada.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/VendasNFeDanfeRetornoErro"
                },
                "example": {
                  "code": "CONFLICT",
                  "message": "Item já cadastrado!",
                  "details": "Documento informado nao e uma NF-e modelo 55 autorizada ou encerrada."
                }
              }
            }
          },
          "500": {
            "description": "Erro interno ao processar a geração do PDF.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/VendasNFeDanfeRetornoErro"
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
      "VendasNFeDanfeRetornoErro": {
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "example": "CONFLICT"
          },
          "message": {
            "type": "string",
            "example": "Item já cadastrado!"
          },
          "details": {
            "type": "string",
            "example": "Documento informado nao e uma NF-e modelo 55 autorizada ou encerrada."
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
      "VendasNFeDanfeBearer": {
        "type": "apiKey",
        "name": "Authorization",
        "in": "header",
        "description": "Insira o token com o prefixo Bearer"
      }
    }
  }
}
```
