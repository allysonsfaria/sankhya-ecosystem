---
id: "360045116453"
titulo: "Zeramento de Contas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116453-Zeramento-de-Contas"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilidade"
atualizado_em: "2026-09-15T20:54:50Z"
rotulos: ["AJUDA DO SKW", "manual", "Lançamento", "Configuração", "Relatórios", "Contas", "Zeramento", "br.com.sankhya.mgecontab.zeramentodecontas", "Zeramento de Contas manual", "Contabilidade", "Financeiro", "Resultado", "Zeramento de Contas: Relatórios Precisos"]
---

# Zeramento de Contas

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42314973911575) Módulo: Contabilidade > Rotinas
```

---

A partir da configuração desta tela, será possível realizar o zeramento das contas de resultado, seguindo o intervalo de grupos para zeramento informado em uma determinada data. Com isso, será praticável a emissão de relatórios relacionados ao resultado contábil. O sistema realiza uma comparação entre as receitas e despesas, chegando a um resultado final, que pode ser lucro ou prejuízo dentro do período analisado.

![Imagem 2: A partir da configuração desta tela, será possível realizar o zeramento das contas de resultado, seguindo o intervalo…](https://ajuda.sankhya.com.br/hc/article_attachments/360082876874)

**Observação:** Para realização do zeramento de contas, é necessário que tenha sido realizada, inicialmente, a configuração das Contas de Resultado.

Primeiramente, ao solicitar a abertura da tela Zeramento de Contas, esta será aberta com uma pequena tela inicial, solicitando a empresa que você deseja realizar o zeramento das contas. Ao informá-la, sua Razão Social passará a ser exibida na parte superior da tela, onde, caso seja necessário alterar a empresa, clica-se sobre o nome apresentado, para que a tela de escolha de empresas seja reaberta.

Localizado logo abaixo do nome da empresa, existe a **"Conta de Resultado"**, que servirá como embasamento para realização do zeramento.

A tela é dotada de alguns campos de preenchimento obrigatório, que servirão como filtros para realização do zeramento das contas:

Informe no campo **"Número do Lote"** o número do lote contábil. Este será alimentado de acordo com a configuração realizada na tela [Lotes Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607414).

Preencha o campo **"Data do Movimento"** com a data do movimento referente ao zeramento contábil.

No campo **"Histórico"**, será informado o histórico utilizado nos lançamentos contábeis. Previamente, este histórico foi cadastrado na tela [Histórico Padrão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116113).

**Seção Intervalo de grupos para zeramento**

Referente ao campo **"Grupo inicial"**, informe o código da conta contábil que terão seus lançamentos zerados. Ao definir neste campo uma conta sintética, as suas contas **"filhas"** analíticas, também serão zeradas. Por exemplo, suponhamos que foi informada neste campo a conta de código **"1.1.2"**; caso esta conta possua contas filhas de código 1.1.2.1 e 1.1.2.2, estas também serão zeradas.

Preencha no campo **"Grupo final"** a conta contábil que servirá de limitador final para o zeramento das contas, ou seja, até esta conta, será feito o zeramento.

**Seção Contas para resultado final**

Feito o comparativo entre as receitas e despesas registradas no período, a fim de se obter o zeramento, o resultado desta comparação (lucro ou prejuízo) é transferido para as contas definidas como **"Conta prejuízo"** e **"Conta lucro"**.

**Seção Outros**

Quando a marcação **"Lançamentos para a conta de resultado SEM Centro de Resultado?"** for efetuada, definirá que os lançamentos para contas de resultado que não possuem Centro de Resultado, serão também considerados no zeramento.

Ao realizar a marcação, **"Lançamentos para a conta de resultado SEM Projeto?"** fará com que os lançamentos para contas de resultado que não possuem Projeto, sejam também, considerados no zeramento.

Após serem inseridos os dados dos campos desta tela, e acionando o botão **"Salvar Configurações"**, o sistema fará a inclusão da configuração para que seja gerado o relatório da tela Balancete de Verificação, com as contas zeradas.

**Observação:** Caso o Grupo final seja menor que o Grupo inicial, será exibida a seguinte mensagem:

**"Grupo final não pode ser menor que o grupo inicial".**

Depois de preenchidos todos os campos obrigatórios, o botão **"Efetuar Zeramento"** será apresentado habilitado e, ao acioná-lo, caracteriza-se a finalização do processo de zeramento de contas. Será aberta uma pequena tela questionando sobre a certeza da execução do procedimento.

A partir disso, podem ser gerados relatórios relacionados aos resultados contábeis, que irão apontar o comportamento da empresa dentro do período definido, de modo a auxiliar nas tomadas de decisão dentro da organização.
