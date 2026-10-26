---
id: "30889983208087"
titulo: "O que fazer quando o arquivo da logomarca está sendo salvo com 0KB?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30889983208087-O-que-fazer-quando-o-arquivo-da-logomarca-est%C3%A1-sendo-salvo-com-0KB"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T14:34:25Z"
rotulos: ["Configuração", "Impressão", "NF-e", "DANFE", "Preferências", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Impressao corrompida", "0", "KB", "0KB", "alta resolucao", "logomarca", "Erro"]
---

# O que fazer quando o arquivo da logomarca está sendo salvo com 0KB?

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31054897801879) **SITUAÇÃO:**

Ao imprimir um documento em PDF no Sankhya, o arquivo gerado é salvo com **0KB**, tornando-o impossível de ser aberto.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30889992932759)SOLUÇÃO:**

Revise o **tamanho e a resolução da logomarca** associada ao documento.

Se o erro ocorrer em um **DANFE**, siga estes passos para verificar e ajustar a logomarca:

![Imagem 3: Acesse a tela " Empresa" ( Comercial » Preferências ).](https://ajuda.sankhya.com.br/hc/article_attachments/31054897803543) Acesse a tela "**Empresa"** (Comercial » Preferências).

![Imagem 4: Vá para a aba "Documentos Fiscais Eletrônicos" .](https://ajuda.sankhya.com.br/hc/article_attachments/31054897805335) Vá para a aba **"Documentos Fiscais Eletrônicos"**.

![Imagem 5: Acesse a sub-aba "NF-e/NFC-e" e depois a sub-aba "NF-e" .](https://ajuda.sankhya.com.br/hc/article_attachments/31054897806615) Acesse a sub-aba **"NF-e/NFC-e"** e depois a sub-aba **"NF-e"**.

![Imagem 6: Localize o campo " Arquivo logomarca" e copie o caminho do repositório onde a imagem está armazenada.](https://ajuda.sankhya.com.br/hc/article_attachments/31054963370647) Localize o campo "**Arquivo logomarca"** e copie o caminho do repositório onde a imagem está armazenada.

![Imagem 7: Acesse o Repositório de Arquivos, encontre o arquivo da logomarca e verifique o tamanho da imagem utilizada.](https://ajuda.sankhya.com.br/hc/article_attachments/31054897812375) Acesse o **Repositório de Arquivos,** encontre o arquivo da logomarca e verifique o tamanho da imagem utilizada.

Se a logomarca estiver em uma **resolução muito alta** (exemplo: milhares de pixels de largura e altura ou arquivos muito pesados), **redimensione-a para uma versão otimizada** antes de utilizá-la no documento.

**Recomendação:** utilize um tamanho adequado para impressão, como **300 a 600 pixels de largura** e um formato otimizado (PNG de qualidade média a alta).

Isso garantirá que o PDF seja gerado corretamente sem comprometer a qualidade da impressão.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30889983199255)CAUSA:**

Esse problema ocorre devido ao **uso de uma imagem de altíssima resolução (gigapixel) na logomarca vinculada ao documento**. Quando o sistema tenta processar a geração do PDF, o tamanho excessivo da imagem pode:

- Exceder a capacidade de memória do servidor ou do gerador de PDFs;
- Causar um **timeout** no processamento da impressão;
- Tornar o arquivo gerado corrompido ou inutilizável.

Como resultado, o documento final não é salvo corretamente, aparecendo com **0KB**.
