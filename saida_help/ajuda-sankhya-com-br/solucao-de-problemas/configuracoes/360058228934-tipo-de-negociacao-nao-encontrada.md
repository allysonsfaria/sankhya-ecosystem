---
id: "360058228934"
titulo: "Tipo de negociação não encontrada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360058228934-Tipo-de-negocia%C3%A7%C3%A3o-n%C3%A3o-encontrada"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:26:34Z"
rotulos: ["#PUBLIFER", "Configuração", "Tipo de Negociação", "Financeiro", "não apagar", "CORE_E04654", "Correção de Erro de Tipo de Negociação Não Encontrada", "Erro"]
---

# Tipo de negociação não encontrada

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16272245153303) MENSAGEM**:

[CORE\_E04654]  Tipo de negociação não encontrada:

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16272282907415) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Solicite a Equipe de TI da sua empresa ou Terceiro que se certifique de que o horário do servidor de banco de dados não…](https://ajuda.sankhya.com.br/hc/article_attachments/16272282908055) Solicite a Equipe de TI da sua empresa ou Terceiro que se certifique de que o horário do servidor de banco de dados não está adiantado. Caso esteja, solicite o devido ajuste.

![Imagem 4: Após os ajustes feitos, efetue o lançamento do documento novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16272282909463) Após os ajustes feitos, efetue o lançamento do documento novamente.

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16272282910359) OBSERVAÇÃO:**

Caso não tenha um especialista de TI ou DBA, entre em contato com a Unidade ou aloque horas com a Equipe de TI da Sankhya para os devidos ajustes.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16272282911767) CAUSA:**

Ao tentar efetuar algum lançamento ou faturamento que utilize determinado 'Tipo de Negociação', caso o cadastro desse tipo de negociação esteja com **horário superior** ao horário do lançamento que está sendo realizado, o tipo de negociação não será "encontrado", apresentando a mensagem.

- Suponhamos o cadastro do tipo de negociação X;
- O tipo de negociação exemplificado foi cadastrado considerando a data/hora do computador: **29/10 às 15:00.**
- Porém, o **servidor de banco de dados está 2 horas adiantado**, salvando a data/hora desse cadastro: **29/10 às 17:00.**
- Dessa forma, antes que o computador local aponte 17:00h, não será possível utilizar esse cadastro. Justificando a necessidade de ajuste/correção do horário do servidor de banco.
