---
id: "44011632312087"
titulo: "[Routing] - Release Notes 2.26"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011632312087--Routing-Release-Notes-2-26"
trilha: "Lincros > Releases (Atualizações) > Routing (Releases)"
atualizado_em: "2026-10-05T19:07:35Z"
rotulos: ["sync_hc", "lincros", "lincros_13438067", "sync_hash_d3e7d5a89bf2"]
---

# [Routing] - Release Notes 2.26

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44011632518551)

## Melhorias:

- ## Relatório de Romaneio e Roteirização - Renomear o filtro de datas

Alterado o texto do campo de data, para deixar mais claro que o filtro da data é por data do roteiro, conforme imagem abaixo:

![Imagem 2: Alterado o texto do campo de data, para deixar mais claro que o filtro da data é por data do roteiro, conforme imagem…](https://static.intercomassets.com/assets/article_broken_image_placeholder.png)

- ## Fixar valores para rotas de vários dias em uma sessão de roteirização

Implementamos na rota manual na tela de seleção de veículo, a funcionalidade de gravar o valor preenchido pela primeira vez no campo “Quantidade máxima de dias em rota” e removemos o campo “Permitir rotas de vários dias”. Assim, ao criar uma nova rota manual, o sistema busca o valor utilizado na primeira rota e preenche o campo automaticamente, facilitando a criação das rotas manuais que atende as rotas de vários dias.

![Imagem 3: Implementamos na rota manual na tela de seleção de veículo, a funcionalidade de gravar o valor preenchido pela primeira…](https://static.intercomassets.com/assets/article_broken_image_placeholder.png)

- ## Filtro Numero Sessão e Número Pedido Tela Pedidos

Na tela de pedidos foi adicionado filtro que permite buscar os pedidos vinculados a uma sessão. Também foi alterado para que ao buscar um pedido pelo número não seja obrigatório informar a data do mesmo.Campo novo de sessão:

![Imagem 4: Na tela de pedidos foi adicionado filtro que permite buscar os pedidos vinculados a uma sessão. Também foi alterado…](https://static.intercomassets.com/assets/article_broken_image_placeholder.png)

- ## Botão "Histórico" nos cadastros

Adicionado o histórico nos cadastros abaixo, que apresentará as alterações realizadas pelos usuários.

- Setor;
- Usuário;
- Veiculo;
- Tipo Veiculo;
- Clientes;
- Motorista;
- Transportadora;
- Estratégia de Roteirização;
- Deposito;
- Checkpoint;
- Ponto de Apoio;

Localização do botão nos cadastros:

![Imagem 5: Localização do botão nos cadastros:](https://static.intercomassets.com/assets/article_broken_image_placeholder.png)

- ## Real tonelada e real quilo

Adicionado nas informações de rota selecionada os valores de **custo por tonelada** e **custo por quilo**.Estas novas informações poderão ser extraídas pelo relatório de roteirização, permitindo controle dos fluxos.

![Imagem 6: Adicionado nas informações de rota selecionada os valores de custo por tonelada e custo por quilo .Estas novas…](https://static.intercomassets.com/assets/article_broken_image_placeholder.png)

- ## Vinculo das estratégias de roteirização com os setores

Adicionado no cadastro de setor a possibilidade de vincular uma estratégia de roteirização, permitindo que o cliente utilize uma estratégia para sessão e outras para setores específicos. O setor que não possuir estratégia selecionada utilizará a mesma informada no início da sessão.

![Imagem 7: Adicionado no cadastro de setor a possibilidade de vincular uma estratégia de roteirização, permitindo que o cliente…](https://static.intercomassets.com/assets/article_broken_image_placeholder.png)

![Imagem 8: Adicionado no cadastro de setor a possibilidade de vincular uma estratégia de roteirização, permitindo que o cliente…](https://ajuda.sankhya.com.br/hc/article_attachments/44011624375703)
