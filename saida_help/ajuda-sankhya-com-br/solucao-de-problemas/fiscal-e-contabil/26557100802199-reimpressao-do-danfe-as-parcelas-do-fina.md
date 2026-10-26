---
id: "26557100802199"
titulo: "Reimpressão do Danfe as parcelas do financeiro estão saindo diferente do que está no sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26557100802199-Reimpress%C3%A3o-do-Danfe-as-parcelas-do-financeiro-est%C3%A3o-saindo-diferente-do-que-est%C3%A1-no-sistema"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:41:21Z"
rotulos: ["Configuração", "NF-e", "Movimentação Financeira", "XML", "DANFE", "Preferências", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Reimpressão do Danfe", "parcelas do financeiro estão saindo diferente"]
---

# Reimpressão do Danfe as parcelas do financeiro estão saindo diferente do que está no sistema

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26647498350103) **SITUAÇÃO:**

Reimpressão do Danfe as parcelas do financeiro estão saindo diferente do que está no sistema.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26557100797591)SOLUÇÃO:**

Neste caso a solução está ligada ao parâmetro **"Imprimir faturas no DANFE pelo xml- FINANCEXMLDANFE"** (Caminho: Configurações » Avançado » Preferências):

- **Quando ligado**, ao imprimir o DANFE, será impresso em conformidade com o XML da nota;
- **Quando desligado** será impresso em conformidade com o financeiro da nota.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26557087016855)CAUSA:**

Ocorre quando por algum motivo o é alterado a data de vencimento de um financeiro na movimentação

financeira por algum motivo e o parâmetro está FINANCEXMLDANFE ligado.
