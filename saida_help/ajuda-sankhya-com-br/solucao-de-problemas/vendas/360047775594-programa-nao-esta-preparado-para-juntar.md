---
id: "360047775594"
titulo: "Programa não está preparado para juntar Atualizações de Estoque diferentes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360047775594-Programa-n%C3%A3o-est%C3%A1-preparado-para-juntar-Atualiza%C3%A7%C3%B5es-de-Estoque-diferentes"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:31:47Z"
rotulos: ["Configuração", "Atualização", "TOP", "Estoque", "CORE_E04632", "Atualizações de estoque diferentes não podem ser juntadas", "Documentos com diferentes configurações de atualização de estoque", "Verifique e ajuste os tipos de operação; documents precisam ter configurações iguais", "Erro"]
---

# Programa não está preparado para juntar Atualizações de Estoque diferentes

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18667058902807) MENSAGEM:**

[CORE\_E04632] Programa não está preparado para juntar Atualizações de Estoque diferentes.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18667058912535) CAUSA:**

Mensagem será apresentada ao tentar juntar/faturar documentos que possuem atualizações de estoque diferentes [Campo ATUALESTOQUE].

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18667058922135) SOLUÇÃO:**

![Imagem 4: Verifique dentre todos os documentos que estão sendo faturados, quais os 'Tipos de Operação' utilizados.](https://ajuda.sankhya.com.br/hc/article_attachments/18667018375191)Verifique dentre todos os documentos que estão sendo faturados, quais os 'Tipos de Operação' utilizados.

![Imagem 5: Acesse a tela Tipos de Operação-TOP (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verificar para as…](https://ajuda.sankhya.com.br/hc/article_attachments/18667058930839) Acesse a tela **Tipos de Operação-TOP** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verificar para as TOP'S utilizadas como está configurado o campo **"Atualização do Estoque"** [Aba Estoque].

- **NÃO** será permitido "juntar/faturar" **documentos que possuem atualizações de estoque distintas**.
- Dessa forma, reavalie essa marcação, e realize os ajustes necessários.

**Importante:**

- Os documentos lançados com a TOP que teve essa informação alterada, deverão ser **lançados novamente** para que a nova informação do campo seja lida.
- Caso a configuração de atualização de estoque das TOP'S de fato devam ser diferentes, será necessário que o faturamento desses documentos ocorra de forma separada [Juntando apenas os que possuem a mesma "atualização de estoque"].
