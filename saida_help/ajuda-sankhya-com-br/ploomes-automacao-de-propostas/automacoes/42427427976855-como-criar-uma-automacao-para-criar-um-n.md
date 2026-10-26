---
id: "42427427976855"
titulo: "Como criar uma automação para criar um negócio para clientes criados há X dias e sem negócio?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427427976855-Como-criar-uma-automa%C3%A7%C3%A3o-para-criar-um-neg%C3%B3cio-para-clientes-criados-h%C3%A1-X-dias-e-sem-neg%C3%B3cio"
trilha: "PLOOMES: Automação de propostas  > Automações"
atualizado_em: "2026-08-10T18:01:24Z"
rotulos: ["sync_hc", "ploomes", "ploomes_14813688", "sync_hash_3e904dad48bd"]
---

# Como criar uma automação para criar um negócio para clientes criados há X dias e sem negócio?

Automatizar a criação de negócios para clientes sem oportunidades registradas é uma forma eficiente de garantir que nenhum contato fique sem acompanhamento. Com as automações do Ploomes, é possível identificar clientes que atingiram um período específico desde a criação e ainda não possuem negócio, criando automaticamente uma nova oportunidade para o time atuar.

## Configuração

## 1. Criar uma nova automação

- Acesse **Administração > Automações**
- Selecione a entidade **Cliente**
- Clique em **Nova automação**

[GIF animado: Imagem 1: Clique em Nova automação](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2331174790/31a069a39b69fc9c713440730031/vivaldi_2NWMBeB9ng.gif?expires=1786536000&signature=9da5e12f05f7117c7167d85e229125003bfcba18fd44a02f0248a8a8669ac851&req=diMkF8h5mYZWWfMW3nq%2BgXWtzRYL4P4JBrsG94yyte4GxfJY1y5qaQ71ubSn%0AcFtCYT8kbXiExdaVB4o03oViiJs%3D%0A)

## 2. Configurar descrição, gatilho e filtros

- No campo **Descrição da automação**, informe um nome que identifique a ação
  Exemplo: Criar negócio para clientes criados há 30 dias sem negócio

- Em **Quando a automação deve ser disparada**, selecione:

  - Periodicamente
  - Executar automação a cada: 1 dia
  - Iniciar em: data atual (data de sua escolha)
  - Horário: 21:00 (horário de sua escolha)

- Em seguida, clique no ícone **+** para adicionar os filtros. Nessa etapa, configure os seguintes critérios:

  1° Filtro
  **Data de criação > Data relativa - igual a - Últimos 30 dias**

  2**°** Filtro
  **Data de criação > Data relativa - diferente de - Últimos 29 dias**

  3° Filtro
  **Último negócio - igual a - vazio**

[GIF animado: Imagem 2: 3° Filtro Último negócio - igual a - vazio](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2331179751/49f34d047a2c1eb98a36af19df50/vivaldi_RrUFo7PAYt.gif?expires=1786536000&signature=c19a325647ea3bb45d39f18532a7b5c8ba8d6298096b90cc6ab87c63684eb8f6&req=diMkF8h5lIZaWPMW3nq%2BgeNDRRCnNg7Iok1nKhbJqphnAt5Q7b0iMP0svNNo%0A0saIgyXPuaoZ6m7HHK7MqUXIaDM%3D%0A)

**Observação**: A combinação dos dois primeiros filtros garante que a automação selecione apenas os clientes que “bateram” exatamente 30 dias desde a criação. Se quiser outro período, basta ajustar os valores (exemplo: 15 dias → igual a Últimos 15 dias e diferente de Últimos 14 dias).

## 3. Definir a ação

- Em **Ao ser disparada, o que a automação deve fazer?**, selecione:

  - **Criar negócio**
  - **Escolha o Funil e estágio** onde o negócio será criado
  - Configure os campos do negócio conforme sua necessidade

    (Você pode preencher os campos com valores fixos ou utilizar a opção de buscar informações de campos do cliente, ajustando o tipo de preenchimento conforme necessário.)
- Clique em **Salvar**

[GIF animado: Imagem 3: Clique em Salvar](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2331183437/92ce2c398d984146531911146a34/vivaldi_ifTyiEmdxs.gif?expires=1786536000&signature=745b19eddc87513a9298466cfcfe3bd01c2c0406e228d3074aaeb0ea497ed3cd&req=diMkF8h2noVcXvMW3nq%2BgcxLqNs9skJi27sk12%2BQ8VvEnQMnkvu3oYGU2kr%2F%0ADfUWL4Bm0dB1EcSvMTKduxpqjUg%3D%0A)

---

**Este artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).

##
