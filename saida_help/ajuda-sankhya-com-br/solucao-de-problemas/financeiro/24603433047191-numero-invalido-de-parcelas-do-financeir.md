---
id: "24603433047191"
titulo: "Número inválido de parcelas do financeiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24603433047191-N%C3%BAmero-inv%C3%A1lido-de-parcelas-do-financeiro"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:46:34Z"
rotulos: ["Configuração", "Movimentação Financeira", "TOP", "Financeiro", "COM_E00220", "Erro"]
---

# Número inválido de parcelas do financeiro

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/24603462733079) **MENSAGEM:**

[COM\_E00220] Número inválido de parcelas do financeiro

![Imagem 2: SOLUÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/24603462735767) **SOLUÇÃO**

A mensagem é exibida quando é realizada uma tentativa de exclusão das parcelas da aba Financeiro dentro das centrais. Neste caso é necessário avaliar a situação da nota e se realmente tem a necessidade de gerar financeiro.

Atualmente não é permitida a exclusão integral das parcelas de uma nota lançada. Se é necessário o lançamento de uma nota que não tenha nenhuma parcela financeira, a sugestão é que faça novamente o lançamento da nota usando uma TOP que não gere financeiro.

Para verificar se a TOP gera financeiro, acesse a tela **"Tipos de Operação - TOP"**, busque pela TOP desejada, vá até a aba geral e observe qual informação está marcada no campo **"Financeiro"**. Ele deve estar com a opção **"Não atualizar"**.

![Imagem 3: Para verificar se a TOP gera financeiro, acesse a tela "Tipos de Operação - TOP" , busque pela TOP desejada, vá até a…](https://ajuda.sankhya.com.br/hc/article_attachments/24603433031319)

![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/24603462744215)**CAUSA:**

O erro é apresentado ao tentar excluir o financeiro de uma nota lançada e na qual é usada uma TOP que gera financeiro.
