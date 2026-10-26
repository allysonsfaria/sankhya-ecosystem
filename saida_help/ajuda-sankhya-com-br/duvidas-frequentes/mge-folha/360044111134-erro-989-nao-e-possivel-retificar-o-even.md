---
id: "360044111134"
titulo: "Erro 989 - Não é possível retificar o evento. Existe evento de pagamento associado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044111134-Erro-989-N%C3%A3o-%C3%A9-poss%C3%ADvel-retificar-o-evento-Existe-evento-de-pagamento-associado"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:32:44Z"
rotulos: ["#criadoporRayssa", "Eventos", "Fiscal", "Pagamento", "eSocial", "Central do eSocial", "Erro 989: Impossível Retificar Evento com Pagamento Associado", "Erro"]
---

# Erro 989 - Não é possível retificar o evento. Existe evento de pagamento associado

**![Imagem 1: MENSAGEM: (Erro 989): Não é possível retificar o evento. Existe evento de pagamento associado que será impactado pelo…](https://ajuda.sankhya.com.br/hc/article_attachments/16784339139479) MENSAGEM:**
[Erro 989]: Não é possível retificar o evento. Existe evento de pagamento associado que será impactado pelo evento retificador. Recibos impactados: R.
Ação Sugerida: Retificar ou excluir o evento de Pagamento que contenha o demonstrativo de pagamento que está causando a inconsistência e tentar enviar o evento novamente.

**![Imagem 2: SOLUÇÃO: Acesse: MGEPessoal » Avançado » Consulta eventos por funcionário Faça um filtro por empresa e funcionário, em…](https://ajuda.sankhya.com.br/hc/article_attachments/16784316709143) SOLUÇÃO:**

![Imagem 3: SOLUÇÃO: Acesse: MGEPessoal » Avançado » Consulta eventos por funcionário Faça um filtro por empresa e funcionário, em…](https://ajuda.sankhya.com.br/hc/article_attachments/16784316713623) Acesse: MGEPessoal » Avançado » Consulta eventos por funcionário

Faça um filtro por empresa e funcionário, em seguida localize o S-1210 referente ao S-2299/S-1200 que está tentando alterar. Em seguida, selecione e clique com o mouse direito e clique na opção **"Gerar exclusão"**. Feito isso, na parte superior da tela clique no botão **"Aplicar"**.

![Imagem 4: SOLUÇÃO: Acesse: MGEPessoal » Avançado » Consulta eventos por funcionário Faça um filtro por empresa e funcionário, em…](https://ajuda.sankhya.com.br/hc/article_attachments/16784339150999) Acesse: MGEPessoal » Avançado » Central do E-social

Clique no botão **"Selecionar Eventos Disponíveis"**. Feito isso, o sistema irá trazer o S-1210 que colocamos para ser excluído, despreze os demais eventos e envie o S-1210 .
Após a exclusão do evento S-1210 envie a alteração do S-2299/S-1200 e posteriormente o S-1210 de inclusão.

**![Imagem 5: CAUSA: Ocorre quando o envio do S-1200/S-2299, que é de alteração, está sendo alterado depois que já enviou o S-1210…](https://ajuda.sankhya.com.br/hc/article_attachments/16784339153047) CAUSA:**
Ocorre quando o envio do S-1200/S-2299, que é de alteração, está sendo alterado depois que já enviou o S-1210 relativo ao IR da sua folha.
**Exemplo:** Folha Normal da referência  01/2019 com pagamento em 31/01/2019.

![Imagem 6: CAUSA: Ocorre quando o envio do S-1200/S-2299, que é de alteração, está sendo alterado depois que já enviou o S-1210…](https://ajuda.sankhya.com.br/hc/article_attachments/16784316713623)  É enviado o S-1200 (Folha Normal) e, em seguida, o S-1210(IRRF);
![Imagem 7: CAUSA: Ocorre quando o envio do S-1200/S-2299, que é de alteração, está sendo alterado depois que já enviou o S-1210…](https://ajuda.sankhya.com.br/hc/article_attachments/16784339150999) É gerada uma alteração na folha de pagamento, então é necessário excluir o S-1210 para enviar o S-1200.
