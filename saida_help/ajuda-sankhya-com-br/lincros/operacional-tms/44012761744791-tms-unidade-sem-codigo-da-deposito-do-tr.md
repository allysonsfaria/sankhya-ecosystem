---
id: "44012761744791"
titulo: "[TMS] Unidade sem código da depósito do Tracking"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012761744791--TMS-Unidade-sem-c%C3%B3digo-da-dep%C3%B3sito-do-Tracking"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:37:38Z"
rotulos: ["sync_hc", "lincros", "lincros_13433288", "sync_hash_3474eccdd6d2"]
---

# [TMS] Unidade sem código da depósito do Tracking

**Menu:** Operacional > Cargas > Embarques

**Objetivo:** Entender como ajustar os cadastros no TMS, para que o NiFi possa integrar o embarque com o Tracking, em caso de críticas na integração.

**Considerações:** Utilizar integração (TMS > TRK) de embarques via NiFi

Caso na integração de um embarque entre os sistemas, TMS e Tracking, que ocorra via NiFi, seja gravada a seguinte mensagem no campo de integração do embarque: Unidade sem código da depósito do Tracking.

![Imagem 1: Caso na integração de um embarque entre os sistemas, TMS e Tracking, que ocorra via NiFi, seja gravada a seguinte…](https://ajuda.sankhya.com.br/hc/article_attachments/44012748308503)

 Será necessário realizar o procedimento abaixo para ajustes:

**1.** Na aba "Cadastro" do embarque, deverá clicar no lápis ao lado do campo "Unidade".

![Imagem 2: 1. Na aba "Cadastro" do embarque, deverá clicar no lápis ao lado do campo "Unidade".](https://ajuda.sankhya.com.br/hc/article_attachments/44012762096663)

**2.** Será aberta a tela de "Cadastro de Unidade". Clique no lápis para acessar o "Cadastro de pessoa".

![Imagem 3: 2. Será aberta a tela de "Cadastro de Unidade". Clique no lápis para acessar o "Cadastro de pessoa".](https://ajuda.sankhya.com.br/hc/article_attachments/44012731650455)

**3.** Desça até o campo "**Informações da pessoa**" e acrescente (ou edite) os parâmetros "GE\_CODEMPRESA", que se refere ao **código da unidade de negócio** no Tracking, e "GE\_DEPOSITO", que se refere ao **nome do depósito**, também no Tracking.

![Imagem 4: 3. Desça até o campo " Informações da pessoa " e acrescente (ou edite) os parâmetros "GE_CODEMPRESA", que se refere ao…](https://ajuda.sankhya.com.br/hc/article_attachments/44012762332695)

 Feito os três (3) passos acima, pode-se clicar em "Integrar" no embarque, para alterar a situação de integração para "Aguardando integração", e aguardar que o NiFi consuma este embarque e o integre com o Tracking.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
