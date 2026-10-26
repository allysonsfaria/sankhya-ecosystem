---
id: "37228329318295"
titulo: "E0714 Rejeição: Arquivo enviado com erro na assinatura"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37228329318295-E0714-Rejei%C3%A7%C3%A3o-Arquivo-enviado-com-erro-na-assinatura"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-09-25T00:03:28Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Erro", "Artigo atualizado KCS", "O arquivo XML foi enviado com erro na assinatura digital", "Problemas na assinatura digital do arquivo XML", "certificado digital vencido", "Arquivo enviado com erro na assinatura", "cadeia de certificação incompleta ou inválida", "erro no acesso à Lista de Certificados Revogados (LCR)", "certificado digital não instalado corretamente", "E0714 Rejeição", "Docs Eletrônicos - KCS", "Documentos Eletrônicos"]
---

# E0714 Rejeição: Arquivo enviado com erro na assinatura

**MENSAGEM**

[E172] ou [E0714] Arquivo enviado com erro na assinatura.

**SITUAÇÃO**

O erro ocorre na transmissão da **Nota Fiscal de Serviço Eletrônica (NFS-e)**. A prefeitura ou o Ambiente Nacional não conseguiu validar a **assinatura digital** do arquivo enviado, e a nota não é autorizada.

Os cenários mais comuns são:

- Certificado digital vencido, revogado ou instalado incorretamente.
- Certificado de um CNPJ diferente do emitente da nota.
- Caracteres especiais nos textos da nota, que alteram o arquivo depois de assinado.
- Sistema desatualizado em relação ao layout ou ao padrão de assinatura exigido pelo município.

**SOLUÇÃO**

O erro de assinatura pode ter diferentes causas. Siga as verificações abaixo:

**Verificação 1: Validade do certificado digital**

**(1)** Acesse a tela **"Console NFe"** (Comercial >> Configuração >> Console NFe).

**(2)** Confira se o certificado está dentro do prazo de validade. Se estiver vencido, providencie a renovação junto à autoridade certificadora.

**Verificação 2: Certificado correto para a empresa**

**(1)** Confira se o certificado configurado pertence ao **mesmo CNPJ da empresa emitente**. Em ambientes com várias empresas ou filiais, é comum a empresa estar vinculada ao certificado de outra.

**(2)** Se houver mais de um certificado instalado no computador ou no servidor, confira se o sistema está usando o certificado atual e não um antigo com o mesmo nome.

**(3)** Para certificado **A3** (token ou cartão), confira se o dispositivo está conectado e se o driver está instalado.

**Verificação 3: Reinstalação do certificado**

**(1)** Remova o certificado atual do repositório do sistema.

**(2)** Instale novamente o certificado digital e configure-o no Sankhya, vinculando-o à empresa correta.

**Verificação 4: Caracteres especiais na nota**

**(1)** Revise a **descrição do serviço**, as **observações** e os dados do tomador (razão social e endereço).

**(2)** Remova caracteres especiais ou incomuns, como **&, <, >, aspas, emojis, quebras de linha e textos colados de outros programas** (Word, e-mail, WhatsApp).

**(3)** Salve a nota e transmita novamente.

**Verificação 5: Instabilidade no ambiente da prefeitura**

**(1)** Se todas as verificações anteriores estiverem corretas, confira no site da prefeitura ou do provedor da NFS-e se há instabilidade ou manutenção.

**(2)** Se houver, aguarde a normalização e transmita novamente.

**CAUSA**

A prefeitura ou o Ambiente Nacional valida a assinatura digital para garantir que o arquivo foi gerado pelo emitente e não foi alterado depois de assinado. O erro ocorre quando essa validação falha. As principais causas são:

- Certificado digital vencido, revogado ou instalado incorretamente.
- Certificado vinculado a um CNPJ diferente do emitente.
- Certificado A3 desconectado ou sem driver.
- Caracteres especiais que alteram o conteúdo do arquivo depois da assinatura.
- Instabilidade no ambiente da prefeitura (menos comum).
