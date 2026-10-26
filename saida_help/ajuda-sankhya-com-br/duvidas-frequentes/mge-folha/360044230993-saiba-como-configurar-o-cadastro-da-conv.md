---
id: "360044230993"
titulo: "Saiba como configurar o cadastro da Convenção Coletiva, Acordo Coletivo ou Sentença Normativa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044230993-Saiba-como-configurar-o-cadastro-da-Conven%C3%A7%C3%A3o-Coletiva-Acordo-Coletivo-ou-Senten%C3%A7a-Normativa"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:33:00Z"
rotulos: ["Configuração", "Folha de Pagamento", "Reajuste Salarial", "Reajuste Proporcional Ocorrência Data Base", "Cadastro Sindicatos Convenção Acordo", "Reajuste Salarial Percentual Arredondamento", "Convenção Coletiva", "Sindicatos"]
---

# Saiba como configurar o cadastro da Convenção Coletiva, Acordo Coletivo ou Sentença Normativa

![Imagem 1: Para esta configuração siga as orientações abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16199495890839)Para esta configuração siga as orientações abaixo:

![Imagem 2: Acesse MGEPessoal » Arquivos » Cadastros » Sindicatos .](https://ajuda.sankhya.com.br/hc/article_attachments/16199502070423) Acesse MGEPessoal  » Arquivos » Cadastros » Sindicatos.

É indispensável que seja preenchido os campos do quadro **"Convenção Coletiva, Acordo Coletivo ou Sentença Normativa"**, antes do efetivo ajuste.

![Imagem 3: É indispensável que seja preenchido os campos do quadro "Convenção Coletiva, Acordo Coletivo ou Sentença Normativa" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/14472533178903)

![Imagem 4: Acesse MGEPessoal » Rotinas » Reajuste Salarial](https://ajuda.sankhya.com.br/hc/article_attachments/16199495898007) Acesse MGEPessoal » Rotinas » Reajuste Salarial

Este menu possibilita fazer um reajuste de salário em percentual, com condições de arredondamento e seleção.

O campo **“Salário Mínimo da Classe”** deverá ser preenchido com um valor, que será o mínimo que o sistema aceitará como salário. Por exemplo, se for dado ao funcionário um reajuste de 10% e o valor informado como salário mínimo da classe for R$ 200,00, se o percentual de reajuste dado não alcançar o mínimo e se o salário de algum funcionário ficar inferior a este valor, o sistema automaticamente reajustará o salário para R$ 200,00.

Logo, se:
• Salário = R$ 100,00
• Reajuste de 10%
• Salário Mínimo da Classe = R$ 200,00.

O salário será reajustado para R$ 200,00 e não para R$ 110,00.

Nesta tela:
- Preencha a informação no campo **“Tipo de Arredondamento”**. Se for arredondar, preencha também o campo **“Fator de Arredondamento”** logo abaixo.

- Informe o **“Percentual de Reajuste”**.

Para que sejam aplicados percentuais diferenciados em relação à Data de Admissão e o Período que abrange a Data Base da categoria, marque também a opção **“Reajuste Sindical”**, além da opção **“Reajuste Sindical Proporcional ao Tempo de Serviço”** existente no Menu » Avançado » Regras para Cálculo.

- Informe o valor do **“Salário Mínimo da Categoria”**, conforme explicação acima.

- Marque a opção **“Atualiza Registro de Ocorrência”**.

- Descreva o motivo do Reajuste Salarial no campo **“Descrição Para o Registro de Ocorrência”**.
- Clique no botão **“OK”** para confirmar.

![Imagem 5: Se desejar alterar o Salário de alguns funcionários após o reajuste coletivo, entre no Cadastro do Funcionário, aba…](https://ajuda.sankhya.com.br/hc/article_attachments/16199502073879) Se desejar alterar o Salário de alguns funcionários após o reajuste coletivo, entre no Cadastro do Funcionário, aba **Contrato**, altere o valor do campo **“Salário Base”**, e informe a **“Ocorrência”**.

**![Imagem 6: Cálculo de Reajuste Sindical Proporcional ao tempo de serviço](https://ajuda.sankhya.com.br/hc/article_attachments/16199502078487) Cálculo de Reajuste Sindical Proporcional ao tempo de serviço**

O reajuste proporcional será gerado automaticamente, sem que seja necessária a execução de Filtros ou atualizações manuais para os admitidos após a data Base.

A opção Reajuste Sindical Proporcional ao Tempo de Serviço na tela Menu » Avançado » Regras para Cálculo, quando marcada faz com que o sistema passe a levar em consideração os meses entre a Data de Admissão e a Data Base aplicando assim um percentual proporcional.

Para que essa proporcionalidade seja aplicada é necessário que a opção Reajuste Sindical, localizada nesta tela do lado do campo Percentual de Reajuste, esteja marcada.

Para que seja possível a consulta dos Percentuais que foram aplicados para os funcionários; existe uma View (Recurso do banco de dados) e SELECT que buscam o valor do evento ‘9999’ da tabela TFPACU (Lançamentos » Acumulados do Ano) comparando o valor em cada mês, e naqueles meses que ocorreram diferenças o percentual é apurado.

Em algumas situações a Empresa antecipa, com base em uma estimativa, o Percentual de Reajuste da Convenção Coletiva ou Acordo Coletivo, nessas situações o funcionário poderá ter direito ou não a um novo Reajuste. Para que isso aconteça é necessário inserir o código do Histórico de Ocorrência (Menu » Lançamentos » Histórico do Funcionário » Histórico de Ocorrência) no parâmetro "**FPREAJANTECIPA’ - Código Histórico de Ocorrência para antecipação de Reajuste Sindical"**.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16199495901975) OBSERVAÇÃO:**

Para aplicação correta da diferença entre o percentual de antecipado e o real, a referência que essa antecipação foi realizada precisa estar fechada, do contrário os Acumulados do Ano (Lançamentos » Acumulados do Ano) não serão alimentados e o sistema não terá o valor correto.

(1)** EXEMPLO¹:** 

Quando tiver um funcionário com o Histórico de antecipação nas ocorrências (Lançamento » Histórico do Funcionário » Registro de Ocorrência), o sistema irá apurar o percentual que foi aplicado no mês em que o Histórico do Parâmetro estiver no Registro de Ocorrências e compará-lo com o percentual que foi concedido na própria tela de Reajuste Salarial.

Se o percentual concedido for menor, no momento em que a opção Rotina » Reajuste Salarial estiver sendo executado, o percentual a ser aplicado será o resultado da diferença entre o que foi Adiantado e o que estiver no campo Percentual de Reajuste. Ou seja, o funcionário recebeu uma antecipação de 5%, quando chegou a data base o reajuste ficou em 10%, nesse caso o funcionário receberia mais 5% de reajuste. Em um segundo exemplo, mas levando em consideração que a concessão foi de 10%, temos um funcionário que recebeu a antecipação de 10%, nesse caso esse funcionário não teria a aplicação de reajuste, já que todo o percentual foi realizado na antecipação.

O Reajuste Proporcional quando configurado, somente será realizado para aqueles funcionários que foram admitidos entre a Data Base da Convenção Atual e 12 meses anteriores. Importante, o campo **"Data Base"** da tela Arquivos » Cadastros » Sindicatos deverá ser preenchido antes da execução da Rotina de Reajuste Salarial, isso porque se a convenção atual não for inserida, os admitidos selecionados ficarão incorretos.

(1)** EXEMPLO²:** 

Convenção atual com data 01/09/2013, nesse caso os admitidos que serão usados são os que estiverem com Data de Admissão de 01/09/2012 até 31/08/2013.

O Reajuste Proporcional consiste em dividir por 12 o Percentual informado pelo usuário na tela de Reajuste Salarial, em seguida, multiplicar pela quantidade de Meses na Empresa, ou seja, (% Informado / 12) \* Quantidade de Meses na Empresa.

(1)** EXEMPLO³:**

Funcionário com data de admissão 01/05/13, o Reajuste Proporcional consiste em contar dessa data até 01/09/2013, nesse seriam 4 meses. Então, se o percentual fosse de 10%, teríamos (10 / 12) \* 4 = 3,3333, esse resultado seria aplicado sobre o salário atual.

As frações superiores há 15 dias são consideradas como sendo validas para o Reajuste, exemplo, se a Data Base for 01/09/2012 e o percentual foi de 5%, para os Admitidos até 15/09/2012 a aplicação dos 5% seria válida. Aproveitando essa mesma data se a admissão fosse 18/09/2012 o percentual aplicado seria de 4,58. Esse percentual de 4,58 foi resultado da operação (5/12) \* 11, sendo 05 o percentual integral, 12 os meses do Ano e 11 os meses de Empresa até a data da próxima convenção.

Essa proporcionalização não se aplica para aqueles funcionários que possuem mais de 12 meses, ou seja, a aplicação do Percentual será integral.
