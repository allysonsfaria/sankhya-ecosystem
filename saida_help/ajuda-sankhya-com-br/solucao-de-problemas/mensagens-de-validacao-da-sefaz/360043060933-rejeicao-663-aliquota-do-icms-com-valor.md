---
id: "360043060933"
titulo: "Rejeição 663: Alíquota do ICMS com valor superior a 4% na operação de saída interestadual com produtos importados [nItem:999](NT2015/003)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043060933-Rejei%C3%A7%C3%A3o-663-Al%C3%ADquota-do-ICMS-com-valor-superior-a-4-na-opera%C3%A7%C3%A3o-de-sa%C3%ADda-interestadual-com-produtos-importados-nItem-999-NT2015-003"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:19Z"
rotulos: ["ERRONF", "Produtos", "Configuração", "NF-e", "SEFAZ", "ICMS", "Impostos", "Alíquotas de ICMS", "663", "Ajuste cadastro e refaça nota", "Rejeição ICMS superior a 4%", "Verifique origem e alíquota", "Rejeição 663"]
---

# Rejeição 663: Alíquota do ICMS com valor superior a 4% na operação de saída interestadual com produtos importados [nItem:999](NT2015/003)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16474949709207) MENSAGEM:**

[663] - Rejeição: Alíquota do ICMS com valor superior a 4 por cento na operação de saída interestadual com produtos importados [nItem:999](NT2015/003).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16474977305495) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a tela de cadastro de " Produtos " (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos ), vá até…](https://ajuda.sankhya.com.br/hc/article_attachments/16474949714839) Acesse a tela de cadastro de "**[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)"** (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos), vá até a aba "**Geral"** e verifique:

- **"Origem do Produto":** observe o Código correspondente neste campo

Caso seja uma Operação Interestadual e a **Origem da Mercadoria seja 1, 2, 3 ou 8** e a Tributação(CST) for 00, 10, 20, 70 ou 90, o  valor da alíquota de ICMS deverá ser **4%**.

![Imagem 4: Sintonize com seu contador, caso a 'Origem do produto' esteja correta, acesse o cadastro de " Alíquotas de ICMS "…](https://ajuda.sankhya.com.br/hc/article_attachments/16474949717527) Sintonize com seu contador, caso a 'Origem do produto' esteja correta, acesse o cadastro de "**[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)"** (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas), pesquise pela regra de ICMS que incidiu na nota e realize os devidos ajustes do Percentual(%) de Alíquota de ICMS. É importante que esse ajuste seja realizado por um usuário certificado na utilização do sistema, que compreenda os impactos e exceções vinculados a esse ajuste.

![Imagem 5: Finalizado os devidos ajustes, lance novamente a nota ou redigite os itens na nota e gere lote/Buscar Autorização.](https://ajuda.sankhya.com.br/hc/article_attachments/16474949721879) Finalizado os devidos ajustes, lance novamente a nota ou redigite os itens na nota e gere lote/Buscar Autorização.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16474977313175) CAUSA:**

Quando for emitida uma NF-e sob todas as circunstâncias abaixo, será retornada a rejeição.

Se a Operação Interestadual de Saída, onde os Campos idDest = 2 e tpNF = 1;
idDest = Indicador de Destino da Mercadoria; tpNF = Tipo da NF-e.

1. **Se a Origem da Mercadoria igual a 1, 2, 3 ou 8;**
   1 = Estrangeira - Importação direta, exceto a indicada no código 6;
   2 = Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7;
   3 = Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%;
   8 = Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%.
2. **Se o CST de ICMS igual a 00, 10, 20, 70 ou 90;**
   00 = Tributada integralmente;
   10 = Tributada e com cobrança do ICMS por substituição tributária;
   20 = Tributação com redução de base de cálculo;
   70 = Tributação ICMS com redução de base de cálculo e cobrança do ICMS por substituição tributária;
   90 = Tributação ICMS: Outros.
3. **Se a Data de Emissão igual ou superior a 01/01/2013** (apesar de ainda presente na regra de validação, não pode-se emitir NF-es com datas muito antigas);
4. **Se o Valor da alíquota do ICMS maior do que "4.00%**" (quatro por cento).

**![Imagem 7: OBSERVAÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16474949728919) OBSERVAÇÃO:**

([**NT2015/003**](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=1MUP2q/QTuQ=)) - Nota Técnica.
