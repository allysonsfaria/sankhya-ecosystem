---
id: "31591543672599"
titulo: "Como não enviar o e-mail do destinatário no xml da NF-e?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31591543672599-Como-n%C3%A3o-enviar-o-e-mail-do-destinat%C3%A1rio-no-xml-da-NF-e"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:32:37Z"
rotulos: ["Configuração", "NF-e", "XML", "Preferências", "Passos para resolver", "Razão do erro", "Detalhe do erro", "não enviar o e-mail do destinatário no xml da NF-e", "Suprimir email do destinatário para NF-e", "Documentos Eletrônicos"]
---

# Como não enviar o e-mail do destinatário no xml da NF-e?

Para que a tag **<emailDest>** não seja preenchida no xml de uma NF-e, acesse **"Empresa"**(Comercial » Preferências » Empresa), vá até a aba **"Documentos Fiscais Eletrônicos",**sub aba **"NF-e/NFC-e",**sub aba **"NF-e"** e marque o campo **"Suprimir email do destinatário para NF-e?"**

![Imagem 1: Para que a tag <emailDest> não seja preenchida no xml de uma NF-e, acesse "Empresa" (Comercial » Preferências »…](https://ajuda.sankhya.com.br/hc/article_attachments/31991266930199)

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31591516640663)CAUSA:**

Essa situação acontece quando o campo Suprimir email do destinatário para NF-e?, nas preferências da empresa, está desmarcado. Assim, o e-mail do destinatário, configurado no cadastro do parceiro, será enviado na Tag emailDest no xml da nfe.
