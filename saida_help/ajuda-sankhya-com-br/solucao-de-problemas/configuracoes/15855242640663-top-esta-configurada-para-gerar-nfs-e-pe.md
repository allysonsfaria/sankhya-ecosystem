---
id: "15855242640663"
titulo: "TOP está configurada para gerar NFS-e pela Natureza da nota, no entanto não existe a tabela adicional NFSENAT"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15855242640663-TOP-est%C3%A1-configurada-para-gerar-NFS-e-pela-Natureza-da-nota-no-entanto-n%C3%A3o-existe-a-tabela-adicional-NFSENAT"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:56:02Z"
rotulos: ["Configuração", "TOP", "Financeiro", "CORE_E00573", "Prefeituras", "NFS-e"]
---

# TOP está configurada para gerar NFS-e pela Natureza da nota, no entanto não existe a tabela adicional NFSENAT

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18918970953751) MENSAGEM:**

[CORE\_E00573] TOP está configurada para gerar NFS-e pela Natureza da nota, no entanto não existe a tabela adicional NFSENAT.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18918970981271) CAUSA:**

Ocorre ao utilizar uma TOP com o campo ' NFS-e' selecionado sem ter a tabela adicional criada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18918948638871) SOLUÇÃO:**

Esse erro é apresentado quando a **TOP** (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) utilizada possui a marcação ativa no campo NFS-e por natureza, na aba NFS-e.

![Imagem 4: Esse erro é apresentado quando a TOP ( Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) utilizada possui a…](https://ajuda.sankhya.com.br/hc/article_attachments/15854364715671)

**(1)** Caso a empresa necessite utilizar essa marcação, segue abaixo trecho da documentação:
 
**NFS-e por natureza:** Para empresas que usam NFS-e por Natureza é necessário a criação de uma tela adicional, pelo Construtor de telas do Sankhya-W, do tipo Tela detalhe tendo como tela mestre a tela Natureza de Receitas/Despesas. Criada esta tela adicional, na tela de Natureza de Receitas/Despesas do Sankhya-W aparecerá uma nova aba, com a descrição da tela que foi criada (sugere-se para esta aba o nome 'NFS-e').
Nesta nova aba, informa-se, por empresa, o CNAE e demais campos que fazem sentido para a prefeitura da empresa.'
 
**(1)** Caso não precise dessa marcação ativa, desmarque-a e lance a nota novamente.
