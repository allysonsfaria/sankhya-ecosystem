---
id: "42427450811927"
titulo: "Tela de logs da integração Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427450811927-Tela-de-logs-da-integra%C3%A7%C3%A3o-Sankhya"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:01:45Z"
rotulos: ["sync_hc", "ploomes", "ploomes_14364442", "sync_hash_3943667b7915"]
---

# Tela de logs da integração Sankhya

## 1) Sobre a Tela de Registros do Sankhya

A **Tela de Registros do Sankhya** é o painel de consulta onde você pode visualizar, investigar e auditar todos os eventos processados pela integração entre Ploomes e Sankhya.

Cada ação de importação (Sankhya → Ploomes) ou exportação (Ploomes → Sankhya) gera um registro que fica disponível nessa tela, com informações detalhadas sobre o que aconteceu, quando aconteceu e o resultado da operação.

Essa tela é útil para confirmar se um documento ou cadastro foi processado corretamente, identificar falhas na integração e entender o motivo de eventuais erros — tudo a partir de uma interface centralizada com filtros de busca.

[GIF animado: Imagem 1: Essa tela é útil para confirmar se um documento ou cadastro foi processado corretamente, identificar falhas na…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223690022/3e5c8ea698df5bf1a58df898ff08/nova_tela_logs_sankhya.gif?expires=1786536000&signature=cfe377db2a55a167880f9bd2d4edd6fda7d1a50ef5acce3b91c496bc313f769e&req=diIlFc93nYFdW%2FMW3nq%2BgdUYWMFgKL80MltTAxkzWOxyqjIi1M7MuP2KOpRD%0AFX%2BzmUV%2F%2F0l6ITOqiz2ijUpudXw%3D%0A)

A tela está disponível para **usuários administradores** e **não administradores**, com diferenças de visibilidade:

- **Administradores** têm acesso completo aos registros de importação e exportação de todos os usuários da conta.
- **Não administradores** visualizam apenas os registros de exportação gerados pelas suas próprias ações.

---

## 2) Pré-requisitos

- Possuir a **integração Sankhya V3** ativa na conta Ploomes.

Se a interface da tela de registros for igual à do GIF acima, implica que já está na CV3. Caso a interface esteja diferente, com abas para exportação e importação, a conta ainda estará utilizando a integração Sankhya V2.

---

## 3) Utilizando a Tela de Registros do Sankhya

## 3.1) Acessando a tela

O caminho de acesso varia de acordo com o perfil do usuário:

### Para usuários administradores:

Acesse a **Tela de Administração** > **Menu Integrações** > clique no botão **Registros do Sankhya**.

![Imagem 2: Acesse a Tela de Administração > Menu Integrações > clique no botão Registros do Sankhya .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223701167/cc150f2b22e9d2b5798c2c4bef3c/IntegracaoSankhya-TelaRegistros-AcessoAdministrador.png?expires=1786536000&signature=5d4f82387d5329b32da6bd125d4f7bad76a7d914b1b881aef558c25917754743&req=diIlFc5%2BnIBZXvMW3nq%2BgZypeLkILGIBpcIsaxOBwuvsGjcYVjSTXOvW56Fl%0AttO5BTuJsPOTdJlijuYDtxKi2hw%3D%0A)

### Para usuários não administradores:

Clique no **ícone do Sankhya** localizado no **menu superior direito** do Ploomes. Esse ícone está disponível em todas as telas da plataforma.

![Imagem 3: Clique no ícone do Sankhya localizado no menu superior direito do Ploomes. Esse ícone está disponível em todas as telas…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223702737/87912d4776a68702bab630383be4/IntegracaoSankhya-TelaRegistros-AcessoNaoAdministrador.png?expires=1786536000&signature=3b7eff006bfa4a7e50c706cc4fe612af9800fa726b0ee448a543671057880021&req=diIlFc5%2Bn4ZcXvMW3nq%2BgUBN0GZeej0DnOUyc0zW03JXRWZ5ocYESGcmBHGA%0Ad0%2FS9oQB4gazYTmO09rAhrVGT1Y%3D%0A)

**Observação:** usuários não administradores acessam a tela com um filtro fixo pelo usuário logado, exibindo apenas os registros de exportação gerados por eles mesmos.

---

## 3.2) Filtros de consulta

Ao acessar a tela, você pode utilizar filtros para localizar os registros desejados. Os filtros são divididos em **obrigatórios** e **opcionais**.

![Imagem 4: Ao acessar a tela, você pode utilizar filtros para localizar os registros desejados. Os filtros são divididos em…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223707101/957a1d97a360184a342f663b6df2/IntegracaoSankhya-TelaRegistros-FiltrosPendentes.png?expires=1786536000&signature=1956973e666bf91f32f756a347c0e87cce34b998e5f86b714577d5f348c1c924&req=diIlFc5%2BmoBfWPMW3nq%2Bgb0TgjYZ9nLwS0%2BT6%2FWAkra2Q2Qh4N5%2BHa%2BmLmM8%0A8ksd4DTRAyshri24ghJXNVbJHU8%3D%0A)

**Filtros obrigatórios:**

| Filtro | Descrição |
| --- | --- |
| **Direção da ação** | Define se você deseja consultar registros de importação (Sankhya → Ploomes) ou de exportação (Ploomes → Sankhya). |
| **Entidade Sankhya** | Define qual tipo de entidade você deseja consultar. As opções são: `Parceiro cliente pessoa jurídica`, `Parceiro cliente pessoa física`, `Contato de Cliente`, `Produto e Serviço`, `Grupo de Produto`, `Orçamento`, `Pedido de Venda` e `Nota de Venda`. |
| **Intervalo de datas** | Define o período da consulta. Apenas registros dentro do intervalo selecionado serão exibidos. |

**Filtros opcionais:**

| Filtro | Descrição |
| --- | --- |
| **Usuário Ploomes que gerou a ação** | Permite filtrar registros por um usuário específico que originou a ação. |
| **Status da ação** | Permite filtrar pelo resultado da operação: **Ok** (processada com sucesso) ou **Falhou** (ocorreu erro no processamento). |
| **ID do item no Ploomes** | Permite buscar todos os registros vinculados a um item específico a partir do seu ID no Ploomes. |
| **ID do item no Sankhya** | Permite buscar todos os registros vinculados a um item específico a partir do seu ID no Sankhya.  Para Propostas do Ploomes, deve-se buscar pelo **código** da Proposta e não pelo ID. Para os demais cadastros utiliza-se o ID. |
| **Tipo de ação** | Permite filtrar pelo tipo de operação realizada pela integração. |

Após definir os filtros desejados, a tabela será atualizada exibindo apenas os registros compatíveis com os critérios aplicados.

---

## 3.3) Consultando registros de importação

Para visualizar os registros de dados importados do Sankhya para o Ploomes, selecione **Direção da ação = Sankhya** → **Ploomes** nos filtros de consulta.

Em seguida, defina a **Entidade Sankhya** e o **Intervalo de datas** desejados, e utilize os filtros opcionais caso precise refinar a busca.

A tabela exibirá todos os registros de importação que atendem aos critérios selecionados.

![Imagem 5: A tabela exibirá todos os registros de importação que atendem aos critérios selecionados.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223731696/d7a9431383c071a74d0c3e2caabb/IntegracaoSankhya-TelaRegistros-FiltroImportacao-Rule1.png?expires=1786536000&signature=1a1b2b529fe42c876c5d90bca3b4c9cac87aa5b12eda36a6980aa6f4b3cbc525&req=diIlFc59nIdWX%2FMW3nq%2BgSGJc9YyyVksTp6Lc3VwRIJtxtN1yxaEIRVTDAAr%0A7l8Fw5jQYKQZ0i%2Flle0FlYum%2B2U%3D%0A)

---

## 3.4) Consultando registros de exportação

Para visualizar os registros de dados exportados do Ploomes para o Sankhya, selecione **Direção da ação = Ploomes** → **Sankhya** nos filtros de consulta.

Em seguida, defina a **Entidade Sankhya** e o **Intervalo de datas** desejados, e utilize os filtros opcionais caso precise refinar a busca.

A tabela exibirá todos os registros de exportação que atendem aos critérios selecionados.

![Imagem 6: A tabela exibirá todos os registros de exportação que atendem aos critérios selecionados.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223732823/5fd3d3ae584787641b686258ef91/IntegracaoSankhya-TelaRegistros-FiltroExportacao-Rule1.png?expires=1786536000&signature=cb2bd459d1998572a08c4a86337cccb346e8e4666326bb4d8fb4cec4baaced4b&req=diIlFc59n4ldWvMW3nq%2BgdMI%2FTra5ZqMKBWDoEPOT6wKXsn0r3prjNlv6MLQ%0A2fpO5p3wcloM7n7OtOXox7o%2Fi0g%3D%0A)

---

## 3.5) Consultando o histórico de um item específico

Se você precisa investigar tudo o que aconteceu com um item específico na integração, pode buscá-lo diretamente pelo seu ID — seja o ID do Ploomes ou o ID do Sankhya.

**Buscando pelo ID do Ploomes:**

1. No campo de filtro **ID do item no Ploomes**, informe o ID do item desejado.
2. Defina a **Entidade Sankhya** e o **Intervalo de datas**.
3. A tabela exibirá todos os registros (importação e exportação) vinculados a esse item.

**Buscando pelo ID do Sankhya:**

1. No campo de filtro **ID do item no Sankhya**, informe o ID do item desejado.
2. Defina a **Entidade Sankhya** e o **Intervalo de datas**.
3. A tabela exibirá todos os registros (importação e exportação) vinculados a esse item.

![Imagem 7: A tabela exibirá todos os registros (importação e exportação) vinculados a esse item.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223737042/59dce123c9d639e80242ffcba258/IntegracaoSankhya-TelaRegistros-FiltroItemEspecifico.png?expires=1786536000&signature=65089741a510df0b343d03aa5f9f550e792d17a0c3113a8feffb53a6f688d3f2&req=diIlFc59moFbW%2FMW3nq%2BgchR5f0aw%2FK3ZPtVe5bA9y7MaBb8zrgcKBmz3Dfw%0AKUWq4eukui4hTGayp3oR6KJ8dLU%3D%0A)

**Dica:** essa consulta é especialmente útil para auditar o histórico completo de um cadastro ou documento e entender todas as ações que a integração executou para aquele item.

---

## 3.6) Visualizando os detalhes de um registro

Para acessar as informações completas de um registro, clique sobre a linha desejada na tabela. Um **painel de detalhes** será aberto na lateral da tela com todas as informações técnicas do evento.

Abaixo estão listado os campos disponíveis no painel de detalhes:

**Informações do registro:**

| Campo | Descrição |
| --- | --- |
| **Data da ação** | Data e hora em que a ação foi processada pela integração. |
| **ID da ação** | Identificador único do registro da ação. |
| **Data de criação na fila** | Data e hora em que o evento entrou na fila de processamento da integração. |
| **ID da integração** | Identificador da integração na conta. |
| **Direção da ação** | Indica se o registro é de importação (Sankhya → Ploomes) ou exportação (Ploomes → Sankhya). |
| **ID do item no Ploomes** | ID do cadastro ou documento no Ploomes. |
| **ID do item no Sankhya** | ID do cadastro ou documento no Sankhya. |
| **Entidade Ploomes** | Tipo de entidade correspondente no Ploomes. |
| **Entidade Sankhya** | Tipo de entidade correspondente no Sankhya. |
| **Status da ação** | Resultado da operação: **Ok** ou **Falhou**. |
| **Tipo de ação** | Tipo de operação realizada pela integração. |
| **Motivo da falha** | Descrição resumida do erro, caso a ação tenha falhado. |
| **Detalhamento da falha** | Informações adicionais sobre o erro ocorrido. |
| **Quantidade de retries** | Número de tentativas realizadas pela integração para processar a ação. |
| **Usuário Ploomes que gerou a ação** | Usuário do Ploomes responsável pela ação que originou o evento. |

![Imagem 8: Usuário do Ploomes responsável pela ação que originou o evento.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223741796/5a0c8fffbf19128513f10cd71a84/IntegracaoSankhya-TelaRegistros-DetalhesDoRegistro-Info.png?expires=1786536000&signature=871edd6f4e462a15cbb12e4b40a3e3944e2a61ee031650747b0566e467680068&req=diIlFc56nIZWX%2FMW3nq%2BgYZFUaOFSW7xGvXDYMcr6PV%2FqK76CB3m%2BbLM76Ts%0A1tSqQdGYyuSsgnySIOgzGfboxMU%3D%0A)

**Payloads:**

O painel também exibe os payloads do evento em formato JSON:

| Payload | Descrição |
| --- | --- |
| **Dados da ação** | Informações gerais da ação processada. |
| **Payload de requisição** | Dados enviados pela integração ao sistema de destino. |
| **Payload de resposta** | Dados retornados pelo sistema de destino após o processamento. |

![Imagem 9: Dados retornados pelo sistema de destino após o processamento.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223742857/6a6ca34bed24b138d8d4de116238/IntegracaoSankhya-TelaRegistros-DetalhesDoRegistro-Payloads.png?expires=1786536000&signature=b561495033ad0c2d0564325a886873c2edf8709d4d790b18715ceeb893b51f3c&req=diIlFc56n4laXvMW3nq%2BgV6PIUxDx0JDhJ1wDkZFMZt5o%2BxinHzmW7BCgjJ4%0AIR4cZXqqFwlEsPGXS1OzcP%2BGl6o%3D%0A)

**Dica 1:** os campos do painel de detalhes possuem a opção de **copiar o conteúdo**, facilitando o compartilhamento de informações para análise ou suporte.

**Dica 2:** Para copiar os payloads, passe o cursor do mouse sobre a célula com o conteúdo e clique no ícone de copiar.

**Dica 3:** para formatar os payloads com indentação clique no botão "Alternar formatação".

---

## 4) Limitações

- **Consulta somente leitura:** não é possível editar, excluir ou reprocessar registros diretamente pela tela. A consulta é exclusivamente para visualização.
- **Visibilidade limitada para não administradores:** usuários não administradores visualizam apenas os registros de exportação gerados por suas próprias ações.

---

## 5) F.A.Q.

**Por que não consigo ver registros de importação?**

Se você é um usuário não administrador, a tela exibe apenas os registros de exportação gerados pelas suas próprias ações. Para ter acesso aos registros de importação e aos dados de todos os usuários, é necessário ter perfil de administrador.

**Os logs dos eventos somem após a edição da integração?**

Não. A partir da V3 da integração Sankhya, com a nova interface da tela de logs os registros não somem após uma edição da integração.

**Posso editar ou excluir registros pela tela?**

Não. A Tela de Registros do Sankhya é exclusivamente de consulta. Não é possível alterar, excluir ou reprocessar registros por ela.

**Como encontro o registro de um item específico?**

Utilize os filtros **ID do item no Ploomes** ou **ID do item no Sankhya** para buscar diretamente pelo identificador do cadastro ou documento desejado. A tabela exibirá todos os registros de importação e exportação vinculados a esse item e a **Entidade Sankhya** filtrada.

**O que significa o Status da ação "Ok"?**

Significa que a operação foi processada com sucesso pela integração — o dado foi importado ou exportado sem erros.

**O que significa o Status da ação "Falhou"?**

Significa que ocorreu um erro durante o processamento da ação. Para entender o motivo, clique sobre o registro e consulte os campos **Motivo da falha** e **Detalhamento da falha** no painel de detalhes.

**A tela mostra registros em tempo real?**

A tela exibe os registros disponíveis no momento da consulta. Para visualizar novos registros, aplique os filtros desejados novamente ou atualize a página.

---

## 6) Glossário

- **Importação:** processo no qual dados são trazidos do Sankhya para o Ploomes pela integração.
- **Exportação:** processo no qual dados são enviados do Ploomes para o Sankhya pela integração.
- **Direção da ação:** indica o sentido do fluxo de dados do registro — se é uma importação (Sankhya → Ploomes) ou uma exportação (Ploomes → Sankhya).
- **Entidade Sankhya:** tipo de cadastro ou documento no Sankhya ao qual o registro se refere (ex: `Parceiro cliente pessoa jurídica`, `Orçamento`, `Pedido de Venda`, etc.).
- **Entidade Ploomes:** tipo de cadastro ou documento no Ploomes ao qual o registro se refere.
- **Payload:** conjunto de dados técnicos transmitidos ou recebidos pela integração durante o processamento de uma ação. Exibido em formato JSON.
- **Status da ação:** resultado do processamento do registro pela integração — **Ok** (sucesso) ou **Falhou** (erro).
- **Tipo de ação:** classificação da operação realizada pela integração (ex: criação, edição, deleção).
- **Retry:** tentativa automática de reprocessamento que a integração realiza quando uma ação falha.
- **JSON:** formato de texto estruturado utilizado para representar dados de forma organizada em pares de chave e valor.
