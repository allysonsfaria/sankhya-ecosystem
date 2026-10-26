---
id: "4570924321943"
titulo: "Benefícios+: cadastro de benefícios e fórmulas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4570924321943-Benef%C3%ADcios-cadastro-de-benef%C3%ADcios-e-f%C3%B3rmulas"
trilha: "Manual do Produto > Pessoas+ > Benefícios > Lançamento e Cálculo dos Benefícios"
atualizado_em: "2026-09-27T18:38:35Z"
rotulos: ["Configuração", "Fórmulas", "Financeiro", "Pessoal", "br.com.sankhya.rh.FolhaBeneficios", "Benefícios +", "Pessoal +", "Cadastro de benefícios e fórmulas", "Sub-abas: Geral Fórmulas Funcionários", "Integração financeira e boas práticas", "Benefícios"]
---

# Benefícios+: cadastro de benefícios e fórmulas

```
 Módulo: Pessoal + > Cadastros          Versão disponível: A partir da 4.11
```

---

Após cadastrados os benefícios que serão oferecidos pelas empresas, é necessário informar como ele será calculado e processado junto ao financeiro. Para isso, realize nesta tela o cadastro dos **Benefícios+** que serão responsáveis pelos valores na integração financeira com a folha de pagamento e conheça as boas práticas para o cadastro de fórmulas em cada benefício.

| Cadastro e boas práticas de Benefícios |
| --- |
| [Cadastro Benefícios+](https://ajuda.sankhya.com.br/hc/pt-br/articles/4570924321943-Benef%C3%ADcios-cadastro-de-benef%C3%ADcios-e-f%C3%B3rmulas#CadastroBenef%C3%ADcios+) |
| [Boas práticas para cadastro de Fórmulas Benefícios+](https://ajuda.sankhya.com.br/hc/pt-br/articles/4570924321943-Benef%C3%ADcios-cadastro-de-benef%C3%ADcios-e-f%C3%B3rmulas#Boaspr%C3%A1ticasparacadastrodeF%C3%B3rmulasBenef%C3%ADcios+) |

---

![Imagem 1: Boas práticas para cadastro de Fórmulas Benefícios+](https://ajuda.sankhya.com.br/hc/article_attachments/17532916446999)

---

## Cadastro Benefícios+

Este cadastro se dá por meio das seguintes abas:

| [Aba Benefícios](https://ajuda.sankhya.com.br/hc/pt-br/articles/4570924321943-Benef%C3%ADcios-cadastro-de-benef%C3%ADcios-e-f%C3%B3rmulas#ababeneficios) | [Aba Agrupadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/4570924321943-Benef%C3%ADcios-cadastro-de-benef%C3%ADcios-e-f%C3%B3rmulas#abaagrupadores) |
| --- | --- |

### Aba Benefícios

Para adicionar um benefício, acione no botão ![Imagem 2: Para adicionar um benefício, acione no botão "Adicionar benefício" e observe que a tela irá dispor três sub-abas para…](https://ajuda.sankhya.com.br/hc/article_attachments/17532998335767) **"Adicionar benefício"** e observe que a tela irá dispor três sub-abas para configurações do mesmo.

#### Sub-aba Geral

Aqui serão adicionadas as informações gerais referente ao registro que está sendo incluso na tela.

![Imagem 3: Aqui serão adicionadas as informações gerais referente ao registro que está sendo incluso na tela.](https://ajuda.sankhya.com.br/hc/article_attachments/17533783577111)

**Informações Gerais**

Informe o **"Código"** e a **"Descrição"** do benefício.

Preencha o campo **"Valor Parte Empresa"** com o valor que será de responsabilidade da empresa, que será utilizado para apoio nas fórmulas de cálculo do benefício.

A marcação **"Desconta Afastamento?"** deve ser efetuada quando o benefício tiver uma dedução em períodos de afastamentos diversos pelo funcionário, por exemplo, se ele tiver um afastamento legal (auxílio doença, licença maternidade), o sistema fará o cálculo do benefício deduzindo esses dias. Lembrando que, atestados médicos não são considerados afastamentos, diante disso, se houver esse desconto, deverá ser incluído em fórmula.

Com a marcação **"Desconsiderar dias com carga < 6:00 horas"** ativada, não será realizado cálculo para funcionários que trabalham até seis horas diárias.

O **"Evento Beneficiário"** será utilizado para o valor da mensalidade, tanto para titular como para o dependente, se for um caso de plano de saúde ou odontológico, por exemplo. É importante atentar-se que nos casos de coparticipação de plano de saúde, deverá ser informado diretamente na [Central de Benefícios+](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015). Nos casos de benefícios como vale transporte, é necessária a criação de um evento neutro que vai trazer o valor zerado na folha, por ser um campo obrigatório na movimentação.

O campo **"Evento Empresa"** identificará a parte da empresa referente ao valor total do benefício, que será apresentado no cálculo do funcionário.

No campo **"Tipo Benefício"** localize o benefício cadastrado anteriormente na tela [Tipo de Benefício](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405110225175). Caso não tenha cadastrado, clique na seta disponível a frente do campo, para ser aberta a tela.

---

**Integração ao Financeiro**

Indique o **"Banco"** e a **"Conta Bancária"** que utilizará para fazer o pagamento do benefício.

O campo **"Centro de Resultado"** irá apontar para onde será o custo do benefício. Já, o campo **"Centro de Resultado Diferença"** identificará a diferença de um valor que seja exceção, ou seja, um valor que não estava programado, como, por exemplo, a segunda via de uma carteirinha. Caso não tenha nenhum centro de custo, insira o código zero.

Os campos **"Natureza"**, **"Parceiro Empresa"**, **"Projeto"**, **"Empresa para Integração Financeira"**, **"Tipo Operação"**, **"Tipo de Título"** e **"Fornecedor"** são para identificação e geração do pagamento no financeiro. Caso não possua informações específicas para os campos obrigatórios, preencha com o código zero.

---

#### Sub-aba Fórmulas

Nesta aba serão criadas as fórmulas para que sejam efetuados os lançamentos das partes empresa e funcionário.

![Imagem 4: Nesta aba serão criadas as fórmulas para que sejam efetuados os lançamentos das partes empresa e funcionário.](https://ajuda.sankhya.com.br/hc/article_attachments/17534363072151)

Utilize a **"Lista de Variáveis"** para a construção da fórmula do cálculo.

Em **"Fórmula do Valor"** e **"Fórmula do índice"** digite a fórmula de cálculo e, em seguida, clique no botão **"Compilar Fórmula"** e salve as informações.

Lembre-se ainda que, mesmo quando não houver uma edição, será preciso compilar a fórmula.

**Importante:** as fórmulas para o cálculo de benefícios precisam ser construídas com a variável EHBEN, com o valor parte beneficiário e valor para empresa: IF(EHBEN = ‘S’,S,N).

Após **Compilar Fórmula**, clique no botão ![Imagem 5: Após Compilar Fórmula , clique no botão "Salvar alterações" para habilitar a sub-aba Funcionários .](https://ajuda.sankhya.com.br/hc/article_attachments/17534875485335) **"Salvar alterações"** para habilitar a sub-aba **Funcionários**.

---

#### Sub-aba Funcionários

Nesta sub-aba, inclua ou remova os funcionários em benefícios específicos.

![Imagem 6: Nesta sub-aba, inclua ou remova os funcionários em benefícios específicos.](https://ajuda.sankhya.com.br/hc/article_attachments/17535014001559)

Para incluir funcionários, basta acionar o botão ![Imagem 7: Para incluir funcionários, basta acionar o botão "Adicionar funcionários" , selecionar os cards desejados e confirmar a…](https://ajuda.sankhya.com.br/hc/article_attachments/17532998335767) **"Adicionar funcionários"**, selecionar os cards desejados e confirmar a inclusão clicando em ![Imagem 8: Para incluir funcionários, basta acionar o botão "Adicionar funcionários" , selecionar os cards desejados e confirmar a…](https://ajuda.sankhya.com.br/hc/article_attachments/17534875485335) **"Inserir Funcionários"**.

Caso precise excluir funcionários beneficiários, ative o toogle de seleção, escolha o(s) funcionário(s) e acione o botão **"Remover funcionários do benefício"**.

[GIF animado: Imagem 9: Caso precise excluir funcionários beneficiários, ative o toogle de seleção, escolha o(s) funcionário(s) e acione o…](https://ajuda.sankhya.com.br/hc/article_attachments/21548390749463)

| ℹ️ **Sobre funcionários desligados e transferidos**  A sub-aba Funcionários não apresenta colaboradores desligados ou transferidos, mesmo que eles ainda estejam vinculados ao benefício.  Se você precisar consultar, incluir ou remover o vínculo de um colaborador desligado ou transferido, faça isso pela tela [**Central de Benefícios+**](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015), que contempla esses colaboradores. |
| --- |

---

#### Sub-aba Agrupadores

Esta sub-aba será habilitada somente para os benefícios que fazem parte de algum agrupador.

![Imagem 10: Esta sub-aba será habilitada somente para os benefícios que fazem parte de algum agrupador.](https://ajuda.sankhya.com.br/hc/article_attachments/17564280792215)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4570924321943-Benef%C3%ADcios-cadastro-de-benef%C3%ADcios-e-f%C3%B3rmulas#top)

### Aba Agrupadores

Aqui, pode-se visualizar os **Agrupadores** do qual o referido benefício está inserido, bem como, agrupá-los para determinados tomadores de serviços, por exemplo.

![Imagem 11: Aqui, pode-se visualizar os Agrupadores do qual o referido benefício está inserido, bem como, agrupá-los para…](https://ajuda.sankhya.com.br/hc/article_attachments/17536329787799)

Adicione os agrupadores por meio do botão **![Imagem 12: Adicione os agrupadores por meio do botão "Adicionar agrupador" , em seguida, informe uma "Descrição" para este e…](https://ajuda.sankhya.com.br/hc/article_attachments/17532998335767) "Adicionar agrupador"**, em seguida, informe uma **"Descrição"** para este e confirme. 

Depois, clique sobre o card do agrupador cadastrado para adicionar os benefícios e funcionários desejados.

---

#### Sub-aba Benefícios

Nesta sub-aba, acione o botão **"Adicionar benefícios ao agrupador"**, selecione o(s) card(s) do benefício que vai compor esse agrupador e salve.

[GIF animado: Imagem 13: Nesta sub-aba, acione o botão "Adicionar benefícios ao agrupador" , selecione o(s) card(s) do benefício que vai compor…](https://ajuda.sankhya.com.br/hc/article_attachments/21548579525527)

---

#### Sub-aba Funcionários

Em seguida, na aba **Funcionários**, acione o botão **"Adicionar funcionários ao agrupador"**, escolha os que vão participar e confirme-os.

![Imagem 14: Em seguida, na aba Funcionários , acione o botão "Adicionar funcionários ao agrupador" , escolha os que vão participar…](https://ajuda.sankhya.com.br/hc/article_attachments/17563830975127)

**Nota:** caso queira editar o nome do **Agrupador** criado, basta fazê-lo por meio do botão **"Editar agrupador"** presente no canto superior da tela. 

![Imagem 15: É importante lembrar que os agrupadores não são obrigatórios em seus cadastros, o intuito é facilitar a manutenção de…](https://ajuda.sankhya.com.br/hc/article_attachments/16457015943575) É importante lembrar que os agrupadores não são obrigatórios em seus cadastros, o intuito é facilitar a manutenção de lançamentos de benefícios para um mesmo grupo de funcionários.

Quando a inclusão de um benefício é realizada por **Agrupador**, no card do funcionário é apresentado o ícone **"Pertence ao agrupador X"**, e aqueles que foram adicionados por **Benefício** não terão esse ícone no respectivo card.

![Imagem 16: Quando a inclusão de um benefício é realizada por Agrupador , no card do funcionário é apresentado o ícone "Pertence ao…](https://ajuda.sankhya.com.br/hc/article_attachments/17564650477719)

Os benefícios poderão ser excluídos ou duplicados nesta tela, por meio dos botões **"Deletar Benefício"** e **"Duplicar Benefício"**, respectivamente. 

[GIF animado: Imagem 17: Os benefícios poderão ser excluídos ou duplicados nesta tela, por meio dos botões "Deletar Benefício" e "Duplicar…](https://ajuda.sankhya.com.br/hc/article_attachments/21548725559319)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4570924321943-Benef%C3%ADcios-cadastro-de-benef%C3%ADcios-e-f%C3%B3rmulas#top)

## Boas práticas para cadastro de Fórmulas Benefícios+

Para criação de fórmulas na **Central de Benefícios** é necessário entender o conceito geral da variável EHBEN, é bem simples:

**IF(EHBEN = 'S',** 

- Nesta primeira condição da pergunta **"Se é beneficiário?"**, deve-se criar a fórmula onde vai-se descontar do funcionário sua parcela do benefício;
- Na segunda condição, no caso a negativa de que não é beneficiário, entra a parte da fórmula em que a empresa arca com o valor do benefício.

Existe uma outra condição também que é a **SEQUÊNCIA**. 

Essa condição é usada praticamente em plano de saúde e odontológico, onde existe dependentes. A regra geral é que seja a **SEQUENCIA = 0** para titular, e se for **SEQUENCIA > 0**, ou seja, maior que 0, é sempre um dependente, por exemplo:

```
IF(EHBEN = 'S',
IF(SEQUENCIA > 0,
```

Aqui, trata-se de dois fatores:

- **1ª condição:** a primeira parte é onde entrará o desconto do beneficiário (funcionário), agora dentro da condição de que a SEQUENCIA é maior que 0, ou seja, quem entrar aqui com certeza é um dependente, então deve-se criar a condição para desconto do dependente;
- **2ª condição:** da SEQUENCIA, é uma lógica, se não for maior que 0, é 0, então é titular, deve-se por aqui a condição de desconto para o titular.

Na condição negativa, de que não é um beneficiário, a partir desse ponto tudo será custeado pela empresa.

Outro exemplo mais simples:

```
IF(EHBEN = 'S',
IF(SEQUENCIA > 0,
```

Desconto do Dependente,

Desconto do Titular,

Desconto Parte Empresa.

---

### Vale transporte/ Vale alimentação

De regra geral tem-se uma função **"DiasTrabProximaReferencia"**, que calcula os dias úteis que serão trabalhados analisando algumas variações: **Carga horária**, **Feriados**, **Afastamentos** e **Férias**. Através dessa composição, a função determina quantos dias úteis o funcionário irá trabalhar e com isso pode-se chegar ao valor do vale.

```
DiasTrabProximaReferencia(CODEMP, CODFUNC, DTOC(REFERENCIA))
```

---

Exemplos:

![Imagem 18: Sem desconto do valor de recarga:](https://ajuda.sankhya.com.br/hc/article_attachments/16456999097495) Sem desconto do valor de recarga:

```
IF(EHBEN = 'S',0,(PDES('VALOR','TFPVAL','CODEMP='+STR(CODEMP)+' AND CODFUNC='+STR
(CODFUNC)+' AND TIPO="T"') * PDES('PASSESDIA','TFPVAL','CODEMP='+STR(CODEMP)+' AND
 CODFUNC='+STR(CODFUNC)+'AND TIPO="T"')) * DiasTrabProximaReferencia(CODEMP,
CODFUNC, DTOC(REFERENCIA)))
```

Desmistificando:

```
IF(EHBEN = 'S',0,
```

Nesse caso, o funcionário não terá desconto algum.

**PDES('VALOR','TFPVAL','CODEMP='+STR(CODEMP)+' AND CODFUNC='+STR(CODFUNC)+' AND TIPO="T"')**, uma estrutura de PDES para buscar da tabela TFPVAL (Onde cadastra-se os optantes pelo Vale Transporte / Alimentação), o campo VALOR. Ou seja, o valor diário do VT.

**PDES('PASSESDIA','TFPVAL','CODEMP='+STR(CODEMP)+' AND CODFUNC='+STR(CODFUNC)+'AND TIPO='T''')**, muda-se apenas do campo VALOR para buscar o campo PASSESDIA, ou seja, a quantidade diária de passes.

```
DiasTrabProximaReferencia(CODEMP, CODFUNC, DTOC(REFERENCIA))
```

Como já citado, a função que calcula os dias úteis trabalhados.

Então:

```
(PDES 1 * PDES 2) * DIAS ÚTEIS.
```

![Imagem 19: Descontando faltas e atestados do valor de recarga:](https://ajuda.sankhya.com.br/hc/article_attachments/16456999103127) Descontando faltas e atestados do valor de recarga:

Como esse caso também é comum nos nossos parceiros, tem-se duas funções nativas que já faz essa leitura:

```
FBM(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&REFERE,'M','102','I')
```

É uma função em que busca do movimento do funcionário, a quantidade do índice do evento 102. Ou seja, ao preencher a rotina de faltas, o movimento é preenchido automaticamente, e essa função busca de lá essa quantidade.

```
FDiasAbsenteismo(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&REFERE,'T')
```

É uma função que busca os atestados médicos lançados na referência da recarga. 

Mas tem uma diferença, ela analisa exatamente a quantidade de atestados que corresponde a carga horária do funcionário, pois atestados lançados em dias não úteis não são levados em consideração para abatimento da recarga.

```
IF(EHBEN = 'S',0,(PDES('VALOR','TFPVAL','CODEMP='+STR(CODEMP)+' AND CODFUNC='+STR
(CODFUNC) + ' AND TIPO="T"') * PDES('PASSESDIA','TFPVAL','CODEMP='+STR(CODEMP)+'
 AND CODFUNC='+STR(CODFUNC)+' AND TIPO="T"')) * (DiasTrabProximaReferencia(CODEMP,
CODFUNC, DTOC(REFERENCIA))) - (FBM(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,
&REFERE,'M','102','I') + FDiasAbsenteismo(QueFuncionario.CODEMP,QueFuncionario.
CODFUNC,&REFERE,'T')))
```

A única diferença aqui é que pega a:

```
DiasTrabProximaReferencia(CODEMP, CODFUNC, DTOC(REFERENCIA))
```

E subtrai os dias úteis encontrados pela soma das faltas e atestados ou seja: 

```
DiasTrabProximaReferencia(CODEMP, CODFUNC, DTOC(REFERENCIA)) -
(FBM(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&REFERE,'M','102','I')+FDiasAbsenteismo
(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&REFERE,'T'))
```

Se o funcionário teria 22 dias úteis, mas tem 3 faltas e 2 dias úteis de atestado, ele ficará com uma recarga de 17 dias.

O que muda para o VA, é que nos PDES utilizados para buscar da TFPVAL o valor e a quantidade, o  TIPO='A'. 

- **A** = Alimentação;
- **T** = Transporte.

---

### Plano de saúde/odontológico

De maneira geral, para a regra de saúde usa-se três artifícios: 

1. A função **"fValorConvenio"** (Análise de Titular)
2. **"fValorConvenioDPD"** (Análise de dependente)
3. E uma **"Tabela de Faixa"**.

```
fValorConvenioDPD(CODEMP,CODFUNC,99,99,DTOC(REFERENCIA),'A',SEQUENCIA)
```

```
fValorConvenio(CODEMP,CODFUNC,99,99,DTOC(REFERENCIA),'A','S')
```

Pode-se perceber aqui que temos o 3º e 4º parâmetro, 99 e 99. Respectivamente se referem a: Qual tabela de faixa? E qual o número da faixa?

Uma [tabela de faixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405167002519) é uma rotina usada em diversos casos onde se quer armazenar valores e posteriormente, buscá-los para que algum cálculo seja efetuado. Nesse caso, comumente nossos parceiros possuem para desconto de plano de saúde através de faixa etária, como segue um exemplo de cadastro:

![Imagem 20: Uma tabela de faixa é uma rotina usada em diversos casos onde se quer armazenar valores e posteriormente, buscá-los…](https://ajuda.sankhya.com.br/hc/article_attachments/17613000685719)

- **Limite da Faixa:** é onde informa a idade;
- **Valor (1,2,3):**  informa-se o valor da mensalidade daquela faixa.

O trabalho das nossas funções fValorConvenio (Análise de títular) e fValorConvenioDPD (Análise de dependente) é justamente avaliar essa tabela de faixa, olhar a idade do funcionário e/ou dependente, e aplicar a tabela de faixa para trazer o valor.

Entendido isso, observe os exemplos:

![Imagem 21: É comum a empresa arcar com 100% do plano do titular, e o titular arcar com 100% de seus dependentes.](https://ajuda.sankhya.com.br/hc/article_attachments/16456999097495) É comum a empresa arcar com 100% do plano do titular, e o titular arcar com 100% de seus dependentes. 

Aqui podemos observar que na parte do beneficiário, quando a SEQUENCIA for maior que 0, ou seja, dependente, vai-se descontar totalmente o valor encontrado, e quando não for, será 0, pois será o titular. (Por isso a ",0"). 

```
IF(EHBEN = 'S',
IF(SEQUENCIA > 0,
fValorConvenioDPD(CODEMP,CODFUNC,100,1,DTOC(REFERENCIA),'A',SEQUENCIA),0)
```

Agora, na parte da empresa, observe que se a SEQUENCIA for maior que 0, ou seja, dependente, é 0, pois a empresa não arca com nada.

```
IF(SEQUENCIA > 0,0,
fValorConvenio(CODEMP,CODFUNC,100,1,DTOC(REFERENCIA),'A','S')))
```

Caso contrário, titular, a empresa arca com 100%.

![Imagem 22: Um outro cenário é quando a empresa arca com um determinado % (exemplo 50%) do valor do plano para o titular, mas ele…](https://ajuda.sankhya.com.br/hc/article_attachments/16456999103127) Um outro cenário é quando a empresa arca com um determinado % (exemplo 50%) do valor do plano para o titular, mas ele ainda continua arcando 100% para seus dependentes:

```
IF(EHBEN = 'S',
IF(SEQUENCIA > 0,
fValorConvenioDPD(CODEMP,CODFUNC,100,1,DTOC(REFERENCIA),'A',SEQUENCIA),
fValorConvenio(CODEMP,CODFUNC,100,1,DTOC(REFERENCIA),'A','S') * 0.50),
IF(SEQUENCIA > 0,0,
fValorConvenio(CODEMP,CODFUNC,100,1,DTOC(REFERENCIA),'A','S') * 0.50))
```

Aqui, pode-se perceber que a condição do beneficiário na parte do dependente se mantém: 

```
IF(EHBEN = 'S',
IF(SEQUENCIA > 0,
fValorConvenioDPD(CODEMP,CODFUNC,100,1,DTOC(REFERENCIA),'A',SEQUENCIA),
```

Agora na parte do titular, tem uma nova função em que seu resultado fica 50% do valor retornando:

```
fValorConvenio(CODEMP,CODFUNC,100,1,DTOC(REFERENCIA),'A','S') * 0.50),
```

E, na parte empresa, para dependente também se mantém:

```
IF(SEQUENCIA > 0,0,
```

Porém para o titular a empresa está arcando com outros 50%:

```
fValorConvenio(CODEMP,CODFUNC,100,1,DTOC(REFERENCIA),'A','S') * 0.50)).
```

![Imagem 23: Um outro cenário é quando a empresa arca com um determinado %, tanto para o titular quanto para o dependente. Não é…](https://ajuda.sankhya.com.br/hc/article_attachments/16456999106199) Um outro cenário é quando a empresa arca com um determinado %, tanto para o titular quanto para o dependente. Não é muito habitual, mas pode acontecer (exemplo 50%).

```
IF(EHBEN = 'S',
IF(SEQUENCIA > 0,
```

```
fValorConvenioDPD(CODEMP,CODFUNC,100,1,DTOC(REFERENCIA),'A',SEQUENCIA) * 0.50,
fValorConvenio(CODEMP,CODFUNC,100,1,DTOC(REFERENCIA),'A','S') * 0.50),
IF(SEQUENCIA > 0,fValorConvenioDPD(CODEMP,CODFUNC,100,1,DTOC(REFERENCIA),'A',
SEQUENCIA) * 0.50, fValorConvenio(CODEMP,CODFUNC,100,1,DTOC(REFERENCIA),'A','S')
* 0.50))
```

Pode-se observar aqui, que a única diferença é que na parte tanto do beneficiário quanto da parte empresa, entra agora:

```
fValorConvenioDPD(CODEMP,CODFUNC,100,1,DTOC(REFERENCIA),'A',SEQUENCIA) * 0.50
```

Que ao invés de descontar o valor total encontrado via tabela de faixa, aplica apenas 50% dele.

A **Fórmula do Valor** para o cálculo do **Trintídio - Lei 7238/84 - artigo 9º** é a seguinte:

```
IF((&CAUAFA = 60),IF(MES(DTOC(&DTDEMISSAO + IF(&TIPOAVISO = 2, &DIAAVI, 0)))
= IF((quePrefSindicato.MESDATABASE - 1) = 0, 12, quePrefSindicato.MESDATABASE - 1),
(queFuncionario.SALBASE + &VLRINCORPORA), 0),0)
```

E a **Fórmula do Índice**:

```
&DIAAVI
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4570924321943-Benef%C3%ADcios-cadastro-de-benef%C3%ADcios-e-f%C3%B3rmulas#top)
