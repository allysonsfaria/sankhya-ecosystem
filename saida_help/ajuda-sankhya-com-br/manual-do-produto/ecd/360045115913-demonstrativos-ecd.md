---
id: "360045115913"
titulo: "Demonstrativos ECD"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > ECD"
atualizado_em: "2026-09-15T17:42:34Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "ECD", "Padrão", "Histórico", "Contabilidade", "ACUMULADOS", "Balanço Patrimonial", "DEMONSTRAÇÃO", "Demonstrativos ECD", "DFC", "DLPA", "DMPL", "DRA", "DRE", "LÍQUIDO", "LUCROS", "MUTAÇÕES", "PATRIMÔNIO", "PREJUÍZOS", "br.com.sankhya.contab.mov.demonstrativoecd", "Demonstrativos ECD manual", "SPED Contábil"]
---

# Demonstrativos ECD

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42314939367703) Módulo: Contabilidade > Conexão > ECD > Configuração P/ ECD
```

---

O objetivo da tela **"Demonstrativos ECD"** é permitir a configuração da estrutura das Demonstrações Contábeis, que são necessárias para geração de Registros que irão compor o SPED Contábil, de modo a evidenciar as Demonstrações Contábeis das Empresas obrigadas a transmitirem o ECD.

Inicialmente para construção e posterior consulta dos Demonstrativos Contábeis, ao acessar a tela é necessário através do link localizado no lado superior esquerdo da tela, **"Clique para selecionar uma empresa"**, definir a empresa para a qual será realizada a configuração.

Dividimos a composição das Demonstrações Contábeis em quatro abas. A saber:

| [Aba Balanço Patrimonial](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#ababalanopatrimonial) | [Aba DRE/DRA](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#abadredra) |
| --- | --- |
| [Aba Fatos DMPL/DLPA](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#abafatosdmpldlpa) | [Aba DMPL/DLPA](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#abadmpldlpa) |
| [Aba DFC](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#abadfc) | [Copiar Estrutura de contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#copiarestruturadecontas) |
| [Botão Inserir Múltiplas Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#Bot%C3%A3oinserirm%C3%BAltiplascontas) |  |

## Aba Balanço Patrimonial

O Balanço Patrimonial é o demonstrador contábil que apresenta a posição patrimonial e financeira da empresa em um período determinado (normalmente anual). Ele avalia a posição contábil e financeira da empresa, uma vez que considera não apenas o caixa, mas também propriedades, dívidas e pagamentos a receber.

![Imagem 2: O Balanço Patrimonial é o demonstrador contábil que apresenta a posição patrimonial e financeira da empresa em um…](https://ajuda.sankhya.com.br/hc/article_attachments/360098819773)

Informe o **"Código"** aglutinador da conta.

**Observação:** O código de aglutinador será apresentado nos registros J100, J150 e também no registro I052 conforme manual SPED Contábil.

Cadastre no campo **"Descrição"** o nome da conta.

Quando a marcação **"Ativo:"** for efetuada, definirá que a conta cadastrada está ativa.

Ao selecionar a opção **"Analítico"** será indicado que o cadastro em questão é analítico.

Defina no campo **"Grupo Balanço"** a qual grupo o cadastro pertence, podendo ser ao **"Ativo"** ou **"Passivo e Patrimônio Líquido"**.

**Nota:** Na Versão de Layout 7.00 da [Geração de Arquivo - ECD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608014) o grupo Ativo será representado por **"A"** e o Passivo e Patrimônio Líquido por **"P"**.

O campo **"Grupo p/ Demonstrativo"** é utilizado na geração dos demonstrativos contábeis, atuando como uma espécie de agrupador das Contas Contábeis. Ele pode ser definido dentre as seguintes opções:

- Ativo Circulante;
- Ativo Não Circulante;
- Passivo Circulante;
- Passivo Não Circulante;
- Patrimônio Líquido.

Na parte inferior da tela, teremos como preenchimento obrigatório, o **"Código Reduzido"** da conta, com base no plano de contas da empresa. Vincula-se a(s) conta(s) contábil(eis) conforme regra da empresa.

**Observação:** O Balanço Patrimonial irá gerar dados para o registro J100.

**Importante:** Para os registros J100 e J150 tem-se no campo **"Indicador do tipo de aglutinação da linha"** do validador as opções **"T - Totalizador"** (para as contas sintéticas) e **"D - Detalhe"** (para as contas analíticas), sendo que, estes dois indicadores irão diferenciar a hierarquia das contas nos Demonstrativos ECD.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#top)

## Aba DRE/DRA

O DRE (Demonstração do Resultado do Exercício) é uma demonstração contábil destinada a evidenciar a formação do resultado líquido em um exercício, por meio do confronto das receitas, custos e resultados, apuradas segundo o princípio contábil do regime de competência. Trata-se de um relatório contábil elaborado em conjunto com o "Balanço Patrimonial", que descreve as operações realizadas pela empresa em um determinado período.

A demonstração do resultado do exercício oferece uma síntese financeira dos resultados operacionais e não operacionais da empresa. Embora sejam elaboradas anualmente para fins legais de divulgação, em geral, são feitas mensalmente para fins administrativos e trimestralmente para fins fiscais.

**Nota:** A DRE é elaborada ao mesmo tempo em que se define o **"Balanço Patrimonial"** (BP), logo não é possível conceber este relatório dissociado do "BP".

![Imagem 3: Nota: A DRE é elaborada ao mesmo tempo em que se define o "Balanço Patrimonial" (BP), logo não é possível conceber este…](https://ajuda.sankhya.com.br/hc/article_attachments/360098819993)

Informe o **"Código"** aglutinador da conta.

**Observação:** O código de aglutinador será apresentado nos registros J100, J150 e também no registro I052 conforme manual SPED Contábil.

Cadastre no campo **"Descrição"** o nome da conta.

Ao efetuar a marcação **"Ativo"**, você definirá que a conta cadastrada está ativa.

Quando a marcação **"Analítico"** estiver realizada, tem-se que o cadastro em questão é analítico.

Defina nesse campo a qual **"Situação"** o cadastro pertence, tendo-se as seguintes opções:

- Automático;
- Subtotal ou total.

Sobre o campo Situação:

- Para linhas criadas na DRE que estejam no Plano de Contas, deve-se informar a opção Automático;
- Para linhas criadas na DRE e que não estejam no Plano de Contas, informe a opção Subtotal ou total, de acordo com a natureza da conta que será apurada;
- Para as contas de aglutinação, ou seja, contas sintéticas, a configuração deste campo não poderá ser Automático e sim, Subtotal ou total.

A marcação **"Gera DRA?"** quando realizada, tem-se que a conta contábil fará parte do demonstrativo contábil da DRA.

Na parte inferior da tela, tem-se como preenchimento obrigatório, o **"Código Reduzido"** da conta, com base no plano de contas da empresa. Vincula-se a(s) conta(s) contábil(eis) conforme regra da empresa.

Para que o campo **"Grupo da DRE"** do validador do ECD seja preenchido, deve-se selecionar uma das seguintes opções no campo **"Indicador de grupo da DRE"** desta aba:

- Representa incremento do lucro, ou;
- Representa redução do lucro.

Informe o **"Número da ordem"** da linha na visualização do Demonstrativo.

A **"Classificação do Saldo Inicial"** e a **"Classificação do Saldo Final"** serão calculados automaticamente para a geração do registro J150, obedecendo a natureza do saldo credor ou devedor. Assim, para que a geração do registro analítico J150 siga a somatória de crédito/débito e de forma automática, o sistema informará no campo IND\_DC\_INI e IND\_DC\_INI\_MF se o resultado deu positivo (C-Credor) ou negativo (D-Devedor).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#top)

## Aba Fatos DMPL/DLPA

Fatos Contábeis são as ocorrências que alteram, qualitativa e/ou quantitativamente o Patrimônio.

![Imagem 4: Fatos Contábeis são as ocorrências que alteram, qualitativa e/ou quantitativamente o Patrimônio.](https://ajuda.sankhya.com.br/hc/article_attachments/360098820053)

Informe inicialmente o **"Código Fato Contábil"**, bem como sua descrição **(Desc. Fato Contábil)**.

Defina também, o campo **"Situação"** que possui as seguintes alternativas:

- **Automático:** É um agrupador de históricos, que de forma automática calculará o movimento do grupo de contas dentro do período de geração.
- **Subtotal ou total:** É uma linha totalizadora do somatório dos valores das linhas automáticas anteriores, acrescido do saldo inicial do grupo de contas.

Através do campo **"Tipo"**, determine o tipo do saldo a ser apresentado no demonstrativo dentre as seguintes opções:

- Saldo inicial;
- Saldo final;
- Normal.

No campo **"Cód. do Histórico Padrão"** serão informados os respectivos históricos que compõem os Fatos Contábeis.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#top)

## Aba DMPL/DLPA

A **DMPL** - Demonstrações de Mutações do Patrimônio Líquido, faz a indicação do fluxo de uma conta para outra, a origem e o valor de cada acréscimo ou diminuição no Patrimônio Líquido (PL) durante o período. Tem por finalidade apresentar as alterações que ocorreram no PL da empresa em determinado exercício, trata-se de uma demonstração mais completa e abrangente, uma vez que evidencia a movimentação de todas as contas do patrimônio líquido, inclusive a formação e utilização das reservas não derivadas do lucro. São informações que complementam o Balanço Patrimonial e a Demonstração de Resultados.

A **DLPA** - Demonstração de Lucros ou Prejuízos Acumulados,  destaca as alterações ocorridas no saldo das contas de lucros ou prejuízos acumulados, no Patrimônio Líquido. Exibe o resultado da empresa e as alterações nos lucros ou prejuízos acumulados para o período de divulgação.

A DLPA discriminará:

1. Saldo do início do período e ajustes de exercícios anteriores;

2. Reversões de reservas e lucro líquido do exercício;

3. Transferências para reservas, dividendos, a parcela dos lucros incorporada ao capital e o saldo ao fim do período;

4. Montante do dividendo por ação do capital social.

**Importante:** As informações apresentadas na DLPA fazem parte da DMPL, ou seja, a DLPA é uma das colunas da DMPL.

![Imagem 5: Importante: As informações apresentadas na DLPA fazem parte da DMPL, ou seja, a DLPA é uma das colunas da DMPL.](https://ajuda.sankhya.com.br/hc/article_attachments/360098820373)

Informe o **"Código"** aglutinador da conta.

Cadastre no campo **"Descrição"** o nome da conta.

A marcação **"Ativo"** quando efetuada, definirá que a conta cadastrada está ativa.

A marcação **"Agrupamento p/ DLPA"** definirá se a conta cadastrada irá representar a DLPA.

**Observações:**

- Se a marcação Agrupamento p/ DLPA estiver realizada, o sistema gerará o demonstrativo como DLPA; caso contrário, se não estiver marcada, será gerado o demonstrativo como DMPL;
- Se você não marcar o Agrupamento p/ DLPA, será gerado o registro J210 com o código 1; e, se você marcar o Agrupamento p/ DLPA, será gerado o registro J210 com o código 0.

Mais abaixo na tela, tem-se como preenchimento obrigatório, o **"Código Reduzido"** da conta, com base no plano de contas da empresa. Vincula-se a(s) conta(s) contábil(eis) conforme regra da empresa.

Os lançamentos efetuados nestas contas, obrigatoriamente deverão possuir **"Histórico Padrão"** informado, para que seja possível gerar as demonstrações. A falta desta informação em algum lançamento, provocará uma inconsistência nos saldos.

**Nota:** Estas informações geram registros J210 e são utilizados na geração do J215.

**REGISTRO J210:** DLPA – Demonstração de Lucros ou Prejuízos Acumulados / DMPL – Demonstração De Mutações do Patrimônio Líquido.

**REGISTRO J215:** Fato Contábil que altera a conta Lucros Acumulados ou a conta Prejuízos Acumulados ou todo o Patrimônio Líquido.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#top)

## Aba DFC

![Imagem 6: Aba DFC](https://ajuda.sankhya.com.br/hc/article_attachments/4413465260439)

Informe obrigatoriamente o **"Código"** aglutinador da conta.

Preencha o campo **"Descrição"** com o nome da conta.

A marcação **"Ativo"** quando efetuada, definirá que a conta cadastrada está ativa.

Quando a marcação **"Analítico"** estiver realizada, tem-se que o cadastro em questão é analítico.

A marcação **"Inverter valor automático"** terá impacto para o cálculo do saldo no seu respectivo Demonstrativo Contábil.

O campo **"Grupo p/ Demonstrativo"** é utilizado na geração dos demonstrativos contábeis, atuando como uma espécie de agrupador das Contas Contábeis. Ele pode ser definido dentre as seguintes opções:

- Atividades Operacionais;
- Atividades De Investimento;
- Atividades De Financiamento;
- Outras Atividades;
- Totalizador das Atividades Principais.

O campo **"Situação"** afetará na geração do demonstrativo, possuindo as seguintes opções:

- Saldo Inicial;
- Saldo Final;
- Saldo do Movimento;
- Subtotal ou total.

Na parte inferior da tela, tem-se como preenchimento obrigatório, o **"Código Reduzido"** da conta, com base no plano de contas da empresa. Vincula-se a(s) conta(s) contábil(eis) conforme regra da empresa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#top)

## Copiar Estrutura de contas

Esta opção está localizada no alto da tela e, ao acioná-la, apresenta-se o seguinte pop-up:

![Imagem 7: Esta opção está localizada no alto da tela e, ao acioná-la, apresenta-se o seguinte pop-up:](https://ajuda.sankhya.com.br/hc/article_attachments/360098820453)

No campo **"Empresa destino"** insere-se a empresa para a qual deseja-se copiar a estrutura de contas.

**Observação:** A Empresa destino deverá ser uma empresa dona do Plano de Contas e este deve ser diferente do Plano de Contas da empresa selecionada na tela inicial.

Seleciona-se no campo **"Demonstrativo"** qual o tipo de relatório deseja-se copiar.

A marcação **"Substituir registros já existentes"** quando realizada, substituirá os registros cadastrados na Empresa destino caso os mesmos existam.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#top)

## Botão Inserir Múltiplas Contas

Nas abas [Balanço Patrimonial](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#ababalanopatrimonial), [DRE/DRA](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#abadredra), [DMPL/DLPA](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#abadmpldlpa) e [DFC](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#abadfc), por meio do botão ![Imagem 8: Nas abas Balanço Patrimonial , DRE/DRA , DMPL/DLPA e DFC , por meio do botão "Inserir Múltiplas Contas" , você pode…](https://ajuda.sankhya.com.br/hc/article_attachments/4412879700759) **"Inserir Múltiplas Contas"**, você pode adicionar mais de uma de conta de uma só vez, conforme sua preferência.

Para isso, basta pressionar o botão **"Ctrl"** do seu teclado e clicar nas contas que deseja adicionar:

[GIF animado: Imagem 9: Para isso, basta pressionar o botão "Ctrl" do seu teclado e clicar nas contas que deseja adicionar:](https://ajuda.sankhya.com.br/hc/article_attachments/4412879705111)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#top)
