---
id: "360044607434"
titulo: "Importação do Plano de Contas com base no ECD"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607434-Importa%C3%A7%C3%A3o-do-Plano-de-Contas-com-base-no-ECD"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > ECD"
atualizado_em: "2026-09-15T17:43:04Z"
rotulos: ["AJUDA DO SKW", "manual", "ECD", "Contas", "Plano", "br.com.sankhya.mgecontab.planodecontasecd", "Importação do Plano de Contas com base no ECD manual", "Importação", "Contabilidade", "Plano de Contas", "Eficiência na Importação: Plano de Contas do ECD"]
---

# Importação do Plano de Contas com base no ECD

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42314963762711) Módulo: Contabilidade > Rotinas
```

---

Essa rotina tem por objetivo promover a importação do Plano de Contas e o Saldo das Contas, com base na importação de um arquivo de ECD - Escrituração Contábil Digital. Tem-se aqui, uma rotina que poderá ser adotada apenas para as Empresas Filiais que utilizam um Plano de Contas diferente do cadastrado no sistema, de modo que, para as filiais que possuem o mesmo plano de contas, não se faz necessária sua importação.

| [Definições iniciais e Botões da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607434-Importa%C3%A7%C3%A3o-do-Plano-de-Contas-com-base-no-ECD#definiesiniciaisebotesdatela) | [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607434-Importa%C3%A7%C3%A3o-do-Plano-de-Contas-com-base-no-ECD#abageral) |
| --- | --- |
| [Aba Saldo ECD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607434-Importa%C3%A7%C3%A3o-do-Plano-de-Contas-com-base-no-ECD#abasaldoecd) | [Validações e Restrições para importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607434-Importa%C3%A7%C3%A3o-do-Plano-de-Contas-com-base-no-ECD#validaeserestriesparaimportao) |
| [Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607434-Importa%C3%A7%C3%A3o-do-Plano-de-Contas-com-base-no-ECD#h_272d8ac0-96db-43b9-a1bd-98fa19b48a79) |  |

 

![Imagem 2: Parâmetros](https://ajuda.sankhya.com.br/hc/article_attachments/8494500962967)

## Definições iniciais e Botões da tela

Primeiramente, na abertura da tela, deve-se selecionar a empresa para a qual serão importados os dados pertinentes ao Plano de Contas.

No alto da tela, tem-se três botões que irão influenciar no andamento desta rotina da seguinte maneira:

![Imagem 3: "Importar" - Este botão quando acionado, apresenta um pop-up para escolha e consequente importação do arquivo…](https://ajuda.sankhya.com.br/hc/article_attachments/15437995820055) **"Importar"** - Este botão quando acionado, apresenta um pop-up para escolha e consequente importação do arquivo correspondente ao Plano de Contas.

![Imagem 4: "Importar" - Este botão quando acionado, apresenta um pop-up para escolha e consequente importação do arquivo…](https://ajuda.sankhya.com.br/hc/article_attachments/8494549442967)

![Imagem 5: "Excluir" - Através deste botão realiza-se a exclusão de um Plano de Contas já importado. Ao solicitar a eliminação de…](https://ajuda.sankhya.com.br/hc/article_attachments/15437991251607) **"Excluir"** - Através deste botão realiza-se a exclusão de um Plano de Contas já importado. Ao solicitar a eliminação de um Plano de Contas, será apresentada uma mensagem de confirmação de tal procedimento; optando-se por continuar a exclusão (botão Sim), o sistema irá verificar se existe algum lançamento contábil que utiliza a Conta Contábil vinculada ao Plano de Contas que será excluído. Caso exista, será exibida a seguinte mensagem:

**"Não é possível excluir o Plano de Contas, pois existem lançamentos contábeis vinculados às contas desse Plano de Contas. Para excluí-lo, é necessário excluir antes os lançamentos contábeis vinculados a tais contas."**

![Histórico](https://ajuda.sankhya.com.br/hc/article_attachments/15438037477399) **"Histórico de importação"** - Este botão exibe um pop-up de nomenclatura "Histórico" que trás um breve detalhamento das importações já realizadas. Ainda por meio deste pop-up pode-se realizar a baixa do arquivo correspondente à importação desejada, de modo a analisá-lo mais minuciosamente, se for o caso.

![Imagem 7: "Histórico de importação" - Este botão exibe um pop-up de nomenclatura "Histórico" que trás um breve detalhamento das…](https://ajuda.sankhya.com.br/hc/article_attachments/8494554022807)

Por meio do botão ![Ver](https://ajuda.sankhya.com.br/hc/article_attachments/15438004949015) **"Ver Andamento"** você poderá acompanhar o andamento da importação que será realizada:

![Imagem 9: Por meio do botão "Ver Andamento" você poderá acompanhar o andamento da importação que será realizada:](https://ajuda.sankhya.com.br/hc/article_attachments/8494600892567)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607434-Importa%C3%A7%C3%A3o-do-Plano-de-Contas-com-base-no-ECD#top)

## Aba Geral

![Imagem 10: Aba Geral](https://ajuda.sankhya.com.br/hc/article_attachments/8494603135767)

Tem-se na Aba Geral alguns dados provenientes da importação realizada. Os campos abaixo não permitem edição; seu objetivo é somente de visualização. São eles:

**Analítica:** Conforme importação, quando assinalada, tem-se uma conta analítica.

**Grupo de Conta:** Tem-se neste campo, a Descrição e Código na qual a conta está vinculada.

**Dt. Inclusão:** Apresenta-se neste campo, a Data da Inclusão da conta.

**Usuário:** Tem-se aqui, o Código e Descrição do Usuário que realizou a importação.

**Data e hora primeira importação:** Este campo registra a data e hora em que a primeira importação foi efetuada.

**Data e hora alteração:** Tem-se neste campo, o registro da última alteração realizada na tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607434-Importa%C3%A7%C3%A3o-do-Plano-de-Contas-com-base-no-ECD#top)

## Aba Saldo ECD

![Imagem 11: Aba Saldo ECD](https://ajuda.sankhya.com.br/hc/article_attachments/8494640320023)

A Aba Saldo é composta pelos dados pertinentes aos Saldos das Contas importadas. São informações que não permitem edição; seu objetivo é somente de visualização. É uma grade composta pelas seguintes colunas:

**Referência:** Apresenta a referência do saldo composta por mês e ano (01/2016, por exemplo), conforme importação.

**Centro de Resultado:** Tem-se aqui, o código do Centro de Resultado do saldo, se houver.

**Saldo Inicial:** Exibe o valor do Saldo Inicial, conforme importação.

**Indicador de Situação do Saldo Inicial:** Esta coluna apresenta a situação do saldo inicial, ou seja, se este é Devedor (D) ou Credor (C), de acordo com a importação.

**Débitos:** Tem-se aqui, o valor de débitos, conforme importação.

**Créditos:** Nota-se nesta coluna, o valor de créditos, de acordo com a importação.

**Saldo final:** Apresenta o valor do Saldo Final, conforme importação.

**Indicador de Situação do Saldo Final:** Tem-se nesta coluna, a situação do saldo final, ou seja, se o mesmo é Devedor (D) ou Credor (C), conforme importação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607434-Importa%C3%A7%C3%A3o-do-Plano-de-Contas-com-base-no-ECD#top)

## Validações e Restrições para importação

Na importação do Plano de Contas, algumas verificações são efetuadas. A saber:

- No arquivo importado, o registro I010:
- O Campo 2 (IND\_ESC) - sua forma deve ser 'G' - (Livro Diário completo sem Escrituração Auxiliar) ou 'R' (Livro Diário com Escrituração Resumida, com escrituração auxiliar). Se esta regra não for atendida, será apresentado o seguinte erro:

**"Somente os tipos de escriturações: G - (Livro Diário Completo sem escrituração auxiliar) ou R (Livro Diário com Escrituração Resumida, com escrituração auxiliar) estão preparados para realizar a importação do arquivo."**

- O Campo 3 (COD\_VER\_LC) deste registro, se refere a versão do layout; esta deve ser igual ou maior que 4.00. Caso não seja, será apresentado o seguinte erro:

**"Somente versão maior ou igual a 4.00 é suporta para importação."**

- A Importação do arquivo só poderá ocorrer, caso tenha-se configurado a Máscara da Conta Externa da empresa selecionada, por meio da tela [Vinculação de Contas Contábeis Externas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025394653-Vincula%C3%A7%C3%A3o-de-Contas-Cont%C3%A1beis-Externas). Caso esta configuração não tenha sido feita, será apresentada a seguinte mensagem:

**"Para realizar a importação do Plano de Contas e dos Saldos das Contas é necessária a definição da máscara das Contas Contábeis na tela de Vinculação de Contas Contábeis Externas."**

- Caso seja feita a importação de um arquivo ECD da empresa selecionada, em que já ocorreu a importação, os valores dos saldos serão reprocessados, e será salvo sempre o valor do saldo da última importação ocorrida.
- Quando já tiver ocorrido alguma importação do arquivo para a empresa selecionada, e uma nova importação for realizada, o sistema verificará se houve alteração no Plano de Contas do arquivo; para cada tipo de alteração o sistema irá se comportar de uma forma diferente. Vejamos:
- Caso no novo arquivo exista uma nova conta contábil que não foi cadastrada anteriormente, esta conta contábil será incluída com seu respectivo saldo, e na finalização da importação do arquivo, será informado que a importação ocorreu com sucesso e que ocorreram alterações no Plano de Contas:

**"Foram encontradas novas contas contábeis no último arquivo importado, a mesma não existiam na estrutura anterior e foi adicionada ao plano de contas."**

- Caso alguma conta contábil que foi cadastrada anteriormente não tenha sido encontrada na nova importação, a referida conta não será excluída e seu saldo não será atualizado; na finalização da importação do arquivo, será exibida a mensagem que a importação ocorreu com sucesso, porém ocorreram alterações no plano de contas:

**"Algumas Contas contábeis que foram incluídas em importações anteriores, não foram encontradas no último arquivo importado. Favor verifique a vinculação das Contas Contábeis Externas."**

Depois de realizada a importação, o sistema apresentará o Plano de Contas importado e seu respectivo saldo da conta.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607434-Importa%C3%A7%C3%A3o-do-Plano-de-Contas-com-base-no-ECD#top)

## Parâmetros

Com o parâmetro **"Consid. per. contáb. emp. plano conta p/ saldo ECD - CONPERCONSALECD"** ligado, o sistema irá considerar o período contábil da empresa do plano de contas para realizar a Importação do Plano de Contas com base no ECD, ou seja, se a empresa que estiver realizando a importação possuir o plano de contas compartilhado de outra empresa e ela estiver com o período contábil com um ano diferente do arquivo importado, os saldos não será importados corretamente. Caso se encontre desligado, o sistema considerará apenas o período contábil da empresa que está fazendo a importação, mesmo tendo o plano de contas compartilhado de outra empresa.

Você poderá realizar a importação de plano de contas da ECD tendo como referência o arquivo de conta contábil reduzida; para isto, basta que você ligue o parâmetro **"Saldo Plano de Contas do ECD pela conta reduzida? - SALDOCONTREDUZ"** e importe o arquivo .txt. Dessa forma, a rotina irá avaliar a conta e seguirá com o fluxo de importação, considerando o saldo correto para as contas reduzidas.

**Observação:** Se você desligar o parâmetro, as contas reduzidas não serão importadas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607434-Importa%C3%A7%C3%A3o-do-Plano-de-Contas-com-base-no-ECD#top)
