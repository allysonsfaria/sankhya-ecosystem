---
id: "360043579534"
titulo: "A tabela de origem tem data de vigor maior que a data de vigor da própria tabela"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043579534-A-tabela-de-origem-tem-data-de-vigor-maior-que-a-data-de-vigor-da-pr%C3%B3pria-tabela"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-09-03T14:30:42Z"
rotulos: ["#RevisadoGui", "#RevisadoCarmen", "Configuração", "Correção", "TOP", "ORA-20101", "Erro de Data em Tabela de Preços", "Erro", "Tabelas de Preço"]
---

# A tabela de origem tem data de vigor maior que a data de vigor da própria tabela

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16363271243287) MENSAGEM:**

[ORA-20101]: A tabela de origem tem data de vigor maior que a data de vigor da própria tabela. CODTABORIG: 0 DTVIGOR: 29/08/18
[ORA-06512]: em "SANKHYA.TRG\_INC\_TGFTAB\_AFTER", line 105
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG\_INC\_TGFTAB\_AFTER'

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16363316185495) SITUAÇÃO:**

Ao tentar confirmar uma Nota de Compra, utilizando uma TOP que atualize Custo e Preço de Venda, a mensagem  é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16363271252375) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse a tela 'Tabelas de Preços' (Comercial » Arquivo)](https://ajuda.sankhya.com.br/hc/article_attachments/16363271253911) Acesse a tela **'Tabelas de Preços'** (Comercial  »  Arquivo)

- Faça uma busca nessa tela pela possível tabela com Data de Vigor maior que a data de entrada/saída**\*\*** do seu lançamento.
- Para isso, aplique os dados da tela e ordene  por Dt.Vigor.
- Caso haja **alguma tabela com Data de Vigor maior que a data de lançamento da nota**, ocorrerá o erro.

![Imagem 5: Será necessário alinhar com sua equipe sobre a tabela e caso ela realmente tenha que existir, verifique a data e…](https://ajuda.sankhya.com.br/hc/article_attachments/16363271256343) Será necessário alinhar com sua equipe sobre a tabela e caso ela realmente tenha que existir, verifique a data e reconsidere lançar a nota com data superior a data de vigor da tabela.

![Imagem 6: Verifique também se existe uma nota de compra com data superior, no qual originou a tabela com data de vigor superior.…](https://ajuda.sankhya.com.br/hc/article_attachments/16363316198807) Verifique também se existe uma nota de compra com data superior, no qual originou a tabela com data de vigor superior. Caso esteja incorreta, exclua a nota e lance as notas com as datas corretas novamente.

**![Imagem 7: OBSERVAÇÃO: A Tabela de preço pode ser criada de forma manual, automática, através de algum processo interno da empresa…](https://ajuda.sankhya.com.br/hc/article_attachments/16363271264407) OBSERVAÇÃO:**A Tabela de preço pode ser criada de forma manual, automática, através de algum processo interno da empresa ou através do lançamento de uma nota de compra, no qual a TOP está configurada para atualizar custo e preço de venda (Campo: Precifica do Cadastro da TOP).

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16363316204951)CAUSA:**

Ocorre quando a data de entrada da nota está inferior a data de vigor da última tabela de preço do(s) produto(s) correspondente a Nota.

**Exemplo:**

**Data de lançamento da nota:** 28/09/2018 - Produto X

**Data de vigor da ultima tabela de preço do produto X:** 30/09/2018

**Ocorre em 2 casos:**

**Caso 1:** Quando já existe uma tabela de preço em uma data de vigor X e a data de lançamento da nota é inferior a esta data da tabela de preço.

**Caso 2:** Quando equivocadamente a tabela de preço criada tem um data de vigor errada: Ex: 01/09/2048 (erro de digitação).

**![Imagem 9: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16363271264407) OBSERVAÇÕES:**

**(1)** Para saber qual data de lançamento é considerada para Data de Vigor, acesse a rotina de Preferências e pesquise pelo parâmetro **"DTPDTVIGOR-Data de entrada para Data de Vigor da tab.de Preço".**

**(1)** Esse erro normalmente ocorre quando a nota de compra é lançada com data retroativa. Sendo necessário confirmar a nota com a data atual e depois de confirmada alterar a data para a correta.
