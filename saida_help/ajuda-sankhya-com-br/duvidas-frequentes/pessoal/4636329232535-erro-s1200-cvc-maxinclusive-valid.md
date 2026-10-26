---
id: "4636329232535"
titulo: " Erro S1200 - cvc-maxInclusive-valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4636329232535--Erro-S1200-cvc-maxInclusive-valid"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:29:59Z"
rotulos: ["Configuração", "Folha", "não apagar", "eSocial", "Erro de Validação no Valor de Rubrica", "Erro", "Central de Projetos"]
---

#  Erro S1200 - cvc-maxInclusive-valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16339983560087)  MENSAGEM:**

cvc-maxInclusive-valid: O valor '10087.00' não tem um aspecto válido em relação ao maxInclusive '9999.99' do tipo '#AnonType\_qtdRubrTItemRemuneracao'.
cvc-type.3.1.3: O valor '10087.00' do elemento 'qtdRubr' não é válido.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16339967833367) CAUSA:**

A formula do índice esta incorreta, fazendo com que apresente um valor maior que o permitido pelo layout.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16339967835799) SOLUÇÃO:**

Para a resolução do erro, siga os passos abaixo:

![Imagem 4: Avalie a fórmula do índice utilizado para evento que apresentou quantidade maior que o permitido;](https://ajuda.sankhya.com.br/hc/article_attachments/16339967847575) Avalie a fórmula do índice utilizado para evento que apresentou quantidade maior que o permitido;

![Imagem 5: Logo após, ajuste a fórmula do índice, recalcule a folha;](https://ajuda.sankhya.com.br/hc/article_attachments/16339983583383) Logo após, ajuste a fórmula do índice, recalcule a folha;

![Imagem 6: Desmarque a folha e libere novamente para Esocial;](https://ajuda.sankhya.com.br/hc/article_attachments/16339967853975) Desmarque a folha e libere novamente para Esocial;

![Imagem 7: Gere os eventos e libere para envio o S-1200.](https://ajuda.sankhya.com.br/hc/article_attachments/16339983593367) Gere os eventos e libere para envio o S-1200.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16339983601047) OBSERVAÇÃO:**

Caso não possa ser realizado o recálculo da folha por motivos de integração já realizada, como paliativo, pode ser feito o ajuste do valor do índice na tabela TFPFOL para o respectivo evento que apresentou erro. E posteriormente, como solução definitiva, avaliar a fórmula do índice.
