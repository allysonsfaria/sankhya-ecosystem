---
id: "360057819854"
titulo: "Manual configuração para geração dos registros restituição do ICMS ST - MG"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360057819854-Manual-configura%C3%A7%C3%A3o-para-gera%C3%A7%C3%A3o-dos-registros-restitui%C3%A7%C3%A3o-do-ICMS-ST-MG"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:26:45Z"
rotulos: ["#PUBLIFER", "Configuração", "SPED", "ICMS", "EFD", "Substituição Tributária", "O.S1568307", "#SOFTWARE", "Restituição e Complemento", "C180 C185 C181 C186 H005 H010 H030 1250 1255", "Restituição/Complemento Registro ICMS", "MG"]
---

# Manual configuração para geração dos registros restituição do ICMS ST - MG

[DECRETO Nº 47.809, DE 20 DE DEZEMBRO DE 2019 (MG de 21/12/2019)](http://www.fazenda.mg.gov.br/empresas/legislacao_tributaria/decretos/2019/d47809_2019.html)

O decreto [47.809/2019](http://www.fazenda.mg.gov.br/empresas/legislacao_tributaria/decretos/2019/d47809_2019.html) de MG em seus artigos 5º e 6º altera a parte 1 do anexo XV do RICMS de MG, sendo instituídas duas hipóteses de restituição do ICMS devido por substituição tributária:

![Imagem 1: Restituição do ICMS ST - Fato Gerador Presumido Não Realizado : Considerando o Decreto 47.809/2019 e os arts. 22 a 31,…](https://ajuda.sankhya.com.br/hc/article_attachments/16252975966743) [Restituição do ICMS ST - Fato Gerador Presumido Não Realizado](http://www.sped.fazenda.mg.gov.br/spedmg/export/sites/spedmg/efd/downloads/EFD-Manual-de-Escrituracao-Restituicao-do-ICMS-ST-Fato-Gerador-Presumido-Nao-Realizado-2021.01-.pdf): Considerando o Decreto 47.809/2019 e os arts. 22 a 31, da Parte 1 do Anexo XV do RICMS;

![Imagem 2: Complemento e Restituição do ICMS ST Aspecto Quantitativo : Considerando o Decreto 47.809/2019, e os arts. 31-A ao 31-J…](https://ajuda.sankhya.com.br/hc/article_attachments/16252989813527) [Complemento e Restituição do ICMS ST Aspecto Quantitativo](http://www.sped.fazenda.mg.gov.br/spedmg/export/sites/spedmg/efd/downloads/EFD-Manual-de-Escrituracao-Complemento-e-Restituicao-do-ICMS-ST-Aspecto-Quantitativo-Versao-2021.01.pdf): Considerando o Decreto 47.809/2019, e os arts. 31-A ao 31-J da Parte 1 do Anexo XV do RICMS, nas hipóteses da complementação e da restituição do ICMS devido por substituição tributária em razão da não definitividade da base de cálculo presumida;

### Configurações para geração dos registros C180, C185, C181, C186, H005, H010, H030, 1250 e 1255

#### Configuração do campo "Considerar operações com ressarcimento/complemento de ST"

A funcionalidade **"Operação com ressarcimento/complemento de ST"** foi criada para **garantir** que **apenas os movimentos fiscais** relacionados a ressarcimento ou complemento de ICMS-ST **sejam considerados na geração dos registros C180, C181, C185 e C186 no SPED EFD**.

(1)** Para que essa lógica seja aplicada, ative o campo "Considerar operações com ressarcimento/complemento de ST", na tela "Empresa" (Comercial » Preferências » Empresa),** aba “EFD - Escrituração Fiscal Digital”, sessão EFD, sub aba "Geração C180/C181/C185/C186".

**(1)**A partir dessa **ativação, o sistema passa a considerar apenas os movimentos que tenham** o campo Operação com ressarcimento/complemento de ST marcado**em pelo menos um dos seguintes cadastros: TOP, CFOP ou Observação Padrão.**

- No cadastro da **TOP**, o campo permite informar que a operação envolvida trata de ressarcimento ou complemento, sinalizando ao sistema que os movimentos gerados devem ser incluídos nos registros fiscais correspondentes;
- No cadastro de **CFOP**, a marcação identifica o código como vinculado a uma operação de ressarcimento ou complemento, habilitando sua inclusão nos registros;
- No cadastro de **Observações para Notas**, o campo serve para sinalizar observações padrão aplicáveis a esse tipo de operação, garantindo o correto enquadramento fiscal dos movimentos.

Vale destacar que, esses marcadores funcionam em conjunto com a ativação principal nas Preferências da Empresa, assegurando conformidade com a legislação e automatizando a geração dos registros específicos apenas quando necessário.

**Configuração do campo “Complemento/Restituição ICMS/ST - MG”**

**(1)** Ainda tela Empresa (Comercial » Preferências » Empresa), aba EFD - Escrituração Fiscal Digital, sessão EFD, sub aba Geração C180/C181/C185/C186, configure o campo “**Complemento/Restituição ICMS/ST - MG**” com uma das opções disponíveis:

(2)** Não se Aplica**: Nenhum registro referente a restituição ICMS/ST será gerado;

(2)** Restituição do ICMS ST – Fato Gerador Presumido Não Realizado:** O fato gerador presumido não realizado refere-se às operações com mercadorias que em etapa anterior tenham sofrido o recolhimento do ICMS por substituição tributária e ocorra uma das situações abaixo:

- Saídas sequentes para estabelecimento de contribuinte situado em outra unidade da federação;
- Saída amparada por isenção ou não incidência;
- Saída destinada a baixa de estoque por perecimento, furto, roubo ou qualquer outro tipo de perda.

Neste caso será necessário a geração e envio dos registros C180, C185, H030, 1250 e 1255, conforme [Manual de Escrituração – Restituição do ICMS ST – Fato Gerador Presumido Não Realizado](http://www.sped.fazenda.mg.gov.br/spedmg/export/sites/spedmg/efd/downloads/EFD-Manual-de-Escrituracao-Restituicao-do-ICMS-ST-Fato-Gerador-Presumido-Nao-Realizado-.pdf).

(2)** Complemento e Restituição do ICMS ST – Aspecto Quantitativo:** Para esta situação dois aspectos distintos em relação às mercadorias que em etapa anterior tenham sofrido o recolhimento do ICMS por substituição tributária.

- O contribuinte substituído que promover operação interna destinada a consumidor final e cujo valor de saída da mercadoria seja superior ao valor da base de cálculo do ICMS ST da sua respectiva compra, haverá complemento do ICMS ST pela diferença identificada;
- Por outro lado, nos casos em que saída da mercadoria tenha seu valor inferior à base de cálculo do ICMS ST da sua respectiva compra, haverá restituição do ICMS ST pela diferença identificada.

Neste caso será necessário a geração e envio dos registros C180, C181, C185, C186, C430, H030, 1250 e 1255 (registro C330 não foi implementado), conforme [Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo](http://www.sped.fazenda.mg.gov.br/spedmg/export/sites/spedmg/efd/downloads/EFD-Manual-de-Escrituracao-Complemento-e-Restituicao-do-ICMS-ST-Aspecto-Quantitativo-Versao-2021.01.pdf).

**Nota:** Para a hipótese “Complemento e Restituição do ICMS ST – Aspecto Quantitativo” o contribuinte substituído, exclusivamente varejista ou atacadista e varejista em relação às operações que atuar como varejista em venda a consumidor final, deverá ter realizado junto ao Sistema Integrado de Administração da Receita Estadual - SIARE a opção pela Definitividade da Base de Cálculo do ICMS ST.

Na sub-guia “**Blocos e Registros**”, cadastre os blocos a serem considerados na geração do arquivo EFD ICMS/IPI, a configuração deve ser realizada seguindo definição do campo “**Complemento/Restituição ICMS/ST - MG”,** da guia **“EFD - Escrituração Fiscal Digital”** quando selecionamos o “Tipo de escrituração” igual a “EFD”**:**

- **Restituição do ICMS ST – Fato Gerador Presumido Não Realizado:** os registros C180, C185, H005, H010, H030, 1250 e 1255.

| **Registro** | **Descrição** | **Gerar Registro** | **Gerar entrada** | **Gerar Saída** |
| --- | --- | --- | --- | --- |
| C180 | Informações complementares das operações de entrada de mercadorias sujeitas à substituição tributária (código 01, 1B, 04 e 55) | SIM | SIM | NÃO |
| C185 | Informações complementares das operações de saída de mercadorias sujeitas à substituição tributária (código 01, 1B, 04 e 55) | SIM | NÃO | SIM |
| H005 | Totais do Inventário | SIM |  |  |
| H010 | Inventário | SIM |  |  |
| H030 | Informações complementares do inventário das mercadorias sujeitas ao regime de substituição tributária | SIM |  |  |
| 1250 | Informações consolidadas de saldos de restituição, ressarcimento e complementação do ICMS | SIM |  |  |
| 1255 | Informações consolidadas de saldos de restituição, ressarcimento e complementação do ICMS por motivo | SIM |  |  |

- **Complemento e Restituição do ICMS ST – Aspecto Quantitativo:**  todos os registros do item a, acrescido dos registros C181 e C186

| **Registro** | **Descrição** | **Gerar Registro** | **Gerar entrada** | **Gerar Saída** |
| --- | --- | --- | --- | --- |
| C181 | Informações complementares das operações de devolução de saídas de mercadorias sujeitas à substituição tributária (código 01, 1B, 04 e 55). | SIM | SIM | NÃO |
| C186 | Informações complementares das operações de devolução de entradas de mercadorias sujeitas à substituição tributária (código 01, 1B, 04 e 55). | SIM | NÃO | SIM |

### Geração do arquivo  Escrituração Fiscal Digital - ICMS/IPI

**EFD - Escrituração Fiscal Digital - ICMS/IPI (Livros Fiscais » Conexão)**

Na geração do arquivo EFD Escrituração Fiscal Digital ICMS/IPI, as configurações realizadas na guia “**Restituição/Complementação de ST**” são utilizadas no cálculo e registro dos valores médios, utilizados na elaboração dos registros C180, C185, C181, C186, H005, H010, H030, 1250 e 1255.

**Restituição/Complementação de ST (Livros Fiscais » Conexão » EFD - Escrituração Fiscal Digital - ICMS/IPI )**

(1)** Inventário**

O EFD exige que o inventário esteja com a data do primeiro dia anterior à data do início do período de geração do arquivo. Informe no campo a data do inventário somente se desejar gerar os registros de Restituição/Complementação de ST. Este inventário será utilizado na elaboração do inventário de motivo 06 (Para controle das mercadorias sujeitas ao regime de substituição tributária – restituição/ ressarcimento/ complementação). 

Caso tenha dúvidas sobre a geração do inventário, consulte o tópico [Melhores Práticas para configuração e geração do Bloco H (Inventário) no EFD-Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045094453-Melhores-Pr%C3%A1ticas-para-configura%C3%A7%C3%A3o-e-gera%C3%A7%C3%A3o-do-Bloco-H-Invent%C3%A1rio-no-EFD-Fiscal-) no ajuda.sankhya.com.br.

**Data do Inventário**: informe neste campo a data a ser considerada para inventário;

**Forma de utilização do inventário**: indica se vai usar a cópia ou a contagem do inventário;

(1)** Cálculo dos Valores Médios**

Os valores médios serão calculados conforme fórmula definida em cada um dos campos de valor. Além dos campos para definição das fórmulas, botões para facilitar a configuração, utilização de fórmulas padrão e os campos para a configuração do filtro personalizado. 

Foram criados os campos para a configuração da fórmula de cada campo de valor médio e os campos para a configuração do filtro personalizado. Alguns botões foram criados para facilitar a configuração e utilização dos valores padrão do sistema, ou acessar o construtor de expressões e personalizar a fórmula a ser utilizada no cálculo dos valores médios.

**Valor do ICMS da Operação:** Informe neste campo a expressão responsável por retornar o valor do ICMS da operação a ser considerado no cálculo dos valores médios.

**Base de ST**: Informe neste campo a expressão responsável por retornar o valor da base de ST a ser considerado no cálculo dos valores médios.

**Valor de ST**: Informe neste campo a expressão responsável por retornar o valor de ST a ser considerado no cálculo dos valores médios.

**Valor do FCP de ST**: Informe neste campo a expressão responsável por retornar o valor do FCP de ST a ser considerado no cálculo dos valores médios.

**Filtro Personalizado**: A finalidade do filtro personalizado é a definição de regras específicas do parceiro a serem utilizadas na obtenção das movimentações de venda e de compra com substituição tributária dentro da referência.

**Ignorar filtro padrão**: Quando marcado o sistema inclui no movimento as notas com quantidades negociadas igual a zero e que não atualizaram o estoque. Quando desmarcada o sistema inclui no movimento apenas notas com quantidades negociadas maiores que zero e que atualizaram o estoque dando entrada e ou saída.

**Recalcula Inventário:** Quando marcado gera os movimentos na tabela de **Valor Médio para Restituição de ST**, com base nos dados presentes no inventário e movimentações retroativas que embasam o estoque. Quando desmarcado gera os movimentos na tabela de **Valor Médio para Restituição de ST**, apenas com base nas movimentações da referência que satisfaçam as condições.

(1)** Registro dos Valores Médios**

Foram criadas duas novas tabelas TGFEFDVMRST e TGFEFDVMRSTDIA , tendo **VMRST** contido em seus nomes como **Valor Médio para Restituição de ST**. Essas tabelas terão como único objetivo armazenar os dados dos valores médios de cada dia, que será utilizado para preencher os registros necessários com essas informações.

A tabela pai é um cabeçalho, com as seguintes colunas: CODEMP, DTREF, a coluna USOU é uma coluna que define se o cálculo usou inventário (“I”) ou saldo do mês anterior (“M”)  para iniciar os cálculos dos registros filhos da referência, a coluna DTFORMULA registra a última data de alteração da fórmula utilizada para gerar este registro, a coluna TIPINVENT define qual o tipo de inventário utilizado se copia (“P”) ou contagem (“T”).

TGFEFDVMRST (Pai)

![Imagem 3: TGFEFDVMRST (Pai)](https://ajuda.sankhya.com.br/hc/article_attachments/5011801910295)

A tabela filha guarda a média diária por produto e por imposto, para que essa possa ser utilizada para prover dados aos registros H030, C185, C330, entre outros.

TGFEFDVMRSTDIA (Filha)

![Imagem 4: TGFEFDVMRSTDIA (Filha)](https://ajuda.sankhya.com.br/hc/article_attachments/5011826219287)

A coluna TIPIMPOSTO define qual o tipo de imposto que aquela média diária se trata ICMS (“I”), BASEST (“B”), ST (“S”) e ou FCP ST (“F”), a coluna TIPOMEDIA define qual o tipo daquela média, se ela é uma média diária (“D”) ou se é uma contagem/cópia de inventário (“I”).

**Fluxo do processo utilizado pelo sistema no cálculo dos valores médios**

- Limpa a tabela TGFEFDVMRSTDIA para o período a ser gerado do EFD;

- Busca os produtos que estão no inventário;

- Busca as notas de entradas que justificam a quantidade do inventário, fazendo o cálculo dos valores de médias;

- Grava os produtos do inventário na tabela TGFEFDVMRSTDIA com o campo TIPMEDIA igual a 'I' (Inventário);

- Usa a média gravada para o inventário para gerar o registro H030;

- A partir das médias calculadas para  inventário, processa os movimentos do período a serem gerados do EFD, TIPMOV IN ('C', 'D', 'V', 'E', 'T') calculando novas médias e gravando na tabela TGFEFDVMRSTDIA com o campo TIPMEDIA igual a 'D' (Diário);

**Nota**: Foi criado o parâmetro DTINIAMPINVEFD (Dt. Limite p/ amparo de estoque calc invent p/ EFD) com default ‘01/01/2019’. O processo de amparar o inventário de um produto vai procurar as notas de entradas anteriores ao inventário, até o limite da data que está no parâmetro DTINIAMPINVEFD, e calcular a média conforme essas notas, resultando em uma média para a data do inventário. Depois essa média continua a ser calculada conforme o movimento de entrada e saída do mês, resultando em uma média diária a cada dia de movimento. Os valores médios calculados são: “Valor do ICMS”, “Base de ST”, “Valor de ST”, “Valor de FCP de ST”.

**Regras de geração dos registros C180, C185, C181, C186, H005, H010, H030, 1250 e 1255**

Para a execução dos processos é preciso que a data inicial informada no período da geração seja superior a ‘01/01/2020’, a UF da empresa seja de Minas Gerais e a **“Data do Inventário”** da aba **“Restituição/Complementação de ST”** esteja informada, e versão do layout do arquivo seja igual ou superior ao layout 014, versão 1.13.

**Nota**: Os registros **C181** e **C186** serão gerados quando a data inicial informada no período da geração for superior a ‘01/01/2021’, período em que entra em vigor a versão do layout do arquivo 015 - versão 1.14.

A geração dos registros **NÃO** depende da implantação e ou utilização da rotina de rastreamento de estoque.

**Registro C180 - Informações complementares das operações de entrada de mercadorias sujeitas à substituição tributária**

Serão consideradas todas as operações de entrada com mercadorias sujeitas ao regime de substituição tributária, cujo modelo do documento seja igual a 01, 1b, 04 e 55, e possuam registro na tabela de valores médios diários de substituição tributária (TGFEFDVMRSTDIA).

**Nota:** Até 12/2020 são geradas no registro C180 também as entradas por devolução de saídas, a partir de 01/2021 as entradas por devolução de saídas passam a ser geradas no registro C181.

Na geração do registro C180 o sistema grava o conteúdo utilizado na elaboração do registro para fins de geração futura do registro C186 (tabela TGFC180F).

**Regras de preenchimento dos campos registros C180**

| **Nº** | **Campo** | **Descrição** | **Regra geração/Origem valores** |
| --- | --- | --- | --- |
| 1 | REG | Texto fixo contendo "C180” |  |
| 2 | COD\_RESP\_RET | Código que indica o responsável pela retenção do ICMS ST:  1-Remetente Direto  2-Remetente Indireto  3-Próprio declarante | 1) Remetente Direto: ST Normal (CST 10, 30 e 70);  2) Remetente Indireto: ST Anterior (CST 60);  3) Próprio declarante: ST Extra (se não for nenhum dos CST anteriores e tiver valor ST extra nota); |
| 3 | QUANT\_CONV | Quantidade do item | Quantidade informada no item da nota.  (TGFITE.QTDNEG) |
| 4 | UNID | Unidade adotada para informar o campo QUANT\_CONV. | Unidade informada no item da nota.  (TGFITE.CODVOL) |
| 5 | VL\_UNIT\_CONV | Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo “QUANT\_CONV” | Valor unitário informado no item da nota.  (TGFITE.VLRUNIT) |
| 6 | VL\_UNIT\_ICMS\_OP\_CONV | Valor unitário do ICMS operação própria que o informante teria direito ao crédito caso a mercadoria estivesse sob o regime comum de tributação, considerando unidade utilizada para informar o campo “QUANT\_CONV” | Valor do ICMS OP da tabela de impostos dividido pela quantidade.  (TGFDIN.VALOR/TGFITE.QTDNEG WHERE TGFDIN.TIPIMP=1) |
| 7 | VL\_UNIT\_BC\_ICMS\_ST\_CONV | Valor unitário da base de cálculo do imposto pago ou retido anteriormente por substituição, considerando a unidade utilizada para informar o campo “QUANT\_CONV”, aplicando-se redução, se houver. | -ST Normal (CST 10, 30 e 70):   Utiliza o valor do campo "Base substituição" do item da nota dividido pela "Quantidade".  (TGFITE.BASESUBSTIT/TGFITE.QTDNEG)   -ST Anterior (CST 60):   Utiliza o valor registrado no campo "Base de Cálc. da ST de oper. ant." do item da nota divido pela "Quantidade".  (TGFITE.BASESUBSTITANT/TGFITE.QTDNEG)   -ST Extra (se não for nenhum dos CST anteriores e tiver valor ST extra nota):   Utiliza o valor registrado no campo "Base ST Extra Nota" do item da nota dividido pela "Quantidade".  (ITE.BASESTEXTRANOTA/ITE.QTDNEG) |
| 8 | VL\_UNIT\_ICMS\_ST\_CONV | Valor unitário do imposto pago ou retido anteriormente por substituição, inclusive FCP se devido, considerando a unidade utilizada para informar o campo “QUANT\_CONV”. | -ST Normal (CST 10, 30 e 70):  Utiliza o valor do campo "Vlr. substituição" do item da nota dividido  pela "Quantidade".  (TGFITE.VLRSUBST/TGFITE.QTDNEG)   -ST Anterior (CST 60):  Utiliza o valor registrado no campo "Vlr. do ICMS da ST da oper. ant." do item da nota divido pela "Quantidade".  ( TGFITE.VLRSUBSTANT/TGFITE.QTDNEG)   -ST Extra (se não for nenhum dos CST anteriores e tiver valor ST extra nota):  Utiliza o valor registrado no campo "Valor ST Extra Nota" do item da nota dividido pela "Quantidade".  ( ITE.VLRSTEXTRANOTA/ITE.QTDNEG) |
| 9 | VL\_UNIT\_FCP\_ST\_CONV | Valor unitário do FCP\_ST agregado ao valor informado no campo “VL\_UNIT\_ICMS\_ST\_CONV” | Utiliza o valor registrado no campo "Vlr. FCP Interno" da tabela de impostos para o ICMS ST dividido pela quantidade.  (TGFDIN.VLRFCPINT/TGFITE.QTDNEG WHERE TGFDIN.TIPIMP=2) |
| 10 | COD\_DA | Código do modelo do documento de arrecadação:  0 – Documento estadual de arrecadação  1 – GNRE | Não está previsto geração de conteúdo neste campo. |
| 11 | NUM\_DA | Número do documento de arrecadação estadual, se houver | Não está previsto geração de conteúdo neste campo. |

**Exemplo:**

|C100|0|1|000000003|55|00|001|18|...

|C170|1|1||1200,00000|UN|1992,00|0,00|0|000|2102|200|1992,00|12,00|...

|C170|2|4||1200,00000|UN|3180,00|0,00|0|010|2403|200|0,00|0,00|0,00|...

|C180|1|1200,000000|UN|2,650000|0,318000|0,000000|0,000000|0,000000|||

|C190|000|2102|12,00|2191,20|1992,00|239,04|0,00|0,00|0,00|0,00||

|C190|010|2403|0,00|3966,41|0,00|0,00|0,00|0,00|0,00|0,00||

**Registro C186 - Informações complementares das operações de devolução de entradas de mercadorias sujeitas à substituição tributária**

Serão consideradas todas as operações de devolução de entrada de mercadorias sujeitas ao regime de substituição tributária, cujo modelo do documento seja igual a 01, 1b, 04 e 55, que estejam ligadas a nota de entrada de mercadorias sujeitas ao regime de substituição tributária (TGFVAR), que a nota de entrada de mercadoria que originou a devolução tenha participado da geração do registro C180 (possuam registro na tabela TGFC180F) e possuam registro na tabela de valores médios diários de substituição tributária (TGFEFDVMRSTDIA).

Não está prevista a geração deste registro para hipótese de restituição pelo **Fato Gerador Presumido Não Realizado.**

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16252975976727) OBSERVAÇÃO:**

Até 12/2020 são geradas no registro C185 as saídas por devolução de entradas, a partir de 01/2021 as saídas por devolução de entradas passam a ser geradas no registro C186.

**Regras de Preenchimento dos campos no registro C186**

| **Nº** | **Campo** | **Descrição** | **Regra geração/Origem valores** |
| --- | --- | --- | --- |
| 1 | REG | Texto fixo contendo "C186” |  |
| 2 | NUM\_ITEM | Número sequencial do item no documento fiscal de saída | Sequencia fiscal e ou sequência do item na nota.  (TGFITE.SEQUENCIAFISCAL ou TGFITE.SEQUENCIA) |
| 3 | COD\_ITEM | Código do item (campo 02 do Registro 0200) | Codigo do produto.  (TGFITE.CODPROD) |
| 4 | CST\_ICMS | Código da Situação Tributária referente ao ICMS no documento fiscal de saída | Tributação do item da nota.  (TGFITE.CODTRIB) |
| 5 | CFOP | Código Fiscal de Operação e Prestação no documento fiscal de saída | CFOP do item da nota.  (TGFITE.CODCFO) |
| 6 | COD\_MOT\_REST\_COMPL | Código do motivo da restituição ou complementação conforme Tabela 5.7 | MG400 |
| 7 | QUANT\_CONV | Quantidade do item no documento fiscal de saída de acordo com as instruções de preenchimento. | Quantidade item da nota.  (TGFITE.QTDNEG) |
| 8 | UNID | Unidade adotada para informar o campo QUANT\_CONV. | Unidade do item da nota.  (TGFITE.CODVOL) |
| 9 | COD\_MOD\_ENTRADA | Código do modelo do documento fiscal de entrada, conforme a tabela indicada no item 4.1.1 | Modelo documento fiscal de entrada que originou a devolução e foi previamente gerado no registro C180.  (TGFC180F.COD\_MOV) |
| 10 | SERIE\_ENTRADA | Número de série do documento de entrada em papel | Série do documento fiscal de entrada que originou a devolução e que foi previamente gerado no registro C180.  (TGFC180.SER) |
| 11 | NUM\_DOC\_ENTRADA | Número do documento fiscal de entrada | Número do documeno fiscal de entrada que originou a devolução e que foi previamente gerado no registro C180.(TGFC180F.NUM\_DOC) |
| 12 | CHV\_DFE\_ENTRADA | Chave do documento fiscal eletrônico de entrada | Chave do documeno fiscal de entrada que originou a devolução e que foi previamente gerado no registro C180.  (TGFC180F.CHV\_DFE) |
| 13 | DT\_DOC\_ENTRADA | Data da emissão do documento fiscal de entrada | Data de entrada/saída do documeno fiscal de entrada que originou a devolução e que foi previamente gerado no registro C180.  (TGFC180F.DT\_DOC) |
| 14 | NUM\_ITEM\_ENTRADA | Item do documento fiscal de entrada | Sequência fiscal ou sequência do item no documeno fiscal de entrada que originou a devolução e que foi previamente gerado no registro C180.  (TGFC180F.NUM\_ITEM) |
| 15 | VL\_UNIT\_CONV\_ENTRADA | Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo “QUANT\_CONV”, correspondente ao valor do campo VL\_UNIT\_CONV, preenchido na ocasião da entrada | Valor unitário do item do documeno fiscal de entrada que originou a devolução e que foi previamente gerado no registro C180.  (TGFC180F.VL\_UNIT\_CONV) |
| 16 | VL\_UNIT\_ICMS\_OP\_CONV\_ ENTRADA | Valor unitário do ICMS correspondente ao valor do campo VL\_UNIT\_ICMS\_OP\_CONV, preenchido na ocasião da entrada | Valor unitário do ICMS do documeno fiscal de entrada que originou a devolução e que foi previamente gerado no registro C180.  (TGFC180F.VL\_UNIT\_ICMS\_OP\_CONV) |
| 17 | VL\_UNIT\_BC\_ICMS\_ST \_CONV\_ENTRADA | Valor unitário da base de cálculo do imposto pago ou retido anteriormente por substituição, correspondente ao valor do campo VL\_UNIT\_BC\_ICMS\_ST\_CONV, preenchido na ocasião da entrada | Valor unitário da base de ICMS ST do documeno fiscal de entrada que originou a devolução e que foi previamente gerado no registro C180.  (TGFC180F.VL\_UNIT\_BC\_ICMS\_ST\_CONV) |
| 18 | VL\_UNIT\_ICMS\_ST\_CONV\_ ENTRADA | Valor unitário do imposto pago ou retido anteriormente por substituição, inclusive FCP se devido, correspondente ao valor do campo VL\_UNIT\_ICMS\_ST\_CONV, preenchido na ocasião da entrada | Valor unitário do ICMS ST do documeno fiscal de entrada que originou a devolução e que foi previamente gerado no registro C180.  (TGFC180F.VL\_UNIT\_ICMS\_ST\_CONV) |
| 19 | VL\_UNIT\_FCP\_ST\_CONV\_E NTRADA | Valor unitário do FCP\_ST, correspondente ao valor do campo VL\_UNIT\_FCP\_ST\_CONV, preenchido na ocasião da entrada | Valor unitário do FCP ST do documeno fiscal de entrada que originou a devolução e que foi previamente gerado no registro C180.  (TGFC180F.VL\_UNIT\_FCP\_ST\_CONV) |

**Exemplo:**

|C100|1|0|000000003|55|00|010|110122|...

|C186|1|5|010|6411|**MG400**|10,000000|UN|55|||33333333333333333333333333333333333333333333|20082021|1|5,250000|0,630000|0,000000|0,000000|0,000000|

|C190|010|6411|12,00|65,48|52,50|6,30|0,00|0,00|0,00|0,00|

 

**Registro C185 - Informações complementares das operações de saída de mercadorias sujeitas à substituição tributária**

Serão consideradas as operações de saída de mercadorias sujeitas ao regime de substituição tributária, cujo o modelo do seja igual a 01, 1B, 04, 55 e 65, possuam registro na tabela de valores médios diários de substituição tributária (TGFEFDVMRSTDIA) e satisfaçam as condições abaixo descritas seguindo as diferentes hipóteses de restituição:

**- Fato Gerador Presumido Não Realizado:** Serão considerados os seguintes movimentos de saída de mercadorias:

- Notas tributadas novamente: Notas de saída com valores de ICMS ou ST maiores que zero, e CST’s “000", "010", "020", "030", "070" e "090", ou CSOSN’s  "201" e "202";
- Notas de Perda, Roubo ou Consumo: Notas de saída com CFOP 5927, ou com CFOP 5949 e CST “090” ou CSOSN “900");
- Notas emitidas com isenção: Notas de saída com CST "040" e "041", ou CSOSN "103", "400";

**- Aspecto Quantitativo:** Serão considerados os seguintes movimentos de saída de mercadorias:

- Notas com ICMS cobrado anteriormente por substituição: Notas de saída com valores de ICMS ou ST maiores igual a ZERO e CST “060", ou CSOSN  "500";

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16252975976727) OBSERVAÇÃO:**

Até 12/2020 são geradas no C185 também as saídas por devolução de entradas, a partir de 01/2021 as saídas por devolução de entradas passam a ser geradas no registro C186.

Durante a geração do registro C185 gravamos todo o conteúdo utilizado na elaboração do registro para fins de geração futura do registro C181 (tabela TGFC185F).

 

**Regras de Preenchimento dos campos no registro C185**

| **Nº** | **Campo** | **Descrição** | **Regra geração/Origem valores** |
| --- | --- | --- | --- |
| 1 | REG | Texto fixo contendo "C185” |  |
| 2 | NUM\_ITEM | Número sequencial do item no documento fiscal | Sequência fiscal e ou sequência do item na nota.  (TGFITE.SEQUENCIAFISCAL ou TGFITE.SEQUENCIA) |
| 3 | COD\_ITEM | Código do item (campo 02 do Registro 0200) | Codigo do produto.  (TGFITE.CODPROD) |
| 4 | CST\_ICMS | Código da Situação Tributária referente ao ICMS | Tributação do item da nota.  (TGFITE.CODTRIB) |
| 5 | CFOP | Código Fiscal de Operação e Prestação | CFOP do item da nota.  (TGFITE.CODCFO) |
| 6 | COD\_MOT\_REST\_COMPL | Código do motivo da restituição ou complementação conforme Tabela 5.7 | -**Fato Gerador Presumido Não Realizado**:  a) Notas tributadas novamente, notas de perda, roubo ou consumo, Notas emitidas com isenção.  MG200 - Restituição de ICMS/ST, em razão da não ocorrência do fato gerador presumido   -**Aspecto Quantitativo**: Notas com ICMS cobrado anteriormente por substituição:  b) Quando o valor unitário da mercadoria for igual ao valor da base de ICMS ST unitária média.  MG000 - Não se aplica restituição ou complementação de ICMS/ST;  c) Quando o valor unitário da mercadoria for inferior ao valor da base de ICMS ST unitária média.  MG100 - Restituição de ICMS/ST, em razão do valor de saída da mercadoria final ser inferior ao da BC/ST;  d) Quando o valor unitário da mercadoria for superior ao valor da base de ICMS ST unitária média.  MG300 - Complementação de ICMS/ST, em razão do valor de saída da mercadoria a consumidor final ser superior ao da BC/ST; |
| 7 | QUANT\_CONV | Quantidade do item | Quantidade item da nota.  (TGFITE.QTDNEG) |
| 8 | UNID | Unidade adotada para informar o campo QUANT\_CONV. | Unidade do item da nota.  (TGFITE.CODVOL) |
| 9 | VL\_UNIT\_CONV | Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo “QUANT\_CONV”. | Valor unitario do item.  (TGFITE.VLRUNIT) |
| 10 | VL\_UNIT\_ICMS\_NA\_OPE RACAO\_CONV | Valor unitário para o ICMS na operação, caso não houvesse a ST, considerando unidade utilizada para informar o campo “QUANT\_CONV”, considerando redução da base de cálculo do ICMS ST na tributação, se houver. | -Fato Gerador Presumido Não Realizado  Vazio;   -Aspecto Quantitativo  a) Caso exista aliquota interna configurada o valor unitário da mercadoria vezes a alíquota interna de ICMS;  b) Não existindo aliquota interna o valor unitário do ICMS da nota;  (TGFDIN.VALOR AND TGFDIN.CODIMP=1) |
| 11 | VL\_UNIT\_ICMS\_OP\_CONV | Valor unitário do ICMS OP calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo “QUANT\_CONV”, utilizado para cálculo de ressarcimento/restituição de ST, no desfazimento da substituição tributária, quando se utiliza a fórmula descrita nas instruções de preenchimento do campo 15, no item a1). | -Fato Gerador Presumido Não Realizado  Vazio;   -Aspecto Quantitativo  Vazio |
| 12 | VL\_UNIT\_ICMS\_OP\_EST OQUE\_CONV | Valor médio unitário do ICMS que o contribuinte teria se creditado referente à operação de entrada das mercadorias em estoque caso estivesse submetida ao regime comum de tributação, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo “QUANT\_CONV” | Valor médio unitário do ICMS.  (TGFEFDVMRSTDIA.VLRICMSUNITMED) |
| 13 | VL\_UNIT\_ICMS\_ST\_EST OQUE\_CONV | Valor médio unitário do ICMS ST, incluindo FCP ST, das mercadorias em estoque, considerando a unidade utilizada para informar o campo “QUANT\_CONV” | Valor médio unitário do ICMS ST.  (TGFEFDVMRSTDIA.VLRSTUNITMED) |
| 14 | VL\_UNIT\_FCP\_ICMS\_ST\_ ESTOQUE\_CONV | Valor médio unitário do FCP ST agregado ao ICMS das mercadorias em estoque, considerando a unidade utilizada para informar o campo “QUANT\_CONV” | Valor médio unitário do FCP ST.  (TGFEFDVMRSTDIA.VLRFCPSTUNITMED) |
| 15 | VL\_UNIT\_ICMS\_ST\_CON V\_REST | Valor unitário do total do ICMS ST, incluindo FCP ST, a ser restituído/ressarcido, calculado conforme a legislação de cada UF, considerando a unidade utilizada para informar o campo “QUANT\_CONV”. | a) Quando o código do motivo da restituição ou complementação for igual a MG000, MG300:  O conteúdo do campo fica vazio;   b) Quando o código do motivo da restituição ou complementação for igual a MG100, MG200:  O conteúdo do campo é preenchido com o valor médio unitário do ICMS ST.  (TGFEFDVMRSTDIA.VLRSTUNITMED) |
| 16 | VL\_UNIT\_FCP\_ST\_CONV \_REST | Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo “VL\_UNIT\_ICMS\_ST\_CONV\_REST”, considerando a unidade utilizada para informar o campo “QUANT\_CONV”. | a) Quando o código do motivo da restituição ou complementação for igual a MG000, MG300:  O conteúdo do campo fica vazio;   b) Quando o código do motivo da restituição ou complementação for igual a MG100, MG200:  O conteúdo do campo é preenchido com o valor médio unitário do ICMS ST vezeze a aliquota de FCP ST.  (TGFEFDVMRSTDIA.VLRSTUNITMED \* Alíquota FCP ST) |
| 17 | VL\_UNIT\_ICMS\_ST\_CON V\_COMPL | Valor unitário do complemento do ICMS, incluindo FCP ST, considerando a unidade utilizada para informar o campo “QUANT\_CONV”. | a) Quando o código do motivo da restituição ou complementação for igual a MG000, MG100, MG200:  O conteúdo do campo fica vazio;   b) Quando o código do motivo da restituição ou complementação for igual a MG300:  O conteúdo do campo é preenchido com o Valor médio unitário do ICMS meno o Valor médio unitário do ICMS ST, incluindo FCP ST.  (C185.CAMPO12 - C185.CAMPO13) |
| 18 | VL\_UNIT\_FCP\_ST\_CONV \_COMPL | Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo “VL\_UNIT\_ICMS\_ST\_CONV\_COMP L”, considerando unidade utilizada para informar o campo “QUANT\_CONV”. | a) Quando o código do motivo da restituição ou complementação for igual a MG000, MG100, MG200:  O conteúdo do campo fica vazio;   b) Quando o código do motivo da restituição ou complementação for igual a MG300:  O conteúdo do campo é preenchido com o Valor unitário do complemento do ICMS vezes a alíquota de FCP ST.  (C185.CAMPO17 \* Alíquota de FCP ST) |

**Exemplos:**

**- Fato Gerador Presumido Não Realizado:**

**Notas tributadas novamente:**

|C100|1|0|000000004|55|00|010|110111|31210899999999000191550100001101112211428430|20082021|20082021|22,28|0|0,00|0,00|17,38|1|0,00|0,00|0,00|17,38|1,22|25,80|3,17|0,00|||||

|C185|1|4|010|6403|**MG200**|2,000000|UN|2,770000|||0,318000|0,390342|0,000000|0,390342|0,000000|||

|C185|2|5|010|6403|**MG200**|2,000000|UN|5,920000|||0,630000|0,773325|0,000000|0,773325|0,000000|||

|C190|010|6403|7,00|22,28|17,38|1,22|25,80|3,17|0,00|0,00||

**Notas de Perda, Roubo ou Consumo:**

|C100|1|0|000000002|55|00|010|110113|31210899999999000191550100001101132853871744|20082021|20082021|10,31|0|0,00|0,00|9,37|1|0,00|0,00|0,00|9,37|1,69|0,00|0,00|0,00|||||

|C185|1|4|000|5927|**MG200**|1,000000|UN|3,450000|||0,318000|0,390342|0,000000|0,390342|0,000000|||

|C185|2|5|000|5927|**MG200**|1,000000|UN|5,920000|||0,630000|0,773325|0,000000|0,773325|0,000000|||

|C190|000|5927|18,00|10,31|9,37|1,69|0,00|0,00|0,00|0,00||

**Notas emitidas com isenção:**

|C100|1|0|000000005|55|00|010|110114|31210899999999000191550100001101142332490502|20082021|20082021|10,31|0|0,00|0,00|9,37|1|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|||||

|C185|1|4|040|6102|**MG200**|1,000000|UN|3,450000|||0,318000|0,390342|0,000000|0,390342|0,000000|||

|C185|2|5|040|6102|**MG200**|1,000000|UN|5,920000|||0,630000|0,773325|0,000000|0,773325|0,000000|||

|C190|040|6102|0,00|10,31|0,00|0,00|0,00|0,00|0,00|0,00||

**- Aspecto Quantitativo**

**Notas com ICMS cobrado anteriormente por substituição**

|C100|1|0|000000006|55|00|010|110117|31210899999999000191550100001101172368392251|23082021|23082021|0,50|0|0,00|0,00|0,45|1|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|||||

|C185|1|4|060|5405|**MG100**|1,000000|UN|0,450000|0,000000||0,318000|0,390342|0,000000|0,390342|0,000000|||

|C190|060|5405|0,00|0,50|0,00|0,00|0,00|0,00|0,00|0,00||

|C100|1|0|000000006|55|00|010|110118|31210899999999000191550100001101182338980896|23082021|23082021|13,59|0|0,00|0,00|12,35|1|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|||||

|C185|1|4|060|5405|**MG300**|1,000000|UN|12,350000|0,000000||0,318000|0,390342|0,000000|||-0,708342|0,000000|

|C190|060|5405|0,00|13,59|0,00|0,00|0,00|0,00|0,00|0,00||

**Registro C181 - Informações complementares das operações de devolução de saídas de mercadorias sujeitas à substituição tributária**

Serão consideradas todas as operações de devolução de saída de mercadorias sujeitas ao regime de substituição tributária, cujo modelo do documento seja igual a 01, 1b, 04 e 55, que estejam ligadas a nota de saída de mercadorias sujeitas ao regime de substituição tributária (TGFVAR), que a nota de saída de mercadoria que originou a devolução tenha participado da geração do registro C185 (possuam registro na tabela TGFC185F) e possuam registro na tabela de valores médios diários de substituição tributária (TGFEFDVMRSTDIA).

Não está prevista a geração deste registro para hipótese de restituição pelo **Fato Gerador Presumido Não Realizado.**

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16252975976727) OBSERVAÇÃO:**

Até 12/2020 são geradas no registro C180 as entradas por devolução de saídas, a partir de 01/2021 as entradas por devolução de saídas passam a ser geradas no registro C181.

**Regras de Preenchimento dos campos no registro C181**

| **Nº** | **Campo** | **Descrição** | **Regra geração/Origem valores** |
| --- | --- | --- | --- |
| 1 | REG | Texto fixo contendo "C181” |  |
| 2 | COD\_MOT\_REST\_COMPL | Código do motivo da restituição ou complementação conforme Tabela 5.7 | a) Devolução de notas de saída com valor unitário da mercadoria for igual ao valor da base de ICMS ST unitária média, que geraram no registro C185 o código de motivo de restituição ou complementação igual a MG000.  Geram o código do motivo de restituição ou complementação igual a MG500 - Devolução de Saída em que não se aplicou restituição, ressarcimento ou complemento   b) Devolução de notas de saída com valor unitário da mercadoria for inferior ao valor da base de ICMS ST unitária média, que geraram no registro C185 o código de motivo de restituição ou complementação igual a MG100.  Geram o código do motivo de restituição ou complementação igual a MG600 - Estorno de restituição/ressarcimento do imposto, calculado com base no valor saída inferior ao valor da B/C ICMS ST   c) Devolução de notas de saída com valor unitário da mercadoria for superior ao valor da base de ICMS ST unitária média, que geraram no registro C185 o código de motivo de Restituição ou complementação igual a MG300.  Geram o código do motivo de restituição ou complementação igual a MG800 - Estorno de Complemento do Imposto, calculado com base no valor de saída da mercadoria superior ao valor da B/C ICMS ST |
| 3 | QUANT\_CONV | Quantidade do item | Quantidade do item devolvido considerando a nota de saída que originou a devolução..  (TGFC181F.QUANT\_CONV) |
| 4 | UNID | Unidade adotada para informar o campo QUANT\_CONV | Unidade do item devolvido considerando a nota de saída que originou a devolução..  (TGFC181F.UNID) |
| 5 | COD\_MOD\_SAIDA | Código do modelo do documento fiscal de saída, conforme a tabela indicada no item 4.1.1 | Código do modelo do documento fiscal da nota de saída que originou a devolução.  (TGFC181F..COD\_MOD\_SAIDA) |
| 6 | SERIE\_SAIDA | Número de série do documento de saída em papel | Série da nota fiscal de saída que originou a devolução.  (TGFC181F.SERIE\_SAIDA) |
| 7 | ECF\_FAB\_SAIDA | Número de série de fabricação do equipamento ECF | Número de série de fabricação do equipamento ECF que originou a devolução.  (TGFC181F..ECF\_FAB\_SAIDA) |
| 8 | NUM\_DOC\_SAIDA | Número do documento fiscal de saída | Número do documento fiscal de saída que originou a devolução.  (TGFC181F.NUM\_DOC\_SAIDA) |
| 9 | CHV\_DFE\_SAIDA | Chave do documento fiscal eletrônico de saída | Chave do documento fiscal eletrônico de saída que originou a devolução.  (TGFC181F.CHV\_DFE\_SAIDA) |
| 10 | DT\_DOC\_SAIDA | Data da emissão do documento fiscal de saída | Data da emissão do documento fiscal de saída que originou a devolução.  (TGFC181F.DT\_DOC\_SAIDA) |
| 11 | NUM\_ITEM\_SAIDA | Número do item em que foi escriturada a saída em um registro C185, C380, C480 ou C815 quando o contribuinte informar a saída em um arquivo de perfil A. | Sequência e ou sequência fiscal do item na nota de saída que originou a devolução.  (TGFC181F.NUM\_ITEM\_SAIDA) |
| 12 | VL\_UNIT\_CONV\_SAIDA | Valor unitário da mercadoria, considerando a unidade utilizada para informar o campo “QUANT\_CONV”, correspondente ao valor do campo VL\_UNIT\_CONV, preenchido na ocasião da saída | Valor unitário da mercadoria na nota de saída que originou a devolução.  (TGFC181F.VL\_UNIT\_CONV\_SAIDA) |
| 13 | VL\_UNIT\_ICMS\_OP\_EST OQUE\_CONV\_SAIDA | Valor médio unitário do ICMS OP, das mercadorias em estoque, correspondente ao valor do campo VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV, preenchido na ocasião da saída | Valor médio unitário do ICMS OP na nota de saída que originou a devolução.  (TGFC181F.VL\_UNIT\_ICMS\_OP\_EST\_CONV\_S) |
| 14 | VL\_UNIT\_ICMS\_ST\_EST OQUE\_CONV\_SAIDA | Valor médio unitário do ICMS ST, incluindo FCP ST, das mercadorias em estoque, correspondente ao valor do campo VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV, preenchido na ocasião da saída | Valor médio unitário do ICMS ST na nota de saída que originou a devolução.  (TGFC181F.VL\_UNIT\_ICMS\_ST\_EST\_CONV\_S) |
| 15 | VL\_UNIT\_FCP\_ICMS\_ST\_ ESTOQUE\_CONV\_SAIDA | Valor médio unitário do FCP ST agregado ao ICMS das mercadorias em estoque, correspondente ao valor do campo VL\_UNIT\_FCP\_ICMS\_ST\_ESTOQUE\_CON V, preenchido na ocasião da saída | Valor médio unitário do FCP ST na nota de saída que originou a devolução.  (TGFC181F.VL\_UNIT\_FCP\_ICMS\_ST\_EST\_CONV\_S) |
| 16 | VL\_UNIT\_ICMS\_NA\_OPE RACAO\_CONV\_SAIDA | Valor unitário para o ICMS na operação, correspondente ao valor do campo VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV, preenchido na ocasião da saída | Valor unitário para o ICMS na operação da nota de saída que originou a devolução.  (TGFC181F.VL\_UNIT\_ICMS\_NA\_OP\_CONV\_S) |
| 17 | VL\_UNIT\_ICMS\_OP\_CON V\_SAIDA | Valor unitário do ICMS correspondente ao valor do campo VL\_UNIT\_ICMS\_OP\_CONV, preenchido na ocasião da saída | Valor unitário do ICMS correspondente ao valor do campo VL\_UNIT\_ICMS\_OP\_CONV, preenchido na ocasião da saída que originou a devolução.  (TGFC181F.VL\_UNIT\_ICMS\_OP\_CONV\_SAIDA) |
| 18 | VL\_UNIT\_ICMS\_ST\_CON V\_REST | Valor unitário do total do ICMS ST, incluindo FCP ST, a ser restituído/ressarcido, correspondente ao estorno do complemento apurado na operação de saída. | Valor unitário do total do ICMS ST, incluindo FCP ST, a ser restituído/ressarcido, correspondente ao estorno do complemento apurado na operação de saída.que originou a devolução  (TGFC181F.VL\_UNIT\_ICMS\_ST\_CONV\_REST) |
| 19 | VL\_UNIT\_FCP\_ST\_CONV \_REST | Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo “VL\_UNIT\_ICMS\_ST\_CONV\_REST”, considerando a unidade utilizada para informar o campo “QUANT\_CONV”. | Valor unitário correspondente à parcela de ICMS FCP ST preenchido na ocasião da saída que originou a devolução.  (TGFC181F.VL\_UNIT\_FCP\_ST\_CONV\_REST) |
| 20 | VL\_UNIT\_ICMS\_ST\_CON V\_COMPL | Valor unitário do estorno do ressarcimento/restituição, incluindo FCP ST, apurado na operação de saída | Valor unitário do estorno do ressarcimento/restituição, incluindo FCP ST, apurado na operação de saída que originou a devolução. (TGFC181F.VL\_UNIT\_FCP\_ST\_CONV\_COMPL) |
| 21 | VL\_UNIT\_FCP\_ST\_CONV \_COMPL | Valor unitário correspondente à parcela de ICMS FCP ST que compõe o campo “VL\_UNIT\_ICMS\_ST\_CONV\_COMPL”, considerando unidade utilizada para informar o campo “QUANT\_CONV”. |  |

**Exemplos:**

|C100|0|0|000000006|55|00|010|110119|31210899999999000191550100001101192596847940|23082021|23082021|3,45|0|0,00|0,00|3,45|1|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|||||

|C170|1|4||1,00000|UN|3,45|0,00|0|060|1411|1200|0,00|0,00|0,00|0,00|0,00|0,00||||0,00|0,00|0,00||||||||||||||0,00|

|C181|**MG600**|1,000000|UN|55||||31210899999999000191550100001101162270001028|23082021|1|3,450000|0,318000|0,390342|0,000000|0,000000||||0,390342|0,000000|

|C190|060|1411|0,00|3,45|0,00|0,00|0,00|0,00|0,00|0,00||

|C100|0|0|000000006|55|00|010|110121|31210899999999000191550100001101212883402230|23082021|23082021|13,59|0|0,00|0,00|12,35|1|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|||||

|C170|1|4||1,00000|UN|12,35|0,00|0|060|1411|1200|0,00|0,00|0,00|0,00|0,00|0,00|0|00||0,00|0,00|0,00||||||||||||||0,00|

|C181|**MG800**|1,000000|UN|55||||31210899999999000191550100001101202536633651|23082021|1|12,350000|0,318000|0,390342|0,000000|0,000000||-0,708342|0,000000|||

|C190|060|1411|0,00|13,59|0,00|0,00|0,00|0,00|0,00|0,00||

**Registros H005, H010 e H030 - Inventário motivo 06 - Para controle das mercadorias sujeitas ao regime de substituição tributária – restituição/ ressarcimento/ complementação.**

**Observação:** Para gerar as informações de quantidade do registro H005 e filhos do EFD Fiscal, o produto tem que ter custos calculados, por isso é importante dar atenção aos os valores de custo médio do produto na tabela TGFCUS.

Na geração dos registros **H005**, **H010** e **H030**, serão considerados os itens cujo o “Tipo de Substituição” igual a “Subst. na compra e na venda” e ou “Revenda com subst. tributária (cálculo de Subst. na compra)”, que tenham gerado registros do tipo **C180** e **C185** e que estejam presentes no inventário informado no campo **"Data do Inventário"** da guia **"Restituição/Complementação de ST":**

![Imagem 8: Na geração dos registros H005 , H010 e H030 , serão considerados os itens cujo o “ Tipo de Substituição” igual a…](https://ajuda.sankhya.com.br/hc/article_attachments/5012864760983)

O sistema deve gerar um registro **H005** com motivo 06 (para controle das mercadorias sujeitas ao regime de substituição tributária – restituição/ressarcimento/complementação), junto aos registros **H010** e **H030** dos itens gerados nos registros **C180** e **C185**.

**Nota:** A partir de janeiro de 2020, todos os itens que forem declarados nos registros C180, C185, C330, C380, C430, C480, C815 e C870 devem ter pelo menos um registro H010, sob um registro H005 com o campo 04 “MOT\_INV” = “06” (controle das mercadorias sujeitas ao regime de substituição tributária – restituição/ ressarcimento/ complementação). Esta regra não se aplica quando o campo 03 (VL\_INV) do registro H005 for igual a “0” (zero). A partir de janeiro de 2021, aplica-se a regra para os registros C181 e C186.

**Regras de Preenchimento dos campos no registro H030**

| **Nº** | **Campo** | **Descrição** | **Regra geração/Origem valores** |
| --- | --- | --- | --- |
| 1 | REG | Texto fixo contendo "H030" |  |
| 2 | VL\_ICMS\_OP | Valor médio unitário do ICMS OP | Valor médio unitário do ICMS OP obtido na tabela de valores medios para restituição de ST.  (TGFEFDVMRSTDIA.VLRUNITMED AND TIPIMPOST='I' AND TIPMEDIA='I'  ) |
| 3 | VL\_BC\_ICMS\_ST | Valor médio unitário da base de cálculo do ICMS ST | Valor médio unitário da base de cálculo do ICMS ST obtido na tabela de valores medios para restituição de ST.  (TGFEFDVMRSTDIA.VLRUNITMED AND TIPIMPOST='B' AND TIPMEDIA='I'  ) |
| 4 | VL\_ICMS\_ST | Valor médio unitário do ICMS ST | Valor médio unitário do ICMS ST obtido na tabela de valores medios para restituição de ST.  (TGFEFDVMRSTDIA.VLRUNITMED AND TIPIMPOST='S' AND TIPMEDIA='I'  ) |
| 5 | VL\_FCP | Valor médio unitário do FCP | Valor médio unitário do FCP obtido na tabela de valores medios para restituição de ST.  (TGFEFDVMRSTDIA.VLRUNITMED AND TIPIMPOST='F' AND TIPMEDIA='I'  ) |

**Exemplo:**

|H005|31072021|3675,06|06|

|H010|4|UN|1201,000|3,060000|3675,06|0||||3675,06|

|H030|0,000000|0,000000|0,000000|0,000000|

|H010|5|UN|0,000|0,000000|0,00|0|||||

|H030|0,000000|0,000000|0,000000|0,000000|

Caso ocorra situações em que alguns dos itens presentes nas movimentações (registros C180, C181, C185, C186, etc), não possuam registro no inventário, o sistema deve inserir um registro H010 e um registro H030 com os valores zerados, apenas para registro de que esses itens não tiveram inventário. Pois, de acordo com o manual EFD, quando o valor total do H005 é maior do que zero, devemos ter no mínimo um H010 e H030 para cada produto presente nas movimentações. 

No exemplo a seguir, digamos que apenas o produto 4 tinha inventário, logo os demais produtos devem ter registros zerados.

**Exemplo:**

|H005|31072021|3675,06|06|

|H010|4|UN|1201,000|3,060000|3675,06|0||||3675,06|

|H030|0,000000|0,000000|0,000000|0,000000|

|H010|5|UN|0,000|0,000000|0,00|0|||||

|H030|0,000000|0,000000|0,000000|0,000000|

|H990|3|

Caso não seja encontrado nenhum item que satisfaça as condições, o sistema gera o registro **H005** com o valor total zerado e, de acordo com o manual do EFD, neste caso, não existe a obrigatoriedade de geração dos registros **H010** e **H030.** Sendo então gerado no arquivo apenas a abertura e fechamento do bloco.

**Exemplo:**

|H001|0|

|H005|31012020|0|06|

|H990|3|

**Registros 1250 e 1255 - Informações consolidadas de saldos de restituição, ressarcimento e complementação do ICMS.**

As informações consolidadas dos valores a restituir no registro 1250 são gerados a partir dos valores declarados no registro 1255, já os valores declarados no registro 1255 são gerados a partir dos valores acumulados dos registros C181, C185 e C430.

**Exemplos:**

**- Fato Gerador Presumido Não Realizado**

|1250|5,70|6,98|0,00|0,00|0,00|

|1255|MG200|5,70|6,98|0,00|0,00|0,00|

**- Aspecto Quantitativo**

|1250|1,92|0,07|0,00|1,03|0,00|

|1255|MG800|0,32|0,71|0,00|0,00|0,00|

|1255|MG600|0,32|0,00|0,00|0,39|0,00|

|1255|MG300|0,64|0,00|0,00|1,42|0,00|

|1255|MG100|0,64|0,78|0,00|0,00|0,00|

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16252975976727) OBSERVAÇÃO:**

Não foram implementados os registros C330, C380, C480.
