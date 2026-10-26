---
id: "https://developer.sankhya.com.br/reference/get_v1-veiculos-codigoveiculo"
titulo: "Veículo específico"
url: "https://developer.sankhya.com.br/reference/get_v1-veiculos-codigoveiculo"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Veículo específico

Retorna um Veículo específico com base no parâmetro enviado na requisição.

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
      "name": "Cadastros Básicos",
      "description": "Cadastros Básicos disponíveis no SankhyaOM"
    }
  ],
  "paths": {
    "/v1/veiculos/{codigoVeiculo}": {
      "get": {
        "tags": [
          "Cadastros Básicos"
        ],
        "summary": "Veículo específico",
        "description": "Retorna um Veículo específico com base no parâmetro enviado na requisição.",
        "parameters": [
          {
            "name": "codigoVeiculo",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código do Veículo para retorno"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados do Veículo retornados com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Veiculo"
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
      "Veiculo": {
        "type": "object",
        "properties": {
          "codigoVeiculo": {
            "type": "integer",
            "description": "Código do veículo",
            "example": 1234
          },
          "placa": {
            "type": "string",
            "description": "Placa do veículo",
            "example": "ABC1D23"
          },
          "marcaModelo": {
            "type": "string",
            "description": "Marca e modelo do veículo",
            "example": "Ford Focus"
          },
          "numeroMotor": {
            "type": "string",
            "description": "Número do motor",
            "example": "XYZ123456789"
          },
          "renavam": {
            "type": "string",
            "description": "Número do RENAVAM",
            "example": 12345678900
          },
          "chassis": {
            "type": "string",
            "description": "Número do chassi",
            "example": "9BWZZZ377VT004251"
          },
          "categoria": {
            "type": "string",
            "description": "Categoria do veículo",
            "example": "Caminhão"
          },
          "pesoMaximo": {
            "type": "number",
            "format": "float",
            "description": "Peso máximo suportado pelo veículo",
            "example": 2500.5
          },
          "veiculoProprio": {
            "type": "boolean",
            "description": "Indica se o veículo pertence à empresa",
            "example": true
          },
          "combustivel": {
            "type": "integer",
            "description": "Tipo de combustível:\n1 - Álcool  \n2 - Gasolina/Elétrico  \n3 - Gás Metano  \n4 - Diesel  \n5 - Elétrico/Fonte Interna  \n6 - Álcool/Gasolina  \n7 - Gasolina  \n8 - Elétrico/Fonte Externa  \n9 - Gasolina/Gás Natural Combustível  \n10 - Álcool/Gás Natural Combustível  \n11 - Diesel/Gás Natural Combustível  \n12 - Álcool/Gás Natural Veicular  \n13 - Gasolina/Gás Natural Veicular  \n14 - Gás Natural Veicular  \n15 - Vide/Campo/Observação  \n16 - Diesel/Gás Natural Veicular  \n17 - Gasolina/Álcool/Gás Natural Veicular  \n18 - Gasogênio\n",
            "enum": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18
            ],
            "example": 7
          },
          "cor": {
            "type": "string",
            "description": "Cor do veículo",
            "example": "Preto"
          },
          "anoFabricacao": {
            "type": "integer",
            "description": "Ano de fabricação do veículo",
            "example": 2022
          },
          "anoModelo": {
            "type": "integer",
            "description": "Ano do modelo do veículo",
            "example": 2023
          },
          "codigoCidade": {
            "type": "integer",
            "description": "Código da cidade de emplacamento",
            "example": 3543402
          },
          "nomeCidade": {
            "type": "string",
            "description": "Nome da cidade de emplacamento",
            "example": "Uberlândia"
          },
          "codigoFuncionario": {
            "type": "integer",
            "description": "Código do funcionário",
            "example": 5678
          },
          "nomeFuncionario": {
            "type": "string",
            "description": "Nome do funcionário",
            "example": "Mário Regis"
          },
          "codigoMotorista": {
            "type": "integer",
            "description": "Código do motorista",
            "example": 4321
          },
          "nomeMotorista": {
            "type": "string",
            "description": "Nome do motorista",
            "example": "Roberto Magalhães"
          },
          "codigoParceiro": {
            "type": "integer",
            "description": "Código do parceiro",
            "example": 1111
          },
          "nomeParceiro": {
            "type": "string",
            "description": "Nome do parceiro",
            "example": "José da Silva"
          },
          "ativo": {
            "type": "boolean",
            "description": "Indica se o veículo está ativo",
            "example": true
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
