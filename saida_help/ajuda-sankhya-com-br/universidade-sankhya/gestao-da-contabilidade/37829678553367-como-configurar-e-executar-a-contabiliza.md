---
id: "37829678553367"
titulo: "Como configurar e executar a contabilização de mov. bancárias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37829678553367-Como-configurar-e-executar-a-contabiliza%C3%A7%C3%A3o-de-mov-banc%C3%A1rias"
trilha: "Universidade Sankhya > Gestão da Contabilidade "
atualizado_em: "2026-07-22T14:07:21Z"
rotulos: ["Configuração", "Movimentação Financeira", "TOP", "Contabilização", "Financeiro"]
---

# Como configurar e executar a contabilização de mov. bancárias

| Categoria |
| --- |
| [Contabilização de movimentações bancárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829678553367-Como-configurar-e-executar-a-contabiliza%C3%A7%C3%A3o-de-mov-banc%C3%A1rias#h_01KFGGDV9954N7MQGP5WTPZNY6) |
| [Demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829678553367-Como-configurar-e-executar-a-contabiliza%C3%A7%C3%A3o-de-mov-banc%C3%A1rias#h_01KFGGDZPTADRCGD3KFWXF1Q75) |
| [Cenário de aplicação](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829678553367-Como-configurar-e-executar-a-contabiliza%C3%A7%C3%A3o-de-mov-banc%C3%A1rias#h_01KFGGED8ZE3DD2VNW3B82W1ZX) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829678553367-Como-configurar-e-executar-a-contabiliza%C3%A7%C3%A3o-de-mov-banc%C3%A1rias#h_01KFGGEMV7H83GA10JGGGRQBVD) |

## Contabilização de movimentações bancárias

A contabilização de movimentações bancárias garante que operações como transferências, pagamentos via TED ou PIX, recebimentos em conta e tarifas bancárias sejam registradas de forma estruturada no módulo contábil do ERP Sankhya. Esse processo assegura que cada transação realizada nas contas correntes da empresa seja convertida em lançamentos contábeis consistentes, vinculados às contas e históricos adequados. Dessa forma, é possível manter o controle patrimonial atualizado, assegurar conformidade contábil e facilitar a conciliação entre os extratos bancários e os registros internos, fortalecendo a confiabilidade das informações financeiras.

#### Demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1118204691)

#### Cenário de aplicação

A empresa Axis LTDA., do segmento Atacado Distribuidor, realiza diariamente diversas movimentações financeiras em suas contas bancárias, como pagamentos diretos, recebimentos de clientes via depósito, transferências entre contas correntes, além do registro de tarifas e juros. Como essas operações não estão necessariamente vinculadas a notas fiscais ou títulos previamente cadastrados no sistema, é fundamental que sejam devidamente contabilizadas para assegurar conformidade fiscal e consistência nos relatórios financeiros.

**Tarefa:** assista ao vídeo de demonstração prática e siga o passo a passo abaixo para configurar a contabilização das movimentações bancárias. Atente-se ao mapeamento correto das contas contábeis nos cadastros de contas correntes e nos tipos de movimentação bancária, garantindo que as operações sejam refletidas de forma automática e confiável na contabilidade.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

**Atenção**

- Para a correta aplicação desta prática, é indispensável que as configurações apresentadas na aula “Configurações e Cadastros para Contabilização” estejam devidamente executadas.
- Para fins de demonstração, utilizaremos a TOP MOVIMENTACAO BANCARIA

**1.** Acesse a tela **Tipos de Operação - TOP**

**Menu:** Comercial » Arquivo » Cadastros » Tipos de Operação - TOP 

- Localize, em sua base de testes, a TOP utilizada para as movimentações de entrada.

Ex.: MOVIMENTACAO BANCARIA

**Aba Geral**

- Valide se o campo ”**Atualiza Contabilidade**” está marcado.

**2.** Acesse a tela **TOP Contabilização**

**Menu:** Contabilização » Arquivos » TOP Contabilização

- No menu lateral, localize a TOP desejada e a selecione, na grade de resultado abra com um duplo clique.

Ex.: MOVIMENTACAO BANCARIA

- No painel principal, certifique-se que as opções “**Ativo**” e “**Atualiza** **Contabilidade**” estejam marcadas.

**Aba Configurações p/ Lançamentos Contábeis**

- Nesta aba são definidas todas as configurações necessárias para a contabilização da movimentação.
- Caso a aba não esteja parametrizada e não possua template de configuração, siga as orientações abaixo para realizar a configuração manual:
- Clique em “**+**” (**Cadastrar** **Parâmetros Contabilização**) para cadastrar os 4 lançamentos utilizados

**1º lançamento**

- **Tipo de Lançamento**: Débito
- **Tipo de Conta Contábil:** Variável
- **Conta Contábil:** Conta da Conta bancária
  É necessário que na conta bancária o campo Conta Contábil esteja alimentado.
- **Lançamento:** 1
- **Fórmula:** FORMULA.VLRLANC
  Acione o botão “Construtor” para buscar o VALOR DO LANÇAMENTO  nas categorias e salve o registro.
- Salve o registro.

- Duplique o lançamento.

**2º lançamento**

- **Tipo de Lançamento**: Débito
- **Tipo de Conta Contábil:** Variável
- **Conta Contábil:** Conta da Conta bancária
  É necessário que na conta bancária o campo Conta Contábil esteja alimentado.
- **Lançamento:** 1
- **Fórmula:** FORMULA.VLRLANC
  Acione o botão “Construtor” para buscar o VALOR DO LANÇAMENTO  nas categorias e salve o registro.
- Salve o registro.

**3.** Acesse a tela **Agendamento**

**Menu:** Contabilização » Rotinas » Agendamento

- Clique no botão “**+**” (**Cadastrar** **Agendamento Tarefa**).
- Informe a **Descrição** agendamento no campo indicado. 
  Ex.: Pagamentos
- Identifique a **Empresa** no campo indicado.
- O campo **Tipo Execução** define a forma de realização da contabilização. Selecione a opção **Ambos**.

**Aba Frequência Agendamento**

- Informe o horário da 1ª execução.
- Na seção **Meses** marque a opção **Todos**.

**Aba Filtros**

- Marque a opção “**Mov. Bancário**” e, em seguida, clique no botão “**Filtros**” ao lado.
- Clique no botão “**+ Filtro**” (**Cadastrar** **Filtro**).
- Defina o **Nome do Filtro** no campo indicado.
  Ex.: Movimentação bancária

**1ª Condição**

- Clique em **+ Condição**.
- Clique em Selecione o campo para escolher critérios e nos Campos de Movimento bancário  selecione **Dt. Lançamento.**
- Selecione **Maior igual (>=)** e marque a opção **Variável**.

**2ª Condição**

- Clique em **+ Condição**.
- Clique em Selecione o campo para escolher critérios e nos Campos de Movimento bancário  selecione **Dt.** **Lançamento**.
- Selecione **Menor igual (<=)** e marque a opção **Variável**.
- Clique no botão “**Salvar**”.

Para que a operação seja efetiva é necessário que ao menos uma transferência esteja registrada na rotina Movimentação Bancária.

**4.** Acesse a tela **Movimentação Bancária**

**Menu:** Financeiro » Rotinas » Movimentação Bancária

- No canto superior direito, acione o botão “**+ Cadastrar**”.
- Preencha as informações obrigatórias (sinalizadas com \* ).

  - **Tipo de Movimento**: Transferência
  - **Tipo de Operação**: MOVIMENTAÇÃO BANCARIA
  - **Conta Origem**: sinalize a conta de origem
  - **Lanç.** **Origem**: Transf. bancos
  - **Conta Destino**: sinalize a conta de destino
  - **Lanç.** **Destino**: Crédito
  - **Vlr Lançamento**: 1000
  - **Dt.** **Lançamento**: informe a data
- Salve o registro.

**5.** Retorne à  tela **Agendamento**

**Menu:** Contabilização » Rotinas » Agendamento

- Clique em **Contabilizar Agora**
- Informe o período da contabilização e aplique a referência para avançar.
- Se necessário, informe a numeração do lote.
- Informe a **Data do movimento** da contabilização e em seguida o **Período para gerar dia a dia**.
- Acesse a aba Histórico e selecione o registro do lote gerado.
- Acione o botão “**Ver** **Lotes Gerados**” e selecione com um duplo clique o registro informado no pop-up aberto para ser direcionado à tela Lotes Contábeis (**Menu:** Contabilidade » Arquivos » Lotes Contábeis).
- Nas colunas é possível verificar:

  - **Usuário responsável pela contabilização**
  - **Nro. Lote**
  - **Referência**
  - **Data do Movimento**
  - **Total do Lote**
  - **Situação**

Para acessar a tela a partir da rotina Lotes Contábeis siga uma das opções:

- Selecione o lote desejado com um clique e pressione no teclado ctrl + L.
- No menu principal, acione o botão “**...**” (**Outras** **opções…**) e selecione a opção **Visualizar Lançamentos (Ctrl** **+ L)**.

**6.** Acesse a tela **Consulta Lançamentos Contábeis** 

**Menu:** Contabilização » Consultas » Consulta Lançamentos Contábeis

- Na caixa Procurando por Empresa, selecione o registro de sua empresa.
- Nos Filtros rápidos informe a **Referência**.
- Defina o status **Conciliado** e aplique o filtro para consultar as informações.

Nesta tela, são apresentados todos os lançamentos contábeis de débito e crédito referentes às notas de entrada emitidas no período de referência.
