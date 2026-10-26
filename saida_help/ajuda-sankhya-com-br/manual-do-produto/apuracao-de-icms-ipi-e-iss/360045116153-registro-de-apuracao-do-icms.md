---
id: "360045116153"
titulo: "Registro de Apuração do ICMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Apuração e Livros Fiscais > Apuração de ICMS, IPI e ISS"
atualizado_em: "2026-09-15T14:22:35Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "Registro de Apuração do ICMS", "Livros Fiscais", "SEFAZ", "ICMS", "Impostos", "CFOP", "CODOBSDIFICMS", "CODOBSICMSCOMP", "Deduções", "DIFICMSNAOBSERV", "Estorno de Créditos", "Estorno de Débitos", "Outros Créditos", "Outros Débitos", "PERCFINANIND", "PERCGARANTIND", "Substituição Tributária", "br.com.sankhya.mgeliv.rel.registroapuracaoicms", "Registro de Apuração do ICMS manual", "LIVICMSCALZERO"]
---

# Registro de Apuração do ICMS

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313096476823) Módulo: Livros Fiscais > Relatórios
```

---

Por meio desta tela, será realizada a emissão dos Livros de Apuração do ICMS (modelo 9), para um Estabelecimento específico ou para as filiais vinculadas.

A intenção é que sejam gerados os valores totais referentes as notas de Entradas (créditos), notas de saídas (débitos) e os ajustes tanto a débito quanto a crédito, onde serão encontrados os valores finais do período, e apurando neste caso se o Estabelecimento terá um saldo credor ou devedor de ICMS.

![Imagem 2: A intenção é que sejam gerados os valores totais referentes as notas de Entradas (créditos), notas de saídas (débitos)…](https://ajuda.sankhya.com.br/hc/article_attachments/13753808707095)

| [Configurações iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS#configuraesiniciais) |  | [Opções de Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS#opesdeimpresso) |
| --- | --- | --- |
| [Botões do topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS#botesdotopodatela) |  | [Seção Demonstrativos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS#seodemonstrativos) |
| [Parâmetros que influenciam essa rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS#par%C3%A2metrosqueinfluenciamessarotina) |  |  |

## Configurações iniciais

Primeiramente, você deverá efetuar o preenchimento dos campos que irão filtrar os dados no sistema, a fim de serem gerados de forma agrupada em um relatório.

O primeiro a ser obrigatoriamente preenchido é a **"Empresa"** da qual serão buscadas as informações para apuração.

Se você preencher o campo **"Filiais da UF:"**, o relatório irá conter a apuração de todas as empresas pertencentes ao estado definido.

**Observação:** esse campo só será habilitado para preenchimento se você ligar o parâmetro **"Utiliza UF para apuração de ICMS? - USAUFAPURACAO"**.

Em seguida, determine o período que irá abranger a geração do relatório; este período é informado através dos campos **"Data Inicial"** e **"Data Final"**.

Nos casos em que ainda a geração do relatório ainda não foi realizada, o campo **"Página Inicial"** estará preenchido com o numeral "0". A medida que forem sendo feitas gerações, ele será alimentado com a numeração da última página do período gerado anteriormente.  também a liberdade de informá-lo manualmente, caso necessário.

O campo **"Página Final"** será automaticamente alimentado com a numeração da última página referente a última geração efetuada.

A **"Data Emissão"** será apresentada automaticamente já na abertura da tela; se refere a data em que está sendo realizada a criação do referido relatório.

O campo **"Formato da Impressão"** disponibiliza duas formas de exportação dos dados na geração do relatório, auxiliando na conferência e verificação de possíveis erros. O campo pode ser definido entre os formatos PDF e Excel; caso o campo fique em branco, o padrão será o formato PDF. As referidas opções apresentam respectivamente os seguintes comportamentos:

- **PDF:** Quando for selecionado o formato de impressão PDF, na visualização do relatório, o mesmo será aberto neste formato.
- **Excel:** Sendo selecionado o formato de impressão Excel, ao clicar para visualizar o relatório, o mesmo será baixado conforme as configurações do navegador que está sendo utilizado, ou seja, o arquivo poderá ser baixado automaticamente ou poderá ser aberta uma tela questionando ao usuário o local onde deseja salva-lo. Deste modo deve-se acessar o local onde o arquivo foi baixado e abri-lo.

Também teremos nesta tela, algumas marcações que irão influenciar diretamente nas informações que serão impressas no relatório:

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS#top)

## Opções de Impressão

Quando a marcação **"Imprimir data/hora da emissão?"** estiver realizada, fará com que a data e a hora de emissão do relatório, sejam impressas em seu lado superior direito.

Se a marcação **"Imprimir apuração Subs. Tributária"** for efetuada, será apresentada na emissão deste livro, um complemento com as informações para apuração de Substituição Tributária.

Ao ligar a marcação **"Imprimir detalhamento de ICMS/ST por UF"**, o sistema irá gerar um sub-relatório de Apuração ST por UF, junto à Apuração ST normal, ou seja, será gerado um relatório de apuração por UF inserido no relatório de Apuração ST normal, caso você possua registros com ICMS/ST em UF's diferentes. Se não houverem registros com ICMS/ST e a referida marcação estiver ligada, o sub-relatório será gerado com valores zerados. Considere também que, os valores apresentados são um somatório das movimentações da tela [Cadastro Livro ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874), sendo elas separadas por UF. 

---

![Imagem 3: Informações adicionais acerca das respectivas marcações:](https://ajuda.sankhya.com.br/hc/article_attachments/16345491583767) **Informações adicionais acerca das respectivas marcações:**

**(1)** Quando a marcação Imprimir apuração Subs. Tributária? for acionada e a marcação Imprimir detalhamento de ICMS/ST por UF? desabilitada, apenas a apuração consolidada será gravada no registro;

**(1)** Porém, ao habilitar ambas as marcações acima, o sistema irá armazenar a apuração consolidada e a apuração por UF, uma vez que, as informações por UF serão consideradas no relatório conforme a marcação Imprimir detalhamento de ICMS/ST por UF? e na geração dos registros E200 e E210.

**Nota:** realizando qualquer alteração no movimento das notas do período apurado, ao emitir novamente um relatório, então os valores afetados substituirão as informações do período anterior, mesmo que neste período não tenha tido alterações de movimento.

---

Ao selecionar a marcação **"Imprimir apenas imobilizados?"** serão selecionados para impressão, apenas ajustes com os códigos referentes ao Imobilizado e também os valores já apurados pelos movimentos das Notas Fiscais com as seguintes CFOP's:

- **Entrada:** 1551, 2551, 3551, 1552, 2552, 3552, 1553, 2553, 3553
- **Saída:** 5551, 6551, 7551, 5552, 6552, 7552, 5553, 6553, 7553

A marcação **"Imprimir 'S' da Tare junto com CFOP?"** quando realizada, irá imprimir o identificador **"S"** nos casos em que forem apresentadas operações sujeitas a TARE.

Quando você marca a opção **"Convênio Produzir?"**, o sistema organiza os movimentos em **"Normal"** e **"Produzir"** no relatório, mostrando os totais separados por tipo de [CFOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714).

Isso ajuda a seguir as regras da Instrução Normativa - IN 467/00-GSF da SEFAZ-GO.

Ao marcar a opção **"Convênio Produzir?"**, o sistema desconsidera os valores digitados manualmente nos campos de débito, crédito e ajustes, pois essa funcionalidade é incompatível com o preenchimento desses dados.

Esta Instrução Normativa se refere a um incentivo fiscal, que beneficia suas operações fiscais financiando o valor do saldo devedor nas operações de industrialização em 73%, recolhendo apenas 27% do saldo devedor e 10% sobre os 73% como garantia de cumprimento do programa.

Dois parâmetros influenciam esta Instrução Normativa no sistema:

- **Percentual Imobilizado Financiado para Indústria - PERCFINANIND:** Neste será informado o percentual financiado para a indústria.
- **Percentual de Garantia Financiado para Indústria - PERCGARANTIND:** Neste parâmetro, informe qual o percentual de garantia sobre o financiamento.

**Importante:** a marcação **"Convênio produzir?"** é incompatível com a marcação **"Imprimir apenas imobilizados?"**; deste modo, ambas não podem estar marcadas simultaneamente.

**Observação:** quando a marcação Convênio Produzir for realizada, o campo **"Saldo Credor Ant."** terá duas opções para informar o saldo; uma para o **"Saldo Normal"** e outra para o **"Saldo Produzir"**.

Ao acionar a marcação **"Imprimir número do livro?"**, será habilitado para preenchimento o espaço abaixo da marcação, para que seja informado o número do livro e esta numeração seja impressa no relatório.

Ao marcar o campo **"Imprimir filiais com movimento?"**, será definido se as filiais sem movimento irão aparecer no relatório a ser gerado.

**Nota:** assim como o campo Filiais da UF:, a marcação Imprimir filiais com movimento? será disponibilizada apenas se o parâmetro Utiliza UF para apuração de ICMS? - USAUFAPURACAO estiver ligado.

O campo **"Imprimir Ajuste"** possui uma lista de opções para que o "Resumo da Apuração do Imposto (ICMS)" possa contemplar ou não os lançamentos do **"Sub-Apuração"**, sendo elas:

- **Ajuste de Apuração e Ajuste de Sub-Apuração:** Ao selecionar esta opção, o ajuste de apuração e sub-apuração serão impressos no Resumo da Apuração do ICMS, independente se a marcação Sub-Apuração (tela [Ajuste da Apuração de ICMS e ICMS ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607654), aba **"Geral"**) estiver efetuada.
- **Somente Ajuste de Apuração:** Ao selecionar esta, o resumo da apuração contemplará somente os lançamentos de Ajustes de Apuração que não estiverem marcados como Sub-Apuração.
- **Somente Ajuste de Sub-Apuração:** Quando esta opção for selecionada, serão exibidos nos relatórios de Resumo da Apuração do ICMS apenas os ajustes que se encontrarem marcados como Sub-Apuração.

**Nota:** de acordo com a opção selecionada no campo acima, será exibido na página Resumo da Apuração do Imposto (ICMS) do relatório o nome do ajuste escolhido.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS#top)

## Botões do topo da tela

No alto da tela, pode-se notar alguns botões de suma importância para geração do relatório. São eles:

![Imagem 4: Abrir: Ao acionar este botão, serão recuperadas e apresentadas na seção Demonstrativos (detalhada mais abaixo) as…](https://ajuda.sankhya.com.br/hc/article_attachments/360076226914) **Abrir:** Ao acionar este botão, serão recuperadas e apresentadas na seção Demonstrativos (detalhada mais abaixo) as informações relacionadas às apurações anteriores da empresa e período definidos.

![Imagem 5: Salvar: Nesta opção, é feito o salvamento dos valores apurados do período, somados aos ajustes lançados já apurando o…](https://ajuda.sankhya.com.br/hc/article_attachments/360076226994) **Salvar:** Nesta opção, é feito o salvamento dos valores apurados do período, somados aos ajustes lançados já apurando o saldo e gravando os totais com seus respectivos tipos de apuração. Deste modo para o mês seguinte, os saldos do mês anterior serão considerados. Além disso, estes valores também são base para geração dos registros do EFD Fiscal no registro de apuração deste.

![Imagem 6: Visualizar: Por este botão, o relatório poderá ser visualizado, sendo que este estará construído de acordo com os…](https://ajuda.sankhya.com.br/hc/article_attachments/360076226934) **Visualizar:** Por este botão, o relatório poderá ser visualizado, sendo que este estará construído de acordo com os filtros e marcações anteriormente efetuadas.

![Imagem 7: Gerar Dif.Alíq.ICMS em Outros Déb/Créd ou Gerar Dif.Alíq.ICMS em Observação: Estes botões serão utilizados, se para a…](https://ajuda.sankhya.com.br/hc/article_attachments/360077396573) **Gerar Dif.Alíq.ICMS em Outros Déb/Créd** ou ![Imagem 8: Gerar Dif.Alíq.ICMS em Outros Déb/Créd ou Gerar Dif.Alíq.ICMS em Observação: Estes botões serão utilizados, se para a…](https://ajuda.sankhya.com.br/hc/article_attachments/360077399073) **Gerar Dif.Alíq.ICMS em Observação:** Estes botões serão utilizados, se para a Empresa e período selecionados, existirem valores de diferencial de alíquota em suas notas de Entrada ou Saída.

A forma com que este botão será apresentado e, consequentemente seu comportamento, irão depender da configuração do parâmetro **"Gerar Dif.Alíq.ICMS em Observação no Liv. Apuração - DIFICMSNAOBSERV"**. Caso ele esteja desabilitado, teremos o botão**"Gerar Dif.Alíq.ICMS em Outros Déb/Créd"**; caso o referido parâmetro seja habilitado, o botão será lido como **"Gerar Dif.Alíq.ICMS em Observação"**.

Além disto, poderemos fazer esta modificação, através da marcação apresentada à frente do próprio botão, denominada **"Dif.ICMS na observação, sem afetar Débito/Crédito"**.

Independente da forma que a empresa trabalhe utilizando o botão mencionado, na primeira ou segunda situação, você deverá configurar o parâmetro **"Código da Observação para Diferença de ICMS - CODOBSDIFICMS"**, em que será informado o código referente a observação para diferença de alíquota de ICMS. Não sendo realizada a configuração mencionada, será apresentada a seguinte mensagem:

**"O parâmetro CODOBSDIFICMS está sem o código de observação para a Dif.Aliq.ICMS."**

É importante ressaltar que, no parâmetro **"Código da Observação para ICMS Complementar - CODOBSICMSCOMP"** informe o código relacionado a observação para ICMS Complementar. Este parâmetro não pode ser preenchido com o mesmo código informado no parâmetro citado anteriormente; caso isso ocorra, será exibida a mensagem abaixo:

**"O parâmetro CODOBSDIFICMS de 'Dif.Alíq.ICMS' não pode ser igual ao parâmetro CODOBSICMSCOMP de 'ICMS Complementar'.**

Além disso, quando a geração for realizado, o sistema exibirá uma mensagem o informando a quantidade de registros que foram gerados.

Ao clicar no botão **"Gerar Financeiro do ICMS Normal Op. Própria a Recolher"** o sistema terá o seguinte comportamento:

1. Primeiramente, será verificado se a empresa indicada para a apuração possui dados de ICMS Normal Op. Própria a Recolher informados na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba [EFD - Escrituração Fiscal Digital](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaefdescrituraofiscaldigital), seção [EFD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#se%C3%A7%C3%A3oefd):

- Se existir, será efetuado o lançamento do ICMS Normal Op. Própria a Recolher Apurados no financeiro. Além disso, o pop-up **"Confirmar geração dos financeiros?"** será apresentado com todos os financeiros que serão incluídos.

![Imagem 9: Se existir, será efetuado o lançamento do ICMS Normal Op. Própria a Recolher Apurados no financeiro. Além disso, o…](https://ajuda.sankhya.com.br/hc/article_attachments/4408830834711)

- Caso não exista será apresentada a mensagem abaixo:

**"Não existem valores apurados a recolher para a geração do Financeiro gravados. Execute a opção 'Gravar'."**

2. Depois, será verificado se já foi gerado o financeiro para a **"Empresa"** informada. Caso encontre, será apresentada a mensagem:

**"Já existe um registro para a empresa no período informado. Deseja substitui-lo?"**

Optando por **"Sim"**, será analisado o status do titulo no financeiro. Se ele já estiver baixado e/ou contabilizado, será apresentada uma mensagem comunicando que não foi possível excluir o titulo, devido o mesmo estar baixado e/ou contabilizado. Do contrário, o sistema irá excluir o titulo e incluir um novo com as informações das preferências.

Clicando em **"Não"**, o sistema não executará nenhuma operação.

Com os financeiros gerados, serão preenchidos automaticamente os seguintes campos da tela [Movimentação financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874):

- No Painel Principal o campo **"Parceiro"**, será informado de acordo com o **"Cód. Parceiro Secretaria da Receita Estadual"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294-Estados#abageral), localizada na tela [Estados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294).
- Os campos **"Dt. Negociação"** e **"Dt. Entrada e Saída"**, localizados no Painel Principal e na aba Geral, respectivamente, serão preenchidos com a **"Data Emissão"** da efetiva apuração do impostos a pagar.
- Na aba [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#abalanamento), o campo **"Receita/Despesa"** será informado como **"Despesa"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS#top)

## Seção Demonstrativos

A seção **"Demonstrativos"** será alimentada com o acionamento do botão **"Abrir"**, que traz os dados relacionados às apurações anteriores realizadas pela empresa.

![Imagem 10: A seção "Demonstrativos" será alimentada com o acionamento do botão "Abrir" , que traz os dados relacionados às…](https://ajuda.sankhya.com.br/hc/article_attachments/1500004668881)

Serão apresentados os valores referentes a:

- Outros Débitos;
- Estorno de Débitos;
- Outros Créditos;
- Estorno de Créditos;
- Deduções.

Valores estes, a respeito do ICMS e Substituição Tributária. Poderemos observar à frente de cada campo, o botão ![Imagem 11: Valores estes, a respeito do ICMS e Substituição Tributária. Poderemos observar à frente de cada campo, o botão que…](https://ajuda.sankhya.com.br/hc/article_attachments/360077400193) que quando acionado, abre a tela [Ajuste da Apuração de ICMS e ICMS ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607654), onde são inseridos os ajustes necessários (na maioria dos casos, estes ajustes são solicitados pela contabilidade da empresa).

**Observação:** a apuração de valores referentes ao ICMS-ST se referem a devoluções de compras e vendas.

Caso a empresa possua algum saldo credor, este deve ser informado nos campos **"Saldo Credor Ant."** Normal e **"Saldo Credor Ant"** para Substituição Tributária. O campo **"Observações"** é destinado a informar algum ponto relevante para a apuração que está sendo realizada.

**Observação:** para que o sistema mantenha o valor 0 (zero) no campo Saldo Credor Ant, o parâmetro **"Liv. Apuração calc. saldo anterior se inf. zero-LIVICMSCALZERO"** deve estar desligado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS#top)

## Parâmetros que influenciam essa rotina

Quando o parâmetro **"Consid. Apuração ST, Notas com base sem ret. - CONSAPUSEMVLRET"** estiver ligado, o sistema irá identificar as notas que estão na tela [Cadastro Livro ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874-Cadastro-Livro-ICMS-IPI) que tenham a base de retenção e não possua o valor da retenção. Com o parâmetro desligado, serão levadas ao relatório apenas as bases de ST cujo imposto seja maior do que zero.

Com o parâmetro **"Usar Dt. Ent/Saída na Ger. do Liv. Fis. de Saída - USADTSAILIVSAI"** ligado, quando você acessar a rotina Registro de Apuração do ICMS e gerar a apuração, o sistema irá considerar a data do campo **"Dt. do Movimento"** do Livro Fiscal de Saída para gerar esse registro de apuração. Caso esteja desligado, será considerada a **"Dt. do documento"** do Livro Fiscal de Saída.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS#top)
