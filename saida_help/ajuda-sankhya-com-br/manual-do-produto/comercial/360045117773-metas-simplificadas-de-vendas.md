---
id: "360045117773"
titulo: "Metas Simplificadas de Vendas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117773-Metas-Simplificadas-de-Vendas"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:32:57Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Metas", "Vendedor", "TOP", "Vendas", "Natureza", "Resultado", "Metas Simplificadas de Vendas", "RESTRINGEVLRMET", "br.com.sankhya.com.mov.metsimpvendas", "Metas Simplificadas de Vendas manual", "Configuração de Filtros", "Grade Principal", "Assistente de Lançamento", "Comercial"]
---

# Metas Simplificadas de Vendas

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312142641815) Módulo: Comercial > Avançado 
```

---

![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/360083251054)

Quando você acessa essa tela pela primeira vez, o sistema automaticamente lança as configurações de metas simplificadas na tabela. Essas configurações são gravadas na tabela TGMCFG, com um código arbitrário, com as seguintes descrições:

- Meta Simplificada para Vendedores;
- Meta Simplificada para Grupos de Produtos;
- Meta Simplificada para Produtos;

Essas configurações recebem os valores **"V"**, **"G"**, e **"P"** para o campo **"Simplificada"**, identificando o tipo de configuração de meta simplificada. Quando a tela é acessada novamente, busca-se apenas as configurações já cadastradas.

Uma vez que as metas já estão configuradas, você poderá definir metas por períodos mensais. Estas metas podem ser estabelecidas para Vendedor, Grupo de Produto ou Produto. Além de lançar metas, você poderá também configurar para quais TOP's o sistema considerará na atualização do realizado.

Esta tela é subdividida nos seguintes pontos:

- Painel lateral de filtros;
- Painel superior de metas mensais;
- Barra de botões;
- Grade principal;
- Rodapé.

O Painel Lateral de Filtros é dividido em 3 seções, **"Vendedor"**, **"Grupo de Produto"** e **"Produto"**, ou seja, uma para cada tipo de meta simplificada. Selecionando a seção desejada no Painel de Filtros, automaticamente indique, para qual tipo de Meta está sendo lançado as Metas Simplificadas. Cada seção contém um controle de filtro personalizado e filtros rápidos adequados para cada tipo de meta. As seções Grupo de Produto e Produto permitem ainda configurar se a meta será lançada em termos de "**Quantidade"**, **"Peso"**, **ou "Valor"**, através do botão **"Nível"**.

No painel **"Produto"**, no campo **"Apresentar por"** indique se o tipo de apresentação será por **"Código"** ou por **"Referência"**. Se você solicitar que a apresentação seja por **"Referência"**, a coluna Código será alterada automaticamente para Referência e ao invés do sistema exibir os produtos por código, passará a apresentar por suas respectivas referências. Tanto a coluna Código/Referência e a coluna Descrição podem ser ordenadas.

Ainda no painel Produto, teremos além dos recursos de filtros rápidos, a opção de se exibir o complemento do produto de modo a se obter maior agilidade na consulta e visualização dos itens.

![Imagem 3: Ainda no painel Produto , teremos além dos recursos de filtros rápidos, a opção de se exibir o complemento do produto…](https://ajuda.sankhya.com.br/hc/article_attachments/360083252174)

Filtros rápidos:

- Produto;
- Fornecedor;
- Marca.

Opção:

- Exibir complemento;

O filtro Fornecedor tem o funcionamento semelhante aos demais, é um campo de pesquisa na qual será selecionado o fornecedor do produto antes de efetuar a busca.

Os filtros Marca e Complemento são campos para entrada de texto, em que você informará a marca ou o complemento a ser pesquisado, podendo ser as primeiras letras ou a descrição completa.

O sistema permite a escolha da apresentação ou não do complemento do produto. Se a opção "**Exibir o complemento"** estiver marcada, será exibida a descrição do produto acompanhada do complemento do produto, na mesma linha mas separado por colchetes. Se não existir complemento cadastrado para o produto o sistema exibe apenas a descrição.

Os filtros configurados são memorizados, ou seja, ao acessar novamente a tela, os filtros realizados são mantidos.

No Painel Superior de Metas Mensais, são lançados os totais das metas estipuladas para cada mês do ano. O sistema permite lançar metas apenas para o mês atual ou para meses posteriores. Sendo assim, entradas de meses anteriores vêm desabilitadas. Os lançamentos podem ser feitos manualmente ou através do assistente (botão "**Estipular metas mensais pelo assistente"**), que será explicado no próximo tópico.

![Imagem 4: No Painel Superior de Metas Mensais , são lançados os totais das metas estipuladas para cada mês do ano. O sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/360084418933)

A barra de botões apresenta diversos controles que permitem a manipulação dos dados. Essa barra exibe:

**Seletor de ano:** Através desse controle selecionamos o ano para o qual as metas mensais serão lançadas. Somente podem ser lançadas metas para o ano atual ou anos posteriores. No entanto, anos anteriores podem ser consultados.

**Confirmar:** Grava no banco de dados as metas digitadas para o Vendedor, Grupo de Produto ou Produto.

**Cancelar:** Descarta as digitações realizadas e recarrega os dados da grade.

**Distribuir:** Para cada linha da grade e para cada mês, ele aplica o percentual informado na coluna % sobre o total informado no painel, para aquele mês, e então, guarda o resultado na coluna valor.

**Distribuir igualmente:** Distribui a meta informada no painel superior em partes iguais entre as linhas da grade;

**Configurar TOP's:** Abre o pop-up para configuração de TOP's.

![Imagem 5: Configurar TOP's: Abre o pop-up para configuração de TOP's .](https://ajuda.sankhya.com.br/hc/article_attachments/360084419153)

Essa configuração indica ao sistema para qual ou quais TOP's serão atualizados o realizado das metas simplificadas. Ou seja, no momento de atualizar o realizado das metas simplificadas, o sistema irá totalizar apenas notas/financeiros que foram lançados com alguma das TOP's configuradas nessa tela.

As TOP's informadas neste botão, refletem nas três metas (vendedor, grupo de produtos e produtos). Sendo assim, a tabela de TOP's das metas é atualizada de modo a manter as configurações das três metas idênticas.

Nesta opção, você poderá indicar uma única TOP ou várias. Todas as vezes que uma destas TOP's for utilizada dentro do mês de referência, a meta ou as metas (quando configurado mais de uma meta) serão atualizadas.

**Observação:** no campo **"Receita/Despesa"**, temos a opção de escolher se a operação atualizará **"Receitas"**, **"Despesas"** ou se usará as atualizações da TOP (**"Usar da TOP"**) nas metas que utilizam aquela TOP.

Ao selecionar a opção Usar da TOP, o sistema verificará no cadastro de [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) , aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), as marcações para **"Atualização de Estoque"** e **"Atualização de Estoque de MP"** e, conforme a marcação, fará o seguinte:

- TOP de Venda e Pedido de Venda - Campo **"Baixa"** marcado:  O sistema atualizará Receita.
- TOP de Compra e Pedido Compra - Campo **"Entrada"** marcado: O sistema atualizará Despesa.
- TOP Devolução de Compra - Campo **"Baixa"** marcado:  O sistema atualizará Receita.
- TOP Devolução de Venda - Campo **"Entrada"** marcado: O sistema atualizará Despesa.

![Metsim9](https://ajuda.sankhya.com.br/hc/article_attachments/360061018794)

A barra de botões apresenta também um link que da acesso ao **"Assistente de lançamento de metas"**. Ao clicar no assistente o sistema abre uma tela que permite definir as metas mensais para todo ano.

![Imagem 7: A barra de botões apresenta também um link que da acesso ao "Assistente de lançamento de metas" . Ao clicar no…](https://ajuda.sankhya.com.br/hc/article_attachments/360083252394)

Esta tela solicita que sejam preenchidas as seguintes informações:

- O primeiro mês para o qual serão lançadas as metas;
- O valor da meta do primeiro mês;

Se a meta será ou não aumentada, teremos as seguintes opções:

- Não aumentar;
- Valor (R$);
- Porcentagem (%);
- Valor do acréscimo;
- Distribuição que deve ser aplicada ao confirmar;

A opção de não aplicar acréscimo aplica o mesmo valor para todos os meses subsequentes (até dezembro do ano corrente). A opção acréscimo por valor soma o valor informado ao mês anterior. Por exemplo:

Para valor inicial de R$ 1.000,00 e acréscimo de R$ 500,00 teríamos a sequencia R$ 1.000,00, R$ 1.500,00, R$ 2.000,00 etc. Já a opção acréscimo por percentual aplica o valor informado como um percentual sobre o mês anterior. Exemplo: valor inicial = R$ 1.000,00 e acréscimo = 5%. Teríamos a sequencia R$ 1.000,00, R$ 1.050,00, R$ 1.102,50 etc.

O sistema valida a escolha do primeiro mês. Somente podem ser definidas metas para o mês atual ou para meses posteriores.

Nesta tela, você poderá realizar a distribuição das metas ao informar o valor destas na parte superior, na qual, encontram-se os meses. Em seguida acione o botão **"Distribuir"**; se forem alterados os valores na grade, o sistema ajusta o valor da parte superior do menu.

Assim será definido como as metas serão distribuídas entre os vendedores, grupos de produto ou produto. As opões **"Distribuir considerando os percentuais já existentes"** e **"Distribuir igualitariamente"**, fazem praticamente a mesma função. A diferença é que ao selecionar para distribuir igualitariamente o sistema divide a porcentagem total das metas em partes iguais para cada vendedor (com exceção do caso em que a divisão não é exata, com relação à porcentagem).

Exemplo:

- Você informa que a meta para o mês de Abril/2015 é de 10.000,00. E existem 5 vendedores na grade. Pra cada vendedor, informe o percentual sobre a meta, por exemplo, 15, 25, 30, 10, e 20. Se colocar em distribuir, o sistema aplica respectivamente R$ 1.500,00, R$ 2.500,00, R$ 3.000,00, R$ 10.000,00 e R$ 20.000,00 para cada um deles.
- Ao abrir a tela do Assistente, lançar 12.000 para o mês de Abril, e selecionar Distribuir considerando os percentuais já existentes, será aplicado o valor da meta usando as porcentagens utilizadas anteriormente, então fica 1.800,00, 3.000,00, 4.000,00, 1.200,00 e 2.400,00.

Porém, se ele escolhe Distribuir igualitariamente, então o sistema divide 100% pelo número de vendedores e aplica para cada um. Assim cada vendedor fica com 20% de meta a cumprir, totalizando 2.400,00 para cada um.

A Grade Principal traz o resultado da aplicação dos filtros de acordo com o tipo de Meta escolhida.

![Imagem 8: A Grade Principal traz o resultado da aplicação dos filtros de acordo com o tipo de Meta escolhida.](https://ajuda.sankhya.com.br/hc/article_attachments/360083252434)

Por exemplo, se o você escolheu Vendedor, então a grade traz o Código e o Apelido do Vendedor, nas colunas Código e Descrição, respectivamente.

Para mês do ano a grade traz um par de colunas % e Valor, agrupadas pelo nome do mês.

**Nota:** as colunas Código e Descrição não podem ser editadas. Também não podem ser editadas colunas de meses anteriores ao mês atual.

Para cada mês, você poderá informar a meta específica para aquele Vendedor (ou Grupo, ou Produto). Ele pode informar a meta tanto em % (porcentagem) quanto em Valor, de forma que o sistema ajusta a coluna correspondente imediatamente. Por exemplo: 

Você definiu uma meta global para Janeiro de R$ 10.000,00. Para o vendedor 1 - João ele digita o valor 15,00 na coluna %. Automaticamente o sistema calcula 1.500,00 para a coluna valor. Porém, o usuário muda de ideia e digita 2.500,00 na coluna Valor. O sistema deve automaticamente calcular 25,00 para a coluna %.

![Imagem 9: Você definiu uma meta global para Janeiro de R$ 10.000,00. Para o vendedor 1 - João ele digita o valor 15,00 na coluna…](https://ajuda.sankhya.com.br/hc/article_attachments/360084419553)

O Rodapé exibe os totais de metas para cada mês, tanto em porcentagem quanto em valor. Caso o total de metas daquele mês não atinja 100%, a coluna daquele mês é apresentada em Vermelho. Ao ajustar para 100% a coluna é exibida na cor padrão (Preto). Ao clicar em **"Distribuir"**, **"Distribuir Igualmente"** ou **"Confirmar"** o sistema valida a grade, de forma que a soma das porcentagens não ultrapasse 100%.
