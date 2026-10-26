---
id: "360049264134"
titulo: "Geração do DIFAL no Financeiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360049264134-Gera%C3%A7%C3%A3o-do-DIFAL-no-Financeiro"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T15:31:09Z"
rotulos: ["Configuração", "DIFAL", "Portal de Vendas", "Impostos", "Financeiro", "Geração DIFAL financeiro", "Lançamento vendas portal", "Processo FCP similar"]
---

# Geração do DIFAL no Financeiro

![Imagem 1: A geração do DIFAL no financeiro é feita através do Tipo de Negociação, incluindo uma parcela no título com a fórmula…](https://ajuda.sankhya.com.br/hc/article_attachments/15936750722455) A geração do DIFAL no financeiro é feita através do Tipo de Negociação, incluindo uma parcela no título com a fórmula **VLRICMSDIFALDEST**:

- Tela 'Tipos de Negociação' (Comercial » Arquivo » Cadastros) >> Aba 'Parcelas':

![Imagem 2: Tela 'Tipos de Negociação' (Comercial » Arquivo » Cadastros) >> Aba 'Parcelas':](https://ajuda.sankhya.com.br/hc/article_attachments/14472523212439)

Conforme demonstrado abaixo, esse campo refere-se ao 'Valor DIFAL UF Destino' da tabela de Nota/Pedido [TGFCAB]:

![Imagem 3: Conforme demonstrado abaixo, esse campo refere-se ao 'Valor DIFAL UF Destino' da tabela de Nota/Pedido (TGFCAB):](https://ajuda.sankhya.com.br/hc/article_attachments/14472528481047)

![Imagem 4: No portal de vendas, ao efetuar um lançamento de venda, o valor do DIFAL é lido da TGFCAB e depois lançado no…](https://ajuda.sankhya.com.br/hc/article_attachments/15936750723991) No portal de vendas, ao efetuar um lançamento de venda, o valor do DIFAL é lido da TGFCAB e depois lançado no financeiro com o valor do VLRICMSDIFALDEST:

![Imagem 5: No portal de vendas, ao efetuar um lançamento de venda, o valor do DIFAL é lido da TGFCAB e depois lançado no…](https://ajuda.sankhya.com.br/hc/article_attachments/14472566040471)

![Imagem 6: No portal de vendas, ao efetuar um lançamento de venda, o valor do DIFAL é lido da TGFCAB e depois lançado no…](https://ajuda.sankhya.com.br/hc/article_attachments/14472568560663)

**![Atenção](https://ajuda.sankhya.com.br/hc/article_attachments/15936750725911) Importante:**

Para **'Fundo de Combate a Pobreza'** servirá o mesmo processo, mas a fórmula será **VLRICMSFCP** na parcela do tipo de negociação.

**![Imagem 8: Observação:](https://ajuda.sankhya.com.br/hc/article_attachments/15936738404375)Observação:**

Se houver uma compensação financeira no lançamento da Nota Fiscal feita com DIFAL, o sistema a reconhecerá como um título. Sendo assim, o valor da referida Nota Fiscal será afetado, logo é necessário realizar esse lançamento através de um projeto adaptativo."
