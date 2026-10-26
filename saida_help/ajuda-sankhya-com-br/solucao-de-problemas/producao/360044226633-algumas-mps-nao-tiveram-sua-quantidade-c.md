---
id: "360044226633"
titulo: "Algumas MPs não tiveram sua quantidade completamente reproporcionalizada pois a quantidade reservada já foi totalmente distribuída em apontamentos da OP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044226633-Algumas-MPs-n%C3%A3o-tiveram-sua-quantidade-completamente-reproporcionalizada-pois-a-quantidade-reservada-j%C3%A1-foi-totalmente-distribu%C3%ADda-em-apontamentos-da-OP"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T16:00:02Z"
rotulos: ["#RevisadoCarmen", "OS-1207510", "Apontamento", "Ordem de Serviço", "Estoque", "Produção", "Transferência MP necessária", "Estoque indisponível OP", "MPs faltantes produção", "Erro"]
---

# Algumas MPs não tiveram sua quantidade completamente reproporcionalizada pois a quantidade reservada já foi totalmente distribuída em apontamentos da OP

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16365388548887) MENSAGEM:**

Algumas MPs não tiveram sua quantidade completamente reproporcionalizada pois a quantidade reservada já foi totalmente distribuída em apontamentos da OP.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16365388551319) SITUAÇÃO:**

Ao fazer um apontamento parcial ou confirmar um apontamento total retorna a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16365359675415) SOLUÇÃO:**

![Imagem 4: Para solução deverá ser feito uma transferência de MPs faltantes para o Local de Produção onde será consumido na…](https://ajuda.sankhya.com.br/hc/article_attachments/16365388558999) Para solução deverá ser feito uma transferência de MPs faltantes para o Local de Produção onde será consumido na produção.

- **Exemplo:** o PA 10 usa as MPs A, B e C em sua composição e a proporção é de 1 para 1, ou seja uma MP para produzir um PA;
- Ao lançar a OP de 100 o sistema executa a operação de estoque que separa 100 unidades de cada MP. Essas quantidades são vinculadas à aba de **"Movimentações Acessórias"** e o sistema passa a considerar esse estoque para a produção.
- Após iniciar a produção, o usuário redimensiona o tamanho do lote para 150, como a OP já está em andamento o sistema não faz uma nova transferência.
- Após apontar todas as MPs para produzir a quantidade inicial da OP de 100, não haverá mais estoque disponível nas movimentações acessórias.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16365388560151) CAUSA:**

Ao iniciar uma OP que tenha configurado operações de estoque que façam transferência ou requisição de MPs, a quantidade para produzir o lote do PA é alocada como estoque para produção na aba Movimentações acessórias e o sistema passa a considerar essa quantidade como estoque disponível para produção.

Caso o usuário faça o redimensionamento do tamanho do lote para uma quantidade maior do que a quantidade lançada, após usar toda a quantidade da MP que está na aba de movimentações acessórias,  a mensagem vai retornar para os próximos apontamentos, pois não há mais estoque de MP disponível para a produção.
