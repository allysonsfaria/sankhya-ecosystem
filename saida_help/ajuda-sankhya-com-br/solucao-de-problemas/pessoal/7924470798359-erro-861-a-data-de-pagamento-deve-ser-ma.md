---
id: "7924470798359"
titulo: "Erro 861 - A data de pagamento deve ser maior ou igual ao mês anterior de rescisão do contrato de trabalho. Como resolver?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7924470798359-Erro-861-A-data-de-pagamento-deve-ser-maior-ou-igual-ao-m%C3%AAs-anterior-de-rescis%C3%A3o-do-contrato-de-trabalho-Como-resolver"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:24:35Z"
rotulos: ["não apagar", "#validadoAnalúcia", "eSocial", "Folha de Pagamento", "Erro 861", "Rescisão", "Central do eSocial", "Pagamento Precoce", "Rescisão Ausente", "Verificação e Correção", "Erro", "Contrato de Trabalho"]
---

# Erro 861 - A data de pagamento deve ser maior ou igual ao mês anterior de rescisão do contrato de trabalho. Como resolver?

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16585037654935) MENSAGEM**:

Erro 861 - A data de pagamento deve ser maior ou igual ao mês anterior de rescisão do contrato de trabalho.
Elemento: /eSocial/evtPgtos/ideBenef/infoPgto[2]/dtPgto
[2022-06-10]
-----------------------------------Erro 726 - Não foi localizado um evento de rescisão contratual para o trabalhador com mesmo recibo de pagamento.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16585037657367) SITUAÇÃO:**

Ao enviar o S-1210 ocorre o erro.

**Ação Sugerida:**
Deve ser um identificador de recibo de pagamento atribuído pela empresa em um dos eventos rescisórios (S-2299 ou S-2399), no campo **"Identificador de recibo de pagamento"**.
.Se Tipo de Pagamento= [2] deve ser um valor atribuído pela empresa em S-2299;
.Se Tipo de Pagamento= [3], deve ser um valor atribuído pela empresa em S-2399

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16585037660055)SOLUÇÃO:**

![Imagem 4: Acesse a central do esocial e confira se o registro de remuneração S-2299/S-2399 foi enviado sem erros.](https://ajuda.sankhya.com.br/hc/article_attachments/16585053607703) Acesse a central do esocial e confira se o registro de remuneração S-2299/S-2399 foi enviado sem erros.

Caso tenha retornado com algum erro, realize a correção e depois de processado envie o S-1210 novamente.

![Imagem 5: Se o S-2299/S-2399 já estiver como enviado, acesse o portal do esocial e confira se os valores de rescisão constam no…](https://ajuda.sankhya.com.br/hc/article_attachments/16585053612055) Se o S-2299/S-2399 já estiver como enviado, acesse o portal do esocial e confira se os valores de rescisão constam no site. Caso não conste, exclua o S-2299, libere a folha para o esocial e realize um novo envio do evento. Após isso, envie o S-1210 novamente.

**Para verificar se as rubricas constam no esocial acesse: Folha de pagamento->Totalizadores->Trabalhador->Contribuição Previdenciária**

![Imagem 6: Para verificar se as rubricas constam no esocial acesse: Folha de pagamento->Totalizadores->Trabalhador->Contribuição…](https://ajuda.sankhya.com.br/hc/article_attachments/7925593726999)

Informe a referência e o CPF e clique em pesquisar.

![Imagem 7: Informe a referência e o CPF e clique em pesquisar.](https://ajuda.sankhya.com.br/hc/article_attachments/7925675021719)

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16585037670167)CAUSA:**

Este erro ocorre no retorno do registro **S-1210** quando por algum motivo este foi enviado antes do evento **S-2299/S-2399** ser processado ou quando o **S-2299/S-2399** está processado, mas as rubricas não constam no portal do eSocial.
