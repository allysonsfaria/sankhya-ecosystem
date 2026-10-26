---
id: "1500001885241"
titulo: "Um ou mais produtos da nota não possuem código de barras cadastrado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001885241-Um-ou-mais-produtos-da-nota-n%C3%A3o-possuem-c%C3%B3digo-de-barras-cadastrado"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:25:50Z"
rotulos: ["Produtos", "Configuração", "WMS", "NF-e", "Estoque", "#formatadoroger", "Produtos sem código de barras", "Valide e corrija cadastro no WMS", "Produtos sem código de barras configurado", "Erro"]
---

# Um ou mais produtos da nota não possuem código de barras cadastrado

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16287002070807) MENSAGEM**:

Um ou mais produtos da nota não possuem código de barras cadastrado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16287002074263) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a Validação de Configuração do WMS em: WMS » Rotinas » Validação de Configurações do WMS](https://ajuda.sankhya.com.br/hc/article_attachments/16286987447319) Acesse a Validação de Configuração do WMS em: WMS » Rotinas » Validação de Configurações do WMS

Filtro por:
Tipo de Validações: Produto

Clique no botão de filtro e selecione as opções:
[X] Produtos sem código de barras (Propriedades)
[X] Produtos sem código de barras (Unidade alternativa)

Clique em OK, depois 'Aplicar'.

![Imagem 4: Clique em OK, depois 'Aplicar'.](https://ajuda.sankhya.com.br/hc/article_attachments/360102952353)

O resultado, apresentara os produtos que estão com cadastros incompletos.

![Imagem 5: Acesse o cadastro de Produtos em: Configurações » Cadastros » Produtos » Produtos Aba: " Geral" Campo: "Referência"](https://ajuda.sankhya.com.br/hc/article_attachments/16286987450775) Acesse o cadastro de Produtos em: Configurações » Cadastros » Produtos » Produtos
Aba: **"Geral"**
Campo: **"Referência"**

Aba: **"Unidade alternativa"**Campo: **"Código de Barras"**

![Imagem 6: Após os ajustes, efetue o envio para o recebimento novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16287002084631) Após os ajustes, efetue o envio para o recebimento novamente.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16287002088471) CAUSA:**

Ocorre quando os produtos enviados para o recebimento não possuem código de barras, devidamente configurado.
