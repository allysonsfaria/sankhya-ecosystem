---
id: "360042917074"
titulo: "Não temos produtos que permitam o rateio do desconto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042917074-N%C3%A3o-temos-produtos-que-permitam-o-rateio-do-desconto"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:02Z"
rotulos: ["#PUBLIFER", "CORE_E02346", "Produtos", "Configuração", "Nota Fiscal", "Desconto", "Vendas", "Produtos não permitem rateio de desconto", "Percentual de desconto insuficiente", "Ajuste o \"%Desconto Máximo\" nos produtos"]
---

# Não temos produtos que permitam o rateio do desconto

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16117681339543) MENSAGEM:**

[CORE\_E02346] Não temos produtos que permitam o rateio do desconto.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16117681348503) SITUAÇÃO:**

Ao realizar a confirmação da nota/pedido, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16117657471383) SOLUÇÃO:**

![Imagem 4: Acesse o cadastro dos produtos e defina um percentual máximo de desconto que seja suficiente para que o rateio ocorra.](https://ajuda.sankhya.com.br/hc/article_attachments/16117657475735) Acesse o cadastro dos produtos e defina um percentual máximo de desconto que seja suficiente para que o rateio ocorra.

**(2)** Tela **"[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)"** (Caminho de acesso: Configurações/Cadastros/Produtos), aba **"Venda"**, Campo **"%Desconto Máximo"**.

![Imagem 5: Definido o desconto máximo, redigite o cabeçalho da nota e teste a confirmação.](https://ajuda.sankhya.com.br/hc/article_attachments/16117681369495) Definido o desconto máximo, redigite o cabeçalho da nota e teste a confirmação.

![Imagem 6: Definido o desconto máximo, redigite o cabeçalho da nota e teste a confirmação.](https://ajuda.sankhya.com.br/hc/article_attachments/14608934128151)

**![Imagem 7: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16117657492375) CAUSA**:

Ocorre quando ao realizar lançamentos, informando desconto no rodapé, caso os parâmetros **"DISTJDCONF"** e/ou **"DISTDESCNFE"** estejam ligados e o desconto máximo definido nos itens não for suficiente para o rateio do valor aplicado em desconto.
