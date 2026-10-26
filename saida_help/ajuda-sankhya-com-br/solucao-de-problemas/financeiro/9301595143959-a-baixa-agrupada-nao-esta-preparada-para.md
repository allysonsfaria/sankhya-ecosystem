---
id: "9301595143959"
titulo: "A baixa agrupada não está preparada para títulos de parceiros diferentes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9301595143959-A-baixa-agrupada-n%C3%A3o-est%C3%A1-preparada-para-t%C3%ADtulos-de-parceiros-diferentes"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:08:56Z"
rotulos: ["Configuração", "Parceiro", "Movimentação Financeira", "Financeiro", "CORE_E03693", "Baixa Agrupada", "Parceiros Diferentes", "Erro"]
---

# A baixa agrupada não está preparada para títulos de parceiros diferentes

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16694237234455) MENSAGEM:**

[CORE\_E03693]: A baixa agrupada não está preparada para títulos de parceiros diferentes.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16694192850711) SITUAÇÃO:**

Ao tentar fazer uma baixa agrupada a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16694237242135)SOLUÇÃO:**

Pela movimentação financeira, o sistema gera uma renegociação e baixa somente o titulo novo. Desta maneira, não é permitido fazer com mais de um parceiro, pois titulo de destino pode ter apenas um parceiro.
Para essa questão existe a rotina de Baixa automática, na qual pode ser feita a baixa de vários títulos e de parceiros diferentes, pois renegociação não é feita por essa rotina.
Na rotina de baixa automática pode-se fazer a baixa dos títulos de parceiros diferentes selecionando-os todos de uma vez.

Clicando em baixar será apresentada a tela de confirmação de baixa na qual deverá flegar o campo **"Baixa Separada",** com isso os títulos serão mantidos de forma individual na movimentação financeira.

![Imagem 4: Clicando em baixar será apresentada a tela de confirmação de baixa na qual deverá flegar o campo "Baixa Separada", com…](https://ajuda.sankhya.com.br/hc/article_attachments/16694237245079)

A baixa agrupada será definida pela movimentação financeira ou baixa automática através da configuração do parâmetro **"OFEROPCBAIXTIT-BAIXA DE MÚLTIPLOS TÍTULOS":**

![Imagem 5: A baixa agrupada será definida pela movimentação financeira ou baixa automática através da configuração do parâmetro…](https://ajuda.sankhya.com.br/hc/article_attachments/9301364241559)

O parâmetro **"Baixa de múltiplos títulos - OFEROPCBAIXTIT"** pode influenciar na rotina de baixa de três maneiras:

- Se definido como **"Baixa com Renegociação"**, será possível nas rotinas de Movimentação Financeira e [Acerto de Ordem de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga), efetuar a seleção e posterior baixa de múltiplos títulos de uma única vez. Este procedimento implica na realização de uma baixa agrupada, de modo que os títulos selecionados serão incorporados em um único título;
- Uma vez que o parâmetro citado esteja determinado com a opção **"Não permitir"**, não será possível proceder com a baixa de múltiplos títulos ao utilizar-se da Movimentação Financeira e do Acerto de Ordem de Carga. Persistindo a tentativa de baixa, o sistema irá proceder com esta ação apenas para o primeiro título selecionado, mesmo que vários títulos tenham sido assinalados.
- Optando-se pela opção **"Baixa Automática"**, você pode efetuar nas rotinas de Movimentação Financeira e Acerto de Ordem de Carga a baixa de múltiplos títulos de uma única vez; sem gerar a renegociação dos mesmos. Deste modo, temos a baixa individual de cada título.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16694192856343)CAUSA:**

Ao tentar fazer a baixa agrupada quando o parâmetro OFEROPCBAIXTIT estiver definido como baixa com renegociação.
