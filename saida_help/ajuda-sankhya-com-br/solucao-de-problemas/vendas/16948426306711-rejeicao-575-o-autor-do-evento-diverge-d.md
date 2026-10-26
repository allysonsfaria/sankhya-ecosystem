---
id: "16948426306711"
titulo: "Rejeição 575: O autor do evento  diverge do destinatário da NF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16948426306711-Rejei%C3%A7%C3%A3o-575-O-autor-do-evento-diverge-do-destinat%C3%A1rio-da-NF-e"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-09-10T18:04:59Z"
rotulos: ["Eventos", "NF-e", "XML", "SEFAZ", "Rejeição 575", "Rejeição 575: Autor do evento diverge do destinatário", "Ajuste o CNPJ do autor para coincidir com o destinatário da NF-e", "CNPJ do autor deve ser o destinatário da NF-e", "Erro"]
---

# Rejeição 575: O autor do evento  diverge do destinatário da NF-e

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16948446820375) **MENSAGEM:**

Rejeição 575: O autor do evento diverge do destinatário da NF-e.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16948432333207)CAUSA:**

A Rejeição (575):"O autor do evento diverge do destinatário da NF-e", indica que ao emitir um evento de Manifestação do Destinatário, obrigatoriamente o CNPJ Auto do evento tem que ser o destinatário da NF-e.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16948441517463)SOLUÇÃO:**

Para resolver a Rejeição 575, o CNPJ do Autor do evento deve ser o CNPJ do destinatário da NF-e a qual se está tentando vincular o evento.

![Imagem 4: Para resolver a Rejeição 575, o CNPJ do Autor do evento deve ser o CNPJ do destinatário da NF-e a qual se está tentando…](https://atendimento.tecnospeed.com.br/hc/article_attachments/360022611394/mceclip0.png)

No exemplo acima,  o CNPJ 88888888888888 **obrigatoriamente** deve ser o destinatário da NF-e com chave de acesso, 43141299999999999999554171297963781000355991, caso contrário a rejeição irá ocorrer.

**Nota:** Sabe-se que para dar ciência da operação de uma NF-e, obrigatoriamente precisa ser o destinatário da NF-e, pois o certificado digital que assinará o pedido do evento terá o CNPJ comparado com o CNPJ que está como destinatário do documento. Sendo assim, para resolver a rejeição o CNPJ do Autor do evento deve ser o CNPJ do destinatário da NF-e a qual se está vinculando o evento.
