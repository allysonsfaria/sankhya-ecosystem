---
id: "360044608034"
titulo: "Geração de Blocos para Integração - ECF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608034-Gera%C3%A7%C3%A3o-de-Blocos-para-Integra%C3%A7%C3%A3o-ECF"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > ECF (Escrituração Contábil Fiscal)"
atualizado_em: "2026-09-15T17:32:37Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "ECF", "SPED", "RFB", "br.com.sankhya.contab.mov.geracaoblocosintegracao", "Geração de Blocos para Integração - ECF manual", "Integração", "Contabilidade", "Geração de Blocos para Integração na ECF: Processo e Configurações"]
---

# Geração de Blocos para Integração - ECF

```
![módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42314971056535) Módulo: Contabilidade > Conexão > ECF
```

---

O objetivo desta tela é realizar a geração de blocos que serão integrados através da importação pelo PVA da ECF e através destes finalizar o processo.

Algumas informações e registros deverão ser alimentados diretamente no PVA e outros são calculados automaticamente por ele. Também é feita a recuperação dos dados da ECF entregue pela empresa, necessária para fechamento e envio da obrigação.

O sistema gerará todo o bloco 0 com os registros 0000, 0010, 0020, 0030, 0035, 0930 e 0990 conforme exigência e layout definido pelo Manual de Orientação da RFB. De acordo com as configurações do módulo Contabilidade/W serão gerados os registros M001, M030, M300, M310, M312 e M990 relativos à Parte A do e-Lalur.

**Importante:** para que o campo "03 - CNAE\_FISCAL" seja preenchido no Registro 0030 da ECF, é necessário que o CNAE da empresa esteja informado no campo **"Atividade Econômica"** na aba [Naturezas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas#abanaturezas) do [Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas#top).

Caso tenham sido configurados os Blocos: N, P, T, U, X e Y com seus respectivos registros, através da rotina de configurador de blocos e registros estes serão gerados durante o processo. Os registros de abertura e encerramento destes blocos serão gerados pelo sistema. A primeira etapa foi a parte relacionada aos cadastros e a importação das tabelas dinâmicas que pode ser encontrada em [Geração do ECD - ECF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597794). Esta segunda etapa visa a geração propriamente dita do arquivo. Os cadastros realizados serão consumidos para tal geração.

Também serão gerados os blocos 9001, 9900, 9990 e 9999 de encerramento do arquivo, inclusive os relativos aos Blocos e Registros que você configurou. Para maiores detalhes sobre o layout sobre a ECF definido pela Receita federal Brasileira acesse <http://sped.rfb.gov.br/pasta/show/1644>. Dessa forma, teremos:

| Funcionalidades da tela | |
| --- | --- |
| [Botões do topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608034-Gera%C3%A7%C3%A3o-de-Blocos-para-Integra%C3%A7%C3%A3o-ECF#bot%C3%B5esdotopodatela) | |
| [Atualização das tabelas dinâmicas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608034-Gera%C3%A7%C3%A3o-de-Blocos-para-Integra%C3%A7%C3%A3o-ECF#atualiza%C3%A7%C3%A3odastabelasdin%C3%A2micas) | |
| [Parâmetros de geração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608034-Gera%C3%A7%C3%A3o-de-Blocos-para-Integra%C3%A7%C3%A3o-ECF#par%C3%A2metrosdegera%C3%A7%C3%A3o) | |

Selecione a **"Empresa"** para a qual se deseja gerar os blocos e o **"Período"** das informações.

**Nota:** deverá estar dentro de um mesmo ano.

- Deverá contemplar todo o período do exercício contábil;
- Caso a empresa tenha iniciado suas atividades em data diferente do início do ano, a data inicial deverá ser a mesma data;
- No caso de situação especial já informada para a ECD (fusão, cisão, incorporação ou extinção o sistema automaticamente fará o ajuste da data final).

![Imagem 2: No caso de situação especial já informada para a ECD (fusão, cisão, incorporação ou extinção o sistema automaticamente…](https://ajuda.sankhya.com.br/hc/article_attachments/18951550469399)

### Botões do topo da tela

Ao mandar gerar o arquivo por meio do botão ![GERAR](https://ajuda.sankhya.com.br/hc/article_attachments/15437896563095) **"Gerar Arquivo"**, um pop up de acompanhamento do processo será mostrado na tela.

![Imagem 4: Ao mandar gerar o arquivo por meio do botão "Gerar Arquivo" , um pop up de acompanhamento do processo será mostrado na…](https://ajuda.sankhya.com.br/hc/article_attachments/13002640159255)

**Baixar Arquivo:** Ao finalizar a geração, você poderá baixar o arquivo gerado.

**Parar:** Durante a execução da geração pode-se parar a mesma a qualquer momento;

**Ver Histórico:** O pop-up mudará sua face para que possa ser verificado o históricos das gerações.

![Imagem 5: Ver Histórico: O pop-up mudará sua face para que possa ser verificado o históricos das gerações.](https://ajuda.sankhya.com.br/hc/article_attachments/13002680407063)

Em Ver Histórico é possível baixar o arquivo gerado que foi finalizado ou verificar quais os processos em que houve erro.

**Importante:** ao finalizar a geração do arquivo os mesmos estarão salvos no repositório de arquivos no seguinte caminho: Contabilidade / ECF.

![Imagem 6: Importante: ao finalizar a geração do arquivo os mesmos estarão salvos no repositório de arquivos no seguinte caminho:…](https://ajuda.sankhya.com.br/hc/article_attachments/13002743202839)

Ao clicar-se no botão ![Ref.](https://ajuda.sankhya.com.br/hc/article_attachments/15437897615255) **"Rel. c/ Plano de Cta Ref."**, o sistema irá apresentar um relatório informando as contas contábeis sem relacionamento com Plano de Contas Referencial ou que foram cadastradas incorretamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608034-Gera%C3%A7%C3%A3o-de-Blocos-para-Integra%C3%A7%C3%A3o-ECF#tamb%C3%A9m)

### Atualização das tabelas dinâmicas

Pela tela **Geração de Blocos para Integração - ECF** também será possível realizar a atualização das tabelas dinâmicas da mesma forma que ocorre pelas telas [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116393), [Plano de Contas Referencial](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116353) e [Configurador de Blocos e Registros - ECF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116493).

O processo de atualização funciona da mesma forma. Ao acessar a tela, se houver arquivo zipado no **Repositório de Arquivos** (Contabilidade > ECF > Tabelas Dinâmicas), o sistema irá lançar o pop-up de atualização e o usuário não poderá fechá-lo. Será necessário aguardar a finalização do processo para continuar com a utilização da tela.

Nas demais telas, caso você esteja com alguma outra tela aberta e o processo de atualização for iniciado em outra tela ou por outro usuário, as telas que fazem atualização estarão com o processo de atualização ativo. Se você clicar no botão **"Atualizações Sped ECF"**, o pop-up com o processo de atualização será lançado. Contudo, nesta tela, **Geração de Blocos para Integração**, este processo não ocorrerá dessa forma. E caso você faça a solicitação da geração do arquivo, o monitoramento da atualização irá parar, e irá voltar somente depois que o usuário fechar o Pop-Up de Processos da geração do arquivo.

Conforme manual do ECF, foram atualizadas as tabelas dinâmicas do ECF para os modelos:
**Arquivo:** “Tabelas\_Dinamicas\_ECF\_Leiaute\_11\_AC2024\_SIT\_ESP\_2025.xlsx”, acessível no link: [Manuais](http://sped.rfb.gov.br/pasta/show/1644)

- **Regras de validação das tabelas dinâmicas:**

Arquivos **“SPEDECF\_DINAMICO\_2021$SPEDECF\_DINAMICA\_AAAA\_REGRAS”** disponíveis no diretório:

```
C:\Arquivos de Programas RFB\Programas SPED\ECF\recursos\tabelas
```

Para mais informações sobre utilização e atualização das Tabelas Dinâmicas, acesse o tópico **Atualização das Tabelas Dinâmicas em** [Geração do ECD - ECF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597794-Gera%C3%A7%C3%A3o-do-ECD-ECF).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608034-Gera%C3%A7%C3%A3o-de-Blocos-para-Integra%C3%A7%C3%A3o-ECF#tamb%C3%A9m)

### Parâmetros de geração

**Tipo ECF:** Este campo pode ser definido dentre as seguintes opções:

- **Original:** Opção utilizada quando o arquivo for origem a ser enviado para RFB.
- **Retificadora:** Opção utilizada quando já foi enviado um arquivo original a RFB e que precisa realizar a retificação deste arquivo com correção de registros gerados e/ou novas informações.
- **Original com mudança de forma de tributação:** Só pode ser utilizada essa opção, quando a retificação se refere ao regime de tributação nos casos previstos na legislação.

**Número do Recibo da ECF a Ser Retificada:**  Será digitado pelo usuário com até 41 dígitos (Números e Letras). O campo estará disponível para digitar, caso o tipo de ECF seja diferente de Original.

**Indicador de Situação Início do Período:** Combo Box, com as seguintes opções:

- **0** - Regulador (Início no primeiro dia do ano);
- **1** - Abertura (Início de atividades no ano-calendário);
- **2** - Resultante de Cisão/Fusão ou remanescente de cisão, ou realizou incorporação;
- **3** - Resultante de Mudança de Qualificação da Pessoa Jurídica;
- **4** - Início de obrigatoriedade da Entrega no ano-calendário;
- **5** - Resultante de desenquadramento como imune ou isenta do IRPJ);
- **6** - Realizou incorporação ou remanescente de cisão parcial.

Estas opções são utilizadas para casos em que a empresa teve alguma situação especial no período da geração do arquivo, devendo ser de responsabilidade da contabilidade da empresa que estiver gerando o arquivo, escolher qual opção será utilizada.

**% Patrimônio Remanescente (Cisão):** Informar neste campo um percentual de 0 a 100, referente ao percentual de  Patrimônio Remanescente, em casos de cisão entre empresas.

**Versão do Layout:** após o preenchimento da Empresa e do Período nesta tela, o campo Versão do Layout apresentará a versão do arquivo do respectivo ano, assim ao **“Gerar Arquivo”** um arquivo txt contendo a versão layout no registro 0000 será gerado.

Estão disponíveis as seguintes versões:

- 0001 - Ano-Calendário 2014 e Sit. Especial 2015;
- 0002 - Ano-Calendário 2015 e Sit. Especial 2016;
- 0003 - Ano-Calendário 2016 e Sit. Especial 2017;
- 0004 - Ano-Calendário 2017 e Sit. Especial 2018;
- 0005 - Ano-Calendário 2018 e Sit. Especial 2019;
- 0006 - Ano-Calendário 2019 e Sit. Especial 2020;
- 0007 - Ano-Calendário 2020 e Sit. Especial 2021;
- 0008 - Ano-Calendário 2021 e Sit. Especial 2022;
- 0009 - Ano-Calendário 2022 e Sit. Especial 2023;
- 0010 - Ano-calendário 2023 e Sit. Especial 2024;
- 0011 - Ano Calendário 2024 e Sit Especial 2025.

A partir da versão 0003 do layout, na geração da ECF caso seja encontrada uma situação com um dos seguintes códigos 7 - Transformação ou 0 - Transferência de Sede, o registro 0000, campo 07 - SIT\_ESPECIAL será preenchido igual a "0" Normal. Nos casos em que se tem situações especiais na ECF, o sistema altera a data final para geração do arquivo considerando a data da situação especial.

A partir de 01/01/2017, tem-se a versão de layout 0004. Nesta versão, alguns registros sofrem modificações. O Registro 0000, campo 03, será gerado de acordo com a versão do layout. Vejamos um exemplo de geração do registro:

|0000|LECF|0004|25650383000174|GESTÃO CONTABIL S.A|0|0|||01012017|31012017|N||1||

Ao gerar o arquivo ECF da empresa X, considerando a data inicial 01/01/2015 e a data final 31/12/2015. Caso a empresa possua uma situação especial de **"Cisão"** com início em 01/07/2015. Nesse caso, será apresentada a mensagem abaixo informando que foi alterada a data final da geração do arquivo e que o mesmo será gerado considerando novas datas:

**"Existe Cisão no período informado. Ajustando data final do período."**

**"Geração do arquivo: data inicial em 01/01/2015 e data final em 01/07/2015."**

Gerando o arquivo ECF da empresa X, levando em consideração a data inicial 01/01/2017 e a data final 31/12/2017 e a empresa, dispondo de uma situação especial de **"Transformação"** ou **"Transferência de Sede"** com início em 01/07/2017. Nesse caso, será analisado como se não houvesse uma situação especial, a mensagem não será apresentada e a geração do arquivo utilizará a data informada:

**"Geração do arquivo: data inicial em 01/01/2017 e data final em 31/12/2017"**

Além disso, o sistema valida a existência de alguma diferença entre os valores totais dos lançamentos a débito e crédito. Solicitando-se a geração do arquivo em que exista alguma divergência, será exibida a seguinte mensagem:

**"Existem erros no fechamento de D/C por dia de movimento. A ECF gerada não será validada. Deseja visualizar o relatório, gerar o arquivo mesmo assim ou cancelar a operação?"**

Ao gerar a [ECF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116493)/[ECD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607454), se existir alguma Conta Contábil que possua o grupo de contas igual a 01-Contas de ativo, 02-Contas de passivo, 03-Patrimônio líquido e 04-Contas de resultado e que teve movimento ou saldo no período, sem sua respectiva conta contábil referencial vinculada, ao clicar em **"Gerar Arquivo"**, será apresentada a seguinte mensagem:

**"Existem contas contábeis sem vínculo de contas contábeis referencias. O ECD/ECF gerado não será validado. Deseja visualizar o relatório, gerar o arquivo mesmo assim ou cancelar a operação?"**

Na geração do arquivo da ECF/ECD, caso o sistema encontre alguma inconsistência, será feita a gravação do problema no registro de log de erro que é gerado.

- Caso o arquivo gerado contenha Contas Contábeis configuradas com um dos grupos de conta definidos como 05-Contas de Compensação ou 09-Outras, existindo alguma Conta Contábil Referencial vinculada, o sistema grava a seguinte mensagem de erro no arquivo de log:

Lista de Contas Contábeis que são contas de 'Compensação' e/ou 'Outras' e possuem conta contábil referencial vinculada: 'Código da conta contábil' + 'Descrição da conta' + 'Código da Conta Contábil Referencial' de cada conta que foi encontrada para essa situação.

- Caso o arquivo gerado possua Contas Contábeis configuradas com um dos grupos de conta definidos como 05-Contas de Compensação ou 09-Outras ou que a Conta Contábil de Encerramento de Resultado da empresa que está realizando a geração, possua valor de saldo final maior que 0 (zero), o sistema irá gravar a seguinte mensagem de erro no arquivo de log:

Lista de Contas Contábeis que são contas de 'Compensação', 'Outras' e 'Conta de Encerramento de Resultado' possuem valor de saldo final. Apresentar o 'Código da conta contábil' + 'Descrição da conta' + 'Data de Referência' em que a conta possui o saldo para cada conta.

**Gerar J100 apenas de centros de resultado com movimento ou saldo?:** quando a marcação estiver habilitada, o sistema validará e guardará apenas os Centros de Resultados que tenham movimentações ou saldo inicial/final dentro do período gerado, para assim descarregá-los no registro J100. Ou seja, somente os centros de resultados utilizados na elaboração do arquivo devem ser gerados no registro.

![Imagem 8: Só será possível habilitar esta marcação se a empresa da geração do arquivo utilizar Centro de Resultado em sua…](https://ajuda.sankhya.com.br/hc/article_attachments/18951550475031)  Só será possível habilitar esta marcação se a empresa da geração do arquivo utilizar Centro de Resultado em sua contabilidade, ou seja, é necessário que a marcação **"Utiliza Centro de resultado"** da tela Empresa, aba [Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa#abalanamentos) esteja ativada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608034-Gera%C3%A7%C3%A3o-de-Blocos-para-Integra%C3%A7%C3%A3o-ECF#tamb%C3%A9m)
