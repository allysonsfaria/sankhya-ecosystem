---
id: "360045110093"
titulo: "Pontos de Decisões (Gateways)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110093-Pontos-de-Decis%C3%B5es-Gateways"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-10-15T14:16:08Z"
rotulos: ["AJUDA DO SKW", "Configuração", "Ordem de Produção", "Gateways", "Pontos de Decisões (Gateways) manual", "Produção", "Caminhos de correção", "Pontos de decisão", "Gateways em fluxos", "Processos Produtivos"]
---

# Pontos de Decisões (Gateways)

Na execução de um fluxo de processo, é comum existir pontos de decisões onde se define que, a partir dali, o fluxo de processo deverá seguir um determinado caminho. Nas Indústrias este cenário também existe, visto que os Processos Produtivos são fluxos de processos da mesma.

Pensando neste cenário, a Sankhya disponibilizou no módulo de Produção/W uma forma para se criar Processos Produtivos contendo pontos de decisões ao longo do fluxo. Estes pontos de decisões são representados graficamente por elementos chamados de Gateways.

[Gateways](https://ajuda.sankhya.com.br/hc/pt-br/articles/pontos-de-decisoes-(gateways).html#gateways)                                                                   [Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/pontos-de-decisoes-(gateways).html#casodeuso)

[Cadastros](https://ajuda.sankhya.com.br/hc/pt-br/articles/pontos-de-decisoes-(gateways).html#cadastros)                                                                  [Execução](https://ajuda.sankhya.com.br/hc/pt-br/articles/pontos-de-decisoes-(gateways).html#execucao)

## Gateways

Abaixo, trouxemos a descrição e funcionalidade de cada um dos Gateways:

![Imagem 1: Com este Gateway , podemos dar continuidade ao fluxo de processo, a partir de um único caminho, dada uma determinada…](https://ajuda.sankhya.com.br/hc/article_attachments/8892737382295) Com este Gateway, podemos dar continuidade ao fluxo de processo, a partir de um único caminho, dada uma determinada condição. Sendo assim, o Gateway possui vários fluxos de saída (caminhos) e cada um dos fluxos possuem uma condição.

Durante a execução da Ordem de Produção, o sistema avalia as várias condições, seguindo uma ordem pré-estabelecida. A primeira condição que retornar verdadeira terá seu fluxo de processo escolhido (caminho) e, consequentemente, executado. É possível definir um fluxo de saída (caminho) como **"padrão"**, assim, caso as condições dos demais fluxos (caminhos) sejam falsas, este será o fluxo (caminho) escolhido.

![Imagem 2: Através deste Gateway , é permitido dar seguimento ao fluxo de processo, a partir de vários caminhos paralelamente dada…](https://ajuda.sankhya.com.br/hc/article_attachments/8892738037143) Através deste Gateway, é permitido dar seguimento ao fluxo de processo, a partir de vários caminhos paralelamente dada uma determinada condição. Deste modo, o Gateway contém vários fluxos de saídas (caminhos) e cada um dos fluxos possui uma condição. No decorrer da execução da Ordem de Produção, o sistema analisa as várias condições percorrendo uma ordem pré-estabelecida. Todas as condições cujo retorno seja verdadeiro, terão seu fluxo de processo escolhido (caminho) e, consequentemente, executado paralelamente. É permitido definir um fluxo de saída (caminho) como **"padrão"**, assim caso as condições dos demais fluxos (caminhos) sejam falsas, este será o fluxo (caminho) escolhido.

![Imagem 3: Este Gateway não representa um ponto de decisão conforme os demais Gateways . O que este elemento faz é dar…](https://ajuda.sankhya.com.br/hc/article_attachments/8892789117719) Este Gateway não representa um ponto de decisão conforme os demais Gateways. O que este elemento faz é dar continuidade à vários fluxos no processo ao mesmo tempo (fluxos paralelos).

**Observação:** as transições que saem do Gateway para uma atividade ou outro elemento qualquer (Gateway ou evento), são os caminhos possíveis a serem seguidos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110093-Pontos-de-Decis%C3%B5es-Gateways#top)

## Caso de Uso

O caso a ser apresentado, consiste na fabricação de Shampoo em uma Indústria de Cosméticos. O processo se inicia na atividade de Separação de MPs, onde os Almoxarifes separam todas as matérias-primas necessárias para a fabricação daquele lote de produção de Shampoo.

Uma vez separadas as matérias-primas e entregues à Produção, os operários podem iniciar a Manipulação do produto que consiste na junção de todas as matérias-primas em um reator, para que seja feita a mistura base para o shampoo. Ao concluir essa atividade, os operários retiram o produto manipulado da máquina e o mesmo é armazenado em um pulmão.

O produto ficará armazenado até que o técnico do Laboratório de Qualidade realize a inspeção no produto na atividade Qualidade. A inspeção consiste em analisar diversas características da mistura base do shampoo. O resultado da analise é o Ponto de Decisão, pois é ele que define qual será o caminho que a mistura base deverá seguir, tem-se as seguintes opções:

- **Caminho 1 – Produção liberada:** todas as características analisadas da mistura estão dentro do intervalo de aceitação. Deste modo, o produto pode seguir para o envaze;
- **Caminho 2 – Necessidade de correção c/ materiais:** a mistura teve uma ou mais características reprovadas, sendo necessário realizar uma correção com acréscimo de materiais. Assim sendo, a execução da Ordem deve voltar à atividade de Separação de MPs para que o almoxarife separe os materiais necessários para a correção.
- **Caminho 3 – Necessidade de correção s/ materiais:** a mistura conteve uma ou mais características reprovadas, fazendo-se necessário a realização de uma correção sem acréscimo de materiais. Portanto, a execução da Ordem deve voltar à atividade de Manipulação onde o operário voltará o produto para o Reator para a correção.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110093-Pontos-de-Decis%C3%B5es-Gateways#top)

## Cadastros

O primeiro passo a ser realizado é o cadastro de um Processo Produtivo que represente o caso de uso apresentado, ou seja, deve ser cadastrado um Processo com quatro Atividades e um Gateway do tipo Exclusivo. Na figura abaixo, mostramos como ficará o Processo:

![Imagem 4: O primeiro passo a ser realizado é o cadastro de um Processo Produtivo que represente o caso de uso apresentado, ou…](https://ajuda.sankhya.com.br/hc/article_attachments/8892752074519)

Além disso, se faz necessário acessar a rotina [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados) para realizar a criação do campo adicional **"Cabeçalho Laudo"**, na tabela TGACLL. Este campo adicional será utilizado pelo técnico de laboratório responsável pela inspeção da mistura, onde o mesmo poderá informar em caso de correção se serão necessários materiais. Temos abaixo os dois pontos que abordam os detalhes para construção do novo campo:

**1)** Preenchimento dos campos obrigatórios:

![Imagem 5: 1) Preenchimento dos campos obrigatórios:](https://ajuda.sankhya.com.br/hc/article_attachments/8892790511639)

**2)** Configurar o botão **"Opções"**:

![Imagem 6: 2) Configurar o botão "Opções" :](https://ajuda.sankhya.com.br/hc/article_attachments/8892790865303)

Por questão de segurança, cria-se uma Trigger na tabela TGACLL, para impedir que o técnico de laboratório ao reprovar o laudo, deixe de especificar a necessidade de correção (c/ materiais ou s/materiais). As características para estruturação da trigger podem ser visualizadas a seguir:

CREATE OR REPLACE TRIGGER TRG\_UPT\_STATUS\_AD

    BEFORE UPDATE

    ON TGACLL

    FOR EACH ROW

    WHEN (OLD.STATUS <> NEW.STATUS)

DECLARE

    --ERROR    EXCEPTION;

    --ERRMSG   VARCHAR2 (255);

BEGIN

    IF (:NEW.STATUS = 'R') AND (:NEW.AD\_NECESSIDADECORRECAO = 'N')

    THEN

        RAISE\_APPLICATION\_ERROR(-20101, 'Laudos reprovados não podem estar

definidos com necessidade de correção igual à Não.');

   END IF;

END;

/

Ao final, se faz necessário definir no Processo Produtivo a condição de cada um dos caminhos para que o sistema verifique durante a execução da OP e resolva qual fluxo deverá seguir.

- **Caminho 1:** na transição que representa o **"Caminho 1"**, indica-se que este será o caminho Padrão para o fluxo de processo. Deste modo, quando a condição de todas as demais transições retornarem falso, este será o caminho escolhido:

![Imagem 7: Caminho 1: na transição que representa o "Caminho 1" , indica-se que este será o caminho Padrão para o fluxo de…](https://ajuda.sankhya.com.br/hc/article_attachments/8892753339031)

- **Caminho 2:** na transição que representa o **"Caminho 2"**, define-se sua ordem como "1" e adiciona-se um Filtro de Transição do tipo "Condição personalizada":

![Imagem 8: Caminho 2: na transição que representa o "Caminho 2" , define-se sua ordem como "1" e adiciona-se um Filtro de Transiçã…](https://ajuda.sankhya.com.br/hc/article_attachments/8892753702807)

Temos abaixo a expressão que deverá ser utilizada:

SELECT CASE WHEN AD\_NECESSIDADECORRECAO = 'C' THEN 1 ELSE 0 END

  FROM TGACLL

WHERE NUCLL = (SELECT MAX (NUCLL)

                          FROM TPRLCCQ

                        WHERE IDICCQ = (SELECT MAX (IDICCQ)

                                                    FROM TPRICCQ

                                                  WHERE IDIPROC = :IDIPROC))

- **Caminho 3:** na transição que representa o **"Caminho 3"**, determina-se sua ordem como "2" e acrescenta-se um Filtro de Transição do tipo **"Condição personalizada"**:

![Imagem 9: Caminho 3: na transição que representa o "Caminho 3" , determina-se sua ordem como "2" e acrescenta-se um Filtro de…](https://ajuda.sankhya.com.br/hc/article_attachments/8892754378135)

A seguir, trouxemos a expressão que deverá ser aplicada:

SELECT CASE WHEN AD\_NECESSIDADECORRECAO = 'S' THEN 1 ELSE 0 END

  FROM TGACLL

WHERE NUCLL = (SELECT MAX (NUCLL)

                          FROM TPRLCCQ

                        WHERE IDICCQ = (SELECT MAX (IDICCQ)

                                                    FROM TPRICCQ

                                                  WHERE IDIPROC = :IDIPROC))

**Nota:** em alternativa as expressões personalizadas inseridas nos Filtros de Transições, poderíamos ter construídos expressões em JavaScript e inseri-las na rotina de [Configuração da Transições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es#abageral), campo **"Expressão"**.

Lembrando que, durante a execução de OPs do Processo, a expressão será executada quando chegar ao Ponto de Decisão e se espera um resultado igual a verdadeiro (true = '1') ou falso (false = '0').

A expressão da Transição será utilizada em conjunto com os Filtros de Transições da Transição, utilizado o operador de adição AND.

(Expressão javaScript aba Geral) && Filtros de Transição (transição 1511)

**Observação:** os filtros de transições são avaliados de forma agrupada ao tipo do filtro (Produto Acabado, Estoque Disponível de MP, Necessidade de Setup para o Centro de Trabalho e Condição personalizada) considerando **"OR"** para cada filtro do mesmo grupo, ou seja, se qualquer uma das expressões do grupo retornar verdadeiro (true = '1'), então o grupo resulta em verdade.

Os grupos são avaliados considerando AND, ou seja, o resultado da transição será verdadeiro, apenas se todos os grupos existentes resultarem em verdadeiro (true = '1'). Vejamos um exemplo:

- P – Produto Acabado = { true , false , false } -> resultado do grupo P = 'true';
- S – Expressão Personalizada = { false, false } -> resultado do grupo S = 'false';
- Resultado da Transição, neste exemplo será 'false', pois o grupo S é false.

**Nota:** para as expressões personalizadas do filtro de transição, estão disponíveis alguns parâmetros para uso, são eles :IDPROC – Código de identificação do Processo Produtivo e :IDIPROC – Nro da Ordem de Produção.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110093-Pontos-de-Decis%C3%B5es-Gateways#top)

## Execução

Dadas as configurações, temos a fundamentação para lançamento de uma Ordem de Produção para o Processo Produtivo e entendimento do comportamento executado pelo sistema. Após realizar o registro da Ordem, será necessário executar suas atividades até que seja alcançada a atividade **"Qualidade"**. Neste ponto, será lançado o laudo com a definição, apontando se a mistura base do produto necessita ou não de correção.

Na atividade Qualidade, realize os seguintes procedimentos:

- Iniciar um novo Ciclo de Qualidade;
- Incluir uma amostra;
- Aprovar esta amostra;
- Inserir um Laudo;
- Apontar resultados que façam com que o Laudo seja reprovado;
- Concluir o laudo como "reprovado".

Podemos analisar que a Trigger criada será executada e impedirá que o laudo seja aprovado, pois não foi especificado pelo responsável, o tipo de correção necessária conforme apresentado na imagem abaixo:

![Imagem 10: Podemos analisar que a Trigger criada será executada e impedirá que o laudo seja aprovado, pois não foi especificado…](https://ajuda.sankhya.com.br/hc/article_attachments/8892793416343)

Voltando no Laudo e definindo o campo **"Necessidade de correção"** com a opção **"Sim, c/ materiais"**, representará que a correção a ser executada exige materiais. Assim, o fluxo de processo seja direcionado ao caminho 2 e uma nova atividade **"Separação de MPs"** seja criada para que o Almoxarife separe os materiais necessários para correção.

![Imagem 11: Voltando no Laudo e definindo o campo "Necessidade de correção" com a opção "Sim, c/ materiais" , representará que a…](https://ajuda.sankhya.com.br/hc/article_attachments/8892823072151)

Executando novamente as atividades até chegar na atividade Qualidade, ao iniciar um novo Ciclo de Qualidade, incluindo e aprovando uma Amostra, e inserindo um Laudo. Desta vez, o laudo também deverá ser reprovado, mas no campo **"Necessidade de correção"** deverá estar selecionada a opção **"Sim, s/ materiais"**. Sendo assim, o fluxo de processo será direcionado ao caminho 3 e uma nova atividade **"Mistura"** será criada para que o Operário volte a mistura do Pulmão para o Reator e seja executada a correção.

Efetuando os mesmos passos citados no parágrafo acima, você deve concluir e aprovar o laudo de forma que o fluxo de processo seja direcionado ao caminho 1 e uma atividade de **"Envase"** seja criada para dar continuação e finalização do Processo de fabricação de Shampoo.

Dessa forma foi possível simular todos os possíveis caminhos do Processo Produtivo a partir de um Ponto de Decisão.

**Importante:** o exemplo apresentado trata-se de uma ilustração para se conhecer e entender o uso das funcionalidades existentes no módulo. Por este fato, não foi considerado no mesmo a melhor lógica para desenvolvimento das expressões, assim como expressões com melhor performance.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110093-Pontos-de-Decis%C3%B5es-Gateways#top)
