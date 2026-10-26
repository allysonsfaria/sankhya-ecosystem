---
id: "4403858563735"
titulo: "Obrigatória a informação do identificador do CSRT e do Hash do CSRT"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403858563735-Obrigat%C3%B3ria-a-informa%C3%A7%C3%A3o-do-identificador-do-CSRT-e-do-Hash-do-CSRT"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:23:34Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "Preferências", "#criadoFer", "O.S1765538", "975", "Identificador e Hash do CSRT obrigatórios"]
---

# Obrigatória a informação do identificador do CSRT e do Hash do CSRT

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16345568272023) **MENSAGEM:**

[975 - Rejeição]: Obrigatória a informação do identificador do CSRT e do Hash do CSRT

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16345552509591) SOLUÇÃO:**

![Imagem 3: Acesse a tela "Preferências" e ligue o parâmetro "ENVTAGCSRTHOM" :](https://ajuda.sankhya.com.br/hc/article_attachments/16345552512151) Acesse a tela **"Preferências"** e ligue o parâmetro **"ENVTAGCSRTHOM"**:

- Quando ele estiver ligado e o ambiente da NF-e for Homologação, as tags idCSRT e hashCSRT do grupo infRespTec serão geradas com os valores fixos para que a nota não seja rejeitada;

![Imagem 4: Quando ele estiver ligado e o ambiente da NF-e for Homologação, as tags idCSRT e hashCSRT do grupo infRespTec serão…](https://ajuda.sankhya.com.br/hc/article_attachments/15083151330455)

**![Imagem 5: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16345552514071) IMPORTANTE:**

**(1)** O parâmetro foi implementado na **versão 4.8b327 ou superior**;

**(1)** O parâmetro ENVTAGCSRTHOM foi criado com default desligado para manter a funcionalidade anterior do sistema.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16345568288151)CAUSA:**

Se informado o grupo do Responsável Técnico é obrigatório a informação do identificador do CSRT (<idCSRT) e Hash do CSRT (<hashCSRT>);

**OBSERVAÇÃO:** Implementação a critério da UF.
