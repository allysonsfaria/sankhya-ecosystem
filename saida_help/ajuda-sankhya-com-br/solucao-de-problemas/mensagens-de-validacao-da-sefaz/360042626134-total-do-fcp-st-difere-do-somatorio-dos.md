---
id: "360042626134"
titulo: "Total do FCP ST difere do somatorio dos itens.(NT2016/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042626134-Total-do-FCP-ST-difere-do-somatorio-dos-itens-NT2016-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:19Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "862", "Divergência no Total do FCP ST", "FCP ST"]
---

# Total do FCP ST difere do somatorio dos itens.(NT2016/002)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16086365844631) MENSAGEM:**

862-Rejeição: Total do FCP ST difere do somatório dos itens.(NT2016/002)

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16086336676631) SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

Geralmente estas divergências estão relacionadas a arredondamentos e/ou conversões de casas decimais. Abaixo, trecho do Manual do Contribuinte onde considera uma tolerância de R$ 0,01 para mais ou para menos:

O valor resultante da multiplicação deve ser arredondado para um valor numérico com duas casas decimais. Considerar uma tolerância de R$ 0,01 para mais ou para menos na validação.

Porém há situações em que algumas **Secretarias Estaduais** não permitem o arredondamento.

Considere o cálculo da seguinte forma: Exemplo do cálculo considerado pela Sefaz

- vFCPST [Total] **=** vFCPST [item 1] **+** vFCPST [item 2]
- vFCPST [Total] **=** 2.49 **+** 2.49
- vFCPST [Total] **=** 4.98

No sistema considere analisar o XML de Conferência (Portal de Vendas>>Botão NF-e>>Gerar XML de NF-e em arquivo para Conferência).

Analisar em cada item o valor do campo **vFCPST**onde a soma do valor desse campo, seja o total no campo **vFCPST** do grupo de Totais.

![Imagem 3: Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/article_attachments/16086336677783) Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS

- aba: **"Substituição Tributária"**
- Campo **"% ST FCP Interno":** verifique o percentual de acordo com a [Tabela de Alíquotas de FCP por UF](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=TKvyZLZP3cA=) da SEFAZ

![Imagem 4: Acesse: Configurações » Cadastros » Produtos » Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/16086365852311) Acesse: Configurações » Cadastros » Produtos » Produtos

- Aba: **"Impostos"**
- Campo **"Tipo de Substituição":** Subst. na compra e na venda

![Imagem 5: Acesse: Configurações » Cadastros » Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/16086365854743) Acesse: Configurações » Cadastros » Parceiros

- Aba: **"Fiscal"**
- Campo **"Classificação ICMS":** 'Revendedor'

![Imagem 6: Feito as conferências e ajustes, gere o Lote novamente. Considere entrar em contato com o Service Desk Sankhya, caso o…](https://ajuda.sankhya.com.br/hc/article_attachments/16086336689559) Feito as conferências e ajustes, gere o Lote novamente. Considere entrar em contato com o Service Desk Sankhya, caso o problema persista e os valores no XML estejam corretos.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16086336692247) CAUSA:**

Quando for emitida uma NF-e (modelo 55) e o total do FCP ST, calculado no grupo de totais da NF-e, for diferente do somatório do FCP ST dos itens que fazem parte do cálculo, haverá a rejeição.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16086336693399) OBSERVAÇÃO:**

1- (**NT2016/002**)

Nota Técnica:

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=uvfnqOj%20spg=>
