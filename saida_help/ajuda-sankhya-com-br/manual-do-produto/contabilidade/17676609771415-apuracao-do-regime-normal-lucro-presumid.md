---
id: "17676609771415"
titulo: "Apuração do Regime Normal - Lucro Presumido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17676609771415-Apura%C3%A7%C3%A3o-do-Regime-Normal-Lucro-Presumido"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilidade"
atualizado_em: "2026-07-29T16:01:41Z"
rotulos: ["Configuração", "CSLL", "Impostos", "Contabilidade", "br.com.sankhya.mgecontab.apurlucpres", "br.com.sankhya.mgecontab.configapurlucpres ", "br.com.sankhya.mgecontab.itensapurlp", "Apuração Eficiente do Lucro Presumido no Transporte de Cargas", "Lucro Presumido", "IRPJ"]
---

# Apuração do Regime Normal - Lucro Presumido

```
 Módulo: Contabilidade > Rotinas             Versão: A partir da 4.25
```

---

Neste artigo, abordaremos as etapas de configuração necessárias para realizar a Apuração do Regime Normal - Lucro Presumido (LP).

Essa rotina permite aos optantes pelo Lucro Presumido, tributados pelo Regime de Competência, realizar a apuração do IRPJ e da CSLL de maneira efetiva. E está disponível para execução a partir da Referência 2022.

Podem optar pelo regime tributário Lucro Presumido as empresas com lucro anual de até 78 milhões que estão enquadradas nas seguintes atividades:

- Serviços hospitalares;
- Transportadores;
- Rurais;
- Comércio de mercadorias ou produtos;
- Profissionais liberais, como advogados, dentistas, administradores, médicos, contadores, engenheiros, etc;
- Construção civil;
- Transporte de cargas.

![Imagem 1: Transporte de cargas.](https://ajuda.sankhya.com.br/hc/article_attachments/18142617101207)

## Configurações

### Itens para Apuração do LP

Inicialmente, os registros que constituem a estrutura da apuração são originados na tela **"Itens para Apuração do LP"**. Esta tela tem como finalidade organizar a apuração, tornando mais eficiente a localização dos componentes na estrutura da ECF.

![Imagem 2: Os registros exibidos nessa tela estão em conformidade com os requisitos da ECF.](https://ajuda.sankhya.com.br/hc/article_attachments/17676978711959) Os registros exibidos nessa tela estão em conformidade com os requisitos da ECF.

![Imagem 3: Os registros exibidos nessa tela estão em conformidade com os requisitos da ECF.](https://ajuda.sankhya.com.br/hc/article_attachments/18016693982615)

Se necessário, é possível editar o campo **"Alíquota"** para ajustar a taxa a ser aplicada no registro e o campo **"Grupo"**, que indica o grupo de cálculo ao qual esse registro será atribuído na apuração.

![Imagem 4: Se necessário, é possível editar o campo "Alíquota" para ajustar a taxa a ser aplicada no registro e o campo "Grupo" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/18016655887895)

#### Alíquotas de Presunção correspondentes aos registros da Discriminação da Receita

**(1)** **Presunção da base de cálculo para o IRPJ:**

- 1,6% – Revenda de combustíveis;
- 8,0% – Regra geral (todas empresas que não estão explicitamente nas definições acima e abaixo);
- 16,0% – Serviço de transporte que não seja de carga;
- 32,0% – Prestação de serviços em geral, intermediação de negócios e administração, locação ou cessão de bens móveis, imóveis ou direitos;
- 38,4% – Atividades de operação de empréstimo, de financiamento e de desconto de títulos de crédito realizadas por Empresa Simples de Crédito (ESC) - Lei Complementar nº 167/2019.

(1)** Presunção da base de cálculo para a CSLL:**

- 12,0% – Regra geral (todas empresas que não estão na alíquota de 32%);
- 32% – Prestação de serviços em geral, intermediação de negócios e administração, locação ou cessão de bens móveis, imóveis ou direitos;
- 38,4% – Atividades de operação de empréstimo, de financiamento e de desconto de títulos de crédito realizadas por Empresa Simples de Crédito (ESC) - Lei Complementar nº 167/2019.

### Configurações para apuração do Lucro Presumido

Agora, acesse a tela **"Configurações para apuração do Lucro Presumido"** para cadastrar as regras que serão consideradas para a apuração do Lucro Presumido.

![Imagem 5: Lembre-se que é preciso salvar as configurações iniciais antes de preencher os campos das abas presentes nessa tela.](https://ajuda.sankhya.com.br/hc/article_attachments/17678152534039) Lembre-se que é preciso salvar as configurações iniciais antes de preencher os campos das abas presentes nessa tela. 

No painel principal informe os seguintes campos:

![Imagem 6: No painel principal informe os seguintes campos:](https://ajuda.sankhya.com.br/hc/article_attachments/18016833107735)

Primeiramente informe a **"Empresa"** desejada. Pode-se inserir nesse campo o código da matriz para cadastrar as configurações considerando as especificações contidas nela.

**Nota:** pode-se salvar dois registros para a mesma Empresa com a mesma **"Natureza"**. 

Depois, informe o **"Item da Apuração"**. Este campo representa as linhas analíticas que compõem a apuração e que receberão as configurações para o correto cálculo.

Nesse campo, há alguns itens que não podem ser selecionados, pois referem-se a uma linha fixa na apuração, são eles:

- P300 - 3 À Alíquota de 15%;
- P300 - 4 Adicional IRPJ;
- P300 - 5 Diferença de IRPJ;
- P500 - 2 À Alíquota de 9%;
- P500 - 3 Diferença de CSLL.

Caso tente escolher um deles, o sistema exibirá a mensagem abaixo:

**"O Item selecionado não poderá ser configurado, pois o mesmo refere-se a uma linha fixa na apuração e representa o cálculo do Imposto."**

Em seguida, selecione no campo **"Tipo de Data para Nota"** as datas que serão consideradas na apuração para as informações vindas do [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654). No campo **"Tipo de Data para Financeiro"**, indique as datas que serão consideradas na apuração para as informações provenientes da [Movimentação financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753).

Se necessário pode-se configurar as seguintes marcações:

- **Deduz IPI da BC:** se ativada, os valores de IPI no cabeçalho da nota serão ignorados e lançados diretamente no financeiro. Se desativada, não se aplica;
- **Deduz ICMS ST da BC:** se ligada, os valores de ICMS ST no cabeçalho da nota serão desconsiderados e lançados diretamente no financeiro. Se desligada, não se aplica;
- **Deduz FCP ST da BC:** se ativada, serão desconsiderados os valores de FCP ST somente do cabeçalho da nota. Se desligado, não se aplica;
- **Deduz Descontos Incondicionais da BC:** se ligada, serão desconsiderados os valores de descontos incondicionais somente do cabeçalho da nota. Se desativada, não se aplica.

![Imagem 7: Os campos acima foram definidos com base na Lei 8.541/1992, artigo 14, § 4° .](https://ajuda.sankhya.com.br/hc/article_attachments/17677351131159) Os campos acima foram definidos com base na [Lei 8.541/1992, artigo 14, § 4°](https://www.planalto.gov.br/ccivil_03/leis/l8541.htm#:~:text=no%20Lucro%20Presumido-,Art.,na%20atividade%2C%20expressa%20em%20cruzeiros.).

A marcação **“Considera IRF na receita”** define se o valor do **Imposto de Renda Retido na Fonte (IRF)** presente na nota fiscal deve ser considerado no cálculo da receita para fins de apuração.

- **Quando a opção está marcada:**
  O valor do IRF será **somado** ao total da nota para compor a receita bruta.
  **Exemplo:**
  Nota fiscal com valor bruto de **R$ 50.000,00** e **R$ 750,00** de IR retido.
  Se o IR estiver deduzindo o valor da nota (ou seja, total da nota = R$ 49.250,00), ao marcar essa opção, o valor levado como receita será **R$ 50.000,00**.
- **Quando a opção está desmarcada:**
  O sistema considera o valor **deduzido do IR**, levando **R$ 49.250,00** como receita.

Essa configuração é útil em cenários onde a apuração da receita bruta precisa refletir o valor total original da nota, sem deduções de IRF.

Na aba **"Natureza de Receitas e Despesas"** cadastre as naturezas que originam as informações a serem consideradas na apuração para seu respectivo item de apuração.

![Imagem 8: Na aba "Natureza de Receitas e Despesas" cadastre as naturezas que originam as informações a serem consideradas na…](https://ajuda.sankhya.com.br/hc/article_attachments/18016918971287)

Na aba **"Filtros"**, ao acionar as marcações **"Financeiro"** e **"Notas"** será disponibilizado o botão ![Imagem 9: Na aba "Filtros" , ao acionar as marcações "Financeiro" e "Notas" será disponibilizado o botão "Filtros" , que permite…](https://ajuda.sankhya.com.br/hc/article_attachments/18044286893335) **"Filtros"**, que permite a criação de condições específicas que não estão contidas na regra geral da consulta. Desse modo, a condição estabelecida neste botão irá priorizar a regra geral da natureza.

![Imagem 10: Na aba "Filtros" , ao acionar as marcações "Financeiro" e "Notas" será disponibilizado o botão "Filtros" , que permite…](https://ajuda.sankhya.com.br/hc/article_attachments/18045476339095)

**(2)** Realize as configurações acima para as naturezas de IRPJ e CSLL e seus respectivos registros.

### Apuração do Regime Normal - Lucro Presumido

Com as configurações para apuração do Lucro Presumido realizadas, agora é necessário cadastrar a apuração. Para isso acesse a tela **"Apuração do Regime Normal - Lucro Presumido"**.

No painel principal informe os seguintes campos:

![Imagem 11: No painel principal informe os seguintes campos:](https://ajuda.sankhya.com.br/hc/article_attachments/18017124602007)

Busque no campo **"Empresa"** pela empresa matriz; caso haja filiais, estas já estarão contidas na consulta. Em sequência, informe no campo **"Referência"** o ano da referência que será apurada com 4 dígitos, como, por exemplo, 2022.
Caso esse formato não seja respeitado, o sistema irá informá-lo por meio da mensagem:

**"O ano-calendário a ser informado deverá conter 4 dígitos. Exemplo: 2022."**

Depois, selecione o **"Trimestre"** que será realizada a apuração.

Os campos **"Data Início"** e **"Data Fim"** serão preenchidos, conforme a Referência e o Trimestre informados.

Por fim, de acordo com as ações realizadas nesta tela, o campo **"Status Apuração"** será atualizado automaticamente.

Logo abaixo, você encontrará a marcação **"Lei Complementar 224/2025"**. Ao ativar este botão, o sistema passa a controlar automaticamente os novos limites de receita (trimestrais e anuais), os saldos e o recálculo do IRPJ e da CSLL exigidos por esta legislação, aplicando o acréscimo de 10% sobre os percentuais de presunção apenas na parcela excedente. Se mantido desativado, a apuração seguirá a regra antiga. Para entender mais, acesse o artigo: [Apuração do Lucro Presumido: Regras da Lei Complementar nº 224/2025](https://ajuda.sankhya.com.br/hc/pt-br/articles/39443027294999-Apura%C3%A7%C3%A3o-do-Lucro-Presumido-Regras-da-Lei-Complementar-n%C2%BA-224-2025).

Caso realize a reabertura de uma apuração por meio do botão ![Imagem 12: Caso realize a reabertura de uma apuração por meio do botão "Reabrir" o campo Status da Apuração será alterado…](https://ajuda.sankhya.com.br/hc/article_attachments/18046863589143) **"Reabrir"** o campo Status da Apuração será alterado automaticamente para **"Processado"** e irá manter os valores e os ajustes já processados.

Ao realizar novamente o processamento por meio do botão ![Imagem 13: Ao realizar novamente o processamento por meio do botão "Processar" , os valores e ajustes lançados manualmente serão…](https://ajuda.sankhya.com.br/hc/article_attachments/18022360478231) **"Processar"**, os valores e ajustes lançados manualmente serão sobrepostos e mantidos.

Ao salvar o cadastro da apuração, a aba **"Ajustes"** ficará disponível.

#### Aba Ajustes

Nessa aba, sub-aba **"Retenções"**, ao acionar o botão ![Imagem 14: Nessa aba, sub-aba "Retenções" , ao acionar o botão "Consultar" será apresentado o pop-up "Retenção para as Deduções"…](https://ajuda.sankhya.com.br/hc/article_attachments/18021890325271) **"Consultar"** será apresentado o pop-up **"Retenção para as Deduções"** onde é possível consultar as notas de saídas com impostos retidos para compor as deduções.

**Importante:** para retenções com origem de estoque, é fundamental que sejam gerados os livros fiscais e o status da nota como **"Aprovada"**.

![Imagem 15: Importante: para retenções com origem de estoque, é fundamental que sejam gerados os livros fiscais e o status da nota…](https://ajuda.sankhya.com.br/hc/article_attachments/18021784521239)

Neste pop-up pode-se filtrar todas as notas de saídas (origem Estoque) e financeiro (origem Financeiro) com impostos retidos IRPJ e/ou CSLL da Matriz e suas filiais, por meio dos campos:

- **Parceiro:** busque aqui por um parceiro específico.
- **Nro.Docto:** procure por meio deste campo pelo número do documento.
- **TOP:** selecione o [Tipo de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) para aplicar no filtro.
- **Tipo de Movimento:** defina o tipo de movimento dentre as opções **"Ambos"**, **"Financeiro"** ou **"Notas"**.
- **Tipo de Data:** neste campo defina o tipo de data de acordo com as opções **"Data de Ent/Saída"**, **"Data de Movimento"** ou **"Data de Negociação"**.

Com os campos acima preenchidos, clique em **"Aplicar Filtro"** para que os registros sejam apresentados.

Além disso, quando o Status Apuração estiver como Processado, pode-se efetivar os ajustes no pop-up Retenção para as Deduções. Porém, antes da confirmação, será emitida a mensagem:

**"Atenção! Referência já processada, ao editar informações de cadastro ou ajustes desta apuração o processamento atual será desconsiderado. Deseja continuar?"**

Ao clicar em **"Não"** o sistema irá ignorar a edição e manter a referência, além de não transferir os lançamentos para a aba Retenções, e irá manter o Status Apuração como Processado.

Quando optar-se por **"Sim"**, os valores já processados nas abas **"IRPJ"** e **"CSLL"** serão limpos e o campo Status Apuração será atualizado para **"Aberto"**.

![Imagem 16: Se efetivada uma primeira carga na consulta, ao efetuar novamente a pesquisa, as notas e os financeiros que foram…](https://ajuda.sankhya.com.br/hc/article_attachments/17678152534039) Se efetivada uma primeira carga na consulta, ao efetuar novamente a pesquisa, as notas e os financeiros que foram efetivados não serão apresentados, pois já estarão selecionados na sub-aba Retenções.

Na coluna **"Nro. Docto"** ao lado do número do documento tem-se o botão ![Imagem 17: Na coluna "Nro. Docto" ao lado do número do documento tem-se o botão "Lançador" ; ao acioná-lo o sistema abrirá a nota…](https://ajuda.sankhya.com.br/hc/article_attachments/17678110351255) **"Lançador"**; ao acioná-lo o sistema abrirá a nota na tela [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) e o financeiro na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753). 

Após a consulta dos registros, acione o botão ![Imagem 18: Após a consulta dos registros, acione o botão "Efetivar Ajustes Informados" , assim, serão consideradas todas as notas…](https://ajuda.sankhya.com.br/hc/article_attachments/18021956444311) **"Efetivar Ajustes Informados"**, assim, serão consideradas todas as notas e financeiros que estão listadas na grade, independente de estarem marcadas ou não. Além disso, as informações contidas no pop-up irão compor a sub-aba Retenções.

Agora, retorne a sub-aba Retenções e clique no botão ![Imagem 19: Agora, retorne a sub-aba Retenções e clique no botão "Considerar na Apuração" para que os dados contidos nos itens…](https://ajuda.sankhya.com.br/hc/article_attachments/18021975638295) **"Considerar na Apuração"** para que os dados contidos nos itens sejam carregados em seus respectivos registros nas apurações do IRPJ e CSLL.

Para desconsiderar a ação executada no botão Considerar na Apuração, basta acionar o botão **"Desconsiderar"**. Feito isso, será necessário efetuar uma nova consulta para reiniciar o processo.

Na sub-aba **"Ajustes Manuais"** pode-se cadastrar os ajustes necessários do item da apuração. 

![Imagem 20: Na sub-aba "Ajustes Manuais" pode-se cadastrar os ajustes necessários do item da apuração.](https://ajuda.sankhya.com.br/hc/article_attachments/18022162878359)

![Imagem 21: O valor do lançamento será inserido integralmente na linha indicada do item de apuração para o mês de seu lançamento,…](https://ajuda.sankhya.com.br/hc/article_attachments/17678152534039) O valor do lançamento será inserido integralmente na linha indicada do item de apuração para o mês de seu lançamento, assim o valor a ser considerado irá respeitar o sinal, sendo positivo ou negativo conforme necessidade.

Após a consulta, o aceite das retenções e os lançamentos de ajustes, se necessário, ao pressionar o botão ![Imagem 22: Após a consulta, o aceite das retenções e os lançamentos de ajustes, se necessário, ao pressionar o botão "Processar"…](https://ajuda.sankhya.com.br/hc/article_attachments/18022360478231) **"Processar"** será exibida uma mensagem de confirmação para a ação proposta:

**"Confirma a busca de informações para o preenchimento da apuração do lucro presumido da empresa X no período de DD/MM/AA a DD/MM/AA?"**

Clicando em **"Sim"**, os registros serão processados com sucesso.

![Imagem 23: Clicando em "Sim" , os registros serão processados com sucesso.](https://ajuda.sankhya.com.br/hc/article_attachments/18045243362327)

Além disso, as abas de **"IRPJ"** e **"CSLL"** ficarão disponíveis para consulta. 

#### Aba IRPJ

Os cálculos são executados na estrutura de cascata, assim inicia-se com o grupo:

![Imagem 24: Discriminação da Receita Bruta](https://ajuda.sankhya.com.br/hc/article_attachments/17679329658519) **Discriminação da Receita Bruta**

Nesse grupo serão considerados os Itens de Apuração determinados pela Receita, são eles:

![Imagem 25: Nesse grupo serão considerados os Itens de Apuração determinados pela Receita, são eles:](https://ajuda.sankhya.com.br/hc/article_attachments/18025246033687)

Tendo a possibilidade de origem em Notas e Financeiros, deverão ser configuradas as receitas correspondentes ao percentual a ser aplicado para cada atividade existente na empresa.

**Importante:** as vendas canceladas não irão compor a Receita Bruta e não serão consideradas nas deduções.

O cálculo é composto pela seguinte fórmula:

```
 (Vendas - Deduções) - (Devoluções + Deduções) + ((Financeiro (R)- Deduções) - (Financeiro
(D) + Deduções)) * Alíquota = Vlr X (+/-) Ajustes manuais
```

Respeitando os sinais:

- **Receita**: valor positivo;
- **Despesa**: valor negativo.

Encontra-se o total da Base de Cálculo Ajustada.

![Imagem 26: As deduções serão consideradas no cálculo somente se as marcações localizadas no painel principal da tela…](https://ajuda.sankhya.com.br/hc/article_attachments/17678152534039) As deduções serão consideradas no cálculo somente se as marcações localizadas no painel principal da tela **"Configurações para apuração do Lucro Presumido"** estiverem configuradas. 

**![Imagem 27: Receita com Tributação Integral](https://ajuda.sankhya.com.br/hc/article_attachments/17679585815191) Receita com Tributação Integral**

![Imagem 28: Receita com Tributação Integral](https://ajuda.sankhya.com.br/hc/article_attachments/18027800747799)

Caso exista a possibilidade de origem Financeira, deverão ser configuradas as naturezas de receitas e despesas correspondentes a cada registro que será calculado.

O cálculo é composto pela seguinte fórmula:

```
 Mov. Financeira [Receita - Despesa] * Alíquota = Vlr X (+/-) Ajustes manuais
```

Onde parte do valor obtido da Base de Cálculo Ajustada somado ao valor encontrado nas Receitas com Tributação Integral resulta na Base de Cálculo para o Lucro Presumido.

A alíquota em regra geral representa 100% do valor registrado.

![Imagem 29: Quaisquer benefícios que a empresa possua podem ser ajustados diretamente no campo "Alíquota" da tela de "Itens de…](https://ajuda.sankhya.com.br/hc/article_attachments/17676978711959) Quaisquer benefícios que a empresa possua podem ser ajustados diretamente no campo **"Alíquota"** da tela de **"Itens de Apuração"**.

**![Imagem 30: Cálculo para IRPJ](https://ajuda.sankhya.com.br/hc/article_attachments/17679585818391) Cálculo para IRPJ**

![Imagem 31: Cálculo para IRPJ](https://ajuda.sankhya.com.br/hc/article_attachments/18028029657751)

Corresponde ao cálculo efetivamente do imposto, onde a partir do valor obtido pela Base de Cálculo para o Lucro Presumido serão aplicados os registros:

- Alíquota de 15%= 15% sobre o valor total encontrado;
- Adicional IRPJ = 10% da parcela excedente aos 60.000,00 ao trimestre;

**Observação:** para que a regra seja devidamente aplicada, os registros mensais não serão lançados em seu respectivo mês, sendo feito um registro único apenas na coluna de totais.

"Valor do adicional do imposto de renda, determinado mediante a aplicação da alíquota de 10% (dez por cento), sobre a parcela da base de cálculo que exceder o valor resultante da multiplicação de R$ 20.000,00 (vinte mil reais) pelo número de meses do respectivo período de apuração." (art. 3º da Lei nº 9.249,1995)

- Diferença de IRPJ: em decorrência da mudança de coeficiente sobre a Receita Bruta, este é um registro específico para lançamentos manuais, conforme requisito particular estabelecido nas orientações da ECF abaixo:

"A pessoa jurídica exclusivamente prestadora de serviços que utilizou o percentual favorecido de 16% (dezesseis por cento) para apuração da base de cálculo do imposto e cuja receita bruta acumulada até o trimestre tenha ultrapassado a R$ 120.000,00 (cento e vinte mil reais) deverá informar, nesta linha, no trimestre em que exceder o limite, a diferença do imposto de renda determinada com a aplicação do percentual de 32% (trinta e dois por cento) sobre a receita bruta de cada trimestre transcorrido.

Atenção: as pessoas jurídicas prestadoras de serviços de profissão legalmente regulamentada estão sempre sujeitas à aplicação do percentual de 32% para determinação da base de cálculo do imposto."

**![Imagem 32: Deduções](https://ajuda.sankhya.com.br/hc/article_attachments/17679695294103) Deduções**

Conforme artigo 10 da Lei 9.532/1997**:**

"Poderá deduzir do imposto devido no período de apuração, o imposto pago ou retido na fonte sobre as receitas que integram a base de cálculo, bem como o imposto de renda pago indevidamente em períodos anteriores." 

![Imagem 33: "Poderá deduzir do imposto devido no período de apuração, o imposto pago ou retido na fonte sobre as receitas que…](https://ajuda.sankhya.com.br/hc/article_attachments/18028151119511)

Tendo a possibilidade de origem Financeiro, deverão ser configuradas as naturezas de Despesas correspondentes a cada registro que será calculado. Exceto para as retenções, pois estas serão selecionadas diretamente na sub-aba **"Retenções"**.

O cálculo é composto pela seguinte fórmula:

```
 Mov. Financeira [Despesa] * Alíquota = Vlr X (+/- Ajustes Manuais)
```

Serão consideradas as informações da aba **"Ajustes"**, sub-aba **"Retenções"** onde obedecerá o seguinte critério para alocação nos registros corretos:

- IR Retido na Fonte;
- Imposto de Renda Retido na Fonte por Órgãos, Autarquias e Fundações Federais (Lei nº 9.430/1996, art. 64);
- Imposto de Renda Retido na Fonte pelas Demais Entidades da Administração Pública Federal (Lei n° 10.833/2003, art. 34).

O cálculo parte do valor encontrado do IRPJ apurado antes das Deduções subtraindo os valores encontrados no grupo de Deduções, resultando no IRPJ apurado a pagar.

#### Aba CSLL

Os cálculos são executados na estrutura de cascata, assim inicia-se com o grupo:

**![Imagem 34: Discriminação da Receita Bruta](https://ajuda.sankhya.com.br/hc/article_attachments/17679329658519) Discriminação da Receita Bruta**

Nesse grupo serão considerados os Itens de Apuração determinados pela Receita, são eles: 

![Imagem 35: Nesse grupo serão considerados os Itens de Apuração determinados pela Receita, são eles:](https://ajuda.sankhya.com.br/hc/article_attachments/18028316307223)

Caso haja a possibilidade de origem em Notas e Financeiro, deverão ser configuradas as receitas correspondentes ao percentual a ser aplicado para cada atividade existente na empresa.

O cálculo é composto pela seguinte fórmula: 

```
 (Vendas - Deduções) - (Devoluções - Deduções) + ((Financeiro (R)- Deduções) -
(Financeiro (D) - Deduções)) * Alíquota = Vlr X (+/-) Ajustes manuais
```

Respeitando os sinais:

- **Receita:** valor positivo;
- **Despesa**: valor negativo.

Encontra-se o total da Base de Cálculo Ajustada.

![Imagem 36: As deduções serão consideradas no cálculo somente se as marcações localizadas no painel principal da tela…](https://ajuda.sankhya.com.br/hc/article_attachments/17678152534039) As deduções serão consideradas no cálculo somente se as marcações localizadas no painel principal da tela **"Configurações para apuração do Lucro Presumido"** estiverem configuradas. 

**![Imagem 37: Receita com Tributação Integral](https://ajuda.sankhya.com.br/hc/article_attachments/17679585815191) Receita com Tributação Integral**

![Imagem 38: Receita com Tributação Integral](https://ajuda.sankhya.com.br/hc/article_attachments/18046521527063)

É importante ressaltar que os itens de característica redutora desse grupo, só serão considerados para redução se lançados na forma de Despesa no financeiro, e para o lançamento manual com sinal negativo.

Tendo a possibilidade de origem Financeiro, deverão ser configuradas as naturezas de receitas e despesas correspondentes a cada registro que será calculado.

O cálculo é composto pela seguinte fórmula:

```
 Mov. Financeira [Receita - Despesa] * Alíquota = Vlr X (+/-) Ajustes manuais
```

Onde parte do valor obtido da Base de Cálculo Ajustada somado aos valores encontrados nas Receitas com Tributação Integral resulta na Base de Cálculo para o Lucro Presumido.

A alíquota em regra geral representa 100% do valor registrado.

![Imagem 39: Quaisquer benefícios que a empresa possua podem ser ajustados diretamente no campo "Alíquota" da tela de "Itens de…](https://ajuda.sankhya.com.br/hc/article_attachments/17676978711959) Quaisquer benefícios que a empresa possua podem ser ajustados diretamente no campo **"Alíquota"** da tela de**"Itens de Apuração"**.

**![Imagem 40: Cálculo para CSLL](https://ajuda.sankhya.com.br/hc/article_attachments/17679585818391) Cálculo para CSLL**

![Imagem 41: Cálculo para CSLL](https://ajuda.sankhya.com.br/hc/article_attachments/18046543765911)

Corresponde ao cálculo efetivamente do imposto, onde a partir do valor encontrado pela Base de Cálculo para o Lucro Presumido serão aplicados nos registros:

- Alíquota de 9% = 9% sobre o valor total encontrado;
- Diferença de CSLL: em decorrência da mudança de coeficiente sobre a Receita Bruta, este é um registro específico para lançamentos manuais, conforme requisito particular estabelecido nas orientações da ECF abaixo:

“A pessoa jurídica que deixar de ser tributada com base no lucro real deverá informar nesta linha os créditos aproveitados anteriormente. Essa adição deve ser feita no primeiro período de apuração do novo regime de tributação (presumido ou arbitrado).”  

**![Imagem 42: Deduções](https://ajuda.sankhya.com.br/hc/article_attachments/17679695294103) Deduções**

Conforme artigo 10 da Lei 9.532/1997:

"Poderá deduzir do imposto devido no período de apuração, o imposto pago ou retido na fonte sobre as receitas que integram a base de cálculo, bem como o imposto de renda pago indevidamente em períodos anteriores."

![Imagem 43: "Poderá deduzir do imposto devido no período de apuração, o imposto pago ou retido na fonte sobre as receitas que…](https://ajuda.sankhya.com.br/hc/article_attachments/18046633054231)

**Importante:** o registro **"(-) CSLL Retida na Fonte por Órgãos, Autarquias e Fundações dos Estados, Distrito Federal e Municípios (Lei n° 10.833/2003, art. 33)"** é exclusivo para lançamentos manuais.

Tendo a possibilidade de origem Financeiro, deverão ser configuradas as naturezas de Despesas correspondentes a cada registro que será calculado. Exceto para as retenções, pois estas serão selecionadas diretamente na sub-aba **"Retenções"**.

O cálculo é composto pela seguinte fórmula:

```
 Mov. Financeira [Despesa] * Alíquota = Vlr X (+/- Ajustes Manuais)
```

Serão consideradas as informações da aba **"Ajustes"**, sub-aba **"Retenções"** onde obedecerá ao seguinte critério para alocação nos registros corretos:

- CSLL Retida na Fonte por Pessoas Jurídicas de Direito Privado (Lei n° 10.833/2003, art. 30);
- CSLL Retida na fonte por Órgãos Públicos (Lei 9.430/1996 art 64);
- CSLL Retida na Fonte pelas Demais Entidades da Administração Pública Federal (Lei n° 10.833/2003, art. 34).

O cálculo parte do valor encontrado da CSLL apurado antes das deduções subtraindo os valores encontrados no grupo de Deduções resultando no CSLL apurado a pagar.

---

![Imagem 44: Com a apuração finalizada, feche o registro por meio do botão "Fechar" . Ao acioná-lo será apresentada a mensagem:](https://ajuda.sankhya.com.br/hc/article_attachments/17677351131159) Com a apuração finalizada, feche o registro por meio do botão ![Imagem 45: Com a apuração finalizada, feche o registro por meio do botão "Fechar" . Ao acioná-lo será apresentada a mensagem:](https://ajuda.sankhya.com.br/hc/article_attachments/18046801766423) **"Fechar"**. Ao acioná-lo será apresentada a mensagem:

**"Deseja efetuar o fechamento deste trimestre?"**

Ao clicar em **"Sim"** o registro será fechado e a edição do mesmo não será mais permitida. Além disso, o **"Status Apuração"** será alterado para **"Fechado"**, sinalizando que a apuração foi validada e registrada para o trimestre.

**Importante:** essa ação não trava nenhuma edição dos movimentos de notas e financeiros considerados nesta apuração. Para isso utilize a rotina de [Fechamento Contábil/Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595654-Configura%C3%A7%C3%A3o-Fechamento-Cont%C3%A1bil-Fiscal).

Se for necessário fazer um ajuste específico ou recalcular a apuração, pode-se clicar no botão ![Imagem 46: Se for necessário fazer um ajuste específico ou recalcular a apuração, pode-se clicar no botão "Reabrir" . Porém, todos…](https://ajuda.sankhya.com.br/hc/article_attachments/18046863589143) **"Reabrir"**. Porém, todos os dados serão descartados e a apuração precisará ser refeita.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/17676609771415-Apura%C3%A7%C3%A3o-do-Regime-Normal-Lucro-Presumido#top)
