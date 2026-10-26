---
id: "360044612054"
titulo: "Verificação de Saldo de Estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-09-21T18:12:39Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "INICIOCONTEST", "Configuração", "Relatórios", "Análise", "Verificação", "estoque", "Sankhya-W", "Saldo", "Estoque", "Financeiro", "br.com.sankhya.core.cfg.verificacaosaldoestoque", "Verificação de Saldo de Estoque manual"]
---

# Verificação de Saldo de Estoque

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310861317655) Módulo: Configurações > Avançado
```

---

Através desta rotina é realizada a análise do estoque dos produtos; tem-se aqui um comparativo entre a quantidade dos produtos lançados ou não nas [Centrais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas) via Notas Fiscais e o saldo dos respectivos produtos em estoque (tabela de estoque - TGFEST).

Neste artigo trataremos sobre os seguintes tópicos:

| [Opções para verificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#opesparaverificao) | [Filtro empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#filtroempresas) |
| --- | --- |
| [Filtro produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#filtroprodutos) | [Grade Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#gradeprincipal) |
| [Botões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#botes) |  |

![Imagem 2: Botões](https://ajuda.sankhya.com.br/hc/article_attachments/13345744683543)

## Opções para verificação

![Imagem 3: Opções para verificação](https://ajuda.sankhya.com.br/hc/article_attachments/13345808101271)

O valor apresentado no campo **"Nro. único inicial"** será o valor informado no parâmetro **"Num. Início(TGFNum) do controle de estoque - INICIOCONTEST"**.

Ao selecionar a marcação **"Estoque"**, o sistema considerará a quantidade de produtos das Centrais com a quantidade de produtos em estoque, executando a rotina de Verificação de Saldos de Estoque, realizando uma consulta nas seguintes tabelas:

- TGFITE - Itens de Entrada e Saída de Produto;
- TGFEST - Estoque;
- TGFPRO - Produto;
- TGFEMP - EmpresaFinanceiro.

Assim como na marcação Estoque, ao selecionar **"Estoque de Terceiros"** o sistema considerará a quantidade de produtos das Centrais com a quantidade de produtos em estoque, de forma que irá consultar as tabelas:

- TGFITE - Itens de Entrada e Saída de Produto;
- TGFEST - Estoque;
- TGFPRO - Produto;
- TGFEMP - EmpresaFinanceiro.

Quando a opção **"Estoque sem Lançamento na Central"** é selecionada, a consulta será feita com base nos produtos que não passaram pela movimentação das Centrais, ou seja, foram efetuados lançamentos diretos via banco informando empresa, local, produto, estoque e outros dados pertinentes a tabela de estoque.

Essa consulta é feita na tabela TGFEST - Estoque e desconsiderando os dados que estão na TGFITE - Itens de Entrada e Saída de Produto.

Ao selecionar a marcação **"Estoque de Terceiros sem Lançamento na Central"** será feita uma consulta com base nos produtos que não passaram pela movimentação das Centrais e foram lançados na tabela de estoque. A consulta é feita na tabela TGFEST - Estoque.

Quando a marcação **"Reserva"** for habilitada, será verificada a quantidade de produtos das Centrais com a quantidade de produtos em estoque, para isso o sistema considera a soma das três consultas nas seguintes tabelas:

- TGFITE - Itens de Entrada e Saída de Produto;
- TGFEST - Estoque;
- TGFPRO - Produto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#top)

## Filtro empresas

![Imagem 4: Filtro empresas](https://ajuda.sankhya.com.br/hc/article_attachments/13345924539031)

Caso a organização trabalhe com o Sankhya-Om controlando duas ou mais empresas, pode-se por meio desta seção escolher quais empresas terão o estoque de seus produtos analisado. Clique no botão **"Adicionar"** para definir as empresas desejadas.

As empresas assinaladas ![Imagem 5: As empresas assinaladas terão seus estoques apresentados. Caso nenhuma empresa seja escolhida no filtro será exibido o…](https://ajuda.sankhya.com.br/hc/article_attachments/9535799304343) terão seus estoques apresentados. Caso nenhuma empresa seja escolhida no filtro será exibido o estoque de todas elas na [Grade Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#gradeprincipal).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#top)

## Filtro produtos

![Imagem 6: Filtro produtos](https://ajuda.sankhya.com.br/hc/article_attachments/13346004421143)

De forma semelhante à seção anterior, mas com foco direto nos produtos, é possível escolher os itens que passarão pela análise de estoque.

Os produtos que estiverem assinalados ![Imagem 7: Os produtos que estiverem assinalados terão seus estoques apresentados. Caso nenhum produto seja escolhida no filtro,…](https://ajuda.sankhya.com.br/hc/article_attachments/9535799304343) terão seus estoques apresentados. Caso nenhum produto seja escolhida no filtro, será exibido na [Grade Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#gradeprincipal) o estoque de todos aqueles itens que o sistema identificou com algum tipo de divergência.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#top)

## Grade Principal

Uma vez selecionadas as [Opções para verificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#opesparaverificao) necessárias e formulados os [Filtros para empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#filtroempresas) e [Filtros para produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#filtroprodutos) desejados, acione o botão **"Verificar"** para que a Grade Principal seja preenchida.

![Imagem 8: Uma vez selecionadas as Opções para verificação necessárias e formulados os Filtros para empresas e Filtros para…](https://ajuda.sankhya.com.br/hc/article_attachments/13346159406871)

Pode-se notar na grade, os produtos identificados pelo sistema que se enquadraram nas condições estabelecidas. Além disto, a medida que uma linha é selecionada, o produto em questão é destacado no rodapé da tela, onde nota-se também a Empresa a qual ele pertence, o Parceiro com o qual o item foi negociado, o Local onde o produto se encontra, qual é seu Tipo de estoque e logo abaixo, temos as quantidades do produto em questão em cada cenário de estocagem, ou seja, são exibidos os valores em:

- **Estoque:** Informação pertinente ao estoque;
- **Est. na central:** Resultado da somatória das movimentações de entrada e saída do produto registradas no sistema;
- **Est. sem movimento:** Informação registrada no estoque, porém sem movimentação;
- **Reserva no estoque:** Informação registrada no estoque;
- **Reserva na central:** Resultado da somatória das movimentações de reserva do produto registradas no sistema;
- **Reserva sem movimento:** Informação sobre a reserva registrada no estoque sem movimentação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#top)

## Botões

Abaixo trataremos das funcionalidades de cada botão presente na tela:

**+** **Filtro:** Além das opções de filtragem disponibilizadas no [Filtro para empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#filtroempresas) e no [Filtro para produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#filtroprodutos), pode-se através deste botão criar filtros personalizados de modo a identificar os itens desejados ainda mais facilmente.

**Verificar:** Este botão toma por base os cenários de estocagem selecionados nas [Opções para verificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#opesparaverificao) e os filtros definidos, e realiza as devidas apurações de estoque apresentando os resultados na [Grade Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#gradeprincipal).

**![Imagem 9: Mostrar/esconder painel de filtros: Através deste botão, pode-se exibir ou ocultar da tela todo o painel de filtros, ou…](https://ajuda.sankhya.com.br/hc/article_attachments/16813936645143) Mostrar/esconder painel de filtros:** Através deste botão, pode-se exibir ou ocultar da tela todo o painel de filtros, ou seja, além dos botões Filtro e Verificar, as [Opções para verificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#opesparaverificao), o [Filtro empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#filtroempresas) e o [Filtro produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#filtroprodutos). Caso algum filtro tenha sido construído, esse botão será apresentado com a coloração **vermelha**.

![Imagem 10: Configurar grade: Por meio deste botão pode-se selecionar e/ou ocultar alguma coluna da Grade Principal , deixando-a da…](https://ajuda.sankhya.com.br/hc/article_attachments/16813936648983) **Configurar grade:** Por meio deste botão pode-se selecionar e/ou ocultar alguma coluna da [Grade Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#gradeprincipal), deixando-a da forma mais adequada para uso, de acordo com a sua necessidade.

![Imagem 11: Botões de navegação: Estes botões permitem a navegação entre as linhas dos itens na Grade Principal . Além destes,…](https://ajuda.sankhya.com.br/hc/article_attachments/16813936652567) **Botões de navegação:** Estes botões permitem a navegação entre as linhas dos itens na [Grade Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#gradeprincipal). Além destes, utiliza-se as teclas de atalho **"Ctrl + <" ou "Ctrl + >"**, ou ainda as setas direcionais também presentes no teclado, sendo as setas á e â para navegação na vertical e as setas à e ß para andamento horizontal entre as colunas.

**Corrigir:** Este botão é o principal desta rotina, pois ele irá eliminar as movimentações efetuadas via banco e corrigir os saldos de estoque.

**Importante:** esse botão, bem como toda a rotina, devem ser utilizados com cautela e acompanhamento de um Implantador Sankhya, a fim de se evitar posteriores anomalias no estoque.

![Imagem 12: Outras Opções...: Este botão apresenta a funcionalidade "Reconstrução de saldo diário das movimentações de entradas e…](https://ajuda.sankhya.com.br/hc/article_attachments/16813936660375) **Outras Opções...:** Este botão apresenta a funcionalidade **"Reconstrução de saldo diário das movimentações de entradas e saídas"**, que ao ser acionada, irá apresentar um pop-up com esta mesma nomenclatura, onde é determinado obrigatoriamente o Período, e pode-se optar por preencher a [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Empresas), [Tipo de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), Tipo de Movimento e/ou [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113); esta funcionalidade tem seu acionamento com o botão **"Processar"** localizado na parte inferior do referido pop-up; ele reequilibra o saldo de estoque, removendo e refazendo as correspondentes movimentações com base nos itens de nota contidas no período definido.

**Importante:** esta é uma ação que pode levar alguns instantes de acordo com os filtros definidos, além disto, ela bloqueia momentaneamente outras rotinas que trabalhem com estoque de produtos. Desse modo, é essencial a análise detalhada dos processos de entrada e saída de mercadoria da empresa, de forma que esta funcionalidade seja utilizada com prudência e parcimônia.

Ao acionar o botão Corrigir para correção dos saldos de estoque será apresentada a seguinte mensagem de confirmação do procedimento:

**"Esta ação irá recompor a tabela de estoque(TGFEST) removendo entradas que não estejam lastreadas por documentos da central. Esta operação é irreversível."**

Vale ressaltar que este procedimento deverá ser executado com ponderação, com o acompanhamento de um Consultor Sankhya.

### Imagem 13: Registros Zerados na Verificação de Saldo de EstoqueRegistros Zerados na Verificação de Saldo de Estoque

**1. Comportamento identificado**

É um comportamento **normal e esperado** do sistema exibir linhas com saldo de estoque zerado na tela **Verificação de Saldo de Estoque** após a exclusão de uma nota fiscal (seja de venda, compra ou remessa). Isso ocorre porque a exclusão da nota zera a quantidade do produto na tabela de estoque (**TGFEST**), mas não apaga o registro de controle. A tela, então, exibe essa linha zerada, pois identifica um registro de estoque sem um documento fiscal ativo que o justifique.

**2. Justificativa: Por que o Registro de Estoque não é deletado?**

A principal razão é a **rastreabilidade**. O sistema foi projetado para preservar o histórico de movimentação e as configurações de um item. Um registro na **TGFEST** não é apagado se ele possuir qualquer vínculo ou configuração importante, tais como:

- **Controle de Estoque em Poder de Terceiros** (quando o campo **CODPARC** está preenchido);
- Configuração de **Estoque Mínimo/Máximo**;
- Controle de **Lote por Data de Validade ou Data de Fabricação**;
- Vínculo com **Código de Barras, Percentual de Pureza ou Germinação**.

Manter o registro, mesmo zerado, garante que nenhuma informação de contexto seja perdida e que a rastreabilidade seja assegurada.

**3. Cenários que causam este Comportamento**

**Cenário 1: Exclusão de Nota com Estoque em poder de Terceiro**

1. **Criação:** Na Central de Vendas, um pedido é criado para o parceiro **96311**, movimentando 1 unidade do produto 1.
2. **Confirmação:** Ao confirmar a nota, o sistema cria um registro na **TGFEST** com Estoque = 1 e o campo **CODPARC** preenchido com **96311**, indicando que o produto está em posse de um terceiro.
3. **Exclusão:** O usuário retorna à Central de Vendas e remove a nota recém-criada.
4. **Resultado:** O sistema zera o campo Estoque para 0, mas **não deleta a linha da TGFEST**, porque o campo **CODPARC** está preenchido. Ao abrir a tela **Verificação de Saldo de Estoque**, a linha aparecerá com saldo 0, pois o sistema preservou o registro para manter o histórico da operação com o parceiro.

**Cenário 2: Exclusão de Nota de Compra**

O mesmo comportamento se repete em outras operações. Por exemplo, ao cadastrar uma nota de compra para um produto que tem uma configuração de **Estoque Mínimo** ou uma **Data de Validade** associada. Se essa nota de compra for posteriormente excluída, o saldo será zerado, mas o registro na **TGFEST** será mantido por causa desses vínculos.

**Resultado:** a linha zerada será exibida na tela **Verificação de Saldo de Estoque**.

**4. Solução: Como limpar a visualização da Tela**

Para que esses registros zerados e sem nota não interfiram na sua análise, a solução consiste em **ajustar os filtros da própria tela**.

**Passos para a correção:**

1. Acesse a tela **Verificação de Saldo de Estoque**.
2. Abra o painel de **Configurações/Filtros**.
3. Desmarque as seguintes opções:

   - **Estoque de terceiros sem lançamentos na central**
   - **Estoque sem lançamentos na central**.

Ao fazer isso, você instrui a tela a exibir apenas os saldos de estoque que possuem um documento fiscal correspondente e ativo no sistema. Isso efetivamente limpa a visualização, ocultando os registros zerados cujo vínculo foi quebrado pela exclusão da nota, sem comprometer a rastreabilidade que o sistema preservou no banco de dados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054-Verifica%C3%A7%C3%A3o-de-Saldo-de-Estoque#top)
