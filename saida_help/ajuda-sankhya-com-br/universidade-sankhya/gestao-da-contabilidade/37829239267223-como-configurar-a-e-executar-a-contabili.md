---
id: "37829239267223"
titulo: "Como configurar a e executar a contabilização de notas de saída"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37829239267223-Como-configurar-a-e-executar-a-contabiliza%C3%A7%C3%A3o-de-notas-de-sa%C3%ADda"
trilha: "Universidade Sankhya > Gestão da Contabilidade "
atualizado_em: "2026-07-22T14:07:24Z"
rotulos: ["Configuração", "NF-e", "Portal de Vendas", "TOP", "Contabilização", "Financeiro"]
---

# Como configurar a e executar a contabilização de notas de saída

| Categoria |
| --- |
| [Contabilização de notas de saída](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829239267223-Como-configurar-a-e-executar-a-contabiliza%C3%A7%C3%A3o-de-notas-de-sa%C3%ADda#h_01KFGFFWVFNJH7XCPWJ8E49KZP) |
| [Demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829239267223-Como-configurar-a-e-executar-a-contabiliza%C3%A7%C3%A3o-de-notas-de-sa%C3%ADda#h_01KFGFG6D5Z8SDV3WF8F9Z7SG5) |
| [Cenário de Aplicação](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829239267223-Como-configurar-a-e-executar-a-contabiliza%C3%A7%C3%A3o-de-notas-de-sa%C3%ADda#h_01KFGFGCN0DCQSHXBCG2YEBJ2G) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37829239267223-Como-configurar-a-e-executar-a-contabiliza%C3%A7%C3%A3o-de-notas-de-sa%C3%ADda#h_01KFGFGJJPDGKBHSAE02SSMHTF) |

#### Contabilização de notas de saída

A contabilização de notas de saída é o processo que transforma os registros fiscais de vendas em lançamentos contábeis de débito e crédito dentro do ERP Sankhya. A partir da emissão da nota fiscal, os lançamentos são gerados por meio da contabilização e passam a alimentar a contabilidade, assegurando que todas as operações de saída — como vendas de mercadorias, prestação de serviços ou remessas — sejam refletidas de forma correta e segura. Esse recurso garante conformidade contábil, integra as áreas fiscal e contábil e proporciona maior confiabilidade às informações gerenciais.

#### Demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1118205884)

#### Cenário de Aplicação

A empresa Axis LTDA. utiliza o ERP Sankhya para gestão de seus processos. Por meio de uma configuração criteriosa, o processo contábil foi estruturado para garantir que todas as operações de saída sejam devidamente contabilizadas, assegurando controle, conformidade e confiabilidade às informações.

**Tarefa:** assista ao vídeo de demonstração prática no sistema e confira o passo a passo abaixo para configurar e realizar a contabilização das notas de saída em sua base de testes.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

**Atenção**

- Para a correta aplicação desta prática, é indispensável que as configurações apresentadas na aula “Configurações e Cadastros para Contabilização” estejam devidamente executadas.
- Para fins de demonstração, utilizaremos a TOP VENDA NF-E.

**1**. Acesse a tela **Portal de Vendas**

**Menu:** Comercial » Consulta » Portal de Vendas

No menu **Filtros Rápidos**, preencha os campos de Data de Negociação com o período correspondente à contabilização que deseja gerar.

Identifique os lançamentos aprovados e o valor acumulado no período.

        **2**. Acesse a tela **Tipos de Operação - TOP**

**Menu:** Comercial » Arquivo » Cadastros » Tipos de Operação - TOP 

- Localize, em sua base de testes, a TOP utilizada para as movimentações de entrada.

Ex.: VENDA NF-E.

**Aba Geral**

- Valide se o campo ”**Atualiza Contabilidade**” está marcado.

**3.** Acesse a tela **TOP Contabilização**

**Menu:** Contabilização » Arquivos » TOP Contabilização

- No menu lateral, localize a TOP desejada e a selecione, na grade de resultado abra com um duplo clique.

Ex.: VENDA NF-E

- No painel principal, certifique-se que as opções “**Ativo**” e “**Atualiza** **Contabilidade**” estejam marcadas.

**Aba Configurações p/ Lançamentos Contábeis**

- Nesta aba são definidas todas as configurações necessárias para a contabilização da movimentação. Essa parametrização pode ser realizada manualmente ou por meio de templates, sendo executada pelo time técnico da Sankhya, de acordo com as orientações do contador da empresa cadastrada na base.
- Caso a aba não esteja parametrizada siga as orientações para cadastrar o template:
- Acione o botão “**Ações**”, representado pelo ícone de raio.
- Selecione a opção **Buscar Template Contabilização -** **Melhores Práticas**.
- Clique sobre a lupa no campo **Nro. Template** e selecione entre as opções disponíveis a descrição adequada para a TOP selecionada.

Ex.: Vendas PA / Revenda / MP

- No campo **TOP Destino**, informe o tipo de operação que está configurando.
- Ex.: VENDA NF-E
- Acione o botão “**Aplicar**” para finalizar.

O template vinculado trará todas as regras necessárias para que as movimentações realizadas com o Tipo de Operação configurado sejam contabilizadas corretamente.

**Importante:** caso algum registro apresente a **Conta Contábil** zerada, será necessário realizar a devida configuração para que a contabilização seja efetivada. O vídeo de demonstração prática disponibiliza as orientações para esse ajuste.

**4.** Acesse a tela **Agendamento**

**Menu:** Contabilização » Rotinas » Agendamento

- Clique no botão “**+**” (**Cadastrar** **Agendamento Tarefa**).
- Informe a **Descrição** agendamento no campo indicado. 
  Ex.: Notas de saída
- Identifique a **Empresa** no campo indicado.
- O campo **Tipo Execução** define a forma de realização da contabilização. Selecione a opção **Ambos**.
  Essa configuração permite que o sistema execute a contabilização na frequência definida e, adicionalmente, possibilita a execução manual sempre que necessário.

**Aba Frequência Agendamento**

- Informe o horário da 1ª execução.
- Na seção **Meses** marque a opção **Todos**.

**Aba Parâmetros**

- Se as fórmulas da TOP Contabilização fizerem menção ao custo, localize na seção Geral o campo **Usar custo** e realize a marcação.
- Na seção Lançamentos, defina como serão agrupados os lançamentos contábeis.
- Defina na seção Numeração Lotes como serão numerados os lotes gerados.
  Ex.: A opção Empresa/TOP determina que o lote será gerado com a mesma numeração da TOP configurada.
- Salve o registro

**Aba Filtros**

- Marque a opção “**Notas**” e, em seguida, clique no botão “**Filtros**” ao lado.
- Clique no botão “**+ Filtro**” (**Cadastrar** **Filtro**).
- Defina o **Nome do Filtro** no campo indicado.
  Ex.: Notas de saída

**1ª Condição**

- Clique em **+ Condição**.
- Clique em Selecione o campo para escolher critérios e nos Campos de Nota/Pedido selecione **Dt. Neg.**
- A escolha está condizente com o Tipo de data escolhido na configuração de TOP Contabilização
- Selecione **Maior igual (>=)** e marque a opção **Variável**.

**2ª Condição**

- Clique em **+ Condição**.
- Clique em Selecione o campo para escolher critérios e nos Campos de Nota/Pedido selecione **Dt. Neg.**
- Selecione **Menor igual (<=)** e marque a opção **Variável**.

**3ª Condição**

- Clique em Selecione o campo para escolher critérios e nos Campos de Nota/Pedido selecione **Empresa**
- Selecione **Igual (=)** e informe o código da empresa.

**4ª Condição**

- Clique em Selecione o campo para escolher critérios e nos Campos de Nota/Pedido selecione **Tipo de Movimento**
- Selecione **Igual (=)** e selecione a opção **Venda**.
- Clique no botão “**Salvar**”.
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

Para acessar a tela a partir da rotina Lotes Contábeis siga uma das opções:

- Selecione o lote desejado com um clique e pressione no teclado ctrl + L.
- No menu principal, acione o botão “**...**” (**Outras** **opções…**) e selecione a opção **Visualizar Lançamentos (Ctrl** **+ L)**.

**5**. Acesse a tela **Consulta Lançamentos Contábeis** 

**Menu:** Contabilização » Consultas » Consulta Lançamentos Contábeis

- Na caixa Procurando por Empresa, selecione o registro de sua empresa.
- Nos Filtros rápidos informe a **Referência**.
- Defina o status **Conciliado** e aplique o filtro para consultar as informações.

Nesta tela, são apresentados todos os lançamentos contábeis de débito e crédito referentes às notas de entrada emitidas no período de referência.
