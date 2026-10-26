---
id: "44010743161751"
titulo: "[Routing] - Rota Definitiva"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010743161751--Routing-Rota-Definitiva"
trilha: "Lincros > Roteirizador"
atualizado_em: "2026-10-05T18:45:31Z"
rotulos: ["sync_hc", "lincros", "lincros_13433561", "sync_hash_4bed38bdde09"]
---

# [Routing] - Rota Definitiva

**Menu**: Roteirizador > Roteirizar > Pesquisar por sessões já existentes e/ou iniciar uma nova sessão

**Objetivo**: Entender a mensagem exibida na sessão "Excluir rota. Rota definitiva."

## Considerações:

- É necessário possuir uma sessão com rota finalizada;
- A mensagem informa a impossibilidade de excluir rota, por estar finalizada;
- A rota finalizada não permite exclusão da mesma, inclusão ou exclusão de pedidos, mas permite editar o veículo.

1. No Routing há possibilidade de excluir uma rota, porém, devemos levar em consideração se ela já está finalizada ou não;

   ![Imagem 1: No Routing há possibilidade de excluir uma rota, porém, devemos levar em consideração se ela já está finalizada ou não;](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963496861/a63b2be54be8762b16e740c092a6/EA1B4DCFE10BAF80BDBE3F022EFEAC0B?expires=1791331200&signature=46fc7fd2d1a95c2cfe6809099c82f5e4ae2107daf9ce96ae6fe26953fa029d96&req=dSkhFc13m4lZWPMW3nq%2Bge3ZsLcQonCaq%2BLjXj8fCdAvbjs%2Fa0SqaCXykPh1%0AgVq24FsJrivoiNnxx2A2TU1VdwI%3D%0A)
2. Ao tentar executar a exclusão de uma rota já finalizada, é exibido a mensagem "Excluir rota - Rota Definitiva", impossibilitando a exclusão dela, pois uma rota já finalizada não poderá ser excluída;

   ![Imagem 2: Ao tentar executar a exclusão de uma rota já finalizada, é exibido a mensagem "Excluir rota - Rota Definitiva",…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963496890/94669ab69bf5dd4a5ab5be68a9b5/7E6D93CBC11020E8A52EA883038E47FF?expires=1791331200&signature=d69a03dfe1272746a29d14067192db75389e20adcf2e9b3113a6212e64d35dec&req=dSkhFc13m4lWWfMW3nq%2BgUukO1KkeZHf55UW2VN%2FMeVHNN4Ma%2BphHxiIbObg%0A%2FU6P3xXKjk6GQv12vcke7mJajSE%3D%0A)
3. Para identificar se a rota já está finalizada, ela estará exibida da seguinte forma na parte inferior do lado esquerdo da tela na sessão;

   ![Imagem 3: Para identificar se a rota já está finalizada, ela estará exibida da seguinte forma na parte inferior do lado esquerdo…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963496897/c9fa3a2592053f374da465b6087f/200C2D776A5F4EAA78B2D0B026C16CF3?expires=1791331200&signature=ae6c13dca5a7ed98093892486021d7b1d21aee03f2fbee1eb8fd7a2efe33ff18&req=dSkhFc13m4lWXvMW3nq%2BgQbUucBZySOOTO%2FwoKRrYfffRh4s3i%2Ft%2FT%2BBHor0%0AXTBdBJDwLyO2904j%2B7OozBFZSyc%3D%0A)

- Se a rota ainda não foi finalizada, poderá estar efetuando a exclusão dela seguindo os seguintes procedimentos.

Na tela da Sessão, selecionar a rota que deseja efetuar a exclusão na lateral esquerda, no canto inferior da sessão, onde consta a informação "**Rotas**":

![Imagem 4: Na tela da Sessão, selecionar a rota que deseja efetuar a exclusão na lateral esquerda, no canto inferior da sessão,…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963496923/4cba0528e89d4722f0b2d3f2c36f/69E333313D0DE87C55CEA38315951928?expires=1791331200&signature=c5fb6111ba606c23f567ec08c8d941718d5db9fc40363746f313f00ea95a29ad&req=dSkhFc13m4hdWvMW3nq%2BgQV0xBxdWNqQ6bi90W0jt4OMpgks%2FyQZzPOkZEyw%0AqGVlI27RXgm03nRbzAwX3x1y7c8%3D%0A)

4. No mapa estará a rota, clicando sobre a mesma com o botão direito do mouse, é exibido um "menu de opções" aonde contém a opção "**Excluir rota**":

![Imagem 5: 4. No mapa estará a rota, clicando sobre a mesma com o botão direito do mouse, é exibido um "menu de opções" aonde…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963496938/91a6fb22c962e8e77e11a335b741/B87B0790182479A6788A33FDA9D6C563?expires=1791331200&signature=f36a693a911659396841360e1823579feb5fe656e83d61c2b0c67c9185b583bc&req=dSkhFc13m4hcUfMW3nq%2Bgfy0MixVAi7D6icUYYSmX61Sn6puD2KIK6mVS4Re%0AAl5LmaWOXn0h%2BdLA4zmYqG5Vuh4%3D%0A)

Observação: Quando na sessão houver duas rotas para uma mesma placa ([rota de recarga](https://sankhya.zendesk.com/hc/pt-br/articles/44010743161751)), a mensagem também pode ocorrer, no caso de a segunda rota da placa estiver finalizada, a primeira rota não pode ser excluída, porque a exclusão influenciaria nos dados da segunda rota, e se ela está finalizada não pode mais ser editada. Já a ordem contrária (1ª rota finalizada, e a 2ª em aberto) não deve gerar a mensagem de rota definitiva, e deve permitir a exclusão da segunda rota.

**Conclusão**: Ao tentar realizar a exclusão de uma rota já finalizada, a mensagem que será exibida não se trata de um erro, mas sim um informativo de que uma rota estando finalizada não pode sofrer alteração.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
