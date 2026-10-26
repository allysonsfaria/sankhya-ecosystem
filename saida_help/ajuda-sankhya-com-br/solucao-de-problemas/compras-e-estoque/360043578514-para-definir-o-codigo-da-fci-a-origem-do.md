---
id: "360043578514"
titulo: "Para definir o Código da FCI a origem do produto (ORIGPROD) deve ser definida entre 3, 5 ou 8. Produto: 'X'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043578514-Para-definir-o-C%C3%B3digo-da-FCI-a-origem-do-produto-ORIGPROD-deve-ser-definida-entre-3-5-ou-8-Produto-X"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-10-16T13:29:20Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "NF-e", "Origem do Produto", "XML", "SQL-50001", "Importação de XML", "Erro SQL-50001"]
---

# Para definir o Código da FCI a origem do produto (ORIGPROD) deve ser definida entre 3, 5 ou 8. Produto: 'X'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16106529445399) MENSAGEM:**

SQL-50001 Para definir o Código da FCI a origem do produto(ORIGPROD) deve ser definida entre 3, 5 ou 8. Produto: 'X'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16106552366743) SOLUÇÃO:**

![Imagem 3: Abra o XML que está sendo importado (Bloco de Notas e/ou Internet Explorer) e verifique para os respectivos itens qual…](https://ajuda.sankhya.com.br/hc/article_attachments/16106537285143) Abra o XML que está sendo importado (Bloco de Notas e/ou Internet Explorer) e verifique para os respectivos itens qual o valor informado na **tag <orig>**, conforme imagem abaixo:

![Imagem 4: Abra o XML que está sendo importado (Bloco de Notas e/ou Internet Explorer) e verifique para os respectivos itens qual…](https://ajuda.sankhya.com.br/hc/article_attachments/14507299367063)

![Imagem 5: Acesse a tela " Produtos " (Caminho de acesso: Configurações » Cadastros » Produtos ) e confira se os itens cadastrados…](https://ajuda.sankhya.com.br/hc/article_attachments/16106537297431) Acesse a tela "[**Produtos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)" (Caminho de acesso: Configurações » Cadastros » Produtos ) e confira se os itens cadastrados no sistema, que estão relacionados aos itens do XML, contém a mesma informação de 'Origem do produto'.

(2)** Exemplo:**

Para o produto do XML exemplificado acima o campo **"Origem do Produto"**, aba **"Geral"** será cadastrado:**5**, respeitando a tag <orig>5</orig>.

![Imagem 6: Para o produto do XML exemplificado acima o campo "Origem do Produto" , aba "Geral" será cadastrado: 5 , respeitando a…](https://ajuda.sankhya.com.br/hc/article_attachments/14507266966551)

![Imagem 7: Feito o ajuste, teste a importação do XML novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16106537300119) Feito o ajuste, teste a importação do XML novamente.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16106537301399) CAUSA:**

Na importação de XML, a mensagem será apresentada quando os produtos do XML, que possuem vínculos com os produtos do sistema, estão com a origem do Produto diferente de 3, 5 ou 8.
