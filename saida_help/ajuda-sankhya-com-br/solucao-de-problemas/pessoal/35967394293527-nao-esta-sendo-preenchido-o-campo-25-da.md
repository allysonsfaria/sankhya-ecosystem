---
id: "35967394293527"
titulo: "Não está sendo preenchido o campo 25 da GRRF - Mês Anterior a Rescisão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35967394293527-N%C3%A3o-est%C3%A1-sendo-preenchido-o-campo-25-da-GRRF-M%C3%AAs-Anterior-a-Rescis%C3%A3o"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:21:23Z"
rotulos: ["Configuração", "Folha", "zerado", "GRRF", "Rescisão", "FGTS", "Pessoal+", "Não está sendo preenchido", "o campo 25 da GRRF", "Mês", "Anterior", "Calcula Mês Anterior"]
---

# Não está sendo preenchido o campo 25 da GRRF - Mês Anterior a Rescisão

O campo 25 da GRRF (Guia de Recolhimento Rescisório do FGTS) corresponde ao “Mês Anterior à Rescisão”, utilizado para identificar o período de competência imediatamente anterior à data de desligamento do trabalhador. Esse campo é essencial para que a Caixa Econômica Federal possa conferir corretamente os depósitos do FGTS.

Abaixo, temos um exemplo em que esse campo foi gerado com valor “zerado”:

![Imagem 1: Abaixo, temos um exemplo em que esse campo foi gerado com valor “zerado”:](https://ajuda.sankhya.com.br/hc/article_attachments/36182019821591)

**SOLUÇÃO:**

- Acesse o **''Pessoal+''** (Rotinas Folha» Cálculos) na aba **''Info. Tipo Rescisão e FGTS**'' e selecione a opção **''Calcula Mês Anterior'**':

![Imagem 2: Acesse o ''Pessoal+'' (Rotinas Folha» Cálculos) na aba ''Info. Tipo Rescisão e FGTS '' e selecione a opção ''Calcula…](https://ajuda.sankhya.com.br/hc/article_attachments/36182019825047)

- Após a marcação, será exibido automaticamente o evento demonstrativo '**'988 – Base FGTS Mês Anterior**'', apresentando a base de cálculo referente ao mês anterior:

![Imagem 3: Após a marcação, será exibido automaticamente o evento demonstrativo ' '988 – Base FGTS Mês Anterior '', apresentando a…](https://ajuda.sankhya.com.br/hc/article_attachments/36182021045783)

- Em seguida, acesse o portal **''Pessoal+'' (**Rotinas Folha» Geração de Guias), e selecione a opção **''GRRF**'':

![Imagem 4: Em seguida, acesse o portal ''Pessoal+'' ( Rotinas Folha» Geração de Guias), e selecione a opção ''GRRF '':](https://ajuda.sankhya.com.br/hc/article_attachments/36182021047831)

- Ao emitir novamente a guia, ela será gerada com os valores corretos:

![Imagem 5: Ao emitir novamente a guia, ela será gerada com os valores corretos:](https://ajuda.sankhya.com.br/hc/article_attachments/36182019830423)
