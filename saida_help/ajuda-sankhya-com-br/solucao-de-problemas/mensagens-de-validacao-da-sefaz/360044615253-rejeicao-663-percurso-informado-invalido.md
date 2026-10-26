---
id: "360044615253"
titulo: "Rejeição 663: Percurso informado inválido - MDF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615253-Rejei%C3%A7%C3%A3o-663-Percurso-informado-inv%C3%A1lido-MDF-e"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-10-13T14:00:37Z"
rotulos: ["#criadoRoger", "ERROMDFE", "MDF-e", "Configuração", "SEFAZ", "Transporte", "Percurso Inválido no MDF-e", "Rejeição 663"]
---

# Rejeição 663: Percurso informado inválido - MDF-e

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16813411557783) **MENSAGEM:**

Rejeição 663: Percurso informado inválido - Como resolver?

![Imagem 2: SITUAÇÃO 1:](https://ajuda.sankhya.com.br/hc/article_attachments/32394664745495) **SITUAÇÃO 1:**

Foi emitido um MDFe onde o transporte será iniciado no Estado Brasília (DF) e será concluído no Estado do Mato Grosso  (MT). **Os Estados não fazem fronteira e o percurso não foi informado.**

![Imagem 3: SITUAÇÃO 2:](https://ajuda.sankhya.com.br/hc/article_attachments/32394664745495) **SITUAÇÃO 2:**

Foi emitido MDFe onde o transporte será iniciado em Minas Gerais e finalizado em São Paulo. **Os Estados são fronteiriços, no entanto foi informado o percurso.**

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16813427758103)SOLUÇÃO:**

**(1)** Para a **situação 1,**vá até a tela **"Viagens"**(Comercial » Rotinas » Viagens de Transporte (MDF-e), selecione a viagem em questão, acesse a aba **"MDF-e",**em seguida, sub aba **"UFs do percurso"** e preencha corretamente o percurso no qual o transporte da mercadoria irá transitar, considerando todos os Estados que estão entre as fronteiras dos Estados início e fim da viagem. No caso da **situação 1**, coloque a UF do Estado de Goiás.

**(1)** Para a **situação 2,** vá até a tela Viagens, selecione a viagem em questão, acesse a aba MDF-e, em seguida, sub aba UFs do percurso e remova as UF's que estiverem cadastradas. Pois, os Estados são fronteiriços e suas UF's já foram informadas anteriormente.

![Imagem 5: (1) Para a situação 2, vá até a tela Viagens, selecione a viagem em questão, acesse a aba MDF-e , em seguida, sub aba…](https://ajuda.sankhya.com.br/hc/article_attachments/32405908998551)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16813411580183)CAUSA:**

A rejeição é apresentada quando os **Estados início e fim não fazem fronteira e não foi informado o percurso**. Também, quando os **Estados são fronteiriços e foi informado um percurso.**
