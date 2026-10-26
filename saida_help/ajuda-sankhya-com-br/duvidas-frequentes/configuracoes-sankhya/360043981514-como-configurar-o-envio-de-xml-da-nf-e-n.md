---
id: "360043981514"
titulo: "Como configurar o envio de XML da NF-e/NFC-e/CC-e e Danfe por e-mail?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043981514-Como-configurar-o-envio-de-XML-da-NF-e-NFC-e-CC-e-e-Danfe-por-e-mail"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-10-21T18:00:31Z"
rotulos: ["DUVIDANF", "#PUBLIFER", "Configuração", "Parceiro", "NF-e", "XML", "DANFE", "Configuração de Envio de XML e Danfe", "Servidor SMTP"]
---

# Como configurar o envio de XML da NF-e/NFC-e/CC-e e Danfe por e-mail?

![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17124725274647) SOLUÇÃO:

Para o correto funcionamento desta funcionalidade, execute as seguintes configurações:

(1)** Envio de XML:**

![Imagem 2: Na tela "Parceiros" (Caminho de acesso: Configurações » Cadastros » Parceiros) , aba "NF-e" :](https://ajuda.sankhya.com.br/hc/article_attachments/17124734911127) Na tela **"Parceiros"** (Caminho de acesso: Configurações » Cadastros » Parceiros), aba **"NF-e"**:

- No campo **“Tipo do anexo”:**escolha se o e-mail será mandado como arquivo compactado (extensão zip) ou arquivo normal (extensão xml).
- No campo **“E-mail p/ envio de NF-e”:** informe o e-mail para o qual será enviado o XML da Nota, caso o campo **“Ambiente NF-e”**, da tela **“Financeiro\Preferências\Empresa”**, esteja configurado como **“Produção”**.

**Nota:** se o campo Ambiente NF-e estiver configurado como **“Homologação”**, enquanto a NF-e estiver em implantação, o e-mail será enviado para o e-mail da própria empresa, cadastrado na tela **“Configurações\Cadastros\Empresas”**, na aba **“Endereço”**, campo **“Email”**. Uma vez que o Ambiente NF-e tenha sido alterado para Produção, o e-mail será enviado para o e-mail do parceiro da nota.

![Imagem 3: Na tela "Servidor SMTP" (Caminho de acesso: Configurações » Avançado » Envio de Mensagens » Servidor SMTP) realiza-se a…](https://ajuda.sankhya.com.br/hc/article_attachments/17124734913559) Na tela **"Servidor SMTP"** (Caminho de acesso: Configurações » Avançado » Envio de Mensagens » Servidor SMTP) realiza-se a configuração para envio dos e-mail's nas diversas rotinas do sistema que contam com este recurso. (Detalhes em: [Servidor SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593494))

(1)** Envio de DANFE:**

Para envio do DANFE junto ao XML verifique:

![Imagem 4: Na tela Parceiros (Caminho de acesso: Configurações » Cadastros » Parceiros) , aba NF-e:](https://ajuda.sankhya.com.br/hc/article_attachments/17124734911127) Na tela Parceiros (Caminho de acesso: Configurações » Cadastros » Parceiros), aba NF-e:

- O campo **"Enviar DANFE por e-mail?"** quando assinalado autoriza o envio do PDF da Nota Fiscal Eletrônica aprovada, juntamente com o XML, por e-mail para o Parceiro.

![Imagem 5: Na tela " Tipos de Operação" (Caminho de acesso: Comercial\Arquivos\Cadastros):](https://ajuda.sankhya.com.br/hc/article_attachments/17124734913559) Na tela **"Tipos de Operação"** (Caminho de acesso: Comercial\Arquivos\Cadastros):

- Para que o Danfe seja enviado, na TOP o campo **“Imprimir”** da **“Aba Impressão”** deve estar informado como **“Na confirmação”**. Dessa forma, ao gerar o Lote da NF-e, o Danfe será impresso e o e-mail será enviado com o xml e o Danfe.
- Na TOP se o campo Imprimir estiver como **“Manual”** e o usuário desejar enviar o Danfe junto com o XML no e-mail, ele deverá imprimir o Danfe antes de enviar Manual. Ou seja, para que o Danfe seja enviado, ele deve ter sido impresso anteriormente, caso contrário o Danfe não será enviado.

![Imagem 6: Tem-se ainda a possibilidade de enviar o e-mail de forma manual: Portal de Vendas/Compras >> Botão NF-e >> "Enviar XML…](https://ajuda.sankhya.com.br/hc/article_attachments/17124725294231) Tem-se ainda a possibilidade de enviar o e-mail de forma manual: Portal de Vendas/Compras >> Botão NF-e >> "Enviar XML da NF-e/CC-e e Danfe por e-mail"

![Imagem 7: Se o ‘Parceiro’ da nota não tiver e-mail cadastrado, o e-mail não será enviado.](https://ajuda.sankhya.com.br/hc/article_attachments/17124734920087) Se o ‘Parceiro’ da nota **não** tiver e-mail cadastrado, o e-mail não será enviado.
