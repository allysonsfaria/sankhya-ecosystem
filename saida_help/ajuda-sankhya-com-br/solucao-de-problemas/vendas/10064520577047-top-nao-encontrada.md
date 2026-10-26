---
id: "10064520577047"
titulo: "TOP não encontrada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10064520577047-TOP-n%C3%A3o-encontrada"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:04:50Z"
rotulos: ["CT-e", "Configuração", "Movimentação Financeira", "XML", "Importação", "TOP", "CORE_E03183", "Configure TOP nas Preferências e Portal de Importação de XML", "TOP não encontrada ao importar XML", "TOP não informada corretamente no Portal de Importação de XML"]
---

# TOP não encontrada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18918039139351) MENSAGEM:**

[CORE\_E03183] TOP não encontrada.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18918047565975) SITUAÇÃO:**

Ao realizar a importação de um XML a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18918039153943) SOLUÇÃO:**

![Imagem 4: Realize os lançamentos de CT-e, no Portal de Importação de XML (Comercial » Rotinas » Portal de importação de XML) , o…](https://ajuda.sankhya.com.br/hc/article_attachments/18918039158679) Realize os lançamentos de CT-e, no **Portal de Importação de XML** (Comercial » Rotinas » Portal de importação de XML), o sistema sempre vai pegar a TOP de movimentação Financeira configurado nas Preferências para Importar o CT-e.

![Imagem 5: Realize os lançamentos de CT-e, no Portal de Importação de XML (Comercial » Rotinas » Portal de importação de XML) , o…](https://ajuda.sankhya.com.br/hc/article_attachments/10064368029079)

![Imagem 6: Realize os lançamentos de CT-e, no Portal de Importação de XML (Comercial » Rotinas » Portal de importação de XML) , o…](https://ajuda.sankhya.com.br/hc/article_attachments/10064316732183)

Grid do Portal de Importação de XML.

![Imagem 7: Grid do Portal de Importação de XML.](https://ajuda.sankhya.com.br/hc/article_attachments/18918039168407)

![Imagem 8: Caso utilize a Opção de Importar CT-e com Cabeçalho e TOP de movimento de compra, marque o campo: "Importar CT-e com…](https://ajuda.sankhya.com.br/hc/article_attachments/18918047592471) Caso utilize a Opção de Importar CT-e com Cabeçalho e TOP de movimento de compra, marque o campo: "Importar CT-e com Cabeçalho", na tela de Preferencias para Importação do CT-e,  e desligue o parâmetro: TOPDIGIMPXMLCTE.

![Imagem 9: Caso utilize a Opção de Importar CT-e com Cabeçalho e TOP de movimento de compra, marque o campo: "Importar CT-e com…](https://ajuda.sankhya.com.br/hc/article_attachments/18918047593879)

![Imagem 10: Caso utilize a Opção de Importar CT-e com Cabeçalho e TOP de movimento de compra, marque o campo: "Importar CT-e com…](https://ajuda.sankhya.com.br/hc/article_attachments/18918039190679)

![Imagem 11: Ao realizar o processo acima, a TOP será atribuída "APENAS" na tela de central de Compras.](https://ajuda.sankhya.com.br/hc/article_attachments/18918039192727) Ao realizar o processo acima, a TOP será atribuída "APENAS" na tela de central de Compras.

![Imagem 12: Ao realizar o processo acima, a TOP será atribuída "APENAS" na tela de central de Compras.](https://ajuda.sankhya.com.br/hc/article_attachments/18918047610519)

![Imagem 13: Na tela de Portal de Importação de XML prevalecerá a TOP informada.](https://ajuda.sankhya.com.br/hc/article_attachments/18918039209111) Na tela de Portal de Importação de XML prevalecerá a TOP informada.

![Imagem 14: Na tela de Portal de Importação de XML prevalecerá a TOP informada.](https://ajuda.sankhya.com.br/hc/article_attachments/18918047619223)

Ou seja, a TOP é convertida apenas na tela de Central de compras, considerando configurações acima.

**![Imagem 15: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18918039218711) OBSERVAÇÃO:**

Se desejar que a tela do Portal de Importação de XML fique com o mesmo layout da Central de Compras, será necessário fazer a alteração manualmente. Acesse o [Portal de importação de XML – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML) para maiores informações.

**![Imagem 16: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18918039223703)CAUSA:**

Ocorre quando a TOP para importação do CT-e não é devidamente informada na tela Portal de Importação de XML.
