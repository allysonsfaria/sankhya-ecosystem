---
id: "360052261594"
titulo: "Gerência de Rastreamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052261594-Ger%C3%AAncia-de-Rastreamento"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Substituição Tributária  > Rastreamento e cálculo"
atualizado_em: "2026-09-15T17:09:33Z"
rotulos: ["Configuração", "Relatórios", "Fiscal", "Livros Fiscais", "Estoque", "br.com.sankhya.mgeliv.mov.gerrastreamentost", "Gerência de Rastreamento", "Entradas saídas saldo ligações", "Exportar PDF abrir documentos"]
---

# Gerência de Rastreamento

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313134228759) Módulo: Livros Fiscais > Conexão
```

---

Por meio desta tela, você poderá consultar as notas rastreadas e as ligações vinculadas à estas que foram realizadas por meio de configurações específicas para a validação do rastreamento a ser gerado.

![Imagem 2: Por meio desta tela, você poderá consultar as notas rastreadas e as ligações vinculadas à estas que foram realizadas…](https://ajuda.sankhya.com.br/hc/article_attachments/4416283779607)

Informe a **"Empresa"** para qual você deseja que o rastreamento seja verificado de acordo com as movimentações.

Selecione o **"Produto"** em que as movimentações de rastreamento serão verificadas.

Nos campos **"Dr. Inicial"** e **"DT. Final"**, preencha a data inicial e final das movimentações de rastreamentos.

Ao preencher o campo **"Nro. Único Entrada"**, o sistema trará apenas as movimentações de entrada do número informado.

Se o campo **"Nro. Único Saída"** for informado, apenas as movimentações de saída serão filtradas.

**Nota:** se você informar o Nro. Único Entrada, não será permitido que o campo Nro. Único Saída seja preenchido.

Além desses, na seção **"Legenda"** o sistema trará a legenda para o resultado dos campos de filtros que foram ou não preenchidos:

**Azul:** **Mov. Fiscal:** Aqui, todos os lançamentos de entrada ou saída que atualizarem o Livro de ICMS ficarão com essa cor.

**Vermelho:** **Mov. Não Fiscal:** Todos os lançamentos de entrada ou saída que não atualizarem o Livro de ICMS ficarão em vermelho.

Depois de utilizar o botão ![Imagem 3: Depois de utilizar o botão "Aplicar" , serão exibidas no quadro "Notas de entrada rastreadas" todas as notas de entrada…](https://ajuda.sankhya.com.br/hc/article_attachments/4416284734231) **"Aplicar"**, serão exibidas no quadro **"Notas de entrada rastreadas"** todas as notas de entrada que amparam o saldo de estoque do rastreamento.
Neste quadro, quando você selecionar uma determinada nota, e posteriormente em **"Ligação entre as notas de saída e entrada"** as ligações referentes à nota selecionada serão exibidas.

A grade Notas de entrada rastreadas mostrará todas as notas de entrada que foram rastreadas. Ela é composta pelas seguintes colunas:

As colunas **"Código do Produto"** e **"Código da Empresa"** exibirão o código do produto e o código da empresa que foram rastreados, respectivamente.

Caso o rastreamento tenha sido feito por controle, a informação será exibida na coluna **"Controle"**.

A coluna **"Saldo disponível"** será preenchida com seu saldo de estoque disponível.

Temos também as colunas **"Data de entrada"** e **"Nro. único"** que mostram a data de entrada da nota bem como seu número único.

As colunas **"Qtd. entrada"** e **"Qtd. saída"** informam a quantidade do item da nota de entrada e a quantidade já utilizada no rastreamento de estoque, respectivamente.

A coluna **"Sequência do item"** exibe a sequência do item da nota de entrada.

A grade Ligação entre as notas de saída e entrada tem o objetivo de mostrar todas as notas de saída que foram rastreadas com as suas origens (entradas) ligadas. Assim, será possível que você identifique de qual nota de entrada o sistema utilizou para gerar os valores dos impostos de ICMS e ST da operação anterior, no XML da nota de saída. Essa grade é composta pelas colunas abaixo:

O **"Nro. único da saída"** rastreada bem como sua **"Seq. do item da saída"**.

O **"Nro. único da origem"** da nota de entrada em que o sistema fez a ligação com a nota de saída no rastreamento de estoque e sua **"Seq. do item da origem"**.

A coluna **"Qtd. ligada"** com a quantidade de itens da nota de saída ligada com a nota de entrada.

A coluna **"Vlr do ICMS"** mostrará o valor do ICMS da nota de entrada, proporcional à quantidade ligada da nota de saída utilizada na coluna Qtd. ligada.

A **"Base ST"** exibirá a base da substituição tributária da nota de entrada, proporcional à quantidade ligada da nota de saída utilizada na coluna Qtd. ligada.

O sistema irá considerar os valores dos campos **"Base ST Extra Nota"** e **"Valor ST Extra Nota"** do item da nota de compra no rastreamento de estoque. Assim, ao acessar a rotina de Gerência de Rastreamento e consultar o rastreamento do seu produto, você pode verificar que a nota de saída ligada à nota de entrada está com os impostos de **"Valor da Substituição Tributária Total Proporcional à QTDSAI (VLRSUBST)"** e **"Base de Cálculo da Substituição Tributária Proporcional à QTDSAI (BASESUBST)"** preenchidos.

Nos dois quadros da tela, temos disponível o botão ![Imagem 4: Nos dois quadros da tela, temos disponível o botão "Exportar Grade para PDF" , onde você poderá realizar a exportação…](https://ajuda.sankhya.com.br/hc/article_attachments/16313994606615) **"Exportar Grade para PDF"**, onde você poderá realizar a exportação dos dados das grades.

Também temos disponível o botão ![Imagem 5: Também temos disponível o botão "Outras Opções..." nos dois quadrantes da tela. Nele, existem as opções "Abrir…](https://ajuda.sankhya.com.br/hc/article_attachments/16313994607511) **"Outras Opções..."** nos dois quadrantes da tela. Nele, existem as opções **"Abrir documento de entrada (CTRL + K)"** e **"Abrir documento de saída (CTRL + K)"**; sendo assim, quando você clicar sobre essas opções, será aberta a nota de número único dos campos **"Nro. único da nota de entrada"** ou **"Nro. único da nota de saída"** que estiver selecionada.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052261594-Ger%C3%AAncia-de-Rastreamento#top)
