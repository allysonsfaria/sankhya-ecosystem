---
id: "44010081633047"
titulo: "[TMS] - Validações para Auditoria de Frete"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010081633047--TMS-Valida%C3%A7%C3%B5es-para-Auditoria-de-Frete"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:30:07Z"
rotulos: ["sync_hc", "lincros", "lincros_13433437", "sync_hash_8936d10cbd2c"]
---

# [TMS] - Validações para Auditoria de Frete

**Menu**: Operacional > Cargas > Pré-conhecimentos

Cadastros Gerais > Transportadoras >  Negociações > Tabelas de Frete

Operacional > Processos > Auditoria de fretes

**Objetivo**: Auxiliar na auditoria de fretes, realizando as principais validações para auditar um CT-e em algumas situações

**Considerações**:

- CT-e sem erro de importação;
- Possuir tabela de frete cadastradas ou possuir Cotação Spot confirmada;

## Situações

## -> Pré-conhecimento não encontra tabela (validação realizada dentro da tabela de fretes):

Em casos onde o pré-conhecimento não encontra a tabela de frete a qual deveria se vincular, é importante realizar algumas validações:

- Se a tabela em questão está deferida (aprovada);
- A data de vigência da tabela: Deve ser anterior à emissão da Nota Fiscal;
- Se a tabela está ativa;
- O tipo de negociação (Pré-conhecimento, embarque ou ambos): Uma tabela do tipo Embarque não será encontrada por um CT-e de carga fracionada e vice-versa. É importante ressaltar que o cálculo de embarque deve ser realizado dentro do próprio embarque, e o pré-conhecimento deve estar vinculado ao embarque para encontrar tabela, portanto as validações para embarque serão tratadas em outro artigo.

![Imagem 1: O tipo de negociação (Pré-conhecimento, embarque ou ambos): Uma tabela do tipo Embarque não será encontrada por um CT-e…](https://ajuda.sankhya.com.br/hc/article_attachments/44010059975575)

Em seguida, ao acessar a aba de restrições, é importante verificar se a tabela não possui nenhuma informação que faça com que o pré-conhecimento não seja atendido. Basta selecionar alguma das guias para confirmar a informação. As restrições podem ser por modal, por pessoas, por grupo de veículos ou por produtos.

![Imagem 2: Em seguida, ao acessar a aba de restrições, é importante verificar se a tabela não possui nenhuma informação que faça…](https://ajuda.sankhya.com.br/hc/article_attachments/44010082048151)

Também é importante verificar o tipo de restrição, visto que o tipo de restrição pode ser por atendimento, por exclusividade ou restrita.

Quando o símbolo for verde, significa que essa tabela atende apenas àquele tipo específico de modal, pessoa, veículo ou produto.

![Imagem 3: Quando o símbolo for verde, significa que essa tabela atende apenas àquele tipo específico de modal, pessoa, veículo ou…](https://ajuda.sankhya.com.br/hc/article_attachments/44010082218775)

Quando o símbolo for amarelo, significa que apenas essa tabela atende àquele tipo específico de modal, pessoa, veículo ou produto.

![Imagem 4: Quando o símbolo for amarelo, significa que apenas essa tabela atende àquele tipo específico de modal, pessoa, veículo…](https://ajuda.sankhya.com.br/hc/article_attachments/44010064293015)

Quando o símbolo for cinza, significa que essa tabela não atende àquele tipo específico de modal, pessoa, veículo ou produto.

![Imagem 5: Quando o símbolo for cinza, significa que essa tabela não atende àquele tipo específico de modal, pessoa, veículo ou…](https://ajuda.sankhya.com.br/hc/article_attachments/44010094186519)

Além das restrições, é necessário verificar também se a localidade informada no pré-conhecimento consta na rota da tabela. É possível fazer isso acessando a aba Componentes por rota, selecionando a rota desejada e clicando em editar:

![Imagem 6: Além das restrições, é necessário verificar também se a localidade informada no pré-conhecimento consta na rota da…](https://ajuda.sankhya.com.br/hc/article_attachments/44010091575191)

Em seguida, verificar a localidade do destino. Se for uma única localidade, basta compará-la. Também já é possível identificar se a rota está ativa ou não. Caso possua uma região como destino, selecionar o lápis de edição:

![Imagem 7: Em seguida, verificar a localidade do destino. Se for uma única localidade, basta compará-la. Também já é possível…](https://ajuda.sankhya.com.br/hc/article_attachments/44010091719191)

Uma nova janela abrirá, lá é possível verificar as localizações que compõe a região, bem como localizações restritas daquela região. Também é possível identificar se a rota está ativa ou não.

![Imagem 8: Uma nova janela abrirá, lá é possível verificar as localizações que compõe a região, bem como localizações restritas…](https://ajuda.sankhya.com.br/hc/article_attachments/44010102332055)

Outra informação à ser validada é se as faixas de peso atendem ao informado no pré-conhecimento:

![Imagem 9: Outra informação à ser validada é se as faixas de peso atendem ao informado no pré-conhecimento:](https://ajuda.sankhya.com.br/hc/article_attachments/44010065091735)

**Importante**: A faixa de peso excedente sempre deve iniciar com 0Kg.

Além disso, dentro do pré-conhecimento, é preciso validar se este possui marcadores:

![Imagem 10: Além disso, dentro do pré-conhecimento, é preciso validar se este possui marcadores:](https://ajuda.sankhya.com.br/hc/article_attachments/44010065232919)

É importante salientar que uma tabela de frete que contém marcadores busca pré-conhecimentos sem marcadores. Porém, um pré-conhecimento com marcadores só irá buscar tabelas que contenham os mesmos marcadores.

O tipo de pré-conhecimento também influencia na busca da tabela. Se for um pré-conhecimento do tipo devolução ou reentrega, é necessário possuir o componente informado na tabela de fretes:

![Imagem 11: O tipo de pré-conhecimento também influencia na busca da tabela. Se for um pré-conhecimento do tipo devolução ou…](https://ajuda.sankhya.com.br/hc/article_attachments/44010092394775)

![Imagem 12: O tipo de pré-conhecimento também influencia na busca da tabela. Se for um pré-conhecimento do tipo devolução ou…](https://ajuda.sankhya.com.br/hc/article_attachments/44010095278231)

Para mais informações sobre o tema, é possível acessar este arquivo:

É importante verificar também, caso seja uma devolução, se a rota em questão é bidirecional.

![Imagem 13: É importante verificar também, caso seja uma devolução, se a rota em questão é bidirecional.](https://ajuda.sankhya.com.br/hc/article_attachments/44010092696471)

A forma de negociação é outro ponto a ser analisado. Caso você não seja o pagador do frete, a tabela não será encontrada. Por exemplo: A nota está com o tipo de frete FOB e você é o emissor da nota fiscal.

**Frete CIF**: pago pelo emissor da nota fiscal;

**Frete FOB**: pago pelo destinatário da nota fiscal.

![Imagem 14: Frete FOB : pago pelo destinatário da nota fiscal.](https://ajuda.sankhya.com.br/hc/article_attachments/44010095570455)

## De/Para de componentes

Muitas vezes é difícil realizar a auditoria de fretes se os componentes não são equiparados. Isso significa fazer o De/Para dos mesmos, que nada mais é do que informar que um componente que a transportadora chama de ABC é a mesma coisa que está cadastrada no sistema como 123. Portanto, é muito importante realizar o De/Para para auxiliar na auditoria.

![Imagem 15: Muitas vezes é difícil realizar a auditoria de fretes se os componentes não são equiparados. Isso significa fazer o…](https://ajuda.sankhya.com.br/hc/article_attachments/44010103286551)

É importante lembrar que, caso o componente não possua o de/para, ele também será exibido movimento do pré-conhecimento. O componente informado pela transportadora aparecerá como componente não encontrado na tabela de frete e o valor aparecerá na coluna do valor realizado.

![Imagem 16: É importante lembrar que, caso o componente não possua o de/para, ele também será exibido movimento do…](https://ajuda.sankhya.com.br/hc/article_attachments/44010112804375)

## Cálculo Incorreto

## -> Tipo do Pré-conhecimento:

Verificar se o tipo do pré-conhecimento condiz com o cálculo da tabela. Conforme descrito anteriormente, pré-conhecimentos de devolução ou reentrega não possuem o mesmo valor que conhecimentos normais. Pré-conhecimentos do tipo complementar cobram apenas Frete Peso e ICMS.

![Imagem 17: Verificar se o tipo do pré-conhecimento condiz com o cálculo da tabela. Conforme descrito anteriormente,…](https://ajuda.sankhya.com.br/hc/article_attachments/44010093262487)

![Imagem 18: Verificar se o tipo do pré-conhecimento condiz com o cálculo da tabela. Conforme descrito anteriormente,…](https://ajuda.sankhya.com.br/hc/article_attachments/44010113066391)

## -> Componentes não cadastrados na faixa de cálculo:

Se o pré-conhecimento não encontra o valor mínimo ou o componente esperado mesmo com a tabela correta vinculada, verifique se os componentes foram cadastrados na faixa de cálculo correspondente à rota. Isso é diferente de "componente ausente na tabela" — o componente pode existir na tabela, mas não estar associado à faixa específica que o pré-conhecimento está usando. Acesse Cadastros Gerais > Transportadoras > Negociações > Tabelas de Frete, edite a rota, e confirme que os componentes desejados estão incluídos na faixa de peso/valor em uso.

## -> Lacuna entre faixas de peso ("Componente fora da tabela de negociações"):

Se o frete peso não é calculado e a auditoria exibe "Componente fora da tabela de negociações", confira as faixas de peso da tabela de frete da transportadora, na rota do pré-conhecimento. Se houver lacuna entre uma faixa e a seguinte, um peso que caia nessa lacuna não é atendido por nenhum componente.

Exemplo: faixas de 41,0000 a 60,0000 kg e de 61,0000 a 100,0000 kg. Um peso de 60,80 kg fica fora das duas faixas e o frete peso não é calculado.

Para corrigir, ajuste o limite da faixa seguinte para fechar a lacuna sem sobreposição (por exemplo, 60,0001 a 100,0000 kg), desde que esteja de acordo com o combinado com a transportadora. Depois, salve a tabela e recalcule o pré-conhecimento.

## ICMS

Existe uma documentação própria para validar as principais divergências sobre ICMS. Você pode visualizá-la [clicando aqui](https://lincros.movidesk.com/kb/article/68376/auditoria-calculo-icms%20).

## CEP de Origem/Destino

É importante verificar se o CEP informado no CT-e está correto. Quando a plataforma não encontra o CEP, ela gera um CEP genérico no pré-conhecimento, dessa forma a rota fica incorreta na tabela. É possível confirmar o CEP dentro do [site dos correios](http://www.buscacep.correios.com.br/sistemas/buscacep/buscaCepEndereco.cfm). Para corrigir, basta alterar o campo de destino do pré-conhecimento, salvar e recalcular o frete.

## Peso

É importante validar se o peso considerado para cálculo está correto. Por padrão, o sistema busca o peso e a cubagem informados na Nota Fiscal.

A Plataforma grava esses dados no pré-conhecimento e realiza o cálculo do peso cubado.

![Imagem 19: A Plataforma grava esses dados no pré-conhecimento e realiza o cálculo do peso cubado.](https://ajuda.sankhya.com.br/hc/article_attachments/44010096271255)

O cálculo realizado é Metros Cúbicos X Fator de Cubagem. O Fator de Cubagem é buscado, inicialmente, na tabela de frete, o campo Cubagem Utilizada:

![Imagem 20: O cálculo realizado é Metros Cúbicos X Fator de Cubagem. O Fator de Cubagem é buscado, inicialmente, na tabela de…](https://ajuda.sankhya.com.br/hc/article_attachments/44010096407703)

Caso não possua o componente cadastrado, é buscado na Transportadora (Empresa):

![Imagem 21: Caso não possua o componente cadastrado, é buscado na Transportadora (Empresa):](https://ajuda.sankhya.com.br/hc/article_attachments/44010127496855)

Caso não possua valor cadastrado, o sistema assume por padrão o fator de cubagem como 300.

Efetuado o cálculo do peso cubado, o sistema valida qual das informações é maior (peso cubado ou peso) para então fazer o cálculo do valor do frete com base no peso escolhido.

Existe um componente na tabela de frete chamado cubagem mínima. Caso a tabela possua esse componente, o peso cubado só será calculado se o valor dos metros cúbicos for maior do que o informado no componente.

![Imagem 22: Existe um componente na tabela de frete chamado cubagem mínima. Caso a tabela possua esse componente, o peso cubado só…](https://ajuda.sankhya.com.br/hc/article_attachments/44010066944791)

Há uma configuração que pode ser realizada para que o cálculo se baseie nas informações do CT-e, ao invés da NF-e. É possível solicitar que seja configurado esse parâmetro pela equipe de Help Desk. Caso seja necessário esse parâmetro para apenas algumas transportadoras, é possível acessar o menu: Cadastros Gerais > Transportadoras> Transportadora (empresa) e selecionar a transportadora desejada. Nas configurações da empresa, marcar as TAGs Considerar cubagem do CT-e e Considerar peso do CT-e. Em seguida salvar a edição.

![Imagem 23: Há uma configuração que pode ser realizada para que o cálculo se baseie nas informações do CT-e, ao invés da NF-e. É…](https://ajuda.sankhya.com.br/hc/article_attachments/44010118937623)

## Quantidade notas referenciadas no CT-e

Para verificar se o cálculo está correto, é importante validar se todas as NF-es estão mencionadas no CT-e. Para tanto, basta acessar o CT-e (Documentos Eletrônicos > CT-es) e conferir quais as notas referenciadas no mesmo:

![Imagem 24: Para verificar se o cálculo está correto, é importante validar se todas as NF-es estão mencionadas no CT-e. Para tanto,…](https://ajuda.sankhya.com.br/hc/article_attachments/44010119053591)

## TRT/TDE

Taxas como TRT e TDE devem estar cadastradas na tabela para que contabilizem no movimento. A Taxa TRT é relacionada a localidade, portanto, basta verificar se possui uma rota que possui todas as localidades que fazem parte dessa rota:

![Imagem 25: Taxas como TRT e TDE devem estar cadastradas na tabela para que contabilizem no movimento. A Taxa TRT é relacionada a…](https://ajuda.sankhya.com.br/hc/article_attachments/44010097158551)

Já em caso da taxa TDE,onde a restrição é por pessoa, o ideal é utilizar a aba de componente com restrição, incluir o valor e vincular as pessoas correspondentes. Também é possível que a tabela seja restrita por pessoa. Incluir pessoas nessa aba restringe toda a tabela apenas a elas.

![Imagem 26: Já em caso da taxa TDE,onde a restrição é por pessoa, o ideal é utilizar a aba de componente com restrição, incluir o…](https://ajuda.sankhya.com.br/hc/article_attachments/44010128193303)

![Imagem 27: Já em caso da taxa TDE,onde a restrição é por pessoa, o ideal é utilizar a aba de componente com restrição, incluir o…](https://ajuda.sankhya.com.br/hc/article_attachments/44010105087511)

## Compara frete peso/frete valor

Caso a negociação com a transportadora seja o maior valor entre frete peso e frete valor, é necessário que a tabela possua o componente Compara Frete Peso / Frete Valor ativado:

![Imagem 28: Caso a negociação com a transportadora seja o maior valor entre frete peso e frete valor, é necessário que a tabela…](https://ajuda.sankhya.com.br/hc/article_attachments/44010128491415)

## Componente frete peso com valor muito alto

Se o componente Frete Peso estiver com um valor muito alto, é importante verificar a forma de cadastro. Um equívoco comum é a confusão entre os campos Valor Fixo e Valor Mínimo.

Caso o contrato com a transportadora seja um valor fixo por faixa de peso, é necessário cadastrá-lo no campo Valor Mínimo. O campo Valor Fixo é preenchido no caso do valor ser o multiplicado pelo peso.

Um exemplo:  Se você possui uma rota cujo o valor do frete peso é R$200,00 fixo, esse valor deve ser informado no campo de Valor Mínimo:

![Imagem 29: Um exemplo: Se você possui uma rota cujo o valor do frete peso é R$200,00 fixo, esse valor deve ser informado no campo…](https://ajuda.sankhya.com.br/hc/article_attachments/44010067930775)

Caso o custo seja, por exemplo, 0,7000 por quilo, ele deve ser preenchido no campo Valor Fixo:

![Imagem 30: Caso o custo seja, por exemplo, 0,7000 por quilo, ele deve ser preenchido no campo Valor Fixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44010128793111)

## Casos especiais

## Componentes customizados

Existem casos em que é necessário incluir um componente customizado, pois o componente pode ter um comportamento diferente do padrão. Por exemplo: uma taxa que cobre somente sobre determinados componentes, mas não todos da tabela. Para isso, é necessário solicitar o atendimento do Help Desk.

## Divergência da transportadora

Se após ter validado os campos e o cadastro parece correto, é importante questionar à transportadora se o valor cobrado é realmente correto, e pedir um detalhamento da cobrança, para verificar se confere com o valor acordado.

  "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
