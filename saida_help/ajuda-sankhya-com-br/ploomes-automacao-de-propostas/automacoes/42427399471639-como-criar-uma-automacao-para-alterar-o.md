---
id: "42427399471639"
titulo: "Como criar uma automação para alterar o estágio do negócio e criar uma tarefa ao gerar uma proposta em determinado funil?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427399471639-Como-criar-uma-automa%C3%A7%C3%A3o-para-alterar-o-est%C3%A1gio-do-neg%C3%B3cio-e-criar-uma-tarefa-ao-gerar-uma-proposta-em-determinado-funil"
trilha: "PLOOMES: Automação de propostas  > Automações"
atualizado_em: "2026-08-10T18:00:48Z"
rotulos: ["sync_hc", "ploomes", "ploomes_14993512", "sync_hash_7069d9ead9dc"]
---

# Como criar uma automação para alterar o estágio do negócio e criar uma tarefa ao gerar uma proposta em determinado funil?

Automatizar ações após a criação de propostas ajuda a padronizar processos e garantir que nenhuma etapa importante seja esquecida. Com as automações do Ploomes, é possível atualizar o estágio do negócio automaticamente e criar tarefas para o time dar continuidade no processo comercial.

## Configuração

### 1. Criar uma nova automação

- Acesse **Administração > Automações**

- Selecione a entidade **Proposta**

- Clique em **Nova automação**

[GIF animado: Imagem 1: Clique em Nova automação](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2355180220/597be6f4b9f8e5e4bc9a245a6760/vivaldi_cTsSz85uJL.gif?expires=1786536000&signature=acd64e7c99a8e63b66f8111351c9bc35c5acc8d1b1a03132cbd1899562b4774d&req=diMiE8h2nYNdWfMW3nq%2BgUnoLQrToKaJ02KWZCN4RfJ9SNJ524foc0CyPrbA%0A7RmEKGywe0az8tQNx2X0Sct7634%3D%0A)

## 2. Configurar descrição, gatilho e filtro

- No campo **Descrição da automação**, informe um nome que identifique a ação
  Exemplo: Alterar estágio do negócio e criar tarefa ao gerar proposta
- Em **Quando a automação deve ser disparada**, selecione:

  - **Quando o item for criado**

- Em seguida, clique no ícone **+** para adicionar o filtro:

  Filtro
  **Negócio > Funil - igual a - Funil de vendas**

[GIF animado: Imagem 2: Filtro Negócio > Funil - igual a - Funil de vendas](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2355183278/e93c352756106ed02dd606496a60/vivaldi_kTreA73uJX.gif?expires=1786536000&signature=8d7f74f70c5aff2e3a0be833415309ba82b5fa027fe13ef72092a11173a6212d&req=diMiE8h2noNYUfMW3nq%2Bgf7afAseQQuR%2BKcmzJDZeesqUhdOHOpBWQ8EANiq%0AQrYo2BOpvKkfNa7d4vrEdgmHHIg%3D%0A)

## 3. Configurar a primeira ação (Alterar estágio)

- Em **Ao ser disparada, o que a automação deve fazer?**, selecione:

  - **Editar dados**
  - Em **Selecione um campo**, escolha: **Negócio > Estágio**
  - Defina o estágio desejado
    Exemplo: **Fechamento**

[GIF animado: Imagem 3: Defina o estágio desejado Exemplo: Fechamento](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2355197555/69c09ffc2e656490b69dfb2e6701/vivaldi_pZ7aSq19Pe.gif?expires=1786536000&signature=b96806ddd1b5b62322afad62031641418fd9a3ed409d07eb2d65fd1b65195da9&req=diMiE8h3moRaXPMW3nq%2BgY3%2F%2BgeuZzgixbBf5YAJsEwFfJROSRRd9eOZATqv%0ArcpxN1V9yzmfOrQKJUxUX1vY7g4%3D%0A)

## 4. Configurar a segunda ação (Criar tarefa)

- Clique em **Adicionar nova ação** e selecione:

  - **Criar tarefa**
  - Configure os campos da tarefa conforme sua necessidade:

    **Responsável**
    Exemplo: utilizar campo dinâmico → **Proposta > Responsável**

    **Tipo da tarefa**
    Exemplo: Simples

    **Título**
    Exemplo: Dar andamento na proposta criada

    **Descrição**
    Exemplo: Acompanhar proposta recém-criada e dar sequência no processo comercial.

    **Data**
    Você pode utilizar a opção de dias após a automação para definir o tempo de vencimento da tarefa.
    Exemplo: **3 dias após a automação**

- Clique em **Salvar**

[GIF animado: Imagem 4: Clique em Salvar](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2355202834/ab6d82cd548e7986c73cdd809908/vivaldi_L5DB5BUYER.gif?expires=1786536000&signature=4936275af3bde2197255a1b4e7a3e70208220c12c1b37ada5091dd25436972e3&req=diMiE8t%2Bn4lcXfMW3nq%2BgVun32DZNpytHOEnnUeNDhIqnxFBOWTfDxpObovv%0AqcTm%2FGxPB%2FTtHj9SNPE54EWhYkI%3D%0A)

---

**Este artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
