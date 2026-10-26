---
id: "30742322315415"
titulo: "Unmarshalling Error: Not a number: A"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30742322315415-Unmarshalling-Error-Not-a-number-A"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:34:49Z"
rotulos: ["Configuração", "TOP", "Natureza", "Prefeituras", "NFS-e", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Cód. Natureza Oper. ISS (NFS-e)", "Unmarshalling Error", "Not a number: A", "Erro"]
---

# Unmarshalling Error: Not a number: A

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30742306178583) **MENSAGEM:**

**Ao gerar o lote de uma NFse o erro é apresentado.**

Unmarshalling Error: Not a number: A.
Esse erro pode ter ocorrido por falta de conexão com a Internet.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30742322311191)SOLUÇÃO:**

No Cadastro do **"**[Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top), acesse a aba "[NFS-e"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse) e configure no campo **"Cód. Natureza Oper. ISS (NFS-e)"** com uma opção cujo código seja numérico, por exemplo: **1 -** XXXX / **2 -**YYYYY:

**Importante:** **antes de fazer qualquer alteração, verifique com o contador a opção correta da empresa**.

Depois de fazer o ajuste, gere o lote novamente.

![Imagem 3: Depois de fazer o ajuste, gere o lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/30768670918935)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30742322312599)CAUSA:**

A mensagem é apresentada quando para o campo Cód. Natureza Oper. ISS (NFS-e) é escolhida alguma opção cujo código é uma letra, sendo que a prefeitura em questão aceita somente códigos numéricos.
