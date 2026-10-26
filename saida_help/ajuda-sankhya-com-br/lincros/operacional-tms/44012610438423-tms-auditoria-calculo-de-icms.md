---
id: "44012610438423"
titulo: "[TMS] - Auditoria Cálculo de ICMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012610438423--TMS-Auditoria-C%C3%A1lculo-de-ICMS"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:34:04Z"
rotulos: ["sync_hc", "lincros", "lincros_13433435", "sync_hash_d8681a52250b"]
---

# [TMS] - Auditoria Cálculo de ICMS

**Objetivo**: Facilitar a investigação do cálculo de ICMS incorreto, do motivo do não destaque ou não soma no total do frete.

**Considerações**:

- Existem algumas situações que podem impactar o cálculo do ICMS na Ferramenta Lincros. O ICMS pode não destacar nos movimentos do Pré-conhecimento, destacar, mas não somar no total do frete, ou calcular incorretamente;
- Os CT-es não podem ter erro de importação;
- ICMS Destacado -> Se no cadastro da transportadora estiver como ‘Optante pelo Simples’ não vai destacar ICMS', o mesmo deve ser 'lucro presumido' ou 'lucro real';

## ICMS não destacado

1. Todos os Componentes vinculados às Tabelas de frete possuem um box chamado Calcular ICMS. Caso ele estiver desmarcado, o componente não será considerado na base de cálculo de ICMS. É importante validar os Componentes vinculados nas Rotas / Faixas para cálculo e nas Generalidades da tabela, no caminho Cadastros gerais > Transportadoras > Negociações > Tabelas de frete:

   ![Imagem 1: Todos os Componentes vinculados às Tabelas de frete possuem um box chamado Calcular ICMS. Caso ele estiver desmarcado,…](https://ajuda.sankhya.com.br/hc/article_attachments/44012627970839)
2. Caso os componentes de ICMS estejam marcados na Tabela de frete e mesmo assim o movimento não apresente o Componente ICMS: acessar o caminho Cadastros Gerais > Transportadoras > Transportadora, pesquisar pelo nome da transportadora, e consultar o Regime tributário informado no cadastro:

   ![Imagem 2: Caso os componentes de ICMS estejam marcados na Tabela de frete e mesmo assim o movimento não apresente o Componente…](https://ajuda.sankhya.com.br/hc/article_attachments/44012598918423)

Quando a opção marcada for Optante pelo Simples, o ICMS não será destacado nos movimentos. Você pode consultar se a transportadora é Optante pelo Simples Nacional [neste link](https://servicos.receita.fazenda.gov.br/servicos/cnpjreva/cnpjreva_solicitacao.asp), basta informar o CNPJ da transportadora.

Se a transportadora não for Optante pelo Simples Nacional e essa opção (Simples Nacional) estiver informada no cadastro, você pode entrar em contato com o [atendimento@lincros.com](mailto:atendimento@lincros.com) solicitando alteração. Isso pode acontecer, pois, algumas transportadoras já possuem cadastro na Ferramenta Lincros e posteriormente mudam seu regime de tributação.

3.Tipo de Frete não marcado para destacar ICMS por modalidade do responsável pelo frete, nas Taxas Estaduais: Caso os modais CIF e FOB não estiverem com a opção Calcula ICMS marcada, o imposto não será destacado nos movimentos.

Para conferir se a ausência de cálculo está relacionada a matriz de taxas personalizada, acessar o caminho Cadastros gerais > Configurações da empresa > Taxas > Taxas estaduais. Caso a tela estiver vazia (não trouxer informações cadastradas), a empresa não possui base personalizada. Caso trouxer, pesquisar pela UF de origem e destino do Pré-conhecimento que apresenta a divergência no cálculo, e conferir se as opções de Calcular ICMS CIF e Calcular ICMS FOB estão marcadas:

![Imagem 3: Para conferir se a ausência de cálculo está relacionada a matriz de taxas personalizada, acessar o caminho Cadastros…](https://ajuda.sankhya.com.br/hc/article_attachments/44012636491799)

Caso o cliente destinatário não possua Inscrição Estadual no seu cadastro, entende-se que ele se trata de um não contribuinte, neste caso é necessário informar a alíquota no campo "ICMS não contribuinte" para que o ICMS seja calculado;

![Imagem 4: Caso o cliente destinatário não possua Inscrição Estadual no seu cadastro, entende-se que ele se trata de um não…](https://ajuda.sankhya.com.br/hc/article_attachments/44012610930711)

## ICMS destacado não soma nos movimentos

1. Para que o componente ICMS seja somado aos movimentos do Pré-conhecimento, é necessário adicionar na Tabela de fretes o componente ICMS Destacado. Acesse o caminho Cadastros gerais > Transportadoras > Negociações > Tabelas de frete, na aba Generalidades, e inclua o componente. Esta opção apresenta no movimento o destaque do imposto uma única vez, e soma-o ao valor total do frete;

![Imagem 5: 1. Para que o componente ICMS seja somado aos movimentos do Pré-conhecimento, é necessário adicionar na Tabela de…](https://ajuda.sankhya.com.br/hc/article_attachments/44012611026967)

**Importante**: O cálculo de ICMS realizado por este componente é de uso padrão da maioria das transportadoras, que adicionam o valor do ICMS na somatória dos componentes. (Fórmula de cálculo ICMS destacado = Base / ((100 - alíquota) / 100))). O resultado será a Base + ICMS. Logo, para descobrir qual o valor apenas do ICMS, Diminuir a Base do resultado da Fórmula.

## Exemplo:

Base: R$ 50,00.

Alíquota 12%: ((100 - 12) / 100)) = 0,88

Cálculo: R$ 50,00 / 0,88 = R$ 56,81

ICMS: R$ 56,81 - R$ 50,00 = R$ 6,81

Para as transportadoras que apenas destacam o ICMS, sem adicioná-lo no total do frete, o componente que deve ser informado na tabela ao invés do ICMS Destacado, deve ser o ICMS Reduzido.

(Fórmula de cálculo ICMS reduzido: Base x alíquota).

## Exemplo:

Base: R$ 50,00.

Alíquota 12%

Cálculo: R$ 50,00 x 12% = R$ 6,00 ou seja, ICMS = R$ 6,00

![Imagem 6: Cálculo: R$ 50,00 x 12% = R$ 6,00 ou seja, ICMS = R$ 6,00](https://ajuda.sankhya.com.br/hc/article_attachments/44012628577303)

Os movimentos de um Pré-conhecimento calculado com o ICMS reduzido ficam da seguinte forma (observe o valor destacado, sem somar no total dos componentes):

![Imagem 7: Os movimentos de um Pré-conhecimento calculado com o ICMS reduzido ficam da seguinte forma (observe o valor destacado,…](https://ajuda.sankhya.com.br/hc/article_attachments/44012636985111)

## ICMS REDUZIDO

Para utilizar o cálculo reduzido no sistema, deve ser inserido o componente de frete ICMS reduzido na tabela de fretes.

O componente deve ser cadastrado na empresa:

![Imagem 8: O componente deve ser cadastrado na empresa:](https://ajuda.sankhya.com.br/hc/article_attachments/44012611413783)

 2. Algumas transportadoras somam o ICMS no cálculo do frete total, porém, realizam a distribuição do valor do imposto correspondente a cada componente. Podemos visualizar no destaque dos componentes nos movimentos do Pré-conhecimento:

![Imagem 9: 2. Algumas transportadoras somam o ICMS no cálculo do frete total, porém, realizam a distribuição do valor do imposto…](https://ajuda.sankhya.com.br/hc/article_attachments/44012608938647)

Neste caso, você deve acessar o caminho Cadastros gerais > Transportadoras > Transportadora (Empresa) e clicar no código da transportadora desejada. Na aba Cadastro localizar a opção Rateia ICMS por movimento, e marcar como sim. Configurando o cadastro da Transportadora (empresa) desta forma, independente do que estiver informado na Tabela de frete,o valor do ICMS será rateado nos componentes:

![Imagem 10: Neste caso, você deve acessar o caminho Cadastros gerais > Transportadoras > Transportadora (Empresa) e clicar no…](https://ajuda.sankhya.com.br/hc/article_attachments/44012609099671)

**Importante**: Quando a transportadora opta pelo rateio de ICMS por componente, não deve-se incluir na tabela o componente ICMS Destacado, mencionado na solução anterior. Caso ambas as opções estejam marcadas, o ICMS será somado duas vezes o total do movimento do Pré-conhecimento, tornando o cálculo divergente.

## Cálculo do ICMS incorreto

Algumas validações já indicadas anteriormente nas opções de ICMS não destacado ou não somado ao total do frete podem contribuir para a validação de cálculo de imposto divergente, como observar se o box do ICMS está marcado em todos os componentes que compuseram o cálculo do frete, entre outros.

1. Pedágio na base do ICMS: Algumas transportadoras não estão incluindo o Pedágio para cálculo do ICMS. Experimente acessar o caminho Cadastros gerais > Transportadoras > Negociações > Tabelas de frete, localizar o componente Pedágio, desmarcar o Calcular ICMS do componente e recalcular o Pré-conhecimento:

![Imagem 11: 1. Pedágio na base do ICMS: Algumas transportadoras não estão incluindo o Pedágio para cálculo do ICMS. Experimente…](https://ajuda.sankhya.com.br/hc/article_attachments/44012599935639)

Caso a situação for o contrário, o Componente Pedágio está com a opção de Calcular ICMS marcada, porém não está compondo a base de cálculo do ICMS, a origem pode estar no cadastro das Taxas Estaduais, mencionado no item '3' das instruções de ICMS não destacado. Acesse o caminho Cadastros Gerais > Configurações de Empresa> Taxas > Taxas Estaduais e verifique se a opção Calcular ICMS no pedágio está marcada:

![Imagem 12: Caso a situação for o contrário, o Componente Pedágio está com a opção de Calcular ICMS marcada, porém não está…](https://ajuda.sankhya.com.br/hc/article_attachments/44012629454871)

2. Alíquota de ICMS do Modal: algumas alíquotas interestaduais aplicadas no transporte com modal Aéreo e Rodoviário são diferentes. Caso a alíquota no movimento apresente divergência, acesse o Pré-conhecimento na aba Cadastro, e observe se o modal informado corresponde a alíquota aplicada:

![Imagem 13: 2. Alíquota de ICMS do Modal: algumas alíquotas interestaduais aplicadas no transporte com modal Aéreo e Rodoviário são…](https://ajuda.sankhya.com.br/hc/article_attachments/44012629561367)

3. Componente Total do Frete (quando estiver presente em uma tabela que contém nas Generalidades o componente ICMS destacado marcado): Algumas transportadoras trabalham com um tipo de negociação que realiza a cobrança total do frete partindo de um valor mínimo: para a rota 'X' ,caso a soma de todos os componentes ( Frete peso, Frete Valor, Pedágio, Gris, etc.) destacados nos movimentos do Pré-conhecimento totalize um valor menor do que o Componente Total do Frete + ICMS, o valor que será cobrado será o valor do Componente Total do Frete + ICMS.

Detalhamos o comportamento do Componente Total do Frete conforme o exemplo abaixo:

Os componentes de frete destacados ( Despacho, Frete Peso, Taxas, Frete Valor, Pedágio) + ICMS correspondente são somados, e o resultado desta soma é comparado com o Componente Total do Frete + ICMS.

Soma dos componentes destacados + ICMS    X     Componente Total do Frete

Se o resultado da soma for menor que o valor informado no componente **Total do Frete + ICMS** incluso na Tabela de frete, o valor de cobrança será o Total do Frete + ICMS.

A exibição deste componente no movimento ficará assim:

1. Na linha Total do Frete consta o valor do Componente + ICMS (Neste caso, R$ 123,68) . Atenção: o valor da cobrança, já com ICMS, é o valor que a transportadora informa na negociação de frete;
2. Na linha Total Frete ( terceira linha marcada de laranja na imagem): traz o valor da soma dos componentes destacados ( Despacho, Frete Peso, Taxas, Frete Valor, Pedágio), sem o ICMS proporcional (este será acrescido no final do cálculo);
3. Na linha Total do Frete Mínimo (segunda linha marcada de laranja na imagem): traz preenchido o valor da diferença entre o valor do Componente Total do Frete informado na tabela + ICMS ( R$ 115,02 + R$ 8,66 = R$ 123,68) e a soma dos componentes destacados (terceira linha marcada de laranja na imagem = R$ 49,60) ou seja: R$ 123,68 - R$ 49,60 = R$ 74,08;

![Imagem 14: Na linha Total do Frete Mínimo (segunda linha marcada de laranja na imagem): traz preenchido o valor da diferença entre…](https://ajuda.sankhya.com.br/hc/article_attachments/44012600169111)

## Exemplo do componente utilizado para calcular o movimento acima, cadastrado na tabela

![Imagem 15: Exemplo do componente utilizado para calcular o movimento acima, cadastrado na tabela](https://ajuda.sankhya.com.br/hc/article_attachments/44012629743511)

**Importante**: As transportadoras costumam indicar na negociação o valor final da tarifa, já com o ICMS calculado. Para que a Ferramenta Lincros calcule corretamente o ICMS neste caso, o valor informado no cadastro da Tabela de frete deve ser o valor da tarifa sem o ICMS. Isso ocorre porque o Componente Total do frete sobrepõe os demais, e serve de base de cálculo do ICMS destacado.

Para encontrar o valor sem imposto, basta realizar o seguinte cálculo: (Valor informado pela transportadora x ((100 - alíquota) / 10))

**Exemplo**:

Valor informado pela transportadora: R$ 123,68.

Alíquota ICMS: 7% >>>  100 - 7 / 100 = 0,93.

R$ 123,68 x 0,93 = R$ 115,02 >> Esse será o valor que deve ser informado na Tabela de frete.

**Obs**.: Nos CTe-s de **serviço**, onde a origem e destino são iguais, o ICMS não é calculado, e sim o ISS;

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos."
