---
id: "34945017571223"
titulo: "WMS_E00936: no endereço: Y, o Produto está configurado para armazenar no máximo: X UN"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34945017571223-WMS-E00936-no-endere%C3%A7o-Y-o-Produto-est%C3%A1-configurado-para-armazenar-no-m%C3%A1ximo-X-UN"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:26:21Z"
rotulos: ["Produtos", "Configuração", "WMS", "Estoque", "Erro", "No endereço: Y o Produto está configurado para armazenar no máximo", "Quantidade à transferir", "Estoque atual no endereço de destino", "WMS_E00936"]
---

# WMS_E00936: no endereço: Y, o Produto está configurado para armazenar no máximo: X UN

**MENSAGEM**

[WMS\_E00936] No endereço: Y, o Produto está configurado para armazenar no máximo: X UN. Quantidade à transferir: X UN. Estoque atual no endereço de destino: X UN.

**SITUAÇÃO**

O usuário estava realizando uma **transferência entre endereços** no sistema WMS e a operação foi bloqueada porque a quantidade a ser transferida **excede a capacidade máxima** configurada para o endereço de destino.

**SOLUÇÃO**

**(1)** Acesse a tela **"Endereço de Armazenamento"** (WMS » Cadastros » Endereço de Armazenamento) e navegue até a aba **"Produtos"**.

**(2)** Localize o produto em questão e **altere a quantidade de estoque máximo** permitido de acordo com a capacidade real do endereço de destino.

**Alternativa:**

**(3)** Caso a capacidade do endereço já esteja no **máximo permitido**, identifique outro endereço disponível que possua capacidade suficiente para receber a transferência do estoque.

**CAUSA**

A mensagem ocorre quando o sistema detecta que uma **transferência entre endereços** resultaria em uma quantidade de estoque que **excede o limite máximo** configurado para o produto no endereço de destino.
