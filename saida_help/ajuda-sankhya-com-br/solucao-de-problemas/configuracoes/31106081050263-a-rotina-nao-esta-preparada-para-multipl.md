---
id: "31106081050263"
titulo: "A rotina não está preparada para múltiplos modelos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31106081050263-A-rotina-n%C3%A3o-est%C3%A1-preparada-para-m%C3%BAltiplos-modelos"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-30T11:48:00Z"
rotulos: ["Configuração", "Portal de Vendas", "XML", "TOP", "NFS-e", "Passos para resolver", "Razão do erro", "Detalhe do erro", "CORE_E05182", "danf por email", "Envio de DANF", "múltiplos modelos", "DANF NFSE", "Erro"]
---

# A rotina não está preparada para múltiplos modelos

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31106081046679) **MENSAGEM:**

[CORE\_E05182] A rotina não está preparada para múltiplos modelos.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31286331513367) SITUAÇÃO:**

Esse erro pode causar o não envio do PDF da NFS-e no envio automático de e-mails. Nessa situação, o sistema encaminha apenas o XML e o boleto, sem anexar o PDF da nota fiscal.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31106081047447)SOLUÇÃO:**

Este erro ocorre devido a uma configuração inadequada na TOP, especificamente na aba **"E-mails da TOP"**. Quando são atribuídos dois modelos diferentes simultaneamente, o sistema não consegue processar corretamente o envio de e-mails, resultando nesse erro.

Para corrigir o problema, siga os passos abaixo:

**![Imagem 4: Verifique a configuração da TOP:](https://ajuda.sankhya.com.br/hc/article_attachments/31291124328471) Verifique a configuração da TOP:**

- - Acesse a aba **"E-mails da TOP"** e verifique se há mais de um modelo configurado.
  - Caso existam dois modelos atribuídos (por exemplo, um modelo de nota e um modelo de boleto), remova um deles, deixando apenas o necessário para o envio correto.

**![Imagem 5: Teste o envio manualmente:](https://ajuda.sankhya.com.br/hc/article_attachments/31291124330647) Teste o envio manualmente:**

- - Utilize a opção **"Outras opções" > "Enviar e-mails com seleção de destinatário"**, localizada no **"Portal de vendas"**.
  - Caso o erro ocorra, ajuste as configurações conforme necessário e teste novamente

Após realizar esses ajustes, o sistema deverá encaminhar os e-mails corretamente. O XML e o boleto da nota serão enviados em um e-mail, enquanto o PDF e o boleto serão enviados em outro.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31106106648983)CAUSA:**

O erro ocorre porque a rotina não suporta múltiplos modelos configurados simultaneamente na aba E-mails da TOP. Quando essa configuração indevida está presente, o envio automático pode falhar sem exibir mensagens de erro, impedindo o envio do PDF corretamente. Ajustar a configuração da TOP para conter apenas um modelo por vez resolve o problema e permite que os e-mails sejam enviados corretamente.
