---
id: "37880797703191"
titulo: "Analise e Cadastro de Serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880797703191-Analise-e-Cadastro-de-Servi%C3%A7o"
trilha: "Universidade Sankhya > Jornada da NFSe"
atualizado_em: "2026-07-22T14:06:23Z"
rotulos: ["Produtos", "ISS", "Configuração", "Impostos", "Financeiro", "NFS-e"]
---

# Analise e Cadastro de Serviço

## Serviço

O cadastro de serviço é a âncora fiscal da NFS-e: nele se definem o tipo de serviço (LC 116) e o código de tributação do município que alimentam o XML/RPS e precisam estar alinhados às regras locais. É esse cadastro que sustenta alíquota, base, deduções e retenções de ISS, assegurando cálculo correto, validação na prefeitura e integração limpa com o financeiro — reduzindo rejeições e retrabalho.

#### Siga as orientações para realizar a configuração no ERP Sankhya

1. Acesse a tela **Serviço**
   **Menu:** Configurações » Cadastros »  Produtos » Serviço

Para este treinamento cadastre o serviço de **Representação Comercial**

- Ative o cadastro
- Informe na descrição o nome do serviço

**Aba Geral**

- Selecione as opções correspondentes nos campos abaixo:

  - Tem ISS - **“Tributado”**
  - Tipo de Serviço - **1009 - Representação de qualquer natureza, inclusive comercial**
- Tem IRF -  **marcado**
- Adicione as informações correspondentes nos campos abaixo: 

  - % IRF - **1,50**
  - CNAE - **461760000**
- No campo "Grupo PIS" vincule  os grupos previamente cadastrados na tela **Alíquotas de PIS**.
- No campo "Grupo COFINS" os grupos previamente cadastrados na rotina **Alíquotas de COFINS**.

**Aba Alíquotas de ISS**

- Cidade - **2 - Uberlândia**
- Empresa - **1**
- Percentual de ISS - **2,00**
- Cód. Tributação ISS - **“00 - Tributado”**
- Cod. Trib. Município - **3170206**
- Tipo de Serviço - **“1009 - Representação de qualquer natureza, inclusive comercial”**
  **Na aba Tabela de Retenção por Parceiro, define-se, para cada parceiro, se haverá retenção de ISS no município selecionado, independentemente do município onde o parceiro está cadastrado.**

**Aba Outros Impostos**

- Clique no botão “**+**” (**Cadastrar Outros Impostos**)

**PIS**

- Imposto - **2 - PIS RETIDO**
- Tipo do Imposto - **Já incluso**
- Alíquota - **0,65**
- Na Nota - **Já incluso**
- No Financeiro Origem Financeiro - **Nenhum**
- No Financeiro Origem Estoque- **Subtrair**
- **Salve os registros.**

**COFINS**

- Imposto - **3 - COFINS RETIDO**
- Tipo do Imposto **- Já incluso**
- Alíquota - **3,00**
- Na Nota - **Já incluso**
- No Financeiro Origem Financeiro - **Nenhum**
- No Financeiro Origem Estoque- **Subtrair**
- **Salve os registros.**

**CSLL**

- Imposto - **4 - CSLL RETIDO**
- Tipo do Imposto - **Já incluso**
- Alíquota - **1,00**
- Na Nota - **Já incluso**
- No Financeiro Origem Financeiro - **Nenhum**
- No Financeiro Origem Estoque - **Subtrair**
- **Salve os registros.**

**INSS**

- Imposto - **6 - INSS RETIDO**
- Tipo do Imposto - **Já incluso**
- Alíquota - **11,00**
- Na Nota - **Já incluso**
- No Financeiro Origem Financeiro - **Nenhum**
- No Financeiro Origem Estoque - **Subtrair**
- **Salve os registros.**
