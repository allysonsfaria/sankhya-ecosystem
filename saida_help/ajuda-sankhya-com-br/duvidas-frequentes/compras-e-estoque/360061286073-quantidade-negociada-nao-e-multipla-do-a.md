---
id: "360061286073"
titulo: "Quantidade negociada não e múltipla do agrupamento mínimo (XX) do produto YYY"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360061286073-Quantidade-negociada-n%C3%A3o-e-m%C3%BAltipla-do-agrupamento-m%C3%ADnimo-XX-do-produto-YYY"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T15:26:02Z"
rotulos: ["Produtos", "Configuração", "TOP", "Estoque", "não apagar", "#validadoSilvio", "ORA-20101", "Erro ORA-20101", "Agrupamento mínimo", "Solução de incidente"]
---

# Quantidade negociada não e múltipla do agrupamento mínimo (XX) do produto YYY

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16282527648535) MENSAGEM:**

[ORA-20101] Quantidade negociada não e múltipla do agrupamento mínimo (XX) do produto YYY.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16282527678231) CAUSA:**

Quando consta configurado Agrupamento mínimo para o produto e a quantidade do lançamento do item não é um múltiplo deste valor, ocorre a validação.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16282499602455) SOLUÇÃO:**

Para a resolução do incidente, siga os passos abaixo:

![Imagem 4: Acesse o cadastro do produto em: Configurações » Cadastros » Produto](https://ajuda.sankhya.com.br/hc/article_attachments/16282499606423) Acesse o cadastro do produto em: Configurações » Cadastros » Produto

![Imagem 5: Verifique na aba "Medidas e Estoque" o valor informado no campo "Agrupamento mínimo" .](https://ajuda.sankhya.com.br/hc/article_attachments/16282527669655) Verifique na aba **"Medidas e Estoque"** o valor informado no campo **"Agrupamento mínimo"**.

![Imagem 6: A quantidade a ser informada no lançamento deve ser um múltiplo deste valor.](https://ajuda.sankhya.com.br/hc/article_attachments/16282527671703) A quantidade a ser informada no lançamento deve ser um múltiplo deste valor.

(2)** Exemplo:** Agrupamento mínimo =5,  então no lançamento do item informe no campo Quantidade = 5; 10; 15; 20; 25; ....

(1)** IMPORTANTE:**

| - Essa validação pode ser controlada por 'Tipo de Operação', conforme marcação **'Valida agrupamento mínimo?'** da tela 'Comercial » Arquivo » Cadastros » **Tipos de Operação - TOP'**, aba Estoque:   **'Valida agrupamento mínimo?':**Por meio deste campo define-se qual validação será executada de acordo com o **"Agrupamento mínimo"** definido no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025389093-Produtos-), aba Medidas e estoque. São apresentadas as seguintes opções:   - **Não valida:** esta opção caracteriza que o agrupamento mínimo não será validado; - **Valida e bloqueia:** com esta opção selecionada, caso haja algum item negociado com a quantidade que não respeite o agrupamento mínimo e efetuado o bloqueio deste lançamento; - **Valida e exige liberação:** esta opção funciona de forma semelhante a opção anterior, sendo que ao invés de ocorrer o bloqueio, será solicitada a liberação do evento [78 - Liberação de agrupamento mínimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#78-liberaodeagrupamentomnimo) para que um usuário com alçada autorize o lançamento.     ![Imagem 7: Valida e exige liberação: esta opção funciona de forma semelhante a opção anterior, sendo que ao invés de ocorrer o…](https://ajuda.sankhya.com.br/hc/article_attachments/14921984132247) |
| --- |
