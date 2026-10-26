---
id: "360045108593"
titulo: "Padrões de Classificação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108593-Padr%C3%B5es-de-Classifica%C3%A7%C3%A3o"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:55:00Z"
rotulos: ["Produtos", "manual", "Configuração", "Padrão de Classificação", "br.com.sankhya.arm.cad.padraoclassificacao", "Padrões de Classificação manual", "Controle de Qualidade", "Parâmetros", "Padrões de Classificação no Controle de Qualidade", "Qualidade"]
---

# Padrões de Classificação

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310884413591) Módulo: Configurações > Cadastros
```

---

O padrão de classificação é a representação sistêmica do ensaio (análise) ao qual o produto deve ser submetido durante o processo de controle de qualidade. Ao padrão de classificação são relacionadas as características analisáveis que devem ser consideradas no ensaio, bem como o intervalo de aceitação de cada uma delas para o produto.

![Imagem 2: O padrão de classificação é a representação sistêmica do ensaio (análise) ao qual o produto deve ser submetido durante…](https://ajuda.sankhya.com.br/hc/article_attachments/9927195027223)

O campo **"Código"** pode ser alimentado de forma manual ou automática; esta definição é feitar pelo botão ![Imagem 3: O campo "Código" pode ser alimentado de forma manual ou automática; esta definição é feitar pelo botão "Configuração da…](https://ajuda.sankhya.com.br/hc/article_attachments/16694714948375) **"Configuração da tela"**. Neste campo é informada a numeração de identificação do Padrão de Classificação.

Através do campo **"Descrição"** aponta-se um detalhamento do padrão. As informações deste campo serão levadas para o laudo de análise quando os valores do laudo se enquadrarem nos valores do padrão.

## Aba Geral

Na opção **"Ativo"** indica-se se o padrão de classificação está ativo ou não.

Através do campo **"Grupo de produtos"** seleciona-se o grupo de produtos dos produtos que serão classificados. Se o parâmetro **"Usa produto no padrão de classificação da produção -USAPRODPADCLASS"** estiver habilitado trará como campo "Produto" e neste deverá ser informado o produto que contém cadastrado o Padrão de Classificação.

Por meio do campo **"Classificação"** define-se a ordem de qualidade dos padrões de classificação. Exemplo: Tem-se os padrões Tipo 1, Tipo 2 e Tipo 3. O milho do tipo 1 é de melhor qualidade, então, informa-se 1 no campo classificação. Em seguida informa-se 2 e 3 na classificação dos outros tipos, sendo o de melhor qualidade primeiro.

No campo **"Observação"** são inseridas as informações adicionais sobre o padrão.

A informação apontada no campo **"Fórmula"** é usada para calcular os descontos por fórmula. No construtor de expressão, botão **"Banco de Dados"**, aparecem as tabelas TGACLC (Características), TGFCLT (Padrões de Classificações), TGACLI (Características por Padrão) e no botão **"Variável"** existe a variável RESULTADO.

No campo **"Tipo de Laudo"** são apresentas as opções **"Interno"** e **"Externo"**. Este campo é utilizado na Rotina de Laudo Matéria-Prima (esta tela não foi implementada ainda no Sankhya Om). Se tiver marcado como Externo apresentará nesta rotina a possibilidade de informar o Parceiro, pois significa que o Laudo foi emitido pelo Fornecedor. Se tiver marcado como Interno é porque a empresa que emitirá o próprio Laudo.

As marcações **"Exige Liberação"** e **"Permite confirmar quando laudo for rejeitado"** são empregados pelo Tipo de Operação - TOP para validação de laudos no lançamento de notas. A validação de Laudo ainda não foi implementada no Sankhya Om.

O campo **"Calcular o Prazo de validade a partir da"** disponibiliza as opções **"Data de Fabricação"** e **"Data do Laudo"**. Este campo é utilizado na rotina de [Controle de Laudo de Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611114).

No campo **"Prazo de validade"** deve-se informar a quantidade de dias que deverá ser considerada, juntamente com a opção de Calcular o Prazo de validade a partir da que irá compor os dados na rotina de **"Controle de Laudo de Análises"**.

## Aba Características Classificação

![Imagem 4: Aba Características Classificação](https://ajuda.sankhya.com.br/hc/article_attachments/10481654636951)

Por meio do campo **"Característica"** será executado a pesquisa da característica analisável. Esta característica deve ser cadastrada previamente no [Cadastro de Características Analisáveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600194).

O Valor máximo e o mínimo para que o produto se encaixe no padrão, será apontado no campo **"Mínimo"** e **"Máximo"** respectivamente.

Através do campo **"Desconto"** é especificado o percentual de desconto que será aplicado sobre o produto para reduzir o peso depois de limpo e seco, retirando as impurezas, carunchos, etc.

No campo **"Fórmula Desconto"** será indicada a fórmula para cálculo do percentual de desconto. A fórmula é prioridade no lançamento do desconto no laudo de análise. Caso não se apresenta a fórmula, o sistema irá analisar o valor informado no campo **"Desconto"**. Pode-se usar um construtor de expressões, clicando no botão **"f(x) Construtor"**.

A opção **"Obrigatório"** define se característica analisável é obrigatória ou não para o laudo.

No campo **"Observação"** são inseridas informações adicionais sobre a característica analisável.

As marcações **"Usa Intervalos"** e **"Usa Índices"** quando ativadas, indicam que o [Laudo de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595074-Laudo-de-Classifica%C3%A7%C3%A3o) utilizará as faixas de classificação e seus respectivos descontos cadastrados na sub-aba **"Intervalo"** como parâmetro para apuração da qualidade dos produtos. Dessa forma, observe abaixo como estes cadastros impactam no cálculo do Laudo:

- Quando a marcação Usa Intervalos estiver habilitada, o cálculo do valor a **"Descontar"** do Laudo levará em consideração o valor informado no campo **"% Descontar"** da sub-aba Intervalo, aba Características Classificação.
- Com a marcação Usa Índices ativada, o cálculo do valor a Descontar do Laudo será feito por meio da fórmula **Descontar = (Resultado - Vlr. Base p/ Cálculo por Índices) \* Índice**, sendo que, o resultado não poderá ser negativo.
- Caso ambas as marcações estejam desativadas, o campo Descontar do Laudo irá apresentar o valor **"0,00''**.

O campo **"Vlr. Base p/ Cálculo por Índices"** será habilitado para o preenchimento do valor que será usado como base para apuração do desconto, quando a marcação Usa Índices estiver ativada.

**Nota:** o campo Usa Intervalos e a sub-aba Intervalo são recursos utilizados apenas no módulo Armazéns Gerais.

**Sub-aba Intervalo**

Referente aos campos pertinentes à sub-aba, teremos:

O campo **"Código Intervalo"** será alimentado automaticamente ao inserir um novo registro de intervalo.

Em **"Mínimo"** você informará o valor mínimo aceitável para a faixa de classificação do respectivo intervalo.

No campo **"Máximo"**, informe o valor máximo aceitável para a faixa de classificação do respectivo intervalo.

Insira em **"% Descontar"** a porcentagem de desconto a ser aplicado no laudo considerando a respectiva faixa de classificação da característica. Este campo será bloqueado para edição quando a marcação Usa Índices estiver ativada.

No campo **"Exige Liberação"** indique se uma liberação será necessária caso o resultado de classificação do laudo esteja dentro dessa faixa.

O campo **"Índice"** será considerado na apuração do desconto realizado no Laudo de Classificação quando a marcação Usa Índices estiver ativada. O cálculo do valor a Descontar será efetuado conforme a seguinte fórmula:

```
![Imagem 5: O campo "Índice" será considerado na apuração do desconto realizado no Laudo de Classificação quando a marcação Usa…](https://ajuda.sankhya.com.br/hc/article_attachments/42310884414487) Descontar = (Resultado - Vlr. Base p/ Cálculo por Índices) * Índice
```

Onde:

**"Descontar"** = Valor final calculado pela fórmula. 

**"Resultado"** = Valor apontado no Laudo de Classificação para cada característica. 

**"Vlr. Base p/ Cálculo por Índices"** = Valor informado no mesmo padrão classificação do laudo para a respectiva característica.

**"Índice"** = Valor cadastrado para o intervalo em que o Resultado informado no laudo se enquadra.

Ao acionar o botão ![Imagem 6: Ao acionar o botão "Duplicar" , as informações contidas na aba Características Classificação também serão duplicadas…](https://ajuda.sankhya.com.br/hc/article_attachments/16694928464535) **"Duplicar"**, as informações contidas na aba Características Classificação também serão duplicadas para o novo registro, caso no pop-up que é apresentado, a caixa de seleção esteja marcada:

![Imagem 7: Ao acionar o botão "Duplicar" , as informações contidas na aba Características Classificação também serão duplicadas…](https://ajuda.sankhya.com.br/hc/article_attachments/10843443438743)

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108593-Padr%C3%B5es-de-Classifica%C3%A7%C3%A3o#top)
