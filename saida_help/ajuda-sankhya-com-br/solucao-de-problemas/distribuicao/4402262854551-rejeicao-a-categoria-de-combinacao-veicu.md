---
id: "4402262854551"
titulo: "Rejeição: A categoria de combinação veicular deve ser preenchida para o grupo vale pedágio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4402262854551-Rejei%C3%A7%C3%A3o-A-categoria-de-combina%C3%A7%C3%A3o-veicular-deve-ser-preenchida-para-o-grupo-vale-ped%C3%A1gio"
trilha: "Solução de Problemas > Distribuição"
atualizado_em: "2026-07-22T15:24:26Z"
rotulos: ["ERROMDFE", "MDF-e", "Configuração", "Atualização", "Transporte", "Exigir tags categCombVeic e tpValePed.", "Atualizar sistema para versões recentes.", "Preencher \"Tipo do vale pedágio\" e \"Categoria de combinação veicular\"", "Vale Pedágio"]
---

# Rejeição: A categoria de combinação veicular deve ser preenchida para o grupo vale pedágio

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16341850328343) SITUAÇÃO:**

Ao realizar a emissão de MDF-e, quando registradas informações de vale pedágio (valor nota e outros), o sistema está exigindo que as tags categCombVeic e tpValePed sejam enviadas.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16341850329751) SOLUÇÃO:**

![Imagem 3: Realize a atualização do sistema, para as versões abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16341837377047) Realize a atualização do sistema, para as versões abaixo:

- 4.7b629 ou superior
- 4.8b259 ou superior

![Imagem 4: Preencha, conforme informações do seu 'Vale Pedágio', os campos "Tipo do vale pedágio" e "Categoria de combinação…](https://ajuda.sankhya.com.br/hc/article_attachments/16341837378839) Preencha, conforme informações do seu 'Vale Pedágio', os campos **"Tipo do vale pedágio"** e **"Categoria de combinação veicular"** (campos serão apresentados após atualização mencionada no tópico 1);

- Tela **"Viagens de Transporte"**, Aba **"MDF-e"**, Sub-Aba **'Vale Pedágio"**

![Imagem 5: Tela "Viagens de Transporte" , Aba "MDF-e" , Sub-Aba 'Vale Pedágio"](https://ajuda.sankhya.com.br/hc/article_attachments/15079225821463)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16341850337815)CAUSA:**

Quando for emitida um MDF-e, se modal rodoviário e informado o grupo de informações do vale pedágio (<valePed>), a informação da categoria de combinação veicular deverá ser preenchida (<categCombVeic);
