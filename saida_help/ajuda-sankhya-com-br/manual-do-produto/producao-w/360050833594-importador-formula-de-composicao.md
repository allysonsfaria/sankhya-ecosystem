---
id: "360050833594"
titulo: "Importador Fórmula de Composição"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360050833594-Importador-F%C3%B3rmula-de-Composi%C3%A7%C3%A3o"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:56:23Z"
rotulos: ["Produtos", "Fórmulas", "Importação", "Estoque", "Processo Produtivo", "Produção", "br.com.sankhya.prod.ImportadorFormulaComposicao"]
---

# Importador Fórmula de Composição

| ``` ![Imagem 1: Módulo: Produção > Rotinas Versão disponível: A partir da 4.1](https://ajuda.sankhya.com.br/hc/article_attachments/42312835757079) Módulo: Produção > Rotinas                ![Imagem 2: Módulo: Produção > Rotinas Versão disponível: A partir da 4.1](https://ajuda.sankhya.com.br/hc/article_attachments/42312835758871) Versão disponível: A partir da 4.1 ``` |
| --- |

---

Esta rotina tem por objetivo converter a fórmula de composição de produtos em Processos Produtivos.

![Imagem 3: Esta rotina tem por objetivo converter a fórmula de composição de produtos em Processos Produtivos.](https://ajuda.sankhya.com.br/hc/article_attachments/4785626024215)

Observe abaixo, alguns detalhes a respeito da importação:

↪ As etapas de produção de uma fórmula se transformam em um Processo Produtivo;

↪ Cada fórmula de composição se transforma em uma composição de produto para o       processo produtivo criado;

↪ As fórmulas de composição que utilizam as mesmas etapas de produção em uma          mesma sequência, darão origem a um único Processo Produtivo;

↪ Fórmulas de composição de um produto com as mesmas etapas e sequência de            produção, são conflitantes e precisaram ser ajustadas manualmente.

Ao importar as fórmulas, será criada uma operação de estoque do tipo nota de produção (fabricação de produtos) na última atividade dos processos. Para isso, é necessário informar o **"Modelo de nota"**, o **"Parceiro"**, o **"Tipo de operação"** e a **"Empresa"** no pop-up **"Operação de estoque (Nota de produção)"**:

![Imagem 4: Ao importar as fórmulas, será criada uma operação de estoque do tipo nota de produção (fabricação de produtos) na…](https://ajuda.sankhya.com.br/hc/article_attachments/4786417647255)

Se ao importar a fórmula, houver algum tipo de variação, ou conflito, o processo produtivo e produto acabado serão criados, porém, sem matérias-primas. Será necessário solucionar o conflito, ou seja, definir MPs principais e MPs alternativas para que estas sejam importadas para o processo/PA em questão.

![Imagem 5: Se ao importar a fórmula, houver algum tipo de variação, ou conflito, o processo produtivo e produto acabado serão…](https://ajuda.sankhya.com.br/hc/article_attachments/4787639729943)

O botão ![Imagem 6: O botão "Visualizar processo" ao ser acionado, abrirá a tela Processo Produtivo com o processo criado da fórmula…](https://ajuda.sankhya.com.br/hc/article_attachments/16674492689431) **"Visualizar processo"** ao ser acionado, abrirá a tela [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova) com o processo criado da fórmula importada selecionada.
Ao clicar no botão ![Imagem 7: O botão "Visualizar processo" ao ser acionado, abrirá a tela Processo Produtivo com o processo criado da fórmula…](https://ajuda.sankhya.com.br/hc/article_attachments/16674508320535) **"Solucionar conflito"**, a seguinte tela será apresentada.

![Imagem 8: O botão "Visualizar processo" ao ser acionado, abrirá a tela Processo Produtivo com o processo criado da fórmula…](https://ajuda.sankhya.com.br/hc/article_attachments/4787813221271)

Para solucionar o conflito, selecione os produtos que irão corresponder as MPs principais do processo e arraste, ou utilize o botão ![Imagem 9: Para solucionar o conflito, selecione os produtos que irão corresponder as MPs principais do processo e arraste, ou…](https://ajuda.sankhya.com.br/hc/article_attachments/16674508326039) para levar o(s) registro(s) para a grade **"MPs principais"**, logo após, na grade **"MPs alternativas"** ficarão as respectivas MPs alternativas desses produtos.

[GIF animado: Imagem 10: Para solucionar o conflito, selecione os produtos que irão corresponder as MPs principais do processo e arraste, ou…](https://ajuda.sankhya.com.br/hc/article_attachments/4787779804567)

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050833594-Importador-F%C3%B3rmula-de-Composi%C3%A7%C3%A3o#top)

![Imagem 11: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16674496275223) Acesse também:

[Composição do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto)
