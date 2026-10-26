---
id: "44013308285847"
titulo: "[TMS] - Prazo de Entrega - Transportadora"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013308285847--TMS-Prazo-de-Entrega-Transportadora"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:53:29Z"
rotulos: ["sync_hc", "lincros", "lincros_13432718", "sync_hash_cd01fbf01305"]
---

# [TMS] - Prazo de Entrega - Transportadora

**Menu**: Cadastros gerais > Transportadora > Negociações > Prazos de entrega > Transportadora

**Objetivo**: O prazo de entrega da transportadora constitui-se de um cadastro onde constam as cidades e os dias para entrega da mercadoria determinados pela transportadora. Possibilita o controle do andamento do transporte de suas cargas.

## Considerações:

- As informações para este cadastro e o cálculo em si, são fornecidas diretamente pela transportadora;
- Este cadastro pode ser realizado de duas formas: via importação ou manualmente via botão novo encontrado na tela de listagem de prazos de entrega;
- É necessário ter os campos abaixo já cadastrados no TMS para realizar o cadastramento do prazo de entrega:

- Transportadora;

Abaixo segue o passo a passo para cadastrar uma nova tabela de prazos:

1. Acessar o menu: Cadastros gerais > Transportadora > Negociações > Prazos de entrega > Transportadora;
2. Clicar na opção 'Novo';

![Imagem 1: Clicar na opção 'Novo';](https://ajuda.sankhya.com.br/hc/article_attachments/44013287374231)

3. Após, o sistema irá abrir uma nova tela para preenchimento dos campos:

- **Código**: É gerado automaticamente quando a tabela é salva;
- **Início da vigência**: Informe a data de início que essa tabela de prazos começa a valer;
- **Fim da Vigência**: Não é necessário colocar o fim da vigência da tabela de prazos, mas também existe essa opção, caso o embarcador possua essa data;
- **Situação de aprovação**: A tabela pode estar Aguardando Aprovação ou Deferida (aprovada). O prazo de entrega só passará a ser contado como ativo quando estiver com situação igual a DEFERIDO;
- **Transportadora**: seleciona a transportadora para qual está cadastrando os prazos;
- **Rota:** Selecionar a rota a qual esse prazo é aplicado. Este campo é de suma importância pois define quais rotas serão atendidas por este prazo de entrega, logo, para que uma carga tenha sua previsão de entrega calculada, é necessário garantir que a rota atenda a origem e destino da carga;
- **Faixa**: Caso seja necessário, é possível selecionar a faixa de peso que a rota atende, no caso de produtos com mais ou menos peso demorarem tempos diferentes para serem entregues;
- **Modal**: Selecionar o tipo de modal (rodoviário, aéreo...);
- **Tipo de Operação**: escolher se a tabela de prazos vale apenas para operações de saída, operações de entrada, ou se é bidirecional (o mesmo prazo é válido para ambas);
- **Somente dias úteis**: Quando selecionado, ele não contará no prazo os feriados cadastrados. Esta configuração determina que a entrega só poderá ser efetuada em dias úteis, ou seja, finais de semana e feriados são ignorados no cálculo do agendamento de entrega;
- Prazo: Esse prazo é o que contará, caso não tenha um prazo para a cidade específica. Consiste na quantidade de dias necessários para a transportadora realizar a entrega;
- **Dias pós coleta**: Quantidade de dias pós coleta da mercadoria que iniciará a contagem do prazo. Este campo indica a quantidade de dias após realizada a coleta em que deve ser iniciada a contagem do cálculo do agendamento de entrega;
- **Dias da Semana**: Frequência de dias no qual a transportadora realiza as entregas na cidade. Determina os dias da semana em que são realizadas entregas pela transportadora;
- **Localizações**: Este campo permite customizar os campos de Prazo e Dias da semana, onde é possível selecionar pra cada cidade ou estado (pertencentes à rota informada) a quantidade de dias necessárias para entrega e os dias em que são feitas as entregas. Caso esteja preenchido com algum valor, este será considerado o prazo. Caso zerado, será considerado o prazo geral.

Com a rota definida, é possível detalhar as localizações por região, estado ou cidade;

![Imagem 2: Com a rota definida, é possível detalhar as localizações por região, estado ou cidade;](https://ajuda.sankhya.com.br/hc/article_attachments/44013287489559)

 Ao detalhar por cidade, por exemplo, são listadas todas as cidades que compõe aquela rota. Caso o prazo para determinada cidade seja diferente do prazo geral, é possível adicionar na tabela. Dessa forma, o prazo que conta é o adicionado na cidade. Caso o prazo da cidade conste como zero, o prazo é o geral da tabela. Caso em alguma cidade a transportadora realize entregas somente em dias específicos da semana, também é possível selecionar na tabela.

![Imagem 3: Ao detalhar por cidade, por exemplo, são listadas todas as cidades que compõe aquela rota. Caso o prazo para…](https://ajuda.sankhya.com.br/hc/article_attachments/44013325839383)

É através desse cadastro que a ferramenta calcula os prazos de entrega das NF-es.

Nesta tela é possível visualizar o código da tabela de prazos, a rota que esses prazos contemplam, a faixa de peso, a origem e o destino, o prazo geral para esta tabela (dentro dela, poderão ser cadastrados prazos individuais), o modal e a transportadora.

## Aba Histórico

Após salvar o prazo de entrega, o sistema irá criar uma nova aba 'Histórico'. Nesta aba estão registrados os históricos de alterações realizados pelos usuário no item selecionado.

A manutenção do prazo de entrega pode ser realizada via planilha em caso de muitas alterações, para agilizar o processo:

- Na tela de listagem, filtrar o prazo desejado e exportá-lo em excel.
- Na aba Prazo (geral) são exibidas as informações da tela de cadastro do prazo:

- Observação: o campo Código (sistema) se refere ao código do determinado prazo de entrega. Caso o mesmo seja alterado na planilha, ao importá-la será criado um novo prazo de entrega ao invés de atualizar o existente.

![Imagem 4: - Observação: o campo Código (sistema) se refere ao código do determinado prazo de entrega. Caso o mesmo seja alterado…](https://ajuda.sankhya.com.br/hc/article_attachments/44013301437975)

- Na aba Prazo (localizações) são listadas as cidades (somente se em tela elas possuírem dias informados)

![Imagem 5: Na aba Prazo (localizações) são listadas as cidades (somente se em tela elas possuírem dias informados)](https://ajuda.sankhya.com.br/hc/article_attachments/44013278804375)

- Após realizar as alterações necessárias, salvar a planilha e importá-la. Basta clicar na opção 'Importar';

![Imagem 6: Após realizar as alterações necessárias, salvar a planilha e importá-la. Basta clicar na opção 'Importar';](https://ajuda.sankhya.com.br/hc/article_attachments/44013326292503)

Basta adicionar o arquivo a ser importado e clicar na opção 'Updload'. Logo abaixo da tela é possível consultar o 'Resultado da Importação'.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
