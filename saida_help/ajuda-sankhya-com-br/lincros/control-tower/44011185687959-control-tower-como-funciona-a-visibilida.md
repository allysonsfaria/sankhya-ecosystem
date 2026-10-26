---
id: "44011185687959"
titulo: "[Control Tower] - Como funciona a visibilidade da ativação de uma viagem"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011185687959--Control-Tower-Como-funciona-a-visibilidade-da-ativa%C3%A7%C3%A3o-de-uma-viagem"
trilha: "Lincros > Control Tower"
atualizado_em: "2026-10-05T18:57:44Z"
rotulos: ["sync_hc", "lincros", "lincros_13439085", "sync_hash_a3f3ddee4fe8"]
---

# [Control Tower] - Como funciona a visibilidade da ativação de uma viagem

Na versão 1.8 do Lincros Control Tower foi implementada uma funcionalidade que facilita a visibilidade de quando uma viagem será ativada para monitoramento;

Cada mensagem tem o intuito de orientar o usuário sobre a situação da ativação de uma viagem, uma vez que pode haver mais de uma viagem para a mesma placa ao mesmo tempo.

Por padrão, o sistema define qual viagem será ativada com base na agenda programada de carregamento. A ativação ocorre da mais antiga para a mais recente.

| Condição | Mensagem |
| --- | --- |
| Se a viagem não possuir uma placa associada | ![Imagem 1: Se a viagem não possuir uma placa associada](https://ajuda.sankhya.com.br/hc/article_attachments/44011185821335) |
| Se nenhuma das placas possuir um rastreador definido (número da antena e tecnologia) | ![Imagem 2: Se nenhuma das placas possuir um rastreador definido (número da antena e tecnologia)](https://ajuda.sankhya.com.br/hc/article_attachments/44011156976023) |
| Se algum das paradas não possuir uma coordenada cadastrada | ![Imagem 3: Se algum das paradas não possuir uma coordenada cadastrada](https://ajuda.sankhya.com.br/hc/article_attachments/44011186041751) |
| Quando a viagem é invalidada por tempo de execução superior ao parametrizado | ![Imagem 4: Quando a viagem é invalidada por tempo de execução superior ao parametrizado](https://ajuda.sankhya.com.br/hc/article_attachments/44011186141591) |
| Quando a viagem é invalidada por incompatibilidade de agenda | ![Imagem 5: Quando a viagem é invalidada por incompatibilidade de agenda](https://ajuda.sankhya.com.br/hc/article_attachments/44011203433111) |
| Quando a viagem é cancelada | ![Imagem 6: Quando a viagem é cancelada](https://ajuda.sankhya.com.br/hc/article_attachments/44011203622807) |
| Quando há mais de uma viagem para a mesma placa além da viagem que está em execução | ![Imagem 7: Quando há mais de uma viagem para a mesma placa além da viagem que está em execução](https://ajuda.sankhya.com.br/hc/article_attachments/44011203748503) |
| Quando a viagem é a próxima a ser ativada | ![Imagem 8: Quando a viagem é a próxima a ser ativada](https://ajuda.sankhya.com.br/hc/article_attachments/44011203843223) |
| Quando há apenas uma viagem para a placa, no entanto, o parâmetro de tempo de ativação ainda não foi atingido | ![Imagem 9: Quando há apenas uma viagem para a placa, no entanto, o parâmetro de tempo de ativação ainda não foi atingido](https://ajuda.sankhya.com.br/hc/article_attachments/44011195656087) |
| Quando a viagem está ativada. O tempo de ativação é considerado a partir da data programada de carregamento | ![Imagem 10: Quando a viagem está ativada. O tempo de ativação é considerado a partir da data programada de carregamento](https://ajuda.sankhya.com.br/hc/article_attachments/44011186871959) |
| Quando a viagem é finalizada manualmente | ![Imagem 11: Quando a viagem é finalizada manualmente](https://ajuda.sankhya.com.br/hc/article_attachments/44011171922071) |
| Quando a viagem é finalizada automaticamente pelo sistema ou por alguma integração | ![Imagem 12: Quando a viagem é finalizada automaticamente pelo sistema ou por alguma integração](https://ajuda.sankhya.com.br/hc/article_attachments/44011220805143) |

 "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
