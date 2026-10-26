---
id: "9403939895319"
titulo: "Não encontramos Produção p/Produtos com Filtro no período"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9403939895319-N%C3%A3o-encontramos-Produ%C3%A7%C3%A3o-p-Produtos-com-Filtro-no-per%C3%ADodo"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T15:08:02Z"
rotulos: ["Produtos", "Custos", "Configuração", "Produção", "COM_E00549", "Produção não encontrada no período", "Falta de nota com tarifa CIP ou configuração incorreta", "Verifique notas e tarifação; ajuste se necessário", "Erro"]
---

# Não encontramos Produção p/Produtos com Filtro no período

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18696640210967) MENSAGEM:**

[COM\_E00549] Não encontramos Produção p/Produtos com Filtro no período.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18696640217111) SITUAÇÃO:**

Ao realizar a Apropriação de Custos Indiretos de Produção, na tela Produção » Rotinas » Apropriação de Custos Indiretos de Produção (CIP)", apresenta a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18696640219671) SOLUÇÃO:**

![Imagem 4: Verifique se existe nota de produção, com a tarifa CIP dentro do período informado;](https://ajuda.sankhya.com.br/hc/article_attachments/18696640224279) Verifique se existe nota de produção, com a tarifa CIP dentro do período informado;

![Imagem 5: Caso alguma nota não contenha a tarifa CIP, verifique se o tipo de índice da tarifa é variável (execução de…](https://ajuda.sankhya.com.br/hc/article_attachments/18696627152151) Caso alguma nota não contenha a tarifa CIP, verifique se o tipo de índice da tarifa é variável (execução de atividades). Para incluir a CIP, cancele a OP e lance uma nova OP, com um tempo de apontamento entre data hora início e data hora fim maior que zero minutos.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18696640241175) CAUSA:**

![Imagem 7: Quando não existe nota de produção com a tarifa CIP no período informado;](https://ajuda.sankhya.com.br/hc/article_attachments/18696640224279) Quando não existe nota de produção com a tarifa CIP no período informado;

![Imagem 8: Quando a configuração do tipo de índice da tarifa CIP está como "Variável (execução de atividades)" e o tempo de…](https://ajuda.sankhya.com.br/hc/article_attachments/18696627152151) Quando a configuração do tipo de índice da tarifa CIP está como "Variável (execução de atividades)" e o tempo de execução da atividade - entre a diferença de data hora início e data hora do fim do apontamento - for igual a zero, a CIP não é lançada na nota de produção.
