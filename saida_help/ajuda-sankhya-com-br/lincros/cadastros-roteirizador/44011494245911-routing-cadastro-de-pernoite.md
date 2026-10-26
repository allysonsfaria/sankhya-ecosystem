---
id: "44011494245911"
titulo: "[Routing] - Cadastro de pernoite"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011494245911--Routing-Cadastro-de-pernoite"
trilha: "Lincros > Roteirizador > Cadastros - Roteirizador"
atualizado_em: "2026-10-05T19:05:05Z"
rotulos: ["sync_hc", "lincros", "lincros_13438254", "sync_hash_909d209ea769"]
---

# [Routing] - Cadastro de pernoite

**Menu:** Cadastros > Veículos

**Objetivo:** Entender como parametrizar o sistema para que de forma automática seja definida uma parada para descanso (pernoite) do motorista.

**Considerações**:

- Necessário possuir acesso ao sistema;
- Necessário possuir acesso ao menu: Cadastros > Veículos

Abaixo segue os procedimentos:

1. Necessário que em: Cadastros > Veículos os seguintes parâmetros sejam habilitados, conforme imagem abaixo:
          - Ativo;
          - Rota de vários dias;
          - Sair do depósito/ponto de apoio no início das entregas/coletas;
          - Volta para o depósito/ponto de apoio no término das entregas/coletas;

   ![Imagem 1: Necessário que em: Cadastros > Veículos os seguintes parâmetros sejam habilitados, conforme imagem abaixo: - Ativo; -…](https://ajuda.sankhya.com.br/hc/article_attachments/44011512948887)
2. Realizada a configuração acima, então quando for realizar a roteirização dos pedidos, e habilitar o parâmetro **"Permitir rotas de vários dias para os veículos configurados"**, então na montagem da rota o sistema de forma automática definirá o ponto de parada para repouso (pernoite) para o motorista. Esta parada será identificada no mapa pelo símbolo "P".

   ![Imagem 2: Realizada a configuração acima, então quando for realizar a roteirização dos pedidos, e habilitar o parâmetro "Permitir…](https://ajuda.sankhya.com.br/hc/article_attachments/44011545081623)
3. Um detalhe importante é que o sistema considera a informação definida nos campos "Hora início" e "Hora término", lá em Cadastros > Motoristas, para definir o horário de pernoite do motorista. Ou seja, a pausa para descanso iniciará logo após a hora final da jornada do motorista, e finalizará o descanso na hora de início de jornada do motorista.

   ![Imagem 3: Um detalhe importante é que o sistema considera a informação definida nos campos "Hora início" e "Hora término", lá em…](https://ajuda.sankhya.com.br/hc/article_attachments/44011538504983)

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
