---
id: "37829149672215"
titulo: "Como configurar a e executar a contabilização de notas de entrada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37829149672215-Como-configurar-a-e-executar-a-contabiliza%C3%A7%C3%A3o-de-notas-de-entrada"
trilha: "Universidade Sankhya > Gestão Patrimonial"
atualizado_em: "2026-07-22T14:07:25Z"
rotulos: ["Configuração", "NF-e", "TOP", "Contabilização", "Financeiro"]
---

# Como configurar a e executar a contabilização de notas de entrada

| **Categoria** |
| --- |
| [Contabilização de notas de entrada](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829149672215-Como-configurar-a-e-executar-a-contabiliza%C3%A7%C3%A3o-de-notas-de-entrada#h_01KFGF7GXFZSEX639NYC2PC94V) |
| [Demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829149672215-Como-configurar-a-e-executar-a-contabiliza%C3%A7%C3%A3o-de-notas-de-entrada#h_01KFGF77FR3AEFY8TGBEH4R3DW) |
| [Cenário de aplicação](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829149672215-Como-configurar-a-e-executar-a-contabiliza%C3%A7%C3%A3o-de-notas-de-entrada#h_01KFGF7YYT66NRC8MV0AE8FV69) |
| [É o momento de aplicar o conhecimento adquirido! Confira as etapas de execução no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829149672215-Como-configurar-a-e-executar-a-contabiliza%C3%A7%C3%A3o-de-notas-de-entrada#h_01KFGF85YHZ0TW27RW5V2G8S43) |

## Contabilização de notas de entrada

A contabilização de notas de entrada é o processo que transforma os registros fiscais de compras em lançamentos contábeis de débito e crédito dentro do ERP Sankhya. A partir da nota fiscal registrada, os lançamentos são gerados por meio da contabilização e passam a alimentar a contabilidade, garantindo que todas as operações de entrada — como aquisições para revenda, consumo ou movimentações internas — sejam refletidas de forma correta e segura. Esse recurso assegura conformidade contábil, integra as áreas fiscal e contábil e proporciona maior confiabilidade às informações gerenciais.

#### Demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1118204475)

#### Cenário de aplicação

A empresa Axis LTDA. utiliza o ERP Sankhya para gestão de seus processos. Por meio de uma configuração criteriosa, o processo contábil foi estruturado para garantir que todas as operações de entrada sejam devidamente contabilizadas, oferecendo segurança e confiabilidade às informações.

**Tarefa:** Assista o vídeo de demonstração prática no sistema e confira o passo a passo abaixo para configurar e realizar a contabilização das notas de entrada em sua base de testes.

#### É o momento de aplicar o conhecimento adquirido! Confira as etapas de execução no ERP Sankhya

**Atenção**

- Para a correta aplicação desta prática, é indispensável que as configurações apresentadas na aula “Configurações e Cadastros para Contabilização” estejam devidamente executadas.
- Para fins de demonstração, utilizaremos a TOP COMPRA REVENDA.

**1**. Acesse a tela **Portal de Compras**

**Menu:** Comercial » Consulta » Portal de Compras

- No menu **Filtros Rápidos**, preencha os campos de Data de Negociação com o período correspondente à contabilização que deseja gerar.
- Identifique os lançamentos aprovados e o valor acumulado no período.

**2**. Acesse a tela **Tipos de Operação - TOP**

**Menu:** Comercial » Arquivo » Cadastros » Tipos de Operação - TOP 

- Localize, em sua base de testes, a TOP utilizada para as movimentações de entrada.

Ex.: COMPRA REVENDA.

**Aba Geral**

- Valide se o campo ”**Atualiza Contabilidade**” está marcado.

**3**. Acesse a tela **TOP Contabilização**
**Menu:** Contabilização » Arquivos » TOP Contabilização

- No menu lateral, localize a TOP desejada e a selecione, na grade de resultado abra com um duplo clique.

Ex.: COMPRA REVENDA

- No painel principal, certifique-se que as opções “**Ativo**” e “**Atualiza** **Contabilidade**” estejam marcadas.

**Aba Configurações p/ Lançamentos Contábeis**

- Nesta aba são definidas todas as configurações necessárias para a contabilização da movimentação. Essa parametrização pode ser realizada manualmente ou por meio de templates, sendo executada pelo time técnico da Sankhya, de acordo com as orientações do contador da empresa cadastrada na base.
- Caso a aba não esteja parametrizada siga as orientações para cadastrar o template:
- Acione o botão “**Ações**”, representado pelo ícone de raio.
- Selecione a opção **Buscar Template Contabilização -** **Melhores Práticas**.
- Clique sobre a lupa no campo **Nro. Template** e selecione entre as opções disponíveis a descrição adequada para a TOP selecionada.

Ex.: Compra MP /  Revenda - CT-e Conta Transitória

- No campo **TOP Destino**, informe o tipo de operação que está configurando.
- Ex.: COMPRA REVENDA
- Acione o botão “**Aplicar**” e em seguida confime para finalizar.

O template vinculado trará todas as regras necessárias para que as movimentações realizadas com o Tipo de Operação configurado sejam contabilizadas corretamente.

**4**. Acesse a tela **Agendamento**
**Menu:** Contabilização » Rotinas » Agendamento

- Clique no botão “**+**” (**Cadastrar** **Agendamento Tarefa**).
- Informe a **Descrição** agendamento no campo indicado. 
  Ex.: Notas de entrada
- Identifique a **Empresa** no campo indicado.
- O campo **Tipo Execução** define a forma de realização da contabilização. Selecione a opção **Ambos**.
  Essa configuração permite que o sistema execute a contabilização na frequência definida e, adicionalmente, possibilita a execução manual sempre que necessário.

**Aba Frequência Agendamento**

- Informe o horário da 1ª execução.
- Na seção **Meses** marque a opção **Todos**.
- Salve o registro.

**Aba Parâmetros**

- Se as fórmulas da TOP Contabilização fizerem menção ao custo, localize na seção Geral o campo **Usar custo** e realize a marcação.
- Na seção Lançamentos, defina como serão agrupados os lançamentos contábeis.
- Defina na seção Numeração Lotes como serão numerados os lotes gerados.
  Ex.: A opção Empresa/TOP determina que o lote será gerado com a mesma numeração da TOP configurada.

**Aba Filtros**

- Marque a opção “**Notas**” e, em seguida, clique no botão “**Filtros**” ao lado.
- Clique no botão “**+ Filtro**” (**Cadastrar** **Filtro**).

Atenção! 
Nesta configuração, será usada uma fórmula no modo avançado, mas o filtro pode ser ajustado conforme a rotina e as necessidades da sua operação. 

- Marque a opção “**Notas**” e, em seguida, clique no botão “**Filtros**” ao lado.
- Clique no botão “**+ Filtro**” (**Cadastrar** **Filtro**).
- Defina o **Nome do Filtro** no campo indicado.
  Ex.: Notas de entrada

**1ª Condição**

- Clique em **+ Condição**.
- Clique em Selecione o campo para escolher critérios e nos Campos de Nota/Pedido selecione **Dt. Entrada/Saída.**
- A escolha está condizente com o Tipo de data escolhido na configuração de TOP Contabilização
- Selecione **Maior igual (>=)** e marque a opção **Variável**.

**2ª Condição**

- Clique em **+ Condição**.
- Clique em Selecione o campo para escolher critérios e nos Campos de Nota/Pedido selecione **Dt. Entrada/Saída.**
- Selecione **Menor igual (<=)** e marque a opção **Variável**.

**3ª Condição**

- Clique em Selecione o campo para escolher critérios e nos Campos de Nota/Pedido selecione **Empresa**
- Selecione **Igual (=)** e informe o código da empresa.

**4ª Condição**

- Clique em Selecione o campo para escolher critérios e nos Campos de Nota/Pedido selecione **Tipo de Movimento**
- Selecione **Igual (=)** e selecione a opção **C - Compra**.
- Clique no botão “**Salvar**”.
- Clique em **Contabilizar Agora**
- Informe o período da contabilização e aplique a referência para avançar.
- Se necessário, informe a numeração do lote.
- Informe a **Data do movimento** da contabilização e em seguida o **Período para gerar dia a dia**.
- Acesse a aba Histórico e selecione o registro do lote gerado.
- Acione o botão “**Ver** **Lotes Gerados**” e selecione com um duplo clique o registro informado no pop-up aberto para ser direcionado à tela Lotes Contábeis (**Menu:** Contabilidade » Arquivos » Lotes Contábeis ).
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
