---
id: "360044608014"
titulo: "Geração de Arquivo - ECD"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608014-Gera%C3%A7%C3%A3o-de-Arquivo-ECD"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > ECD"
atualizado_em: "2026-09-15T17:42:16Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "ECD", "Fiscal", "Receita Federal", "Geração", "Arquivo", "Contabilidade", "br.com.sankhya.contab.mov.geracaoarquivoecd", "Geração de Arquivo - ECD manual", "Geração de Arquivo da ECD: Configuração e Processo de Geração", "Documentos Eletrônicos"]
---

# Geração de Arquivo - ECD

```
 Módulo: Contabilidade > Conexão > ECD
```

---

Por meio dessa tela realiza-se a geração do arquivo da ECD composto por seus respectivos blocos e registros. Inicialmente, define-se obrigatoriamente a **"Empresa"** e o **"Período"** de geração do arquivo.

**Observação:** ao gerar os registros I350 e I355 será necessário que a data informada no campo Período esteja de acordo com a configuração realizada na respectiva aba, caso não esteja, os registros não serão populados.

[Aba Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608014-Gera%C3%A7%C3%A3o-de-Arquivo-ECD#abaparmetros)                                                        [Botões do topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608014-Gera%C3%A7%C3%A3o-de-Arquivo-ECD#botesdotopodatela)

![Imagem 1: Aba Parâmetros Botões do topo da tela](https://ajuda.sankhya.com.br/hc/article_attachments/360069911514)

**Aba Parâmetros**

No campo **"Forma de Escrituração"** determine a que se refere a escrituração em questão. Temos duas opções:

- G = Livro Diário (Completo, sem escrituração auxiliar);
- R = Livro Diário com Escrituração Resumida (com escrituração auxiliar).

No campo **"Natureza do Livro"** informe o nome da Natureza do livro associado; sua finalidade e a que se destina o instrumento.

O campo **"Versão do Layout"** trata o formato do arquivo, respeitando sempre as atualizações encaminhadas pela Receita Federal. Sendo que, este é preenchido automaticamente de acordo com a informação do Período. Nele tem-se as seguintes versões: 

- 0004 - Ano-Calendário 2015;
- 0005 - Ano-Calendário 2016;
- 0006 - Ano-Calendário 2017;
- 0007 - Ano-Calendário 2018;
- 0008 - Ano-Calendário 2019;
- 0009 - A partir Ano-Calendário 2020.

O campo **"Ult. Instrumento Escrituração"** é somente de visualização, e apresentará o código do N.º Ordem Instrumento Escrituração (G) OU (R) acrescido de 1 ([Preferências da Empresa da Contabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa), aba Exercício). Assim, teremos o exemplo:

Se nas Preferências da Empresa da Contabilidade, aba Exercício, o campo N.º Ordem Instrumento Escrituração (G) estiver informado 7, na tela Geração de Arquivo - ECD, no campo Ult. Instrumento Escrituração será apresentado 8.

O botão **"Atualizar N.º Ordem"** localizado à frente do campo Ult. Instrumento Escrituração, quando acionado, o número de instrumento da escrituração que estiver sendo apresentado, será gravado no campo N.º Ordem Instrumento Escrituração (G) OU (R), conforme a forma de escrituração, localizado nas Preferências da Empresa da Contabilidade, aba Exercício.

Determine no campo **"Indicador de sit. Início do período"** a situação da empresa referente à geração do arquivo em relação ao início do período informado. Temos, portanto, as seguintes opções:

- 0 - Normal (Início no primeiro dia do ano);
- 1 - Abertura;
- 2 - Resultante de cisão/fusão ou remanescente de cisão, ou realizou incorporação;
- 3 - Início de obrigatoriedade da entrega da ECD no curso do ano 'calendário'.

No campo **"Indicador de existência NIRE"** selecione a situação da empresa em relação à NIRE (Número de Identificação do Registro de Empresas - registro de legalidade da empresa na Junta Comercial do Estado). Temos as alternativas a seguir:

- 0 - Empresa não possui NIRE;
- 1 - Empresa possui NIRE.

Defina no campo **"Ind. finalidade da escrituração"** a identificação do propósito da escrituração. Pode-se fazê-lo dentre as seguintes opções:

- 0 - Original;
- 1 - Substituta com NIRE;
- 2 - Substituta sem NIRE;
- 3 - Substituta com troca de NIRE.

Informe o **"Hash da escrituração subst."** apenas se o campo Ind. Finalidade da Escrituração for definido com uma opção diferente de 0 - Original.

Determine o **"NIRE da escrituração subst."** somente se o campo Indicador de existência NIRE for definido com uma opção diferente de 0 - Empresa não possui NIRE e o campo Ind. Finalidade da Escrituração for igual a 3 - Substituta com troca de NIRE.

Defina no campo **"Ind. de entidade sujeita a auditoria independente"** como é o comportamento em relação a auditoria independente. Temos as seguintes opções:

- 0 - Não sujeita a auditoria independente;
- 1 - Sujeita a auditoria independente.

A realização da marcação **"Escriturações Contábeis Consolidadas"** irá determinar a geração do Registro 0000, mais detalhadamente, o campo IND\_ESC\_CONS.

Caso você efetue a marcação **"Gerar J100, J150 e J210 somente para contas contábeis com saldo?"**, teremos a geração dos registros J100, J150 e J210, mesmo que as contas possuam saldo inicial ou final diferente de 0 (zero). Ao marcá-la, serão gerados os registros mencionados apenas se as contas possuírem saldo inicial ou final diferente de 0.

A respeito da geração do registro J150, para os campos 06 - IND\_VL - Indicador da situação do valor informado no campo anterior e 08 - IND\_VL\_ULT\_DRE - Indicador da situação do valor informado no campo anterior, teremos a seguinte definição automática para ambos:

- P - Subtotal ou total positivo;
- N - Subtotal ou total negativo.

**Observação:** Temos o parâmetro **"Calc. indicador grupo registro sintético J150 DRE - CALINGRUDREJ150"** que, quando habilitado, faz com que o sistema efetue o cálculo do campo 12 - Indicador de Grupo do Registro J50 para linhas configuradas com a marcação **"Analítico"** desmarcado, na tela [Demonstrativos ECD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913).

Se o campo 11 for igual a **"Credor"**, o campo 12 então será preenchido com **"R"**; caso contrário, será preenchido com **"D"**.

**Nota:** Quando o parâmetro estiver desabilitado, o campo 12 sempre será preenchido considerando o cadastro da tela Demonstrativos ECD, aba [DRE/DRA](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913?flash_digest=b274774eaccfab21d61141cb7a11e5d2af095e37#abadredra).

**Observação:** Para que a geração dos campos 9 e 11 do Registro J150 da linha **"Sintético"** seja preenchida considerando o cálculo das contas filhas, sendo assim, caso o cálculo do campo 8 das linhas filhas seja maior que zero, será considerado **"D"** (devedor); caso contrário considera-se **"C"** (credor). Se o cálculo do campo 10 das linhas filhas for maior do que zero, considera-se **"D"**; caso contrário, **"C"**.

Com base no saldo da conta para os aglutinadores que possuem a configuração igual a Subtotal ou Total, teremos a seguinte regra:

- Caso o saldo acumulado da conta (VL\_CTA) seja positivo, o campo IND\_VL será gerado igual a P - Subtotal ou total positivo; caso seja negativo será gerado igual a N - Subtotal ou total negativo.
- Caso o saldo acumulado da conta (VL\_CTA\_ULT\_DRE) seja positivo, o campo IND\_VL\_ULT\_DRE será gerado igual a P - Subtotal ou total positivo; caso seja negativo, será igual a N - Subtotal ou total negativo.

Quando você efetuar a marcação **"Gerar registro I200 considerando o número de documento/lançamento?"** e gerar o arquivo ECD, será gerado o **"Número do Lançamento"** no campo **"02 (NUM\_LCTO)"** do registro I200, com agrupamento mais analítico. Por outro lado, caso você não efetue a marcação, a geração do registro I200 não terá o Número do Lançamento ligado aos outros campos que compõem o campo 02 (NUM\_LCTO), tornando o agrupamento mais sintético.

Quando a marcação **"Gerar I100 apenas de centros de resultado com movimento ou saldo"** estiver habilitada, o sistema validará e guardará apenas os Centros de Resultados que tenham movimentações ou saldo inicial/final dentro do período gerado, para assim descarregá-los no registro l100. Ou seja, somente os centros de resultados utilizados na elaboração do arquivo devem ser gerados no registro.

![Imagem 2: Só será possível habilitar esta marcação, se a empresa da geração do arquivo utilizar centro de resultado em sua…](https://ajuda.sankhya.com.br/hc/article_attachments/18952075468567) Só será possível habilitar esta marcação, se a empresa da geração do arquivo utilizar centro de resultado em sua contabilidade, ou seja, é necessário que a marcação **“Utiliza Centro de resultado”** da tela [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa), aba [Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa#abalanamentos), esteja ativada.

Quando a marcação **"Gerar I050 somente para contas com movimento ou com saldo?"** estiver selecionada, fará com que, somente as contas com movimento no período de geração ou com saldo diferente de zero sejam geradas.

Com a opção **Ignorar Centro de Resultado**, você define se o arquivo da ECD será gerado com ou sem o Centro de Resultado nos registros contábeis. Ao marcar esta opção, o sistema consolida os saldos e lançamentos por conta contábil e gera o campo `COD_CCUS` vazio nos registros do SPED.

🚨 **IMPORTANTE:** Esta opção é exclusiva para empresas que já entregam a ECD sem o Centro de Resultado. Se você sempre entregou o arquivo com essa informação pelo Sankhya, **não** ative essa opção, pois a alteração pode gerar a rejeição do arquivo pela Receita Federal.

**Comportamento da marcação:**

- **Marcada:** O sistema ignora o Centro de Resultado e consolida os lançamentos de uma mesma conta contábil em um único registro. Os campos que carregam o Centro de Resultado ficam em branco.
- **Desmarcada (padrão):** A ECD é gerada com as informações de Centro de Resultado, mantendo o comportamento habitual do sistema.

**Observação:** Esta opção vem desmarcada por padrão. Caso a sua empresa já esteja parametrizada para não utilizar Centro de Resultado, a marcação será ativada e bloqueada automaticamente assim que você selecionar a empresa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608014-Gera%C3%A7%C3%A3o-de-Arquivo-ECD#top)

**Botões do topo da tela**

![GERAR](https://ajuda.sankhya.com.br/hc/article_attachments/15437812883735) **"Gerar Arquivo"** - Este botão é responsável pelo agrupamento das informações, e consequente junção destas em arquivo. Ao clicar nesse botão será aberto um pop-up denominado **"Processos"** que demonstrará o andamento do processo de geração. Nesse pop-up também será possível baixar o arquivo gerado e ver o histórico de geração.

![Imagem 4: "Gerar Arquivo" - Este botão é responsável pelo agrupamento das informações, e consequente junção destas em arquivo. Ao…](https://ajuda.sankhya.com.br/hc/article_attachments/360069916114)

![Ref.](https://ajuda.sankhya.com.br/hc/article_attachments/15437771091991) **"Rel. c/ Plano de Cta Ref."** - Ao clicar nesse botão, o sistema irá apresentar um relatório informando as contas contábeis sem relacionamento com Plano de Contas Referencial ou que foram cadastradas incorretamente.

![clip6093](https://ajuda.sankhya.com.br/hc/article_attachments/360061014834)

Além disso, o sistema valida a existência de alguma diferença entre os valores totais dos lançamentos a débito e crédito. Caso você solicite a geração do arquivo em que exista alguma divergência, será exibida a seguinte mensagem:

**"Existem erros no fechamento de D/C por dia de movimento. A ECF gerada não será validada. Deseja visualizar o relatório, gerar o arquivo mesmo assim ou cancelar a operação?"**

Ao gerar a [ECF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116493)/[ECD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607454), se existir alguma Conta Contábil que possua o grupo de contas igual a 01-Contas de ativo, 02-Contas de passivo, 03-Patrimônio líquido e 04-Contas de resultado e que teve movimento ou saldo no período, sem sua respectiva conta contábil referencial vinculada, ao clicar em **"Gerar Arquivo"**, será apresentada a seguinte mensagem:

**"Existem contas contábeis sem vínculo de contas contábeis referencias. O ECD/ECF gerado não será validado. Deseja visualizar o relatório, gerar o arquivo mesmo assim ou cancelar a operação?"**

Na geração do arquivo da ECF/ECD, caso o sistema encontre alguma inconsistência, será feita a gravação do problema no registro de log de erro que é gerado.

- Caso o arquivo gerado contenha Contas Contábeis configuradas com um dos grupos de conta definidos como 05-Contas de Compensação ou 09-Outras, existindo alguma Conta Contábil Referencial vinculada, o sistema grava a seguinte mensagem no arquivo de log:

**"Lista de Contas Contábeis que são contas de 'Compensação' e/ou 'Outras' e possuem conta contábil referencial vinculada: 'Código da conta contábil' + 'Descrição da conta' + 'Código da Conta Contábil Referencial' de cada conta que foi encontrada para essa situação."**

- Caso o arquivo gerado possua Contas Contábeis configuradas com um dos grupos de conta definidos como 05-Contas de Compensação ou 09-Outras ou que a Conta Contábil de Encerramento de Resultado da empresa que está realizando a geração, possua valor de saldo final maior que 0 (zero), o sistema irá gravar a seguinte mensagem no arquivo de log:

**"Lista de Contas Contábeis que são contas de 'Compensação', 'Outras' e 'Conta de Encerramento de Resultado' possuem valor de saldo final. Apresentar o 'Código da conta contábil' + 'Descrição da conta' + 'Data de Referência' em que a conta possui o saldo para cada conta."**

![Historico](https://ajuda.sankhya.com.br/hc/article_attachments/15437804885143) **"Histórico de gerações"** - O acionamento deste botão apresentará o pop-up **"Processos"**, contendo o histórico de geração do arquivo, onde será possível baixar o arquivo selecionado por meio deste pop-up; ao selecionar uma linha, o botão **"Baixar Arquivo"** ficará habilitado para utilização.

![Imagem 8: "Histórico de gerações" - O acionamento deste botão apresentará o pop-up "Processos" , contendo o histórico de geração…](https://ajuda.sankhya.com.br/hc/article_attachments/360071044233)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608014-Gera%C3%A7%C3%A3o-de-Arquivo-ECD#top)
