---
id: "44011727059479"
titulo: "[Tracking] - Gestão de Entregas 02.00.060"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011727059479--Tracking-Gest%C3%A3o-de-Entregas-02-00-060"
trilha: "Lincros > Tracking"
atualizado_em: "2026-10-05T19:10:12Z"
rotulos: ["sync_hc", "lincros", "lincros_13434757", "sync_hash_515be561eb2c"]
---

# [Tracking] - Gestão de Entregas 02.00.060

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44011740690839)

Esta atualização é de extrema importância por que contem diversas melhorias internas que vão tornar sua experiência de uso bem mais fluída e sem travamentos. Trabalhamos duro para remover bugs e corrigir problemas de compatibilidade. Pra você visualmente não há mudanças, mas por trás dos panos melhoramos bastante a performance para consumir menos bateria do seu aparelho.

Agora é só iniciar sua viagem e mandar ver nas suas entregas.

- **Corrigimos o envio de posições repetidas:**Ajustamos o método de captura de posição que em alguns momentos duplicava os pacotes enviados para o sistema.

- **Travamentos da aplicação em locais sem sinal de rede:** Toda vez que o smartphone ficava sem sinal, as localizações capturadas geram eventos que eram armazenados em um banco de dados interno do smartphone e também eram armazenados na memória volátil do mesmo. A medida que a aplicação conseguia enviar as ocorrências, ele as removia do banco de dados, no entanto, devido à tentativas falhas de envio, elas se mantinham armazenadas na memória volátil. Quanto mais tempo o aparelho ficasse sem sinal, maior era o volume de dados que ele enviava quando recuperava o sinal. Isso só ficou evidente quando aplicamos as correções anteriores, pois haviam diversas situações que "matavam" esse job que fazia o envio das informações. Agora a aplicação apenas envia os dados que estão registrados no banco de dados e utiliza a memória volátil corretamente, impedindo que os mesmos dados sejam enviados mais de uma vez.

- **Envio de muitas informações ao mesmo tempo:**Antes era feito o envio de todas as ocorrências que estavam no banco de dados de uma só vez. Dependendo da quantidade de fotos que a aplicação tinha que enviar, isso acabava tornando o processo de envio da ocorrência ainda mais lento. Agora a aplicação serialize e envia a informação ao servidor com um timeout de 40 segundo

- ## Ícone da notificação fora do padrão

![Imagem 2: Ícone da notificação fora do padrão](https://ajuda.sankhya.com.br/hc/article_attachments/44011711023127)
