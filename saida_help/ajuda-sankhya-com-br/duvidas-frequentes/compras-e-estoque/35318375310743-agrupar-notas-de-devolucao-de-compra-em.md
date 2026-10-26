---
id: "35318375310743"
titulo: "Agrupar notas de devolução de compra em uma única nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35318375310743-Agrupar-notas-de-devolu%C3%A7%C3%A3o-de-compra-em-uma-%C3%BAnica-nota"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-30T12:48:59Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "Estoque", "Preferências", "Ao selecionar mais de uma nota de compra para fazer devolução", "o sistema cria uma nota de devolução para cada nota selecionada", "mesmo com a opção \"Uma nota para cada\" desmarcada", "Artigo atualizado KCS", "CVE - KCS"]
---

# Agrupar notas de devolução de compra em uma única nota

**SITUAÇÃO**

Ao selecionar mais de uma nota de compra para devolução, desmarcar a opção **"Uma nota para cada"** e clicar em **"Botão Dev./Est."**, o sistema deveria gerar uma única nota de devolução para todas as notas selecionadas. Porém, ele gera uma nota separada para cada nota, como se a consolidação não tivesse sido aplicada.

![Imagem 1: Ao selecionar mais de uma nota de compra para devolução, desmarcar a opção "Uma nota para cada" e clicar em "Botão…](https://ajuda.sankhya.com.br/hc/article_attachments/35318375303703)

**Observação:** No processo de devolução de estoque de terceiros, é possível consolidar várias notas fiscais de entrada em uma única nota de saída, desde que o usuário tenha a permissão de acesso necessária para a rotina de agrupamento.

**SOLUÇÃO**

**(1)** Confira se todas as notas selecionadas têm o mesmo TOP, parceiro e empresa. Se algum desses campos divergir, a consolidação não é possível nesse caso, separe as notas por grupos com os mesmos valores antes de gerar a devolução.

**(2)** Se os campos estiverem corretos e o problema persistir, verifique com o administrador se o usuário possui a permissão para agrupar devoluções.

**Alternativa: devolução individual**

Se não for possível ajustar as notas ou liberar a permissão, é possível seguir com a devolução individual (uma nota para cada). Isso mantém o controle separado das operações e facilita a rastreabilidade em caso de impactos no financeiro ou na contabilidade.

**CAUSA**

Isso pode acontecer por dois motivos:

- As notas de compra selecionadas não têm os mesmos **TOP, parceiro e empresa**. Esses três campos precisam ser idênticos em todas as notas para que o agrupamento seja possível.
- O usuário não tem permissão para executar a rotina de agrupamento de devoluções.
