---
id: "32128045631255"
titulo: "Peso bruto e Peso liquído. dos itens do cabecalho da nota não são calculados automaticamente, o que fazer?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32128045631255-Peso-bruto-e-Peso-liqu%C3%ADdo-dos-itens-do-cabecalho-da-nota-n%C3%A3o-s%C3%A3o-calculados-automaticamente-o-que-fazer"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T14:32:00Z"
rotulos: ["Produtos", "Configuração", "NF-e", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Peso bruto", "PESOLIQUIMANUAL", "Peso liq. dos itens", "PESOBRUTOMANUAL", "Peso Bruto Manual", "Erro"]
---

# Peso bruto e Peso liquído. dos itens do cabecalho da nota não são calculados automaticamente, o que fazer?

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32128032042519) **SITUAÇÃO:**

Embora os campos de "**Peso Bruto"** e "**Peso Líquido"** sejam corretamente calculados nos itens da nota, os valores não são refletidos nos respectivos campos do **cabeçalho** da nota.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32128032044055)SOLUÇÃO:**

Para que os campos de peso no cabeçalho da nota sejam calculados automaticamente, siga os passos abaixo:

**![Imagem 3: Verifique no cabeçalho da nota se os campos Peso Líquido Manual e Peso Bruto Manual estão disponíveis e visíveis.](https://ajuda.sankhya.com.br/hc/article_attachments/32419540148119) Verifique** no cabeçalho da nota se os campos Peso Líquido Manual e Peso Bruto Manual estão disponíveis e visíveis.

**(1)** Caso os campos **não estejam visíveis**, acesse a tela **"Configurador de Layout da Nota"**(Comercial » Configuração » Configurador de Layout da Nota), localize e **inclua** os campos Peso Líquido Manual (PESOLIQUIMANUAL) e Peso Bruto Manual (PESOBRUTOMANUAL) no layout do cabeçalho da nota.

![Imagem 4: Após incluir os campos, feche e reabra a Central , acesse a nota novamente e verifique se os campos Peso Líquido Manual…](https://ajuda.sankhya.com.br/hc/article_attachments/32419540153239) Após incluir os campos, **feche e reabra a Central**, acesse a nota novamente e **verifique se os campos Peso Líquido Manual e Peso Bruto Manual estão marcados**. Caso estejam, **desmarque ambos**.

![Imagem 5: Crie uma nova nota para que as alterações tenham efeito. A partir desse momento, os campos Peso Bruto e Peso Líquido do…](https://ajuda.sankhya.com.br/hc/article_attachments/32419533001495) Crie uma nova nota para que as alterações tenham efeito. A partir desse momento, os campos Peso Bruto e Peso Líquido do cabeçalho passarão a ser calculados automaticamente com base nos itens da nota.

![Imagem 6: Os campos incluídos no layout podem ser removidos posteriormente , pois, uma vez desmarcados, o sistema passa a assumir…](https://ajuda.sankhya.com.br/hc/article_attachments/32419533004311) Os campos incluídos no layout podem ser **removidos posteriormente**, pois, uma vez desmarcados, o sistema passa a assumir o valor padrão “**Não**”, mesmo que não estejam visíveis no layout.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/32128032044695)CAUSA:**

Esse comportamento ocorre porque os campos **PESOLIQUIMANUAL** e **PESOBRUTOMANUAL**, quando marcados como “**Sim**”, dizem ao sistema que o peso será informado manualmente. Nesse cenário, a rotina de totalização da nota não calcula os valores de forma automática, mesmo que os itens estejam preenchidos corretamente.
