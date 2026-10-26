---
id: "7621277524887"
titulo: "Envio de XML e DANFE da NF-e por e-mail"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7621277524887-Envio-de-XML-e-DANFE-da-NF-e-por-e-mail"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-08-21T16:17:05Z"
rotulos: ["Configuração", "Impressão", "Parceiro", "NF-e", "XML", "DANFE", "#PubliFer", "Envio de XML e DANFE por E-mail", "Artigo atualizado KCS", "Plataforma - KCS"]
---

# Envio de XML e DANFE da NF-e por e-mail

Para o correto funcionamento desta rotina, realize algumas configurações:

![Imagem 1: Na tela "Cadastro do Parceiro", aba "NF-e" onde:](https://ajuda.sankhya.com.br/hc/article_attachments/16532220689047) Na tela **"Cadastro do Parceiro",** aba [**"NF-e"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abanf-enfs-ect-e) onde:

**(1)** No campo **"Tipo do anexo",** o usuário poderá escolher se o e-mail será mandado como arquivo compactado (extensão zip) ou arquivo normal (extensão xml).

**(1)** No campo **"E-mail p/ envio de NF-e"** informe o e-mail para para o qual será enviado o XML da Nota, caso o campo **"Ambiente NF-e"**, da tela [**"Preferências da Empresa"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), esteja configurado como **"Produção"**.

| **Nota:**se o campo Ambiente NF-e estiver configurado como **"Homologação"**, enquanto a NF-e estiver em implantação, o e-mail será enviado para o e-mail da própria empresa, cadastrado na tela **"**[**Empresas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293), na aba **"Endereço"**, campo **"Email"**. Uma vez que o Ambiente NF-e tenha sido alterado para Produção, o e-mail será enviado para o e-mail do parceiro da nota, que deverá ser cadastrado no cadastro do Parceiro, campo **"E-mail p/ envio de NF-e"**. |
| --- |

![Imagem 2: É importante informar que, para que o Danfe seja enviado, na TOP o campo "Imprimir", da aba "Impressão", deve estar…](https://ajuda.sankhya.com.br/hc/article_attachments/16532182441879) É importante informar que, para que o Danfe seja enviado, na TOP o campo **"Imprimir",** da aba **"Impressão",** deve estar informado como **"Na confirmação"**. Dessa forma, ao gerar o Lote da NF-e, o Danfe será impresso e o e-mail será enviado com o XML e o Danfe:

![Imagem 3: É importante informar que, para que o Danfe seja enviado, na TOP o campo "Imprimir", da aba "Impressão", deve estar…](https://ajuda.sankhya.com.br/hc/article_attachments/16532182444311)

![Imagem 4: Tem-se ainda a possibilidade de enviar o e-mail de forma manual, pelo botão "Outras opções", escolhendo a opção "Nota…](https://ajuda.sankhya.com.br/hc/article_attachments/16532182447639) Tem-se ainda a possibilidade de enviar o e-mail de forma manual, pelo botão **"Outras opções",** escolhendo a opção **"Nota Fiscal Eletrônica"** e respectivamente,**"Enviar XML da nota por e-mail"**.

| **Importante:** Na TOP se o campo Imprimir estiver como Manual e houver desejar de enviar o Danfe junto com o XML no e-mail, deverá imprimir o Danfe antes de enviar Manual. Ou seja, para que o Danfe seja enviado, ele deve ter sido impresso anteriormente, caso contrário o Danfe não será enviado. |
| --- |

**Observação:** o arquivo XML da nota será enviado para a lista de e-mails tanto do parceiro Destinatário, quanto do parceiro Transportador, se o campo **"E-mail p/ envio NF-e/NFS-e/CT-e"** do cadastro de Parceiros, aba [**"NF-e/NFS-e/CT-e"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abanf-enfs-ect-e) estiver preenchido. Lembrando que, o parceiro Transportador receberá o e-mail mesmo que o parceiro Destinatário não tenha e-mail cadastrado.
