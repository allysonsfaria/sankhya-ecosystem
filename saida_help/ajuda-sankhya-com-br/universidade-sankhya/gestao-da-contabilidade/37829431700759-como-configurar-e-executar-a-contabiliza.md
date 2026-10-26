---
id: "37829431700759"
titulo: "Como configurar e executar a contabilização financeira"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37829431700759-Como-configurar-e-executar-a-contabiliza%C3%A7%C3%A3o-financeira"
trilha: "Universidade Sankhya > Gestão da Contabilidade "
atualizado_em: "2026-08-25T20:05:29Z"
rotulos: ["Configuração", "Movimentação Financeira", "TOP", "Contabilização", "Financeiro"]
---

# Como configurar e executar a contabilização financeira

| Categoria |
| --- |
| [Contabilização de movimentos financeiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829431700759-Como-configurar-e-executar-a-contabiliza%C3%A7%C3%A3o-financeira#h_01KFGFW6ZK4B55J80B0PY8Z044) |
| [Demonstração prática no Sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829431700759-Como-configurar-e-executar-a-contabiliza%C3%A7%C3%A3o-financeira#h_01KFGFVY5X6MCPVTV1T1ATKN33) |
| [Cenário de aplicação](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829431700759-Como-configurar-e-executar-a-contabiliza%C3%A7%C3%A3o-financeira#h_01KFGFVN1TTCGAJ9RF4YZW2X25) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829431700759-Como-configurar-e-executar-a-contabiliza%C3%A7%C3%A3o-financeira#h_01KFGFVA5BZN4P9YRNCSRJXR7P) |

#### Contabilização de movimentos financeiros

A contabilização de movimentos financeiros consolida no módulo contábil todas as operações que transitam pela área financeira do ERP Sankhya. Esse processo organiza de forma padronizada registros como pagamentos, recebimentos, baixas de títulos e conciliações bancárias, transformando-os em lançamentos contábeis alinhados ao plano de contas da empresa. Com isso, a contabilidade passa a refletir com precisão a realidade financeira, permitindo maior rastreabilidade, agilidade no fechamento e confiabilidade nas análises de resultado.

#### Demonstração prática no Sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1118231285)

#### Cenário de aplicação

A empresa Axis LTDA., do segmento Atacado Distribuidor, realiza diariamente pagamentos a fornecedores referentes a compras de mercadorias e serviços. Esses pagamentos, após serem baixados no ERP Sankhya, precisam ser devidamente contabilizados para garantir que as saídas financeiras sejam refletidas no módulo contábil. Com isso, é possível assegurar que as obrigações estejam quitadas e registradas de forma correta, mantendo a conformidade contábil e a integridade das informações financeiras.

**Tarefa:** assista ao vídeo de demonstração prática e, em seguida, siga o passo a passo abaixo para configurar e realizar a contabilização dos pagamentos baixados. 

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

**Atenção**

- Para a correta aplicação desta prática, é indispensável que as configurações apresentadas na aula “Configurações e Cadastros para Contabilização” estejam devidamente executadas.
- Para fins de demonstração, utilizaremos as TOPs PAGAMENTO e RECEBIMENTO.

        **1**. Acesse a tela **Movimentação Financeira**

**Menu:** Financeiro » Rotinas  » Movimentação Financeira

- Acione o botão “**+ Filtros**” e na aba Filtros rápidos, valide se na base de testes há  títulos de receitas e despesas baixados.

**2.** Acesse a tela **Tipos de Operação - TOP**

**Menu:** Comercial » Arquivo » Cadastros » Tipos de Operação - TOP 

- Localize, em sua base de testes, a TOP utilizada para as movimentações de entrada.

Ex.: PAGAMENTO e RECEBIMENTO.

**Aba Geral**

- Valide se o campo ”**Atualiza Contabilidade**” está marcado.

**3**. Acesse a tela **TOP Contabilização**

**Menu:** Contabilização » Arquivos » TOP Contabilização

- No menu lateral, localize a TOP desejada e a selecione, na grade de resultado abra com um duplo clique.

Ex.: PAGAMENTO e RECEBIMENTO

- No painel principal, certifique-se que as opções “**Ativo**” e “**Atualiza** **Contabilidade**” estejam marcadas.

**Aba Configurações p/ Lançamentos Contábeis**

- Nesta aba são definidas todas as configurações necessárias para a contabilização da movimentação. Essa parametrização pode ser realizada manualmente ou por meio de templates, sendo executada pelo time técnico da Sankhya, de acordo com as orientações do contador da empresa cadastrada na base.
- Caso a aba não esteja parametrizada e não possua template de configuração, siga as orientações abaixo para realizar a configuração manual:
- Clique em “**+**” (**Cadastrar** **Parâmetros Contabilização**) para cadastrar os 4 lançamentos utilizados

**1º lançamento**

- **Tipo de Lançamento**: Débito
- **Conta Contábil:** FORNECEDORES DIVERSOS
- **Lançamento:** 1
- **Fórmula:** FORMULA.VLRDESDOB
  Acione o botão “Construtor” para buscar o VALOR DO DESDOBRAMENTO nas categorias e salve o registro.
- **Tipo de data:** Baixa
- Salve o registro.

**2º lançamento**

- **Tipo de Lançamento**: Crédito
- **Tipo de Conta Contábil:** Variável
- **Conta Contábil:** Conta da Conta bancária
  É necessário que na conta bancária o campo Conta Contábil esteja alimentado.
- **Lançamento:** 2
- **Fórmula:** FORMULA.VLRBAIXA
  Acione o botão “Construtor” para buscar o VALOR DE BAIXA nas categorias e salve o registro.
- **Tipo de data:** Baixa
- Salve o registro.

**3º lançamento**

- **Tipo de Lançamento**: Débito
- **Conta Contábil:** JUROS DE MORA
- **Lançamento:** 3
- **Fórmula:** FORMULA.VLRJURO + FORMULA.VLRMULTA
  Acione o botão “Construtor” para buscar o VALOR DO JURO e VALOR DE MULTA nas categorias e salve o registro.
- **Tipo de data:** Baixa
- Salve o registro.

**4º lançamento**

- **Tipo de Lançamento**: Crédito
- **Conta Contábil:** DESCONTOS OBTIDOS
- **Lançamento:** 4
- **Fórmula:** FORMULA.VLRDESC
  Acione o botão “Construtor” para buscar o VALOR DE DESCONTO  nas categorias e salve o registro.
- **Tipo de data:** Baixa
- Salve o registro.

**4**. Acesse a tela **Agendamento**

**Menu:** Contabilização » Rotinas » Agendamento

- Clique no botão “**+**” (**Cadastrar** **Agendamento Tarefa**).
- Informe a **Descrição** agendamento no campo indicado. 
  Ex.: Pagamentos
- Identifique a **Empresa** no campo indicado.
- O campo **Tipo Execução** define a forma de realização da contabilização. Selecione a opção **Automático**.

**Aba Frequência Agendamento**

- Informe o horário da 1ª execução.
- Na seção **Meses** marque a opção **Todos**.

**Aba Parâmetros**

- Na seção Lançamentos, defina como serão agrupados os lançamentos contábeis.
- Defina na seção Numeração Lotes como serão numerados os lotes gerados.
  Ex.: A opção Empresa/TOP determina que o lote será gerado com a mesma numeração da TOP configurada.
- Salve o registro

**Aba Filtros**

- Marque a opção “**Baixas**” e, em seguida, clique no botão “**Filtros**” ao lado.
- Clique no botão “**+ Filtro**” (**Cadastrar** **Filtro**).
- Defina o **Nome do Filtro** no campo indicado.
  Ex.: Pagamentos

**1ª Condição**

- Clique em **+ Condição**.
- Clique em Selecione o campo para escolher critérios e nos Campos de Financeiro  selecione **Data Baixa.**
- A escolha está condizente com o Tipo de data escolhido na configuração de TOP Contabilização
- Selecione **Maior igual (>=)** e marque a opção **Variável**.

**2ª Condição**

- Clique em **+ Condição**.
- Clique em Selecione o campo para escolher critérios e nos Campos de Financeiro  selecione **Data Baixa.**
- Selecione **Menor igual (<=)** e marque a opção **Variável**.

**3ª Condição**

- Clique em Selecione o campo para escolher critérios e nos Campos de Financeiro  selecione **Empresa**
- Selecione **Igual (=)** e informe o código da empresa.

**4ª Condição**

- Clique em Selecione o campo para escolher critérios e nos Campos de Financeiro  selecione **Receita/Despesa**
- Selecione **Igual (=)** e selecione a opção **Despesa**.
- Clique no botão “**Salvar**”.

Para que a operação seja efetiva é necessário que ao menos uma baixa esteja registrada na rotina Movimentação Financeira.

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

**5.** Acesse a tela **Consulta Lançamentos Contábeis** 

**Menu:** Contabilização » Consultas » Consulta Lançamentos Contábeis

- Na caixa Procurando por Empresa, selecione o registro de sua empresa.
- Nos Filtros rápidos informe a **Referência**.
- Defina o status **Conciliado** e aplique o filtro para consultar as informações.

Nesta tela, são apresentados todos os lançamentos contábeis de débito e crédito referentes às notas de entrada emitidas no período de referência.
