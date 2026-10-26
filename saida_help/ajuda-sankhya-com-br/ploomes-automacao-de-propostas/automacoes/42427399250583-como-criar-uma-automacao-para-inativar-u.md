---
id: "42427399250583"
titulo: "Como criar uma automação para inativar um cliente após X dias sem contato?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427399250583-Como-criar-uma-automa%C3%A7%C3%A3o-para-inativar-um-cliente-ap%C3%B3s-X-dias-sem-contato"
trilha: "PLOOMES: Automação de propostas  > Automações"
atualizado_em: "2026-08-10T18:00:44Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452244", "sync_hash_4705b1ebe677"]
---

# Como criar uma automação para inativar um cliente após X dias sem contato?

Registrar quando um cliente fica há **X dias sem contato** é essencial para manter a base organizada e garantir que o time foque nos cadastros realmente ativos. Com as automações do Ploomes, é possível **inativar clientes automaticamente** após esse período, usando o campo **Último contato** como referência e evitando retrabalho em atualizações manuais.

## Configuração

## 1. Criar uma nova automação

- Acesse **Administração > Automações**
- Selecione a entidade **Cliente**
- Clique em **Nova automação**

[GIF animado: Imagem 1: Clique em Nova automação](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2279700015/1a820ecd0d609d486a2f058502ff/vivaldi_toJgcntxkl.gif?expires=1786536000&signature=8c8c17374faea608fabf6213303aafb564987972cf370cdf10de9bfeaf09622e&req=diIgH85%2BnYFeXPMW3nq%2BgUJPtFVKH%2BetVTXhVKCAh61EazQTN5tKl2WXS9bE%0AXiE%2FfqRNcmw1z4s7qnj8EzS2r6M%3D%0A)

## 2. Configurar descrição, gatilho e filtros

- No campo **Descrição da automação**, informe um nome que identifique a ação
  Exemplo: Inativar clientes após 30 dias sem contato
- Em **Quando a automação deve ser disparada**, selecione:

  - Periodicamente
  - Executar automação a cada: 1 dia
  - Iniciar em: data atual (data de sua escolha)
  - Horário: 23:00 (horário de sua escolha)
- Em seguida, clique no ícone **+** para adicionar os filtros. Nessa etapa, configure os seguintes critérios:

  1° Filtro
  **Último contato** > **Data** > **Data relativa** - **igual a** - **Últimos 30 dias**

  2° Filtro
  **Último contato** > **Data** > **Data relativa -**  **diferente de** - **Últimos 29 dias**

  3° Filtro
  **Status** - **diferente de -** **Inativo**

[GIF animado: Imagem 2: 3° Filtro Status - diferente de - Inativo](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2279722632/d16b01609d5b2e1fa94f3dcc53b9/vivaldi_FQ5OzLFd5A.gif?expires=1786536000&signature=bc7d8576422599d295aced1299d0c54975f6e31a652b07f1e30905864aa5dfdb&req=diIgH858n4dcW%2FMW3nq%2BgYhcASy4KbZ1lfa0nv2mUSgDjGBne3R%2Bud0xZoMJ%0AkUs9vr47LNyiQuTxS4Pd7NrtHfc%3D%0A)

**Observação**: A combinação dos dois primeiros filtros garante que a automação selecione apenas os clientes que “bateram” exatamente 30 dias sem contato. Se você quiser considerar 2 meses, por exemplo, pode converter para dias e ajustar para igual a Últimos 60 dias e diferente de Últimos 59 dias.)

## 3. Definir a ação

- Em **Ao ser disparada, o que a automação deve fazer?**, selecione:

  - **Editar dados**
- Em **Selecione um campo**, selecione:

  - **Status**
  - Defina o valor como **Inativo**
- Clique em **Salvar**

[GIF animado: Imagem 3: Clique em Salvar](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2279727173/9e20cb349c590021112ac8486475/vivaldi_u3y4pBVZKf.gif?expires=1786536000&signature=18111a6ba4daaebb78948fc6345aa27aaccd99b165004c1d904f068f95cf653e&req=diIgH858moBYWvMW3nq%2BgUbl3FuEWGzJRjBsSVVSqdSZzKxq6Wua4xtXWtjP%0AzqvWI74rJ197kqGyzQ1TvjLNDF8%3D%0A)

---

**Este artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
