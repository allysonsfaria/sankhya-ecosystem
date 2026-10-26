---
id: "6322879884055"
titulo: "O Gênero do produto é \"30-Produtos farmacêuticos\", para isso é necessário que a opção \"Tem Rastro do Lote\" esteja marcada. Efetue a configuração na aba Geral"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6322879884055-O-G%C3%AAnero-do-produto-%C3%A9-30-Produtos-farmac%C3%AAuticos-para-isso-%C3%A9-necess%C3%A1rio-que-a-op%C3%A7%C3%A3o-Tem-Rastro-do-Lote-esteja-marcada-Efetue-a-configura%C3%A7%C3%A3o-na-aba-Geral"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:16:45Z"
rotulos: ["Produtos", "Configuração", "NF-e", "XML", "Impostos", "Estoque", "não apagar", "CORE_E03874 ", "Erro de Configuração de Produtos Farmacêuticos"]
---

# O Gênero do produto é "30-Produtos farmacêuticos", para isso é necessário que a opção "Tem Rastro do Lote" esteja marcada. Efetue a configuração na aba Geral

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16361759210775) MENSAGEM:**

[CORE\_E03874]  O Gênero do produto é "30-Produtos farmacêuticos", para isso é necessário que a opção "Tem Rastro do Lote" esteja marcada. Efetue a configuração na aba Geral.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16361768617879)SOLUÇÃO:**

Para solução do problema realize as configurações abaixo:

**Tela de produtos**

- - Aba **"Impostos"**, **"Gênero"**: 30 - Produtos Farmacêuticos
  - Aba **"Geral"**, **"Tem Rastro por lote"**: Marcado
  - Ative os parâmetros **"LOTEDTFAB"** e **"LOTEDTVAL"**
  - Abas **"Medidas e Estoque"**, **"Controle Adicional"**, informe qual controle será realizado para o produto
  - Produtos medicamentos precisam ter as informações de lote destacadas no XML da NF-e
  - Conforme a Nota Técnica 2009/003, todo medicamento deve ser controlado por lote e data de validade. Onde no sistema precisa ter essas configurações.

**![Imagem 3: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16361759213591) OBSERVAÇÃO:**

Caso o gênero do produto seja definido como 30 - Produtos Farmacêuticos e não tenha as configurações acima mesmo que seja para **consumo** o erro será apresentado, sendo assim sendo para consumo não deve ser preenchido o gênero.  

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16361759215255)CAUSA:**

Trata-se de erro no cadastro e configuração de produtos do gênero 30 (produtos farmacêuticos);
