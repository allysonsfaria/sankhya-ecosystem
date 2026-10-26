---
id: "42427426594455"
titulo: "Como criar uma automação para inativar clientes sem vendas nos últimos X meses?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427426594455-Como-criar-uma-automa%C3%A7%C3%A3o-para-inativar-clientes-sem-vendas-nos-%C3%BAltimos-X-meses"
trilha: "PLOOMES: Automação de propostas  > Automações"
atualizado_em: "2026-08-10T18:00:52Z"
rotulos: ["sync_hc", "ploomes", "ploomes_14992470", "sync_hash_70b7457e354a"]
---

# Como criar uma automação para inativar clientes sem vendas nos últimos X meses?

Manter a base de clientes atualizada é essencial para garantir que o time comercial foque em oportunidades reais. Com as automações do Ploomes, é possível identificar clientes que estão há um determinado período sem gerar vendas e inativá-los automaticamente, evitando análises manuais e mantendo o CRM organizado.

## Configuração

## 1. Criar uma nova automação

- Acesse **Administração > Automações**
- Selecione a entidade **Cliente**
- Clique em **Nova automação**

[GIF animado: Imagem 1: Clique em Nova automação](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2355058521/e68c5a256a129212e2877cdf4152/vivaldi_q2mEvwENz5.gif?expires=1786536000&signature=34600b8c6b6d1661c4f7a3721b59e0ad2bdf273e50cfe516c0c6814925eaed99&req=diMiE8l7lYRdWPMW3nq%2BgWS1IRwl2FGtCmBqwD164iqYRecrIMoi7r%2ByloxJ%0AcZ5NyFIZL4kHiFWY115s6fKSrZo%3D%0A)

## 2. Configurar descrição, gatilho e filtros

- No campo **Descrição da automação**, informe um nome que identifique a ação
  Exemplo: Inativar clientes sem vendas nos últimos 4 meses

- Em **Quando a automação deve ser disparada**, selecione:

  - Periodicamente
  - Executar automação a cada: 1 dia
  - Iniciar em: data atual (data de sua escolha)
  - Horário: 19:00 (horário de sua escolha)

- Em seguida, clique no ícone **+** para adicionar os filtros. Nessa etapa, configure os seguintes critérios:

  1° Filtro
  **Última venda > Data de criação > Data relativa - diferente de - Últimos 4 meses**

  2° Filtro
  **Status - diferente de - Inativo**

[GIF animado: Imagem 2: 2° Filtro Status - diferente de - Inativo](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2355061552/5bc754e738ea0cff39c3d7f06779/vivaldi_yowWoIeui2.gif?expires=1786536000&signature=be8c43eb2aee0a1c9757720a2c722dd0f8f26789cec18a87cc4b655586534bb7&req=diMiE8l4nIRaW%2FMW3nq%2BgVS4GHjcQ6Nr9qf8%2BK9qGIvm%2Br3rKC6heXfVKX6%2B%0AeODKhRDRPfadNdFlUXcr23cKHNE%3D%0A)

**Observação**: O filtro de data garante que a automação selecione clientes cuja última venda não ocorreu nos últimos X meses. Já o filtro de status evita que clientes já inativos sejam processados novamente.

## 3. Definir a ação

- Em **Ao ser disparada, o que a automação deve fazer?**, selecione:

  - **Editar dados**
  - Em **Selecione um campo**, selecione o campo **Status** e defina o valor como **Inativo**
- Clique em **Salvar**

[GIF animado: Imagem 3: Clique em Salvar](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2355063361/5eea1ea8d093da5c4fcf06120125/vivaldi_q2PZiHRXeF.gif?expires=1786536000&signature=72ca62cf95de1c04efcac7a3b7f5563b29123780e2ce02b8366654910f631afc&req=diMiE8l4noJZWPMW3nq%2BgbmSjEM7OPRl6McnXHk9XAXi7oyYoeVUGjkU8Ea6%0AtiOaBfc2S0%2B%2FOQSY9z0UIYuz4%2Fk%3D%0A)

---

**Este artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
