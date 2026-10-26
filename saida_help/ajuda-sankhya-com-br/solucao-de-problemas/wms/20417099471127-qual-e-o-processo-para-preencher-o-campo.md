---
id: "20417099471127"
titulo: "Qual é o processo para preencher o campo 'Em Recebimento WMS' na tela de Consulta de Produto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/20417099471127-Qual-%C3%A9-o-processo-para-preencher-o-campo-Em-Recebimento-WMS-na-tela-de-Consulta-de-Produto"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:51:07Z"
rotulos: ["Produtos", "Configuração", "WMS", "Estoque", "Preenchimento do Campo 'Em Recebimento WMS' na Tela de Consulta de Produto", "Squad WMS"]
---

# Qual é o processo para preencher o campo 'Em Recebimento WMS' na tela de Consulta de Produto

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/20433946335383) **SITUAÇÃO:**

Qual é o processo para preencher o campo 'Em Recebimento WMS' na tela de Consulta de Produto?

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/20417131308567)SOLUÇÃO:**

![Imagem 3: Ligue o parâmetro "Desconsidera estoque em doca do WMS? - SUBESTDOCAWMS",](https://ajuda.sankhya.com.br/hc/article_attachments/20433973271703) Ligue o parâmetro **"Desconsidera estoque em doca do WMS? - SUBESTDOCAWMS",**

![Imagem 4: Informe a Data de previsão de entrada no cabeçalho da nota de compra.](https://ajuda.sankhya.com.br/hc/article_attachments/20433973286423) Informe a Data de previsão de entrada no cabeçalho da nota de compra.

![Imagem 5: Ao enviar para o recebimento, utilizando a opção 'Enviar para o recebimento WMS' no botão outras opções dos portais, é…](https://ajuda.sankhya.com.br/hc/article_attachments/20433946364695) Ao enviar para o recebimento, utilizando a opção 'Enviar para o recebimento WMS' no botão outras opções dos portais, é necessário escolher uma doca que apenas trabalha com entrada de mercadoria e não entrada/saída.

Com as condições realizadas o campo 'Em recebimento WMS' será preenchido com a quantidade do item a receber consultado na rotina de Consulta de Produtos.

**Observações:**

- O sistema considera como 'a receber' todos os produtos que passaram pelo processo no coletor superwaba/totalcross e tiveram a conferência de entrada concluída.
- Após a finalização da tarefa de armazenagem em um desses dispositivos, o campo 'Em Recebimento WMS' será limpo.
