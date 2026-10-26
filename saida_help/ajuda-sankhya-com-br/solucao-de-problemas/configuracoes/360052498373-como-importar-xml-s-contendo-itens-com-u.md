---
id: "360052498373"
titulo: "Como importar XML'S contendo itens com \"unidades\" com mais de 2 caracteres"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052498373-Como-importar-XML-S-contendo-itens-com-unidades-com-mais-de-2-caracteres"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:29:48Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "XML", "Importação", "Importação de XMLs com Unidades com Mais de 2 Caracteres"]
---

# Como importar XML'S contendo itens com "unidades" com mais de 2 caracteres

Considere o xml do fornecedor contendo itens com mais de 2(dois) caracteres na sigla de sua unidade, conforme exemplo abaixo:

![Imagem 1: Considere o xml do fornecedor contendo itens com mais de 2(dois) caracteres na sigla de sua unidade, conforme exemplo…](https://ajuda.sankhya.com.br/hc/article_attachments/360083297413)

Nesse caso, o XML poderá ser importado normalmente. Visto que, conforme vínculo realizado entre o item do XML com o item correspondente no sistema, a conversão de "Unidade" será realizada.

**![Imagem 2: Como esse vínculo é realizado na Central de Compras?](https://ajuda.sankhya.com.br/hc/article_attachments/18942151806743) Como esse vínculo é realizado na Central de Compras?**

| - Ao tentar importar xml com unidade não cadastrada no sistema é apresentada a mensagem:   ![Imagem 3: Ao tentar importar xml com unidade não cadastrada no sistema é apresentada a mensagem:](https://ajuda.sankhya.com.br/hc/article_attachments/360084348514)   - O quadro 'Cadastre os produtos equivalentes' é apresentado. Neste momento é possível vincular o produto cadastrado no sistema e a unidade correspondente à unidade utilizada no xml, exemplo:   ![Imagem 4: O quadro 'Cadastre os produtos equivalentes' é apresentado. Neste momento é possível vincular o produto cadastrado no…](https://ajuda.sankhya.com.br/hc/article_attachments/360085512813)   - No exemplo será vinculado o produto 'GAI000011' do xml ao produto 'PRODUTO TESTE LU' no sistema, e a unidade PCE do XML para a unidade UN no sistema. - Após informar produtos equivalentes no sistema para todos os produtos sem vínculo, deverá clicar em **'Registrar Cód.Prod.do Fornec.'.**   Dessa forma ficará registrado como produto equivalente, o registro poderá ser visto no cadastro do produto, aba 'Produtos Equivalentes':  ![Imagem 5: Dessa forma ficará registrado como produto equivalente, o registro poderá ser visto no cadastro do produto, aba…](https://ajuda.sankhya.com.br/hc/article_attachments/360085512873)  E também no cadastro do parceiro, aba 'Produtos Equivalentes':  ![Imagem 6: E também no cadastro do parceiro, aba 'Produtos Equivalentes':](https://ajuda.sankhya.com.br/hc/article_attachments/360084348614) |
| --- |

![Imagem 7: Como esse vínculo é realizado no Portal de Importação de XML?](https://ajuda.sankhya.com.br/hc/article_attachments/18942158785431) **Como esse vínculo é realizado no Portal de Importação de XML?**

| - No Portal de Importação de xml, ao importar xml com produtos não cadastrados no sistema e ainda não vinculados, é apresentada a mensagem:   Divergências de produtos não encontrados.   - Neste caso o vínculo deve ser realizado na aba **'Produtos por Parceiro'** (mesmo nos casos onde a unidade do produto no xml contenha mais caracteres do que o cadastrado no sistema para o mesmo produto):   ![Imagem 8: Neste caso o vínculo deve ser realizado na aba 'Produtos por Parceiro' (mesmo nos casos onde a unidade do produto no…](https://ajuda.sankhya.com.br/hc/article_attachments/360084348734)    Da mesma forma o vínculo pode ser visto no cadastro do produto e também no cadastro do parceiro aba 'Produtos Equivalentes'. |
| --- |
