---
id: "https://developer.sankhya.com.br/reference/get_v1-pessoal-locais-ponto-codigolocalponto"
titulo: "Local De Trabalho específico"
url: "https://developer.sankhya.com.br/reference/get_v1-pessoal-locais-ponto-codigolocalponto"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Local De Trabalho específico

Retorna um Local De Trabalho específico com base no parâmetro enviado na requisição. 

 Versão mínima do módulo pessoal: **5.48.0**

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
    "/v1/pessoal/locais-ponto/{codigoLocalPonto}": {
      "get": {
        "tags": [
          "HCM Cadastros"
        ],
        "summary": "Local De Trabalho específico",
        "description": "Retorna um Local De Trabalho específico com base no parâmetro enviado na requisição. \n\n Versão mínima do módulo pessoal: **5.48.0**",
        "parameters": [
          {
            "name": "codigoLocalPonto",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código do Local De Trabalho para retorno"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados do Local De Trabalho retornado com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/LocalPonto"
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Local_Ponto_Pessoal_Maisretorno400"
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
      "Local_Ponto_Pessoal_Maisretorno400": {
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
      "LocalPonto": {
        "type": "object",
        "properties": {
          "codigoLocalTrabalho": {
            "type": "integer",
            "description": "Código do local de trabalho",
            "example": 101
          },
          "nome": {
            "type": "string",
            "description": "Nome do local de trabalho",
            "example": "Local De Trabalho pessoal."
          },
          "controlePonto": {
            "type": "boolean",
            "description": "Indica se há controle de ponto local. Ao ser marcada essa opção, é considerado o endereço informado.",
            "example": true
          },
          "empresa": {
            "type": "object",
            "description": "Informações da empresa associada ao local de trabalho.",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código da empresa.",
                "example": 4
              },
              "descricao": {
                "type": "string",
                "description": "Nome da empresa",
                "example": "TRANSFAST Transportadora ."
              }
            }
          },
          "departamento": {
            "type": "object",
            "description": "Informações do departamento associado ao local de trabalho.",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código do departamento.",
                "example": 252515
              },
              "descricao": {
                "type": "string",
                "description": "Nome do departamento.",
                "example": "Departamento pessoal."
              }
            }
          },
          "endereco": {
            "type": "object",
            "description": "Informações de endereço do local de trabalho.",
            "properties": {
              "cep": {
                "type": "string",
                "description": "CEP do local de trabalho.",
                "example": "60025-000"
              },
              "codigo": {
                "type": "integer",
                "description": "Código do endereço.",
                "example": 252515
              },
              "descricao": {
                "type": "string",
                "description": "Descrição atribuída ao endereço",
                "example": "Rua andorinhas."
              },
              "codigoBairro": {
                "type": "integer",
                "description": "Código do Bairro",
                "example": 200
              },
              "nomeBairro": {
                "type": "string",
                "description": "Nome do bairro",
                "example": "Bairro Andorinhas"
              },
              "codigoCidade": {
                "type": "integer",
                "description": "Código da cidade",
                "example": 200
              },
              "nomeCidade": {
                "type": "string",
                "description": "Nome da cidade",
                "example": "São Paulo"
              },
              "codigoPais": {
                "type": "integer",
                "description": "Código do país",
                "example": 200
              },
              "nomePais": {
                "type": "string",
                "description": "Nome do país",
                "example": "Brasil"
              },
              "uf": {
                "type": "string",
                "description": "Unidade federativa do endereço",
                "example": "SP"
              },
              "complemento": {
                "type": "string",
                "description": "Complemento do endereço",
                "example": "apto 906"
              },
              "numero": {
                "type": "string",
                "description": "Número do logradouro",
                "example": "5"
              }
            }
          },
          "dataAlteracao": {
            "type": "string",
            "description": "Data da última alteração no cadastro",
            "example": "10/03/2022 16:03:12"
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
