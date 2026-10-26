---
id: "17271395687831"
titulo: "Invalid content was found starting with element 'qBCMono'. One of '{\"http://www.portalfiscal.inf.br/nfe\":vProd}' is expected"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17271395687831-Invalid-content-was-found-starting-with-element-qBCMono-One-of-http-www-portalfiscal-inf-br-nfe-vProd-is-expected"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:53:33Z"
rotulos: ["CORE_E04895", "Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "Correção do Erro 'qBCMono' na NF-e"]
---

# Invalid content was found starting with element 'qBCMono'. One of '{"http://www.portalfiscal.inf.br/nfe":vProd}' is expected

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17271395682199) **MENSAGEM:**

[CORE\_E04895] cvc-complex-type.2.4.a: Invalid content was found starting with element 'qBCMono'. One of '{"[http://www.portalfiscal.inf.br/nfe":vProd](http://www.portalfiscal.inf.br/nfe%22:vProd)}' is expected.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17271426025751)CAUSA:**

Ocorre quando a a NT 2023.001 está ativa e o produto da nota não é combustível.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17271441371927)SOLUÇÃO:**

Na tela **Empresa  -** Comercial » Preferências » Empresa quando ativada a NT 2023.001 irá gerar o grupo de tags do ICMS Monofásico utilizado para quem compra e vende combustível apenas.

![Imagem 4: Na tela Empresa - Comercial » Preferências » Empresa quando ativada a NT 2023.001 irá gerar o grupo de tags do ICMS…](https://ajuda.sankhya.com.br/hc/article_attachments/17280753448599)

As tags geradas são as destacadas abaixo:

![Imagem 5: As tags geradas são as destacadas abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/17280872215447)

Após desmarcar a configuração:

![Imagem 6: Após desmarcar a configuração:](https://ajuda.sankhya.com.br/hc/article_attachments/17280736420247)

E gerar lote novamente a nota será aprovada com sucesso, uma vez que ela não tenha combustíveis inclusos.

![Imagem 7: E gerar lote novamente a nota será aprovada com sucesso, uma vez que ela não tenha combustíveis inclusos.](https://ajuda.sankhya.com.br/hc/article_attachments/17270643253655)
