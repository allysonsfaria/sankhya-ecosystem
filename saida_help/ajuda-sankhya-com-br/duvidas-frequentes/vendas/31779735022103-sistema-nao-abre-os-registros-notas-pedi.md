---
id: "31779735022103"
titulo: "Sistema não abre os registros (notas/pedidos) pelas Centrais via Tela de Liberação de Limite, o que fazer?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31779735022103-Sistema-n%C3%A3o-abre-os-registros-notas-pedidos-pelas-Centrais-via-Tela-de-Libera%C3%A7%C3%A3o-de-Limite-o-que-fazer"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:32:23Z"
rotulos: ["Configuração", "Segurança", "Movimentação Financeira", "Centrais", "Liberação de Limites", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Abrir a central", "Tela liberação de limites", "abrir notas", "abrir pedidos", "Central de vendas"]
---

# Sistema não abre os registros (notas/pedidos) pelas Centrais via Tela de Liberação de Limite, o que fazer?

Este artigo descreve o comportamento observado quando ocorre a impossibilidade de abrir pedidos ou notas pelas Centrais (Central de Vendas ou Movimentação Financeira) a partir da tela de **Liberação de Limite**. Também são apresentados os ajustes necessários para a correção do problema.

Ao tentar utilizar a opção **"Abrir a Central"** na tela de Liberação de Limite, o sistema não posiciona  corretamente  no  pedido ou nota correspondente. Esse comportamento normalmente está relacionado a restrições de segurança configuradas no perfil do usuário, que limitam a visualização de documentos de outros vendedores.

#### **(1)** Funcionamento da Opção "Abrir a Central"

A funcionalidade **"Abrir a Central"** tem os seguintes comportamentos, conforme o tipo de Evento posicionado  :

- **Pedidos/Notas**: abre a Central de Vendas ou a **"Venda Assistida"**, já posicionando no registro correspondente.
- **Títulos de Receita/Despesa**: abre a tela de **"Movimentação Financeira"**, também já posicionada no item em questão.

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31779735013911)SOLUÇÃO:**

Para corrigir o problema, siga os passos abaixo:

- Acesse o **cadastro do usuário logado;**
- Vá até a aba **Segurança,** localize o campo : **"Ver Pedidos/notas (WEB)" EDIDOS/NOTAS (WEB)**e nele selecione a opção **"De todos";**
- Salve as alterações;
- Solicite que o usuário refaça o processo na tela de Liberação de Limite.

Após essa alteração, a funcionalidade "Abrir a Central" deverá operar corretamente, permitindo o acesso direto ao registro esperado.

![Imagem 2: Após essa alteração, a funcionalidade "Abrir a Central" deverá operar corretamente, permitindo o acesso direto ao…](https://ajuda.sankhya.com.br/hc/article_attachments/31995803601431)

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31779735015063)CAUSA:**

O problema ocorre quando o usuário possui restrições de visualização definidas, como por exemplo:

- Permissão de visualização configurada como **"Somente do vendedor"**.

Com isso, o sistema impede o acesso a pedidos ou notas de outros vendedores, mesmo ao acionar a opção de abertura via Liberação de Limite.
