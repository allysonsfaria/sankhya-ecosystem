---
id: "29094189728151"
titulo: "Emissão de NFS-e | Lote Rejeitado - 000: Erro: Senha Inválida | Prefeitura de Serra - ES"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29094189728151-Emiss%C3%A3o-de-NFS-e-Lote-Rejeitado-000-Erro-Senha-Inv%C3%A1lida-Prefeitura-de-Serra-ES"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:37:22Z"
rotulos: ["Configuração", "Prefeituras", "NFS-e", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Senha Inválida"]
---

# Emissão de NFS-e | Lote Rejeitado - 000: Erro: Senha Inválida | Prefeitura de Serra - ES

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/29094165058455) **MENSAGEM:**

Lote Rejeitado - 000: Erro: Senha Inválida | Prefeitura de Serra - ES.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/29094189720471)SOLUÇÃO:**

No cadastro de 'Senha NFS-e' nas preferências da **Empresa** (Comercial >> Preferências >> Empresa), aba Documentos Fiscais Eletrônicos, sub aba NFS-e, sub aba Geral)  a senha está cadastrada com os caracteres minúsculos. 
E segundo o documento disponibilizado pela Prefeitura de Serra - ES, as senhas utilizam função hash criptográfica de modelo SHA1. Na qual esta criptografia, para o sistema da prefeitura, não suporta senhas com caracteres minúsculos.

Por mais que ao acessar o Portal da Prefeitura utiliza-se a senha com caracteres minúsculos, no Sankhya o cadastro deve ser em **MAIÚSCULO**.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/29094189722135)CAUSA:**

Ocorre quando a 'Senha NFS-e' possui caracteres minúsculos nas preferências da empresa.
