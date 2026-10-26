---
id: "360044601914"
titulo: "Compensação de Crédito ou Débito em Compra ou Venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601914-Compensa%C3%A7%C3%A3o-de-Cr%C3%A9dito-ou-D%C3%A9bito-em-Compra-ou-Venda"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-09-22T21:05:19Z"
rotulos: ["Configuração", "Parceiro", "Movimentação Financeira", "Compensação de Crédito ou Débito em Compra ou Venda", "COMPTITEMP", "COMPTITPOREMP", "EMAILSCOMPAUT", "Compensação de Crédito ou Débito em Compra ou Venda manual", "Crédito", "Financeiro", "Débito", "COMPPARCCAB"]
---

# Compensação de Crédito ou Débito em Compra ou Venda

Esta funcionalidade deverá ser utilizada quando o cliente fizer uma Devolução de Venda ou de Compra. Normalmente a devolução de venda gera um registro de despesa no financeiro, deixando o cliente com crédito na empresa. O processo de compensação permite que no momento da próxima venda, o cliente possa abater esse crédito.

Além disso, pode-se utilizar esta funcionalidade para compensar financeiros provenientes de outras operações. Sendo válida também para Compras.

#### Vendas

A compensação de Crédito ou Débito para a rotina de Vendas pede a configuração dos parâmetros **"Avisar que o cliente possui Crédito? - AVISARCREDCLI"** e **"Tipo de título para compensação de Crédito - TIPTITCREDCLI"**, assim, o sistema passa a avisar o valor do Crédito que o cliente possui, em qualquer despesa lançada no financeiro para o parceiro, normalmente originada por uma devolução. Porém, para a mensagem ser exibida conforme os parâmetros, o campo **"Atualização do Financeiro"**não pode ser definido com a opção **"Provisionar"**. 

**Observação:** em clientes que trabalham com ECF e que possuem em seu cadastro o Cliente Diversos ou Cliente Padrão, o parâmetro AVISARCREDCLI só poderá ser ligado após análise, pois este parâmetro trabalha em conjunto com o parâmetro TIPTITCREDCLI. Se o parâmetro AVISARCREDCLI estiver ligado e o parâmetro TIPTITCREDCLI estiver com valor **"0"**, ao efetuar uma venda para o Cliente Padrão (Cupom Fiscal/Pedido), o sistema irá varrer o banco de dados buscando todos os Títulos que estiverem pendentes para o referido cliente, ocasionando queda de performance. Isto ocorre devido às vendas em cartão de crédito serem feitas para o cliente padrão, e as mesmas terem baixas programadas, por isso são encontrados Títulos em aberto.

Quando o parâmetro de chave AVISARCREDCLI estiver habilitado, é possível adicionar o campo **"Valor do crédito"** na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) para pedidos ou notas de venda através da tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota).

O campo Valor do crédito, também fica disponível na grade dos Portais.

Na confirmação da nota, o sistema informa que o cliente possui o crédito e pergunta ao vendedor se ele deseja registrar este crédito para compensação. Se o vendedor clicar em **"Sim"** o sistema lança um registro no financeiro da nota com o valor possível de ser compensado e reduz este valor proporcionalmente nas outras parcelas.

O título lançado para compensação é gravado com o Tipo de Título configurado no parâmetro de chave TIPTITCREDCLI.

**Importante:** para notas de compra e/ou venda que possuem compensações de movimentações fiscais com parceiros distintos, é necessário ativar o parâmetro **"Compensar somente para o parceiro da Nota? - COMPPARCCAB"**.

#### Compras

Da mesma forma que para vendas, os parâmetros **"Avisar que o fornecedor possui Débito? - AVISARDEBFOR"** e **"Tipo de título para compensação de Débito - TIPTITDEBFOR"** serão usados na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras) nas notas de compra.

Se o parâmetro de chave AVISARDEBFOR estiver ligado, o sistema passa a avisar sobre os débitos do fornecedor com a empresa, para que possa ser feita a compensação em futuras compras. Além disso, pode-se adicionar o campo **"Valor do débito"** na Central de Compras para pedidos ou notas de compra através da configuração do seu layout na tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota).

O campo Valor do débito ficará disponível na grade dos Portais. O sistema registra no Tipo de Título do título gerado para compensação o título informado no parâmetro de chave TIPTITDEBFOR.

**Nota:** o sistema permite a Baixa Automática na Compensação do Crédito. Para isto, configure os parâmetros **"Top Baixa de Despesa de Compensação de Crédito - TOPBAIDESPCOMP"** e **"Top Baixa de Receita de Compensação de Crédito - TOPBAIRECCOMP"** e as TOP’s que serão utilizadas pelo sistema na baixa automática.

**Observação:** se o parceiro possuir uma receita e uma despesa com o mesmo Tipo de Título informado nos parâmetros TIPTITCREDCLI e TIPTITDEBFOR, o sistema não apresentará a mensagem de crédito e não fará a compensação. Ou seja, esta situação indica que existem compensações que deverão ser realizadas antes de um novo aviso do sistema.

Logo, deve-se utilizar tipos de títulos diferentes nos parâmetros de chave TIPTITCREDCLI e TIPTITDEBFOR, mesmo que o parceiro seja cliente e fornecedor, pois, se houver outro título em aberto o sistema não fará a compensação.

Existem outros parâmetros relacionados a estas rotinas, vejamos sobre cada um deles:

Caso o parâmetro **"Compensar crédito do cliente automaticamente - COMPENSACREDCLI"** esteja habilitado, ele irá substituir a funcionalidade do parâmetro AVISARCREDCLI e caso exista crédito, além de mostrar os avisos de crédito do cliente ele também fará com que o sistema execute a compensação do crédito de maneira automática, ou seja, sem perguntar ao usuário se ele deseja compensar o crédito. Esse parâmetro também habilita o campo Valor do crédito.

Se o parâmetro **"Compensar débito do fornecedor automaticamente - COMPENSADEBFOR"** estiver habilitado ele irá substituir a funcionalidade do parâmetro AVISARDEBFOR e caso exista débito, além de mostrar os avisos de débito do fornecedor ele também fará com que o sistema execute a compensação do débito de maneira automática, ou seja, sem perguntar ao usuário se ele deseja compensar o débito. Esse parâmetro também habilita o campo Valor do débito.

No parâmetro **"Emails p/ relatório de erros compens. automática - EMAILSCOMPAUT"**, pode-se informar separado por vírgula, ponto e vírgula ou quebra de linha, os e-mail's que irão receber o relatório de falhas no processo de compensação automática, caso ocorram. No faturamento direto de vários pedidos, se ocorrerem erros na compensação de notas, será encaminhado um e-mail para os endereços informados no parâmetro, contendo a listagem das notas e seus respectivos erros. O mesmo vale quando na confirmação de notas (Geração de lote NF-e, NFS-e, CT-e); caso aconteça alguma falha, tem-se o envio do e-mail.

O sistema utilizará o parâmetro **"Usar como data de Vencimento na compensação - USADTVINCOMPFIN"** para definir a data de vencimento do título ou a sua parte que será reparada na compensação automática de crédito/débito. Este parâmetro possui as seguintes opções:

- **Título de crédito a compensar:** Será efetuada a cópia da Data de Vencimento do título do crédito para o título compensado;
- **Vencimento da operação atual:** Mantém-se inalterada a Data de Vencimento dos títulos compensados, dessa forma, os títulos (sejam completos ou as partes criadas para baixar), ficarão com a Data de Vencimento que foi calculada para eles ao lançar a nota;
- **Data da Baixa:** Os títulos compensados receberão como Data de Vencimento a Data Atual (sem hora), ou seja, o dia em que a compensação/confirmação da nota está sendo realizada.

**Observação:** a funcionalidade deste parâmetro também se aplica na Compensação com base na empresa das parcelas descrita a seguir.

**Importante:** para notas de compra e/ou venda que possuem compensações de movimentações fiscais com parceiros distintos, é necessário ativar o parâmetro **"Compensar somente para o parceiro da Nota? - COMPPARCCAB"**.

### Compensação com base na empresa das parcelas

Você pode configurar o sistema, para que no processo de compensação automática por empresa, seja considerada a empresa das parcelas das notas, ou seja, serão compensadas somente com créditos/débitos da mesma empresa das parcelas. Para que isso ocorra, é necessário realizar a ativação do parâmetro **"Compensar Tít. por empresa das parcelas da nota? - COMPTITPOREMP"**.

Existindo na nota parcelas com uma determinada empresa, mesmo que o parceiro possua crédito/débito para compensar o valor total da nota, se o parâmetro COMPTITPOREMP estiver ativado e este parceiro não for da mesma empresa das parcelas, a compensação não irá ocorrer.

**Importante:** quando o parâmetro de chave COMPTITPOREMP estiver ligado, o parâmetro **"Compensar títulos somente na mesma Empresa - COMPTITEMP"** não será levado em consideração nesta rotina; caso o primeiro parâmetro citado esteja desligado, o sistema irá manter o comportamento atual sobre o processo de compensação.

**Nota:** Financeiros com referência à GNRE serão desconsiderados na compensação, ou seja, seu valor não será utilizado na compensação. Esse comportamento independe do parâmetro de chave COMPTITPOREMP.

| **(1)** Comportamento do Sistema **Compensação Financeira de Notas**   - **Descrição do comportamento**   Você notará que não é possível finalizar a **compensação financeira** de uma nota fiscal de consumidor eletrônica (NFC-e) quando o seu status está como **"Aguardando Autorização"**. Isso acontece porque o sistema só permite que a compensação ou baixa de títulos seja realizada quando a nota já foi aprovada ou está em um dos seguintes status: "Aprovada", "Enviada EPEC", "DANFE de Segurança" ou "Conting.Off-Line NFC-e".  O status "**Aguardando Autorização**" significa que a nota já foi enviada para a SEFAZ, mas ainda não foi processada e aprovada. É como se ela estivesse na "fila de espera" para ser confirmada.   - **Como proceder**   Para conseguir realizar a compensação financeira da sua NFC-e, siga os passos abaixo:   1. Primeiro, localize a nota desejada na tela **"Movimentação Financeira"** usando o campo "Nro Nota". 2. Em seguida, verifique o status atual da nota no **Portal de Vendas/Compras**. 3. Se a nota estiver com o status **"Aguardando Autorização"**, será necessário regularizá-la antes de qualquer ação financeira. Para isso:    - Acesse o **Portal de Vendas**.    - Utilize a opção **"NF-e"** e depois **"Buscar Autorização"**. 4. Após a nota ser **aprovada** pela SEFAZ, você poderá voltar para a movimentação financeira e realizar a compensação normalmente.  - **Exemplo**   Imagine que você emitiu uma NFC-e e precisa compensar o valor, mas ao tentar, o sistema não permite. Ao verificar o status da nota, você percebe que ela está como "Aguardando Autorização". Nesse caso, você precisará ir ao Portal de Vendas e usar a função "Buscar Autorização" para que a SEFAZ aprove a nota. Somente depois que o status mudar para "Aprovada" (ou um dos outros permitidos), você poderá retornar à movimentação financeira e compensar o valor sem problemas. |
| --- |
