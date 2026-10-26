---
id: "39361858614807"
titulo: "Valor do IPI não está deduzindo da base do PIS/COFINS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39361858614807-Valor-do-IPI-n%C3%A3o-est%C3%A1-deduzindo-da-base-do-PIS-COFINS"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-08-13T16:34:55Z"
rotulos: ["Configuração", "Parceiro", "IPI", "Impostos", "Financeiro", "Artigo criado KCS", "PIS/COFINS", "Fiscal/Contábil - KCS"]
---

# Valor do IPI não está deduzindo da base do PIS/COFINS

**MENSAGEM**

O valor do IPI não está sendo deduzido da base de cálculo do PIS e COFINS.

**SITUAÇÃO**

Ao realizar operações fiscais, o sistema não está deduzindo automaticamente o valor do IPI da base de cálculo do PIS e COFINS, mesmo quando essa dedução deveria ocorrer conforme a configuração tributária da empresa.

**SOLUÇÃO**

Para que o IPI seja deduzido da base de cálculo do PIS e COFINS, configure o parâmetro no cadastro do parceiro:

**(1)** Acesse a tela **"Parceiros"** (Configurações Cadastros Parceiros).

**(2)** Localize e selecione o parceiro desejado.

**(3)** Na aba Fiscal, localize o campo **"Deduzir valor de IPI da BC do PIS e COFINS"** e ative a flag.

**(4)** Salve as alterações realizadas.

![Imagem 1: (1) Acesse a tela "Parceiros" (Configurações Cadastros Parceiros). (2) Localize e selecione o parceiro desejado. (3) Na…](https://ajuda.sankhya.com.br/hc/article_attachments/42696540973335)

**CAUSA**

O campo **"Deduzir valor de IPI da BC do PIS e COFINS"** no cadastro do parceiro está configurado com o valor padrão **"N"**. Quando este campo está marcado como **"N"**, o sistema não realiza a dedução do IPI da base de cálculo do PIS e COFINS, mantendo o valor do IPI compondo a base destes tributos.

A configuração correta deste parâmetro é essencial para garantir que os cálculos tributários sejam realizados de acordo com as regras fiscais aplicáveis à operação e ao regime tributário da empresa.
