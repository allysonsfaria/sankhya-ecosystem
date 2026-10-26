---
id: "360042624194"
titulo: "Total do IPI difere do somatório dos itens (NT2010/010)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042624194-Total-do-IPI-difere-do-somat%C3%B3rio-dos-itens-NT2010-010"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:44Z"
rotulos: ["ERRONF", "Configuração", "Fiscal", "NF-e", "SEFAZ", "Impostos", "538", "Divergência no Total do IPI", "Erro"]
---

# Total do IPI difere do somatório dos itens (NT2010/010)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16447570415639) MENSAGEM:**

[538-Rejeição]: Total do IPI difere do somatório dos itens (NT2010/010).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16447548917399) SOLUÇÃO:**

Para correção siga os passos abaixo:

![Imagem 3: Acesse " Empresa " (Caminho de acesso: Comercial » Preferências » Empresa ), Aba: " Propriedades" e verifique se o…](https://ajuda.sankhya.com.br/hc/article_attachments/16447548920343) Acesse "[**Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)" (Caminho de acesso: Comercial » Preferências » Empresa), Aba: "**Propriedades"** e verifique se o campo: "**Trabalha com IPI"** está marcado (se equiparado a Indústria);

![Imagem 4: Acesse " Parceiros " (Caminho de acesso: Configurações » Cadastros » Parceiros ), Aba: " Fiscal" e verifique o campo: "…](https://ajuda.sankhya.com.br/hc/article_attachments/16447570431895) Acesse "[**Parceiros**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)" (Caminho de acesso: Configurações » Cadastros » Parceiros), Aba: "**Fiscal"** e verifique o campo: "**Código Sit.Trib.IPI** **Saída**:" está preenchido com: 99- Outras Saídas

![Imagem 5: Acesse " Produtos " (Caminho de acesso: Configurações » Cadastros » Produtos ), Aba: " Impostos" e confirmar os itens:](https://ajuda.sankhya.com.br/hc/article_attachments/16447570434199) Acesse "[**Produtos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)" (Caminho de acesso: Configurações » Cadastros » Produtos), Aba: "**Impostos"** e confirmar os itens:

- "**Tem IPI na venda**" = marcado
- "**Tem IPI na Compra"** = marcado
- **"Código Sit.Trib.IPI Saída**:" = 99-Outras Saídas

![Imagem 6: Acesse Configurações » Cadastros » Produtos e verifique no Produto o Código do IPI, e pesquise o nesta tela e ajuste os…](https://ajuda.sankhya.com.br/hc/article_attachments/16447548926743) Acesse Configurações » Cadastros » Produtos e verifique no Produto o Código do IPI, e pesquise o nesta tela e ajuste os campos:

- **"Cód.Sit.Trib.IPI Saída:**"= 99-Outras Saídas
- **"Cód.Sit.Trib.IPI Entrada:"** = 49-Outras Entradas

![Imagem 7: Após o ajuste, gere uma nova nota de Devolução e um Lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16447548928663) Após o ajuste, gere uma nova nota de Devolução e um Lote.

**![Imagem 8: OBSERVAÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16447548929687) OBSERVAÇÃO:**

Deve consultar o contador da empresa para saber qual Cód.Sit.Trib.IPI correto a ser usado no seu lançamento.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16447548931351) CAUSA:**

Quando for emitida uma NF-e com o Total do IPI da NF-e diferente do somatório do valor do IPI de cada item, será retornado a rejeição.

O cálculo do Total do IPI é feito a partir do somatório do valor do IPI de cada item.

Dependendo do Cód.Sit.Trib.IPI usado no lançamento, o IPI será calculado no sistema e não será carregado para o XML, por ser uma CST de IPI não prevista no grupo de tags.

**![Imagem 10: OBSERVAÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16447548929687) OBSERVAÇÃO:**

([NT2010/010](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=AtaVevRXCIQ=)) Nota Técnica.
