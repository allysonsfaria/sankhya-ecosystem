---
id: "360044087533"
titulo: "TOP com NF-e de Terceiros deve ter a chave NF-e informada com 44 caracteres e sem espaço em branco"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044087533-TOP-com-NF-e-de-Terceiros-deve-ter-a-chave-NF-e-informada-com-44-caracteres-e-sem-espa%C3%A7o-em-branco"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:01:51Z"
rotulos: ["#PUBLIFER", "CORE_E02763", "Configuração", "Parceiro", "NF-e", "TOP", "Problema com Chave NF-e de Terceiros", "Documentos Eletrônicos"]
---

# TOP com NF-e de Terceiros deve ter a chave NF-e informada com 44 caracteres e sem espaço em branco

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16107987610519) MENSAGEM:**

[CORE\_E02763] TOP com NF-e de Terceiros deve ter a chave NF-e informada com 44 caracteres e sem espaço em branco.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16108017519767) SITUAÇÃO:**

Ao tentar confirmar nota definida como NF-e de Terceiros, a mensagem poderá ser retornada.

![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16107987620631) **SOLUÇÃO:**

![Imagem 4: Se o lançamento realizado trata-se de uma emissão de terceiros, identifique no documento/nota enviado pelo parceiro,…](https://ajuda.sankhya.com.br/hc/article_attachments/16107987623447) Se o lançamento realizado trata-se de uma emissão de terceiros, identifique no documento/nota enviado pelo parceiro, qual a chave NF-e desse.

![Imagem 5: Essa informação deve ser preenchida no campo "Chave NF-e" disponibilizado na Central onde está sendo feito lançado o…](https://ajuda.sankhya.com.br/hc/article_attachments/16108017526807) Essa informação deve ser preenchida no campo **"Chave NF-e"** disponibilizado na Central onde está sendo feito lançado o documento. Atente-se em inserir corretamente os 44 caracteres:

![Imagem 6: Essa informação deve ser preenchida no campo "Chave NF-e" disponibilizado na Central onde está sendo feito lançado o…](https://ajuda.sankhya.com.br/hc/article_attachments/14529446039575)

![Imagem 7: Caso não localize esse campo, sua inserção pode ser realizada através da rotina " Configurador de layout da nota " .](https://ajuda.sankhya.com.br/hc/article_attachments/16108017528471) Caso não localize esse campo, sua inserção pode ser realizada através da rotina **"[Configurador de layout da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)"**.

![Imagem 8: Se o lançamento não refere-se a uma NF-e de Terceiros, será necessário ajustar no cadastro da TOP o campo "NF-e" , aba…](https://ajuda.sankhya.com.br/hc/article_attachments/16107987633047) Se o lançamento não refere-se a uma NF-e de Terceiros, será necessário ajustar no cadastro da TOP o campo **"NF-e"**, aba **"Impressão"** para uma opção diferente de "**Terceiros**". Caso esse ajuste seja necessário, um novo lançamento deve ser realizado.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16107987635607) CAUSA:**

Ao tentar confirmar lançamentos realizados com Tipo de Operação, no qual foi definido NF-e = [Terceiros] e o campo Chave NF-e não foi devidamente preenchido, será apresentada a mensagem.
