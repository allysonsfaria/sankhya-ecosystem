---
id: "360044598534"
titulo: "Adiantamento/Empréstimo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598534-Adiantamento-Empr%C3%A9stimo"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:47:42Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Contas", "Despesa", "Parcelamento", "Parceiro", "Receitas", "adiantamento", "Adiantamento/ Empréstimo", "Base de Vencimento", "DIASUTEISADEM", "empréstimo", "Núm.Parcelas", "br.com.sankhya.mge.adiantamento", "Adiantamento/Empréstimo manual", "Movimentação Financeira", "Funcionário", "Preferências", "Financeiro", "Adiantamento/Empréstimo", "Tela de Lançamento", "Configurações de Parcelamento"]
---

# Adiantamento/Empréstimo

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42310680153111) Módulo: Configurações > Rotinas
```

---

Esta opção tem o objetivo de criar um adiantamento/empréstimo para um parceiro/funcionário da empresa. Lembrando que, esta tela não tem integração com o orçamentário, visto que esse adiantamento geralmente não é planejado e ele é feito por um controle diferente.

O Adiantamento/Empréstimo é composto por títulos de despesa, mostrados na grade superior desta tela e por títulos de receitas, visualizados na grade inferior.

![Imagem 2: Esta tela também está presente no Controle de Acessos , e assim como as demais telas, existe a possibilidade de…](https://ajuda.sankhya.com.br/hc/article_attachments/16423713476375) Esta tela também está presente no [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos), e assim como as demais telas, existe a possibilidade de configuração de acesso a ela. No entanto, é uma tela de movimentação e consulta, não uma tela operacional comum, e por isso, para qualquer configuração na tela de acesso, o usuário terá permissão para todas as suas funcionalidades, independente dos acessos que forem configurados.

Acesse os links abaixo para navegar pelo artigo:

| Funcionalidades da tela |
| --- |
| [Lançando um Novo Adiantamento/Empréstimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598534-Adiantamento-Empr%C3%A9stimo#lan%C3%A7andoumnovoadiantamento/empr%C3%A9stimo) |
| [Confirmando um Novo Adiantamento/Empréstimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598534-Adiantamento-Empr%C3%A9stimo#confirmandoumnovoadiantamento/empr%C3%A9stimo) |
| [Selecionando um Adiantamento/Empréstimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598534-Adiantamento-Empr%C3%A9stimo#selecionandoumadiantamento/empr%C3%A9stimo) |
| [Cancelando um Adiantamento/Empréstimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598534-Adiantamento-Empr%C3%A9stimo#cancelandoumadiantamento/empr%C3%A9stimo) |
| [Impressão de Adiantamento/Empréstimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598534-Adiantamento-Empr%C3%A9stimo#impress%C3%A3odeadiamento/empr%C3%A9stimo) |

### Lançando um Novo Adiantamento/Empréstimo

![Imagem 3: Lançando um Novo Adiantamento/Empréstimo](https://ajuda.sankhya.com.br/hc/article_attachments/12983389698583)

O Lançamento de um novo adiantamento/empréstimo é feito através do botão **"Novo"** no cabeçalho desta tela, sendo que, ao ser acionado abrirá o pop-up **"Novo Adiantamento/Empréstimo"**, na qual deverá ser realizado as seguintes configurações.

![Imagem 4: O Lançamento de um novo adiantamento/empréstimo é feito através do botão "Novo" no cabeçalho desta tela, sendo que, ao…](https://ajuda.sankhya.com.br/hc/article_attachments/12983428693527)

O primeiro passo do lançamento de um novo empréstimo será definir a **"Empresa"** para o qual será lançado o título, a **"Data de Negociação"** e **"Data de Vencimento da Despesa"**, bem como o **"Parceiro"** que receberá o adiantamento, além de outros dados que referenciarão o novo título.

PreencheNDO o campo **"Dt. Entrada e Saída"**, ao efetuar um adiantamento ou empréstimo, tem-se que, os títulos que forem gerados neste processo, utilizarão estas informações inseridas neste campo. Caso não seja informada uma data, os títulos gerados não possuirão informação referente à Dt. Entrada e Saída.

Esta tela poderá ou não exibir o campo **"Funcionário"** conforme a configuração do parâmetro **"Parceiro p/empréstimo p/Funcionários - CODPARCFUNCS"**.

![Imagem 5: Esta tela poderá ou não exibir o campo "Funcionário" conforme a configuração do parâmetro "Parceiro p/empréstimo…](https://ajuda.sankhya.com.br/hc/article_attachments/23642203051927)

Isto é, este campo somente estará visível se o campo **"Inteiro"** do parâmetro estiver configurado com o código de um Parceiro. Se o campo Inteiro estiver configurado com valor zero (0) o campo Funcionário não será visualizado no pop-up **"Novo adiantamento/empréstimo"**.

Os Funcionários apresentados na pesquisa da tela Novo adiantamento/empréstimo são filtrados pela Empresa, para o qual está sendo lançado o título.

![Imagem 6: Os Funcionários apresentados na pesquisa da tela Novo adiantamento/empréstimo são filtrados pela Empresa, para o qual…](https://ajuda.sankhya.com.br/hc/article_attachments/23642753397399)

Ao selecionar um funcionário, o sistema preencherá automaticamente o campo Parceiro com o código do Parceiro informado no parâmetro CODPARCFUNCS, e desabilitará tanto este campo quanto a opção **"Usar parceiro e veículo da ordem de carga"**, impossibilitando que seja informado um Parceiro diferente do que foi configurado no parâmetro.

Se o Funcionário não for informado nesta tela, então a escolha do Parceiro será livre.

Outra forma de se definir o Parceiro nesta tela, será através do campo **"Ordem de Carga"**, pois uma vez informado basta marcar a opção Usar parceiro e veículo da ordem de carga, para que o sistema preencha automaticamente os campos Parceiro e **"Veículo"** conforme a Ordem de Carga.

![Imagem 7: Outra forma de se definir o Parceiro nesta tela, será através do campo "Ordem de Carga" , pois uma vez informado basta…](https://ajuda.sankhya.com.br/hc/article_attachments/23642463977879)

Os campos Dt. Neg. Despesa e Dt. Venc. Despesa são influenciados pelo parâmetro **"Dias Úteis para Adiantamento/Empréstimo - DIASUTEISADEM"**.

O valor informado no campo Inteiro será usado para calcular a data de vencimento em relação à data de negociação informada, sendo que os dias úteis serão contados a partir do dia seguinte da data de negociação. Considere o exemplo:

Se o campo Inteiro deste parâmetro estiver registrando valor igual a 3 e a configuração da Dt. Neg. Despesa como 16/08/2010, então a Dt. Venc. Despesa será automaticamente preenchida como 19/08/2010, que corresponde a exatamente 3 dias úteis após a negociação. Como o parâmetro considera apenas os dias úteis, supondo que o dia 17/08/2010 fosse um feriado, então a Dt. Venc. Despesa seria igual a 20/08/2010. Por isto é muito importante que os feriados estejam corretamente configurados no sistema.

Os campos **"Contato"** e **"Imóvel"** apenas serão disponibilizados ao realizar um adiantamento, caso possua a licença do Módulo Imobiliária.

**Observação:** quando estes campos forem informados, serão levados ao financeiro gerado.

O próximo passo será configurar o **"Parcelamento"** do adiantamento/empréstimo.

![Imagem 8: O próximo passo será configurar o "Parcelamento" do adiantamento/empréstimo.](https://ajuda.sankhya.com.br/hc/article_attachments/23642463990167)

Informe o **"Valor"** do adiantamento/empréstimo, ou seja, o valor que a empresa irá repassar ao parceiro. Logo, será gerado para a empresa um título de despesa no valor informado neste campo. Em **"Núm.Parcelas"** indique o número de parcelas que o adiantamento/empréstimo será pago a empresa.

Na opção **"Frequência"** insira a frequência de vencimento das parcelas, que poderão ser: **"Diárias"**, **"Semanais"**, **"Quinzenais"**, **"Mensais"**, etc. É possível também configurar a frequência de vencimento de forma **"Personalizada"**, na qual será informado a quantidade de dias manualmente.

Na **"Base de Vencimento"** defina a data na qual vencerá a primeira parcela de Receita, uma vez que a data de vencimento da despesa foi configurada no passo anterior.

A Base de Vencimento da receita poderá ser igual ao **"Vencimento da Despesa"** ou com base na data de **"Negociação"**, que poderá ser consoante o dia do lançamento, isto é, **"Hoje"** ou ainda **"Informado pelo Usuário"**. Quando Informado pelo Usuário, o sistema habilitará o calendário ao lado do campo, para digitação.

A **"Tx. de juros (%)"** é mensal, logo, se for indicado uma frequência que não seja mensal, o sistema fará automaticamente a correção, conforme a frequência definida.

Em **"Tipo de parcelamento"** indique se o parcelamento será por:

- Juros simples;
- Juros compostos;
- Juros compostos (fixas);
- Duplicação (fixas);
- Amortização Constante.

Em **"Tipo de Juros"**, informe onde e como será gravado o juro no título financeiro. Nesta seção, existem as marcações:

- Cobrar juro de todo período (embutido);
- Se atrasar cobrar os juros como multa;
- Cobrar juro de todo o período (negociado);
- Calcular apenas se atrasar.

A opção **"Calcular apenas se atrasar"** só poderá ser utilizada quando o Tipo de Parcelamento for igual a **"Duplicação (fixa)"**.

![Imagem 9: A opção "Calcular apenas se atrasar" só poderá ser utilizada quando o Tipo de Parcelamento for igual a "Duplicação…](https://ajuda.sankhya.com.br/hc/article_attachments/23642464006167)

O último passo do lançamento será a configuração das **"Preferências"**, ou seja, a configuração das informações necessárias para o lançamento de títulos como:

- As TOP’s que serão utilizadas nos títulos de Despesa e Receitas;
- O **"Tipo de Título"** que está sendo gerado no lançamento deste adiantamento/empréstimo;
- Informações gerenciais como o **"Projeto"**, a **"Natureza"** e o **"Centro de Resultado"**;
- E a **"Conta Bancária"**.

Ao gerar os títulos, o sistema utilizará a **"Natureza (Receita)"** para os títulos de receita e a **"Natureza (Despesa)"** para os títulos de despesa gerados, sendo que, na pesquisa da natureza de receita, o sistema trará apenas as naturezas marcadas como **"Ambos"** ou **"Receita"** e, na pesquisa da natureza de despesa, somente as naturezas marcadas como Ambos ou **"Despesa"**.

Ao clicar em **"Concluir"** o sistema apresentará na grade superior da tela o título de Despesa referente ao adiantamento/empréstimo cedido ao parceiro e na grade inferior os títulos de Receitas gerados pelo parcelamento do título de despesa.

![Imagem 10: Ao clicar em "Concluir" o sistema apresentará na grade superior da tela o título de Despesa referente ao…](https://ajuda.sankhya.com.br/hc/article_attachments/23642589032727)

No exemplo da imagem anterior, foi adiantado ao parceiro de código 1 a quantia de R$ 15.000,00 que será restituída à empresa de código 7 em doze parcelas de R$ 1.250,00.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598534-Adiantamento-Empr%C3%A9stimo#top)

### Confirmando um Novo Adiantamento/Empréstimo

Ao Concluir o lançamento de um adiantamento/empréstimo o sistema exibe na tela os dados do novo título e os cálculos que irão constituí-lo, contudo, o lançamento só será efetivado após a confirmação realizada através do botão **"Confirmar"**.

Feito isto, o botão Confirmar ficará desabilitado. O número do **"Adiant./Emp"** será gerado. O **"Nro. Nota"** e **"Nro.Único"** de Despesa e das Receitas, também serão gerados, permitindo a identificação e movimentação dos títulos no Financeiro.

![Imagem 11: Feito isto, o botão Confirmar ficará desabilitado. O número do "Adiant./Emp" será gerado. O "Nro. Nota" e "Nro.Único"…](https://ajuda.sankhya.com.br/hc/article_attachments/23642589063959)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598534-Adiantamento-Empr%C3%A9stimo#top)

### Selecionando um Adiantamento/Empréstimo

Para visualizar os adiantamentos/empréstimos lançados, basta utilizar o botão de **"Buscar"**, e através das opções de filtros selecionar os títulos desejados.

O número da duplicata referente ao título selecionado na busca será apresentado no campo Adiant./Emp., no cabeçalho da tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598534-Adiantamento-Empr%C3%A9stimo#top)

### Cancelando um Adiantamento/Empréstimo

Para limpar a tela basta clicar no botão **"Cancelar"**, lembrando que este botão não fará nenhum cancelamento de adiantamento, apenas limpará a tela.

Um adiantamento/empréstimo confirmado só poderá ser removido pelo botão **"Desfazer"**. Destaca-se ainda que antes de desfazer a ação, o sistema exibirá uma mensagem com a opção de desfazer o adiantamento.

Contudo, o lançamento só poderá ser desfeito se não tiver ocorrido baixa de nenhum dos títulos de despesa ou receita, ou ainda, se nenhum deles tiver sido renegociado. Caso contrário, não será possível desfazer o adiantamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598534-Adiantamento-Empr%C3%A9stimo#top)

### Impressão de Adiantamento/Empréstimo

Somente Adiantamento/Empréstimos confirmados poderão ser impressos.

Para realizar a impressão de um adiantamento/empréstimo é necessário em primeiro plano configurar o **"Modelo e Impressora"** através do botão **"Outras Opções..."** no cabeçalho da tela.

![Imagem 12: Para realizar a impressão de um adiantamento/empréstimo é necessário em primeiro plano configurar o "Modelo e…](https://ajuda.sankhya.com.br/hc/article_attachments/23642589073687)

No pop-up de configuração, informe o nome da **"Impressora"** que será usada e o **"Modelo"** para impressão do adiantamento/empréstimo, lembrando que o modelo deve ter sido pré-cadastrado em [Modelos de Nota Fiscal/Duplicatas/Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913).

É importante definir o **"Tipo de Impressora"**, pois este indicará ao sistema o conjunto de caracteres de controle da impressora.

Se a opção **"Impressão automática"** estiver marcada, no ato da confirmação de um novo lançamento de adiantamento/empréstimo o título será automaticamente impresso.

Para imprimir um título já confirmado, selecione o título desejado e acesse a opção **"Imprimir título de despesa"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598534-Adiantamento-Empr%C3%A9stimo#top)
