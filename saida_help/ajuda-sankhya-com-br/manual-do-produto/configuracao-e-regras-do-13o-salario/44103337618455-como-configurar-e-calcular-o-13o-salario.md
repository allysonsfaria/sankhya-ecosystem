---
id: "44103337618455"
titulo: "Como configurar e calcular o 13º salário durante a licença-maternidade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44103337618455-Como-configurar-e-calcular-o-13%C2%BA-sal%C3%A1rio-durante-a-licen%C3%A7a-maternidade"
trilha: "Manual do Produto > Pessoas+ > 13º Salário > Configuração e Regras do 13º Salário"
atualizado_em: "2026-10-09T17:28:04Z"
rotulos: ["Ocorrências", "FGTS", "Código de Afastamento", "Licença-Maternidade", "Licença Maternidade Cidadã", "13º salário - licença-maternidade", "Identificação 117 - Evento Salário Maternidade", "Identificação 118 - Evento Salário Maternidade 13° Salário"]
---

# Como configurar e calcular o 13º salário durante a licença-maternidade

### O que é e para que serve

Durante a **licença-maternidade**, o Pessoas+ separa o cálculo do 13º salário referente ao período de licença dos demais avos devidos pela empresa.

Para que essa separação seja feita corretamente, é necessário configurar o **código de afastamento**, a **ocorrência de licença-maternidade** e a **identificação dos eventos** utilizados no cálculo.

| ℹ️ **Nota**  As configurações descritas neste artigo determinam como o Pessoas+ direciona os valores do 13º salário relacionados à licença-maternidade para os eventos específicos de salário-maternidade. |
| --- |

Quando uma colaboradora permanece afastada por licença-maternidade durante o período de apuração do 13º salário, o Pessoas+ considera os avos correspondentes ao período de licença e os demonstra em eventos específicos de **13º salário - licença-maternidade**.

Dessa forma, o direito ao 13º salário da colaboradora não é eliminado. O sistema apenas **separa os avos correspondentes ao período de licença-maternidade dos demais avos**, direcionando-os para os eventos específicos.

Para que esse tratamento ocorra, é necessário que:

- O afastamento de licença-maternidade esteja vinculado a um código de afastamento do tipo **FGTS**.

  Nesse código, a opção **Direito ao décimo terceiro** esteja desmarcada.
- A ocorrência de licença-maternidade esteja vinculada ao código de afastamento correto.
- Os eventos utilizados no cálculo do salário-maternidade e do 13º salário durante a licença estejam devidamente identificados.

### Antes de começar

Verifique se você possui:

- Acesso às telas **Ocorrências** (Pessoal+ > Rotinas Folha), **Código de Afastamento** (Pessoal+ > Cadastros) e **Eventos** (Pessoal+ > Cadastros). O administrador libera esse acesso na tela **Acessos** (Configurações > Controle de Acesso).
- Um **código de afastamento** cadastrado com **Tipo de tabela FGTS** para a licença-maternidade.
- A licença lançada para a colaboradora na aba **Lançamento** da tela **Ocorrências**.

### Jornada de uso

#### 1. Configure os códigos de afastamento

Na tela **Código de Afastamento** (Pessoal+ > Cadastros), verifique os códigos de afastamento utilizados pela ocorrência de licença-maternidade.

Na configuração da licença-maternidade, podem ser utilizados códigos relacionados a diferentes tabelas de afastamento. Para o tratamento do 13º salário, é importante identificar o código correspondente à **tabela FGTS**.

- **Código da tabela FGTS**

  ![Imagem 1: Código da tabela FGTS](https://ajuda.sankhya.com.br/hc/article_attachments/44126238749975)

  Localize o código de afastamento utilizado para a licença-maternidade correspondente ao **Tipo de tabela FGTS** e verifique o campo **Direito ao décimo terceiro**.

  Para que os avos referentes ao período de licença sejam direcionados aos eventos específicos de salário-maternidade, **desmarque esse campo**.

  Essa configuração faz com que o período de licença não seja considerado novamente no cálculo dos eventos normais de 13º salário da empresa.

  | **⚠️ Atenção**  Desmarcar **Direito ao décimo terceiro** não significa retirar o direito da colaboradora ao 13º salário. O tratamento do Pessoas+ direciona os avos correspondentes ao período de licença para os eventos específicos de 13º salário da licença-maternidade. |
  | --- |
- **Código da tabela Causa**

  ![Imagem 2: Código da tabela Causa](https://ajuda.sankhya.com.br/hc/article_attachments/44126238751511)

  O código relacionado ao **Tipo de tabela Causa** **do afastamento** também pode estar vinculado à ocorrência, mas a configuração do campo **Direito ao décimo terceiro** desse código não é a responsável pelo tratamento dos avos de 13º salário.

  Para esse cálculo, considere a configuração do código relacionado à **tabela FGTS**.

#### 2. Configure a ocorrência

Depois de conferir o código de afastamento, verifique a ocorrência utilizada para lançar a licença-maternidade.

1. Na tela **Ocorrências** (Pessoal+ > Rotinas Folha), aba **Cadastro**.

   ![Imagem 3: Na tela Ocorrências (Pessoal+ > Rotinas Folha), aba Cadastro .](https://ajuda.sankhya.com.br/hc/article_attachments/44126457174935)
2. Localize a ocorrência correspondente à licença-maternidade e confira suas configurações.

   | **Campo** | **Configuração** |
   | --- | --- |
   | Tipo de Afastamento | **Licença maternidade** ou **Licença Maternidade Cidadã**, conforme o caso. |
   | Descrição FGTS | Código de afastamento da tabela FGTS configurado anteriormente. |
   | Descrição eSocial | Código correspondente ao motivo de afastamento utilizado no eSocial. |
   | Descrição Causa | Código correspondente à causa do afastamento. |

   No campo **Descrição FGTS**, serão apresentados os códigos disponíveis na tabela correspondente ao FGTS.
3. Após conferir, se fizer alguma alteração, clique em **Confirmar alterações**.

| ℹ️ **Nota**  A ocorrência vincula o lançamento da licença-maternidade aos códigos de afastamento utilizados pelo sistema. Por isso, além de conferir o código isoladamente, valide se a ocorrência está apontando para o código correto. |
| --- |

#### 3. Lance a licença-maternidade da colaboradora

Registre o afastamento da colaboradora na tela **Ocorrências** (Pessoal+ > Rotinas Folha), aba **Lançamento**.

📚 Veja o passo a passo completo em [Como lançar a ocorrência de licença-maternidade para uma funcionária](https://ajuda.sankhya.com.br/hc/pt-br/articles/43877669306007).

| **⚠️ Atenção**  Alterações nas datas do afastamento depois de o 13º salário já ter sido calculado podem alterar a quantidade de avos. Nesse cenário, realize novamente o cálculo do 13º para que o resultado considere o período atualizado. |
| --- |

#### 4. Configure a identificação dos eventos de licença-maternidade

No cadastro de **Eventos** (Pessoal+ > Cadastros), confira na aba **Básico** o campo **Identificação** dos eventos de licença-maternidade.

Essa identificação permite que o Pessoas+ reconheça quais valores correspondem ao salário-maternidade e quais correspondem ao 13º salário relacionado à licença.

As descrições dos eventos podem variar de uma base para outra. Por isso, utilize o **código do evento** como referência na conferência.

- **Identificação 117 - Evento Salário Maternidade**

  Configure essa identificação nos seguintes eventos:

  | **Evento** | **Descrição** | **Identificação** |
  | --- | --- | --- |
  | 540 | Licença maternidade | 117 - Evento Salário Maternidade |
  | 541 | Médias licença maternidade | 117 - Evento Salário Maternidade |
- **Identificação 118 - Evento Salário Maternidade 13° Salário**

  Configure essa identificação nos seguintes eventos:

  | **Evento** | **Descrição** | **Identificação** |
  | --- | --- | --- |
  | 308 | 1 Parc 13 Sal-Lic Maternidade | 118 - Evento Salário Maternidade 13° Salário |
  | 309 | 2 Parc 13 Sal-Lic Maternidade | 118 - Evento Salário Maternidade 13° Salário |
  | 313 | 1 Parc Médias 13 Sal-Lic Maternidade | 118 - Evento Salário Maternidade 13° Salário |
  | 314 | 2 Parc Médias 13 Sal-Lic Maternidade | 118 - Evento Salário Maternidade 13° Salário |
  | 221 | 13 Sal Prop - Lic Maternidade | 118 - Evento Salário Maternidade 13° Salário |
  | 229 | Médias 13 Sal Prop - Lic Maternidade | 118 - Evento Salário Maternidade 13° Salário |

  A identificação não altera, por si só, o valor apresentado no holerite. Ela permite ao sistema reconhecer a natureza dos eventos de salário-maternidade e do 13º salário relacionado à licença para os tratamentos correspondentes nas rotinas de folha e obrigações.

Quando a empresa participa do **Programa Empresa Cidadã**, utilize as identificações específicas para os eventos correspondentes:

- **132 - Evento Salário Maternidade Cidadã**;
- **133 - Evento Salário Maternidade 13° Cidadã**.

Confira os eventos utilizados na sua configuração antes de realizar o cálculo. Para o tratamento da licença-maternidade cidadã, também é necessário conferir o tipo de afastamento configurado na ocorrência.

#### 5. Calcule o 13º salário

Depois de concluir as configurações, realize o cálculo do 13º normalmente.

O procedimento pode ser realizado para:

- **1ª parcela**;
- **2ª parcela**;
- **13º na rescisão**.

Durante o cálculo, o Pessoas+ identifica os avos correspondentes ao período de licença-maternidade e direciona os valores para os eventos específicos configurados para esse tratamento.

| ℹ️ **Nota**  Se a configuração do afastamento ou dos eventos for alterada depois que o 13º já tiver sido calculado, realize o cálculo novamente para que as alterações sejam consideradas. |
| --- |

#### 6. Entenda como o Pessoas+ calcula os avos da licença-maternidade

O Pessoas+ calcula o **13º salário referente ao período de licença por avos**, considerando a quantidade mínima de dias de licença exigida para que cada mês seja considerado um avo.

O cálculo do valor integral correspondente ao período de licença pode ser representado pela fórmula:

**13º da licença = (Salário ÷ 12) × avos de licença no ano**

Considere as seguintes informações:

- **Salário:** salário contratual da colaboradora, somado às incorporações. As médias de valores variáveis são calculadas em eventos específicos.
- **Avos de licença:** quantidade de avos correspondente aos meses em que a licença atende ao mínimo de dias exigido pelo sistema. A contagem considera o período do ano de referência, desde 1º de janeiro ou do início da licença até 31 de dezembro. Na rescisão, a contagem considera o período até a data do desligamento.
- **Licença sem Data de término:** o sistema utiliza a **Data de retorno prevista** para determinar a duração da licença. Quando essa data não é informada, considera **120 dias** a partir da **Data de Início**.

**Quando o mês conta como avo de licença**

O mínimo de dias necessário para que o mês seja considerado um avo depende do **Tipo de afastamento** configurado na ocorrência e do tipo de mês utilizado no cálculo.

| **Tipo de afastamento** | **Regra** | **Mês de 30 dias** | **Mês de 31 dias** |
| --- | --- | --- | --- |
| Licença maternidade | Dias trabalhados no mês iguais ou menores que 15 | 15 dias ou mais de licença | 16 dias ou mais de licença |
| Licença Maternidade Cidadã | Dias trabalhados no mês menores que 15 | 16 dias ou mais de licença | 17 dias ou mais de licença |

| ℹ️ **Nota**  Com **mês comercial**, que é o padrão, todos os meses são considerados com 30 dias. Com **mês real**, o sistema considera a quantidade de dias do calendário de cada mês. |
| --- |

Quando o período de licença não atinge o mínimo de dias necessário para gerar o avo, esse avo permanece no **13º salário pago pela empresa**, nos eventos normais de 13º.

Portanto, não considere apenas a quantidade de dias de licença de forma isolada: confira o tipo de afastamento e o tipo de mês utilizado no cálculo.

**Eventos de 13º da licença**

Os principais eventos utilizados pelo Pessoas+ para o 13º relacionado à licença-maternidade são:

| Evento padrão | Quando é calculado | Valor | Compõe base de INSS do 13º |
| --- | --- | --- | --- |
| 308 - 1 Parc 13 Sal-Lic Maternidade | 1ª parcela | (Salário ÷ 12 × avos) ÷ 2 | Não |
| 309 - 2 Parc 13 Sal-Lic Maternidade | 2ª parcela | Salário ÷ 12 × avos | Sim |
| 321 - Desc 1 Parc 13 Sal-Lic Mater | 2ª parcela | Deduz os valores pagos na 1ª parcela pelos eventos 308 e 313 | Não |
| 221 - 13 Sal Prop - Lic Maternidade | Rescisão | Salário ÷ 12 × avos | Sim |
| 313 - 1 Parc Médias 13 Sal-Lic Maternidade | 1ª parcela | Médias de variáveis proporcionais aos avos | Não |
| 314 - 2 Parc Médias 13 Sal-Lic Maternidade | 2ª parcela | Médias de variáveis proporcionais aos avos | Sim |
| 229 - Médias 13 Sal Prop - Lic Maternidade | Rescisão | Médias de variáveis proporcionais aos avos | Sim |

| ℹ️ **Nota**  Na segunda parcela, o evento **321** deduz os valores pagos na primeira parcela pelos eventos **308** e **313**, conforme os valores gerados no cálculo. Quando não há médias de variáveis, o desconto corresponde ao valor pago pelo evento 308.  Na **Empresa Cidadã**, os eventos **330** a **334** seguem o tratamento específico dessa modalidade, utilizando o tipo de afastamento **Licença Maternidade Cidadã**. A regra de contagem de avos é diferente da utilizada para **Licença maternidade** e deve ser conferida conforme a tabela apresentada anteriormente. |
| --- |

**🔹Exemplo de cálculo**

Considere uma colaboradora com:

- **Salário:** R$ 2.009,85;
- **Início da licença-maternidade:** 18/10/2025;
- **Data de término:** não informada;
- **1ª parcela do 13º:** calculada em novembro/2025.

Nesse cenário, a quantidade de avos de licença é determinada conforme o período de afastamento e a configuração do tipo de mês utilizada no cálculo.

| **Mês** | **Dias de licença no mês** | **Avo de licença** |
| --- | --- | --- |
| Outubro | 13 ou 14 dias, conforme o tipo de mês da empresa | Não conta, pois está abaixo do mínimo exigido para esse exemplo |
| Novembro | Mês inteiro, considerando o período da licença | 1 |
| Dezembro | Mês inteiro, considerando a projeção da licença | 1 |

Assim, o exemplo considera **2 avos de licença**.

**1ª parcela**

O valor correspondente aos dois avos de licença é calculado proporcionalmente e, na primeira parcela, corresponde à metade desse valor:

**R$ 2.009,85 ÷ 12 × 2 ÷ 2 = R$ 167,49**

Assim, o evento **308** apresenta **R$ 167,49**.

**2ª parcela**

Na segunda parcela, é apurado o valor integral correspondente aos dois avos.

O cálculo matemático antes do tratamento das casas decimais é:

**R$ 2.009,85 ÷ 12 × 2 = R$ 334,975**

No exemplo, o valor apresentado para o evento **309** deve ser confirmado conforme a regra de arredondamento aplicada nas **Regras de Cálculo** do Pessoas+.

Para conferir o resultado, consulte essa configuração e compare o valor calculado com o valor apresentado pelo evento 309.

| **Evento** | **Cálculo** | **Valor** |
| --- | --- | --- |
| 308 - 1ª parcela, 11/2024 | 2.009,85 ÷ 12 × 2 ÷ 2 | R$ 167,49 |
| 309 - 2ª parcela, 12/2024 | 2.009,85 ÷ 12 × 2 (ex: tratamento das casas decimais = arredondar para maior nas Regras de Cálculo) | R$ 334,98 |
| 321 - Desconto da 1ª parcela, 12/2024 | Dedução do valor pago pelo evento 308 | R$ 167,49, neste exemplo sem médias variáveis |

| **⚠️ Atenção**  Os valores apresentados nos eventos podem variar conforme a regra de arredondamento configurada na tela **Regras de Cálculo do Produto**. Ao conferir uma diferença de centavos, verifique essa configuração antes de concluir que o cálculo está incorreto. |
| --- |

Os outros **dez avos**, correspondentes aos meses que não foram considerados como avos de licença, permanecem no cálculo normal do 13º salário da empresa.

| 💡 **Dica**  Ao conferir o cálculo, analise primeiro a quantidade de avos de licença. Depois, confira se esses avos foram direcionados aos eventos específicos de licença e se os demais avos permaneceram nos eventos normais de 13º. |
| --- |

**Demais avos**

Os avos que não correspondem ao período de licença-maternidade permanecem no cálculo normal do 13º salário da empresa.

Nesse exemplo, o sistema separa:

- os **2 avos correspondentes à licença-maternidade**, tratados pelos eventos específicos;
- os **demais avos**, tratados pelos eventos normais do 13º salário.

O objetivo é evitar que o mesmo período seja considerado duas vezes.

**🔹Exemplo de cálculo com o mês de início gerando avo**

Considere uma colaboradora com as seguintes informações:

- **Salário:** R$ 3.000,00;
- **Início da licença-maternidade:** 16/09/2026;
- **Data de término:** não informada;
- **Data final prevista da ocorrência:** 14/01/2027, considerando 120 dias;
- **1ª parcela do 13º:** calculada em novembro/2026;
- **Tipo de afastamento:** Licença maternidade.

Nesse cenário, setembro possui **15 dias de licença**, de 16 a 30/09. Para o tipo de afastamento e a regra de mês considerados neste exemplo, setembro gera 1 avo. Outubro, novembro e dezembro também geram 1 avo cada.

Dessa forma, são considerados **4 avos de licença-maternidade**. Os outros **8 avos**, correspondentes a janeiro a agosto, permanecem nos eventos normais do 13º salário.

**1ª parcela**

**R$ 3.000,00 ÷ 12 × 4 ÷ 2 = R$ 500,00**

O evento **308** apresenta R$ 500,00, e o evento normal de 1ª parcela do 13º apresenta R$ 1.000,00, correspondentes aos outros 8 avos.

**2ª parcela**

**R$ 3.000,00 ÷ 12 × 4 = R$ 1.000,00**

O evento **309** apresenta o valor correspondente aos quatro avos de licença, considerando a regra de arredondamento configurada no produto.

O evento **321** desconta os R$ 500,00 já pagos na primeira parcela pelos eventos correspondentes.

| ℹ️ **Nota**  Os exemplos consideram o tipo de afastamento indicado e as condições de cálculo descritas. Se a ocorrência estiver configurada como **Licença Maternidade Cidadã**, ou se o tipo de mês utilizado for diferente, confira a regra de contagem de avos antes de comparar os resultados. |
| --- |

#### 7. Confira o resultado do cálculo

Depois de calcular o 13º, confira os eventos gerados para a colaboradora.

Verifique principalmente:

1. Quantos avos foram considerados para o período de licença-maternidade.
2. Se os avos correspondentes à licença foram direcionados aos eventos específicos.
3. Se os demais avos permaneceram nos eventos normais de 13º salário.
4. Se a primeira parcela foi considerada na apuração da segunda parcela.
5. Se os eventos de médias foram gerados quando aplicáveis.
6. Se os eventos estão com as identificações de licença-maternidade configuradas corretamente.
7. Se os valores apresentados estão de acordo com a regra de arredondamento configurada na tela **Regras de Cálculo do Produto**.

Essa conferência é especialmente importante quando a configuração foi alterada após um cálculo anterior.

### Pontos de Atenção

- **O código de afastamento precisa estar corretamente configurado**

  A configuração do campo **Direito ao décimo terceiro** deve ser conferida no código da **tabela FGTS** utilizado pela ocorrência.

  A configuração de um código de outra tabela não substitui essa validação.
- **Evite a duplicidade de avos**

  Se o código FGTS utilizado pela licença-maternidade estiver com **Direito ao décimo terceiro** marcado, o período de licença poderá permanecer no cálculo normal do 13º da empresa, enquanto os eventos específicos de licença também poderão considerar o mesmo período.

  Nesse cenário, os avos podem ser considerados de forma duplicada.

  Para corrigir a configuração:

  1. desmarque **Direito ao décimo terceiro** no código FGTS utilizado pela licença;
  2. confirme a ocorrência;
  3. confira os eventos;
  4. realize novamente o cálculo do 13º.
- **Confira também a ocorrência da Empresa Cidadã**

  Quando a empresa participa do Programa Empresa Cidadã, a mesma conferência vale para a ocorrência de **Licença maternidade cidadã**.

  Verifique se o código informado no campo **Descrição FGTS** dessa ocorrência também está com **Direito ao décimo terceiro** desmarcado. Caso contrário, os avos da prorrogação podem ser considerados tanto nos eventos normais do 13º quanto nos eventos específicos da Empresa Cidadã.
- **Confira o mês de início da licença**

  O mês de início da licença deve ser analisado de acordo com:

  - a quantidade de dias de afastamento no mês;
  - o **Tipo de Afastamento** configurado na ocorrência;
  - o tipo de mês utilizado no cálculo: comercial ou real.

  Não utilize uma regra única de quantidade de dias para todos os tipos de afastamento.
- **Confira o período da licença**

  A data de término ou a previsão de retorno influencia o período considerado pelo sistema.

  Por isso, se o resultado apresentar quantidade de avos diferente da esperada, confira primeiro as datas cadastradas no afastamento.
- **Eventos de médias**

  As médias relacionadas ao 13º da licença são demonstradas nos eventos específicos de médias.

  Confira se os eventos **313, 314 e 229**, conforme a situação, estão corretamente identificados.
- **Incidência de INSS**

  A incidência deve ser conferida de acordo com o evento e a parcela do 13º:

  - evento **308**: não possui incidência de INSS;
  - evento **309**: possui incidência de INSS;
  - evento **221**: possui incidência de INSS;
  - evento **313**: não possui incidência de INSS;
  - eventos **314** e **229**: possuem incidência de INSS.
- **Diferenças de centavos no cálculo**

  Quando o valor calculado apresentar diferença de centavos em relação ao resultado esperado, confira a regra de arredondamento configurada na tela **Regras de Cálculo do Produto**.

  A regra configurada nessa tela influencia o valor apresentado pelo cálculo. Por isso, utilize a configuração do produto para analisar diferenças de arredondamento, em vez de considerar automaticamente que o resultado está incorreto.
- **Alterações depois do cálculo**

  Se qualquer uma das configurações for alterada depois que o 13º já tiver sido calculado, realize o cálculo novamente.

  Isso se aplica, por exemplo, a alterações:

  - no código de afastamento;
  - na ocorrência;
  - nas datas da licença;
  - na identificação dos eventos;
  - na configuração dos eventos utilizados no cálculo.

### Dicas de Usabilidade

Antes de calcular o 13º, faça uma conferência rápida:

**Código de afastamento → Ocorrência → Lançamento da licença → Identificação dos eventos → Cálculo do 13º**

Essa sequência ajuda a identificar inconsistências antes do processamento.

Após o cálculo, confira os eventos gerados para confirmar que:

- os avos da licença foram separados corretamente;
- os demais avos permaneceram no cálculo normal;
- não houve duplicidade;
- os eventos de médias foram considerados quando aplicáveis.

| 💡 **Dica**  Quando estiver analisando uma diferença no valor do 13º de uma colaboradora afastada, compare primeiro a quantidade de avos e os eventos gerados. Essa conferência normalmente permite identificar se a diferença está relacionada ao período de licença, às médias ou à configuração do afastamento. |
| --- |

### Perguntas Frequentes

**1. O 13º salário durante a licença-maternidade é calculado por dias?**

Não. No tratamento realizado pelo Pessoas+, o cálculo é feito por **avos**.

Para determinar o avo relacionado à licença, o sistema considera a quantidade de dias de afastamento no mês. Quando a licença alcança **15 dias ou mais no mês**, o período é considerado um avo de licença.

**2. A colaboradora perde o 13º salário referente ao período de licença-maternidade?**

Não. O tratamento realizado pelo Pessoas+ separa os avos correspondentes ao período de licença dos demais avos do 13º salário.

**3. Por que o mês de início da licença não foi considerado?**

Confira a quantidade de dias de licença no mês.

Se a licença tiver menos de 15 dias naquele mês, o Pessoas+ não considera esse mês como um avo de licença.

**4. Por que o 13º foi calculado pela empresa e também apareceram eventos de licença-maternidade?**

Verifique o código de afastamento utilizado pela ocorrência.

No código da **tabela FGTS**, confira se a opção **Direito ao décimo terceiro** está desmarcada.

Se a configuração estiver incorreta, o período pode permanecer no cálculo normal da empresa e também ser considerado nos eventos específicos da licença.

Depois de corrigir a configuração, realize novamente o cálculo do 13º.

**5. As médias são consideradas no 13º durante a licença-maternidade?**

Sim.

Quando aplicáveis, as médias são demonstradas nos eventos específicos:

- **313** para a primeira parcela;
- **314** para a segunda parcela;
- **229** para o 13º proporcional na rescisão.

**6. Por que o evento 308 não possui INSS e o 309 possui?**

Os eventos possuem tratamentos diferentes de acordo com a parcela do 13º.

O **308** corresponde à primeira parcela e não possui incidência de INSS.

O **309** corresponde à segunda parcela e possui incidência de INSS.

**7. Alterei a configuração do afastamento, mas o cálculo não mudou. O que devo fazer?**

Se o 13º já havia sido calculado antes da alteração, realize novamente o cálculo.

O recálculo é necessário para que o sistema considere a configuração atualizada.

**8. O código da tabela Causa também precisa estar com "Direito ao décimo terceiro" desmarcado?**

Para o tratamento dos avos de 13º da licença-maternidade, a configuração relevante é a do código de afastamento da **tabela FGTS** utilizado pela ocorrência.

Confira esse código antes de alterar a configuração do código da tabela Causa.

**9. O que acontece se a licença não tiver data de término?**

O sistema considera a data prevista de retorno, quando informada, para determinar o período da licença.

Para conferir esse período, verifique no lançamento da licença os campos **Dias previsto** e **Data Final Prevista da Ocorrência**.

**10. Como conferir se o cálculo foi feito corretamente?**

Após o cálculo, confira:

1. o período da licença;
2. a quantidade de avos considerados;
3. os eventos de 13º da licença-maternidade;
4. os eventos normais de 13º;
5. os eventos de médias, quando aplicáveis;
6. a incidência de INSS dos eventos gerados.

### Artigos Relacionados

- [Como cadastrar a ocorrência de licença-maternidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/43940237985815)
- [Prorrogação da licença-maternidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/4413844578327)
- [Cadastro de Códigos de Afastamento para Rescisão](https://ajuda.sankhya.com.br/hc/pt-br/articles/13729923854487)
- [Cadastro de Eventos (Rubricas) da Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)
- [Cálculo do 13º salário](https://ajuda.sankhya.com.br/hc/pt-br/articles/36494077074071)
