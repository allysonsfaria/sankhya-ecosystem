---
id: "360045115953"
titulo: "Geração ICMS/IPI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Apuração e Livros Fiscais > Escrituração dos livros"
atualizado_em: "2026-09-15T14:41:15Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Frequência", "Horários", "NF-e", "Notas", "Livros Fiscais", "Agendamento", "IPI", "Log", "ICMS", "Impostos", "Financeiro", "Canceladas", "Destinatária", "Em execução", "GERACOMERROPER", "Parado", "Redução Z", "br.com.sankhya.mgeliv.mov.geracaoicmsipi", "Geração ICMS/IPI manual", "Ajustes de empresa frequência e horários", "Notas canceladas financeiras e ajuste ICMS", "Dados ICMS/IPI automático/manual"]
---

# Geração ICMS/IPI

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313074973207) Módulo: Livros Fiscais > Arquivos
```

---

Essa rotina está destinada à geração dos dados necessários para posterior emissão dos relatórios e/ou geração dos arquivos digitais destinados ao Fisco, relacionados ao ICMS (Imposto sobre Circulação de Mercadorias e Serviços) e ao IPI (Imposto sobre Produtos Industrializados). Para essa ação é necessária a geração prévia dos lançamentos, que é um procedimento feito nessa tela.

Por meio dessa tela é efetuada a geração automática (agendamento) e/ou manual do Livro Fiscal com base nas Notas Fiscais, cujas TOP's (Tipos de Operação) foram configuradas para atualizar os Livros Fiscais (entrada ou saída).

![Imagem 2: Por meio dessa tela é efetuada a geração automática (agendamento) e/ou manual do Livro Fiscal com base nas Notas…](https://ajuda.sankhya.com.br/hc/article_attachments/13047326064151)

Para sua utilização, teremos o preenchimento automático do **"Nro. agendamento"**.

Em seguida, você deve informar uma **"Descrição"** para o procedimento/agendamento que está sendo realizado, de modo a melhor identificá-lo em meio aos processos envolvidos no módulo de Livros Fiscais.

Um campo de preenchimento essencial é a **"Empresa"** sobre a qual serão gerados os dados em questão.

A marcação **"Ativo"** determinará se o agendamento está ou não operante no processo de Geração ICMS/IPI.

Por fim, no cabeçalho da tela, defina no campo **"Tipo Execução"** como se dará o andamento do que foi ou será agendado, de acordo com as opções abaixo:

- Automático;
- Manual;
- Ambos.

**Observação:** a opção Manual é indicada para obtenção da geração imediata, sem a necessidade de aguardar o agendamento da execução.

Além disso, para realizar a geração de notas e Livros Fiscais, os parâmetros abaixo devem ser configurados da seguinte maneira:

- **Somar impostos no total da NF-e de nacionalizao - SOMAIMPNFNAC:** Desligado;
- **Imposto só em tag exclusiva em nota nacionalização - IMPTAGEXCNOTNAC:** Desligado;
- **Importação, tag vOutro da nota sem valor do ICMS e - VOUTNOTASEMICMS:** Desligado;
- **Importação, tag vOutro do item sem valor do ICMS - VOUTITEMSEMICMS:** Ligado;
- **Tratar II em NF-e Nacionalização - SUMVLRIIOUTNOTA:** Opção **"Soma II ao valor da nota"** selecionada;
- **Tratar ICMS em NF-e Nacionalização - SOMAICMSNFENAC:** Opção **"Soma ICMS ao Vlr Nota"** selecionada;
- **Tratar PIS e COFINS em NF-e Nacionalização - SOMPISCOFNFENAC:** Opção **"Soma PIS e COFINS ao vOutro do item no XML"** selecionada.

Essa tela é composta por quatro abas e dois botões, onde são realizadas as configurações de geração do arquivo.

| Funcionalidades da tela | |
| --- | --- |
| [Aba Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#abaparmetros) | [Aba Frequência Agendamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#abafrequnciaagendamento) |
| [Aba Informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#abainformaes) | [Aba Horários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#abahorrios) |
| [Cálculo do Diferencial de Alíquota...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#clculododiferencialdealquotacomicmspordentro) | [Botões - Gerar Agora | Status...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#botes-geraragorastatusconsultardocumentonogerado) |
| [Configurações do Livro de Entrada Cód. Tributação p/ notas do tipo A - Complemento](https://ajuda.sankhya.com.br/hc/pt-br/articles/27441093067799-Configura%C3%A7%C3%B5es-do-Livro-de-Entrada-C%C3%B3d-Tributa%C3%A7%C3%A3o-para-notas-do-tipo-A-Complemento) | |

## Aba Parâmetros

![Imagem 3: Aba Parâmetros](https://ajuda.sankhya.com.br/hc/article_attachments/1500003271142)

A aba Parâmetros é subdividida nas seguintes seções:

| [Seção Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#se%C3%A7%C3%A3ogeral) |  | [Seção Ações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#se%C3%A7%C3%A3oa%C3%A7%C3%B5es) |  | [Seção Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#se%C3%A7%C3%A3ofiltros) |
| --- | --- | --- | --- | --- |

---

**Seção Geral**

O campo **"Empresa Destinatária"** refere-se à empresa destino. É utilizada quando se trabalha com várias empresas mas a geração dos lançamentos é agrupada em uma única.

**Nota:** o preenchimento dos campos **"Empresa"** e **"Empresa Destinatária"** influencia na geração do arquivo da seguinte forma:

- Não sendo apresentadas informações em nenhum dos campos, a geração será feita para todas as empresas que geram livro fiscal;
- Quando somente o campo Empresa estiver preenchido, a geração será efetuada da referida empresa para ela mesma;
- Ao indicar somente o campo Empresa Destinatária, será gerado o arquivo com os dados de todas as empresas que geram livro para a empresa em questão;
- Caso ambos os campos estejam alimentados, a geração será realizada com os dados da Empresa para a Empresa Destinatária.

Para a geração do ICMS/IPI quando empresas diferentes forem informadas nos campos Descrição agendamento e Empresa Destinatária, é necessário que a Empresa Destinatária esteja cadastrada na tela [Cadastro Livro ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874) com a aba [EFD C195/C197 - D195/D197](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874-Cadastro-Livro-ICMS-IPI#abaefdc195c197c595c597d195d197) preenchida.

Ao realizar a geração dos Livros Fiscais, na qual é informada uma empresa destinatária diferente da empresa da geração do arquivo, será apresentada a seguinte mensagem na [aba Informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#abainformaes) e no log de geração do agendamento:

**"A empresa destinatária possui o plano de contas diferente da empresa de origem dos documentos fiscais. Isso pode ser incompatível com EFD Contribuições e ECD/ECF. Verifique!"**

Em **"Email para informar erros"**, você pode inserir o e-mail do responsável pela geração dos dados caso algum problema ocorra durante o processo, de modo a se obter um controle mais efetivo das ocorrências relacionadas ao procedimento.

**Observação:** quando se tratar de Notas de Transferência, configure os ajustes abaixo para que as informações relacionadas à transferência sejam apresentadas nos registros C195/C197 e D195/D197 do SPED Fiscal.

**1.** Realize na tela [Configurações Ajustes de Apuração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593), o ajuste de saída por transferência da Empresa que está emitindo a nota fiscal, e logo após, o ajuste de entrada para a Empresa que estará recebendo a nota fiscal de transferência.

**2.** Efetue nesta tela, a geração do Livro Fiscal de Saída para a Empresa que está emitindo a nota de saída por transferência, e somente depois, realize a geração do Livro Fiscal de Entrada para a Empresa que receberá esta nota.

Por meio do campo **"Gerar Ajustes"** você pode gerar e atualizar o Livro Fiscal tanto por mês completo quanto por períodos segregados dentro do mês, dessa maneira, a conciliação do Livro será efetuada de forma mais detalhada e os ajustes realizados poderão ser consultados na tela [Ajuste da Apuração de ICMS e ICMS ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607654-Ajuste-da-Apura%C3%A7%C3%A3o-de-ICMS-e-ICMS-ST). Esse campo funciona em conjunto com o parâmetro **"Permitir gerar ajustes apur. ICMS por período - PERMGERAJAICMS"** que, estando ligado influenciará nas opções abaixo: 

- **Gerar e atualizar**: Com essa opção selecionada, o sistema gera e atualiza os ajustes. Além disso, caso seja realizada alguma alteração na tela [Configurações de Ajustes de Apuração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o), aqueles que foram gerados anteriormente serão mantidos e atualizados conforme a nova configuração e, os novos ajustes do período serão incluídos.

Exemplo: PRIMEIRO PERÍODO (01 a 15): gera os ajustes do período informado.

SEGUNDO PERÍODO (16 a 30): mantém os ajustes gerados anteriormente e gera os ajustes do outro período informado.

- **Gerar e não atualizar**: Escolhendo essa opção, os ajustes do período são apenas gerados; se uma nova geração for realizada dentro do mesmo período, os novos ajustes serão gerados e os que foram gerados anteriormente não serão atualizados.
- **Não gerar**: Essa opção não irá gerar nenhum ajuste no período.

**Observação:** ao usar a opção Gerar e Atualizar com o parâmetro desligado, o sistema irá gerar uma linha pra cada nota e atualizará todos os registros independente do período selecionado.

A marcação **"Verificar divergências?"**, quando habilitada, irá analisar se há uma divergência no período informado para a geração do EFD Fiscal e se sim, exibirá uma mensagem na tela [EFD - Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263) para informá-lo da diferença de informações.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#abaparmetros)

**Seção Ações**

Nessa seção, determine os conjuntos de dados relacionados às notas que serão gerados de acordo com as seguintes marcações:

- **Gerar Notas:** Serão geradas todas as informações referentes às notas, dentro do período estabelecido.
- **Gerar Canceladas:** Com essa marcação, serão consideradas apenas as notas canceladas dentro do período definido.
- **Gerar Financeiro:** Ao selecionar essa marcação, será considerado para geração, apenas o financeiro das notas contidas no período estabelecido.
- **Gerar Redução Z:** Por essa marcação, serão gerados os fechamentos fiscais diários de um ECF (Emissor de Cupom Fiscal), uma vez que ele trabalha com base em movimentações diárias.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#abaparmetros)

**Seção Filtros**

Nesse trecho, determine qual operação será considerada para geração dos dados. Você pode marcar uma ou ambas as opções:

- Entradas;
- Saídas.

Se você marcar a opção **"Data inicial"**, o período inicial será definido a ser considerado para o começo da geração das informações. Tem-se as seguintes opções de escolha:

- Hoje;
- Últ. execução;
- 1º dia do Mês;
- Últ. dia do Mês.

De forma semelhante ao campo anterior a **"Data final"**, a definição realizada nesse campo irá estabelecer a data final para busca dos dados a serem gerados. Nele, temos as seguintes opções:

- Hoje;
- Últ. dia do Mês.

Note que, à frente de cada um dos dois últimos campos, o espaço **"somar"** que é informado em **"dias"**, ou seja, será somada à opção definida nos campos **"Data inicial"** e **"Data final"** a quantidade de dias aqui estabelecidos, para que a partir disso, sejam gerados os dados.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#abaparmetros) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#top)

## Aba Frequência Agendamento

Configure nessa aba, os horários em que os agendamentos serão executados:

![Imagem 4: Configure nessa aba, os horários em que os agendamentos serão executados:](https://ajuda.sankhya.com.br/hc/article_attachments/360102145294)

Em **"Horários"**, selecione horários de 00hs:00min à 23hs:00min. Esses horários são informados no campo **"1ª execução"**. Caso seja necessário acrescentar outros horários de execução, clique no botão  **"Adicionar um novo horário de execução"**.

Dessa forma, a hora será adicionada no campo de horários. O botão **"Remover todos os horários de execução"**, localizado logo à frente, limpará todos os horários.

Na opção **"Meses"**, você pode escolher em quais meses serão executados os agendamentos, podendo ser em todos ou em meses específicos.

Por meio dos botões **"Diário"**, **"Semanal"** e **"Mensal"** você define a periodicidade da execução do agendamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#top)

## Aba Informações

Ao iniciar a geração dos Livros Fiscais, nesta aba, em **"Log de execução"** são apresentadas as informações referentes ao resultado da geração, se nenhum problema ocorrer, quantas notas de cada conjunto foram geradas. Se algo não estiver correto para construção dos Livros, será exibido aqui o erro a ser tratado.

![Imagem 5: Ao iniciar a geração dos Livros Fiscais, nesta aba, em "Log de execução" são apresentadas as informações referentes ao…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003322461)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#top)

## Aba Horários

Nesta aba são definidos os horários referentes às execuções dos agendamentos de geração dos Livros Fiscais.

![Imagem 6: Nesta aba são definidos os horários referentes às execuções dos agendamentos de geração dos Livros Fiscais.](https://ajuda.sankhya.com.br/hc/article_attachments/1500003322441)

No campo **"Próxima execução em"**, determine a data e a hora para a execução do agendamento. Esse campo é atualizado conforme a configuração da aba [Frequência Agendamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#abafrequnciaagendamento), contudo, você poderá preenchê-lo manualmente. Após a execução do agendamento, o sistema verificará os horários da aba Frequência Agendamento e atualizará a próxima data e hora da execução por meio deste campo.

O campo **"Data Final de Execução"** também é um campo de data e hora, onde você poderá limitar a data e hora da última execução do agendamento. A partir da data e hora colocadas nesse campo, o agendamento não será mais executado. Esse método é uma forma de limitar o período de execução.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#top)

## Cálculo do Diferencial de Alíquota com ICMS por Dentro

Na rotina de Geração ICMS/IPI, ao gerar notas que contenham as configurações para o Cálculo do Diferencial de Alíquota nas compras, o sistema irá verificar qual o cálculo configurado nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) (aba [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abageraoicmsipi), campo **"Método para Calcular Diferencial de Alíquota"**), sendo que, para cada opção, teremos os seguintes cálculos e respectivos comportamentos:

- **Dif. de Alíq. - Cálculo Padrão:**

```
 ![Imagem 7: Dif. de Alíq. - Cálculo Padrão:](https://ajuda.sankhya.com.br/hc/article_attachments/42313057877399) (Valor ICMS interno sobre o valor da operação) - (Valor ICMS destacado)
```

O cálculo acima será realizado o cálculo que é feito normalmente pelo sistema.

- **Dif. entre Alíq. sobre Valor da Operação:**

```
 ![Imagem 8: Dif. entre Alíq. sobre Valor da Operação:](https://ajuda.sankhya.com.br/hc/article_attachments/42313057877399)  ((% ICMS interno) - (% ICMS destacado)) sobre o valor da operação
```

Este será efetuado o cálculo mencionado.

- **Dif. entre Alíq. sobre Valor da BC:**

```
 ![Imagem 9: Dif. entre Alíq. sobre Valor da BC:](https://ajuda.sankhya.com.br/hc/article_attachments/42313057877399) ((% ICMS interno) - (% ICMS destacado)) sobre a Base de Cálculo
```

Será realizado o cálculo citado.

- **Dif. de Alíq. - ICMS por dentro, sem Red. da BC:**

```
 ![Imagem 10: Dif. de Alíq. - ICMS por dentro, sem Red. da BC:](https://ajuda.sankhya.com.br/hc/article_attachments/42313057877399)  (((Vlr. Operação – Vlr. ICMS Destacado) / (1 - % ICMS Interno)) x % ICMS Interno)
             - Vlr. ICMS Destacado
```

Tem-se aqui o novo cálculo com ICMS por dentro, e o sistema irá calcular exatamente por esta fórmula.

- **Dif. de Alíq. - ICMS por dentro, sob diferença entre Alíquotas:**

```
 ![Imagem 11: Dif. de Alíq. - ICMS por dentro, sob diferença entre Alíquotas:](https://ajuda.sankhya.com.br/hc/article_attachments/42313057877399) (((Vlr. Operação - Vlr. ICMS Destacado) / (1 - % Alíq. Interna Destino)) x
           (% Alíq. Interna Destino - % Alíq. ICMS)
```

- **Dif. de Alíq. - ICMS por dentro, e com redução do valor de ST**

```
 ![Imagem 12: Dif. de Alíq. - ICMS por dentro, e com redução do valor de ST](https://ajuda.sankhya.com.br/hc/article_attachments/42313057877399) ((((Valor da Mercadoria + IPI Destacado na Nota + Despesas acessórias destacadas
             na nota + Frete Destacado na nota - Desconto destacado na nota) - ICMS destacado
             na nota)/(100 - Aliq. Interna)) * (Aliq.Interna - Aliq. Interestadual)) - Vlr ICMS ST.
```

- **Dif. de Alíq. - ICMS por dentro, com exclusão do IPI:**

```
 ![Imagem 13: Dif. de Alíq. - ICMS por dentro, com exclusão do IPI:](https://ajuda.sankhya.com.br/hc/article_attachments/42313057877399) (((Vlr. Operação - Vlr. IPI - Vlr. ICMS Destacado) / (1 - %ICMS Interno)) x %ICMS
        Interno) - Vlr. ICMS Destacado
```

**Importante:** para realização dos devidos cálculos mencionados acima, você deverá se atentar para os cadastros de [CFOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714-CFOP) e [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), com a marcação para **"Cálculo de Diferença de ICMS"**, nas abas [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714-CFOP#abageral) e [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), respectivamente.

Trouxemos o exemplo do cálculo com ICMS por dentro:

Uma Empresa de Minas Gerais adquire um produto de São Paulo no valor de R$1.000,00, com 12% de tributação da operação própria, ou seja, o ICMS Destacado será de R$ 120,00. Esse produto possui alíquota interna destino – UF Empresa (MG-MG) – igual à 18%. Com isso, o cálculo do diferencial de alíquota será:

(((1.000,00 – 120,00) / (1 – 18%)) x 18%) – 120,00 = R$ 73,17

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#top)

## Botões - Gerar Agora | Status | Consultar Documento Não Gerado

Uma vez realizadas todas as configurações necessárias nas abas, a geração dos Livros Fiscais pode ser efetuada. Essa geração ocorre através do acionamento do botão ![Imagem 14: Uma vez realizadas todas as configurações necessárias nas abas, a geração dos Livros Fiscais pode ser efetuada. Essa…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003322601)**"Gerar Agora"** localizado na parte superior central da tela. Ao clicar nesse botão, será aberto o seguinte pop-up:

![Imagem 15: Uma vez realizadas todas as configurações necessárias nas abas, a geração dos Livros Fiscais pode ser efetuada. Essa…](https://ajuda.sankhya.com.br/hc/article_attachments/360104310333)

No campo **"Período"**, informe o intervalo de datas que você deseja gerar os livros fiscais.

**Importante:** na geração do Livro de Entrada, a escrituração será realizada com base no período informado, sendo que o sistema considerará a seguinte prioridade:

1. data de entrada e saída;
2. se a data de entrada e saída não estiver preenchida, a data de faturamento;
3. se a data de faturamento não estiver preenchida, a data de movimento;
4. por último, a data de negociação.

Na geração do Livro de Saída, o sistema verificará a data de negociação.

Ao efetuar a geração a nota de amostra do livro será deletada, isso acontece por que não existe valor comercial e pela nota estar conectada a um CFOP específico.

**Observação:** cumpre salientar que, notas de bonificação são diferentes de notas de amostra grátis. Notas de bonificação possuem valor comercial, mesmo que simbólicos, sofrendo tributação e por isso devem entrar no livro. Nota de amostra grátis por não ter valor comercial, são isentas de impostos.

Além disso, caso seja necessário gerar os dados apenas de uma nota, você poderá fazê-lo ao informar seu **"Número Único"**. Com os devidos preenchimentos realizados, clique em **"OK"** para seguimento na geração ou em **"Cancelar"** para anulá-lo.

![Imagem 16: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/16313545312535) **Informações adicionais:**

- Com o parâmetro **"Permite gerar o livro com nota errada no período? - GERACOMERROPER"** desabilitado, não será possível gerar o livro caso exista uma ou mais notas inconsistentes dentro do período definido para geração. Se o parâmetro for ligado, existindo alguma nota com erro, a geração do livro irá seguir sem impedimentos.
- Ao habilitar o parâmetro **"Gerar o livro para títulos renegociados de frete? - LIVFRETERENEG"** e realizar a geração do livro, será gerado apenas um registro do título renegociado. Se você desabilitá-lo, irá gerar registros dos títulos originais antes de serem renegociados.
- Quando o parâmetro **"Consid.VLRLIQ item monofástico liv.f - LIVMONOFAVLRLIQ"** estiver habilitado, em uma operação de compra, com o CST do item sendo **"61 - Tributação monofásica sobre combustíveis cobrada anteriormente"**, sem despesas acessórias na operação e sendo o primeiro item a ser processado, o valor calculado do item será desconsiderado e, em seu lugar, será atribuído o valor líquido (VLRTOTAL - VLRDESC).
- Além das Notas Fiscais, o sistema está apto à considerar os [CT-e's](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596834) emitidos no período na geração dos Livros Fiscais e posterior geração do EFD.

Ao clicar em **"OK"**, a tela a seguir demonstrará o processamento dos Livros Fiscais:

![Imagem 17: Ao clicar em "OK" , a tela a seguir demonstrará o processamento dos Livros Fiscais :](https://ajuda.sankhya.com.br/hc/article_attachments/1500003271282)

**Nota:** ao término da geração do livro, as informações pertinentes ao valor calculado do IPI serão transformadas em um ajuste, ou seja, será gerado um ajuste automático do IPI. Esse fato irá ocorrer caso ao menos um parceiro do livro esteja com a marcação **"Enquadro no Art. 227. para cálculo de IPI?"** efetuada (aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abafiscal) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros)) e a marcação **"Gerar linhas da Nota separadamente no Livro Fiscal?"** realizada (na aba [Livros Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abalivrosfiscais) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa)).

O botão **"Status"**, também localizado no alto da tela, é modificado à medida que se procede com a geração dos dados. Ele poderá apresentar a descrição **"Em execução"** ou **"Parado"**; no primeiro caso, representa que os Livros Fiscais estão sendo processados e a segunda situação, que a geração está paralisada ou foi finalizada.

**Importante:** para documentos eletrônicos, a geração do livro é feita apenas para documentos com validade jurídica aprovados nos ambientes da SEFAZ/RFB de produção.

A opção de **"Consultar Documento Não Gerado"**, pode ser acessada por meio do botão![Imagem 18: A opção de "Consultar Documento Não Gerado" , pode ser acessada por meio do botão "Outras opções..." que, quando…](https://ajuda.sankhya.com.br/hc/article_attachments/16313519434903)**"Outras opções..."** que, quando selecionada, permitirá que você consulte alguma nota que não tenha sido gerada no livro de ICMS/IPI. Será aberto um pop-up também de nomenclatura Consultar Documento Não Gerado, e você pode utilizar dos seguintes dados para buscar as notas:

- Nro. único;
- Chave NFe\CTe;
- Nro. Nota;
- Série;
- Data de Negociação;
- Empresa.

![Imagem 19: Empresa.](https://ajuda.sankhya.com.br/hc/article_attachments/1500003322741)

Os três últimos campos de filtragem serão habilitados para preenchimento apenas se o Nro. Nota for informado primeiro.

Ao clicar no botão **"Posicionar Documento"** localizado na parte inferior do pop-up, será aberta a tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874) posicionada no financeiro em questão.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#top)
