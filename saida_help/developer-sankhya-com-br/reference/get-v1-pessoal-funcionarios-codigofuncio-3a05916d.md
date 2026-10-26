---
id: "https://developer.sankhya.com.br/reference/get_v1-pessoal-funcionarios-codigofuncionario-empresa-codigoempresa"
titulo: "Retorna os dados completos de um funcionário em uma empresa"
url: "https://developer.sankhya.com.br/reference/get_v1-pessoal-funcionarios-codigofuncionario-empresa-codigoempresa"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Retorna os dados completos de um funcionário em uma empresa

Retorna os dados de um funcionário em uma empresa com base nos parâmetros enviados na requisição. 

 Versão mínima do módulo pessoal: **5.51.0**

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
      "name": "HCM Funcionários",
      "description": "Cadastros relacionados a Funcionários no SankhyaOm"
    }
  ],
  "paths": {
    "/v1/pessoal/funcionarios/{codigoFuncionario}/empresa/{codigoEmpresa}": {
      "get": {
        "summary": "Retorna os dados completos de um funcionário em uma empresa",
        "tags": [
          "HCM Funcionários"
        ],
        "description": "Retorna os dados de um funcionário em uma empresa com base nos parâmetros enviados na requisição. \n\n Versão mínima do módulo pessoal: **5.51.0**",
        "parameters": [
          {
            "name": "codigoFuncionario",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer"
            },
            "description": "Código identificador do funcionário"
          },
          {
            "name": "codigoEmpresa",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer"
            },
            "description": "Código identificador da empresa"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados do funcionário retornados com sucesso",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Funcionario"
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Funcionariosretorno400"
                }
              }
            }
          },
          "404": {
            "description": "Funcionário ou empresa não encontrados"
          },
          "500": {
            "description": "Erro interno no servidor"
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Funcionariosretorno400": {
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
      "Funcionario": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 123
          },
          "cpf": {
            "type": "string",
            "example": "12345678900"
          },
          "nome": {
            "type": "string",
            "example": "João da Silva"
          },
          "matricula": {
            "type": "integer",
            "example": 1234
          },
          "dadosPessoais": {
            "$ref": "#/components/schemas/DadosPessoais"
          },
          "endereco": {
            "$ref": "#/components/schemas/FuncionariosEndereco"
          },
          "dadosContratuais": {
            "$ref": "#/components/schemas/DadosContratuais"
          },
          "afastamento": {
            "$ref": "#/components/schemas/Afastamento"
          },
          "transferencia": {
            "$ref": "#/components/schemas/Transferencia"
          }
        }
      },
      "DadosPessoais": {
        "type": "object",
        "properties": {
          "nascimento": {
            "type": "string",
            "example": "01/01/1990"
          },
          "sexo": {
            "type": "string",
            "description": "`M` - Masculino  \n`F` - Feminino  \n",
            "example": "M"
          },
          "celular": {
            "type": "string",
            "example": "11999998888"
          },
          "email": {
            "type": "string",
            "example": "joao.silva@email.com"
          },
          "nomeMae": {
            "type": "string",
            "description": "Nome completo da mãe do funcionário.",
            "example": "Maria da Silva Santos"
          }
        }
      },
      "FuncionariosEndereco": {
        "type": "object",
        "properties": {
          "cep": {
            "type": "string",
            "example": "01234567"
          },
          "codigo": {
            "type": "integer",
            "example": 456
          },
          "descricao": {
            "type": "string",
            "example": "Rua Exemplo"
          },
          "numero": {
            "type": "string",
            "example": "123"
          },
          "complemento": {
            "type": "string",
            "example": "Apto 45"
          },
          "bairro": {
            "$ref": "#/components/schemas/Bairro"
          },
          "cidade": {
            "$ref": "#/components/schemas/Cidade"
          }
        }
      },
      "Bairro": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 789
          },
          "descricao": {
            "type": "string",
            "example": "Centro"
          }
        }
      },
      "Cidade": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 1011
          },
          "descricao": {
            "type": "string",
            "example": "São Paulo"
          },
          "codigoIBGE": {
            "type": "integer",
            "example": 3550308
          }
        }
      },
      "DadosContratuais": {
        "type": "object",
        "properties": {
          "empresa": {
            "$ref": "#/components/schemas/Empresa"
          },
          "dataAdmissao": {
            "type": "string",
            "example": "15/01/2020"
          },
          "codigoCategoriaEsocial": {
            "type": "integer",
            "example": 101,
            "description": "Tipo de vínculo trabalhista:  \n - 101 - EMPREGADO - GERAL, INCLUSIVE O EMPREGADO PÚBLICO DA ADMINISTRAÇÃO DIRETA OU INDIRETA CONTRATADO PELA CLT  \n - 102 - EMPREGADO - TRABALHADOR RURAL POR PEQUENO PRAZO DA LEI 11.718/2008  \n - 103 - EMPREGADO - APRENDIZ  \n - 104 - EMPREGADO - DOMÉSTICO  \n - 105 - EMPREGADO - CONTRATO A TERMO FIRMADO NOS TERMOS DA LEI 9601/98  \n - 106 - TRABALHADOR TEMPORÁRIO - CONTRATO POR PRAZO DETERMINADO NOS TERMOS DA LEI 6019/74  \n - 107 - EMPREGADO - CONTRATO DE TRABALHO VERDE E AMARELO - SEM ACORDO PARA ANTECIPACAO MENSAL DA MULTA RESCISORIA DO FGTS  \n - 108 - EMPREGADO - CONTRATO DE TRABALHO VERDE E AMARELO - COM ACORDO PARA ANTECIPACAO MENSAL DA MULTA RESCISORIA DO FGTS  \n - 111 - EMPREGADO - CONTRATO DE TRABALHO INTERMITENTE  \n - 201 - TRABALHADOR AVULSO PORTUÁRIO  \n - 202 - TRABALHADOR AVULSO NÃO PORTUÁRIO  \n - 301 - SERVIDOR PÚBLICO TITULAR DE CARGO EFETIVO  \n - 401 - DIRIGENTE SINDICAL  \n - 701 - CONTRIBUINTE INDIVIDUAL - AUTÔNOMO  \n - 901 - ESTAGIÁRIO  \n - 902 - MÉDICO RESIDENTE  \n - 903 - BOLSISTA  \n - 904 - PARTICIPANTE DE CURSO DE FORMAÇÃO\n"
          },
          "situacao": {
            "type": "string",
            "description": "Situação do funcionário:  \n- 0 - Demitido  \n- 1 - Atividade normal  \n- 2 - Afastado sem remuneração  \n- 3 - Afastado por acidente de trabalho  \n- 4 - Afastado para serviço militar  \n- 5 - Afastado por licença gestante  \n- 6 - Afastado por doença acima de 15 dias  \n- 7 - Outros  \n- 8 - Transferido  \n- 9 - Aposentado por invalidez  \n",
            "example": "1"
          },
          "salarioBase": {
            "type": "number",
            "example": 3500
          },
          "bolsaEstagioOuProLabore": {
            "type": "number",
            "example": 1200
          },
          "departamento": {
            "$ref": "#/components/schemas/FuncionariosDepartamento"
          },
          "cargo": {
            "$ref": "#/components/schemas/FuncionariosCargo"
          },
          "funcao": {
            "$ref": "#/components/schemas/FuncionariosFuncao"
          },
          "localTrabalho": {
            "$ref": "#/components/schemas/LocalTrabalho"
          },
          "cidadeTrabalho": {
            "$ref": "#/components/schemas/CidadeTrabalho"
          },
          "sindicato": {
            "$ref": "#/components/schemas/Sindicato"
          },
          "cargaHoraria": {
            "$ref": "#/components/schemas/CargaHoraria"
          }
        }
      },
      "Empresa": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 1
          },
          "cnpj": {
            "type": "string",
            "example": "12345678000199"
          },
          "razaoSocial": {
            "type": "string",
            "example": "Empresa Exemplo S/A"
          }
        }
      },
      "FuncionariosDepartamento": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 22
          },
          "descricao": {
            "type": "string",
            "example": "TI"
          }
        }
      },
      "FuncionariosCargo": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 7
          },
          "descricao": {
            "type": "string",
            "example": "Desenvolvedor"
          },
          "cbo": {
            "type": "integer",
            "example": 317105
          }
        }
      },
      "FuncionariosFuncao": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 15
          },
          "descricao": {
            "type": "string",
            "example": "Analista de Sistemas"
          },
          "cbo": {
            "type": "integer",
            "example": 212415
          }
        }
      },
      "LocalTrabalho": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 3
          },
          "descricao": {
            "type": "string",
            "example": "Matriz"
          }
        }
      },
      "CidadeTrabalho": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 1011
          },
          "descricao": {
            "type": "string",
            "example": "São Paulo"
          },
          "codigoIBGE": {
            "type": "integer",
            "example": 3550308
          }
        }
      },
      "Sindicato": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 9
          },
          "nome": {
            "type": "string",
            "example": "Sindicato dos Programadores"
          },
          "cnpj": {
            "type": "string",
            "example": "11222333444455"
          }
        }
      },
      "CargaHoraria": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 40
          },
          "descricao": {
            "type": "string",
            "example": "Carga Horária Semanal - 40h"
          }
        }
      },
      "Afastamento": {
        "type": "object",
        "properties": {
          "motivoDesligamentoEsocial": {
            "type": "string",
            "example": "Rescisão por Justa Causa"
          },
          "dataAfastamento": {
            "type": "string",
            "example": "01/08/2023"
          },
          "causaAfastamento": {
            "$ref": "#/components/schemas/CausaAfastamento"
          },
          "tipoRescisao": {
            "$ref": "#/components/schemas/TipoRescisao"
          },
          "dataDesligamento": {
            "type": "string",
            "example": "01/09/2023"
          },
          "dataAvisoPrevio": {
            "type": "string",
            "example": "01/08/2023"
          }
        }
      },
      "CausaAfastamento": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 6
          },
          "descricao": {
            "type": "string",
            "example": "Doença"
          }
        }
      },
      "TipoRescisao": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 2
          },
          "descricao": {
            "type": "string",
            "example": "Dispensa sem Justa Causa"
          }
        }
      },
      "Transferencia": {
        "type": "object",
        "properties": {
          "dataTransferenciaDestino": {
            "type": "string",
            "example": "01/10/2023"
          },
          "empresaDestino": {
            "type": "integer",
            "example": 5
          },
          "cnpjEmpresaDestino": {
            "type": "string",
            "example": "98765432000188"
          },
          "codigoFuncionarioDestino": {
            "type": "integer",
            "example": 789
          },
          "motivoDesligamento": {
            "type": "string",
            "example": "Transferência de unidade"
          },
          "dataTransferencia": {
            "type": "string",
            "example": "30/09/2023"
          },
          "empresaOrigem": {
            "type": "integer",
            "example": 1
          },
          "codigoFuncionarioOrigem": {
            "type": "integer",
            "example": 123
          },
          "dataInicioVinculo": {
            "type": "string",
            "example": "01/03/2015"
          },
          "cnpjNaEmpresaAnterior": {
            "type": "string",
            "example": "12345678000199"
          },
          "matriculaNaEmpresaAnterior": {
            "type": "number",
            "example": 567
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
