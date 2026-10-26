---
id: "32217854083351"
titulo: "Erro ao gerar lote ou cancelar lançamento fiscal: src-resolve: Cannot resolve the name 'TEnvEvento' to a(n) 'type definition' component"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32217854083351-Erro-ao-gerar-lote-ou-cancelar-lan%C3%A7amento-fiscal-src-resolve-Cannot-resolve-the-name-TEnvEvento-to-a-n-type-definition-component"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:31:51Z"
rotulos: ["Configuração", "Cache", "NF-e", "XML", "SEFAZ", "Cannot resolve the name", "'TEnvEvento'", "to a(n) 'type definition' component", "Erro ao cancelar lançamento fiscal", "src-resolve", "Erro ao gerar lote", "Erro"]
---

# Erro ao gerar lote ou cancelar lançamento fiscal: src-resolve: Cannot resolve the name 'TEnvEvento' to a(n) 'type definition' component

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/32554025389463) MENSAGEM:**

src-resolve: Cannot resolve the name 'TEnvEvento' to a(n) 'type definition' component

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32554009173271) SITUAÇÃO:**

Ao gerar lote ou cancelar um lançamento fiscal nos portais, ocorre o erro "src-resolve: Cannot resolve the name 'TEnvEvento' to a(n) 'type definition' component ".

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32217854070295)SOLUÇÃO:**

![Imagem 4: Acesse a "Administração do servidor" e verifique se o registro da base está configurado.](https://ajuda.sankhya.com.br/hc/article_attachments/32217822920087) Acesse a **"Administração do servidor"** e verifique se o registro da base está configurado.

![Imagem 5: Acesse a "Administração do servidor" e verifique se o registro da base está configurado.](https://ajuda.sankhya.com.br/hc/article_attachments/32217854071063)

![Imagem 6: Acesse a "Administração do servidor" e verifique se o registro da base está configurado.](https://ajuda.sankhya.com.br/hc/article_attachments/32217854071319)

**![Imagem 7: Ainda na Administração do Servidor, limpe o cache, feche todas as telas e realize um novo teste.](https://ajuda.sankhya.com.br/hc/article_attachments/32217854071959) Ainda na Administração do Servidor, limpe o cache, feche todas as telas e realize um novo teste.**

![Imagem 8: Ainda na Administração do Servidor, limpe o cache, feche todas as telas e realize um novo teste.](https://ajuda.sankhya.com.br/hc/article_attachments/32217822922263)

**![Imagem 9: Se o erro persistir, reinicie o sistema. Lembrando que esse processo vai parar a sua base, e pode demorar até 15…](https://ajuda.sankhya.com.br/hc/article_attachments/32217854072599) Se o erro persistir, reinicie o sistema. Lembrando que esse processo vai parar a sua base, e pode demorar até 15 minutos para voltar. Então, sempre realize fora do horário de expediente ou com aviso prévio.**

![Imagem 10: Se o erro persistir, reinicie o sistema. Lembrando que esse processo vai parar a sua base, e pode demorar até 15…](https://ajuda.sankhya.com.br/hc/article_attachments/32217822924951)

**(1)** Para se **certificar se o serviço voltou**, acesse a tela **"Console NFe"** e, na aba **"Status do Serviço"**, selecione o CNPJ e o ambiente desejado e clique em **"Testar"**.

![Imagem 11: (1) Para se certificar se o serviço voltou , acesse a tela "Console NFe" e, na aba "Status do Serviço" , selecione o…](https://ajuda.sankhya.com.br/hc/article_attachments/32217822925847)

**![Imagem 12: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/32554009173911)CAUSA:**

Este erro ocorre pois o Console NF-e, onde é configurado o certificado digital, perde a comunicação com a Sefaz.
