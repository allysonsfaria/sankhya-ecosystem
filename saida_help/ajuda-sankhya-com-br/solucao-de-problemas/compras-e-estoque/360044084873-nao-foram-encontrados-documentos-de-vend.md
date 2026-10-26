---
id: "360044084873"
titulo: "Não foram encontrados documentos de venda, devolução de compra, devolução de venda, transferência ou conhecimento de transporte na(s) ordem(ns) de carga o modelo de documento 1, 1B, 4, 8, 55 ou 57"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044084873-N%C3%A3o-foram-encontrados-documentos-de-venda-devolu%C3%A7%C3%A3o-de-compra-devolu%C3%A7%C3%A3o-de-venda-transfer%C3%AAncia-ou-conhecimento-de-transporte-na-s-ordem-ns-de-carga-o-modelo-de-documento-1-1B-4-8-55-ou-57"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-08-10T16:22:08Z"
rotulos: ["#RevisadoGui", "ERROMDFE", "COM_E00041", "MDF-e", "SEFAZ", "Transporte", "COM_E00043", "Problema de Geração de MDF-e para Nota de Compra: Documentos Ausentes na Ordem de Carga", "Documentos Eletrônicos"]
---

# Não foram encontrados documentos de venda, devolução de compra, devolução de venda, transferência ou conhecimento de transporte na(s) ordem(ns) de carga o modelo de documento 1, 1B, 4, 8, 55 ou 57

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16106725678103) MENSAGEM:**

[COM\_E00041] Não foram encontrados documentos de venda, devolução de compra, devolução de venda, transferência ou conhecimento de transporte na(s) ordem(ns) de carga o modelo de documento 1, 1B, 4, 8, 55 ou 57.

[COM\_E00043] Não foram encontrados documentos de venda, compra, devolução de compra, devolução de venda, transferência ou conhecimento de transporte na(s) ordem(ns) de carga o modelo de documento 1, 1B, 4, 8, 55 ou 57.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16106725678743) SOLUÇÃO:**

Quando se tratar de Nota de Compra, a melhor prática pra gerar a MDF-e é a seguinte:

![Imagem 3: Efetue o lançamento da nota de Compra, inserindo as informações de Chave e Número da nota - NÃO CONFIRMAR.](https://ajuda.sankhya.com.br/hc/article_attachments/16106725681943) Efetue o lançamento da nota de Compra, inserindo as informações de Chave e Número da nota - NÃO CONFIRMAR.

![Imagem 4: Não vincule a Nota de Compra a uma OC (Ordem de Carga).](https://ajuda.sankhya.com.br/hc/article_attachments/16106725682839) Não vincule a Nota de Compra a uma OC (Ordem de Carga).

![Imagem 5: Acesse a Rotina: Comercial » Rotinas » Viagens de Transporte (MDF-e) e crie a Viagem. Na aba: Geral , marque o campo:…](https://ajuda.sankhya.com.br/hc/article_attachments/16106741226519) Acesse a Rotina: Comercial » Rotinas » Viagens de Transporte (MDF-e) e crie a Viagem.
Na aba: **Geral**, marque o campo: **"Contem documentos de Terceiros [X]**".

![Imagem 6: Aba: MDF-e » Sub-aba: Documentos MDF-e Pesquise pela Nota de Compra, anteriormente lançado.](https://ajuda.sankhya.com.br/hc/article_attachments/16106725685143) Aba: **MDF-e** » Sub-aba: **Documentos MDF-e**
Pesquise pela Nota de Compra, anteriormente lançado.

Preencha os principais campos da Viagem, necessários e obrigatórios para geração da MDF-e.

![Imagem 7: Transmita a MDF-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16106725686039) Transmita a MDF-e.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16106725690647) CAUSA:**

Ocorre quando no Lançamento de uma MDF-e, para uma nota de Compra, não foi marcado a opção que a MDF-e é para Documentos de Terceiros.
