---
id: "360056603434"
titulo: "Configuração de Transições - Nova"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360056603434-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es-Nova"
trilha: "Manual do Produto > Produção > Produção/W - Nova"
atualizado_em: "2026-07-29T15:11:51Z"
rotulos: ["Configuração", "Estoque", "Processo Produtivo", "Produção", "Configuração de transições: duplo clique pop-up", "Filtros: produto acabado estoque MP setup centro", "Aba Geral: ordem expressão condição", "Transições"]
---

# Configuração de Transições - Nova

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313368683287)Módulo:Produção>Cadastros>Processo Produtivo-Botão Roteiro-Configuração de Transições
```

---

Outro ponto de extrema importância na construção do Fluxo do Processo Produtivo, derivado das formatações realizadas através do [Botão Roteiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058453293-Bot%C3%A3o-Roteiro-Processo-Produtivo-Nova), é a configuração das transições do fluxo, onde o sistema permite a realização de tal configuração a partir de um duplo clique sobre as mesmas (as transições são as setas contínuas que ligam os elementos do fluxo). Assim, será exibido o pop-up **"Configuração de Transição"**.

[Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056603434-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es-Nova#abageral)                                                                   [Aba Filtros de Transições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056603434-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es-Nova#abafiltrosdetransies)

![Imagem 2: Aba Geral Aba Filtros de Transições](https://ajuda.sankhya.com.br/hc/article_attachments/360098436193)

## Aba Geral

Esta aba tem por objetivo, a determinação das configurações gerais das transições entre as atividades, que irão de fato estabelecer o fluxo que o processo deverá seguir em tempo de execução.

A marcação **"Padrão"** determina que a transição em questão é a referência no caso de todas as condições falharem.

Aponte por meio do campo **"Ordem"**, a sequência de avaliação da transição, sendo que, o mesmo deverá ser utilizado somente quando a transição participar de um Gateway do tipo Exclusivo, onde a primeira transição verdadeira faz com que siga o fluxo.

O espaço do campo **"Expressão"** é destinado à determinar uma condição que torne a transição executável. Este deverá ser utilizado somente quando a transição for condicional. Você deve utilizar uma expressão escrita em **"Java Script"**.

**Nota:** é importante lembrar que, durante a execução de OP's do Processo, essa expressão será executada assim que o Gateway (ponto de decisão) à qual ela esteja ligada seja atingido. O resultado da execução esperado é verdadeiro (true = 1) ou falso (false = 0). A expressão da Transição será utilizada em conjunto com os filtros de transições, utilizando o operador de adição AND:

(Expressão javaScript aba Geral) && Filtros de Transição (transição 1511)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056603434-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es-Nova#top)

## Aba Filtros de Transições

Nesta aba, definimos os filtros que serão avaliados na transição. Estes filtros deverão ser utilizados somente em situações em que transições condicionais são aceitas. Determine no campo **"Tipo"**, a espécie de filtro de transição a ser utilizado, sendo que, cada possibilidade quando acionada, apresentará seus respectivos campos de acompanhamento. Vejamos abaixo a descrição de cada uma delas:

[Produto Acabado em Processamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056603434-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es-Nova#produtoacabadoemprocessamento)                                        [Estoque Disponível de MP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056603434-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es-Nova#estoquedisponveldemp)

[Necessidade de Setup para Centro de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056603434-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es-Nova#necessidadedesetupparacentrodetrabalho)                     [Condição Personalizada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056603434-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es-Nova#condiopersonalizada)

![Imagem 3: Necessidade de Setup para Centro de Trabalho Condição Personalizada](https://ajuda.sankhya.com.br/hc/article_attachments/360098436673)

**Produto Acabado em Processamento**

Será conveniente o uso desta opção, quando o Produto Acabado estiver em processamento na instância do processo. Nesse caso, é obrigatória a seleção de um produto no campo **"Produto (PA)"**.

Utilize o campo **"Produto (PA)"** para determinar qual Produto Acabado deve estar em processamento na instância do processo para execução do filtro. Quando se deseja que o filtro seja avaliado para qualquer Produto Acabado que esteja sendo processado, este campo não deve ser utilizado.

Informe no campo **"Controle (PA)"** o controle do produto selecionado. Apenas será exibido quando o Produto Acabado possuir controle adicional por lista.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056603434-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es-Nova#abafiltrosdetransies)

**Estoque Disponível de MP**

Esta opção será apropriada, quando a Matéria-Prima possuir estoque disponível conforme necessidade listada na atividade base. Caso necessário, é possível definir uma expressão que busca a quantidade de estoque no campo **"Expressão"**. Essa Matéria-Prima pode ser também um Produto Intermediário e, nestes casos, a atividade base é um sub-processo de produção.

O campo **"Atividade Base"** deve ser utilizado para especificar a atividade que será empregada como base da operação. Seu preenchimento se torna obrigatório, apenas quando o tipo do filtro for **"Estoque disponível de MP"** ou **"Necessidade de Setup para Centro de Trabalho"**.

Utilize o campo **"Matéria-Prima"** para especificar qual Matéria-Prima deve ter o estoque avaliado. Não sendo este campo preenchido, todas as Matérias-Primas necessárias na atividade base serão avaliadas, conforme marcação **"Valida estoque em transições condicionais"** na lista de materiais. Deve ser utilizado somente quando o tipo do filtro for **"Estoque disponível de MP"**.

O campo **"Controle (MP)"** será exibido para preenchimento, quando a matéria-prima selecionada possuir controle adicional por lista. É um campo a ser utilizado para especificar o controle da matéria-prima que deve ter o estoque avaliado.

Informe no campo **"Empresa"** a empresa que será utilizada para busca do estoque. Não sendo informada uma empresa neste campo, será utilizada a mesma do processo de produção.

Determine o **"Local"** onde deve-se checar o estoque.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056603434-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es-Nova#abafiltrosdetransies)

**Necessidade de Setup para Centro de Trabalho**

O uso desta opção se justifica, se o Centro de Trabalho em uso na atividade base sempre exigir setup, ou quando condicional, o setup atual for incompatível com o Produto Acabado em processamento.

O campo **"Atividade Base"** deve ser utilizado para especificar a atividade que será empregada como base da operação. Seu preenchimento se torna obrigatório, apenas quando o tipo do filtro for **"Estoque disponível de MP"** ou **"Necessidade de Setup para Centro de Trabalho"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056603434-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es-Nova#abafiltrosdetransies)

**Condição Personalizada**

A utilização desta opção será válida, se a expressão especificada no campo **"Expressão"** retornar linha onde a primeira coluna seja numérica com valor maior que zero.

No campo **"Expressão"**, defina uma expressão em SQL que deverá retornar uma linha com uma coluna numérica. Caso o valor seja igual a **"0"**, a expressão será considerada falsa, caso contrário será verdadeira. O sistema vai injetar os seguintes parâmetros na consulta:

- CODPRODPA
- CONTROLEPA
- CODPRODMP
- CONTROLEMP
- CODEMP
- CODLOCAL
- IDPROC

**Observações:**

Os filtros de transições são avaliados de forma agrupada ao tipo do filtro (Produto Acabado, Estoque Disponível de MP, Necessidade de Setup para o Centro de Trabalho e Condição personalizada) considerando OR para cada filtro do mesmo grupo, ou seja, se qualquer uma das expressões do grupo retornar verdadeiro (true = 1), então o grupo resulta em verdade.

Os grupos são avaliados considerando AND, ou seja, o resultado da Transição será verdadeiro, apenas se todos os grupos existentes resultarem em verdadeiro (true = 1). Vejamos um exemplo:

P - Produto Acabado = { true , false , false } -> resultado do grupo P = 'true';

S - Expressão Personalizada = { false, false } -> resultado do grupo S = 'false';

Resultado da Transição, neste exemplo será 'false', pois o grupo S é false.

Para as expressões personalizadas do filtro de transição, estão disponíveis alguns parâmetro para uso, são eles:

**:IDPROC -** Código de identificação do Processo Produtivo.

**:IDIPROC -** Nro da Ordem de Produção.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056603434-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es-Nova#abafiltrosdetransies) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056603434-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es-Nova#top)
