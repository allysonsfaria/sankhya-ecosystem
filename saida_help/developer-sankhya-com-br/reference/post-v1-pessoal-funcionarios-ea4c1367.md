---
id: "https://developer.sankhya.com.br/reference/post_v1-pessoal-funcionarios"
titulo: "Cria um novo funcionário"
url: "https://developer.sankhya.com.br/reference/post_v1-pessoal-funcionarios"
atualizado_em: "2026-10-22T11:38:21.000Z"
---

# Cria um novo funcionário

Cria um novo funcionário diretamente no SankhyaOM, sem necessidade de fluxo de requisição de admissão prévia.

O código do funcionário e a matrícula são gerados automaticamente por padrão. Para informar os valores manualmente, defina `gerarCodigoFuncionarioAutomatico: false` e/ou `gerarMatriculaAutomatica: false` e forneça os respectivos campos.

**Campos condicionalmente obrigatórios:**
- `contrato.fgts.tabelaOcorrencia` e `contrato.fgts.tabelaCategoria`: obrigatórios quando `contrato.fgts.optante = true`
- `contrato.periodoExperiencia.dataVencimento1` e `dataVencimento2`: obrigatórios quando `contrato.periodoExperiencia.dispensa = false`
- `naturezaAtividade`: obrigatório para categorias eSocial 401, 731, 734 e 738
- `codigoFuncionario`: obrigatório quando `gerarCodigoFuncionarioAutomatico = false`
- `matricula`: obrigatório quando `gerarMatriculaAutomatica = false`
- `contrato.codigoCidadeTrabalho` ou `contrato.codigoCidadeTrabalhoIbge`: é obrigatório informar pelo menos um
- `nascimento.codigoCidade` ou `nascimento.codigoCidadeIbge`: é obrigatório informar pelo menos um

**Limitações:**
- Não é permitido cadastrar funcionário com vínculo de aprendiz (categoria eSocial 103 ou vínculo 55 - Menor Aprendiz) por este endpoint.

**Versão mínima do módulo pessoal: 5.128.0**

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
    "/v1/pessoal/funcionarios": {
      "post": {
        "summary": "Cria um novo funcionário",
        "tags": [
          "HCM Funcionários"
        ],
        "description": "Cria um novo funcionário diretamente no SankhyaOM, sem necessidade de fluxo de requisição de admissão prévia.\n\nO código do funcionário e a matrícula são gerados automaticamente por padrão. Para informar os valores manualmente, defina `gerarCodigoFuncionarioAutomatico: false` e/ou `gerarMatriculaAutomatica: false` e forneça os respectivos campos.\n\n**Campos condicionalmente obrigatórios:**\n- `contrato.fgts.tabelaOcorrencia` e `contrato.fgts.tabelaCategoria`: obrigatórios quando `contrato.fgts.optante = true`\n- `contrato.periodoExperiencia.dataVencimento1` e `dataVencimento2`: obrigatórios quando `contrato.periodoExperiencia.dispensa = false`\n- `naturezaAtividade`: obrigatório para categorias eSocial 401, 731, 734 e 738\n- `codigoFuncionario`: obrigatório quando `gerarCodigoFuncionarioAutomatico = false`\n- `matricula`: obrigatório quando `gerarMatriculaAutomatica = false`\n- `contrato.codigoCidadeTrabalho` ou `contrato.codigoCidadeTrabalhoIbge`: é obrigatório informar pelo menos um\n- `nascimento.codigoCidade` ou `nascimento.codigoCidadeIbge`: é obrigatório informar pelo menos um\n\n**Limitações:**\n- Não é permitido cadastrar funcionário com vínculo de aprendiz (categoria eSocial 103 ou vínculo 55 - Menor Aprendiz) por este endpoint.\n\n**Versão mínima do módulo pessoal: 5.128.0**",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CadastroFuncionarioRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Funcionário criado com sucesso",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CadastroFuncionarioResponse"
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida — campo obrigatório ausente ou valor inválido.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Funcionariosretorno400"
                }
              }
            }
          },
          "500": {
            "description": "Erro interno no servidor"
          }
        },
        "security": [
          {
            "FuncionariosBearer": []
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "CadastroFuncionarioResponse": {
        "type": "object",
        "description": "Resposta ao criar um funcionário com sucesso",
        "properties": {
          "codigoFuncionario": {
            "type": "integer",
            "description": "Código do funcionário gerado no SankhyaOM",
            "example": 42
          },
          "codigoEmpresa": {
            "type": "integer",
            "description": "Código da empresa do funcionário",
            "example": 1
          },
          "matricula": {
            "type": "integer",
            "description": "Matrícula gerada para o funcionário",
            "example": 1001
          },
          "statusCadastro": {
            "type": "string",
            "description": "Status do cadastro após a criação",
            "example": "ATIVO"
          }
        }
      },
      "CadastroFuncionarioRequest": {
        "type": "object",
        "required": [
          "nome",
          "cpf",
          "sexo",
          "identidadeGenero",
          "orientacaoSexual",
          "estadoCivil",
          "nivelEscolaridade",
          "racaEtnia",
          "nascimento",
          "contato",
          "endereco",
          "contrato"
        ],
        "properties": {
          "nome": {
            "type": "string",
            "description": "Nome completo do funcionário",
            "example": "João da Silva"
          },
          "cpf": {
            "type": "string",
            "description": "CPF do funcionário (somente dígitos)",
            "example": "12345678900"
          },
          "nomeSocial": {
            "type": "string",
            "description": "Nome social do funcionário. Quando preenchido, o sistema registra automaticamente o funcionário como travesti ou transexual.",
            "example": "Joana Silva"
          },
          "sexo": {
            "type": "string",
            "description": "Sexo. Seguem os valores aceitos:\n  - M - Masculino\n  - F - Feminino\n",
            "enum": [
              "M",
              "F"
            ],
            "example": "M"
          },
          "identidadeGenero": {
            "type": "string",
            "description": "Identidade de Gênero. Seguem os valores aceitos:\n  - C - Cisgênero\n  - N - Não-binário\n  - T - Transgênero\n  - U - Não informado\n",
            "enum": [
              "C",
              "N",
              "T",
              "U"
            ],
            "example": "C"
          },
          "orientacaoSexual": {
            "type": "string",
            "description": "Orientação Sexual. Seguem os valores aceitos:\n  - A - Assexual\n  - B - Bissexual\n  - E - Heterossexual\n  - H - Homossexual\n  - N - Não informado\n  - P - Panssexual\n",
            "enum": [
              "A",
              "B",
              "E",
              "H",
              "N",
              "P"
            ],
            "example": "E"
          },
          "estadoCivil": {
            "type": "integer",
            "description": "Estado Civil. Seguem os valores aceitos:\n  - 1 - Solteiro(a)\n  - 2 - Casado(a)\n  - 3 - Viúvo(a)\n  - 4 - Separado(a) Judicialmente\n  - 5 - Desquitado(a)\n  - 6 - Divorciado(a)\n  - 7 - União Estável\n",
            "enum": [
              1,
              2,
              3,
              4,
              5,
              6,
              7
            ],
            "example": 1
          },
          "nivelEscolaridade": {
            "type": "integer",
            "description": "Escolaridade. Seguem os valores aceitos:\n  - 1 - Analfabeto\n  - 2 - Até 5º Ano Incompleto\n  - 3 - 5º Ano Completo\n  - 4 - 6º Ao 9º Ano Incompleto\n  - 5 - Fundamental Completo\n  - 6 - Ensino Médio Incompleto\n  - 7 - Ensino Médio Completo\n  - 8 - Superior Incompleto\n  - 9 - Superior Completo\n  - 10 - Mestrado Completo\n  - 11 - Doutorado Completo\n  - 12 - Pós-Graduação Completa\n",
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
              12
            ],
            "example": 9
          },
          "racaEtnia": {
            "type": "string",
            "description": "Raça/Etnia. Seguem os valores aceitos:\n  - 0 - Indígena\n  - 2 - Branca\n  - 4 - Preta\n  - 6 - Amarela\n  - 8 - Parda\n",
            "enum": [
              "0",
              "2",
              "4",
              "6",
              "8"
            ],
            "example": "2"
          },
          "possuiFilhos": {
            "type": "boolean",
            "description": "Indica se o funcionário possui filhos",
            "example": false
          },
          "observacao": {
            "type": "string",
            "description": "Observações gerais sobre o funcionário",
            "example": "Contratado via portal de integração"
          },
          "observacaoDeficiencia": {
            "type": "string",
            "description": "Informações específicas sobre deficiência do funcionário",
            "example": "Deficiência auditiva leve"
          },
          "naturezaAtividade": {
            "type": "string",
            "description": "Natureza da Atividade. Obrigatório para as categorias eSocial 401, 731, 734 e 738. Seguem os valores aceitos:\n  - P - Rural\n  - U - Urbano\n",
            "enum": [
              "P",
              "U"
            ],
            "example": "P"
          },
          "urlFotoPerfil": {
            "type": "string",
            "description": "URL pública da foto de perfil do funcionário (formatos PNG ou JPEG).",
            "example": "https://exemplo.com/foto.jpg"
          },
          "isParceiro": {
            "type": "boolean",
            "description": "Indica se o funcionário deve ser vinculado como parceiro no SankhyaOM",
            "example": false
          },
          "gerarCodigoFuncionarioAutomatico": {
            "type": "boolean",
            "description": "Quando `true` (padrão), o sistema gera o código do funcionário automaticamente. Quando `false`, o campo `codigoFuncionario` torna-se obrigatório.",
            "default": true,
            "example": true
          },
          "codigoFuncionario": {
            "type": "integer",
            "description": "Código do funcionário a ser cadastrado. Obrigatório quando `gerarCodigoFuncionarioAutomatico = false`.",
            "example": 100
          },
          "gerarMatriculaAutomatica": {
            "type": "boolean",
            "description": "Quando `true` (padrão), o sistema gera a matrícula automaticamente. Quando `false`, o campo `matricula` torna-se obrigatório.",
            "default": true,
            "example": true
          },
          "matricula": {
            "type": "integer",
            "description": "Matrícula do funcionário. Obrigatória quando `gerarMatriculaAutomatica = false`.",
            "example": 1001
          },
          "nascimento": {
            "type": "object",
            "description": "Informações de nascimento do funcionário",
            "required": [
              "data",
              "nacionalidade",
              "nomeMae",
              "codigoPaisNascimento"
            ],
            "properties": {
              "data": {
                "type": "string",
                "format": "date",
                "description": "Data de nascimento (formato DD/MM/AAAA)",
                "example": "15/06/1990"
              },
              "nomeMae": {
                "type": "string",
                "description": "Nome completo da mãe",
                "example": "Maria da Silva"
              },
              "nomePai": {
                "type": "string",
                "description": "Nome completo do pai",
                "example": "José da Silva"
              },
              "nacionalidade": {
                "type": "integer",
                "description": "Nacionalidade. Seguem os valores aceitos:\n  - 10 - Brasileiro\n  - 20 - Naturalizado Brasileiro\n  - 21 - Argentino\n  - 22 - Boliviano\n  - 23 - Chileno\n  - 24 - Paraguaio\n  - 25 - Uruguaio\n  - 26 - Venezuelano\n  - 27 - Colombiano\n  - 28 - Peruano\n  - 29 - Equatoriano\n  - 30 - Alemão\n  - 31 - Belga\n  - 32 - Britânico\n  - 34 - Canadense\n  - 35 - Espanhol\n  - 36 - Estadunidense\n  - 37 - Francês\n  - 38 - Suíço\n  - 39 - Italiano\n  - 40 - Haitiano\n  - 41 - Japonês\n  - 42 - Chinês\n  - 43 - Coreano\n  - 44 - Russo\n  - 45 - Português\n  - 46 - Paquistanês\n  - 47 - Indiano\n  - 48 - Outros Latinos\n  - 49 - Outros Asiáticos\n  - 51 - Outros Europeus\n  - 60 - Angolano\n  - 61 - Congolês\n  - 62 - Sul-Africano\n  - 70 - Outros Africanos\n  - 80 - Outros\n",
                "enum": [
                  10,
                  20,
                  21,
                  22,
                  23,
                  24,
                  25,
                  26,
                  27,
                  28,
                  29,
                  30,
                  31,
                  32,
                  34,
                  35,
                  36,
                  37,
                  38,
                  39,
                  40,
                  41,
                  42,
                  43,
                  44,
                  45,
                  46,
                  47,
                  48,
                  49,
                  51,
                  60,
                  61,
                  62,
                  70,
                  80
                ],
                "example": 10
              },
              "codigoCidade": {
                "type": "integer",
                "description": "Código da cidade de nascimento (atributo CODCID da entidade Cidade)",
                "example": 15
              },
              "codigoCidadeIbge": {
                "type": "integer",
                "description": "Código IBGE da cidade de nascimento (atributo CODMUNFIS da entidade Cidade)",
                "example": 3550308
              },
              "codigoUF": {
                "type": "integer",
                "description": "Código da UF de nascimento (atributo CODUF da entidade UnidadeFederativa)",
                "example": 35
              },
              "codigoPaisNascimento": {
                "type": "integer",
                "description": "Código do país de nascimento (atributo CODPAIS da entidade Pais)",
                "example": 105
              }
            }
          },
          "contato": {
            "type": "object",
            "description": "Informações de contato do funcionário",
            "required": [
              "email"
            ],
            "properties": {
              "email": {
                "type": "string",
                "format": "email",
                "description": "E-mail pessoal do funcionário",
                "example": "joao.silva@email.com"
              },
              "emailCorporativo": {
                "type": "string",
                "format": "email",
                "description": "E-mail corporativo do funcionário",
                "example": "joao.silva@empresa.com.br"
              },
              "celular": {
                "type": "string",
                "description": "Número de celular",
                "example": "11999998888"
              },
              "telefone": {
                "type": "string",
                "description": "Número de telefone fixo",
                "example": "1133334444"
              }
            }
          },
          "endereco": {
            "type": "object",
            "description": "Informações de endereço do funcionário",
            "required": [
              "cep",
              "numero"
            ],
            "properties": {
              "cep": {
                "type": "string",
                "description": "CEP (somente dígitos)",
                "example": "01310100"
              },
              "numero": {
                "type": "string",
                "description": "Número do endereço",
                "example": "100"
              },
              "complemento": {
                "type": "string",
                "description": "Complemento do endereço",
                "example": "Apto 42"
              },
              "anexos": {
                "type": "array",
                "description": "Anexos do comprovante de residência do funcionário",
                "items": {
                  "$ref": "#/components/schemas/AnexoUrl"
                }
              }
            }
          },
          "contrato": {
            "type": "object",
            "description": "Informações contratuais do funcionário",
            "required": [
              "codigoEmpresa",
              "codigoDepartamento",
              "codigoCargaHoraria",
              "codigoCategoriaESocial",
              "horasSemanais",
              "regimePrevidencia",
              "regimeJornadaTrabalho",
              "regimeTrabalho",
              "vinculo",
              "tipoRecebimento",
              "sindicato",
              "admissao",
              "remuneracao",
              "fgts",
              "periodoExperiencia"
            ],
            "properties": {
              "codigoEmpresa": {
                "type": "integer",
                "description": "Código da empresa (atributo CODEMP da entidade EmpresaPessoal)",
                "example": 1
              },
              "codigoDepartamento": {
                "type": "integer",
                "description": "Código do departamento (atributo CODDEP da entidade Departamento)",
                "example": 10
              },
              "codigoCargo": {
                "type": "integer",
                "description": "Código do cargo (atributo CODCARGO da entidade Cargo). Obrigatório se o padrão da empresa vincular cargo ao CBO.",
                "example": 7
              },
              "codigoFuncao": {
                "type": "integer",
                "description": "Código da função (atributo CODFUNCAO da entidade Funcao). Obrigatório se o padrão da empresa vincular função ao CBO.",
                "example": 15
              },
              "codigoCargaHoraria": {
                "type": "integer",
                "description": "Código de identificação da carga horária (atributo CODCARGAHOR da entidade IdentificacaoCargaHoraria)",
                "example": 1
              },
              "codigoCategoriaESocial": {
                "type": "integer",
                "description": "Código de categoria eSocial conforme Tabela 01 do eSocial (atributo CODCATEGESOCIAL da entidade CategoriaEsocial)",
                "example": 101
              },
              "codigoCategoria": {
                "type": "integer",
                "description": "Código de categoria próprio da empresa (atributo CODCATEGORIA da entidade CategoriaPessoal)",
                "example": 1
              },
              "codigoCidadeTrabalho": {
                "type": "integer",
                "description": "Código da cidade de trabalho (atributo CODCID da entidade CidadeTrabalho)",
                "example": 56
              },
              "codigoCidadeTrabalhoIbge": {
                "type": "integer",
                "description": "Código IBGE da cidade de trabalho (atributo CODMUNFIS da entidade CidadeTrabalho)",
                "example": 3550308
              },
              "codigoLocalTrabalho": {
                "type": "integer",
                "description": "Código do local de trabalho (atributo ID da entidade LocalPontoPessoalMais)",
                "example": 3
              },
              "horasSemanais": {
                "type": "number",
                "format": "float",
                "description": "Horas de trabalho semanais",
                "example": 44
              },
              "mei": {
                "type": "boolean",
                "description": "Indica se o funcionário é Microempreendedor Individual (MEI)",
                "example": false
              },
              "percentualAdiantamento": {
                "type": "number",
                "format": "float",
                "description": "Percentual de adiantamento salarial",
                "example": 40
              },
              "percentualInsalubridade": {
                "type": "number",
                "format": "float",
                "description": "Percentual de insalubridade",
                "example": 20
              },
              "percentualPericulosidade": {
                "type": "number",
                "format": "float",
                "description": "Percentual de periculosidade",
                "example": 30
              },
              "regimePrevidencia": {
                "type": "integer",
                "description": "Regime de Previdência. Seguem os valores aceitos:\n  - 1 - RPPS\n  - 2 - RGPS\n  - 3 - RPPS em extinção\n  - 4 - RPPE\n",
                "enum": [
                  1,
                  2,
                  3,
                  4
                ],
                "example": 2
              },
              "regimeJornadaTrabalho": {
                "type": "integer",
                "description": "Regime de Jornada de Trabalho. Seguem os valores aceitos:\n  - 1 - Tempo Integral\n  - 2 - Tempo Parcial\n  - 3 - Intermitente\n  - 4 - Outros\n",
                "enum": [
                  1,
                  2,
                  3,
                  4
                ],
                "example": 1
              },
              "regimeTrabalho": {
                "type": "integer",
                "description": "Regime de Trabalho. Seguem os valores aceitos:\n  - 1 - CLT\n  - 2 - RJU\n  - 3 - RJP\n",
                "enum": [
                  1,
                  2,
                  3
                ],
                "example": 1
              },
              "vinculo": {
                "type": "integer",
                "description": "Tipo de Vínculo. Seguem os valores aceitos:\n  - 2 - Estagiário\n  - 10 - Prazo indeterminado pessoa jurídica\n  - 15 - Prazo indeterminado pessoa física\n  - 20 - Prazo indeterminado rural (jurídica)\n  - 25 - Prazo indeterminado rural (física)\n  - 30 - Regime jurídico único\n  - 31 - Regime Jurídico Único (RGPS)\n  - 35 - Público não efetivo\n  - 40 - Funcionário avulso\n  - 50 - Contrato temporário\n  - 55 - Menor aprendiz\n  - 60 - Prazo determinado urbano (jurídica)\n  - 65 - Prazo determinado urbano (física)\n  - 70 - Prazo determinado rural (jurídica)\n  - 75 - Prazo determinado rural (física)\n  - 80 - Diretor sem vínculo empregatício\n  - 90 - Autônomo\n  - 95 - Prazo determinado (Lei 8.745)\n  - 96 - Prazo determinado (Lei Estadual)\n  - 97 - Prazo Determinado (Lei Municipal)\n  - 99 - Pensionista\n",
                "enum": [
                  2,
                  10,
                  15,
                  20,
                  25,
                  30,
                  31,
                  35,
                  40,
                  50,
                  55,
                  60,
                  65,
                  70,
                  75,
                  80,
                  90,
                  95,
                  96,
                  97,
                  99
                ],
                "example": 15
              },
              "tipoRecebimento": {
                "type": "string",
                "description": "Tipo de Recebimento do salário. Seguem os valores aceitos:\n  - B - Banco\n  - C - Cheque\n  - D - Dinheiro\n",
                "enum": [
                  "B",
                  "C",
                  "D"
                ],
                "example": "B"
              },
              "dataAso": {
                "type": "string",
                "format": "date",
                "description": "Data do Atestado de Saúde Ocupacional (ASO)",
                "example": "10/01/2025"
              },
              "dataTerminoContrato": {
                "type": "string",
                "format": "date",
                "description": "Data de término do contrato (para contratos por prazo determinado)",
                "example": "31/12/2025"
              },
              "trabalhaOutraEmpresa": {
                "type": "boolean",
                "description": "Indica se o funcionário trabalha em outra empresa",
                "example": false
              },
              "sindicato": {
                "type": "object",
                "description": "Informações de sindicato do funcionário",
                "required": [
                  "codigo",
                  "sindicalizado"
                ],
                "properties": {
                  "codigo": {
                    "type": "integer",
                    "description": "Código do sindicato (atributo CODSIND da entidade Sindicato)",
                    "example": 4
                  },
                  "sindicalizado": {
                    "type": "boolean",
                    "description": "Indica se o funcionário é sindicalizado",
                    "example": false
                  }
                }
              },
              "admissao": {
                "type": "object",
                "description": "Informações de admissão do funcionário",
                "required": [
                  "tipo",
                  "indicativo",
                  "data"
                ],
                "properties": {
                  "tipo": {
                    "type": "string",
                    "description": "Tipo de Admissão. Seguem os valores aceitos:\n  - A - Transferência de outro estabelecimento da mesma empresa sem ônus\n  - H - Admissão por sucessão, incorporação e cisão/fusão\n  - N - Admissão com emprego anterior\n  - U - Transferência de empresa considerada inapta por inexistência de fato\n  - R - Reintegração\n  - S - Admissão - Primeiro emprego\n  - T - Transferência de outro estabelecimento da mesma empresa com ônus\n  - O - Outros encerramentos\n",
                    "enum": [
                      "A",
                      "H",
                      "N",
                      "U",
                      "R",
                      "S",
                      "T",
                      "O"
                    ],
                    "example": "N"
                  },
                  "indicativo": {
                    "type": "integer",
                    "description": "Indicativo de Admissão (padrão eSocial S-1.3, atributo indAdmissao). Seguem os valores aceitos:\n  - 1 - Normal\n  - 2 - Decorrente Ação Fiscal\n  - 3 - Decorrente Decisão Judicial\n",
                    "enum": [
                      1,
                      2,
                      3
                    ],
                    "example": 1
                  },
                  "data": {
                    "type": "string",
                    "format": "date",
                    "description": "Data de admissão do funcionário (formato DD/MM/AAAA)",
                    "example": "15/01/2025"
                  }
                }
              },
              "remuneracao": {
                "type": "object",
                "description": "Informações de remuneração do funcionário",
                "required": [
                  "tipo",
                  "salarioBase",
                  "tipoSalario"
                ],
                "properties": {
                  "tipo": {
                    "type": "string",
                    "description": "Tipo de Remuneração. Seguem os valores aceitos:\n  - 1 - Salário Fixo\n  - 2 - Variável\n  - 3 - Sal. Fixo + Variável\n",
                    "enum": [
                      "1",
                      "2",
                      "3"
                    ],
                    "example": "1"
                  },
                  "salarioBase": {
                    "type": "number",
                    "format": "float",
                    "description": "Salário base do funcionário",
                    "example": 4500
                  },
                  "base": {
                    "type": "number",
                    "format": "float",
                    "description": "Remuneração base do funcionário (utilizada em cálculos específicos de remuneração)",
                    "example": 4500
                  },
                  "tipoSalario": {
                    "type": "string",
                    "description": "Tipo de Salário. Seguem os valores aceitos:\n  - 1 - Mensal\n  - 2 - Quinzenal\n  - 3 - Semanal\n  - 4 - Diarista\n  - 5 - Horista\n  - 6 - Tarefa\n",
                    "enum": [
                      "1",
                      "2",
                      "3",
                      "4",
                      "5",
                      "6"
                    ],
                    "example": "1"
                  }
                }
              },
              "fgts": {
                "type": "object",
                "description": "Informações de FGTS do funcionário",
                "required": [
                  "optante"
                ],
                "properties": {
                  "optante": {
                    "type": "boolean",
                    "description": "Indica se o funcionário é optante pelo FGTS. Quando `true`, `tabelaOcorrencia` e `tabelaCategoria` tornam-se obrigatórios.",
                    "example": true
                  },
                  "dataOpcao": {
                    "type": "string",
                    "format": "date",
                    "description": "Data de opção pelo FGTS",
                    "example": "15/01/2025"
                  },
                  "tabelaOcorrencia": {
                    "type": "string",
                    "description": "Tabela de Ocorrência FGTS. Obrigatório quando `optante = true`. Seguem os valores aceitos:\n  - 00 - Não exposição a agente nocivo\n  - 01 - Não exposição a agente nocivo, mas já esteve\n  - 02 - Exposição a agente nocivo (aposentadoria aos 15)\n  - 03 - Exposição a agente nocivo (aposentadoria aos 20)\n  - 04 - Exposição a agente nocivo (aposentadoria aos 25)\n  - 05 - Não exposição, já esteve, múltiplo vínculo\n  - 06 - Exposição (apos. aos 15) múltiplo vínculo\n  - 07 - Exposição (apos. aos 20) múltiplo vínculo\n  - 08 - Exposição (apos. aos 25) múltiplo vínculo\n",
                    "enum": [
                      "00",
                      "01",
                      "02",
                      "03",
                      "04",
                      "05",
                      "06",
                      "07",
                      "08"
                    ],
                    "example": "00"
                  },
                  "tabelaCategoria": {
                    "type": "string",
                    "description": "Tabela de Categoria FGTS. Obrigatório quando `optante = true`. Seguem os valores aceitos:\n  - 00 - Estagiários\n  - 01 - Empregados\n  - 02 - Trabalhador avulso\n  - 03 - Trabalhador sem RGPS mas com direito ao FGTS\n  - 04 - Empregado com contrato temporário ou intermitente\n  - 05 - Contribuinte individual - Diretor com FGTS\n  - 06 - Empregado doméstico\n  - 07 - Aprendiz - Lei 10.097/2000 ou Contrato Verde\n  - 11 - Diretor não empregado e empresários sem FGTS\n  - 12 - Demais agentes públicos\n  - 13 - Autônomo ou operador de máquina com FGTS\n  - 14 - Autônomo ou operador de máquina com salário base\n  - 26 - Dirigente sindical, adicional do sindicato; juiz classista temporário do Trabalho\n  - 27 - Contribuinte individual com remuneração do exterior sujeito ao recolhimento de FGTS\n  - 28 - Contribuinte individual - dirigente sindical com FGTS\n  - 29 - Contribuinte individual - trabalhador que presta serviço a entidade internacional no Brasil\n  - 30 - Estagiário contratado por missão diplomática/consulado\n  - 31 - Trabalhador contratado no exterior e transferido ao Brasil para contrato temporário\n  - 32 - Trabalhador intermitente contratado no exterior para prestar serviços no Brasil\n",
                    "enum": [
                      "00",
                      "01",
                      "02",
                      "03",
                      "04",
                      "05",
                      "06",
                      "07",
                      "11",
                      "12",
                      "13",
                      "14",
                      "26",
                      "27",
                      "28",
                      "29",
                      "30",
                      "31",
                      "32"
                    ],
                    "example": "01"
                  }
                }
              },
              "periodoExperiencia": {
                "type": "object",
                "description": "Informações do período de experiência do funcionário",
                "required": [
                  "dispensa"
                ],
                "properties": {
                  "dispensa": {
                    "type": "boolean",
                    "description": "Indica se o período de experiência é dispensado. Quando `false`, `dataVencimento1` e `dataVencimento2` tornam-se obrigatórios.",
                    "example": false
                  },
                  "dataVencimento1": {
                    "type": "string",
                    "format": "date",
                    "description": "Data final do primeiro período de experiência. Obrigatório quando `dispensa = false`.",
                    "example": "15/04/2025"
                  },
                  "dataVencimento2": {
                    "type": "string",
                    "format": "date",
                    "description": "Data final do segundo período de experiência. Obrigatório quando `dispensa = false`.",
                    "example": "15/07/2025"
                  }
                }
              }
            }
          },
          "documentos": {
            "type": "object",
            "description": "Documentos do funcionário",
            "properties": {
              "pis": {
                "type": "object",
                "properties": {
                  "numero": {
                    "type": "string",
                    "description": "Número do PIS",
                    "example": "12345678901"
                  },
                  "dataCadastro": {
                    "type": "string",
                    "format": "date",
                    "description": "Data de cadastro no PIS",
                    "example": "01/01/2010"
                  }
                }
              },
              "rg": {
                "type": "object",
                "properties": {
                  "numero": {
                    "type": "string",
                    "description": "Número do RG",
                    "example": "123456789"
                  },
                  "data": {
                    "type": "string",
                    "format": "date",
                    "description": "Data de emissão do RG",
                    "example": "10/05/2005"
                  },
                  "orgaoEmissor": {
                    "type": "string",
                    "description": "Órgão emissor do RG",
                    "example": "SSP-SP"
                  },
                  "uf": {
                    "type": "integer",
                    "description": "Código da UF de emissão do RG (atributo CODUF da entidade UnidadeFederativa)",
                    "example": 35
                  },
                  "anexos": {
                    "type": "array",
                    "description": "Anexos do RG do funcionário",
                    "items": {
                      "$ref": "#/components/schemas/AnexoUrl"
                    }
                  }
                }
              },
              "ctps": {
                "type": "object",
                "properties": {
                  "digital": {
                    "type": "boolean",
                    "description": "Funcionário possui CTPS Digital",
                    "example": true
                  },
                  "numero": {
                    "type": "integer",
                    "description": "Número da CTPS",
                    "example": 1234567
                  },
                  "serie": {
                    "type": "string",
                    "description": "Série da CTPS",
                    "example": "001"
                  },
                  "codigoUF": {
                    "type": "integer",
                    "description": "Código da UF da CTPS (atributo CODUF da entidade UnidadeFederativa)",
                    "example": 35
                  },
                  "data": {
                    "type": "string",
                    "format": "date",
                    "description": "Data da CTPS",
                    "example": "01/03/2010"
                  }
                }
              },
              "cnh": {
                "type": "object",
                "properties": {
                  "numero": {
                    "type": "string",
                    "description": "Número da CNH",
                    "example": "12345678900"
                  },
                  "categoria": {
                    "type": "string",
                    "description": "Categoria da CNH (ex.: A, B, AB)",
                    "example": "B"
                  },
                  "vencimento": {
                    "type": "string",
                    "format": "date",
                    "description": "Data de vencimento da CNH",
                    "example": "01/06/2028"
                  },
                  "uf": {
                    "type": "integer",
                    "description": "Código da UF da CNH",
                    "example": 35
                  },
                  "orgao": {
                    "type": "string",
                    "description": "Órgão emissor da CNH",
                    "example": "Detran-SP"
                  },
                  "dataPrimeira": {
                    "type": "string",
                    "format": "date",
                    "description": "Data da primeira CNH",
                    "example": "15/06/2010"
                  },
                  "dataEmissao": {
                    "type": "string",
                    "format": "date",
                    "description": "Data de emissão da CNH atual",
                    "example": "01/07/2023"
                  },
                  "anexos": {
                    "type": "array",
                    "description": "Anexos da CNH do funcionário",
                    "items": {
                      "$ref": "#/components/schemas/AnexoUrl"
                    }
                  }
                }
              },
              "tituloEleitoral": {
                "type": "object",
                "properties": {
                  "numero": {
                    "type": "string",
                    "description": "Número do título eleitoral",
                    "example": "123456789012"
                  },
                  "secao": {
                    "type": "string",
                    "description": "Seção eleitoral",
                    "example": "0001"
                  },
                  "zona": {
                    "type": "string",
                    "description": "Zona eleitoral",
                    "example": "001"
                  },
                  "anexos": {
                    "type": "array",
                    "description": "Anexos do título eleitoral do funcionário",
                    "items": {
                      "$ref": "#/components/schemas/AnexoUrl"
                    }
                  }
                }
              },
              "reservista": {
                "type": "object",
                "properties": {
                  "numero": {
                    "type": "string",
                    "description": "Número da reservista",
                    "example": "12345"
                  }
                }
              },
              "passaporte": {
                "type": "object",
                "properties": {
                  "numero": {
                    "type": "string",
                    "description": "Número do passaporte",
                    "example": "AA123456"
                  },
                  "dataEmissao": {
                    "type": "string",
                    "format": "date",
                    "description": "Data de emissão do passaporte",
                    "example": "01/01/2020"
                  },
                  "dataValidade": {
                    "type": "string",
                    "format": "date",
                    "description": "Data de validade do passaporte",
                    "example": "01/01/2030"
                  },
                  "emissor": {
                    "type": "string",
                    "description": "Órgão emissor do passaporte",
                    "example": "DPF"
                  },
                  "codigoUF": {
                    "type": "integer",
                    "description": "Código da UF de emissão",
                    "example": 35
                  }
                }
              }
            }
          },
          "informacoesBancarias": {
            "type": "object",
            "description": "Informações bancárias para pagamento do salário",
            "properties": {
              "codigoBanco": {
                "type": "integer",
                "description": "Código do banco (atributo CODBCO da entidade Banco)",
                "example": 341
              },
              "codigoAgencia": {
                "type": "string",
                "description": "Código da agência bancária (atributo CODAGE da entidade Agencia)",
                "example": "1234"
              },
              "numeroConta": {
                "type": "string",
                "description": "Número da conta bancária com dígito verificador",
                "example": "12345-6"
              },
              "tipoConta": {
                "type": "string",
                "description": "Tipo de conta bancária. Seguem os valores aceitos:\n  - A - Aplicação\n  - C - Corrente\n  - P - Poupança\n  - S - Salário\n",
                "enum": [
                  "A",
                  "C",
                  "P",
                  "S"
                ],
                "example": "C"
              },
              "anexos": {
                "type": "array",
                "description": "Anexos do comprovante de conta bancária do funcionário",
                "items": {
                  "$ref": "#/components/schemas/AnexoUrl"
                }
              }
            }
          },
          "camposAdicionais": {
            "type": "array",
            "description": "Campos adicionais configurados na entidade Funcionario do SankhyaOM",
            "items": {
              "type": "object",
              "required": [
                "nomeCampo",
                "valor"
              ],
              "properties": {
                "nomeCampo": {
                  "type": "string",
                  "description": "Nome do campo adicional (atributo AD_* da entidade)",
                  "example": "AD_CODINTEGRACAO"
                },
                "valor": {
                  "type": "string",
                  "description": "Valor do campo adicional",
                  "example": "EXT-001"
                }
              }
            }
          },
          "dependentes": {
            "type": "array",
            "description": "Lista de dependentes do funcionário",
            "items": {
              "type": "object",
              "required": [
                "pessoal",
                "dependencia"
              ],
              "properties": {
                "pessoal": {
                  "type": "object",
                  "description": "Dados pessoais do dependente",
                  "required": [
                    "nome",
                    "cpf",
                    "sexo"
                  ],
                  "properties": {
                    "nome": {
                      "type": "string",
                      "description": "Nome completo do dependente",
                      "example": "Maria de Fatima"
                    },
                    "cpf": {
                      "type": "string",
                      "description": "CPF do dependente (somente dígitos)",
                      "example": "65497593070"
                    },
                    "sexo": {
                      "type": "string",
                      "description": "Sexo do dependente:\n  - M - Masculino\n  - F - Feminino\n",
                      "enum": [
                        "M",
                        "F"
                      ],
                      "example": "F"
                    },
                    "convenio": {
                      "type": "boolean",
                      "description": "Indica se o dependente é de convênio médico",
                      "example": true
                    },
                    "idadeEscolar": {
                      "type": "boolean",
                      "description": "Indica se o dependente está em idade escolar",
                      "example": false
                    },
                    "incapazTrabalho": {
                      "type": "boolean",
                      "description": "Indica se o dependente é incapaz para o trabalho",
                      "example": false
                    },
                    "adotivo": {
                      "type": "boolean",
                      "description": "Indica se o dependente é adotivo",
                      "example": false
                    },
                    "racaEtnia": {
                      "type": "integer",
                      "description": "Raça/Etnia do dependente. Seguem os valores aceitos:\n  - 10 - Indígena\n  - 20 - Branca\n  - 30 - Preta\n  - 40 - Parda\n  - 50 - Amarela\n  - 60 - Não informado\n",
                      "enum": [
                        10,
                        20,
                        30,
                        40,
                        50,
                        60
                      ],
                      "example": 20
                    },
                    "anexosCpf": {
                      "type": "array",
                      "description": "Anexos do CPF do dependente",
                      "items": {
                        "$ref": "#/components/schemas/AnexoUrl"
                      }
                    }
                  }
                },
                "nascimento": {
                  "type": "object",
                  "description": "Dados de nascimento do dependente",
                  "properties": {
                    "data": {
                      "type": "string",
                      "format": "date",
                      "description": "Data de nascimento (formato DD/MM/AAAA)",
                      "example": "01/01/2005"
                    },
                    "nacionalidade": {
                      "type": "integer",
                      "description": "Nacionalidade do dependente (mesma tabela de nacionalidade do funcionário; ex.: 10 - Brasileiro)",
                      "enum": [
                        10,
                        20,
                        21,
                        22,
                        23,
                        24,
                        25,
                        26,
                        27,
                        28,
                        29,
                        30,
                        31,
                        32,
                        34,
                        35,
                        36,
                        37,
                        38,
                        39,
                        40,
                        41,
                        42,
                        43,
                        44,
                        45,
                        46,
                        47,
                        48,
                        49,
                        51,
                        60,
                        61,
                        62,
                        70,
                        80
                      ],
                      "example": 10
                    },
                    "naturalidade": {
                      "type": "integer",
                      "description": "Código da cidade de naturalidade (CODCID)",
                      "example": 123
                    },
                    "naturalidadeIbge": {
                      "type": "integer",
                      "description": "Código IBGE da cidade de naturalidade (tem prioridade sobre naturalidade)",
                      "example": 3305802
                    },
                    "nomeMae": {
                      "type": "string",
                      "description": "Nome completo da mãe do dependente",
                      "example": "Carmen"
                    },
                    "anexosRg": {
                      "type": "array",
                      "description": "Anexos do RG do dependente",
                      "items": {
                        "$ref": "#/components/schemas/AnexoUrl"
                      }
                    }
                  }
                },
                "dependencia": {
                  "type": "object",
                  "description": "Dados da dependência",
                  "required": [
                    "grauParentesco"
                  ],
                  "properties": {
                    "grauParentesco": {
                      "type": "integer",
                      "description": "Grau de parentesco. Seguem os valores aceitos:\n  - 1 - Filho(a)\n  - 2 - Esposo(a)\n  - 3 - Pai/Mãe\n  - 4 - Sogro(a)\n  - 5 - Sobrinho(a)\n  - 6 - Inválido(a)\n  - 7 - Outros\n  - 8 - Filho(a)/Enteado(a) incapaz\n  - 9 - Irmão(ã)/Neto(a)/Bisneto(a)\n  - 10 - Irmão(ã)/Neto(a)/Bisneto(a) incapaz\n  - 11 - Menor de até 21 anos sem condições financeiras\n  - 12 - Companheiro(a) com filho ou união acima de 5 anos\n  - 13 - Ex-cônjuge com pensão\n  - 14 - Filho(a)/enteado(a) universitário até 24 anos\n  - 15 - Irmão(ã)/Neto(a)/Bisneto(a) sem arrimo com guarda\n  - 16 - Absolutamente incapaz com tutela\n  - 17 - Agregado(a)\n  - 18 - Enteado(a)\n",
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
                      "example": 1
                    },
                    "dependenteIRRF": {
                      "type": "boolean",
                      "description": "Indica se é dependente para IRRF",
                      "example": true
                    },
                    "dataInicioDependencia": {
                      "type": "string",
                      "format": "date",
                      "description": "Data de início da dependência (formato DD/MM/AAAA)",
                      "example": "01/01/2020"
                    },
                    "dataFimDependencia": {
                      "type": "string",
                      "format": "date",
                      "description": "Data de fim da dependência (formato DD/MM/AAAA)",
                      "example": "01/01/2030"
                    },
                    "motivoInicio": {
                      "type": "integer",
                      "description": "Motivo de início da dependência. Seguem os valores aceitos:\n  - 10 - Nascimento\n  - 11 - Invalidez\n  - 12 - Casamento\n  - 13 - União estável\n  - 14 - Adoção\n  - 15 - Decisão judicial\n  - 16 - Dependência econômica\n  - 17 - Filho póstumo\n  - 18 - Tutela do menor\n  - 19 - Designação expressa\n",
                      "enum": [
                        10,
                        11,
                        12,
                        13,
                        14,
                        15,
                        16,
                        17,
                        18,
                        19
                      ],
                      "example": 10
                    },
                    "motivoFim": {
                      "type": "integer",
                      "description": "Motivo de fim da dependência. Seguem os valores aceitos:\n  - 50 - Maioridade\n  - 51 - Óbito\n  - 52 - Separação judicial\n  - 53 - Divórcio\n  - 54 - Emancipação\n  - 55 - Decisão judicial\n  - 56 - Cessação da invalidez\n  - 57 - Independência econômica\n  - 58 - Revogação da tutela\n  - 59 - Exclusão por designação expressa\n",
                      "enum": [
                        50,
                        51,
                        52,
                        53,
                        54,
                        55,
                        56,
                        57,
                        58,
                        59
                      ],
                      "example": 50
                    },
                    "dataLimiteIRRF": {
                      "type": "string",
                      "format": "date",
                      "description": "Data limite para dedução de IRRF (formato DD/MM/AAAA)",
                      "example": "01/01/2035"
                    },
                    "descricaoDependencia": {
                      "type": "string",
                      "description": "Descrição livre da dependência",
                      "example": "Dependente universitário"
                    }
                  }
                },
                "pensao": {
                  "type": "object",
                  "description": "Dados de pensão alimentícia do dependente",
                  "properties": {
                    "tipo": {
                      "type": "string",
                      "description": "Tipo de pensão. Seguem os valores aceitos:\n  - L - Líquido\n  - B - Bruto\n  - S - Salário Mínimo\n  - P - Personalizado\n",
                      "enum": [
                        "L",
                        "B",
                        "S",
                        "P"
                      ],
                      "example": "L"
                    },
                    "pensionista": {
                      "type": "boolean",
                      "description": "Indica se o dependente é pensionista",
                      "example": true
                    },
                    "codigoParceiro": {
                      "type": "integer",
                      "description": "Código do parceiro (CODPARC) associado ao pensionista",
                      "example": 1
                    },
                    "percentual": {
                      "type": "number",
                      "format": "float",
                      "description": "Percentual da pensão",
                      "example": 20
                    },
                    "valor": {
                      "type": "number",
                      "format": "float",
                      "description": "Valor fixo da pensão",
                      "example": 100
                    },
                    "percentualRepassePensionista": {
                      "type": "number",
                      "format": "float",
                      "description": "Percentual de repasse ao pensionista",
                      "example": 1
                    },
                    "percentualHomologNet": {
                      "type": "number",
                      "format": "float",
                      "description": "Percentual de homologação (rescisão) sobre o líquido",
                      "example": 2
                    },
                    "percentualHomologNetFGTS": {
                      "type": "number",
                      "format": "float",
                      "description": "Percentual de homologação (rescisão) sobre o FGTS",
                      "example": 2
                    },
                    "anexosOficioPensao": {
                      "type": "array",
                      "description": "Anexos do ofício de pensão",
                      "items": {
                        "$ref": "#/components/schemas/AnexoUrl"
                      }
                    }
                  }
                },
                "salarioFamilia": {
                  "type": "object",
                  "description": "Dados de salário-família do dependente",
                  "properties": {
                    "dependente": {
                      "type": "boolean",
                      "description": "Indica se o dependente conta para salário-família",
                      "example": false
                    },
                    "fazRepasse": {
                      "type": "boolean",
                      "description": "Indica se faz repasse do salário-família ao pensionista",
                      "example": true
                    },
                    "dataLimite": {
                      "type": "string",
                      "format": "date",
                      "description": "Data limite do salário-família (formato DD/MM/AAAA)",
                      "example": "01/01/2030"
                    }
                  }
                },
                "auxilioCreche": {
                  "type": "object",
                  "description": "Dados de auxílio-creche do dependente",
                  "properties": {
                    "receber": {
                      "type": "boolean",
                      "description": "Indica se o dependente recebe auxílio-creche",
                      "example": false
                    },
                    "temAtestado": {
                      "type": "boolean",
                      "description": "Indica se há atestado para o auxílio-creche",
                      "example": false
                    },
                    "dataLimite": {
                      "type": "string",
                      "format": "date",
                      "description": "Data limite do auxílio-creche (formato DD/MM/AAAA)",
                      "example": "01/01/2030"
                    }
                  }
                }
              }
            }
          },
          "trabalhoTemporario": {
            "type": "object",
            "description": "Informações de trabalho temporário (obrigatório para vínculos temporários conforme eSocial)",
            "properties": {
              "tipoInclusaoContratual": {
                "type": "integer",
                "description": "Tipo de inclusão contratual do trabalho temporário. Seguem os valores aceitos:\n  - 1 - Locais sem filiais\n  - 2 - Estudo de mercado\n  - 3 - Contratação superior a 3 meses\n",
                "enum": [
                  1,
                  2,
                  3
                ],
                "example": 1
              },
              "contratoTrabalhoTemporario": {
                "type": "integer",
                "description": "Tipo de contrato de trabalho temporário. Seguem os valores aceitos:\n  - 0 - Não se aplica\n  - 1 - Necessidade transitória de substituição de pessoal regular\n  - 2 - Acréscimo extraordinário de serviços\n",
                "enum": [
                  0,
                  1,
                  2
                ],
                "example": 0
              },
              "cpfSubstituido": {
                "type": "string",
                "description": "CPF do trabalhador substituído (somente dígitos)",
                "example": "12345678900"
              },
              "tipoInscricaoEstabelecimentoTomador": {
                "type": "string",
                "description": "Tipo de inscrição do estabelecimento tomador. Seguem os valores aceitos:\n  - 1 - CNPJ\n  - 2 - CPF\n",
                "enum": [
                  "1",
                  "2"
                ],
                "example": "1"
              },
              "inscricaoEstabelecimentoTomador": {
                "type": "string",
                "description": "Número de inscrição do estabelecimento tomador (somente dígitos)",
                "example": "12345678000199"
              },
              "tipoInscricaoEstabelecimentoVinculado": {
                "type": "string",
                "description": "Tipo de inscrição do estabelecimento vinculado. Seguem os valores aceitos:\n  - 1 - CNPJ\n  - 2 - CPF\n",
                "enum": [
                  "1",
                  "2"
                ],
                "example": "1"
              },
              "inscricaoEstabelecimentoVinculado": {
                "type": "string",
                "description": "Número de inscrição do estabelecimento vinculado (somente dígitos)",
                "example": "98765432000188"
              },
              "justificativaContratacao": {
                "type": "string",
                "description": "Justificativa para contratação temporária",
                "example": "Substituição de empregado afastado"
              }
            }
          },
          "trabalhadorEstrangeiro": {
            "type": "object",
            "description": "Informações complementares para trabalhadores estrangeiros",
            "properties": {
              "casadoBrasil": {
                "type": "boolean",
                "description": "Indica se o trabalhador estrangeiro é casado com brasileiro(a)",
                "example": false
              },
              "filhosBrasileiros": {
                "type": "boolean",
                "description": "Indica se o trabalhador estrangeiro possui filhos brasileiros",
                "example": false
              },
              "classificacao": {
                "type": "string",
                "description": "Classificação do trabalhador estrangeiro conforme tabela eSocial",
                "example": "1"
              },
              "dataChegadaPais": {
                "type": "string",
                "format": "date",
                "description": "Data de chegada ao Brasil",
                "example": "01/03/2020"
              },
              "prazoResidencia": {
                "type": "string",
                "description": "Prazo de residência no Brasil",
                "example": "PERMANENTE"
              },
              "rne": {
                "type": "object",
                "description": "Dados do Registro Nacional de Estrangeiros (RNE)",
                "properties": {
                  "numero": {
                    "type": "string",
                    "description": "Número do RNE",
                    "example": "W123456-7"
                  },
                  "dataVencimento": {
                    "type": "string",
                    "format": "date",
                    "description": "Data de vencimento do RNE",
                    "example": "31/12/2030"
                  },
                  "orgaoEmissor": {
                    "type": "string",
                    "description": "Órgão emissor do RNE",
                    "example": "PF"
                  }
                }
              }
            }
          },
          "anexosCpf": {
            "type": "array",
            "description": "Anexos do CPF do funcionário",
            "items": {
              "$ref": "#/components/schemas/AnexoUrl"
            }
          },
          "anexosAdmissao": {
            "type": "array",
            "description": "Anexos do exame admissional (ASO)",
            "items": {
              "$ref": "#/components/schemas/AnexoUrl"
            }
          },
          "deficiencias": {
            "type": "array",
            "description": "Lista de deficiências do funcionário. A presença de ao menos um item marca automaticamente o funcionário como deficiente físico (PCD) e como informação de cota.",
            "items": {
              "type": "object",
              "properties": {
                "tipoDeficiencia": {
                  "type": "integer",
                  "description": "Tipo de deficiência. Seguem os valores aceitos:\n  - 1 - Física\n  - 2 - Visual\n  - 3 - Auditiva\n  - 4 - Mental\n  - 5 - Intelectual\n  - 6 - Reabilitado\n",
                  "enum": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                  ],
                  "example": 2
                }
              }
            }
          }
        }
      },
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
      "AnexoUrl": {
        "type": "object",
        "description": "Anexo em formato de URL para download assíncrono",
        "required": [
          "url"
        ],
        "properties": {
          "url": {
            "type": "string",
            "description": "URL do arquivo a ser baixado e armazenado como anexo",
            "example": "https://storage.exemplo.com.br/docs/rg-joao.pdf"
          },
          "nome": {
            "type": "string",
            "description": "Nome do arquivo (usado como nome do anexo no sistema)",
            "example": "rg-joao.pdf"
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
      "FuncionariosBearer": {
        "type": "http",
        "scheme": "bearer",
        "description": "Token de autenticação JWT obtido via endpoint de login da API Sankhya"
      }
    }
  }
}
```
