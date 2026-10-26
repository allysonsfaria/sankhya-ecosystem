---
id: "360044110614"
titulo: "O modelo para o ajuste de Entrada de estoque com terceiros não foi configurado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110614-O-modelo-para-o-ajuste-de-Entrada-de-estoque-com-terceiros-n%C3%A3o-foi-configurado"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-08-11T20:01:39Z"
rotulos: ["#revisadojunior", "Configuração", "Parceiro", "TOP", "Estoque", "Preferências", "INV_E00001", "Modelo de ajuste de estoque com terceiros não configurado", "Configure modelo em \"Empresa\" e \"Modelo de Notas e Pedidos\".", "Teste o ajuste ou crie filtro para desconsiderar produtos de terceiros."]
---

# O modelo para o ajuste de Entrada de estoque com terceiros não foi configurado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16582287151383) MENSAGEM:**

[INV\_E00001]: O modelo para o ajuste de Entrada de estoque com terceiros não foi configurado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16582271667479) SOLUÇÃO:**

![Imagem 3: Quando executada cópia/contagem de estoque considerando determinado(s) produto(s) com 'Parceiro' diferente de 0 (zero),…](https://ajuda.sankhya.com.br/hc/article_attachments/16582287155991) Quando executada cópia/contagem de estoque considerando determinado(s) produto(s) com 'Parceiro' diferente de 0 (zero), será exigido o modelo de ajuste de terceiros vinculado nas preferências da empresa:

- Tela **"Empresa"** (Caminho de acesso: Comercial » Preferências) » Aba 'Estoque/Preço'
- Campo **"Modelo ajuste de Entrada de Estoque com Terceiros"**.

![Imagem 4: Campo "Modelo ajuste de Entrada de Estoque com Terceiros" .](https://ajuda.sankhya.com.br/hc/article_attachments/15412114348311)

O modelo acima deverá ser configurado na tela **"Modelo de Notas e Pedidos"** (Caminho de acesso: Comercial » Consulta), considerando um 'Tipo de Operação - TOP' que realize as atualizações de estoque de terceiros necessárias para esse processo.

![Imagem 5: Após configuração das etapas acima, teste o ajuste novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16582271672471) Após configuração das etapas acima, teste o ajuste novamente.

**![Imagem 6: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16582287161623) IMPORTANTE:**

Caso não deseje que produtos de terceiros sejam ajustados/inventariados, é possível criar um filtro ao executar o ajuste de estoque para que esses sejam desconsiderados. Dessa forma, as configurações acima não serão exigidas, sendo considerados apenas produtos próprios em poder da empresa.

![Imagem 7: Caso não deseje que produtos de terceiros sejam ajustados/inventariados, é possível criar um filtro ao executar o…](https://ajuda.sankhya.com.br/hc/article_attachments/15412149587991)

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16582287163031) CAUSA:**

Quando executada cópia/contagem de estoque considerando determinado(s) produto(s) com 'Parceiro' diferente de 0 (zero) será exigido o modelo de ajuste de terceiros vinculado nas preferências da empresa para que o ajuste de estoque seja realizado.
