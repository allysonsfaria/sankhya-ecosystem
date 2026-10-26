---
id: "360042506754"
titulo: "Total do vOutro difere do somatório dos itens(NT2011/04)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042506754-Total-do-vOutro-difere-do-somat%C3%B3rio-dos-itens-NT2011-04"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-08-04T18:22:16Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "Impostos", "TOP", "604", "Divergência no Total do vOutro", "Erro"]
---

# Total do vOutro difere do somatório dos itens(NT2011/04)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16457683600023) MENSAGEM:**

[604-Rejeição]: Total do vOutro difere do somatório dos itens(NT2011/04).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16457683604887) SOLUÇÃO:**

**(1)** **Nota de Venda, Devolução de Compra(Emissão Própria) ou Devolução de Compra (Nota de Importação)**

![Imagem 3: Quando destacar um valor no campo " Vlr. Destaque" ou " Vlr. Outros" no rodapé da nota, efetue a configuração na TOP:](https://ajuda.sankhya.com.br/hc/article_attachments/16457683606807) Quando destacar um valor no campo "**Vlr. Destaque"** ou "**Vlr. Outros"** no rodapé da nota, efetue a configuração na TOP:

- Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP, aba: "**Despesas Acessórias"**

- ICMS proporcional ao ICMS dos Itens [x] - Todas as opções
- PIS proporcional ao ICMS dos Itens [x] - Todas as opções
- COFINS proporcional ao ICMS dos itens [x] - Todas as opções

**![Imagem 4: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16457683613207) OBSERVAÇÃO:**

Acessar o sistema com o usuário SUP ou usuário que tenha permissão para os ajustes necessários. Após os ajustes, lance/fature novamente a nota.

(1)** Nota de Nacionalização/Importação (Lançado diretamente da Central de Compras)**

O valor do Destaque informado no rodapé da nota é composto por:

Valor do ICMS de Importação + PIS de Importação + COFINS de Importação + Despesas Aduaneiras(SISCOMEX), que deve ser proporcionalizado entre os itens de forma manual.

![Imagem 5: Efetue a configuração na TOP:](https://ajuda.sankhya.com.br/hc/article_attachments/16457683606807) Efetue a configuração na TOP:

**-** Acesse: Comercial » Arquivo » Cadastros » "**Tipos de Operação - TOP"**, aba: "**Impostos"**

- Não Calcula e Digita

- Acesse: Comercial » Arquivo » Cadastros » "**Tipos de Operação - TOP"**, aba: "**Despesas Acessórias"**

- ICMS proporcional ao ICMS dos Itens [ ] - Todas as opções desmarcadas
- PIS proporcional ao PIS dos Itens  [ ] - Todas as opções desmarcadas
- COFINS proporcional ao COFINS dos itens [ ] - Todas as opções desmarcadas
- IPI proporcional ao IPI dos itens [ ] - Todas as opções desmarcadas
- S.T. proporcional ao S.T. dos itens [ ] - Todas as opções desmarcadas

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16457683617687) CAUSA:**

Quando for emitida uma NF-e com o Total das Despesas Acessórias / Outras Despesas  diferente do somatório do Valor das Despesas Acessórias de cada item, será retornado a rejeição.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16457683613207) OBSERVAÇÃO:**

![Imagem 8: ( NT2011/04 ) - Nota Técnica.](https://ajuda.sankhya.com.br/hc/article_attachments/16457683606807) ([NT2011/04](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=ysYXxjwjYyk=)) - Nota Técnica.

**![Imagem 9: "Parâmetros":](https://ajuda.sankhya.com.br/hc/article_attachments/16457683618967) "Parâmetros":**

(2)**"VOUTITEMSEMICMS"**- Importação, tag vOutro do item sem valor do ICMS

Em determinados casos, empresas podem optar por não destacar o ICMS, para compor o Valor de Destaque (**vOutro**), então poderá optar por desligar o parâmetro "**VOUTITEMSEMICMS"**.

O valor será composto pelo: "Valor das Despesas Aduaneiras + Vlr.PIS Importação + Vlr.COFINS Importação" do item.

(2)**"SEPVIIVPRODNFE"-** Separar <vII> do <vProd> no XML da NFE de compra?

Em determinados casos, empresas podem optar por não destacar o Imposto de Importação(**vII**), para compor o valor do Destaque(**vOutro**), então poderá ligar o parâmetro "**SEPVIIVPRODNFE"** e embutir/majorar o valor do Imposto ao valor unitário total de cada item.

Na geração do XML o sistema irá destacar o Valor de Imposto de Importação em campos próprios, desembutindo do valor total do produto, porém a composição do Total da Nota ficará correto.
