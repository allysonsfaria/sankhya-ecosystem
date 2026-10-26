---
id: "44012282616599"
titulo: "[Routing] - Release Notes 2.25"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012282616599--Routing-Release-Notes-2-25"
trilha: "Lincros > Releases (Atualizações) > Routing (Releases)"
atualizado_em: "2026-10-05T19:25:16Z"
rotulos: ["sync_hc", "lincros", "lincros_13433959", "sync_hash_1671ee6adea4"]
---

# [Routing] - Release Notes 2.25

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44012312455575)

## Melhorias:

- ## Exibir distância cliente x depósito

  - Adicionamos o campo ‘Distância depósito’ no cadastro do cliente, em que calcula a distância entre a geolocalização do cliente e depósito. Esta informação estará disponível na tela de cadastro do cliente e no relatório de clientes. Facilitando a análise da distância das entregas do depósito até seu destino.

![Imagem 2: Adicionamos o campo ‘Distância depósito’ no cadastro do cliente, em que calcula a distância entre a geolocalização do…](https://ajuda.sankhya.com.br/hc/article_attachments/44012312688663)

- ## Valor limite por tipo de veículo

  - Foi implementado o campo ‘valor’ no tipo de veículo, em que permite limitar a criação da rota automática caso atinga o valor máximo definido.
    Para que de fato seja limitado a criação da rota é necessário configurar o valor no tipo de veículo e habilitar o parâmetro X nas estratégias de roteirização.

![Imagem 3: Foi implementado o campo ‘valor’ no tipo de veículo, em que permite limitar a criação da rota automática caso atinga o…](https://static.intercomassets.com/assets/article_broken_image_placeholder.png)

![Imagem 4: Foi implementado o campo ‘valor’ no tipo de veículo, em que permite limitar a criação da rota automática caso atinga o…](https://static.intercomassets.com/assets/article_broken_image_placeholder.png)

- ## Remover atividades pelo laço

  - Adicionado a função de “Remover Atividades(s) da Rota” na ferramenta Laço, desta forma possibilitando que todos os pedidos selecionados possam ser removidos de uma rota existente.

![Imagem 5: Adicionado a função de “Remover Atividades(s) da Rota” na ferramenta Laço, desta forma possibilitando que todos os…](https://static.intercomassets.com/assets/article_broken_image_placeholder.png)

- ## Filtros de pedidos agrupados por data

  - Na tela da sessão de roteirização adicionamos o filtro ‘Pedidos’ (na lupa, localizado no canto direito superior). Ao abrir o filtro de pedidos e aplicar o filtro é listado os pedidos agrupados por data do pedido. Assim, possibilitando de localizar os pedidos mais antigos aos mais recentes e planejar a rota como desejado.

![Imagem 6: Na tela da sessão de roteirização adicionamos o filtro ‘Pedidos’ (na lupa, localizado no canto direito superior). Ao…](https://static.intercomassets.com/assets/article_broken_image_placeholder.png)

- ## Editar caminho antes da atividade

  - Ao editar o caminho da rota até/após a atividade, temos a possibilidade de visualizar todas as atividades das outras rotas (marcadas em cor cinza como padrão). Assim, facilitando a edição rota.
    Antes, isso não erá possível, ao editar a rota, todas as outras atividades das rotas distintas eram ocultadas em tela, sendo possível visualizar somente as atividades da rota que estava sendo editado.

    - Segue exemplo de ações: → [Clique aqui](https://drive.google.com/file/d/1ix385ex6uExDgigq_J75MBpVCdv2ClFK/view?usp=sharing)

- ## Parâmetro de início/fim do horário de trabalho do motorista

  - Adicionamos novos parâmetros nas estratégias de roteirização para possibilitar definir o horário de trabalho do motorista padrão de início e/ou fim e também para desconsiderar paradas de refeição.
    Assim, caso tenha alguma particularidade na criação de rotas de finais de semanas ou feriados, tem a possibilidade de configurar esses parâmetros como horário padrão do motorista para iniciar o planejamento da roteirização. Não tendo mais a necessidade de alterar cadastro por cadastro do horário do motorista.

![Imagem 7: Adicionamos novos parâmetros nas estratégias de roteirização para possibilitar definir o horário de trabalho do…](https://static.intercomassets.com/assets/article_broken_image_placeholder.png)

- ## Configuração de filtros na tela de iniciar uma nova sessão de roteirização

  - Agora será possível deixar expandido os filtros mais desejados e utilizados pelo usuário. Assim, tornando a criação da sessão mais ágil e prática.
    A configuração pode ser realizada pelos parâmetros do depósito no grupo “Configurações de Telas”.

![Imagem 8: Agora será possível deixar expandido os filtros mais desejados e utilizados pelo usuário. Assim, tornando a criação da…](https://static.intercomassets.com/assets/article_broken_image_placeholder.png)

![Imagem 9: Agora será possível deixar expandido os filtros mais desejados e utilizados pelo usuário. Assim, tornando a criação da…](https://static.intercomassets.com/assets/article_broken_image_placeholder.png)

- ## Padrão de cores para as rotas

  - Melhoria implementada voltada na experiência do usuário, criando um padrão de comportamento na coloração das rotas, na sessão de roteirização.
    Agora a cada acesso realizado na sessão, as rotas serão geradas com cores fixas, antes, sempre que gerado a sessão ou fosse reroteirizada, as cores eram atribuídas de forma aleatória.

    - Antes:

      ![Imagem 10: Antes:](https://static.intercomassets.com/assets/article_broken_image_placeholder.png)
    - Depois:

      ![Imagem 11: Depois:](https://static.intercomassets.com/assets/article_broken_image_placeholder.png)

- ## Rótulos em campos

  - Foi adicionado rótulos em campos na tela de iniciar uma nova sessão, com orientações sobre a sua funcionalidade. Facilitando ao usuário entender o funcionamento de cada filtro para gerar a sua sessão de roteirização.

![Imagem 12: Foi adicionado rótulos em campos na tela de iniciar uma nova sessão, com orientações sobre a sua funcionalidade.…](https://static.intercomassets.com/assets/article_broken_image_placeholder.png)

- ## Integração nativa dos volumes entre TMS x Routing x Tracking

  - Implementamos a informação de volume no recebimento desde dado proveniente do TMS e enviado posteriormente ao TRK, exibindo o dado de volumes na sessão de roteirização, dentro das informações das atividades e pedidos.
    Agora, será possível enviar o dado volume nos pedidos para exportação ao TRK, na integração por WebService ou via arquivos manuais.

![Imagem 13: Implementamos a informação de volume no recebimento desde dado proveniente do TMS e enviado posteriormente ao TRK,…](https://ajuda.sankhya.com.br/hc/article_attachments/44012287610263)

![Imagem 14: Implementamos a informação de volume no recebimento desde dado proveniente do TMS e enviado posteriormente ao TRK,…](https://ajuda.sankhya.com.br/hc/article_attachments/44012313072023)

![Imagem 15: Implementamos a informação de volume no recebimento desde dado proveniente do TMS e enviado posteriormente ao TRK,…](https://ajuda.sankhya.com.br/hc/article_attachments/44012333734039)
