---
id: "27061772198039"
titulo: "Ao importar o campo  \"Fabricante\" da instância de Produto para instância de Serviço não aparece para ser importado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27061772198039-Ao-importar-o-campo-Fabricante-da-inst%C3%A2ncia-de-Produto-para-inst%C3%A2ncia-de-Servi%C3%A7o-n%C3%A3o-aparece-para-ser-importado"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T14:40:13Z"
rotulos: ["Produtos", "Configuração", "Importação", "Serviços", "Passos para resolver", "Razão do erro", "Detalhe do erro", "não aparece para ser importado", "importar o campo \"Fabricante\"", "instância de Produto para instância de Serviço", "Erro"]
---

# Ao importar o campo  "Fabricante" da instância de Produto para instância de Serviço não aparece para ser importado

Ao importar o campo **"Fabricante"** da instância de Produto para instância de Serviço, não aparece para ser importado.

![Imagem 1: Ao importar o campo "Fabricante" da instância de Produto para instância de Serviço, não aparece para ser importado.](https://ajuda.sankhya.com.br/hc/article_attachments/27061772171159)

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/27061764129431)SOLUÇÃO:**

Por meio do botão **"Importar Campo",** localizado no alto da aba **"Campos"**, é possível importar para a tela do sistema um campo de outra tabela, sendo ela adicional ou oficial do sistema. Isso é equivalente a criar uma chave estrangeira para a outra tabela. Como ambas as instâncias tratam-se da mesma tabela "TGFPRO" não é possível importar os campos.
Nessa situação, recomenda-se criar novas instâncias adicionais para Fabricante e realizar a ligação da instância de Serviço com estas novas.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/27061764133399)CAUSA:**

Ocorre quando tenta importar um campo da instância do cadastro do produto para a instância de serviço, ou seja o campo é da mesma tabela.
