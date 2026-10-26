---
id: "360045110713"
titulo: "Adiantamento/Empréstimo c/ repasse ao Fornecedor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110713-Adiantamento-Empr%C3%A9stimo-c-repasse-ao-Fornecedor"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:57:07Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Impressão", "Despesa", "Parcelamento", "Parceiro", "Receitas", "adiantamento", "Base de Vencimento", "DIASUTEISADEM", "empréstimo", "Núm.Parcelas", "Movimentação Financeira", "Fornecedor", "Adiantamento/Empréstimo c/ repasse ao Fornecedor", "Repasse", "br.com.sankhya.mge.adiantamento.fornecedor", "Adiantamento/Empréstimo c/ repasse ao Fornecedor manual", "Financeiro", "Adiantamento/Empréstimo", "Tela de Lançamento", "Configurações de Parcelamento"]
---

# Adiantamento/Empréstimo c/ repasse ao Fornecedor

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42310959918231) Módulo: Configurações > Rotinas
```

---

Esta tela é bastante semelhante à tela de [Adiantamento/Empréstimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598534-Adiantamento-Empr%C3%A9stimo), tem o objetivo de controlar adiantamentos ou empréstimos feitos com repasse a fornecedores.

O Adiantamento/Empréstimo c/ repasse ao Fornecedor é composto por títulos de despesa, mostrados na grade superior desta tela e por títulos de receitas, visualizados na grade inferior.

![Imagem 2: O Adiantamento/Empréstimo c/ repasse ao Fornecedor é composto por títulos de despesa, mostrados na grade superior desta…](https://ajuda.sankhya.com.br/hc/article_attachments/360084901174)

O lançamento de um novo adiantamento/empréstimo c/ repasse ao fornecedor é feito por meio do botão **"Novo"** no cabeçalho desta tela, que quando acionado abrirá a tela **"Novo Adiantamento/Empréstimo"**, onde serão feitas as seguintes configurações.

![Imagem 3: O lançamento de um novo adiantamento/empréstimo c/ repasse ao fornecedor é feito por meio do botão "Novo" no cabeçalho…](https://ajuda.sankhya.com.br/hc/article_attachments/23763568135831)

O primeiro passo do lançamento de um novo empréstimo será informar o nº da nota fiscal, logo em seguida defina a **"Empresa"** para qual será lançado o título, a **"Data de Negociação"** e a **"Data de Vencimento da Despesa"**, bem como o **"Parceiro"** (parceiro para os títulos de Receita) e o **"Fornecedor"** (que é o parceiro para os títulos de Despesa) além de outros dados que referenciarão o novo título.

Uma forma de se definir o Parceiro nesta tela será através do campo **"Ordem de Carga"**, pois uma vez informado bastará marcar a opção **"Usar parceiro e veículo da ordem de carga"**, para que o sistema preencha automaticamente os campos Parceiro e **"Veículo"** conforme a Ordem de Carga.

É possível preencher os Campos **"Dt. Neg. Despesa"** e **"Dt. Venc. Despesa"** como desejar, uma vez que a data de vencimento aqui não funciona como na tela de Adiantamento/Empréstimo com base no parâmetro de dias úteis.

Posteriormente, configure o **"Parcelamento"** do Adiantamento/Empréstimo:

![Imagem 4: Posteriormente, configure o "Parcelamento" do Adiantamento/Empréstimo :](https://ajuda.sankhya.com.br/hc/article_attachments/23763540231319)

Informe o **"Valor"** do adiantamento/empréstimo, que será o valor que a empresa irá repassar ao fornecedor. Logo, será gerado para a empresa um título de despesa no valor informado neste campo. No campo **"Núm. Parcelas"** informe o número de parcelas em que o adiantamento/empréstimo será pago a empresa.

Na opção **"Frequência"** insira a frequência de vencimento das parcelas, que poderão ser: Diárias, Semanais, Quinzenais, Mensais e etc. Permitindo inclusive que o usuário configure a frequência de vencimento de forma **"Personalizada"**.

[GIF animado: Imagem 5: Na opção "Frequência" insira a frequência de vencimento das parcelas, que poderão ser: Diárias, Semanais, Quinzenais,…](https://ajuda.sankhya.com.br/hc/article_attachments/360086101773)

Na **"Base de Vencimento"** define-se a data na qual vencerá a primeira parcela de Receita, uma vez que a data de vencimento da despesa foi configurada no passo anterior.

A Base de Vencimento da receita poderá ser igual ao **"Vencimento da Despesa"** ou com base na data de **"Negociação"**, poderá ser com base no dia do lançamento, isto é, **"Hoje"** ou ainda **"Informado pelo Usuário"**. Quando Informado pelo Usuário o sistema habilitará o calendário ao lado do campo, para digitação do usuário.

A **"Tx. de juros (%)"** é mensal, logo, se o usuário escolher uma frequência que não seja mensal, o sistema fará automaticamente a correção, segundo a frequência definida.

Em **"Tipo de parcelamento"** o usuário definirá se o parcelamento será por:

- Juros simples;
- Juros compostos;
- Juros compostos (fixas);
- Duplicação (fixas);
- Amortização Constante.

Em **"Tipo de Juros"**, defina onde e como será gravado o juro no título financeiro.

- Cobrar juro de todo período (embutido);
- Se atrasar cobrar os juros como multa;
- Cobrar juro de todo o período (negociado);
- Calcular apenas se atrasar.

A opção **"Calcular apenas se atrasar"** poderá ser usada apenas quando o Tipo de Parcelamento for igual a **"Duplicação (fixa)"**.

O último passo do lançamento será a configuração das **"Preferências"**, ou seja, configuração das informações necessárias para o lançamento de títulos como:

- As TOP’s que serão usadas nos títulos de Despesa e Receitas;
- O **"Tipo de Título"** que está sendo gerado no lançamento deste adiantamento/empréstimo;
- Informações gerenciais como o **"Projeto"**, a **"Natureza"** e o **"Centro de Resultado"**;
- E a **"Conta Bancária"**.

Ao gerar os títulos, o sistema utilizará a **"Natureza (Receita)"** para os títulos de receita e a **"Natureza (Despesa)"** para os títulos de despesa gerados, sendo que, na pesquisa da natureza de receita, o sistema trará apenas as naturezas marcadas como **"Ambos"** ou **"Receita"** e, na pesquisa da natureza de despesa, somente as naturezas marcadas como Ambos ou **"Despesa"**.

Ao clicar em **"Concluir"** o sistema apresentará na grade superior da tela o título de Despesa referente ao adiantamento/empréstimo cedido ao parceiro e na grade inferior os títulos de Receitas gerados pelo parcelamento do título de despesa.

![Imagem 6: Ao clicar em "Concluir" o sistema apresentará na grade superior da tela o título de Despesa referente ao…](https://ajuda.sankhya.com.br/hc/article_attachments/360084938494)

No exemplo da imagem acima, adiantou-se ao parceiro de código 285 a quantia de R$ 776,00 que será restituída à empresa de código 260 em três parcelas de R$ 276,77.

Ao Concluir o lançamento de um adiantamento/empréstimo c/ repasse ao fornecedor o sistema exibe na tela os dados do novo título e os cálculos que irão compô-lo, contudo, o lançamento só será efetivado após confirmado pelo usuário através do botão **"Confirmar"**.

Feito isto o botão **"Confirmar"** ficará desabilitado;

O número do **"Adiant./Emp."** será gerado;

O **"Nro. Nota"** e **"Nro.Único"** de Despesa e das Receitas, também serão gerados, permitindo ao usuário a identificação e movimentação dos títulos no Financeiro.

No botão **"Outras Opções"** existe a funcionalidade **"Parcelar título de despesa"**, trata-se de um recurso usado para parcelar o título de despesa.

[GIF animado: Imagem 7: No botão "Outras Opções" existe a funcionalidade "Parcelar título de despesa" , trata-se de um recurso usado para…](https://ajuda.sankhya.com.br/hc/article_attachments/360086121013)

Este parcelamento é mais simples e não consta a opção de cálculo de juros, ou seja, o usuário poderá através desta opção efetuar a divisão dos valores.

Se o campo **"Com entrada"** estiver marcado torna-se obrigatório o seu preenchimento.

Este parcelamento só poderá ser efetuado durante a inclusão do adiantamento/ empréstimo, não sendo possível este parcelamento após a sua confirmação.

Na grade de títulos de despesa é possível editar os campos: Nro Nota, **"Dt. Vencimento"** e **"Vlr do Desdobramento"**.

Conforme a marcação do campo Com entrada, na primeira linha da grade superior terá a parcela de entrada.

O totalizador é atualizado à medida que são alterados os valores das parcelas na coluna Vlr de Desdobramento. O total das parcelas, após a edição, deverá ser igual ao total original do lançamento, caso contrário será apresentada a mensagem:

**"O total de despesas (xxxxx) deve ser igual ao valor informado (xxxxx)"**

Para visualizar os adiantamentos/empréstimos lançados, basta utilizar o botão de **"Buscar"**, e através das opções de filtros selecionar os títulos desejados.

[GIF animado: Imagem 8: Para visualizar os adiantamentos/empréstimos lançados, basta utilizar o botão de "Buscar" , e através das opções de…](https://ajuda.sankhya.com.br/hc/article_attachments/360086124173)

O número da duplicata referente ao título selecionado na busca será apresentado no campo Adiant./Emp., no cabeçalho da tela.

Para limpar a tela basta clicar no botão **"Cancelar"**, lembrando que este botão não fará nenhum cancelamento de adiantamento, apenas limpará a tela. Um adiantamento/empréstimo confirmado só poderá ser removido pelo botão **"Desfazer"**, e em seguida selecione **"Sim"** ou **"Não"** para confirmar a ação.

Contudo, o lançamento só poderá ser desfeito se não tiver ocorrido baixa de nenhum dos títulos de despesa ou receita, ou ainda, se nenhum deles tiver sido renegociado. Caso contrário, não será possível desfazer o adiantamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110713-Adiantamento-Empr%C3%A9stimo-c-repasse-ao-Fornecedor#top)

### Impressão de um Adiantamento/Empréstimo com Repasse ao Fornecedor

Somente Adiantamento/Empréstimos c/ repasse ao Fornecedor confirmados poderão ser impressos.

Para realizar a impressão de um adiantamento/empréstimo é necessário em primeiro plano, para tal configure o **"Modelo e Impressora"** por meio do botão Outras Opções no cabeçalho da tela.

![Imagem 9: Para realizar a impressão de um adiantamento/empréstimo é necessário em primeiro plano, para tal configure o "Modelo e…](https://ajuda.sankhya.com.br/hc/article_attachments/360086131133)

Na janela de configuração, informe o nome da **"Impressora"** que será usada e o **"Modelo"** para impressão do adiantamento/empréstimo, lembrando que o modelo deve ter sido pré-cadastrado em **"Configurações > Avançado > Modelos de Nota Fiscal/Duplicatas/Boletos"**.

É importante definir o **"Tipo de Impressora"**, pois este indicará ao sistema o conjunto de caracteres de controle da impressora. Se a opção **"Impressão automática"** estiver marcada, no ato da confirmação de um novo lançamento de adiantamento/empréstimo o título será automaticamente impresso. Para imprimir um título já confirmado, bastará selecionar o título desejado e acessar a opção **"Imprimir título de despesa"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110713-Adiantamento-Empr%C3%A9stimo-c-repasse-ao-Fornecedor#top)
