---
id: "https://developer.sankhya.com.br/reference/get_v1-pessoal-historicos-ocorrencia-codigohistoricoocorrencia"
titulo: "Histórico ocorrência espécífico"
url: "https://developer.sankhya.com.br/reference/get_v1-pessoal-historicos-ocorrencia-codigohistoricoocorrencia"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Histórico ocorrência espécífico

Retorna um Histórico ocorrência específico com base no parâmetro enviado na requisição. 

 Versão mínima do módulo pessoal: **5.50.0**

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
    "/v1/pessoal/historicos-ocorrencia/{codigoHistoricoOcorrencia}": {
      "get": {
        "tags": [
          "HCM Cadastros"
        ],
        "summary": "Histórico ocorrência espécífico",
        "description": "Retorna um Histórico ocorrência específico com base no parâmetro enviado na requisição. \n\n Versão mínima do módulo pessoal: **5.50.0**",
        "parameters": [
          {
            "name": "codigoHistoricoOcorrencia",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código do histórico da ocorrência"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados do Histórico ocorrência retornado com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HistoricosOcorrencia"
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Historico_Ocorrenciaretorno400"
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
      "Historico_Ocorrenciaretorno400": {
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
      "HistoricosOcorrencia": {
        "type": "object",
        "properties": {
          "codigoHistoricoOcorrencia": {
            "type": "integer",
            "description": "Código do histórico de ocorrência",
            "example": 101
          },
          "descricao": {
            "type": "string",
            "description": "Descrição do histórico de ocorrência",
            "example": "LICENÇA GESTANTE."
          },
          "tipoAfastamento": {
            "type": "string",
            "description": "Tipo de afastamento:\n - A: Acidente de trabalho\n  - B: Bonificado\n - C: Compensação de dias\n - D: Doença acima de dias\n - E: Licença Alistamento Eleitoral\n - F: Férias\n - G: Licença Gestante\n - H: Trabalhado\n - I: Atestado em horas\n - J: Licença comparecimento em Juízo\n - K: Licença remunerada\n - L: Faltas\n - M: Serviço militar\n - N: Não é afastamento\n - O: Licença Óbito\n - P: Licença Paternidade\n - Q: Compensação em Horas\n - R: Licença Representante Sindical\n - S: Sem remuneração\n - T: Atestado em dias\n - U: Licença Doação de Sangue\n - V: Licença Vestibular\n - X: Faltas em Horas\n - Y: Aposentadoria por Invalidez\n - W: Licença Gestante Cidadã\n - Z: Licença Casamento\n - 1: Licença Amamentação\n - 2: Cárcere\n - 3: Licença comparecimento em Juízo em Horas\n - 4: Reintegração\n - 5: Licença Paternidade Cidadã\n - 6: Licença Óbito em horas\n - 7: Licença Mandato Sindical\n - 8: Convocação Coletiva/Débito Horas\n - 9: Atestado em dias Parte Empresa",
            "example": "A"
          },
          "codigoMotivoAfastamento": {
            "type": "integer",
            "description": "Traz o motivo do afastamento de acordo com a tabela 18 - Motivos de Afastamento, versão S-1.3 do eSocial",
            "example": 1
          },
          "descricaoMotivoAfastamento": {
            "type": "string",
            "description": "Motivo do afastamento",
            "example": "Licença Gestante"
          },
          "absenteismo": {
            "type": "boolean",
            "description": "Indica se ocorrência é considerada como absenteísmo",
            "example": true
          },
          "abateAviso": {
            "type": "boolean",
            "description": "Indica se ocorrência deve ser retirada na contagem do tempo de serviço para o aviso prévio",
            "example": false
          },
          "indenizaEstabilidade": {
            "type": "boolean",
            "description": "Indica se essa ocorrência gera indenização por estabilidade",
            "example": false
          },
          "qtdMesesEstabilidade": {
            "type": "integer",
            "description": "Quantidade de meses de estabilidade para essa ocorrência",
            "example": false
          },
          "dataAlteracao": {
            "type": "string",
            "description": "Data da última alteração do cadastro",
            "example": "04/07/2024 09:02:10"
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
