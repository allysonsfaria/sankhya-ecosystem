---
id: "4423035314071"
titulo: "Atenção! A TOP está com a opção \"Buscar NF de origem p/ referenciar na NFe\": DESMARCADA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4423035314071-Aten%C3%A7%C3%A3o-A-TOP-est%C3%A1-com-a-op%C3%A7%C3%A3o-Buscar-NF-de-origem-p-referenciar-na-NFe-DESMARCADA"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:19:20Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "TOP", "Devolução", "#validadoFernanda", "#causaraiz", "opção desmarcada", "marcar a opção", "exigência da SEFAZ", "Documentos Eletrônicos"]
---

# Atenção! A TOP está com a opção "Buscar NF de origem p/ referenciar na NFe": DESMARCADA

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16305876364439) MENSAGEM:**

Atenção! A TOP está com a opção "Buscar NF de origem p/ referenciar na NFe": DESMARCADA. Verifique, pois a SEFAZ exige esta informação para validação.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16305883886103) SOLUÇÃO:**

![Imagem 3: Acesse a tela "Tipos de Operação-TOP" , selecione a TOP de Devolução utilizada, localize a marcação "Buscar NF de…](https://ajuda.sankhya.com.br/hc/article_attachments/16305876374423) Acesse a tela **"Tipos de Operação-TOP"**, selecione a TOP de Devolução utilizada, localize a marcação **"Buscar NF de origem p/ referenciar na NFe"** e marque essa opção, conforme print abaixo:

![Imagem 4: Acesse a tela "Tipos de Operação-TOP" , selecione a TOP de Devolução utilizada, localize a marcação "Buscar NF de…](https://ajuda.sankhya.com.br/hc/article_attachments/15752521892375)

![Imagem 5: Refaça o lançamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16305883890583) Refaça o lançamento.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16305883893655) CAUSA:**

Conforme **NT2013/005,** a SEFAZ exige NF-e referenciada, nas seguintes condições:

**(1)** Quando for emitida uma NF-e com finalidade igual à "4 - Devolução de mercadoria" e não for informado documento referenciado que está sendo devolvido, será retornado a rejeição: 321 - Rejeição: NF-e de devolução de mercadoria não possui documento fiscal referenciado.

Dessa forma, foi criado o parâmetro **"VALNFDEVDOCREF", que se ligado:**

**(1)** Avisará o cliente sobre essa necessidade durante o lançamento de uma NF-e de devolução avulsa, sem NF-e referenciada.

**(1)**Impedirá que uma TOP seja criada/alterada sem que a opção Buscar NF-e de origem para referenciar esteja marcada.
