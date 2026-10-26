---
id: "42427412904343"
titulo: "Como criar uma automação para registrar uma interação quando a proposta for aceita pelo cliente?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427412904343-Como-criar-uma-automa%C3%A7%C3%A3o-para-registrar-uma-intera%C3%A7%C3%A3o-quando-a-proposta-for-aceita-pelo-cliente"
trilha: "PLOOMES: Automação de propostas  > Automações"
atualizado_em: "2026-08-10T18:00:42Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452247", "sync_hash_ceca9bcf0a51"]
---

# Como criar uma automação para registrar uma interação quando a proposta for aceita pelo cliente?

Registrar quando uma proposta é aceita pelo cliente é essencial para garantir um acompanhamento ágil e assertivo do processo comercial. Com as automações do Ploomes, é possível automatizar a criação de interações nesse momento, garantindo que o time seja acionado imediatamente após a aprovação.

## Configuração

## 1. Criar uma nova automação

- Acesse **Administração > Automações**
- Selecione a entidade **Proposta**
- Clique em **Nova automação**

[GIF animado: Imagem 1: Clique em Nova automação](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2275567035/ee24c0b83b69151ff2c112d9f323/vivaldi_2uxpVa5BqC.gif?expires=1786536000&signature=db0cc74aad3d16db0a6cc3f7d304c8fd495770c24afc957ab63a00cc68e0c86c&req=diIgE8x4moFcXPMW3nq%2BgTngRjobx8SXB0yQRLUv8RUq7tPd00RCeqJBqr6P%0Av84e9g7h8ZoRfY7reSe9HTCiDfQ%3D%0A)

## 2. Configurar descrição, gatilho e filtros

- No campo **Descrição da automação**, informe um nome que identifique a ação
  Exemplo: Criar interação quando proposta for aceita

- Em **Quando a automação deve ser disparada**, selecione:
  **Quando a proposta for aprovada ou reprovada (online)**
- Em seguida, clique no ícone **+** para adicionar um filtro. Nessa etapa, configure os seguintes critérios:

  1° Filtro

  **Negócio > Funil** igual a **[Nome do funil]** (filtro opcional)
  (A nomenclatura pode variar conforme a conta — “Negócio”, “Workflow”, etc.)

  2° Filtro

  **Aceita externamente** igual a **Sim** (obrigatório)

[GIF animado: Imagem 2: Aceita externamente igual a Sim (obrigatório)](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2275573256/27b538895e16b1b29ab1f4152304/vivaldi_eAs2UxAVJe.gif?expires=1786536000&signature=b8b83c2e543e784145f020b5df0d7f3fe786954270a86fac2d6ac8200a0f02ed&req=diIgE8x5noNaX%2FMW3nq%2BgQdV1IagmiYCtxLA5R9SP5SV9mOosuo5xGy5BDmH%0ATTtQIbAzhL35GFV9c3Su4zlxJMQ%3D%0A)

## 3. Definir a ação

- Em **Ao ser disparada, o que a automação deve fazer?**, selecione:
  **Criar registro de interação**
- Em seguida configure os campos referente ao registro que será criado:

  - **Tipo de interação**: selecione o tipo de interação que deseja (ex: Telefone)
  - **Data**: Neste caso será utilizado 'Dias após a automação = 0' para que a data do registro seja preenchida com a data atual
  - **Descrição**: Informe um texto descritivo
    Exemplo: Cliente aceitou a proposta, faça contato!
  - Clique em **salvar**

[GIF animado: Imagem 3: Clique em salvar](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2275632893/08c33790fe2a3aa2b9a5de923512/vivaldi_tndmiRGWhV.gif?expires=1786536000&signature=756dc482cf6fdd8f828452b127a282224285617fd8df8348596c7e9757a28557&req=diIgE899n4lWWvMW3nq%2BgdQ3BzLepxLA3Iwj9A5Db2C7E9dfPVXrV3SoP34F%0Axhw4dP4wET9qAZoauDdSOylSLCI%3D%0A)

---

**Este artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
