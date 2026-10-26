---
id: "360045116313"
titulo: "Consolidação de Empresas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116313-Consolida%C3%A7%C3%A3o-de-Empresas"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilidade"
atualizado_em: "2026-07-29T16:02:13Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "Empresa", "Destino", "Origem", "Consolidação", "Consolidar", "br.com.sankhya.mgecontab.consolidacaodeempresas", "Consolidação de Empresas manual", "Contabilidade", "Saldo", "Financeiro", "Empresas", "Gerenciamento Eficiente: Consolidação de Empresas"]
---

# Consolidação de Empresas

```
![módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42315001381015) Módulo: Contabilidade> Rotinas
```

---

Entende-se por **"Consolidar"** o ato de **"Unificar"** duas ou mais organizações. A Consolidação de Empresas consiste na junção dos lançamentos contábeis de duas ou mais instituições denominadas **"Empresas de Origem"** em uma nova empresa consolidada denominada **"Empresa de Destino"**.

Tem-se abaixo um exemplo conceitual de Consolidação:

![Imagem 2: Tem-se abaixo um exemplo conceitual de Consolidação:](https://ajuda.sankhya.com.br/hc/article_attachments/5422180333207)

A rotina de Consolidação de Empresas tem como objetivo auxiliar no agrupamento dos lançamentos contábeis de empresas denominadas origem em uma empresa destino. A visão consolidada dos lançamentos contábeis, irá contribuir para a geração de relatórios relevantes para o gerenciamento da empresa e suas tomadas de decisão.

| [Painel Filtro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116313-Consolida%C3%A7%C3%A3o-de-Empresas#painelfiltro) | [Painel Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116313-Consolida%C3%A7%C3%A3o-de-Empresas#painelpreferncias) |
| --- | --- |
| [Grade Empresas disponíveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116313-Consolida%C3%A7%C3%A3o-de-Empresas#gradeempresasdisponveis) | [Empresa Destino Inexistente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116313-Consolida%C3%A7%C3%A3o-de-Empresas#empresadestinoinexistente) |
| [Parâmetros que atuam nesta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116313-Consolida%C3%A7%C3%A3o-de-Empresas#parmetrosqueatuamnestarotina) |  |

 

## Painel Filtro

Nota-se ao lado esquerdo da parte superior da tela, o painel **"Filtro"** que ao ser configurado, irá gerar na grade predominante da tela os dados necessários para realização do processo de consolidação.

![Imagem 3: Nota-se ao lado esquerdo da parte superior da tela, o painel "Filtro" que ao ser configurado, irá gerar na grade…](https://ajuda.sankhya.com.br/hc/article_attachments/5170188922007)

No campo **"Empresa de destino"** informe a empresa que irá receber a consolidação, ou seja, a instituição destinatária.

**Importante:** Serão apresentadas para escolha neste campo, empresas que na tabela TCBEMP estiverem com o campo **"EMPCONSOLIDA"** preenchidos como **"S"**.

**Nota:** Uma prática contábil bem comum ao utilizar a rotina da Consolidação de Empresas com o intuito de facilitar na identificação da empresa consolidadora nos relatórios contábeis, é utilizar o código 999 para a empresa de destino. Por este motivo, quando se utiliza pela primeira vez esta rotina o sistema traz como padrão de sugestão o código 999 no campo Empresa de destino.

Preencha no campo **"Período de consolidação"** o intervalo de referência ao qual deseja-se realizar a consolidação. Tem-se como opção de preenchimento todos os meses do ano.

Informe no campo **"Exercício"** o ano ao qual deseja efetuar a consolidação de Empresas. Ao aplicar-se o filtro, serão exibidas na grade as empresas para consolidar que estiverem no mesmo exercício contábil informado neste campo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116313-Consolida%C3%A7%C3%A3o-de-Empresas#top)

## Painel Preferências

No painel **"Preferências"** teremos marcações fundamentais para realização da consolidação.

![Imagem 4: No painel "Preferências" teremos marcações fundamentais para realização da consolidação.](https://ajuda.sankhya.com.br/hc/article_attachments/5170275877143)

Ao efetuar a marcação **"Preservar o nome da empresa de destino"**, o nome da empresa de destino da consolidação será mantido quando a consolidação ocorrer em uma empresa preexistente.

Por meio da marcação **"Consolidar contas sem movimento e com saldo"**, as contas contábeis que não possuem movimento e com saldo maior que zero, serão consolidadas.

**Observação:** a recomposição de saldos também pode ser realizada por meio do botão ![Imagem 5: Observação: a recomposição de saldos também pode ser realizada por meio do botão "Outras Opções..." da tela Empresa .…](https://ajuda.sankhya.com.br/hc/article_attachments/25940217655447) **"Outras Opções..."** da tela [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa). Neste caso, é necessário que a marcação Consolidar contas sem movimento e com saldo esteja desabilitada.

Selecionando-se a marcação **"Consolidar empresas consolidadoras?"** tem-se que o sistema permitirá que empresas consolidadoras também sejam consolidadas.

O campo **"Regra para Consolidação"** conta com as seguintes opções e funcionalidades:

- **Apenas consolidar:** Quando essa opção for selecionada, será executada apenas a consolidação.
- **Consolidar e Recompor o Saldo:** Ao selecionar essa opção, após a conclusão da rotina de consolidação, será executada a rotina de recomposição de saldo para a empresa destino, com a data de referência igual ao mês anterior à data início da consolidação.
- **Desconsiderar todas as referências da empresa destino e consolidar:** Antes da rotina de consolidação, será verificado se no exercício da consolidação (ou maior), existe movimentação de contabilização; caso não exista, o sistema pegará a soma de saldo contábil das empresas de origem da consolidação, com a referência igual à um mês menor do que a data da consolidação e inserirá a soma destes saldos na empresa destino da consolidação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116313-Consolida%C3%A7%C3%A3o-de-Empresas#top)

## Grade Empresas disponíveis

Nesta grade serão apresentadas as empresas disponíveis para executar a consolidação; serão exibidas somente as empresas que na tabela TCBEMP estiverem com o campo EMPCONSOLIDA preenchidos como **"N"**. Além disso, estas devem estar no mesmo exercício contábil informado no campo **"Exercício"**.

Ao clicar em ![Imagem 6: Ao clicar em "Aplicar" serão exibidas todas as empresas que se enquadram nos filtros definidos.](https://ajuda.sankhya.com.br/hc/article_attachments/5170307069975) **"Aplicar"** serão exibidas todas as empresas que se enquadram nos filtros definidos.

![Imagem 7: Ao clicar em "Aplicar" serão exibidas todas as empresas que se enquadram nos filtros definidos.](https://ajuda.sankhya.com.br/hc/article_attachments/5170305411351)

Os botões ![Imagem 8: Os botões "Marcar todos os registros da grade" e "Desmarcar todos os registros da grade" selecionam e desmarcam todas…](https://ajuda.sankhya.com.br/hc/article_attachments/5170372740503) **"Marcar todos os registros da grade"** e ![Imagem 9: Os botões "Marcar todos os registros da grade" e "Desmarcar todos os registros da grade" selecionam e desmarcam todas…](https://ajuda.sankhya.com.br/hc/article_attachments/5170374366999) **"Desmarcar todos os registros da grade"** selecionam e desmarcam todas as empresas apresentadas na grade de uma só vez, respectivamente.

Quando você selecionar o botão ![Imagem 10: Quando você selecionar o botão "Consolidar" , o sistema efetuará a consolidação das empresas que estiverem selecionadas.](https://ajuda.sankhya.com.br/hc/article_attachments/5170308616215) **"Consolidar"**, o sistema efetuará a consolidação das empresas que estiverem selecionadas.

Na consolidação, todos os lançamentos contábeis constantes nas empresas de origem em seus respectivos lotes para a empresa de destino serão copiados, agrupando-os em lotes numerados sequencialmente, partindo do número "1"; o número do lote da empresa destino não irá corresponder ao número do lote das empresas origem.

Os lançamentos consolidados serão provenientes dos lotes das empresas de origem copiados para a empresa destino. Deste modo, a situação dos lotes criados na empresa de destino, será a mesma dos lotes nas empresas de origem, vejamos abaixo um exemplo

Se em uma empresa de origem a situação do lote for **"Aberto"**, na Empresa de Destino o lote correspondente gerado, também terá a situação igual a **"Aberto"**.

Ao realizar a Consolidação de Empresas será gerada uma chave de rastreabilidade na tela [Lançamentos Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis#detalhesdolanamento) para que os movimentos de origem da contabilização das empresas anteriores sejam identificados com facilidade.

![Imagem 11: Ao realizar a Consolidação de Empresas será gerada uma chave de rastreabilidade na tela Lançamentos Contábeis para que…](https://ajuda.sankhya.com.br/hc/article_attachments/13077335895831)

Esta chave será composta com os seguintes dados:

- CODEMP: 1
- REFERENCIA: 01122022
- NUMLANC: 4
- TIPLANC: R
- ORIGEM: E
- NUNICO: 2371
- NUMLOTE: 16
- VLRLANC: 287,90
- SEQNOTA: 0
- SEQUENCIA: 0

**Nota:** As informações serão separadas por dois pontos (:), conforme apresentado na imagem acima.

Os lançamentos manuais não têm rastreabilidade, sendo assim, as chaves não serão apresentadas na grade.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116313-Consolida%C3%A7%C3%A3o-de-Empresas#top)

## Empresa Destino Inexistente

Na realização da Consolidação de Empresas, caso seja informado um código de empresa destino inexistente, o sistema irá criar uma nova empresa nas rotinas abaixo preenchendo apenas os seguintes campos:

- [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa)

![Imagem 12: Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/5170830986775)

[Aba Exercício](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa#abaexerccio)

**Código da Empresa:** Será alimentado com o código apontado como inexistente.

**Data da Abertura:** Neste campo será apontada a menor data de abertura dentre as empresas selecionadas.

**Data de Início do Período Contábil:** Este campo será preenchido com a data do início do período contábil do Exercício selecionado.

**Data do Fim do Período Contábil:** Será acrescentado neste campo a data final do período contábil do Exercício selecionado.

**Referência:** O sistema irá preencher esta informação com a referência do início do exercício selecionado.

- [Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Empresas)

![Imagem 13: Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/article_attachments/5170887604503)

[Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Empresas#abageral)

**Código da Empresa:** Será preenchido com o código indicado como inexistente.

**Nome Fantasia:** O sistema irá preenche-lo com o termo **"Consolidação"** seguido dos códigos das empresas consolidadas separados por vírgula.

**Razão Social:** Este campo será alimentado com o termo **"Consolidação"** continuado dos códigos das instituições consolidadas separados por vírgula.

**Razão Abreviada:** Será acrescentado neste campo o termo **"Consol."**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116313-Consolida%C3%A7%C3%A3o-de-Empresas#top)

## Parâmetros que atuam nesta rotina

**Consolidar empresas por procedure? - CONSOLIDAPORSTP:** Quando esse parâmetro for habilitado, a consolidação será realizada através de uma rotina alternativa que roda via procedure no banco, evitando lentidão e atingindo assim uma melhor performance para o procedimento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116313-Consolida%C3%A7%C3%A3o-de-Empresas#top)
