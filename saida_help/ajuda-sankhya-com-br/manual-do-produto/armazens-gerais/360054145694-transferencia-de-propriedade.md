---
id: "360054145694"
titulo: "Transferência de Propriedade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360054145694-Transfer%C3%AAncia-de-Propriedade"
trilha: "Manual do Produto > Suprimentos e Estoque > Armazéns Gerais"
atualizado_em: "2026-07-29T15:07:37Z"
rotulos: ["Produtos", "Configuração", "Portal de Compras", "WMS", "Contrato", "Estoque", "Transferência", "br.com.sankhya.armazem.cad.TransPropriedade", "Contrato de Armazenagem", "Apuração/Faturamento de Contratos", "Portal Armazéns", "Comercialização de Grãos", "APURQTPEDOL", "Controle de Contratos e Notas fiscais", "Transferência de Propriedade Automatizada", "Formalização de Negociações de Armazenagem", "Contratos Armazenagem Transferência"]
---

# Transferência de Propriedade

```
Módulo: Armazéns Gerais > Rotinas              Versão disponível: A partir da 4.4
```

---

Essa tela permite que seja realizada a Transferência de Propriedade de produtos entre [Contratos de Armazéns de Grãos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os) lançados no módulo [Armazéns Gerais/W](https://ajuda.sankhya.com.br/hc/pt-br/sections/360008308773-Armaz%C3%A9ns-Gerais).

![Imagem 1: Essa tela permite que seja realizada a Transferência de Propriedade de produtos entre Contratos de Armazéns de Grãos…](https://ajuda.sankhya.com.br/hc/article_attachments/20197391228951)

Nesse tipo de negócio é comum que, após armazenar seus produtos, os contratantes do armazém negociem seu saldo disponível com terceiros ou com o próprio armazém que, por sua vez, podem manter esse saldo no mesmo local. Porém, é necessário que haja a formalização dessa transferência, através do retorno de quem vendeu e do registro da entrada no contrato de quem comprou.

A partir desse momento, o saldo disponível passa a considerar as parametrizações do novo Contrato de Armazenagem ou de Comercialização, registrado em nome daquele que recebeu a transferência.

Para consultar uma transferência já realizada, informe seu número no campo **"Consultar Transferência"** do Painel de Filtros e clique em **"Aplicar"**. Caso não possua o número da transferência, utilize a lupa desse campo; assim, ao ser acionada, fará com que o sistema exiba o assistente de pesquisa **"Histórico de Transferências"**, onde é possível pesquisar por **"Contrato Origem"** ou **"Data de Transferência"**.

![Imagem 2: Para consultar uma transferência já realizada, informe seu número no campo "Consultar Transferência" do Painel de…](https://ajuda.sankhya.com.br/hc/article_attachments/20197482615959)

## Painel de Filtros

No Painel de filtros, temos os seguintes campos e marcações:

**Tipo de Transferência:** permite escolher como transferir de forma automatizada o saldo de armazenagem de um contratante do armazém para o seu contrato de armazenagem ou de comercialização, considerando as seguintes opções:

- **Dev. Armazenagem >> Ent. Armazenagem:** a transferência irá ocorrer entre contratos de armazenagem, gerando a nota de saída e a de entrada no Portal Armazéns.
- **Dev. Armazenagem >> Ent. Compra:** a transferência irá ocorrer de um contrato de armazenagem para um de comercialização, transferindo o saldo comprado pelo armazém e gerando as notas conforme a natureza da operação (uma nota de saída no Portal Armazéns e uma nota de entrada no Portal de Compras).

**Nota:** O recurso Dev. Armazenagem >> Ent. Compra está disponível apenas para clientes que tenham a licença do Opcional [30935 - Comercialização de Grãos/W]. Caso não possua a licença, por padrão, as transferências ocorrem apenas entre contratos de armazenagem.

**Contrato:** destina-se à informação do Contrato de Armazenagem a partir do qual a transferência será realizada. Ou seja, deve-se informar o número do contrato em que ocorrerá o retorno simbólico de armazenagem.

**Selecionar notas para devolução:** determine se deseja escolher ou não as notas de depósito a serem devolvidas simbolicamente. Caso opte por não selecionar as notas, o sistema realizará a devolução conforme a data de entrada das notas de depósito, buscando da mais antiga para a mais nova, até totalizar o saldo a ser transferido.

**Selecionar pedidos para devolução:** lista todos os pedidos de devolução pendentes, confirmados e vinculados ao respectivo contrato informado na pesagem. Além disso, nesta opção serão apresentados os campos **"Cód. Parceiro"** e **"Parceiro Dest."**.

### Parâmetros de Validação e Quebra Técnica

Ao utilizar as opções de seleção de pedidos e notas, o comportamento do sistema é influenciado pelos seguintes parâmetros:

> **Nota Importante (Validação de Estoque):** Para que o sistema valide o estoque de pedidos na tela de Transferência de Propriedade, o parâmetro **VALESTPEDIDO** deve estar ativado.
>
> - **Ativado:** O sistema impede a transferência de uma quantidade maior que o saldo disponível do contrato e exibe a mensagem de erro: "Quantidade solicitada maior que o Saldo Disponível do Contrato".
> - **Desativado:** A validação de estoque para os pedidos de devolução não ocorre nesta tela. Embora a tela realize essa validação básica quando o parâmetro está ativo, ela não executa a validação completa que considera provisões futuras, como as quebras técnicas. Isso ocorre porque o fluxo de transferência direta não possui o contexto detalhado da tela de Pesagem, que é o processo projetado para ter todas as informações necessárias para uma verificação segura do saldo real.

- **Apurar Quebra Técnica sobre Pedido de Devolução (APURQTPEDOL):** Se você optar por "Selecionar pedidos para devolução" e este parâmetro estiver ligado, o decréscimo da quebra será considerado na quantidade disponível de pedidos para faturamento.

  - **LIGADO:** O sistema busca as notas de origem da quebra primeiro nos Pedidos de Devolução pendentes (Tipo 2) e, em seguida, nas Notas Fiscais de Depósito pendentes (Tipo 1). O objetivo principal é considerar a diferença de quebra que surge quando um pedido de devolução é gerado antes do faturamento, mas novas quebras ocorrem nesse intervalo. O sistema considera essa diferença no pop-up de saída para abater o saldo de estoque corretamente.
  - **DESLIGADO:** O sistema considera como origem apenas as Notas Fiscais de Depósito (Tipo 1).
  - Aviso: Não habilite este parâmetro se já houver movimentações de entrada e saída (pois pode quebrar o processo de faturamento) ou se o saldo de estoque for gerado por mais de um Romaneio/NF-Depósito.

## Executando a Transferência

Ao informar um Contrato e marcar as opções Selecionar notas para devolução ou Selecionar pedidos para devolução, após clicar em **Aplicar**, será exibido o campo **"Diferença"**, refletindo a subtração do "Total Selecionado" entre a "Quantidade Transferência". Esse valor será recalculado conforme a edição do campo **"Qtd. a Faturar"** de cada linha dos documentos apresentados na grade.

> **Observação de Segurança:** Verifique na tela de Usuários (aba Segurança) a marcação "Não permite gerar saídas a partir de NF de Depósito". O sistema apresentará os seguintes comportamentos ao informar um contrato de armazenagem:
>
> - **Desabilitada:** Pode-se escolher entre "Selecionar notas para devolução", "Selecionar pedidos para devolução" ou não marcar nenhuma das opções e clicar em "Aplicar".
> - **Selecionada:** Será possível transferir apenas a partir de Pedidos de devolução. Deste modo, ao abrir a tela, a opção Selecionar pedidos para devolução deverá estar marcada e protegida contra edição.

Após aplicar os filtros, o sistema trará, automaticamente, as informações do "Parceiro", "Inscrição Estadual", "Endereço" e "Saldo Disponível" do respectivo contrato, deixando a critério do usuário preencher os seguintes campos:

- **TOP p/ Transferência:** lista as TOP's com Tipo de Movimento = 3 - Saídas, que deverão ser utilizadas para a emissão da nota de retorno simbólico.
- **Série:** destinada à informação da série a ser utilizada na emissão da nota fiscal.
- **Data:** informe o dia de emissão da nota fiscal.
- **Local:** preencha com o local de estoque a ser utilizado, caso sua empresa utilize o Controle por Local.
- **Observação padrão:** selecione alguma observação a ser utilizada na emissão da nota fiscal (deve ser cadastrada previamente na tela Observação para Notas).
- **Qtd. Transferência:** quantidade a ser transferida do respectivo contrato (esta quantidade não pode ser maior do que o Saldo Disponível do contrato).

Após concluir o preenchimento dessas informações, clique no botão **"Transferir"** localizado no Painel de Filtros. Assim, será aberto o pop-up **"Transferir Para"**; nele, defina as parametrizações relacionadas à entrada simbólica da NF de Depósito ou da NF de Compra no contrato de destino, conforme a seleção do campo Tipo de Transferência.

- **Contrato:** informe o contrato de destino da transferência.
- **Parceiro e Inscrição Estadual:** preenchidos automaticamente com as informações do Contrato informado.

[GIF animado: Imagem 3: Parceiro e Inscrição Estadual: preenchidos automaticamente com as informações do Contrato informado.](https://ajuda.sankhya.com.br/hc/article_attachments/8658936212887)

![Imagem 4: GIF animado: Imagem 3: Parceiro e Inscrição Estadual: preenchidos automaticamente com as informações do Contrato…](https://ajuda.sankhya.com.br/hc/article_attachments/20197660905879)

### Seção Configuração para nota

- **Tipo Operação:** lista as TOP's com Tipo de Movimento = 1 - NF Depósito (ou C-Compras, caso o Tipo de Transferência selecionado seja Dev. Armazenagem >> Ent. Compra), que deverão ser utilizadas para o lançamento da nota de entrada simbólica.
- **Série:** série da nota fiscal a ser lançada.
- **Data de Emissão:** dia/mês/ano de emissão da nota.
- **Local:** local de estoque a ser utilizado, caso sua empresa utilize o Controle por Local.
- **Chave Acesso:** informe a chave de acesso da nota fiscal a ser lançada, caso esta seja eletrônica e de terceiros.
- **N° Nota:** destinado à informação do número da nota fiscal a ser lançada, caso esta seja de terceiros.
- **Vlr. Unitário:** valor unitário da nota fiscal a ser lançada.
- **Vlr. Total:** valor total da nota fiscal a ser lançada.

Ainda nessa seção, quando o Tipo de Transferência selecionado for **Dev. Armazenagem >> Ent. Compra**, o pop-up irá apresentar:

- **Observação:** destinado a quaisquer observações adicionais a serem consideradas no lançamento das notas da transferência.
- **Selecionar Pedidos para Compra:** quando ativada, listará os pedidos de compra confirmados e pendentes vinculados ao contrato de comercialização informado no pop-up, para selecionar aquele sobre o qual deseja faturar a nota de compra.

> **Nota (Vínculo Financeiro):** No processo de transferência de propriedade, o sistema utiliza o pedido de compra para gerar a nota de devolução ao parceiro do estoque de origem. Caso o usuário altere informações do pedido durante este processo (como quantidade ou valor unitário), ao gerar a nota de compra, o financeiro correspondente perderá o vínculo com o pedido de origem e um novo financeiro será criado. Nessa situação, a data de vencimento do financeiro da nota de compra será calculada com base na data de negociação da própria nota, e não na data do pedido. Caso seja necessário que o vencimento considere a data de negociação do pedido, será preciso refazer o financeiro da nota de compra.

> **Observação (Exigência de Pedido):** Se o pedido de compra sobre o qual deseja vincular a nota de compra não for selecionado, mas o contrato estiver com a opção "Exige Pedido na Pesagem" marcada, ao clicar em Gerar Transferência o sistema irá buscar o pedido pelo método FIFO para vincular a nota de compra. Dessa forma, a nota de saída será gerada no Portal Armazéns e a nota de entrada no Portal de Compras. Caso não encontre um pedido, a operação não será concluída e uma mensagem será apresentada informando que o contrato de compra referenciado exige o vínculo com um pedido de compra.

### Seção Referência da Negociação

![Imagem 5: Seção Referência da Negociação](https://ajuda.sankhya.com.br/hc/article_attachments/20197660898711)

- **Nf de Venda:** informe o número da NF de Venda que suportou a negociação entre as partes envolvidas na transferência.
- **Valor total:** informe o valor da NF de Venda que suportou a negociação entre as partes envolvidas na transferência.
- **Data de Emissão NF Venda:** preencha com a data de emissão da NF de Venda da negociação entre as partes envolvidas.
- **Observação:** informe quaisquer observações adicionais a serem consideradas no lançamento das notas da transferência.

> **Nota:** Esta seção não será exibida para o Tipo de Transferência Dev. Armazenagem >> Ent. Compra.

![Imagem 6: Nota: Esta seção não será exibida para o Tipo de Transferência Dev. Armazenagem >> Ent. Compra .](https://ajuda.sankhya.com.br/hc/article_attachments/20197910928919)

[GIF animado: Imagem 7: Nota: Esta seção não será exibida para o Tipo de Transferência Dev. Armazenagem >> Ent. Compra .](https://ajuda.sankhya.com.br/hc/article_attachments/4405464522135)

## Finalização e Histórico

Após concluir o preenchimento das informações e clicar em **"OK"**, a transferência será realizada, gerando a Nota de Devolução simbólica a partir do Contrato de Origem e a Nota de Entrada simbólica no Contrato de Destino. Ao final da operação, um pop-up com os **Documentos de Transferência** será exibido.

### Botão Transferir Serviços

Esta tela conta também com o botão **"Transferir Serviços"** que permite o acesso rápido à tela Apuração / Faturamento de Contratos, apresentando o contrato de origem com o "Tipo de Apuração" marcado como "Expedição/ Recepção" e com o "Status" de faturamento igual a "Aberto" e "Parcial". Esse botão pode ser acionado de duas formas:

1. **Ao finalizar uma operação de transferência:** apresentado diretamente no pop-up "Documentos de transferência".
2. **Ao consultar uma transferência já realizada:** exibido de forma fixa no Painel "Transferência".

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360054145694-Transfer%C3%AAncia-de-Propriedade#top)
