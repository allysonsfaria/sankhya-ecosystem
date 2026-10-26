---
id: "30745417324951"
titulo: "835 Rejeição: Produto Agrotóxico Informado sem Número da Receita do Defensivo Agrícola"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30745417324951-835-Rejei%C3%A7%C3%A3o-Produto-Agrot%C3%B3xico-Informado-sem-N%C3%BAmero-da-Receita-do-Defensivo-Agr%C3%ADcola"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:34:48Z"
rotulos: ["Produtos", "Fiscal", "NF-e", "SEFAZ", "CFOP", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Produto Agrotóxico Informado", "sem Número da Receita do Defensivo Agrícola", "Rejeição 835", "Erro", "NCMs relacionados como 3808.52.00 3808.59.2", "835 Rejeição"]
---

# 835 Rejeição: Produto Agrotóxico Informado sem Número da Receita do Defensivo Agrícola

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30745431112599) **MENSAGEM:**

835 Rejeição: Produto Agrotóxico Informado sem Número da Receita do Defensivo Agrícola.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30745417316503)SOLUÇÃO:**

Essa rejeição ocorre quando algum item da **Nota Fiscal Eletrônica (NF-e)** contém um produto classificado como **Defensivo Agrícola** (NCMs relacionados, como **3808.52.00, 3808.59.2X, 3808.6X.XX**, entre outros), mas não foi informado o número da receita ou receituário, quando a finalidade da nota (**finNFe**) é **1 - normal** e o destinatário é **1 - consumidor final**.

**Exceções:**

**![Imagem 3: Operações de Retorno de Mercadorias: a regra não se aplica quando a operação é um retorno de mercadorias;](https://ajuda.sankhya.com.br/hc/article_attachments/30767586434455) Operações de Retorno de Mercadorias:** a regra não se aplica quando a operação é um retorno de mercadorias;

**![Imagem 4: Operações de Transferência de Mercadorias: a regra também não se aplica para operações de transferência de mercadorias,…](https://ajuda.sankhya.com.br/hc/article_attachments/30767600873751) Operações de Transferência de Mercadorias:** a regra também não se aplica para operações de transferência de mercadorias, com os CFOPs entre **X.151** a **X.156.**

Essa regra entrou em vigor no 04/11/2024 em ambiente homologação e entrará a partir do dia 01/04/2025 em ambiente de produção, conforme estabelecido na [**NT 2024.003**](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=7fsG1qp0vrU=).

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30745447893015)CAUSA:**

A rejeição é gerada apenas quando não há receita/receituário associado ao defensivo agrícola em uma operação normal e o destinatário é o consumidor final.
