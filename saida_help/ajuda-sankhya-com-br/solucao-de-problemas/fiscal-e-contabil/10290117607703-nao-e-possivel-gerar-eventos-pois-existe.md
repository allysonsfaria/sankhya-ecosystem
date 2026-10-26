---
id: "10290117607703"
titulo: "Não é possível Gerar Eventos, pois existe uma tentativa de Fechar a Referência com \"Nro. de Recibo\" preenchido. É necessário Consultar o Fechamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10290117607703-N%C3%A3o-%C3%A9-poss%C3%ADvel-Gerar-Eventos-pois-existe-uma-tentativa-de-Fechar-a-Refer%C3%AAncia-com-Nro-de-Recibo-preenchido-%C3%89-necess%C3%A1rio-Consultar-o-Fechamento"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:03:58Z"
rotulos: ["Eventos", "Fiscal", "SEFAZ", "LIV_E00034", "Consultar o fechamento incompleto do REINF.", "Finalize o fechamento antes de gerar eventos.", "Não gerar eventos com \"Nro. de Recibo\" preenchido.", "Erro", "Documentos Eletrônicos", "Reinf"]
---

# Não é possível Gerar Eventos, pois existe uma tentativa de Fechar a Referência com "Nro. de Recibo" preenchido. É necessário Consultar o Fechamento

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18606250743575) MENSAGEM:**

[LIV\_E00034] Não é possível Gerar Eventos, pois existe uma tentativa de Fechar a Referência com "Nro. de Recibo" preenchido. É necessário Consultar o Fechamento.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18606241834903) SITUAÇÃO:**

A mensagem será apresentada no momento de Geração dos eventos do REINF, quando houver alguma referência que está em status de fechamento incompleto, mas que já tem algum número do recibo de tentativa de fechamento.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18606241845783) CAUSA:**

Quando alguma referência não concluiu o processo de fechamento com sucesso, estando ainda com o status que aponte que não foi finalizado o fechamento, o sistema vai apresentar a mensagem citada, para que o usuário primeiro finalize o fechamento, antes de prosseguir com o processo."

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18606241849879) SOLUÇÃO:**

Devemos Consultar o Fechamento, através do botão "Outras Opções". Ao ser clicado listará a mensagem "A consulta do fechamento foi iniciada com sucesso. Aguarde o retorno da Receita."

Assim, o evento de fechamento será consultado, e ocorrendo o processamento correto, o status do fechamento será concluído com sucesso.
