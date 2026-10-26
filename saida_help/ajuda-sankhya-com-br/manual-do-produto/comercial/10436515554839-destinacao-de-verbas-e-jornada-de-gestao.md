---
id: "10436515554839"
titulo: "Destinação de Verbas e Jornada de Gestão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:17:31Z"
rotulos: ["Configuração", "Parceiro", "Crédito", "Fornecedor", "Financeiro", "br.com.sankhya.mgecom.DestinacaoVerbas", "Gestão de Verbas", "Status de Destinação", "Destinação de Verbas"]
---

# Destinação de Verbas e Jornada de Gestão

```
 Módulo: Comercial > Rotinas                    Versão disponível: A partir da 4.16
```

---

![Imagem 1: Essa tela está vinculada ao produto "30936 - Gestão de Verbas de Fornecedor/W" .](https://ajuda.sankhya.com.br/hc/article_attachments/16110043693975) Essa tela está vinculada ao produto **"30936 - Gestão de Verbas de Fornecedor/W"**.

---

A **Gestão de Verbas** visa aumentar suas vendas, melhorar suas campanhas de marketing e ter o apoio financeiro dos seus principais fornecedores. Com ela, é possível organizar recursos para promoções, anúncios e espaço em gôndola, fortalecendo a parceria com fornecedores e ganhando margem de negociação.

Para garantir o uso máximo desses recursos, o módulo segue esta jornada:

1. **Acordo de Verbas:** Cadastro e definição de critérios.
2. **Apuração:** Gerenciamento de metas.
3. **Verbas:** Geração de crédito ou débito.
4. **Gerência:** Visualização gerencial.
5. **Destinação:** Vinculação estratégica (descrita abaixo).

---

### Sobre esta rotina

Após a geração de Verbas, na tela **Destinação de Verbas**, você registra onde a verba será utilizada, podendo ser para: **Destinação Financeira**, **Rebaixa de Preço** (redução de preço de venda) ou **Rebaixa de Custo**.

Esta tela não controla o recebimento físico do valor, apenas informa como ele será processado no sistema. A ligação entre a destinação e o recebimento é definida pelo parâmetro **"Permite Destinar Verba Sem Recebimento? - DESVBASEMRCB"**:

- **Se desligado:** O sistema bloqueia a destinação até que o financeiro seja efetivado (baixa do título). Isso evita reduções de custos ou preços sem a garantia do recebimento.
- **Se ligado:** Permite a destinação para provisões ou títulos ainda em aberto.

> **⚠️ Atenção!** Uma verba pode ser utilizada para **bonificação** (vincular a notas fiscais) ou **destinação**, mas nunca para ambos com o mesmo saldo. O saldo já vinculado a uma nota de bonificação não pode ser utilizado para rebaixa de preço ou custo.

![Imagem 2: ⚠️ Atenção! Uma verba pode ser utilizada para bonificação (vincular a notas fiscais) ou destinação , mas nunca para…](https://ajuda.sankhya.com.br/hc/article_attachments/26787705313943)

Acesse os links abaixo para conhecer as funcionalidades dessa tela:

| Funcionalidades da tela | |
| --- | --- |
| [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o#filtros) | [Grade Verbas](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o#gradeverbas) |
| [Grade Inferior](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o#gradeinferior) | [Botões da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o#bot%C3%B5esdatela) |
| [Parâmetros que influenciam a rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o#par%C3%A2metrosqueinfluenciamarotina) |  |

---

### Filtros

![Imagem 3: Filtros](https://ajuda.sankhya.com.br/hc/article_attachments/26751515716375)

#### Filtros da Grade Verbas

Pode-se filtrar as destinações realizadas ou as verbas que serão utilizadas no processo de destinação. Esse painel de filtros contém os seguintes campos:

O campo **"Cód. Destinação"** será utilizado para consultar, alterar ou cancelar alguma destinação previamente realizada. Com esse código informado, o sistema irá bloquear automaticamente os demais filtros da tela, considerando apenas esse critério para o filtro. Caso queira criar uma nova destinação, deverá utilizar os demais campos do Painel de Filtros.

No campo **"Dt. Acordo"** selecione um período específico para exibição das verbas. 

Também poderá filtrar pelo **"Nro. Verba"**, **"Parceiro"** e/ou **"Empresa"** específicos.

#### Filtros da Grade Financeiros

Esse painel de filtros contém os campos abaixo:

- Construtor de filtros personalizados;
- Dt. Negociação;
- Nro. Único;
- Nro. Nota;
- Parceiro;
- Natureza;
- Centro de Resultado.

#### Filtros da Grade Descontos Promocionais

Quando acionado o botão ![Imagem 4: Quando acionado o botão "Rebaixa de Preço" , a grade inferior terá seu nome alterado para "Descontos Promocionais" .](https://ajuda.sankhya.com.br/hc/article_attachments/10591264548503) **"Rebaixa de Preço"**, a grade inferior terá seu nome alterado para **"Descontos Promocionais"**.

Nessa grade, poderá filtrar por **"Período Vigência"** ou por **"Nro. Único Desconto Promocional"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o#top)

### Grade Verbas

![Imagem 5: Grade Verbas](https://ajuda.sankhya.com.br/hc/article_attachments/26809469296791)

O **"Cód. Destinação"** será gerado automaticamente e preenchido após a concretização da destinação, não sendo possível editá-lo.

O número da verba será apresentado na coluna **"Nro.Verba"**.

Nas colunas **"Parceiro"** e **"Nome Parceiro"** serão exibidos o código e nome do Parceiro, respectivamente.

O código e nome da empresa serão apresentados respectivamente nas colunas **"Empresa"** e **"Nome Fantasia"**.

A coluna **"Valor da Verba"** apresentará o valor da verba cadastrado inicialmente.

O valor da verba que ainda não foi destinado será exibido na coluna **"Valor disponível"**.

A coluna **"Valor a destinar"** inicialmente exibe valor zero e pode ser editada pelo gestor, quando definido o valor a ser destinado. Por padrão, o valor disponível será carregado ao dar um duplo clique no campo.

**Observação:** caso a destinação esteja com o status Destinado, não será permitida a edição do campo Valor a destinar. Nesse caso, poderá apenas consultar os dados ou desfazer a destinação por meio do botão **"Desfazer Destinação"**.

![Imagem 6: O sistema irá apresentar nessa grade apenas as verbas do tipo Crédito , que estejam confirmadas e possuam saldo…](https://ajuda.sankhya.com.br/hc/article_attachments/16110043693975) O sistema irá apresentar nessa grade apenas as verbas do tipo Crédito, que estejam confirmadas e possuam saldo disponível para destinação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o#top)

### Grade Inferior

![Imagem 7: Grade Inferior](https://ajuda.sankhya.com.br/hc/article_attachments/26752065924247)

Quando o botão ![Imagem 8: Quando o botão "Financeiro" estiver acionado, a grade inferior exibirá lançamentos financeiros do tipo Despesa . Serão…](https://ajuda.sankhya.com.br/hc/article_attachments/16110043697559) **"Financeiro"** estiver acionado, a grade inferior exibirá lançamentos financeiros do tipo Despesa. Serão apresentados apenas os lançamentos que não estão vinculados à uma destinação, para evitar que uma mesma despesa seja destinada mais de uma vez. Despesas já destinadas só serão exibidas na grade quando utilizado o filtro por Cód. Destinação.

**Observação:** na coluna **"Vlr. Utilizar"** será definido o valor que será utilizado da verba para a despesa.

Vale ressaltar que, na destinação do tipo Financeiro, o vínculo será estabelecido apenas quando a destinação estiver na situação Destinado, pois, caso contrário, ela será considerada apenas um rascunho.

#### Barra totalizadora da Grade Financeiros

Nessa grade tem-se os seguintes totalizadores:

- **Vlr do Desdobramento:** esse totalizador irá apresentar a soma de todas as Despesas exibidas na grade.
- **Vlr. Utilizar:** aqui, será exibida a soma do valor definido no campo Vlr. Utilizar das despesas selecionadas na grade.

---

Selecionando o botão ![Imagem 9: Selecionando o botão "Rebaixa de Preço" , serão exibidos os descontos promocionais a serem vinculados na destinação.](https://ajuda.sankhya.com.br/hc/article_attachments/10591264548503) **"Rebaixa de Preço"**, serão exibidos os descontos promocionais a serem vinculados na destinação. 

Ao aplicar o filtro da Rebaixa de Preço, serão apresentados apenas descontos promocionais por percentual ou valor.

**Notas:**

- Não é possível selecionar mais de um desconto promocional por destinação. Além disso, na destinação do tipo Rebaixa de Preço, o vínculo da destinação com o desconto promocional será considerado apenas na situação Destinado.
- Quando estiver em um processo de vendas e o produto selecionado pertencer à uma Rebaixa de Preço e a operação utilizar todo o saldo disponível da verba, o sistema irá desativar automaticamente o desconto promocional, alterando a data final da campanha para o dia anterior à data da operação.
- Se a data da operação for maior que a data final da campanha, o desconto promocional não será considerado e será utilizado o preço de venda anterior.

---

Acionando o botão ![Imagem 10: Acionando o botão "Rebaixa de Custo" , serão apresentados os seguintes campos para configuração:](https://ajuda.sankhya.com.br/hc/article_attachments/11330213207831) **"Rebaixa de Custo"**, serão apresentados os seguintes campos para configuração:

No campo **"Data Referência"** informe a data de referência para a rebaixa de custo do produto. Sendo que, este campo deve iniciar com a data atual e só poderá ser alterado para uma data retroativa, isto é, não é permitido inserir uma data futura.

Defina o produto no campo **"Cód. Produto"**. Ao configurar este campo, a **"Unidade"** será preenchida automaticamente, de acordo com o produto selecionado. 

No campo **"Local"** serão exibidas as opções de local para seleção conforme o produto selecionado. Se o parâmetro **"Controla Custos por Local? - CUSTOPORLOC"** estiver ligado, este campo será de preenchimento obrigatório. 

No campo **"Empresa"** serão exibidas para seleção as empresas conforme o produto selecionado.

O campo **"Qtd. Estoque**" exibe o saldo final do estoque de acordo com a **"Data de referência"** informada. Porém, se o parâmetro **"Controla Custos por Controle? - CUSTOPORCONT"** estiver ligado, nesse campo será apresentado o saldo do estoque conforme a Data de referência e o Controle definidos.

No campo **"Controle"** poderá selecionar a variação do produto. Esse campo ficará habilitado para edição apenas se o parâmetro **"Controla Custos por Controle? - CUSTOPORCONT"** estiver ligado e se o produto informado no campo **"Cód. Produto"** estiver configurado com controle adicional do tipo **"Grade"**, **"Lista"**, **"Livre"**, **"Série"**, **"Parceiro"**, **"Número do Lote"** ou **"Data de Validade"** (essa definição é realizada na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos), aba [Medidas Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque), sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abacontroleadicional), campo **"Controlar Por"**).

**Observações:**

- Para o Controle do tipo Série, o campo irá exibir **"Controle Série"**;
- Caso o parâmetro CUSTOPORCONT estiver ligado e o produto não possuir controle, mas tiver saldo de estoque, o campo Controle exibirá **"Sem controle definido"**;
- Se o parâmetro CUSTOPORCONT estiver desligado, o campo Local será desabilitado.

Preencha o campo **"Valor a Destinar"** com o valor que será destinado para o produto. 

Ainda tem os seguintes campos para consulta: 

No campo **"Custo Médio Gerencial (Antes)"** será apresentado o custo médio gerencial da data de referência informada para o produto, antes da rebaixa de custo. 

Será exibido no campo **"Vlr. Estoque (Antes)"** o valor total do estoque da data de referência informada para o produto, antes da rebaixa de custo.

O campo **"Custo Médio Gerencial (Após)"** exibirá o custo médio gerencial após a concretização da rebaixa de custo. Este campo será preenchido apenas se a consulta for realizada pelo  **"Cod. Destinação"** nos [Filtros da Grade Verbas](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas#filtros).

O campo **"Vlr. Estoque (Após)"** apresentará o valor do estoque considerando o novo custo após a concretização da rebaixa de custo, ou seja, o preenchimento deste campo só ocorrerá se a consulta for realizada pelo **"Cod. Destinação"** no Filtros da Grade Verbas.

**Nota:** na destinação do tipo Rebaixa de Custo, a nota gerencial deverá ser gerada apenas quando a destinação for concretizada, ou seja, quando sua situação mudar para Destinada. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o#top)

---

### Botões da tela

Clique nas imagens abaixo para verificar sobre cada um dos botões:

[![Imagem 11: Clique nas imagens abaixo para verificar sobre cada um dos botões:](https://ajuda.sankhya.com.br/hc/article_attachments/10542816226455)](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o#bot%C3%A3odestinarverba)                              [![Imagem 12: Clique nas imagens abaixo para verificar sobre cada um dos botões:](https://ajuda.sankhya.com.br/hc/article_attachments/10543544626455)](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o#bot%C3%A3odesfazerdestina%C3%A7%C3%A3o)                          [![Imagem 13: Clique nas imagens abaixo para verificar sobre cada um dos botões:](https://ajuda.sankhya.com.br/hc/article_attachments/10592176361751)](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o#bot%C3%A3odesvincularsaldorestante)

---

#### Botão Destinar Verba

Esse botão efetiva a destinação da verba nas despesas selecionadas, ou seja, ao acioná-lo, será feito o vínculo da despesa à verba, abatendo o saldo utilizado ao saldo disponível.

**Observação:** esse botão estará ativo somente se o valor definido no campo à destinar nas verbas corresponder ao valor definido nas despesas.

Em relação a destinação do tipo Rebaixa de Custo, ao definir o Valor a Destinar e a Data de Referência e acionar o botão Destinar Verba, o sistema lançará automaticamente uma nota gerencial com base em cada data de referência, utilizando o modelo de nota vinculado no parâmetro **"Modelo de Nota Rebaixa de Custo. - MODNOTAREBCUS"**.

**Importante:** para que a movimentação gerada pela nota gerencial de Rebaixa de Custo seja apresentada na tela [Kardex](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594414-Kardex), selecione na seção **"Tipo de relatório"**, campo **"Tipo Custo"** a opção **"Gerencial"**.  

Quando o valor do campo **"Total Verbas a Destinar"** for diferente do **"Total a utilizar"**, ao acionar o botão Destinar Verba será apresentada a seguinte mensagem:

**“O valor total a destinar da(s) verba(s) está divergente do valor total a utilizar no(s) Produto(s). Verifique os valores definidos.”**

Para desfazer a destinação do tipo Rebaixa de Custo é necessário pesquisá-la por meio do filtro Cód. Destinação e acionar o botão Desfazer Destinação, assim, o sistema irá excluir o lançamento da nota gerencial e recalcular o custo para os produtos.

É importante ressaltar que, não é possível efetuar a destinação do tipo Rebaixa de Custo, caso um dos itens selecionados estejam com o saldo do estoque zerado ou negativado na Data de Referência informada.

---

![Imagem 14: Informações adicionais](https://ajuda.sankhya.com.br/hc/article_attachments/16110043701527) **Informações adicionais**

O sistema irá gerar a nota gerencial da destinação do tipo Rebaixa de Custo, independente das configurações de Local, Agrupamento Mínimo e Tabela de Preço realizadas em outras rotinas. Observe:

- Mesmo que o parâmetro **"Controla Custos por Local ?-CUSTOPORLOC"** esteja desabilitado e a marcação  **"Usa Local"** apresentada na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque), sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abaestoque) esteja habilitada, o sistema utilizará para a nota gerencial o local padrão definido.
- A informação preenchida no campo **"Agrupamento Mínimo"** na tela de Cadastro de Produtos, aba Medidas e Estoque, sub-aba Estoque, não irá impactar na geração da nota gerencial.
- Mesmo que o produto não esteja cadastrado em nenhuma tabela de preço e o parâmetro **"Tabela de Preços por:-TIPTABPRECO"** esteja com a opção **"Única"** selecionada, será realizada a geração da nota gerencial.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o#bot%C3%B5esdatela)

---

#### Botão Desfazer Destinação

O botão Desfazer Destinação será apresentado na tela apenas quando se utilizar o filtro por Cód. Destinação e houver resultado, pois dessa forma serão exibidos todos os registros pertencentes ao processo.

Quando esse botão for acionado, será cancelado o vínculo realizado pela destinação, devolvendo automaticamente o saldo para as verbas:

[GIF animado: Imagem 15: Quando esse botão for acionado, será cancelado o vínculo realizado pela destinação, devolvendo automaticamente o saldo…](https://ajuda.sankhya.com.br/hc/article_attachments/10543802665879)

**Importante:** caso a destinação seja cancelada através do botão Desfazer Destinação, o evento de liberação de limites será excluído automaticamente, para garantir a integridade dos dados.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o#bot%C3%B5esdatela)

---

#### Botão Desvincular saldo restante

Esse botão deve ser utilizado para o caso de ser selecionada uma destinação do tipo **"Rebaixa de Preço"** previamente realizada e for decidido por desfazer o vínculo para reutilizar o saldo remanescente em outra destinação, ou seja, ao acionar esse botão, o sistema automaticamente encerrará a campanha vinculada e retornará o saldo não utilizado para a verba.

![Imagem 16: O botão Desvincular saldo restante será apresentado apenas quando o filtro utilizado for por Cód. Destinação , quando a…](https://ajuda.sankhya.com.br/hc/article_attachments/16110043693975) O botão Desvincular saldo restante será apresentado apenas quando o filtro utilizado for por Cód. Destinação, quando a campanha já tiver vendas relacionadas e a destinação possua saldo não utilizado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o#bot%C3%B5esdatela) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o#top)

---

### Parâmetros que influenciam a rotina

**Permite Destinar Verba Sem Recebimento? - DESVBASEMRCB**: com este parâmetro ligado, o sistema irá permitir destinar uma verba mesmo antes da efetivação do recebimento financeiro (baixa do lançamento no financeiro). Se for desligado, o sistema bloqueará a destinação de uma verba até que o recebimento seja efetivado.

**Observação:** caso haja a concretização ao menos do recebimento da 1ª parcela, será possível destinar apenas o valor recebido até o momento. Nesse caso, quando entrar no modo edição, o valor preenchido automaticamente será o que estiver sido recebido até o momento da destinação e não o valor total da verba.

**Limite para Destinação Retroativa de Verba. - LIMDESRETROVBA**: configure esse parâmetro para definir uma quantidade de dias para realizar uma Rebaixa de Custo retroativa, sendo que, por padrão, esse parâmetro tem o valor de 7 dias. 

**Nota:** o sistema irá bloquear uma destinação retroativa que supera a quantidade de dias informada nesse parâmetro.

**Modelo de Nota Rebaixa de Custo. - MODNOTAREBCUS**: informe nesse parâmetro, o código do modelo de nota para a Rebaixa de Custo cadastrado previamente na tela [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos).

**Valor Limite Exigir Liberação Destinação Verba - VLEXIGLIBDESVBA**: defina nesse parâmetro se o sistema deverá exigir ou não uma liberação para efetivar a destinação de uma verba. Caso esteja vazio ou com valor zero, será considerado que o mesmo está desligado. Porém, se houver um valor estabelecido maior do que zero, será apresentado um pop-up para que a solicitação de liberação de limites seja direcionada a um liberador específico. 

**Observação:** o valor a ser considerado na validação é referente ao valor total da destinação e não de apenas uma única verba.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas-e-Jornada-de-Gest%C3%A3o#top)

---

![Imagem 17: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16110043705495) Acesse também:

[Acordo de Verbas](https://ajuda.sankhya.com.br/hc/pt-br/articles/25805142239767)
[Apuração de Acordo de Verbas](https://ajuda.sankhya.com.br/hc/pt-br/articles/25645696814359)

[Verbas](https://ajuda.sankhya.com.br/hc/pt-br/articles/8106295032343)
[Gerência de Verbas](https://ajuda.sankhya.com.br/hc/pt-br/articles/10631931486615)
[Vincular Bonificações e Verbas](https://ajuda.sankhya.com.br/hc/pt-br/articles/9357252466071)
