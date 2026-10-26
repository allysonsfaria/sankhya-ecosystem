---
id: "12753405611799"
titulo: "Como fazer a reintegração de funcionários no MGE Pessoal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/12753405611799-Como-fazer-a-reintegra%C3%A7%C3%A3o-de-funcion%C3%A1rios-no-MGE-Pessoal"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:30:54Z"
rotulos: ["Ocorrências", "Folha", "eSocial", "Configuração Funcionários", "Central do eSocial", "Verificação e envio do evento S-2298", "Cadastro de histórico de ocorrência", "Registro da reintegração no sistema", "MGE Pessoal"]
---

# Como fazer a reintegração de funcionários no MGE Pessoal

Script de operações
**Como fazer a reintegração de funcionários no MGE Pessoal**

#### ![Imagem 1: Objetivo:](https://ajuda.sankhya.com.br/hc/article_attachments/42310183160599) Objetivo:

Ao final deste documento o usuário conseguirá entender como fazer o processo de reintegração de funcionários no módulo MGE Pessoal, para que atendam às exigências do governo.

#### Imagem 2: Introdução Introdução

A reintegração ao trabalho consiste em restabelecer o cargo ocupado atualmente pelo funcionário na organização, ou seja, em devolver ao empregado o vínculo de emprego que lhe foi tirado pela empresa, bem como todas as garantias contratuais havidas antes da demissão.

A reintegração do empregado também pode ocorrer pelo próprio empregador ao observar que a demissão foi indevida. Essa poderá ocorrer também por determinação judicial ao verificar que o empregador excedeu seu poder diretivo, demitindo injustificadamente o empregado que gozava de estabilidade no emprego, por exemplo.

É importante salientar que legalmente as empresas não precisam de justificativa para demitir o empregado, ou seja, a condição de empregador, determinada pelo art. 2º da CLT, assegura o direito potestativo de despedir o empregado sem justa causa. No entanto, este poder não é ilimitado, uma vez que a própria legislação dispõe de algumas situações em que os empregados são revestidos de proteção contra a demissão sem justo motivo ou imotivada.

Para fins do eSocial, todos os atos que restabelecem o vínculo tornando sem efeito o desligamento. Quando houver esse processo de reintegração, a empresa deverá fazer a prestação da informação, até o dia 07 (sete) do mês seguinte a que se refere a reintegração, através do evento “S-2298 - Reintegração”, desde que não ultrapasse a data do envio do evento “S-1200 - Remuneração de Trabalhador vinculado ao Regime Geral de Previdência Social vinculado ao Regime Geral de Previdência Social”, e o “S-1202 – Remuneração do servidor vinculado a Regime Próprio de Previdência Social”. Outro pré-requisito é que tenha sido enviado previamente o evento “S-2299 – Desligamento” ou S-2200 com o campo {desligamento} preenchido.

#### Imagem 3: Como realizar o processo reintegração de funcionários Como realizar o processo reintegração de funcionários

**3.1 Cadastro de Histórico de ocorrência**

Para fazer o processo de reintegração, primeiramente será preciso um cadastro de histórico de ocorrência, para que seja gravado no sistema, a nível gerencial, os registros de movimentações dos funcionários. Acesse a tela **MGE Pessoal\menu Lançamentos\Histórico do Funcionários\Históricos de Ocorrência**

Clique no botão **“Adicionar novo tipo de ocorrência (sinal de +)”.**

![Imagem 4: Clique no botão “Adicionar novo tipo de ocorrência (sinal de +)”.](https://ajuda.sankhya.com.br/hc/article_attachments/17156465246743)

No campo **"Tipo de afastamento"**, selecione a opção **"Reintegração"**.

Logo em seguida, informe a descrição do histórico de ocorrência que será Reintegração. Clique também em **"Confirmar alterações"**.

![Imagem 5: Logo em seguida, informe a descrição do histórico de ocorrência que será Reintegração. Clique também em "Confirmar…](https://lh3.googleusercontent.com/14qXsBMQs399YAsYN8Vb6qE8eAWuCbZiaPqAnOnFyPSkx7Xv1Yu2zGcsd1p6HhH4pTyQnc22t0e0HsaHdYoUzTcqyYLPvbkrKjF5SulLw82U6d-yLlirUr0MgRlZzySpFcrrIlwh3MPB)

**3.2 Cadastro do processo de reintegração**

Como vimos anteriormente, para que a reintegração aconteça, é necessário que o desligamento do funcionário tenha sido realizado no sistema através do cálculo de rescisão, ou seja, deve possuir rescisão efetivamente calculada, além de ter sido transmitido o evento “S-2299 - Desligamento”.

Acesse o menu **MGE Pessoal\Rotinas\Reintegração**
Clique em **"Novo Registro".**

![Imagem 6: Acesse o menu MGE Pessoal\Rotinas\Reintegração Clique em "Novo Registro".](https://ajuda.sankhya.com.br/hc/article_attachments/17156461627287)

O campo **"Código"** da tela é de preenchimento automático no momento de salvar o registro.

Informe o código da empresa e código do funcionário que será reintegrado.

![Imagem 7: Informe o código da empresa e código do funcionário que será reintegrado.](https://ajuda.sankhya.com.br/hc/article_attachments/17156465251223)

**![Imagem 8: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17156461637911) IMPORTANTE:**

Na tela de **"Reintegração de Funcionários"** só serão apresentados na busca do campo **"Funcionário"** os colaboradores que possuem rescisão efetivamente calculada.

O primeiro campo da tela **"Informações Gerais"** é o de **"Histórico de Ocorrência"**, no qual será informada a ocorrência cadastrada anteriormente e será validado apenas para os Tipo de Afastamento igual a **"Reincidência".**

![Imagem 9: O primeiro campo da tela "Informações Gerais" é o de "Histórico de Ocorrência" , no qual será informada a ocorrência…](https://ajuda.sankhya.com.br/hc/article_attachments/17156465258263)

Logo abaixo tem-se a aba **"Informações Gerais"**. 

No campo **"Tipo de Reintegração"**, tem-se a lista para seleção dos seguintes campos:

- 1 - Reintegração por Decisão Judicial;
- 2 - Reintegração por Anistia Legal;
- 3 - Reversão de Servidor Público;
- 4 - Recondução de Servidor Público;
- 5 - Reinclusão de Militar;
- 9 - Outros.

De acordo com o ‘Manual do eSocial’  se os tipos ‘3,4,5’ forem selecionados,  esses só poderão serem informados por órgãos públicos.

Outra informação importante é que em caso de reintegração por determinação judicial, ou seja, do tipo 1 - Reintegração por Decisão Judicial, o campo **"Número do Processo Judicial"** passará a ser obrigatório".

![Imagem 10: Outra informação importante é que em caso de reintegração por determinação judicial, ou seja, do tipo 1 - Reintegração…](https://ajuda.sankhya.com.br/hc/article_attachments/17156461643927)

**![Imagem 11: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17156461637911) IMPORTANTE:**

O processo aqui informado não é um processo vinculado à tabela de processos S-1070. Validação: Informação obrigatória se {tpReint} = [1]. Não preencher nos demais casos.

No campo **"Lei da Anistia"** informe seu número e ano de publicação se a Reintegração for do tipo ‘2 - Reintegração por Anistia Legal’. 

Opte por qual das opções podem ser de acordo com a Anistia conforme lista abaixo;

- 1 - LEI 6.683/1979
- 2 - LEI 8.632/1993
- 3 - LEI 8.878/1994
- 4 - LEI 10.559/2002
- 5 - LEI 10.790/2003
- 6 - LEI 11.282/2006

![Imagem 12: 6 - LEI 11.282/2006](https://ajuda.sankhya.com.br/hc/article_attachments/17156465264663)

Informe também a ‘Data do Efetivo Retorno’ ao trabalho, que deverá ser uma data válida posterior à data de desligamento do trabalhador, e a ‘Data do Efeito’ que deve ser uma data igual ou anterior à data do efetivo retorno ao trabalho e posterior à data do desligamento. 

![Imagem 13: Informe também a ‘Data do Efetivo Retorno’ ao trabalho, que deverá ser uma data válida posterior à data de desligamento…](https://ajuda.sankhya.com.br/hc/article_attachments/17156461650199)

O campo **"Pagamento das remunerações e contribuições em juízo"** servirá para indicar se as remunerações e correspondentes contribuições do período compreendido entre o desligamento e a reintegração foram pagas em juízo. Marque o campo para **"Sim"** e mantenha desmarcado em caso de **"Não".**

![Imagem 14: O campo "Pagamento das remunerações e contribuições em juízo" servirá para indicar se as remunerações e correspondentes…](https://ajuda.sankhya.com.br/hc/article_attachments/17156461653911)

Salve o registro.

![Imagem 15: Salve o registro.](https://ajuda.sankhya.com.br/hc/article_attachments/17156465281175)

**3.3 Cadastro de funcionários**

Após realizada a reintegração de funcionários, abra a tela MGE Pessoal \menu "Arquivos/Funcionários" e verifique se os dados foram alimentados. 

Na aba **"Reintegração"** tem-se as informações trazidas automaticamente dos registros que foram feitos anteriormente na tela Reintegração de Funcionário.

![Imagem 16: Na aba "Reintegração" tem-se as informações trazidas automaticamente dos registros que foram feitos anteriormente na…](https://ajuda.sankhya.com.br/hc/article_attachments/17156461661719)

![Imagem 17: Na aba "Reintegração" tem-se as informações trazidas automaticamente dos registros que foram feitos anteriormente na…](https://ajuda.sankhya.com.br/hc/article_attachments/17156461665175)

Outra informação importante também será na aba **"Admissão"**, na qual o campo **"Tipo de Admissão"** deverá estar com a opção **"Reintegração"**.

**![Imagem 18: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17156461637911) IMPORTANTE:**

De acordo com o Manual do eSocial, na reintegração deve ser mantida a matrícula anteriormente cadastrada no evento “S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador”.

#### Imagem 19: Ocorrências Ocorrências

Após realizada a reintegração também pode-se verificar que o sistema criou automaticamente o histórico do funcionário, para isso acesse a tela MGE Pessoal\menu Lançamentos\Histórico do Funcionário\Registro de Ocorrências:

Para localizar o seu funcionário, utilize os filtros disponíveis no canto esquerdo da tela, como por exemplo informando o código da empresa e do Funcionário, logo depois clique em aplicar.

![Imagem 20: Para localizar o seu funcionário, utilize os filtros disponíveis no canto esquerdo da tela, como por exemplo informando…](https://lh4.googleusercontent.com/prqZ_am8tcw9MnLzbCE3uemJ_P8TI-PlnGJZYdbtMBgDnwynAwFPxLY1Zn34lT1SMMwm3hvIXUbYtzqithBTXbUOd_iGnEzt5vboB1JnACHYXwZb1lqVIdhqjnCkHOtdGVvNIEVCEpF5)

#### Imagem 21: Central do eSocial Central do eSocial

Após confirmada a reintegração, o sistema estará pronto para envio do evento “S-2298 - Reintegração” na tela da **"Central do eSocial"**. Envie o evento gerado.

![Imagem 22: Após confirmada a reintegração, o sistema estará pronto para envio do evento “S-2298 - Reintegração” na tela da…](https://ajuda.sankhya.com.br/hc/article_attachments/17156465293591)
