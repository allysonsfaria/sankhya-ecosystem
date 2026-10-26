---
id: "360044594854"
titulo: "Ativar/Reprocessar Rastreamento de Estoque/ST"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854-Ativar-Reprocessar-Rastreamento-de-Estoque-ST"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Substituição Tributária  > Rastreamento e cálculo"
atualizado_em: "2026-09-15T17:24:59Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Fiscal", "Livros Fiscais", "br.com.sankhya.mgeliv.processarrastreamento", "Ativar/Reprocessar Rastreamento de Estoque/ST manual", "Estoque", "Substituição Tributária", "Ativar Estoque/ST", "Processar e histórico", "Configurar filtros"]
---

# Ativar/Reprocessar Rastreamento de Estoque/ST

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312868288919) Módulo: Livros Fiscais > Avançados > Rastreamento de Estoque/ST
```

---

Esta rotina visa ativar e reprocessar o Estoque/ST, assim, o sistema irá verificar se o produto já possui o Rastreamento de ST habilitado e, caso haja, a rotina deletará as linhas de rastreamento e irá processá-la novamente.

| [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854-Ativar-Reprocessar-Rastreamento-de-Estoque-ST#filtros) |  | [Aba Dados para Ativar o Rastreamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854-Ativar-Reprocessar-Rastreamento-de-Estoque-ST#abadadosparaativarorastreamento) |
| --- | --- | --- |
| [Aba Produtos com Problemas no Rastre...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854-Ativar-Reprocessar-Rastreamento-de-Estoque-ST#produtoscomproblemasnorastreamento) |  | [Botões do topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854-Ativar-Reprocessar-Rastreamento-de-Estoque-ST#bot%C3%B5esdotopodatela) |

## Filtros

No painel de filtros, temos as seguintes seções:

| [Seção Filtros Rápidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854-Ativar-Reprocessar-Rastreamento-de-Estoque-ST#se%C3%A7%C3%A3ofiltrosr%C3%A1pidos) |  | [Seção Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854-Ativar-Reprocessar-Rastreamento-de-Estoque-ST#seopreferncias) |
| --- | --- | --- |

                                                   

![Imagem 2: Seção Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/4939649670551)

#### Seção Filtros Rápidos

No local em destaque, tem-se o **"Filtro personalizado"** e os **"Filtros rápidos"**. Através de um Filtro personalizado é possível filtrar os produtos para o Rastreamento de ST de uma maneira dinâmica, na qual pode-se utilizar variáveis ou querys; já os Filtros rápidos, estão divididos em:

- Empresa;
- Produto;
- Grupo de Produto;
- Grupo de ICMS do Produto;
- Tipo de Substituição Tributária.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854-Ativar-Reprocessar-Rastreamento-de-Estoque-ST#filtros)

---

#### Seção Preferências

![Imagem 3: Seção Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/4940437816983)

Nesta seção temos os campos:

**Tipo de Rastreamento:** Pode-se escolher neste campo uma dentre as opções a seguir:

- **Rastrear com controle/local, se existir:** Esta opção separa a linha de Controle e Local, distinguindo-as.
- **Rastrear:** Selecionando esta opção, não serão separados nem Local e nem Controle mas sim, somará todo o estoque, independente do mesmo.
- **Rastrear com Controle:** Quando esta opção estiver selecionada, as linhas de estoque serão separadas de acordo com o Controle.
- **Rastrear com Local:** Esta opção separa as linhas de estoque com base no Local.
- **Sem rastreamento:** Ao selecionar esta opção, o rastreamento de estoque será desfeito.

**Observação:** quando houver o reprocessamento do rastreamento de estoque ao utilizar a opção Sem Rastreamento, o sistema atualizará o campo **"Tipo de Rastreamento"** da tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Rastreamento por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abarastreamentoporempresa), para a opção **"Sem rastreamento"**.

**Observação:** você poderá conferir a opção selecionada nesse campo, na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Rastreamento Por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abarastreamentoporempresa), campo **"Tipo de Rastreamento"**.

**Opção de Rastreamento:** Através deste campo, efetue o rastreamento com as seguintes opções:

- Rastrear toda a Vida Útil;
- Rastrear com Cópia de Estoque;
- Rastrear com Contagem de Estoque.

**Observação:** quando for selecionado as opções Cópia e Contagem de Estoque é necessário definir a Empresa do Rastreamento, sendo que, após configurada, será exibido o campo **"Data da Cópia/Contagem"** logo abaixo, nesta seção.

**Nota:** se você indicar a opção Rastrear toda a vida útil, o sistema exibirá o campo Data da Cópia/Contagem, e caso este seja preenchido, o sistema não irá considerar os produtos que estarão na Cópia/Contagem da data informada para realizar o rastreamento.

**Observação:** caso as opções Rastrear com cópia de estoque ou Rastrear com Contagem de Estoque forem selecionadas, o sistema exibirá o campo Data da Cópia/Contagem e ao informá-lo, somente produtos que estão na cópia ou contagem de estoque serão exibidos.

**Exibir somente rastreamento com Erro:** Com esta marcação indicada, o sistema filtrará somente os produtos com erro no rastreamento de estoque na grade **"Produtos"** (abas [Dados para Ativar o Rastreamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854-Ativar-Reprocessar-Rastreamento-de-Estoque-ST#h_01EYTP3BXXRTV24GWAH9TAG508) e [Produtos com Problemas no Rastreamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854-Ativar-Reprocessar-Rastreamento-de-Estoque-ST#h_01EYTP3MRDY0VM0F0XFGN6XM8P)).

**Rastrear produtos inativos:** Por meio dessa marcação, o sistema irá rastrear também, produtos inativos que possuem rastreamento.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854-Ativar-Reprocessar-Rastreamento-de-Estoque-ST#filtros) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854-Ativar-Reprocessar-Rastreamento-de-Estoque-ST#top)

## Aba Dados para Ativar o Rastreamento

Nesta aba, serão exibidas duas grades, sendo elas:

![Imagem 4: Nesta aba, serão exibidas duas grades, sendo elas:](https://ajuda.sankhya.com.br/hc/article_attachments/4940534717847)

#### Grade Empresas

Na Grade Empresas, serão exibidas todas as empresas que foram filtradas e que poderão ser rastreadas/reprocessadas.

**Nota:** as empresas que forem concluídas com pelo menos 1 produto, se encontrarão com a marcação **"Rastreamento de Estoques"** (tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abapropriedades)) habilitada.

---

#### Grade Produtos

Esta grade exibirá todos os produtos que foram filtrados através do Filtro personalizado ou dos Filtros rápidos e que poderão ser rastreados/reprocessados.

**Observação:**os produtos que forem concluídos sem erros, se encontrarão com o campo **"Rastreamento de Estoques"** (tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque), sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaestoque)) com a mesma opção selecionada no campo **"Tipo de Rastreamento"** da seção **"Preferências"** desta rotina.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854-Ativar-Reprocessar-Rastreamento-de-Estoque-ST#top)

## Produtos com Problemas no Rastreamento

![Imagem 5: Produtos com Problemas no Rastreamento](https://ajuda.sankhya.com.br/hc/article_attachments/4940561308951)

Por meio do campo **"Pesquisar registros"** localizada na parte superior da grade, você pode filtrar o produto desejado de maneira mais eficiente.

Além disso, no botão ![Imagem 6: Além disso, no botão "Exportar grade para PDF" , temos as opções:](https://ajuda.sankhya.com.br/hc/article_attachments/360103803053) **"Exportar grade para PDF"**, temos as opções:

- Exportar para PDF;
- Exportar para planilha;
- Exportar para cubo.

Esta aba exibirá os problemas localizados na tentativa de Ativar/Reprocessar o Rastreamento de ST, sendo que, serão divididos em erros de:

- Estoque negativo;
- Sem impostos;
- Outros.

**Nota:** como o produto possui NF-e's sem as informações de amparo de ICMS ST, quando for acionado o botão ![Imagem 7: Nota: como o produto possui NF-e's sem as informações de amparo de ICMS ST , q uando for acionado o botão "Processar"…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002800661) **"Processar"** será exibida a seguinte mensagem:

**"O Processo de Rastreamento de Estoque/ST foi concluído com algum(ns) problema(s).**

**Verifique na aba "Produtos com Problemas no Rastreamento" quais Produtos/Empresas apresentaram problemas!".**

Através do botão ![Imagem 8: Através do botão "Visualizar Movimentações" é possível analisar as movimentações dos Produtos com Problemas no…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002801861) **"Visualizar Movimentações"** é possível analisar as movimentações dos Produtos com Problemas no Rastreamento; assim, clicando sobre este botão, será aberta a tela auxiliar **"Análise de Movimentação do Rastreamento/ST"**:

![AR7](https://ajuda.sankhya.com.br/hc/article_attachments/360061910533)

**Observação:**a rotina de Análise de Movimentação do Rastreamento/ST facilita a demonstração do estoque e saldo do produto.

**Nota:** os parâmetros descritos a seguir, poderão ser criados por você e serão utilizadas para informar quais serão as TOPs Fiscais a serem utilizadas no rastreamento:

Com o **"Lista de TOP Entrada no Rastr. de Doc. Não Fiscais - TOPENTNFISRAST"** este parâmetro preenchido, ele restringirá as TOP's de entrada que serão utilizadas para rastreio de Documentos Não Fiscais.

Tem-se que com o parâmetro **"Lista de TOP Saída no rastr. de Doc. Não Fiscais - TOPSAINFISRAST"** preenchido, será utilizado para restrição de TOP's de Saída utilizadas para rastreio de Documentos Não Fiscais.

**Observação:** os parâmetros acima serão usuais apenas se o parâmetro **"Documentos Não-Fiscais atualizam Rastreamento/ST - DOCNFISCRASTST"** estiver desligado.

Ao ligar o parâmetro **"Documentos Não-Fiscais atualizam Rastreamento/ST - DOCNFISCRASTST"**, o sistema irá restringir TOP's de documentos não-fiscais para rastreamento, considere o exemplo:

Caso o parceiro queira restringir apenas entradas e não queira restringir nenhuma TOP de saída, basta informar o valor das TOP's de Entrada e informar no parâmetro de Saída o valor **"-1"**, tem-se então que nenhum documento não fiscal para saída será considerado. O inverso deste exemplo também será funcional.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854-Ativar-Reprocessar-Rastreamento-de-Estoque-ST#top)

## Botões do topo da tela

![Imagem 10: Processar : Por meio deste botão você poderá Processar os registros filtrados pela tela.](https://ajuda.sankhya.com.br/hc/article_attachments/1500002800661) **Processar**: Por meio deste botão você poderá Processar os registros filtrados pela tela.

![Imagem 11: Histórico : Ao clicar neste botão, o sistema exibirá o pop-up "Processos" onde serão exibidos os processos realizados…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002772562) **Histórico**: Ao clicar neste botão, o sistema exibirá o pop-up **"Processos"** onde serão exibidos os processos realizados na tela, e pode-se também realizar a visualização daqueles que estão sendo processados por meio do botão ![Imagem 12: Histórico : Ao clicar neste botão, o sistema exibirá o pop-up "Processos" onde serão exibidos os processos realizados…](https://ajuda.sankhya.com.br/hc/article_attachments/360103803493) **"Ver andamento"**.

![Imagem 13: Novidades! : Este botão exibirá todas as novidades e implementações que abrangem esta rotina e/ou ao que se refere ao…](https://ajuda.sankhya.com.br/hc/article_attachments/4940762185495) **Novidades!**: Este botão exibirá todas as novidades e implementações que abrangem esta rotina e/ou ao que se refere ao rastreamento de estoque. Além disso, com a marcação **"Não abrir as novidades automaticamente"** habilitada, ao acessar a tela após ter sido fechada, o pop-up Novidades disponíveis! não será exibido novamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854-Ativar-Reprocessar-Rastreamento-de-Estoque-ST#top)
