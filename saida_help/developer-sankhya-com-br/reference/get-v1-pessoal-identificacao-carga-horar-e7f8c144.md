---
id: "https://developer.sankhya.com.br/reference/get_v1-pessoal-identificacao-carga-horaria-codigocargahoraria"
titulo: "Identificação Carga Horária Específica"
url: "https://developer.sankhya.com.br/reference/get_v1-pessoal-identificacao-carga-horaria-codigocargahoraria"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Identificação Carga Horária Específica

Retorna um Cargo específico com base no parâmetro enviado na requisição. 

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
    "/v1/pessoal/identificacao-carga-horaria/{codigoCargaHoraria}": {
      "get": {
        "tags": [
          "HCM Cadastros"
        ],
        "summary": "Identificação Carga Horária Específica",
        "description": "Retorna um Cargo específico com base no parâmetro enviado na requisição. \n\n Versão mínima do módulo pessoal: **5.53.0**",
        "parameters": [
          {
            "name": "codigoCargaHoraria",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código da Carga Horária para retorno"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados da Carga Horária retornado com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/IdentificacaoCargaHoraria"
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
      "IdentificacaoCargaHoraria": {
        "type": "object",
        "properties": {
          "codigoCargaHoraria": {
            "type": "integer",
            "description": "Código atribuído à carga horária.",
            "example": 101
          },
          "descricao": {
            "type": "string",
            "description": "Descrição da Carga Horária.",
            "example": "Carga Horária Padrão"
          },
          "tipo": {
            "type": "string",
            "description": "Tipo de Carga Horária:\n - J: Jornada de Trabalho\n - C: Carga Horária",
            "enum": [
              "J",
              "C"
            ],
            "example": "J"
          },
          "tipoJornada": {
            "type": "integer",
            "description": "Tipo de Jornada:\n - 2: Jornada 12x36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso)\n - 3: Jornada com horário diário fixo e folga variável\n - 4: Jornada com horário diário fixo e folga fixa (no domingo)\n - 5: Jornada com horário diário fixo e folga fixa (exceto no domingo)\n - 6: Jornada com horário diário fixo e folga fixa (em outro dia da semana),com folga adicional periódica no domingo\n - 7: Turno ininterrupto de revezamento\n - 9: Demais tipos de jornada",
            "enum": [
              2,
              3,
              3,
              5,
              6,
              7,
              9
            ],
            "example": 2
          },
          "ativo": {
            "type": "boolean",
            "description": "Indica se o cadastro está ativo.",
            "example": true
          },
          "escalonar": {
            "type": "boolean",
            "description": "Indica se a carga horária é por escala.",
            "example": false
          },
          "diasTrabalho": {
            "type": "integer",
            "description": "Determina quantos dias serão trabalhados nessa escala. Campo obrigatório quando a carga horária for por escala.",
            "example": 5
          },
          "diasFolga": {
            "type": "integer",
            "description": "Determina quantos dias serão de folga nessa escala. Campo obrigatório quando a carga horária for por escala.",
            "example": 2
          },
          "quantidadeTurno": {
            "type": "integer",
            "description": "Indica a quantidade de turnos da escala. Campo obrigatório quando a carga horária for por escala.",
            "example": 3
          },
          "dataAlteracao": {
            "type": "string",
            "description": "Data da última alteração.",
            "example": "08/08/2025 14:00:00"
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
