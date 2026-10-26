---
id: "44011635960599"
titulo: "[Tracking] - Parâmetros de parada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011635960599--Tracking-Par%C3%A2metros-de-parada"
trilha: "Lincros > Tracking > Cadastros - Tracking"
atualizado_em: "2026-10-05T19:08:13Z"
rotulos: ["sync_hc", "lincros", "lincros_13438019", "sync_hash_e9b403d980c7"]
---

# [Tracking] - Parâmetros de parada

**Menu**: Configurações> Parâmetros> Parada

**Objetivo:** Explicar como funciona cada opção nos parâmetros de parada. 

O Tracking disponibiliza dois tipos de PNP's:

![Imagem 1: Menu : Configurações> Parâmetros> Parada Objetivo: Explicar como funciona cada opção nos parâmetros de parada. O…](https://ajuda.sankhya.com.br/hc/article_attachments/44011663098519)

- Esta é uma PNP gerada no raio de um cliente previsto na rota

![Imagem 2: - Esta é uma PNP gerada no raio de um cliente previsto na rota](https://ajuda.sankhya.com.br/hc/article_attachments/44011663260951)

-Este ícone representa uma PNP gerada fora do raio do cliente

![Imagem 3: -Este ícone representa uma PNP gerada fora do raio do cliente](https://ajuda.sankhya.com.br/hc/article_attachments/44011636579607)

**Minutos Parada Desligado:** Minutos parados para que seja apresentada a PNP no mapa sinótico com o veículo desligado.

Este parâmetro está relacionado a PNP gerada fora do raio do cliente. Logo, a geração da PNP será apresentada caso a parada atinja o período de 10 minutos;

**Metros Raio Parada Desligado**: É o raio que o tracking considera para validar se possui algum cliente da base de cadastros próximo quando é gerada uma PNP e retorna esse cliente na parte superior da PNP.

**Minutos Parada Ligado:** Minutos parados para que seja apresentada a PNP no mapa sinótico.
Este parâmetro está relacionado a PNP gerada fora do raio do cliente. Logo, a geração da PNP será apresentada caso a parada atinja o período de 10 minutos;

**Metros Raio Parada Ligado:** É o raio que o tracking considera para validar se possui algum cliente da base de cadastros próximo quando é gerada uma PNP e retorna esse cliente na parte superior da PNP.

![Imagem 4: Metros Raio Parada Ligado: É o raio que o tracking considera para validar se possui algum cliente da base de cadastros…](https://ajuda.sankhya.com.br/hc/article_attachments/44011663590679)

**Minutos Parada Entrega:** Minutos parados no cliente para que seja apresentada a PNP no mapa sinótico. As PNP's são geradas quando o veículo fica PARADO e atinge o tempo limite configurado nos parâmetros do Tracking. Este parâmetro está relacionado a PNP gerada dentro do raio do cliente. Sendo assim, será gerada uma PNP

![Imagem 5: Minutos Parada Entrega: Minutos parados no cliente para que seja apresentada a PNP no mapa sinótico. As PNP's são…](https://ajuda.sankhya.com.br/hc/article_attachments/44011663791895)

  caso a parada seja maior do que 3 minutos.

**Tempo (em minutos) para exibir demora de entrega:** A demora na entrega é caracterizada pela bolinha piscando na cor Laranja

![Imagem 6: Tempo (em minutos) para exibir demora de entrega: A demora na entrega é caracterizada pela bolinha piscando na cor…](https://ajuda.sankhya.com.br/hc/article_attachments/44011655384343)

. Configura-se aqui quantos minutos após o motorista entrar no raio do cliente, a bolinha da entrega começa a piscar Laranja.

**% de tempo aceitável:**Irá destacar a rota quando o motorista estiver X% do tempo previsto de atendimento. No exemplo apresentado, caso o motorista fique parado dentro do raio do cliente 50% do tempo de atendimento previsto, apresentará a cor Amarela:

![Imagem 7: % de tempo aceitável: Irá destacar a rota quando o motorista estiver X% do tempo previsto de atendimento. No exemplo…](https://ajuda.sankhya.com.br/hc/article_attachments/44011664071447)

**% de tempo intermediário:**Irá destacar a rota quando o motorista estiver X% do tempo previsto de atendimento. No exemplo apresentado, caso o motorista fique parado dentro do raio do cliente 100% do tempo de atendimento previsto, a cor ficará Laranja:

![Imagem 8: % de tempo intermediário: Irá destacar a rota quando o motorista estiver X% do tempo previsto de atendimento. No…](https://ajuda.sankhya.com.br/hc/article_attachments/44011655733783)

**% de tempo crítico:**Irá destacar a rota quando o motorista estiver X% do tempo previsto de atendimento. No exemplo apresentado, caso o motorista fique parado dentro do raio do cliente com 125% do tempo de atendimento previsto, a cor será Vermelha:

![Imagem 9: % de tempo crítico: Irá destacar a rota quando o motorista estiver X% do tempo previsto de atendimento. No exemplo…](https://ajuda.sankhya.com.br/hc/article_attachments/44011671254039)

**Notificar motorista por mensagem interna:**Caso os parâmetros acima de "% de tempo" estiverem ativas, o Tracking envia uma mensagem para o motorista informando.

**Metros Raio Cliente:**Utiliza esse valor para cadastrar o raio de um novo ponto de interesse.

**Metros Raio Cliente Próximo PNP:**É utilizado pelo processamento de ocorrências para validar se o tempo parado contabilizado será utilizado como PNP ou Tempo de Atendimento caso tenha um cliente da rota dentro do raio configurado;

**Utilizar raio do cliente no tempo de atendimento:**Utiliza o raio do cliente para contabilizar o tempo de atendimento.

**Contabilizar permanência no depósito:**Caso o Tracking identifique que o motorista está no raio do CDD, se esse parâmetro estiver ativo será contabilizado o tempo parado.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
