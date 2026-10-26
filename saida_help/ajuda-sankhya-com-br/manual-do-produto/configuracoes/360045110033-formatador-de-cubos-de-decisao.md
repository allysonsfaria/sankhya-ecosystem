---
id: "360045110033"
titulo: "Formatador de Cubos de Decisão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110033-Formatador-de-Cubos-de-Decis%C3%A3o"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-22T15:45:51Z"
rotulos: ["SQL", "Análise de Compras e Vendas", "Configuração", "Relatórios", "Fast Service", "Análise Financeira", "Business Intelligence", "Cálculo de Folha", "Cubo de Decisão", "Formatador de Cubos de Decisão", "Movimento Mensal", "Formatador de Cubos de Decisão manual", "Financeiro", "Formatador de Cubos de Decisão: Ferramenta Dinâmica de B.I."]
---

# Formatador de Cubos de Decisão

Essa ferramenta é utilizada para configurar cubos de decisão e gerar informações a partir dos registros armazenados no banco de dados.

Sendo assim, a diferença entre um relatório formatado e o cubo de decisão é que um é estático, ou seja, apesar de mostrar uma quantidade maior de informações, não permite que você as consulte de ângulos diferentes.

O cubo, por sua vez, é dinâmico e possibilita que as informações sejam manipuladas e que novos resultados rapidamente possam ser visualizados. Um relatório deve ser processado, sempre que você quiser consultar uma nova informação.

Para usar o cubo basta processá-lo uma única vez, para obter várias informações diferentes a partir dos mesmos dados de origem.

O Cubo de Decisão é uma ferramenta fundamentada nos conceitos de B.I. (Business Intelligence), e é utilizada por gestores em qualquer nível da empresa, para lhes fornecer análises comparativas, fundamentais na tomada de decisão. Esse tipo de ferramenta amplia a capacidade de comparação das informações, mudando dinamicamente o relacionamento entre os dados.

O Formatador de Cubos disponível no Sankhya Om permite a criação de diversas configurações de cubos, dado que estas são inseridas através de algumas telas. Cada uma dessas configurações, permite trabalhar com um conjunto diferente de campos, permitindo manter várias análises guardadas, para utilização sempre que necessário.

Para facilitar a construção dessas consultas, o Formatador de Cubos usa estruturas básicas pré-cadastradas, que mapeiam os relacionamentos entre as tabelas, rotulando essas estruturas como **"Campos de cubo"** (exatamente da mesma forma do formatador de relatórios). Assim, você poderá encontrar o Formatador de Cubos nas seguintes telas:

- [Análise de Compras e Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594194-An%C3%A1lise-de-Compras-e-Vendas);
- [Cubo de decisão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108513-Cubo-de-Decis%C3%A3o);
- [Análise Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606174-An%C3%A1lise-Financeira);
- [Cubo de decisão - Cálculo de Folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602574-Cubo-de-decis%C3%A3o-C%C3%A1lculo-de-Folha);
- [Cubo de decisão - Movimento Mensal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598854-Cubo-de-decis%C3%A3o-Movimento-Mensal).

Ao acessar, por exemplo, a tela Análise de Compras e Vendas, primeiramente a tela exibirá uma grade, contendo os cubos que já estão cadastrados no sistema:

![Imagem 1: Ao acessar, por exemplo, a tela Análise de Compras e Vendas , primeiramente a tela exibirá uma grade, contendo os cubos…](https://ajuda.sankhya.com.br/hc/article_attachments/4414029453975)

O campo **"Modelo"** indicará se o cubo é ou não um modelo.

Referente ao campo **"Fast Service"** está disponível para edição e indica se o **"Cubo"** estará ou não disponível no módulo **"Fast Service"**.

O sistema não permitirá a modificação de cubos modelos, portanto, caso queira modificá-lo será necessário duplicar o cubo modelo e alterar a cópia.

Ao clicar no botão ![Imagem 2: Ao clicar no botão "Modo Formulário" , no botão "Novo" , ou no botão "Modo Edição" , o sistema entrará no "Formatador…](https://ajuda.sankhya.com.br/hc/article_attachments/16276005252247) **"Modo Formulário"**, no botão ![Imagem 3: Ao clicar no botão "Modo Formulário" , no botão "Novo" , ou no botão "Modo Edição" , o sistema entrará no "Formatador…](https://ajuda.sankhya.com.br/hc/article_attachments/16275962696087) **"Novo"**, ou no botão ![Imagem 4: Ao clicar no botão "Modo Formulário" , no botão "Novo" , ou no botão "Modo Edição" , o sistema entrará no "Formatador…](https://ajuda.sankhya.com.br/hc/article_attachments/16276005264279) **"Modo Edição"**, o sistema entrará no **"Formatador de Cubo de Decisão"**:

![Imagem 5: Ao clicar no botão "Modo Formulário" , no botão "Novo" , ou no botão "Modo Edição" , o sistema entrará no "Formatador…](https://ajuda.sankhya.com.br/hc/article_attachments/4414043932311)

#### A seguir, você pode consultar os campos disponíveis:

No painel abaixo do campo **"Disponível"**, temos um painel onde você pode selecionar quais os campos farão parte do Cubo de Decisão apenas o arrastando para o painel abaixo do campo **"Selecionados"**, ou ainda, fazê-lo por meio das setas entre os painéis.

[GIF animado: Imagem 6: No painel abaixo do campo "Disponível" , temos um painel onde você pode selecionar quais os campos farão parte do Cubo…](https://ajuda.sankhya.com.br/hc/article_attachments/4414044074519)

Assim como na seleção de campos, os campos do painel Disponível poderão ser arrastados para o campo "Expressão de filtro", de forma que, ao inserir um campo no referido filtro, o pop-up "Novo Critério" será exibido, onde você informar os critérios.

[GIF animado: Imagem 7: Assim como na seleção de campos, os campos do painel Disponível poderão ser arrastados para o campo "Expressão de…](https://ajuda.sankhya.com.br/hc/article_attachments/4414044722199)

Essa expressão poderá ser editada livremente, sem a necessidade de usar os campos (A expressão é parte da consulta SQL e os recursos da linguagem podem ser usados).

---

#### Manutenção de campos

Foi dito anteriormente que os campos de cubo são estruturas básicas pré-cadastradas que mapeiam os relacionamentos entre as tabelas. Na prática, podemos pensar nos campos, como fragmentos de consulta SQL, acrescidos de algumas informações necessárias para identificá-lo em um cubo.

| ![Imagem 8: Foi dito anteriormente que os campos de cubo são estruturas básicas pré-cadastradas que mapeiam os relacionamentos…](https://ajuda.sankhya.com.br/hc/article_attachments/16276023352599) | As tarefas de definição e alteração de campos são reservadas aos usuários que possuem habilidades com banco de dados e uma ampla visão das tabelas que o sistema utiliza para gravar as informações, sendo estes, normalmente consultores. |
| --- | --- |

O botão ![Imagem 9: O botão "Manutenção dos Campos" dará acesso ao modo "Manutenção de campos" , onde você poderá editar, inserir ou…](https://ajuda.sankhya.com.br/hc/article_attachments/16276097407767) **"Manutenção dos Campos"**  dará acesso ao modo **"Manutenção de campos"**, onde você poderá editar, inserir ou excluir registros:

![Imagem 10: O botão "Manutenção dos Campos" dará acesso ao modo "Manutenção de campos" , onde você poderá editar, inserir ou…](https://ajuda.sankhya.com.br/hc/article_attachments/4414032296983)

| ![Imagem 11: O botão "Manutenção dos Campos" dará acesso ao modo "Manutenção de campos" , onde você poderá editar, inserir ou…](https://ajuda.sankhya.com.br/hc/article_attachments/16276023352599) | É preciso cautela ao remover campos, pois não é possível determinar de forma rápida quais cubos ele é usado. De forma que, a remoção de um campo compromete o funcionamento de todos os cubos que o utilizam. |
| --- | --- |

Existem dois tipos de campos, aqueles comuns, utilizados para montagem do cubo e outros campos que possuem a finalidade apenas de organizá-lo de maneira hierárquica. Os campos usados com esse propósito devem possuir a marcação  **"Só Hierarquia"** habilitada. Assim, ao criar um campo, pode-se configurar em que parte da árvore você quer que este seja exibido, por meio do campo **"Cód. Campo Pai"**.

**Nota:** os campos que não têm valor informado no campo Cód.Campo Pai, aparecem no primeiro nível da árvore e é possível criar quantos níveis forem necessários. 

Os campos **"Cód.Único"** e **"Cód.Campo"** serão gerados automaticamente.

No campo **"Descrição"**, utilize nomes em que você possa facilmente identificá-lo, de forma a evitar ambiguidade.

O campo **"Tipo"**, possui uma lista com os tipos de dados mais comuns em relatórios.

A **"Máscara"** permite determinar como os dados serão apresentados no cubo. Você poderá ainda, definir as máscaras dos campos **"Dinheiro"**, **"Inteiro"** e **"Número"**.

Existem outros três campos responsáveis por determinar como o gerador de relatórios deve obter os dados. Por exemplo, imaginemos que você queira obter o **"Tipo de Movimento"** de uma Nota, nesse caso, observe a seguir a consulta a ser utilizada, e abaixo, a composição desta: 

```
                          SELECT CAB.TIPMOV FROM TGFCAB CAB
```

- **Expressão:** é a parte da consulta que corresponde à coluna na tabela de origem. No exemplo dado acima, este seria CAB.TIPMOV;
- **Tabelas:** trata-se da parte da expressão correspondente ao "FROM" da consulta, ou seja, determina qual tabela contém os dados;
- **Ligação:** Eventualmente, podem haver campos de tabelas distintas, nesses casos, seu conteúdo determina como o relacionamento entre as tabelas será resolvido. O campo citado como exemplo, pertence à tabela TGFCAB e no Módulo Comercial; nesse caso, podemos considerar essa tabela como o coração do módulo, afinal é ela que guarda as informações de **"Compras"**, **"Vendas"**, **"Transferências"**, entre outros. É a partir dessa tabela que os relatórios do módulo Comercial serão gerados, portanto, será por ela que o mecanismo de relatórios começará a montagem da consulta. Dessa forma, os campos mapeados para a ligação, não deverão possuir valor para a ligação. Caso o campo encontrar-se em outra tabela, por exemplo, na TGFITE, o valor seria ITE.NUNOTA = CAB.NUNOTA, de modo que, ao montar a consulta, o **"WHERE"** contivesse a ligação entre a tabela base e a tabela a qual o campo pertence.

---

#### Visualização do Cubo

Durante ou após a configuração do cubo, você poderá visualizá-lo de modo a encontrar a formatação mais adequada conforme sua necessidade. Essa visualização é realizada através do botão ![Imagem 12: Durante ou após a configuração do cubo, você poderá visualizá-lo de modo a encontrar a formatação mais adequada…](https://ajuda.sankhya.com.br/hc/article_attachments/16276309571095) **"Visualizar Cubo"**. Para mais informações sobre essa funcionalidade, acesse o link [Visualizar Cubo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111653-Visualizador-do-Cubo-de-Decis%C3%A3o).

---

#### Controle de Acesso

Além do controle de acesso padrão do sistema, sendo ele aplicável nas operações básicas de todas as telas, também é possível restringir o acesso a cada relatório através do botão ![Imagem 13: Além do controle de acesso padrão do sistema, sendo ele aplicável nas operações básicas de todas as telas, também é…](https://ajuda.sankhya.com.br/guide-media/01H5J56R7E01RVJ609N28M4KJD) **"Segurança"**. Por meio dessa opção, o sistema permitirá ajustar o nível de acesso de cada grupo de usuários, ao relatório selecionado.

Os usuários são anexados ao grupo de forma a obedecer à configuração realizada no [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), ou seja, para que um usuário tenha acesso liberado a um relatório, este deve ser inserido em um grupo de usuários em seu cadastro, realizado na aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao) no Campo **"Grupo"**; feito isso, escolha o grupo onde o usuário foi inserido, e o adicione, liberando os acessos a ele necessários.

| ![Imagem 14: Os usuários são anexados ao grupo de forma a obedecer à configuração realizada no Cadastro de Usuários , ou seja, para…](https://ajuda.sankhya.com.br/hc/article_attachments/16276023352599) | Esse vínculo é exclusivo por cubo, de maneira que um mesmo usuário pode ser vinculado ao, por exemplo, no Grupo **"A"** no relatório **"X"** e ao Grupo **"B"** no relatório **"Y"**. O acesso pode ser dado a todo grupo ou um usuário específico. |
| --- | --- |

**Nota:** para alterar um Cubo de Decisão, você deverá ter ambos acessos de alteração, sendo eles o da tela e o cubo a ser alterado.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110033-Formatador-de-Cubos-de-Decis%C3%A3o#top)
