---
id: "43548771909783"
titulo: "Como baixar estoque de matéria-prima em OP para terceiros?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548771909783-Como-baixar-estoque-de-mat%C3%A9ria-prima-em-OP-para-terceiros"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-09-30T13:24:23Z"
rotulos: ["Artigo criado KCS", "Produção - KCS"]
---

# Como baixar estoque de matéria-prima em OP para terceiros?

**MENSAGEM**

Ao executar a ordem de produção (OP) para terceiros, o sistema não realiza a baixa da matéria-prima (MP) do estoque de terceiros, impedindo o controle correto do insumo.

**SITUAÇÃO**

Ocorre quando a empresa recebe a matéria-prima do parceiro, transforma em produto acabado e devolve, controlando o estoque de terceiros em poder da empresa. Na configuração do **"Tipo de Operação - TOP"** (Configurações » Cadastros » Tipos de Operação - TOP) de produção para terceiros, a aba **"Estoque de Terceiros"** está ajustada para subtrair a MP e somar o PA no estoque de terceiros em poder da empresa. Ao executar a OP, o sistema gera corretamente a entrada do PA no estoque de terceiros, mas não efetua a baixa da MP do estoque de terceiros.

**SOLUÇÃO**

**(1)** Na aba de matérias-primas da tela **"Composição do Produto"**(Produção » Cadastros » Composição do Produto), confira se a marcação **"Estoque de terceiro"** está habilitada para as MPs que pertencem ao parceiro.

**(2)** Após ajustar as configurações, execute novamente o apontamento e verifique se a baixa da MP do estoque de terceiros ocorre corretamente.

**CAUSA**

A causa principal é a configuração incorreta da TOP utilizada na produção para terceiros, especialmente na aba **"Estoque de Terceiros"**, ou a ausência da marcação **"Estoque de terceiro"** na aba de matérias-primas da composição do produto. Isso impede que o sistema identifique corretamente o estoque a ser movimentado, resultando na baixa incorreta durante a execução da OP.
