---
id: "42427426244503"
titulo: "Como criar uma automação para perder um negócio após X dias sem contato?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427426244503-Como-criar-uma-automa%C3%A7%C3%A3o-para-perder-um-neg%C3%B3cio-ap%C3%B3s-X-dias-sem-contato"
trilha: "PLOOMES: Automação de propostas  > Automações"
atualizado_em: "2026-08-10T18:00:45Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452245", "sync_hash_f8fd3fb15d50"]
---

# Como criar uma automação para perder um negócio após X dias sem contato?

Manter o controle sobre negócios sem interação é essencial para garantir um funil saudável e priorizar oportunidades realmente ativas. Com as automações do Ploomes, é possível perder automaticamente negócios que atingirem um período específico sem contato, utilizando o campo **Último contato** como base e evitando ações manuais.

##

## Configuração

## 1. Criar uma nova automação

- Acesse **Administração > Automações**
- Selecione a entidade **Negócio**
- Clique em **Nova automação**

[GIF animado: Imagem 1: Clique em Nova automação](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2331085718/07ef7581c4239c49362b8075953a/vivaldi_BIDFqxFdFL.gif?expires=1786536000&signature=f019dac8af4c1f9b5eec12e9d96bc3c62702ae8f138d6ac1eea3406f764b8acb&req=diMkF8l2mIZeUfMW3nq%2BgX0VU00uutrFrkCBVoD%2B3T7UllZOJWGzAZ%2BHh2%2F4%0AZAvG%2FomMq3Ci47GvTVBZhhND62c%3D%0A)

## 2. Configurar descrição, gatilho e filtros

- No campo **Descrição da automação**, informe um nome que identifique a ação
  Exemplo: Perder negócio após 45 dias sem contato

- Em **Quando a automação deve ser disparada**, selecione:

  - Periodicamente
  - Executar automação a cada: 1 dia
  - Iniciar em: data atual (data de sua escolha)
  - Horário: 19:00 (horário de sua escolha)

- Em seguida, clique no ícone **+** para adicionar os filtros. Nessa etapa, configure os seguintes critérios:

  1° Filtro
  **Último contato > Data > Data relativa - igual a - Últimos 45 dias**

  2° Filtro
  **Último contato > Data > Data relativa - diferente de - Últimos 44 dias**

[GIF animado: Imagem 2: 2° Filtro Último contato > Data > Data relativa - diferente de - Últimos 44 dias](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2331099185/ff63f02c46f7c9598ca65dbf493b/vivaldi_BIDFqxFdFL.gif?expires=1786536000&signature=77ede6dfefb01fe1a1e73cebca82916e8850314ffc8e6ad560a14d9a348ed6de&req=diMkF8l3lIBXXPMW3nq%2BgVRW9115mCvcPm94pZp%2FYsZUf8ip5SWXfB7TM%2Fgu%0A%2Bxpn%2BOkt3xw89dYJwuDkZREGGTM%3D%0A)

**Observação**: A combinação dos dois filtros garante que a automação selecione apenas os negócios que “bateram” exatamente 45 dias sem contato. Se quiser outro período, basta ajustar os valores (exemplo: 30 dias → igual a Últimos 30 dias e diferente de Últimos 29 dias).

## 3. Definir a ação

- Em **Ao ser disparada, o que a automação deve fazer?**, selecione:

  - **Perder negócio**
  - Em seguida, defina o **motivo de perda** desejado
    Exemplo: **Sem recursos financeiros**
- Clique em **Salvar**

  [GIF animado: Imagem 3: Clique em Salvar](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2331101949/c53a3321664adf2c01009662bd92/vivaldi_Pj27tMPRfa.gif?expires=1786536000&signature=57492a36b2d34e333ecc885ae8b1e9dd9513e24881b92f513c377709efcec213&req=diMkF8h%2BnIhbUPMW3nq%2BgXsKylylGKqkgipTfvm0q9GAm%2F26C4uNgNqay707%0AHIl7%2FNvET6SGNEWe6ERcQsygfPo%3D%0A)

---

**Este artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
