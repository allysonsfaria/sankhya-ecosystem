---
id: "35304603013655"
titulo: "CORE_E06983 - Quando o parceiro de pag. do frete está preenchido as outras formas de pagamento devem estar vazias!"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35304603013655-CORE-E06983-Quando-o-parceiro-de-pag-do-frete-est%C3%A1-preenchido-as-outras-formas-de-pagamento-devem-estar-vazias"
trilha: "Solução de Problemas > Distribuição"
atualizado_em: "2026-10-08T17:57:53Z"
rotulos: ["MDF-e", "Parceiro", "Financeiro", "Erro", "Viagens de Transporte (MDF-e)", "CORE_E06983", "Quando o parceiro de pag. do frete está preenchido", "Parceiro de Pag. do Frete", "utras formas de pagamento devem estar vazias", "Pagamento de Frete"]
---

# CORE_E06983 - Quando o parceiro de pag. do frete está preenchido as outras formas de pagamento devem estar vazias!

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/35304632629783) **MENSAGEM:**

[CORE\_E06983] Quando o parceiro de pag. do frete está preenchido as outras formas de pagamento devem estar vazias!

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/35304632631959)SOLUÇÃO:**

**(1)** Acesse a tela  **"Viagens de Transporte (MDF-e)"** (Comercial » Rotinas » Viagens de Transporte (MDF-e)) e identifique o registro que está gerando o erro;

**(2)** Acesse esse registro em questão, nele vá até a até a aba **"MDF-e"**, sub aba **"Pagamento de frete"**, por fim sub aba **"Geral"** e veja se o campo **"Parceiro de Pag. do Frete"** está preenchido;

![Imagem 3: (2) Acesse esse registro em questão, nele vá até a até a aba "MDF-e" , sub aba "Pagamento de frete" , por fim sub aba…](https://ajuda.sankhya.com.br/hc/article_attachments/35675750623895)

**(3)** Caso o campo Parceiro de Pag. do Frete esteja preenchido, os campos abaixo devem estar vazios:

- Banco
- Agência
- Chave Pix

Assim, **limpe** os campos **Banco, Agência e Chave Pix** e **deixe apenas** o campo **Parceiro de Pagamento do Frete preenchido.**

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/35304632632599)CAUSA:**

Quando os dados bancários são informados e já tem os dados de pagamentos  com o parceiro informados para a vista ou a prazo.
