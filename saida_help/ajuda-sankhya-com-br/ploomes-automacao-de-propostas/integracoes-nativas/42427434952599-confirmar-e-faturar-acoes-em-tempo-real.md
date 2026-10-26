---
id: "42427434952599"
titulo: "Confirmar e Faturar: ações em tempo real pela integração Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427434952599-Confirmar-e-Faturar-a%C3%A7%C3%B5es-em-tempo-real-pela-integra%C3%A7%C3%A3o-Sankhya"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:01:46Z"
rotulos: ["sync_hc", "ploomes", "ploomes_11993949", "sync_hash_b8378bf7a1f1"]
---

# Confirmar e Faturar: ações em tempo real pela integração Sankhya

## 1) Ações em Tempo Real

Em complemento às funcionalidades de importação/exportação de dados e consultas em tempo real, agora também é possível realizar ações em tempo real no Sankhya. As ações possíveis são relacionadas aos Orçamentos e Pedidos de Venda Integrados.

As ações são:

- **Confirmação** de Orçamentos;
- **Faturamento** Direto de Orçamentos;
- **Confirmação** de Pedidos de Venda;
- **Faturamento** Direto de Pedidos de Venda.

Essas ações fazem parte fluxo padrão Sankhya para a geração de documentos no Portal de Vendas, conforme documentação Sankhya: [Portal de Vendas – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)

A confirmação representa a conclusão do documento gerado, e o faturamento gera um novo documento destino a partir de um documento de origem.

## 1.1) O que ocorre no Sankhya ao realizar essas ações?

**Ao confirmar um documento no Sankhya**, o que ocorre com o CabecalhoNota é a alteração do valor do campo `STATUSNOTA` para o valor `L-Liberada`. Caso existam regras de liberação de limite de crédito ou outras validações, ao executar a ação de confirmar no Sankhya, o documento vai para a tela de liberação aguardar a autorização de um usuário aprovador antes de ter seu `STATUSNOTA` alterado.

**Ao faturar um documento no Sankhya**, o que ocorre é a geração de num novo documento destino com base na TOP selecionada para o documento de destino. O faturamento segue a hierarquização de documentos no Sankhya, portanto:

- Ao faturar um Orçamento, é gerado um Pedido de Venda;
- Ao faturar um Pedido de Venda, é gerada uma Nota de Venda.

A geração de um documento novo a partir do faturamento no Sankhya, estabelece o vínculo dos documentos na entidade TGFVAR. Nessa entidade é estabelecido um vínculo entre o Nro. Único (`NUNOTA`) do novo documento criado com o Nro. Único de Origem (`NUNOTAORIG`).

Ao confirmar ou faturar um documento no Sankhya, podem ocorrer diversas rotinas no ERP que dependem da parametrização do Sankhya e independem do Ploomes ou da integração. Reserva de estoque de produtos e envio para liberação de limite de crédito são alguns exemplos, mas podem ser iniciados diversos processos que estejam configurados no Sankhya a partir dessas ações.

## 1.2) O que ocorre no Ploomes ao realizar essas ações?

**Ao confirmar um documento do Sankhya a partir do Ploomes**, ocorre o mesmo comportamento no Sankhya de alterar o valor do campo `STATUSNOTA` para o valor `L-Liberada` e os processos configurados no Sankhya a partir da confirmação serão iniciados no ERP. No Ploomes, será importada através do Pooling a alteração do campo `STATUSNOTA` e será exibido um modal exibindo o status **Confirmado** na tela do documento.

Ao faturar um documento do Sankhya a partir do Ploomes, ocorre o mesmo comportamento no Sankhya de gerar um documento destino para uma TOP selecionada.

- Se faturar um Orçamento do Sankhya integrado a uma Proposta no Ploomes, será gerado um Pedido de Venda no Sankhya que será importado pelo pooling para o mesmo negócio do Ploomes - desde que o gatilho de importação de Pedidos de Venda esteja ativo e que o ID do Negócio esteja mapeado e preenchido no Sankhya.
- Se faturar um Pedido de Venda do Sankhya integrado a uma Venda no Ploomes, será gerada uma Nota de Venda no Sankhya que será importada para o mesmo negócio do Ploomes - desde que o gatilho de importação de Notas de Venda esteja ativo e que o ID do Negócio esteja mapeado e preenchido no Sankhya.

---

## 2) Pré-requisitos

- Integração Plug&Play Sankhya ativa na conta.
- Usuário de integração precisa ter permissão de realizar Confirmação e Faturamento no Sankhya.
- Ao menos importação ou exportação de Propostas e/ou Vendas pela integração precisam ativas na conta.
- Proposta ou Venda precisa estar integrada ao Sankhya.

---

## 3) Configurando as Ações

A configuração das ações em tempo real de Propostas e Vendas estão disponíveis na tela de configuração da integração dentro das subseções de Orçamento e Nota de Venda.

![Imagem 1: A configuração das ações em tempo real de Propostas e Vendas estão disponíveis na tela de configuração da integração…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666897201/b90eb771f427e6e5eb03e6e59ef0/image+%283%29.png?expires=1786536000&signature=c085bd9805b379d1ea35e4ad1ba2e43195549433eb76ba91810020c6a4f7a0da&req=dSYhEMF3moNfWPMW3nq%2BgTvqOhE2AGMEiegs%2FzxMX2kEcGhemaI6m7cRwJs8%0A%2F%2FfRFM4dlFk6WdTSAjatdiCZKBk%3D%0A)

Dentro da subseção de Orçamento serão exibidos dois novos gatilhos para a regra de negócio: gatilho de confirmação e gatilho de faturamento.

![Imagem 2: Dentro da subseção de Orçamento serão exibidos dois novos gatilhos para a regra de negócio: gatilho de confirmação e…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666897942/ccb328dec232d32894320cc0cabb/image+%284%29.png?expires=1786536000&signature=955357d3405b41774b76baf5b3de6a0c134f7aa2432074b72caa6f6fb951a017&req=dSYhEMF3mohbW%2FMW3nq%2BgXrbNTeeMhbR0JrDOvJkh%2BP9H8AZzDZfObOmk8RF%0AQHNCXMzIn8DOiIdlEJEVCs8Zja0%3D%0A)

Exemplo da tela de configuração para a seção de Orçamentos.

**Gatilho de confirmação:** ao ativar este gatilho será exibido na tela de Proposta ou Venda um botão de ação para confirmar o documento integrado do Sankhya através do Ploomes. Esta ação é executada diretamente no Sankhya e confirma os dados do documento integrado conforme estão no Sankhya no momento da ação de confirmação.

**Gatilho de faturamento:** ao ativar este gatilho será exibido na tela de Proposta ou Venda um botão de ação para faturar o documento integrado do Sankhya através do Ploomes. Esta ação é executada diretamente no Sankhya e fatura os dados do documento integrado conforme estão no Sankhya no momento da ação de faturamento.

## 3.1) Configurando ações para Orçamento (Proposta)

Dentro da subseção de Orçamento serão exibidos dois novos gatilhos para a regra de negócio: gatilho de confirmação e gatilho de faturamento.

![Imagem 3: Dentro da subseção de Orçamento serão exibidos dois novos gatilhos para a regra de negócio: gatilho de confirmação e…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666920449/12cf4922959c4803432a23edbfcc/image+%285%29.png?expires=1786536000&signature=d07b478cc442f86ac57c11213b1ae0d6f1a553414445574932f3c5de27ec3e06&req=dSYhEMB8nYVbUPMW3nq%2BgeO906sauQoXPV1WDJ5VVBNGT0njHU1XMaIMvhXw%0A12wvedBcX4Al98ok22lpfBOE5UM%3D%0A)

Estes gatilhos poderão ser habilitados, desde que ao menos os gatilhos de importação ou exportação de Orçamentos do Sankhya estejam ativos na configuração.

![Imagem 4: Estes gatilhos poderão ser habilitados, desde que ao menos os gatilhos de importação ou exportação de Orçamentos do…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666921785/133a61944abd7cde0d5e0b26cbde/image+%286%29.png?expires=1786536000&signature=a0c01ad797de37e887ddb1082e525c477e013b0b90a1957afc87a6006b2e1001&req=dSYhEMB8nIZXXPMW3nq%2BgZ%2BTGJj653%2FM0qjBjnVB%2FLBcezmmtUMoyMiPQD5u%0A4dITZ2m1wlB2uCF%2BQpN7B0GiXlA%3D%0A)

Após ativar os gatilhos desejados é necessário selecionar quais funis do Ploomes terão o comportamento de exibir os botões de ação desejado na tela de Propostas.

![Imagem 5: Após ativar os gatilhos desejados é necessário selecionar quais funis do Ploomes terão o comportamento de exibir os…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666922553/608917de00d4d7ffd7487f262b6c/image+%287%29.png?expires=1786536000&signature=da1ee41e5ed1c7000629efe35149a518bf692490cd6555ca093d4e3b0c5bbe70&req=dSYhEMB8n4RaWvMW3nq%2BgWszZoQu65pa%2FfsHjQbCHIU1YK6IdnOrDc%2Fxc76B%0AClHMK9EQN7uP9i%2Bj1A17sGYXiL4%3D%0A)

Definindo quais gatilhos serão ativos na conta é preciso salvar a configuração da subseção e aplicar a edição para que a nova funcionalidade fique ativa na conta.

## 3.2) Configurando ações para Pedido de Venda (Venda)

Dentro da subseção de Pedido de Venda serão exibidos também dois novos gatilhos para a regra de negócio: gatilho de confirmação e gatilho de faturamento.

![Imagem 6: Dentro da subseção de Pedido de Venda serão exibidos também dois novos gatilhos para a regra de negócio: gatilho de…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666923560/58ecc50f4cb8bcffdbd428ac22c1/image+%288%29.png?expires=1786536000&signature=7c1688d717d797f2c867d4663a17468759eade001870d93b8ed28825750d5b14&req=dSYhEMB8noRZWfMW3nq%2BgfmRlDn0e3ZBckbzL5tv4%2Fu8vZVO0pM6QFlfPxYw%0AjQ1CDwm%2FOhlpqr%2FpT5MctbXcSzQ%3D%0A)

Estes gatilhos poderão ser habilitados, desde que ao menos os gatilhos de importação ou exportação de Pedidos de Venda do Sankhya estejam ativos na configuração.

![Imagem 7: Estes gatilhos poderão ser habilitados, desde que ao menos os gatilhos de importação ou exportação de Pedidos de Venda…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666923966/0b594999be881714bbd1d1da5e09/image+%289%29.png?expires=1786536000&signature=d50f2d7da1fa9e3c1af1243e99e7cfef5e9aacb1547c16f8d671b3fbc1b6edaf&req=dSYhEMB8nohZX%2FMW3nq%2BgUDcXUgD8Z%2Bmef7i9JwNTtiSCMR3HLvvmQ7O5y22%0ALWX3cFuubkBrw4895gpb4I8U04M%3D%0A)

Após ativar os gatilhos desejados é necessário selecionar quais funis do Ploomes terão o comportamento de exibir os botões de ação desejado na tela de Venda.

![Imagem 8: Após ativar os gatilhos desejados é necessário selecionar quais funis do Ploomes terão o comportamento de exibir os…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666924659/87a60428e130b531da7b9926a50a/image+%2810%29.png?expires=1786536000&signature=4a45d11165ac58ce4ea663a7b8e34233ee5704dbd8ee0f46cba2186e1c8363b4&req=dSYhEMB8mYdaUPMW3nq%2BgepSVFVxRHtiOBqvubZ15Tg4GVtdw9XuTOq9KHBd%0AGlanQiBGIChnk0cCX%2F6qPhgMOBw%3D%0A)

Definindo quais gatilhos serão ativos na conta é preciso salvar a configuração da subseção e aplicar a edição para que a nova funcionalidade fique ativa na conta.

---

## 4) Realizando Ações em Tempo Real

## 4.1) Confirmando um Orçamento

Ao abrir uma Proposta integrada, serão exibidos os botões de ação configurados.

![Imagem 9: Ao abrir uma Proposta integrada, serão exibidos os botões de ação configurados.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666925745/31af8c353254591131af128c774a/image+%2811%29.png?expires=1786536000&signature=5c39f6bc51f1b5d5cbfee0c43e4cf1908cdb2f81524024ef83668c9dceb61ed2&req=dSYhEMB8mIZbXPMW3nq%2BgTbZAlJVePhv79l6UQTQJ%2Bp3xdiNjxoFaW%2FtwD8u%0AiGx3FVgikuwpxfxYYRY4N5Qa%2B1U%3D%0A)

Ao acionar o botão de Confirmar, será aberta uma janela com informações sobre a ação de confirmação e com as opções de Visualizar Orçamento no Sankhya, Cancelar ou Confirmar Orçamento.

![Imagem 10: Ao acionar o botão de Confirmar, será aberta uma janela com informações sobre a ação de confirmação e com as opções de…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666926192/f7d0e45ac9893cd9753ba36c861c/image+%2812%29.png?expires=1786536000&signature=3297c84829e30d837e59286dbeca5b4456b0049bad74a72cc2c8dad7e6b66b13&req=dSYhEMB8m4BWW%2FMW3nq%2BgSHd1Zkk3Oje464nBlJphRBr7p8dxPJZTypc5vyO%0A7J%2FCO8OzHiJjo18SyYidST78T6U%3D%0A)

**Selecionando o botão Visualizar Orçamento**, será aberta uma janela com os dados consultados em tempo real no Sankhya para as entidades CabecalhoNota (TGFCAB) e ItemNota (TGFITE). Nessa visualização são consultados somente os campos mapeados. Dessa forma é possível validar os dados do Sankhya em tempo real e checar os dados do Sankhya antes da confirmação através do Ploomes.

![Imagem 11: Selecionando o botão Visualizar Orçamento , será aberta uma janela com os dados consultados em tempo real no Sankhya…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666926627/a8222f11e86c025247b2094524e2/image+%2813%29.png?expires=1786536000&signature=22b4d5e96227a1c935fcc4fb33b3b3d18b14fa215db11e0344d6b6f6208e05b3&req=dSYhEMB8m4ddXvMW3nq%2BgVWL%2BT8LhBoHuXdxcjlZY%2Bdh7GOM2iUxH5MV0Wa7%0A6Osd2Fwkz5iCBGHzvbLoZ7RTkhQ%3D%0A)

**Selecionando o botão Cancelar**, a tela com as opções será fechada e nenhuma ação será realizada.

**Selecionando o botão Confirmar Orçamento**, será realizada uma ação de confirmar no Sankhya para o NUNOTA vinculado à Proposta integrada. Caso a ação seja bem sucedida, será exibida uma mensagem de sucesso na tela.

![Imagem 12: Selecionando o botão Confirmar Orçamento , será realizada uma ação de confirmar no Sankhya para o NUNOTA vinculado à…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666927182/fc07c25306fc37e17258f98ee4d1/image+%2814%29.png?expires=1786536000&signature=c6ff9f2baadd3730b6bf71f4c0f39cbe0ef0ff84081be5f9530c63eb4078a735&req=dSYhEMB8moBXW%2FMW3nq%2BgYtLM1eoM7amA8JGABINe6DL5GmPH3n4ELAfSBLm%0AEQsqbUGKPj%2B2SaHcRE5JhqfaTpQ%3D%0A)

Caso algum erro ocorra na ação de Confirmação, será exibida uma mensagem de erro informando o erro recebido pelo Sankhya.

![Imagem 13: Caso algum erro ocorra na ação de Confirmação, será exibida uma mensagem de erro informando o erro recebido pelo…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666927989/a83f6689dee5d2edf62205b9ddcc/image+%2815%29.png?expires=1786536000&signature=3625a55687e198d66d117f90d62f2e352b72176031af5186ddbcf0372ceaf12b&req=dSYhEMB8mohXUPMW3nq%2BgYtsZRUZ1EkypMcI1w9Hik4Y3vRsFOYEI5bK3XX2%0AhDfUob5ok38NzYCcRze%2ByTigtag%3D%0A)

Após a confirmação será exibido um modal com o status Confirmado.

![Imagem 14: Após a confirmação será exibido um modal com o status Confirmado.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1677586884/eebc73b4e760c86280251ec4130c/image+%2831%29.png?expires=1786536000&signature=44d367e7f97f605d6f6022d2b175fca97d4c7ac4a79dcca481457b4fa753ff81&req=dSYgEcx2m4lXXfMW3nq%2BgSksRtWkzgn0B%2FpGBcySGu5FBPP6HYh%2B%2Bbs7ze4b%0AVN37aefyWKpxmfLWb4vGzYbjH38%3D%0A)

O status de confirmação é consultado no Sankhya em tempo real através do campo STATUSNOTA (se `STATUSNOTA = L`, então está **Confirmado**). Portanto, mesmo que ocorra uma Confirmação pelo Sankhya, essa informação constará na tela do Documento do Ploomes.

## 4.2) Faturando um Orçamento

Ao abrir uma Proposta integrada, serão exibidos os botões de ação configurados.

![Imagem 15: Ao abrir uma Proposta integrada, serão exibidos os botões de ação configurados.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666928628/9ac64ef011b9d1169e1ae85cc652/image+%2816%29.png?expires=1786536000&signature=34afb8b4843d642cd0e0dbe589fe3fca9c7919947ea305d4c93ac3c93a6f18e0&req=dSYhEMB8lYddUfMW3nq%2BgV8K60t96Az2%2FSO5rx0PWgh7UQX9Xje8ygSIdNwK%0A12dpNMq0HAwngghyBOgDQbO0KBc%3D%0A)

Ao acionar o botão de Faturar, será aberta uma janela com informações sobre a ação de faturamento e com um campo para informar a TOP do documento destino e as opções de Visualizar Orçamento no Sankhya, Cancelar ou Faturar Orçamento.

![Imagem 16: Ao acionar o botão de Faturar, será aberta uma janela com informações sobre a ação de faturamento e com um campo para…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666929067/1b79288e5dae0dcef8576cec8f7b/image+%2817%29.png?expires=1786536000&signature=54ae49a90c85abe35f91adca7a21812859ac4194d012bbddbcb19e8c0c3dfc51&req=dSYhEMB8lIFZXvMW3nq%2BgceUBWGgHzJYZ3uhaubYfUgiAJ%2BsrWLM8IPewt4Q%0A7ZlELX1gDt8pOMb4k5HoWJQj%2Fas%3D%0A)

**Selecionando o botão Visualizar Orçamento**, será aberta uma janela com os dados consultados em tempo real no Sankhya para as entidades CabecalhoNota (TGFCAB) e ItemNota (TGFITE). Nessa visualização são consultados somente os campos mapeados. Dessa forma é possível validar os dados do Sankhya em tempo real e checar os dados do Sankhya antes do faturamento através do Ploomes.

![Imagem 17: Selecionando o botão Visualizar Orçamento , será aberta uma janela com os dados consultados em tempo real no Sankhya…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666929458/0921ea1b103f3c669d75545027da/image+%2818%29.png?expires=1786536000&signature=8377fba3811ac7127113b214f59cc6def89131379969ae99f465c825737f5f11&req=dSYhEMB8lIVaUfMW3nq%2BgbioLz3Wc%2BOwM79mm0yW5FmrGQ%2Br6EtKr%2B9xk7RW%0AOA7dP2maRJfwPCQbSSTtgg644%2Fw%3D%0A)

**Selecionando o botão Cancelar**, a tela com as opções será fechada e nenhuma ação será realizada.

Antes de selecionar o botão Faturar Orçamento, é preciso preencher uma informação obrigatório que é a TOP para o Pedido de Venda que será gerado no Sankhya. Essa informação é obrigatória para realização do faturamento no Sankhya.

![Imagem 18: Antes de selecionar o botão Faturar Orçamento, é preciso preencher uma informação obrigatório que é a TOP para o Pedido…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666930682/c9e1e0794af2e2d984186fbec490/image+%2819%29.png?expires=1786536000&signature=aeb455648941cd13851fe19dfd224f4787a0292198db37ddb3fe5e3d79f1a68c&req=dSYhEMB9nYdXW%2FMW3nq%2BgXd76WmdsL6aZD9pTBpkS65Ublq%2FawecGdok4A40%0AtqAalfNtDZ8MIw0lBEx7bVbG9xs%3D%0A)

**Selecionando o botão Faturar Orçamento**, será realizada uma ação de faturar no Sankhya para o NUNOTA vinculado à Proposta integrada. Caso a ação seja bem sucedida, será exibida uma mensagem de sucesso na tela.

![Imagem 19: Selecionando o botão Faturar Orçamento , será realizada uma ação de faturar no Sankhya para o NUNOTA vinculado à…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666931157/439b45227645d628fced36d0656d/image+%2820%29.png?expires=1786536000&signature=114d7103148395445dced2b4d25d2255a37793f68ebb35e8cd78ce4587d49656&req=dSYhEMB9nIBaXvMW3nq%2BgV6fRdMtX%2BrPy%2F8TMHikl5DrhFikaBF5bME5ffl%2B%0AWuo%2B8LRuXQi1s6p6JtdgPYgD%2B6w%3D%0A)

Caso algum erro ocorra na ação de Faturamento, será exibida uma mensagem de erro informando o erro recebido pelo Sankhya.

Após o faturamento será exibido um modal com o status Faturado.

![Imagem 20: Após o faturamento será exibido um modal com o status Faturado.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1677589700/f3bf77683210b6b34702f0c520ba/image+%2832%29.png?expires=1786536000&signature=4b20f410ba761e67dcdd7bca5174093e49fb79576f642ebe220d2e9e99ae4f13&req=dSYgEcx2lIZfWfMW3nq%2BgRaoMZE2FR%2BpLDNGLkc1oHDoNB7s32lpTXv%2BGpy8%0AJCuzwkHzOrkhC0FYhW08oRDhSqs%3D%0A)

O status de faturamento é consultado no Sankhya em tempo real através do campo PENDENTE (se `PENDENTE = N`, então está **totalmente Faturado**). Portanto, mesmo que ocorra um Faturamento pelo Sankhya, essa informação constará na tela do Documento do Ploomes.

## 4.3) Confirmando um Pedido de Venda

Ao abrir uma Venda integrada, serão exibidos os botões de ação configurados.

![Imagem 21: Ao abrir uma Venda integrada, serão exibidos os botões de ação configurados.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666932261/85596c5323cae3c99f4752dcab95/image+%2821%29.png?expires=1786536000&signature=22f876210607112baa176b368670cb36a8a5f0735a46e5c4c3a97a594c675215&req=dSYhEMB9n4NZWPMW3nq%2BgfC4M9%2BWl4%2BGprMMAqeqZm389tQAWyb4w%2BMsRwd%2F%0AoO8PTqjGiolgwx4rOB%2FlD%2FrYokA%3D%0A)

Ao acionar o botão de Confirmar, será aberta uma janela com informações sobre a ação de confirmação e com as opções de Visualizar Pedido de Venda no Sankhya, Cancelar ou Confirmar Pedido de Venda.

![Imagem 22: Ao acionar o botão de Confirmar, será aberta uma janela com informações sobre a ação de confirmação e com as opções de…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666932620/c87277402e47e3180a79dd84f5f4/image+%2822%29.png?expires=1786536000&signature=4a0c22d5547b8aec08420a49bf39f4b0b9925c6ab2f7b634cb63d498f5297fa7&req=dSYhEMB9n4ddWfMW3nq%2Bgd0%2FMfqR4uQCGifNe174r%2FUBDT6RYPelFxHI5VTJ%0Auq9YrNIRV1M1QNwN4NODuwUgYn0%3D%0A)

**Selecionando o botão Visualizar Pedido de Venda**, será aberta uma janela com os dados consultados em tempo real no Sankhya para as entidades CabecalhoNota (TGFCAB) e ItemNota (TGFITE). Nessa visualização são consultados somente os campos mapeados. Dessa forma é possível validar os dados do Sankhya em tempo real e checar os dados do Sankhya antes da confirmação através do Ploomes.

![Imagem 23: Selecionando o botão Visualizar Pedido de Venda , será aberta uma janela com os dados consultados em tempo real no…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666934002/c374843495ecee5cbe658a45c94e/image+%2824%29.png?expires=1786536000&signature=22dbd7b0d0d622301e9ac9cbb07c49dc79561f5aa11dabe0b2b370ac7df39cef&req=dSYhEMB9mYFfW%2FMW3nq%2BgVq3PWuQKdaSex2nvdTHIe%2BtKx60j%2BcQRsXUID6R%0ABu%2FfaQp95pIYBN3q4R5HbJcjMXo%3D%0A)

**Selecionando o botão Cancelar**, a tela com as opções será fechada e nenhuma ação será realizada.

**Selecionando o botão Confirmar Pedido de Venda**, será realizada uma ação de confirmar no Sankhya para o NUNOTA vinculado à Venda integrada. Caso a ação seja bem sucedida, será exibida uma mensagem de sucesso na tela.

![Imagem 24: Selecionando o botão Confirmar Pedido de Venda , será realizada uma ação de confirmar no Sankhya para o NUNOTA…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666934567/543ca551a374e4fa55bf7d3590a9/image+%2825%29.png?expires=1786536000&signature=afa3a97c10ce9ff45a8f33a2f43ec331dcc5feaca580a814da9bca6dfcfa8755&req=dSYhEMB9mYRZXvMW3nq%2Bgb8%2FAWYear%2F4JLXQm0ipWZlgbtp%2F3O5WxX3SMVeG%0AoU5tAus95jMAc6rqcdWvaix9X8s%3D%0A)

Caso algum erro ocorra na ação de Confirmação, será exibida uma mensagem de erro informando o erro recebido pelo Sankhya.

Após a confirmação será exibido um modal com o status Confirmado.

![Imagem 25: Após a confirmação será exibido um modal com o status Confirmado.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1677587921/2fe0307b3753d3a1c62f2020a4eb/image%2B-2831-29.png?expires=1786536000&signature=7e4c7b6393e8314188c77bd5039e2ef70f9ad721dff44ade12f45e74df207f4c&req=dSYgEcx2mohdWPMW3nq%2BgQVhZvpvIiyjwptnFXFAVuBPFWdGBJ0tHwwqVute%0AgupEHHVLm8NuepoAod0p5bprAZ4%3D%0A)

O status de confirmação é consultado no Sankhya em tempo real através do campo STATUSNOTA (se `STATUSNOTA = L`, então está **Confirmado**). Portanto, mesmo que ocorra uma Confirmação pelo Sankhya, essa informação constará na tela do Documento do Ploomes.

## 4.4) Faturando um Pedido de Venda

Ao abrir uma Venda integrada, serão exibidos os botões de ação configurados.

![Imagem 26: Ao abrir uma Venda integrada, serão exibidos os botões de ação configurados.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666935170/8530c614fc4d4eb6409c3bd6c99f/image+%2826%29.png?expires=1786536000&signature=f31bf88a37a19af9c841b23575ef7b049b88332e517b29bb4f809acd5ad6cfba&req=dSYhEMB9mIBYWfMW3nq%2BgYMAUsdMeqCmmKg%2Fch%2BXXh%2FI0sVlG6e5s3n0l%2BxD%0Atvste8jpEZR2dN3JDn50bOLfIOo%3D%0A)

Ao acionar o botão de Faturar, será aberta uma janela com informações sobre a ação de faturamento e com um campo para informar a TOP do documento destino e as opções de Visualizar Pedido de Venda no Sankhya, Cancelar ou Faturar Pedido de Venda.

![Imagem 27: Ao acionar o botão de Faturar, será aberta uma janela com informações sobre a ação de faturamento e com um campo para…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666935927/6cfb37c1d1ba6434862290dd33f2/image+%2827%29.png?expires=1786536000&signature=edf481e8c65a9674bb44471187f011514511a617e2b0c1a124cd1004e1e13b95&req=dSYhEMB9mIhdXvMW3nq%2BgZdCjce%2BEVjRCaINhAaUK1THgHUeYKvxqRWQqp%2F9%0AJaNY6kw6ANtAgINS0GdtOqDOwLQ%3D%0A)

**Selecionando o botão Visualizar Pedido de Venda**, será aberta uma janela com os dados consultados em tempo real no Sankhya para as entidades CabecalhoNota (TGFCAB) e ItemNota (TGFITE). Nessa visualização são consultados somente os campos mapeados. Dessa forma é possível validar os dados do Sankhya em tempo real e checar os dados do Sankhya antes do faturamento através do Ploomes.

![Imagem 28: Selecionando o botão Visualizar Pedido de Venda , será aberta uma janela com os dados consultados em tempo real no…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666936314/3de815a71c2bda9f1d26fa6112a8/image+%2828%29.png?expires=1786536000&signature=7c60df262da41f4bfad397be128dcf6d8c0f91b1accae17389a952753a73c2ec&req=dSYhEMB9m4JeXfMW3nq%2BgXdkKdIhr3p7N20tedciPof2xqFOgmh0Uui6PPgI%0AxxvXuJsZuIqGMTPpXqA8MGvNudA%3D%0A)

**Selecionando o botão Cancelar**, a tela com as opções será fechada e nenhuma ação será realizada.

Antes de selecionar o botão Faturar Pedido de Venda, é preciso preencher uma informação obrigatório que é a TOP para a Nota de Venda que será gerada no Sankhya. Essa informação é obrigatória para realização do faturamento no Sankhya.

![Imagem 29: Antes de selecionar o botão Faturar Pedido de Venda, é preciso preencher uma informação obrigatório que é a TOP para a…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666936787/9de07b502c9f3c5f2d0153aa7e66/image+%2829%29.png?expires=1786536000&signature=529e74023b6c74c47a15a1f972712d9a7af600c1d6500c87429171fe05f6c817&req=dSYhEMB9m4ZXXvMW3nq%2BgXO6PzxWqTkNl%2BgB1%2FZS5rQIekmxw3xF2sD43XBj%0AtRUkPwxJ4%2FsVaig2c8FgO4iRWeQ%3D%0A)

**Selecionando o botão Faturar Pedido de Venda**, será realizada uma ação de faturar no Sankhya para o NUNOTA vinculado à Venda integrada. Caso a ação seja bem sucedida, será exibida uma mensagem de sucesso na tela.

![Imagem 30: Selecionando o botão Faturar Pedido de Venda , será realizada uma ação de faturar no Sankhya para o NUNOTA vinculado à…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1666937251/4a491e646ab33633bba9b6a74a07/image+%2830%29.png?expires=1786536000&signature=62bc1eb5ffeb3ac63e3c00ce0210e9efb9e21381d14bf608093423f90633a7c1&req=dSYhEMB9moNaWPMW3nq%2BgcOQcDBa52WRpRh3%2B7UjaK%2FKHJMFJfHpUkKkWFnY%0AGu55CXr3b4D4h0tYoxxjCoWjjUM%3D%0A)

Caso algum erro ocorra na ação de Faturamento, será exibida uma mensagem de erro informando o erro recebido pelo Sankhya.

Após o faturamento será exibido um modal com o status Faturado.

![Imagem 31: Após o faturamento será exibido um modal com o status Faturado.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1677591160/87093a84e56f75c849b019bbc621/image+%2833%29.png?expires=1786536000&signature=577be0372279f751333c68b8356c206d230cfd2481e7f7a79d3e35313f831640&req=dSYgEcx3nIBZWfMW3nq%2BgXTfJMGht3rx4O%2FLnb5M6DphXP1aqsQmnCGea38H%0A7XF4nCKX%2FkqmE4yXIcGHUKbPQXU%3D%0A)

O status de faturamento é consultado no Sankhya em tempo real através do campo PENDENTE (se `PENDENTE = N`, então está **totalmente Faturado**). Portanto, mesmo que ocorra um Faturamento pelo Sankhya, essa informação constará na tela do Documento do Ploomes.

---

## 5) FAQ

1. **É possível faturar um documento sem antes confirmar?**
   Não. No Sankhya essas ações são diretamente dependentes, é preciso que o documento primeiro seja Confirmado para depois ser Faturado.
2. **É possível confirmar ou faturar um documento não integrado?**
   Não. É preciso que o documento esteja integrado para realizar as ações, pois é necessário enviar ao Sankhya o NUNOTA do documento a ser confirmado/faturado e essa informação só está disponível nos documentos integrados.
3. **É possível configurar e habilitar somente a ação de confirmar ou de faturar?**
   Sim. É possível habilitar as ações de forma independente.
4. **É possível cancelar uma Confirmação ou Faturamento?**
   Não. Nem a Confirmação e nem o Faturamento são ações reversíveis. Caso seja necessário alguma alteração, é preciso realizar o cancelamento ou exclusão do documento no Sankhya diretamente.
