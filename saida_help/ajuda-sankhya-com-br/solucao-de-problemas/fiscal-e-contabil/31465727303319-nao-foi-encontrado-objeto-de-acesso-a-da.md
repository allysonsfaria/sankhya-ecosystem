---
id: "31465727303319"
titulo: "Não foi encontrado objeto de acesso a dados para este BMP: mge-dwf:NFSENAT"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31465727303319-N%C3%A3o-foi-encontrado-objeto-de-acesso-a-dados-para-este-BMP-mge-dwf-NFSENAT"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:32:59Z"
rotulos: ["Configuração", "Tipo de Operação", "TOP", "Financeiro", "NFS-e por Natureza", "Prefeituras", "NFS-e", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Não foi encontrado objeto de acesso", "NFSENAT", "BMP: mge-dwf:NFSENAT", "Squad Fiscal/Contábil"]
---

# Não foi encontrado objeto de acesso a dados para este BMP: mge-dwf:NFSENAT

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31465715889175) **MENSAGEM:**

Não foi encontrado objeto de acesso a dados para este BMP: mge-dwf:NFSENAT

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31465727293335)SOLUÇÃO:**

**(1)** Acesse a tela [**''Tipo de Operação - TOP''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

**(2)** Na aba **''NFS-e'',** desmarque o campo **''NFS-e por natureza''**, conforme a imagem abaixo:

![Imagem 3: (2) Na aba ''NFS-e'', desmarque o campo ''NFS-e por natureza'' , conforme a imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/36803461383447)

**(3)** Após desmarcar essa opção, gere uma nova nota ou duplique a existente, pois esse campo possui caráter histórico e não é atualizado retroativamente.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31465715891479)CAUSA:**

O erro ocorre devido à marcação **“NFS-e por natureza”**.

Quando essa opção está habilitada, o sistema tenta localizar informações na tabela adicional **NFSENAT**, utilizada por algumas prefeituras.

Como essa tabela não existe no ambiente em questão, o sistema não encontra os dados necessários e retorna a mensagem de erro.
