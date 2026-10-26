---
id: "44011403754263"
titulo: "[Routing] - Limite diário de importação de pedidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011403754263--Routing-Limite-di%C3%A1rio-de-importa%C3%A7%C3%A3o-de-pedidos"
trilha: "Lincros > Roteirizador > Cadastros - Roteirizador"
atualizado_em: "2026-10-05T19:02:12Z"
rotulos: ["sync_hc", "lincros", "sync_hash_b72fcc5989d9", "lincros_13438496"]
---

# [Routing] - Limite diário de importação de pedidos

**Menu**: Cadastros > Depósitos > Parâmetros do depósito > Parâmetros de importação

**Objetivo**: Entender qual a finalidade e impacto que este parâmetro tem no sistema

**Considerações**:

      - Possuir pedidos para serem importados (via integração e/ou arquivo de texto);

Importante: Somente usuários da Lincros possuem autorização para realizar alterações de parâmetros no sistema. Portanto, em caso de necessidade de alteração de algum parâmetro, deve-se entrar em contato via e-mail (atendimento@lincros.com), chat e/ou telefone através do número (47) 3237-5816 com nossa equipe de atendimento para podermos realizar essa manutenção nos parâmetros do depósito.

Nos parâmetros do depósito existe um parâmetro chamado "Limite diário de importação de pedidos", que basicamente tira uma média dos pedidos importados nos últimos dez (10) dias e aí acaba definindo um determinado valor no campo. Regra atual para definir o limite automático:

- Na versão 2.18 ou maior, depois de 10 dias, será adicionado 50% do dia com mais importações. Ou seja, se em 10 dias o depósito importou em média 1 pedido por dia, mas em algum dia importou 5.000 então o limite será de 7.500 (5.000 + 50%).

![Imagem 1: - Possuir pedidos para serem importados (via integração e/ou arquivo de texto); Importante: Somente usuários da Lincros…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1964902883/fefde120a7e9df80fbce800d2157/472884D3FEED0E87D28627C5092915E3?expires=1791331200&signature=aa8010e9367ad535f6bc5c52866b0ffc06e67679c5ba411538fbc6ba97171854&req=dSkhEsB%2Bn4lXWvMW3nq%2BgUAViDrGUg7KPS%2BwU1o9DonL1ySOlQ6hj5di2RoW%0ADV3TEfDX8YGuqHse%2BL369gaB%2Bxs%3D%0A)

Caso o sistema entenda que foi ultrapassado o limite diário de pedidos, então ao tentar importar pedidos no sistema, este retornará mensagem conforme imagem abaixo:

Erro: Com "total\_pedidos" importados o depósito "id\_deposito" passou do limite diário de "valor\_definido\_pelo\_parametro". Por favor entrar em contato com o suporte.

![Imagem 2: Caso o sistema entenda que foi ultrapassado o limite diário de pedidos, então ao tentar importar pedidos no sistema,…](https://ajuda.sankhya.com.br/hc/article_attachments/44011404337687)

A correção neste caso seria alterar o valor do parâmetro, por exemplo, para -1 que significa um valor ilimitado. Mas é importante ressaltar que nossa equipe de produto vem trabalhando em melhorias e futuramente será definido um valor "X" neste parâmetro de acordo com a regra mencionada acima. Regra essa que pode sofrer alguma alteração também. Contudo, por ora, todos depósitos foram definidos com o valor -1 (ilimitado).

**Obs:** Caso mesmo alterando o valor do campo do parâmetro **Limite diário de importação de pedidos** nos parâmetros de importações do depósito, o sistema siga apresentando a mensagem de erro, então a equipe de suporte (contato: atendimento@lincros.com ou (47) 3237-5816) deverá abrir uma demanda interna para que a equipe de infraestrutura possa estar checando a situação. Como a alteração fica salva em cache pode ser que a alteração não seja refletida imediatamente, portanto pode ser que seja necessário reiniciar o serviço WebApi.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
