---
id: "44012365998615"
titulo: "[Routing] - Como utilizar o Filtro Importação ao iniciar uma nova sessão de roteirização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012365998615--Routing-Como-utilizar-o-Filtro-Importa%C3%A7%C3%A3o-ao-iniciar-uma-nova-sess%C3%A3o-de-roteiriza%C3%A7%C3%A3o"
trilha: "Lincros > Roteirizador"
atualizado_em: "2026-10-05T19:27:49Z"
rotulos: ["sync_hc", "lincros", "lincros_13433600", "sync_hash_5bdcc24529b1"]
---

# [Routing] - Como utilizar o Filtro Importação ao iniciar uma nova sessão de roteirização

**Menu**: Roteirizador > Roteirizar > Iniciar uma nova sessão de roteirização

Objetivo: Auxiliar no entendimento dos filtros para criação de uma nova sessão

**Considerações**:

         - Possuir pedidos importados e com status de "não roteirizados";

É comum durante o processo de criar uma nova sessão de roteirização, ao utilizar a opção Filtro Importação, que em alguns momentos nem todos os pedidos importados sejam apresentados em tela, mas há uma explicação pra isso. Durante a criação de uma nova sessão de roteirização é possível utilizar as opções presentes no Filtro Padrão bem como o Filtro Importação, sendo que este último possui algumas considerações.

Por exemplo, caso tenha importado um arquivo de pedidos onde as datas destes pedidos sejam diferentes, então é importante atentar-se ao filtro Data do pedido presente nos Filtros Padrão, pois ela é fundamental para que o sistema encontre os pedidos para serem roteirizados;

![Imagem 1: - Possuir pedidos importados e com status de "não roteirizados"; É comum durante o processo de criar uma nova sessão de…](https://ajuda.sankhya.com.br/hc/article_attachments/44012397091991)

Supondo que no arquivo de pedidos importados tenham dez (10) pedidos, sendo que seis (6) deles estão com data de entrega para o dia 1, outros três (3) para entrega no dia 2 e o outro para o dia 3. Então ao utilizar a opção de Filtro Importação, no caso, para buscar apenas os pedidos importados em um determinado arquivo, o sistema acaba validando o intervalo de datas informadas no filtro Data do pedido. Ou seja, se nos filtros de datas seja definido apenas as datas do dia 1 até o dia 2, então o sistema no exemplo dado retornaria apenas 9/10 pedidos pois 1 deles está com entrega definida para o dia 3. Por este motivo o mesmo não será apresentado para ser roteirizado.

O filtro de data em Período de importação refere-se a data em que foi importado o arquivo de texto com os pedidos, e não as datas do pedido em si - data dos pedidos é definida no Filtro Padrão, conforme explicado acima. Portanto caso perceba que um ou mais pedidos não estejam aparecendo nos filtros para roteirização, então deve-se checar o filtro de Data do pedido e aí validar se as datas batem com as datas presentes no arquivo de importação de pedidos.

![Imagem 2: Supondo que no arquivo de pedidos importados tenham dez (10) pedidos, sendo que seis (6) deles estão com data de…](https://ajuda.sankhya.com.br/hc/article_attachments/44012366357143)

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
