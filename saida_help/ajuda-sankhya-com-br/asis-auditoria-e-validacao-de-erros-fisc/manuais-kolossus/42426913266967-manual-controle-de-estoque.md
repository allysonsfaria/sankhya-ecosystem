---
id: "42426913266967"
titulo: "Manual Controle de Estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42426913266967-Manual-Controle-de-Estoque"
trilha: "ASIS: Auditoria e validação de erros fiscais > Base de conhecimento > Manuais Kolossus"
atualizado_em: "2026-08-03T12:37:09Z"
rotulos: ["asis", "sync_hc", "asis_52941227396243", "sync_hash_4b2df035f76b"]
---

# Manual Controle de Estoque

Sumário

[Controle de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426913266967-Manual-Controle-de-Estoque#h238slt4cjm2p7il995v4kf48s31iqk)

[O que compõem o módulo?](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426913266967-Manual-Controle-de-Estoque#h263slt4cjuua1g0f1w9fxb3luuu1716)

[Como gerar o Relatório?](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426913266967-Manual-Controle-de-Estoque#h305slt4ck5eyotvsgk1khc53l17nnp5r)

[Registros utilizados no Controle de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426913266967-Manual-Controle-de-Estoque#h323slt4ckcgvkmxhul3sae2hcvymdv)

[Status de Processamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426913266967-Manual-Controle-de-Estoque#h348slt4ckmeb1o50j26kogamy1k00pfb)

## Controle de Estoque

Este aplicativo permite realizar a análise do estoque sob a ótica das obrigações acessórias. Através da importação prévia dos arquivos do SPED Fiscal, NF-e, SAT e NFC-e o Controle de Estoque realizará os cálculos dos saldos mensais de forma analítica, permitindo a conciliação com controles internos e dados do ERP.

### O que compõem o módulo?

TELA – HOME – Nesse menu você poderá gerar os relatórios.

TELA – PROCESSOS - Nesse menu poderá ser visualizado o andamento do processo dos relatórios.

TELA – MEUS PROCESSOS - Nesse menu poderá ser visualizado o andamento do processo dos relatórios do seu usuário.

![Imagem 1: TELA – MEUS PROCESSOS - Nesse menu poderá ser visualizado o andamento do processo dos relatórios do seu usuário.](https://ajuda.sankhya.com.br/hc/article_attachments/42426913407639)

### Importante!

Para utilização adequada do aplicativo, recomendamos que seja realizada a importação prévia da totalidade dos arquivos de SPED Fiscal e dos documentos fiscais eletrônicos de emissão própria de todo o período que será avaliado.

 A não realização deste processo impactará diretamente nos resultados.

## Como gerar o Relatório?

Para gerar o relatório basta selecionar a Empresa e Ano e clicar em Gerar Relatório.

![Imagem 2: Para gerar o relatório basta selecionar a Empresa e Ano e clicar em Gerar Relatório.](https://ajuda.sankhya.com.br/hc/article_attachments/42426913521815) 

Selecione a Empresa: escolha o CNPJ, ou nome da empresa, ou a Inscrição Estadual que será objeto da análise do Estoque. Lembrando que somente é possível selecionar empresas previamente cadastradas através do aplicativo Conta ou via Upload de Obrigação Acessória.

Selecione o Ano:  indique a competência para a análise do Estoque. Ao selecionar o ano, o aplicativo buscará as informações nas obrigações acessórias (SPED, NFe, NFCe e SAT) importadas no Kolossus e que preencham esse requisito temporal.

Depois de selecionado a Empresa e o Ano clique em  ![Imagem 3: Depois de selecionado a Empresa e o Ano clique em](https://ajuda.sankhya.com.br/hc/article_attachments/42426881996951)

### Você pode acompanhar o processamento de seu relatório em Meus Processos:

![Imagem 4: Você pode acompanhar o processamento de seu relatório em Meus Processos:](https://ajuda.sankhya.com.br/hc/article_attachments/42426870859927)

Assim que finalizado você poderá baixar o resultado em Excel, flegando o arquivo e indo em ![Imagem 5: Assim que finalizado você poderá baixar o resultado em Excel, flegando o arquivo e indo em ou se preferir clicando no…](https://ajuda.sankhya.com.br/hc/article_attachments/42426870954391) ou se preferir clicando no clips verde  também já vai direto para o Excel. 

## Registros utilizados no Controle de Estoque

Os registros utilizados no Controle de Estoque são: 

- Os registros do Bloco K\*;
- O registro C170 das notas de entrada;
- Informações de itens das notas de saídas;
- Informações do Bloco H.

\* Registros do Bloco K utilizados: 

Registro K210: COD\_ITEM\_ORI (código do produto que será movimentado) e QTD\_ORI (quantidade baixada do estoque, ou seja, saída) 

Registro K215: COD\_ITEM\_DES (código do produto que será movimentado) e QTD\_DES (quantidade aumentada de estoque, ou seja, entrada) 

Outras Movimentações:

Registro K220: COD\_ITEM\_ORI (código do produto que será movimentado) e QTD\_ORI (quantidade baixada do estoque, ou seja, saída); COD\_ITEM\_DEST (código do produto que será movimentado) e QTD\_DEST (quantidade aumentada de estoque, ou seja, entrada) 

Ordem de Produção 

Registro K230: COD\_ITEM (código do produto que será movimentado) e QTD\_ENC (Quantidade de produção acabada, ou seja, entrada)

Registro K235: COD\_ITEM (código do produto que será movimentado) e QTD (Quantidade consumida do item, ou seja, saída) 

Reprocessamento 

Registro K260: COD\_ITEM (código do produto que será movimentado), QTD\_SAÍDA (quantidade baixada do estoque, ou seja, saída) e QTD\_RET (quantidade aumentada de estoque, ou seja, entrada) 

Registro K265: COD\_ITEM (código do produto que será movimentado), QTD\_SAÍDA (quantidade baixada do estoque, ou seja, saída) e QTD\_RET (quantidade aumentada de estoque, ou seja, entrada) 

Produção Conjunta 

Registro K291: COD\_ITEM (código do produto que será movimentado) e QTD (Quantidade de produção acabada, ou seja, entrada) 

Registro K292: COD\_ITEM (código do produto que será movimentado) e QTD (Quantidade consumida do item, ou seja, saída)

## Status de Processamento

![Imagem 6: Status de Processamento](https://ajuda.sankhya.com.br/hc/article_attachments/42426887345175)

É possível diagnosticar o erro passando o mouse por cima do X.
