---
id: "31254212596631"
titulo: "Sistema não está respeitando a marcação Cód. Produto p/ NF-e/NFC-e/CF-e do Cadastro do produto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31254212596631-Sistema-n%C3%A3o-est%C3%A1-respeitando-a-marca%C3%A7%C3%A3o-C%C3%B3d-Produto-p-NF-e-NFC-e-CF-e-do-Cadastro-do-produto"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:33:29Z"
rotulos: ["Produtos", "Configuração", "NF-e", "XML", "Impostos", "NFC-e", "Passos para resolver", "Razão do erro", "Detalhe do erro", "marcação Cód. Produto p/ NF-e/NFC-e/CF-e", "não está sendo respeitada", "CF-e"]
---

# Sistema não está respeitando a marcação Cód. Produto p/ NF-e/NFC-e/CF-e do Cadastro do produto

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31934392209303) **SITUAÇÃO:**

Sistema não está respeitando a marcação Cód. Produto p/ NF-e/NFC-e/CF-e do Cadastro do produto, que é responsável por alimentar a tag no XML  **<cProd>**

![Imagem 2: Sistema não está respeitando a marcação Cód. Produto p/ NF-e/NFC-e/CF-e do Cadastro do produto, que é responsável por…](https://ajuda.sankhya.com.br/hc/article_attachments/31934536247063)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31254212571415)SOLUÇÃO:**

Na tela **"Produtos"**(Configurações » Cadastros » Produtos » Produtos), aba **"Impostos"** existe o campo **"Cód. Produto p/ NF-e/NFC-e/CF-e"**.

![Imagem 4: Na tela "Produtos" (Configurações » Cadastros » Produtos » Produtos), aba "Impostos" existe o campo "Cód. Produto p/…](https://ajuda.sankhya.com.br/hc/article_attachments/31934543821079)

Nesse contexto, a tag <cProd> do XML da nota será impressa conforme a definição deste campo Cód. Produto p/ NF-e/NFC-e/CF-e, sendo as opções **"Código do Produto"** ou a **"Referência"**, que corresponde à informação do campo **"Referência"** da aba **"Geral**" do cadastro de produto.

Porém, se a opção Referência for selecionada e o campo correspondente a este estiver vazio, o sistema irá utilizar do campo Código.

**Caso o sistema esteja configurado corretamente e, mesmo assim, não esteja respeitando a configuração**, solicite ao **administrador do banco** de dados que **verifique se a trigger TRG\_INC\_UPD\_TGFITE\_PRODNFE está inativa.** Se estiver, o **administrador precisa ativa-la.** Pois, essa trigger é responsável por alimentar o campo PRODUTONFE na tabela TGFITE, que alimenta a tag <cProd>

![Imagem 5: Caso o sistema esteja configurado corretamente e, mesmo assim, não esteja respeitando a configuração , solicite ao…](https://ajuda.sankhya.com.br/hc/article_attachments/31254217318935)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31254217320727)CAUSA:**

Problema ocorre quando a Trigger TRG\_INC\_UPD\_TGFITE\_PRODNFE  está desabilitado ou a configuração

acima não está correta.

![Imagem 7: acima não está correta.](https://ajuda.sankhya.com.br/hc/article_attachments/31254217332119)
