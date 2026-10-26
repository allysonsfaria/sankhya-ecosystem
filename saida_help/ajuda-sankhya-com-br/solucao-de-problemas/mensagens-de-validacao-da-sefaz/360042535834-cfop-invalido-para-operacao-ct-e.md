---
id: "360042535834"
titulo: "CFOP inválido para operação (CT-e)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042535834-CFOP-inv%C3%A1lido-para-opera%C3%A7%C3%A3o-CT-e"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:54Z"
rotulos: ["#criadoRoger", "ERROCTE", "CT-e", "Configuração", "SEFAZ", "TOP", "CFOP", "519", "[519-Rejeição]: CFOP inválido para operação.", "Ajuste CFOP conforme matriz SEFAZ", "CFOP inválido operação CT-e", "CT-e Anulação", "CFOP SEFAZ Regras", "Ajustes ICMS", "Documentos Eletrônicos"]
---

# CFOP inválido para operação (CT-e)

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16309482145303) **MENSAGEM:**

[519-Rejeição]: CFOP inválido para operação.

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16309482149143) **SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

**(1)** As condições da SEFAZ é a seguinte:

**(2)** Verifique o CFOP informado considerando a seguinte matriz:

**(3)**Para CT-e do tipo Normal, Complementar ou Substituição:

- Se UF de início da prestação = UF de fim de prestação (e UF fim <> EX) --> CFOP deve iniciar por **5**
- Se UF de início da prestação <> UF de fim da prestação (e UF fim <> EX) --> CFOP deve iniciar por **6**
- Se UF fim de prestação = EX --> CFOP deve iniciar por **7**

**(3)**Para CT-e de anulação de valores:

- Se UF de início da prestação = UF de fim de prestação (ambas <> EX) --> CFOP deve ser **1206**
- Se UF de início da prestação <> UF de fim da prestação (ambas <> EX) --> CFOP deve ser **2206**
- Se UF de início ou fim de prestação = EX

**(2)** Ajuste os campos abaixo de acordo com a contabilidade da empresa:

Tela [**Tipos de Operação - TOP**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP » Aba **"Livro Fiscal"),** campos:

- **Atualização de Livro ICMS**
- **CFOP's para FORA do estado**
- **CFOP's para DENTRO do estado**

![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16309482157591) **CAUSA:**

 Essa rejeição se dá pela validação do CFOP e a operação realizada pelo CT-e.

![Imagem 4: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16309438645399) **OBSERVAÇÃO:**

**[Manual de Orientação ao Contribuinte (v. 3.00)](http://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=bx74pJ8hXaM=)**
