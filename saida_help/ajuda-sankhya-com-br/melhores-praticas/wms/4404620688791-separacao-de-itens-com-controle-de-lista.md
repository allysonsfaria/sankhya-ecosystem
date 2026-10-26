---
id: "4404620688791"
titulo: "Separação de itens com controle de lista"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4404620688791-Separa%C3%A7%C3%A3o-de-itens-com-controle-de-lista"
trilha: "Melhores Práticas > WMS"
atualizado_em: "2026-08-04T19:22:56Z"
rotulos: ["Produtos", "Configuração", "WMS", "Estoque", "Erro na Separação de Itens com Controle de Lista", "Erro"]
---

# Separação de itens com controle de lista

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16368896703127) MENSAGEM:**

Parâmetro **wms.exige.controle.voa.produto.lista** não existe na definição de parâmetros.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16368928518167) SOLUÇÃO:**

Para correção do erro:

- Acesse ao cadastro do produto, no qual o item trabalha com controle adicional por 'Lista'. Com este tipo de controle deve ser configurado na unidades alternativas um código de barra para cada controle, sendo que pra multiplicar por '1' e gerando um registro para cada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16368896706711)CAUSA:**

Ao tentar Realizar uma Tarefa de Separação no Coletor SuperWaba, após informar informar um determinando produto ocorre a mensagem a seguir.
