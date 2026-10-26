---
id: "39380443340439"
titulo: "Erro ao processar XML no Portal de Importação - Produtos vinculados manualmente não são salvos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39380443340439-Erro-ao-processar-XML-no-Portal-de-Importa%C3%A7%C3%A3o-Produtos-vinculados-manualmente-n%C3%A3o-s%C3%A3o-salvos"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-09-02T17:55:26Z"
rotulos: ["Produtos", "Configuração", "XML", "Importação", "Erro", "Artigo criado KCS", "Docs Eletrônicos - KCS"]
---

# Erro ao processar XML no Portal de Importação - Produtos vinculados manualmente não são salvos

**Situação**

Ao importar um XML pelo Portal de Importação, o sistema pode continuar exibindo a divergência **"Produto não encontrado"** mesmo após o usuário realizar o vínculo manual na aba Produtos Equivalentes.

A causa, na maioria dos casos, é o campo Controle não preenchido no cadastro do produto.

Durante a importação do XML:

- O produto é identificado como não encontrado.
- O usuário realiza o vínculo manual na aba **"Produtos Equivalentes"**.
- Ao salvar ou processar novamente, o vínculo não é gravado e a divergência permanecce.

**Solução**

Para resolver o problema, verifique e preencha corretamente o campo **"Controlar Por"** no cadastro do produto:

**(1)** Acesse a tela **"Produtos"**.
**(2)**  Verifique se o campo **"Controlar Por"** está devidamente preenchido na aba **"Medidas e Estoque"** no cadastro do produto.
**(3)** Caso o campo **"Controle"** esteja vazio, preencha-o com a informação adequada conforme a configuração do produto.
**(4)** Salve as alterações realizadas no cadastro do produto.
**(5)** Retorne ao **"Portal de Importação"** e processe novamente o arquivo XML.

**Causa**

Esse comportamento ocorre apenas quando o produto possui o campo Controle sem preenchimento. Portanto, sempre valide esse campo antes de recriar os vínculos de produtos equivalentes.
