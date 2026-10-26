---
id: "https://developer.sankhya.com.br/reference/get_v1-pessoal-empresas-codigoempresa"
titulo: "Empresa específica"
url: "https://developer.sankhya.com.br/reference/get_v1-pessoal-empresas-codigoempresa"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Empresa específica

Retorna uma empresa específica com base no parâmetro enviado na requisição.  

 Versão mínima do módulo pessoal: **5.54.0**

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
    "/v1/pessoal/empresas/{codigoEmpresa}": {
      "get": {
        "tags": [
          "HCM Cadastros"
        ],
        "summary": "Empresa específica",
        "description": "Retorna uma empresa específica com base no parâmetro enviado na requisição.  \n\n Versão mínima do módulo pessoal: **5.54.0**",
        "parameters": [
          {
            "name": "codigoEmpresa",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código da Empresa para retorno"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados da Empresa retornado com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/EmpresasEmpresa"
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Empresasretorno400"
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
      "Empresasretorno400": {
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
      "EmpresasEmpresa": {
        "type": "object",
        "properties": {
          "codigoEmpresa": {
            "type": "integer",
            "description": "Código da empresa",
            "example": 1
          },
          "nome": {
            "type": "string",
            "description": "Nome da empresa",
            "example": "SANKHYA Gestão de Negócios."
          },
          "cnpj": {
            "type": "string",
            "description": "Número do Cadastro Nacional da Pessoa Jurídica.",
            "example": "12345678000190"
          },
          "razaoSocial": {
            "type": "string",
            "description": "Nome legal completo da empresa.",
            "example": "Empresa Exemplo Ltda."
          },
          "endereco": {
            "type": "object",
            "description": "Endereço cadastrado para a empresa no cadastro geral.",
            "properties": {
              "cep": {
                "type": "string",
                "description": "CEP do endereço da empresa.",
                "example": "12345678"
              },
              "descricao": {
                "type": "string",
                "description": "Descrição do endereço.",
                "example": "Rua Exemplo"
              },
              "numero": {
                "type": "string",
                "description": "Número do endereço.",
                "example": "123"
              },
              "complemento": {
                "type": "string",
                "description": "Complemento do endereço.",
                "example": "apto 1"
              },
              "bairro": {
                "type": "string",
                "description": "Bairro do endereço.",
                "example": "Bairro Exemplo"
              },
              "cidade": {
                "type": "string",
                "description": "Cidade do endereço.",
                "example": "Cidade Exemplo"
              }
            }
          },
          "empresaMatriz": {
            "type": "object",
            "description": "Dados da empresa matriz associada.",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código de identificação da empresa matriz.",
                "example": 1
              },
              "nomeFantasia": {
                "type": "string",
                "description": "Nome fantasia da empresa matriz.",
                "example": "Matriz Exemplo"
              },
              "cnpj": {
                "type": "string",
                "description": "CNPJ da empresa matriz.",
                "example": "00.000.000/0001-00"
              }
            }
          },
          "registroFiscal": {
            "type": "object",
            "description": "Informações de Registro Fiscal vinculado à empresa.",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código do Registro Fiscal vinculado à empresa",
                "example": 1
              },
              "nome": {
                "type": "string",
                "description": "Nome do Registro Fiscal vinculado à empresa",
                "example": "Registro fiscal padrão."
              }
            }
          },
          "regraCalculo": {
            "type": "object",
            "description": "Informações de Regra de Cálculo vinculada à empresa.",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código da Regra de Cálculo vinculada à empresa.",
                "example": 1
              },
              "nome": {
                "type": "string",
                "description": "Nome da Regra de Cálculo vinculada à empresa",
                "example": "Regra de cálculo padrão."
              }
            }
          },
          "lotacao": {
            "type": "object",
            "description": "Tipo de Lotação conforme estabelece o layout do eSocial versão 1.3 na Tabela 10 - Tipos de Lotação Tributária.",
            "properties": {
              "tipo": {
                "type": "integer",
                "description": "tipo",
                "example": 1
              },
              "descricao": {
                "type": "string",
                "description": "Descrição da Lotação",
                "example": "Obra de Construção Civil - Empreitada Parcial ou Subempreitada."
              }
            }
          },
          "desoneracaoFolha": {
            "type": "integer",
            "description": "Indica se a empresa é optante por desoneração da folha.Valores válidos:\n - 0: Não aplicável\n - 1: Empresa enquadrada nos critérios da legislação vigente.\n - Retorna vazio caso campo não esteja preenchido",
            "enum": [
              0,
              1
            ],
            "example": 1
          },
          "indicadorSimples": {
            "type": "integer",
            "description": "Indica se a empresa tem substituição de contribuição previdenciária patronal. Valores válidos:\n - 0: Não se aplica:\n - 1: Contribuição Substituída Integralmente:\n - 2: Contribuição não substituída:\n - 3: Contribuição não substituída concomitante com contribuição substituída\n - Retorna vazio caso campo não esteja preenchido",
            "enum": [
              0,
              1,
              2,
              3
            ],
            "example": 1
          },
          "contrataPcd": {
            "type": "integer",
            "description": "Indica a obrigatoriedade da empresa na contratação de PCD (Pessoa com deficiência).Valores Válidos:\n - 0: Dispensado de acordo com a lei\n - 1: Dispensado em virtude de processo judicial\n - 2: Exigibilidade suspensa virtude Termo firmado c/ MTE\n - 9: Obrigado\n - Retorna vazio caso campo não esteja preenchido",
            "enum": [
              0,
              1,
              2,
              9
            ],
            "example": 1
          },
          "contrataAprendiz": {
            "type": "integer",
            "description": "Indica a obrigatoriedade da empresa na contratação de Menor Aprendiz.Valores válidos:\n - 0: Dispensado de acordo com a lei:\n - 1: Dispensado em virtude de processo judicial:\n - 2: Obrigado\n - Retorna vazio caso campo não esteja preenchido",
            "enum": [
              0,
              1,
              2
            ],
            "example": 1
          },
          "regimeIrrf": {
            "type": "string",
            "description": "Regime de apuração do IRRF para Folha de Pagamento. Valores Válidos:\n - N: Competência\n - S: Caixa\n - Retorna vazio caso campo não esteja preenchido",
            "enum": [
              "N",
              "S"
            ],
            "example": "S"
          },
          "situacaoPj": {
            "type": "integer",
            "description": "Indica a situação da empresa. Valores válidos:\n - 0: Normal\n - 1: Extinção\n - 2: Fusão\n - 3: Cisão\n - 4: Incorporação\n - Retorna vazio caso campo não esteja preenchido",
            "enum": [
              0,
              1,
              2,
              3,
              4
            ],
            "example": 2
          },
          "cpfResponsavelCnpj": {
            "type": "string",
            "description": "CPF do responsável pelo CNPJ",
            "example": "91182905072"
          },
          "porte": {
            "type": "integer",
            "description": "Indica o porte da empresa. Valores válidos:\n - 1: Microempresa\n - 2: Empresa de Pequeno Porte\n - 3: Empresa Não Classificada nos Itens Anteriores\n - 4: Micro Empreendedor Individual\n - Retorna vazio caso campo não esteja preenchido",
            "enum": [
              1,
              2,
              3,
              4
            ],
            "example": 4
          },
          "cnpjSindicatoPatronal": {
            "type": "string",
            "description": "CNPJ do Sindicato Patronal",
            "example": "11785270000171"
          },
          "ativa": {
            "type": "boolean",
            "description": "Indica se a empresa está ativa no sistema.",
            "example": true
          },
          "dataAlteracao": {
            "type": "string",
            "description": "Data da última alteração no cadastro",
            "example": "10/03/2025 16:03:12"
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
