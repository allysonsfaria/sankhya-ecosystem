---
id: "360044110714"
titulo: "TIP_ECD - Campo obrigatório não preenchido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110714-TIP-ECD-Campo-obrigat%C3%B3rio-n%C3%A3o-preenchido"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:15Z"
rotulos: ["#revisadojunior", "Configuração", "Empresa", "ECD", "Fiscal", "PUBLIFER", "Contabilidade", "Solução: Configure \"Tipo de Empresa\" em \"SCP\" e gere o arquivo ECD novamente.", "Erro: Campo obrigatório não preenchido em TIP_ECD.", "Causa: Campo 17 do registro 0000 não preenchido."]
---

# TIP_ECD - Campo obrigatório não preenchido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16643670616599) MENSAGEM:**

[TIP\_ECD]: Campo Obrigatório não preenchido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16643643331351) SOLUÇÃO:**

![Imagem 3: Acesse a tela "Empresa" (Caminho de acesso: Contabilidade » Preferências).](https://ajuda.sankhya.com.br/hc/article_attachments/16643670621591) Acesse a tela **"Empresa"** (Caminho de acesso: Contabilidade » Preferências).

![Imagem 4: Na aba "SCP - Sociedade em Cota de Participação", preencha o campo "Tipo de Empresa" com a opção adequada para a…](https://ajuda.sankhya.com.br/hc/article_attachments/16643643337623) Na aba **"SCP - Sociedade em Cota de Participação",** preencha o campo **"Tipo de Empresa"** com a opção adequada para a respectiva empresa:

- 2- SCP;
- 0- Empresa não participante de SCP como sócio ostensivo;
- 1 -Empresa participante de SCP como sócio ostensivo;

![Imagem 5: 1 -Empresa participante de SCP como sócio ostensivo;](https://ajuda.sankhya.com.br/hc/article_attachments/14792933477399)

![Imagem 6: Configurado o campo acima, gere um novo arquivo ECD e proceda com sua validação.](https://ajuda.sankhya.com.br/hc/article_attachments/16643670626583) Configurado o campo acima, gere um novo arquivo ECD e proceda com sua validação.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16643643341847)CAUSA:**

Ao tentar validar a Escrituração Fiscal Digital do período, a mensagem é apresentada quando  o conteúdo do campo 17 do registro 0000 do ECD não é devidamente enviado.
