---
id: "4429330688279"
titulo: "Envio de XML, PDF da NFS e boleto por e-mail "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4429330688279-Envio-de-XML-PDF-da-NFS-e-boleto-por-e-mail"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-09-28T20:37:13Z"
rotulos: ["Configuração", "Parceiro", "XML", "TOP", "Financeiro", "não apagar", "NFS-e", "Configuração de Envio de Documentos Fiscais por E-mail"]
---

# Envio de XML, PDF da NFS e boleto por e-mail 

Para realizar a configuração do envio de XML, NF-s (PDF) e boleto por e-mail, os cadastros a seguir devem ser verificados:

**(1)** Cadastro da TOP, aba **"Impressão"**, campo **"Imprimir Pix/Boleto/Duplicata"**: Na confirmação;

**Observação:** Caso a TOP não gere financeiro esse campo deve ser configurado como "Proibido" para que o sistema envie somente o PDF da NFS.

**(1)** Cadastro da TOP, aba **"E-mails da Top"**, vincule o Tipo Parceiro e o modelo a ser utilizado;

**(1)** Cadastro de Parceiro, aba **"Informações"**, campo **"Geração de boleto nas centrais"**: enviar e-mail ou imprimir e Enviar e-mail;

**(1)** Cadastro de Parceiro, aba Informações, campo **"Tipo geração boleto"**: Enviar E-mail;

**(1)** Cadastro de Parceiro, aba **"NFe campo E-mail p/ envio NF-e/CT-e"** deve estar preenchido;

**(1)** Cadastro Tipo de Negociação, aba **"Característica Imprimir boleto/duplicata?":** Na confirmação

**(1)** Configure o e-mail no cadastro de **"Configurações > Cadastros > Empresas / Aba Endereço"**. Caso esse campo não esteja preenchido, não será enviado o XML nem o BOLETO, apenas a DANFE.

Os parâmetros que influenciam a rotina são:

**"NFSEGERARBOLETO":** Sim, conforme Cadastro de Parceiros

![Imagem 1: "NFSEGERARBOLETO": Sim, conforme Cadastro de Parceiros](https://ajuda.sankhya.com.br/attachments/token/VjOBVHmRVMEYns1i6qu5HWgdh/?name=inline-1839314193.png)

**"ENVEMAILNFSE":** Ligado

![Imagem 2: "ENVEMAILNFSE": Ligado](https://ajuda.sankhya.com.br/attachments/token/Wdr4in0Cz3sZ1BPXvhM7CRUHq/?name=inline-1287076278.png)

O parceiro receberá dois e-mails, devido sistema verificar o cadastro da Top para o Danfe (aba Email da top) e o cadastro do parceiro (aba **"NFe/NFSe"**) para envio do XML. Poderá verificar os e-mails enviados pela tela Fila para envio de e-mail de nota/pedido.

![Imagem 3: O parceiro receberá dois e-mails, devido sistema verificar o cadastro da Top para o Danfe (aba Email da top ) e o…](https://ajuda.sankhya.com.br/hc/article_attachments/4429264327319)
