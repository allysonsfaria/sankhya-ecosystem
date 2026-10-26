---
id: "42427469124375"
titulo: "Utilizando o Fluxo de Aprovação como filtro de exportação na integração Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427469124375-Utilizando-o-Fluxo-de-Aprova%C3%A7%C3%A3o-como-filtro-de-exporta%C3%A7%C3%A3o-na-integra%C3%A7%C3%A3o-Sankhya"
trilha: "PLOOMES: Automação de propostas  > Geral"
atualizado_em: "2026-08-11T16:14:48Z"
rotulos: ["sync_hc", "ploomes", "ploomes_14328040", "sync_hash_04b277a381c2"]
---

# Utilizando o Fluxo de Aprovação como filtro de exportação na integração Sankhya

## 1) Sobre o Fluxo de Aprovação como filtro de exportação na integração Sankhya

A integração Sankhya agora permite que você utilize o **[Fluxo de Aprovação do Ploomes](https://sankhya.zendesk.com/hc/pt-br/articles/42427442681111)** como critério para controlar quais Propostas e Vendas serão exportadas ao Sankhya. Na prática, isso significa que você pode configurar a integração para que **apenas documentos aprovados no Ploomes** sejam enviados como Orçamentos ou Pedidos de Venda ao Sankhya.

Esse recurso é especialmente útil para empresas que possuem processos internos de validação antes de oficializar um documento no ERP. Com o filtro de exportação por status de aprovação, você garante que nenhum documento pendente ou reprovado chegue ao Sankhya antes da hora — mantendo a consistência entre o CRM e o ERP.

A integração monitora automaticamente as mudanças de status de aprovação no Ploomes. Não é necessário configurar nada além do próprio filtro de exportação: ao ativar um gatilho de exportação para Propostas ou Vendas, a integração já se prepara para acompanhar os eventos do Fluxo de Aprovação.

---

## 2) Pré-requisitos

- Possuir a **integração Sankhya V3** ativa na conta Ploomes.
- Ter ao menos um **gatilho de exportação ativo** para Propostas e/ou Vendas.
- Possuir um **Fluxo de Aprovação configurado no Ploomes** para Propostas e/ou Vendas.

---

## 3) Configurando o filtro de exportação por Status de Aprovação

Para que a integração exporte apenas documentos aprovados, é necessário configurar um filtro de exportação utilizando o campo **Situação da Aprovação**. Essa configuração é feita diretamente na tela de configuração da integração Sankhya, de forma separada para Propostas e para Vendas.

## 3.1) Acessando os filtros de exportação

Acesse a tela de configuração da integração Sankhya no Ploomes e localize a seção de filtros de exportação referente à entidade desejada — **Propostas** ou **Vendas**.

![Imagem 1: Acesse a tela de configuração da integração Sankhya no Ploomes e localize a seção de filtros de exportação referente à…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223441388/e3be271dd74aaf1819312c07f1fb/IntegracaoSankhya-FiltroExportacaoProposta.png?expires=1786536000&signature=6f35b3fa89c950cf77263cbd75edcdb11342e5357c724b7f723a555c9ffda75b&req=diIlFc16nIJXUfMW3nq%2BgVXyzv9X7FvNc2MMGzf9ElU2FOfhgTx8j1rVIu5G%0A%2Fy8MkzGcyTIVUYyqpxElTREgNSk%3D%0A)

Exemplo da seção de configuração de Orçamentos (Propostas) sem nenhum filtro de exportação configurado.

## 3.2) Adicionando o campo Status de Aprovação como critério

O campo **Situação da Aprovação** estará disponível automaticamente entre as opções de filtro. Selecione-o e defina o critério desejado. Por exemplo:

- **Status de Aprovação = Aprovado** — exportará apenas documentos que já foram aprovados no Fluxo de Aprovação do Ploomes.

![Imagem 2: Status de Aprovação = Aprovado — exportará apenas documentos que já foram aprovados no Fluxo de Aprovação do Ploomes.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223448213/58d7308b9b81f3c23bac21fbca46/IntegracaoSankhya-FiltroExportacaoProposta_FluxoAprovacao.png?expires=1786536000&signature=8a5c87a15a6b12e56e855957de5a87f5357d32cb2674c4bd05b11de9c1be4f5a&req=diIlFc16lYNeWvMW3nq%2BgfapFn3i%2F9pi9a%2Five0TC075Z8WaxkKFQyZjf4l7%0ACOYCejIWwwjdA3%2FrrXNOuFGnjzg%3D%0A)

Exemplo de configuração do filtro de exportação para Propostas com o campo "Situação da Aprovação" selecionado e o valor "Aprovada" definido.

![Imagem 3: Exemplo de configuração do filtro de exportação para Propostas com o campo "Situação da Aprovação" selecionado e o…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223451271/a521b84ff02c1230183b2d9b551e/IntegracaoSankhya-FiltroExportacaoVenda_FluxoAprovacao.png?expires=1786536000&signature=aac755efad3ff0fac53233ba2618a6d258c13f989093dd46d900950bec8142f7&req=diIlFc17nINYWPMW3nq%2BgSCfC%2B%2Fi6TRCa39E1BInMwx6zabe2CPZ7Vfcogzu%0AN3UqH7mSCdY4sEL92f3Y9OyP0P0%3D%0A)

Exemplo de configuração do filtro de exportação para Vendas com o campo "Situação da Aprovação" selecionado e o valor "Aprovada" definido.

## 3.3) Salvando a configuração

Após definir o filtro, salve as configurações da integração. A partir desse momento, a integração passará a considerar o status de aprovação como critério para decidir se um documento será exportado ao Sankhya.

**Importante:** os filtros de exportação de Propostas e Vendas são configurados de forma independente. Caso deseje utilizar o filtro de aprovação para ambos, será necessário configurá-lo em cada um separadamente.

---

## 4) Utilizando o Fluxo de Aprovação como filtro de exportação

Com o filtro configurado, a integração passa a avaliar automaticamente o status de aprovação dos documentos antes de exportá-los ao Sankhya. Abaixo estão os principais cenários de uso no dia a dia.

## 4.1) Documento aprovado e exportado ao Sankhya

Quando uma Proposta ou Venda passa pelo Fluxo de Aprovação no Ploomes e recebe o status de **Aprovado**, a integração identifica que o documento atende ao filtro de exportação configurado.

**O que acontece:**

1. O documento é aprovado no Fluxo de Aprovação do Ploomes.
2. A integração detecta a mudança de status automaticamente.
3. A integração valida que o documento atende ao filtro de exportação (ex: Situação da Aprovação = Aprovada).
4. Os dados do documento são exportados ao Sankhya como Orçamento (para Propostas) ou Pedido de Venda (para Vendas), incluindo os dados de produtos da proposta ou da venda vinculados.

## 4.2) Documento ainda não aprovado (retenção temporária)

Quando um documento é criado ou editado no Ploomes, mas a sua situação da aprovação ainda não atende ao filtro configurado (por exemplo, está como **Pendente** ou **Reprovado**), a integração retém temporariamente os dados desse documento e não os exporta ao Sankhya.

**O que acontece:**

1. O documento é criado ou editado no Ploomes, mas ainda não está aprovado.
2. A integração detecta o evento e avalia o filtro de exportação.
3. Como o documento não atende ao critério (ex: situação diferente de "Aprovada"), a exportação é retida.
4. Caso o documento receba novas edições enquanto estiver retido, a integração acumula essas alterações automaticamente para que nenhuma informação se perca.

**Na prática:** o documento fica "na fila de espera" da integração até que o status de aprovação mude para um valor que atenda ao filtro. Todas as edições realizadas nesse período são acumuladas por até 30 dias e serão enviadas de uma só vez quando a exportação for liberada.

## 4.3) Documento aprovado após edições (liberação da retenção)

Quando um documento que estava retido finalmente recebe o status de **Aprovado** no Fluxo de Aprovação, a integração libera a exportação automaticamente.

**O que acontece:**

1. O documento recebe o status de aprovação que atende ao filtro configurado.
2. A integração detecta a mudança de status automaticamente.
3. A integração reúne todas as edições acumuladas durante o período de retenção e as combina com os dados mais recentes do documento.
4. Os dados completos são exportados ao Sankhya, garantindo que todas as alterações feitas antes e durante o período de retenção cheguem ao ERP.

**Importante:** a exportação de Propostas e Vendas inclui automaticamente os dados de produtos vinculados ao documento, garantindo que o Orçamento ou Pedido de Venda chegue completo ao Sankhya.

## 4.4) Exportação sem filtro de aprovação configurado

Caso você não configure nenhum filtro de exportação que utilize o campo de Situação da Aprovação, as mudanças no Fluxo de Aprovação não impactarão o comportamento da exportação. Nesse cenário, as Propostas e Vendas serão exportadas ao Sankhya seguindo o fluxo padrão de criação e edição, independentemente do status de aprovação do documento.

---

## 5) Limitações

- **Aplicável apenas a Propostas e Vendas:** o filtro por Situação da Aprovação está disponível somente para as regras de exportação de Propostas e Vendas. Não se aplica a Clientes, Parceiros ou outras entidades.
- **Retenção temporária de até 30 dias:** os dados de documentos retidos por não atenderem ao filtro de exportação são armazenados por no máximo 30 dias. Após esse período, os dados retidos são descartados.
- **Máximo de 5 tentativas por exportação:** em caso de falha na exportação ao Sankhya, a integração realizará até 5 tentativas automáticas por documento. Se todas falharem, a exportação não será enviada e o erro registrado nos logs.
- **Exportações bloqueadas não constam na tela de registros:** os dados de registros bloqueados não constam na tela de registros, pois não são armazenados no histórico os logs de cadastros que foram barrados no filtro de exportação.

---

## 6) F.A.Q.

**Preciso configurar webhooks manualmente para que o filtro de aprovação funcione?** Não. A integração cria e gerencia os webhooks de Fluxo de Aprovação automaticamente ao ativar qualquer gatilho de exportação para Propostas ou Vendas. Nenhuma ação manual é necessária.

**Posso usar o filtro de aprovação apenas para Vendas e não para Propostas?** Sim. Os filtros de exportação de Propostas e Vendas são configurados de forma independente. Você pode adicionar o critério de Status de Aprovação apenas na entidade que desejar.

**O que acontece se minha Proposta for reprovada no Fluxo de Aprovação?** Se o filtro de exportação estiver configurado como "Situação da Aprovação = Aprovada", a Proposta reprovada não será exportada ao Sankhya. Ela ficará retida na integração. Caso o status seja alterado para "Aprovada" posteriormente, a integração liberará a exportação com todos os dados acumulados.

**As edições feitas em um documento enquanto ele está retido serão perdidas?** Não. A integração acumula automaticamente todas as edições realizadas no documento durante o período de retenção. Quando o documento for aprovado e a exportação liberada, todas as alterações acumuladas serão enviadas ao Sankhya de uma só vez.

**O que acontece se eu remover o filtro de aprovação depois de já tê-lo configurado?** Ao remover o filtro, as exportações voltarão a seguir o fluxo padrão de criação e edição. Documentos que estiverem retidos no momento da remoção serão avaliados novamente e poderão ser exportados normalmente, já que não haverá mais critério de aprovação bloqueando o envio.

---

## 7) Glossário

- **Fluxo de Aprovação:** funcionalidade do Ploomes que permite configurar etapas de validação e aprovação para documentos como Propostas e Vendas antes que possam ser considerados oficiais.
- **Situação da Aprovação:** campo que indica a situação atual de um documento dentro do Fluxo de Aprovação (ex: Pendente, Aprovada, Reprovada).
- **Filtro de exportação:** regra configurada na integração Sankhya que define quais critérios um documento precisa atender para ser exportado ao ERP.
- **Gatilho de exportação:** configuração que habilita a exportação automática de dados do Ploomes para o Sankhya quando determinados eventos ocorrem (ex: criação ou edição de um documento).
- **Retenção de exportação:** estado temporário no qual um documento fica "em espera" na integração por não atender ao filtro de exportação configurado. Os dados são acumulados até que o critério seja atendido.
- **Delta:** conjunto de alterações (edições) realizadas em um documento desde a última exportação bem-sucedida ou desde a sua retenção.
- **Webhook:** mecanismo automático que notifica a integração quando um evento relevante ocorre no Ploomes (como aprovação, criação ou edição de um documento).
