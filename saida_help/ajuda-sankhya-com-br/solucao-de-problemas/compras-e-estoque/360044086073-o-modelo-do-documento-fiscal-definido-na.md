---
id: "360044086073"
titulo: "O \"Modelo do Documento Fiscal\" definido na TOP, não permite informar a chave NF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044086073-O-Modelo-do-Documento-Fiscal-definido-na-TOP-n%C3%A3o-permite-informar-a-chave-NF-e"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-28T17:34:04Z"
rotulos: ["Configuração", "NF-e", "Impostos", "TOP", "CORE_E05557", "Restrição na Informação da Chave NF-e na TOP", "Modelo do Documento Fiscal"]
---

# O "Modelo do Documento Fiscal" definido na TOP, não permite informar a chave NF-e

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16092762035863) MENSAGEM:**

[CORE\_E05557] Impostos: O "Modelo do Documento Fiscal" definido na TOP, não permite informar a chave NF-e.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16092762039063) SOLUÇÃO:**

![Imagem 3: Para lançamento no sistema de notas fiscais eletrônicas emitidas por Terceiros, sendo necessário informar a respectiva…](https://ajuda.sankhya.com.br/hc/article_attachments/16092814690583) Para lançamento no sistema de notas fiscais eletrônicas emitidas por Terceiros, sendo necessário informar a respectiva chave, é necessário que as configurações estejam de acordo com o mencionado abaixo:

Tela **"[Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** (Caminho de acesso: Comercial » Arquivo » Cadastros), aba **"[NF-e/NFC-e/CF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe)":**

**(2)** Campo **"Modelo de Documento":** 55-Nota Fiscal Eletrônica

**(2)** Campo **"NF-e":** Terceiros

![Imagem 4: (2) Campo "NF-e": Terceiros](https://ajuda.sankhya.com.br/hc/article_attachments/14492391827223)

![Imagem 5: Valide se está sendo utilizado o Tipo de Operação correto para o processo e caso necessário realize os ajustes…](https://ajuda.sankhya.com.br/hc/article_attachments/16092814697623) Valide se está sendo utilizado o Tipo de Operação correto para o processo e caso necessário realize os ajustes mencionados acima.

![Imagem 6: Após ajustes exclua o lançamento atual e realize um novo lançamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16092814700567) Após ajustes exclua o lançamento atual e realize um novo lançamento.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16092814704791) CAUSA:**

Mensagem apresentada ao lançar uma nota fiscal eletrônica de terceiros com o Modelo do Documento Fiscal diferente de 55.
