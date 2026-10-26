---
id: "42427378956311"
titulo: "Como registrar a data de entrada de um negócio em um estágio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427378956311-Como-registrar-a-data-de-entrada-de-um-neg%C3%B3cio-em-um-est%C3%A1gio"
trilha: "PLOOMES: Automação de propostas  > Automações"
atualizado_em: "2026-08-10T18:00:20Z"
rotulos: ["sync_hc", "ploomes_5452242", "ploomes", "sync_hash_d8bac62b0034"]
---

# Como registrar a data de entrada de um negócio em um estágio

Registrar a data de entrada em cada etapa do funil é essencial para acompanhar a evolução dos negócios. Com as automações de funil do Ploomes, é possível automatizar esse registro e manter um histórico preciso de cada movimentação.

## Configuração

## 1. Acessar o funil

Acesse o módulo **Negócios** (a nomenclatura pode variar conforme a configuração da conta).
Selecione o funil desejado e clique em **Menu > Configurar funil**.

[GIF animado: Imagem 1: Acesse o módulo Negócios (a nomenclatura pode variar conforme a configuração da conta). Selecione o funil desejado e…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2220898460/d052e64bcbc37b055e89525a0baa/msedge_rtN2dnM2Wi.gif?expires=1786536000&signature=a76883426df9994ef571e093e2206e3c3cf298e17b67995e685f5ad7dd3c2099&req=diIlFsF3lYVZWfMW3nq%2BgSY4YAt04sS%2FzzIlsbTwuLTLy0updCH8K%2BF597jI%0Af6tpQ0dERqJFqPB6w0HKnFHyoLM%3D%0A)

## 2. Criar a automação na etapa

Escolha a etapa desejada (ex.: Primeiros contatos).
Clique em **Configurar automações > Nova automação**.

Preencha a **Descrição** com o objetivo da automação.

[GIF animado: Imagem 2: Preencha a Descrição com o objetivo da automação.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2220902099/bfdc9ac1a62ab897eca7212dfec8/msedge_VG4t7iCgFG.gif?expires=1786536000&signature=2f35dd18f566139a31a0b0ddb1c27db93635b6a0f7917510b6397fe1b255d250&req=diIlFsB%2Bn4FWUPMW3nq%2BgcEC28p1JTQpQ7MCDDNVF2e3NFcZZOA63M1TqcmX%0AJ42htuWhAIkbeSiihHB81Zgi6yI%3D%0A)

## 3. Configurar o gatilho

No gatilho, selecione **Negócio entrou neste estágio**.

[GIF animado: Imagem 3: No gatilho, selecione Negócio entrou neste estágio .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2220903084/81b3b6119179ed470109ad2d0958/msedge_LVEFcs2pTK.gif?expires=1786536000&signature=a344c7e584833bc5b06b8d12614ede2a3c2742950cc03fe445af67eb962d1b30&req=diIlFsB%2BnoFXXfMW3nq%2BgRQqC3g%2Fr6wvgevM5pBT9AGyeI0oXYGaGe3amfC9%0AMSPeWqQk6ZhYE%2F9j1Jrq%2FZt0iTs%3D%0A)

## 4. Definir a ação

Em **Ao ser disparada, o que a automação deve fazer?**, selecione **Editar dados**.
Escolha o campo que armazenará a informação.

Caso o campo não exista, clique em **Criação rápida** e configure:

- Nome: Data de entrada – [nome da etapa]
- Tipo: **Data**

[GIF animado: Imagem 4: Tipo: Data](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2220906449/5c171d7d9fb326fa8479c951e39c/msedge_aZPguqp2Nb.gif?expires=1786536000&signature=98cb9548aac5fcb1bf97e5ad5427c4c010af47978bad4f84a989bcd9ce16415d&req=diIlFsB%2Bm4VbUPMW3nq%2BgXe%2B85A1Swj65P%2BRS5cAx1hh%2FTZutK0ZC92pFrZc%0AsxtEPHfRzkidLhH9NvPxbps81vc%3D%0A)

## 5. Configurar o preenchimento

Defina o tipo de preenchimento como **Dias após a automação = 0**.
Esse valor garante que o campo seja preenchido com a data em que a automação for executada.

[GIF animado: Imagem 5: Defina o tipo de preenchimento como Dias após a automação = 0 . Esse valor garante que o campo seja preenchido com a…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2220909726/880be7f83bb1843c17d6732fda64/msedge_7ZqbNW1mMc.gif?expires=1786536000&signature=59af31e4ce32b6290eb20070d4fea642ec7c5869c1c6a2a5794a4246e538f099&req=diIlFsB%2BlIZdX%2FMW3nq%2BgQiGoxR0VU%2BUvMYsMRjiAgIyO80s%2ByKTdIQu%2B7W8%0A8w4iJ24TVWIaJi4Sxr268xpzNWs%3D%0A)

## 6. Adicionar condição para evitar sobrescrita

Adicione um filtro:
**[Campo criado] > Vazio**

Essa configuração impede que a data seja sobrescrita caso o negócio retorne à mesma etapa.

[GIF animado: Imagem 6: Essa configuração impede que a data seja sobrescrita caso o negócio retorne à mesma etapa.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2220911450/fc80f3dc17190fe6ec096b432d24/msedge_1FihaIwID7.gif?expires=1786536000&signature=a49acfea7fe24fcf65f2a8c8b4429883e4f33d03978d91df1ef4547a6467664b&req=diIlFsB%2FnIVaWfMW3nq%2BgYABMtBd0gRixq11aTGKLh6aso17fm399Peb2hgK%0AM8vlE8CdycvoihMHz516yguZBJE%3D%0A)

## 7. Salvar a automação

Clique em **Salvar** para concluir a configuração.

[GIF animado: Imagem 7: Clique em Salvar para concluir a configuração.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2220913312/dcc377b75cc4213a63d3cb86f0d6/msedge_kt5LaiOPU9.gif?expires=1786536000&signature=d423e872368bb2e848700f02ac47a1e623e2be4e5a46d6bbab7c66e96aca9f96&req=diIlFsB%2FnoJeW%2FMW3nq%2BgWQcG2ijM1RomedPjRPvOKcRkXVna8oxNwOC5jQ7%0AmPg40YcjdYOo2LqC8fyWGN2hXlU%3D%0A)

🧩 **Dica**: Se precisar registrar a data de entrada para mais de uma etapa, repita o processo, criando um campo de data específico para cada uma delas. Utilize a opção de duplicação de automações para facilitar a criação das automações.

![Imagem 8: 🧩 Dica : Se precisar registrar a data de entrada para mais de uma etapa, repita o processo, criando um campo de data…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2220915601/725976bc6d350943bcf1095a9d00/image.png?expires=1786536000&signature=a3c315b1b19e8c0f6b27bb0f09113705b3e34c739e24d7a2ad8967c37c68daae&req=diIlFsB%2FmIdfWPMW3nq%2BgSqs86CwBDfJI2UYMMiY1Mms%2FnKwFnQGhQmUsMUI%0ASuRtSTGhH2swZjZY%2BCTHqAtcix0%3D%0A)

---

**Este artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
