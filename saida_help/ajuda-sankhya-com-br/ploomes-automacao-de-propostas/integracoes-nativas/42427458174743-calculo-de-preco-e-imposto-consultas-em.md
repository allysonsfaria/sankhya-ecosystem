---
id: "42427458174743"
titulo: "Cálculo de Preço e Imposto: consultas em tempo real pela integração Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427458174743-C%C3%A1lculo-de-Pre%C3%A7o-e-Imposto-consultas-em-tempo-real-pela-integra%C3%A7%C3%A3o-Sankhya"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-11T16:14:45Z"
rotulos: ["sync_hc", "ploomes", "ploomes_11157483", "sync_hash_6c87a4e0517a"]
---

# Cálculo de Preço e Imposto: consultas em tempo real pela integração Sankhya

## 1 Introdução

As novas consultas em tempo real ao Sankhya pela integração são uma modernização no procedimento de consulta pela integração nativa, garantindo maior segurança e disponibilidade nas consultas. [As consultas atualmente disponíveis](https://sankhya.zendesk.com/hc/pt-br/articles/42427469505431#h_9ff0a01b90) pela integração continuam as mesmas, no entanto, com uma alteração nas API's de consulta de preço e de imposto no Sankhya.

As novas consultas de preço e imposto Sankhya permitem que o cálculo em tempo real de valores para produtos siga a lógica completa do ERP Sankhya, sem depender exclusivamente do parâmetro TIPTABPRECOS para valor unitário e também contempla todos os casos de uso de cálculos de impostos existentes no Sankhya.

A nova consulta amplia consideravelmente os casos de uso atendidos - passando a contemplar todos os cenários de configuração no Sankhya, elimina a necessidade de customizações manuais e contribui diretamente para a redução de erros e do tempo de configuração.

As consultas de preço e imposto estão **disponíveis tanto no Ploomes Web quanto no Ploomes Mobile** através do aplicativo**\***.

**\*Não é possível utilizar as consultas no modo offline do aplicativo.**

---

## 2 Pré-requisitos

**Ploomes Web**

- Sankhya ERP em versão 4.31 ou maior
- Ploomes CRM com versão do CPQ 3.0 habilitada
- Integração Plug&Play Sankhya ativa na conta

**Ploomes Mobile (App)**

- Sankhya ERP em versão 4.31 ou maior
- App com recurso "Tirador de Pedidos" habilitado
- Integração Plug&Play Sankhya ativa na conta

---

## 3 Habilitação, Configuração e Ativação da nova consulta de preço e imposto Sankhya

## 3.1 Habilitando a nova consulta na conta

Ao editar a integração o usuário administrador receberá um aviso informando que as novas consultas estão disponíveis para serem ativadas.

Caso a conta não possua algum requisito, será apresentada a informação nessa notificação.

No entanto, caso a conta possua todos os requisitos para a habilitação da nova consulta, será apresentada a opção de ativar as novas consultas na conta como no exemplo abaixo.

![Imagem 1: No entanto, caso a conta possua todos os requisitos para a habilitação da nova consulta, será apresentada a opção de…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1531321787/7647bdd43fc4ef5000f6508bff17/image.png?expires=1786536000&signature=d674d8bac44b7455355473954f21e8d68cf9efda157ef0370a3a2f9d5b6873d3&req=dSUkF8p8nIZXXvMW3nq%2BgfDyBICEsBd3JKaQC9tnQ9s4cZJkoL45%2FTe9q0NJ%0AZ0ZADcGJFqBJ3mXV8MMrAfaQyeE%3D%0A)

Ao ativar as novas consultas, será habilitada uma nova seção de configuração além das seções de Configurar cadastros base da integração e Configurar cadastros de operação, que será a nova seção Configurar consultas em tempo real.

![Imagem 2: Ao ativar as novas consultas, será habilitada uma nova seção de configuração além das seções de Configurar cadastros…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1531327783/fe8678714d1acb042d178cb67375/image.png?expires=1786536000&signature=05c1be52ef285092cfd01f13af818858e793fc7dccde4208c6f7cc64b24e3900&req=dSUkF8p8moZXWvMW3nq%2Bgf4lrwgSzrT59QEdhQ7P4u9hYtRuqfc2XsfjmPbE%0ASbCEb2qUCMor2BPD1ThGJ%2BMe0zo%3D%0A)

Após a seção Configurar consultas em tempo real aparecer na tela de configuração da integração, teremos concluído a habilitação da nova consulta na conta.

## 3.2 Configurando as novas consultas

No painel de “Consultas em tempo real”, defina separadamente quais consultas em tempo real habilitar para Propostas e Vendas, que estarão nas abas "Orçamentos" e "Pedidos de venda" respectivamente.

![Imagem 3: No painel de “Consultas em tempo real”, defina separadamente quais consultas em tempo real habilitar para Propostas e…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1531340078/cd070236274e569bfc6e1357e3e3/image.png?expires=1786536000&signature=899afe8a3bd3828fe9f61058a35d14aa5cd116bbdb90acf572ea2665bc354810&req=dSUkF8p6nYFYUfMW3nq%2BgepU%2FZqP0%2FEf%2FbghgKCAHmT6gPpY9y1oLseb4j5U%0AhVqlWbhLGWsOQddbsFy%2BhSYaTAI%3D%0A)

Para ativar as consultas é necessário que o gatilho de consulta para cada tipo de consulta em cada tipo de documento (Proposta e Venda) esteja habilitado.

As consultas disponíveis para Proposta e Venda são as mesmas:

- **Limite de crédito** dos Parceiros integrados
- **Restrições da TOP** utilizada
- **Estoque do Produto**
- **Valor unitário** do Produto/Serviço
- **Impostos** do Produto/Serviço

### 3.2.1 Configurando as consultas de Limite de crédito, Restrições da TOP e Estoque do Produto

Para a configuração das consultas de Limite de crédito, Restrições da TOP e Estoque do Produto é necessário apenas ativar o gatilho das consultas que a integração criará os campos que recebem o retorno das consultas, conforme exemplo abaixo:

![Imagem 4: Para a configuração das consultas de Limite de crédito, Restrições da TOP e Estoque do Produto é necessário apenas…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1531344232/21062a0dca34cc1aad0112eb0a67/image.png?expires=1786536000&signature=e2d5257412edeccaf4c00c38aa17cacb78823558dbb4c234a9612e4a39487380&req=dSUkF8p6mYNcW%2FMW3nq%2BgXnzluwDGy0cbhnWiIMCrah%2Fwd2gdufJKYOGtN63%0A0CCdXYraIB3nm%2B8KPaBtH1cn8uM%3D%0A)

Com os gatilhos ativos, é necessário salvar a configuração da seção de consultas em tempo real e aplicar a edição da integração para que a ativação das consultas sejam efetivada na conta.

As consultas retornam os dados [conforme o comportamento atual](https://sankhya.zendesk.com/hc/pt-br/articles/42427469505431#h_9ff0a01b90), desde que os campos sejam configurados nos modelos de documento.

### 3.2.2 Configurando a consulta de Preço

Para a consulta preço é necessário realizar configurações adicionais além de ativar o gatilho da consulta.

Com o gatilho da consulta habilitado, serão carregadas mais informações para realizar a configuração da consulta:

#### 3.2.2.1 Parâmetro para simulação de inclusão

A primeira configuração possível é a flag de customizações não nativas no Sankhya para precificação. **Esse parâmetro deve ser utilizado apenas como último recurs**o, caso exista alguma customização no Sankhya que não seja atendida pela engine padrão de cálculo de preço dinâmico do Sankhya.

![Imagem 5: A primeira configuração possível é a flag de customizações não nativas no Sankhya para precificação. Esse parâmetro…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1531363546/0f9c03103c3346640b56b9aaad4a/image.png?expires=1786536000&signature=2bb997c57a6a41fd75a9a1287a672dd8b4180e5979f2e6def94b63b30dcec806&req=dSUkF8p4noRbX%2FMW3nq%2BgTS%2FUp1zKrrfsUyQs8tfsgDFy0Ez6i6tF2DiqMPu%0AMVsOWYhEGPFEA558OnBTPmCOzzI%3D%0A)

Ao ativar esse parâmetro, durante a consulta de preço será realizada uma operação de simulação de inclusão no Sankhya, de modo que qualquer procedure ou rotina configurada no Sankhya seja executada e retorne o preço conforme a configuração do Sankhya. No entanto, essa operação tende a ser mais lenta do que a consulta sem a utilização do processo de simulação.

Caso o Sankhya integrado utilize as funcionalidades de cálculo de preço nativas do Sankhya, esse parâmetro não deve ser marcado.

#### 3.2.2.2 Payload de envio da consulta

Logo abaixo estão as informações do payload de envio para a consulta de preços.

O payload é o conjunto de dados efetivamente enviados ou recebidos, ou seja, o corpo da mensagem que requisita uma informação entre sistemas, que neste caso são Ploomes e Sankhya.

Considerando que o cálculo de preços no Sankhya pode ser influenciado por informações de CabecalhoNota quanto de ItemNota, é necessário selecionar quais informações devem ser enviadas ao Sankhya para que o sistema calcule o preço e retorne a informação ao Ploomes.

Portanto, considerando as entidades do Ploomes, configuramos separadamente os payloads para Proposta ou Venda e Produto da Proposta ou da Venda. Abaixo temos um exemplo de configuração para consulta de preço de Proposta:

![Imagem 6: Portanto, considerando as entidades do Ploomes, configuramos separadamente os payloads para Proposta ou Venda e Produto…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1531374715/e69eeef587545eee878743f5475b/image.png?expires=1786536000&signature=4c23fb5fdddadfea3c30d9fbc91ee19e330a33f595977764eee3af32a411ba23&req=dSUkF8p5mYZeXPMW3nq%2BgcbxMTJ87Nw%2Ft8xJdeqtTlJ7lU7tLa6zOOjo2haK%0A%2FPYjkIlRL2nwzJtUR5zU9oWRkc0%3D%0A)

Por padrão, é obrigatório enviar as seguintes informações mínimas para consulta:

**Proposta/Venda:**

- Empresa
- Cliente
- Vendedor Responsável
- TOP
- Tipo de Negociação
- Natureza
- Centro de Custo

**Produto da Proposta/Venda:**

- Código do Produto
- Controle
- Unidade de Medida
- Quantidade

Os valores enviados do Ploomes para o Sankhya são os valores preenchidos nos campos mapeados com os respectivos campos do Sankhya na entidade integrada. Por esse motivo, os dados mínimos obrigatórios acima citados já possuem o DE-PARA de campos do payload fixos, que são os campos correspondentes do mapeamento da entidade integrada.

Nessas subseções é possível realizar duas configurações.

A **primeira é a definição da obrigatoriedade ou não de um campo para que a consulta seja engatilhada.** Essa configuração é feita com base no modal de ativação/desativação de engatilhamento ao lado direito do campo, conforme exemplo abaixo:

![Imagem 7: A primeira é a definição da obrigatoriedade ou não de um campo para que a consulta seja engatilhada. Essa configuração…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1547381340/dff33553baab6ed98ad18f12e244/image.png?expires=1786536000&signature=36e0d9df7fdaeb6fca039781a555357c5ee39eef2217c3888feebe2fd767f0ad&req=dSUjEcp2nIJbWfMW3nq%2BgfABLyFlYJy%2Fu1b4Uvg4eYFaXO1%2ByDqmeacJta%2BY%0A4kdLIHt0a5A5EaRxQ%2BK%2BrznGBnQ%3D%0A)

Todos os campos incluídos na seção de envio para consulta são enviados no pacote de dados do payload, mas somente os campos configurados como obrigatórios para o engatilhamento é que determinam se uma consulta será enviada ou não.

**Exemplo:** no caso do exemplo acima, a consulta de preço poderia ser engatilhada sem o campo `"Valor da Moeda"` preenchido, mas não poderia ser engatilhada em o valor de `"Tipo de Negociação"`. De todo modo, o campo `"Valor da Moeda"` seria enviado no Payload, mesmo que esteja vazio.

A **segunda configuração possível é a inclusão de mais campos no payload de consulta**, tanto para Proposta/Venda quanto para Produto da Proposta/Venda.

Considerando que existem campos além dos mínimos obrigatórios que podem influenciar no cálculo de preço configurado no Sankhya, é possível adicionar mais campos no payload.

![Imagem 8: Considerando que existem campos além dos mínimos obrigatórios que podem influenciar no cálculo de preço configurado no…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1531403810/95282e557753be499b45638b2457/image.png?expires=1786536000&signature=31eb6be704e3bf522dc0ebe24b0c11a7e59b46c81b8011434a885c449b549075&req=dSUkF81%2BnoleWfMW3nq%2BgbTeOKbwBKM2UoyBmNYA9vqpVP7CB86n98VriOxh%0AZBnnTiNTqBqceZSiAqgdaOs7iGI%3D%0A)

Ao acionar o botão "Novo campo" para Proposta/Venda ou Produto da Proposta/Venda, serão exibidos os campos mapeados para a respectiva entidade integrada, para que possam ser incluídos no payload de configuração.

Após a inclusão dos novos campos é possível configurar também a obrigatoriedade ou não de preenchimento do campo para engatilhamento.

#### 3.2.2.3 Payload de recebimento da consulta

Com o payload de envio da consulta configurado, é preciso configurar o payload de recebimento.

Para a consulta de preço o retorno é apenas do valor unitário do Produto da Proposta ou da Venda.

![Imagem 9: Para a consulta de preço o retorno é apenas do valor unitário do Produto da Proposta ou da Venda.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1531409678/cfa8e59bb1ddb66a1c4be3526558/image.png?expires=1786536000&signature=9330948ddea1394142743dff34852f00c560970ba61b1170e1ddcbb6d12e5b29&req=dSUkF81%2BlIdYUfMW3nq%2BgQWywVqV8oWzZagmSVn0cHd8ZIxvL%2BhqICjmKFlm%0AYuR59%2FMGnyxRqm4boUPXD4%2F4RuQ%3D%0A)

Neste caso, é possível alterar o campo que receberá o retorno da consulta para o campo de preferência do usuário administrador. Após essa configuração, finalizamos a configuração da consulta de preços.

### 3.2.3 Configurando a consulta de Impostos

Para a consulta impostos também é necessário realizar configurações adicionais além de ativar o gatilho da consulta.

Com o gatilho da consulta habilitado, serão carregadas mais informações para realizar a configuração da consulta:

#### 3.2.3.1 Nota Modelo no Sankhya

A primeira configuração é a definição do Nro. Único do Sankhya do CabecalhoNota que será utilizado como Modelo nas consultas de impostos.

No Sankhya é possível realizar diversas parametrizações que influenciam diretamente no cálculo de impostos, a fim de atender a necessidade fiscal do negócio. Para simplificar o processo de cálculo via API, é necessário então que um CabecalhoNota seja utilizado como modelo de parametrização dos cálculos de impostos.

Portanto, informamos aqui o NUNOTA referente à Nota Modelo do Sankhya para o cálculo de impostos.

![Imagem 10: Portanto, informamos aqui o NUNOTA referente à Nota Modelo do Sankhya para o cálculo de impostos.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1531413758/f5b69138509061ed33afaefd1d3d/image.png?expires=1786536000&signature=127a2fe539befadf6269e8dfb0c4e62c326545801b23acc304ddd364d1a6a193&req=dSUkF81%2FnoZaUfMW3nq%2Bge%2FrJSqoTv8H8lQUqSQQH9RLDrXRlR2jWk0peVQg%0ArppUNs5X%2BL64xoIS%2BSeJcQFDgpQ%3D%0A)

Só é possível utilizar um único NotaModelo para as consultas de impostos.

#### 3.2.3.2 Payload de envio da consulta

Logo abaixo estão as informações do payload de envio para a consulta de impostos.

O payload é o conjunto de dados efetivamente enviados ou recebidos, ou seja, o corpo da mensagem que requisita uma informação entre sistemas, que neste caso são Ploomes e Sankhya.

Para a consulta de impostos, além da NotaModelo, são enviadas na requisição informações da Proposta/Venda e do Produto da Proposta/Venda, conforme exemplo abaixo:

![Imagem 11: Para a consulta de impostos, além da NotaModelo, são enviadas na requisição informações da Proposta/Venda e do Produto…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1531423038/de9b141dc310f30bc82c9fd6dcdc/image.png?expires=1786536000&signature=7fc9f65b211b6e93e5169175aa87a73e6643e0447592864ff937be172d22abe6&req=dSUkF818noFcUfMW3nq%2BgV7HRdgzXwgjpA4PR3KtwbZLuRCffF2UpSdr%2Fs2m%0AI8XMQqgecCNAQlLIbDDWv8asSeM%3D%0A)

Por padrão, é obrigatório enviar as seguintes informações para consulta:

**Proposta/Venda:**

- Nota Modelo
- Empresa
- Cliente
- Vendedor Responsável
- TOP
- Tipo de Negociação
- Natureza
- Centro de Custo
- Finalidade da Operação
- Valor de Frete
- Valor de Seguro
- Valor Outras Despesas

**Produto da Proposta/Venda:**

- Código do Produto
- Unidade de Medida
- Quantidade
- Valor Unitário (sem desconto)
- Valor Desconto Total

Diferentemente da consulta de preços, no caso da consulta de impostos não é possível configurar obrigatoriedade de campos para engatilhamento (pois todos os campos listados são obrigatórios) e nem é possível incluir mais campos no payload de envio.

Logo, a consulta enviará todos os campos listados acima no payload de consulta de impostos e também será engatilhada somente se todos os campos estiverem preenchidos.

#### 3.2.3.3 Payload de recebimento da consulta

Com o payload de envio da consulta configurado, é preciso configurar o payload de recebimento.

Para a consulta de impostos o retorno pode ser de N campos, conforme os impostos configurados no Sankhya.

Os valores referente aos cálculos de impostos possíveis de retorno na consulta via API são:

- Base ICMS
- Alíquota ICMS
- Valor ICMS
- Base IPI
- Alíquota IPI
- Valor IPI
- Base ISS
- Alíquota ISS
- Valor ISS
- Base ST
- Alíquota ST
- Valor ST
- Base IRPJ
- Alíquota IRPJ
- Valor IRPJ
- Base IRF
- Alíquota IRF
- Valor IRF
- Base CPP
- Alíquota CPP
- Valor CPP
- Base INSS
- Alíquota INSS
- Valor INSS
- Base CSSL
- Alíquota CSSL
- Valor CSSL
- Base PIS
- Alíquota PIS
- Valor PIS
- Base COFINS
- Alíquota COFINS
- Valor COFINS
- Valor Desoneração
- Valor DIFAL Remetente
- Valor DIFAL Destinatário

E também os impostos da reforma tributária:

- Base CBS
- Alíquota CBS
- Valor CBS
- Base CBS Monofásico
- Alíquota CBS Monofásico
- Valor CBS Monofásico
- Base IBS Monofásico
- Alíquota IBS Monofásico
- Valor IBS Monofásico
- Base IBS Municipal
- Alíquota IBS Municipal
- Valor IBS Municipal
- Base IBS UF
- Alíquota IBS UF
- Valor IBS UF
- Base IS
- Alíquota IS
- Valor IS

![Imagem 12: Valor IS](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1547372129/7d04f2714a6372c52c2a4a281c01/image.png?expires=1786536000&signature=2b0fb05b8d98e37deeaabb8fd8eed1f15dc480fcc9318e729f48bde32f0ca105&req=dSUjEcp5n4BdUPMW3nq%2Bge7MLkCwcdwsAij7%2BkTQ%2BnR40R4sNZ3mXV7A5sak%0ABboX9Lnx6UXYv55LdyxsrmngeYU%3D%0A)

É possível selecionar quais campos receber como retorno da consulta de impostos, bem como em quais campos os valores serão recebidos.

![Imagem 13: É possível selecionar quais campos receber como retorno da consulta de impostos, bem como em quais campos os valores…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1547374997/c7a00bf5352befa4e8278911bfe1/image.png?expires=1786536000&signature=bf03dcc540a41b446e8abc00e4c480217b17d8b6f80a9a67ac5ef3548e746fa7&req=dSUjEcp5mYhWXvMW3nq%2BgSpZ373BKsZ0SauDuS07ma%2BWf%2FCMdUrLVZIUVIAu%0AWc0qav1y1NEyScE6nyK1bvs3E6M%3D%0A)

Após essa configuração, finalizamos a configuração da consulta de impostos.

## 3.3 Ativando as novas consultas

Com todas as consultas configuradas, para que as configurações sejam efetivamente aplicadas à conta e estejam disponíveis é necessário realizar o salvamento da seção **Configurar consultas em tempo real** e aplicar a edição da integração.

![Imagem 14: Com todas as consultas configuradas, para que as configurações sejam efetivamente aplicadas à conta e estejam…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1531438943/217afc5ab486a2a9e06f91a5299e/image.png?expires=1786536000&signature=0ce08b18046133695dea8212f58b0f9e9295f02b6467ff7130def2e3c98056e6&req=dSUkF819lYhbWvMW3nq%2Bgdit%2FdXXH5fdjKmQBHaFG1NLCIajgH%2BikvVWUIYc%0AxJN01u1iFPhX69TpYU5SNDi7GJ8%3D%0A)

É importante se atentar a necessidade de realizar a configuração para Propostas e para Vendas separadamente para que estejam disponíveis as consultas tanto para Propostas quanto para Vendas.

![Imagem 15: É importante se atentar a necessidade de realizar a configuração para Propostas e para Vendas separadamente para que…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1531440159/8a8e721a40b5bdc4df47cfe8da27/image.png?expires=1786536000&signature=0066a334085293ea00cdb269322d6e096f0f273bf1811a74cb262f362e3d1ca3&req=dSUkF816nYBaUPMW3nq%2Bgf9cJGqdCGrqvUHzfF50CGwAdPIntssjEyLVAoHP%0AnFHY3tzDwSrFcclBQktM6vwJSY8%3D%0A)

---

## 4 Configuração dos modelos de documento

Nos modelos de proposta utilizados no CPQ, é necessário configurar:

- Os campos que **disparam** (engatilham) a execução e os que são enviados nos payloads das consultas de preço e imposto .
- Os campos que **recebem** o retorno dessas consultas.

A correta configuração desses campos garante que os valores retornados pela API sejam exibidos na proposta.

---

## 5 Utilizando a Nova consulta de preço e imposto Sankhya

## 5.1 Consultando limites de créditos

Para os Parceiros do Sankhya que estão integrados ao Ploomes como um Cliente, é possível realizar a consulta de detalhes financeiros na tela de Proposta/Venda. É possível engatilhar a consulta de detalhes financeiro do Cliente ao selecionar um Cliente e uma TOP.

Essa consulta retorna os dados em uma tabela resumo com os seguintes totais do Parceiro no Sankhya:

- Títulos a vencer
- Títulos em aberto
- Títulos em atraso
- Limite de crédito total
- Limite de crédito mensal

Para que essa consulta seja possível na tela de edição de Proposta/Venda, é necessário que o campo “Detalhes Financeiros (Sankhya)” - ou o campo utilizado no seu lugar na configuração - seja inserido no modelo de documento da Proposta/Venda. O campo pode ficar oculto que a consulta ainda irá funcionar.

## 5.2 Consultando restrições da TOP

Para as TOP’s do Sankhya que estão configuradas no Ploomes para utilização nas Propostas/Vendas é possível realizar a consulta das restrições/exceções da TOP na tela de edição da Proposta/Venda.

Essa consulta retorna os dados em uma tabela resumo com os seguintes dados:

- Entidade: entidade que possui a restrição ou exceção com a TOP
- Restrição/Exceção: regra de negócio, se é uma exceção ou uma restrição
- Cadastros: código e descrição do cadastro relacionado a regra de negócio de restrição/exceção da TOP

Para que essa consulta seja possível na tela de edição de Proposta/Venda, é necessário que o campo “Detalhes de Restrições da TOP (Sankhya)” - ou o campo utilizado no seu lugar na configuração - seja inserido no modelo de documento da Proposta/Venda. O campo pode ficar oculto que a consulta ainda irá funcionar.

## 5.3 Consultando estoque do produto

Para os Produtos da Proposta/Venda que são inseridos no formulário de CPQ é possível realizar uma consulta em tempo real ao Sankhya para exibir uma tabela resumo com as informações de estoque disponível do Produto.

Essa consulta retorna uma tabela resumo com os dados de estoque do Produto/Serviço no Sankhya conforme os campos preenchidos no Ploomes.

Nessa tabela, vão ser exibidos em linhas os estoques por:

- **Empresa**
- **Local**
- **Controle**

E serão exibidos os totais das colunas de:

- **Estoque:** quantidade total do Produto em estoque
- **Reservado:** quantidade total reservada o Produto
- **Disponível:** quantidade total de estoque do Produto que está disponível

As quantidades exibidas são convertidas em função da unidade de medida selecionada. A conversão é feita pelo Sankhya, com base nos dados das entidades TGFEST (Estoque) e TGFVOA (Volume Alternativo) do Sankhya.

Para que essa consulta seja possível no formulário de CPQ, é necessário que o campo “Detalhes de Estoque (Sankhya)” - ou o campo utilizado no seu lugar na configuração - seja inserido no modelo de documento dentro do bloco de Produto da Proposta/Venda. O campo “Detalhes de Estoque (Sankhya)” não pode ficar oculto.

## 5.4 Consultando preços com nova API

Ao preencher uma Proposta ou Venda no CPQ, o Ploomes executa automaticamente a consulta de preço para cada Produto da Proposta/Venda, conforme as obrigatoriedades definidas na configuração e também nos campos configurados para envio no payload.

A nova API retorna o valor conforme regras de precificação do Sankhya, sem a necessidade de ajustes ou configurações adicionais. O resultado é exibido nos campos configurados no modelo do documento.

## 5.5 Consultando impostos com nova API

Ao preencher uma Proposta ou Venda no CPQ, o Ploomes executa automaticamente a consulta de impostos para cada Produto da Proposta/Venda, conforme as obrigatoriedades estabelecidas na configuração e também nos campos definidos para envio no payload.

A nova API retorna o valor conforme regras de precificação do Sankhya, sem a necessidade de ajustes ou configurações adicionais. O resultado é exibido nos campos configurados no modelo do documento.

---

## F.A.Q.

**1. Posso usar a nova consulta apenas para preço ou apenas para imposto?**

Sim. A tela de configuração permite ativar separadamente a nova API para preço e para imposto.

**2. O que acontece se a consulta falhar?**

Se houver erro na comunicação com a API ou se os dados obrigatórios estiverem ausentes (como código do parceiro ou do produto), o sistema pode não retornar os valores esperados. Nesse caso, uma mensagem de erro será exibida e os campos ficarão em branco.

**3. É possível editar os valores calculados para preço e imposto?**

Sim, desde que o modelo de documento permita edição dos campos de preço e imposto, o usuário poderá ajustá-los manualmente.

**4. As consultas são executadas automaticamente?**

Sim. Uma vez configuradas, as consultas ocorrem de forma automática durante o preenchimento dos campos definidos no payload e configurados no modelo de documento, sem necessidade de ações manuais adicionais.

**5. As consultas funcionam no modo offline do aplicativo?**

Não. As consultas em tempo real só funcionam com acesso à internet, pois dependem da comunicação em tempo real com o ERP Sankhya.

**6. Os impostos da reforma tributária estão disponíveis na consulta de impostos?**

Sim. Os impostos CBS, IBS e IS da reforma tributária estão disponíveis na nova consulta de impostos e podem ser consultados desde que estejam configurados no Sankhya.

---

## Artigos relacionados

[Integração com o ERP Sankhya](https://sankhya.zendesk.com/hc/pt-br/articles/42427469505431#h_9ff0a01b90)

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
