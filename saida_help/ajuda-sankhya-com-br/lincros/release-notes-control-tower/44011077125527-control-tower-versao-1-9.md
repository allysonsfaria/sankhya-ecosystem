---
id: "44011077125527"
titulo: "[Control Tower] - Versão 1.9"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011077125527--Control-Tower-Vers%C3%A3o-1-9"
trilha: "Lincros > Control Tower > Release Notes - Control Tower"
atualizado_em: "2026-10-05T18:53:50Z"
rotulos: ["sync_hc", "lincros", "lincros_13439730", "sync_hash_7547395dc9dd"]
---

# [Control Tower] - Versão 1.9

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44011036239127)

## Melhorias

- Monitoramento - Possibilidade de filtragem de anomalias não tratadas pelo Status da Carga

  - A partir da versão 1.9.0 no momento da geração/atualização das anomalias será gravado o status da carga no ato de sua geração/atualização, isso permitirá que as anomalias sejam filtradas e monitoradas considerando esta nova informação no módulo de monitoramento.
    Para filtrar as anomalias no módulo de monitoramento considerando o status da carga, basta preencher os filtros de “Anomalias não tratadas“ e “Status da rota/carga“, desta forma será considerado além do tipo de anomalia não tratada selecionado, também o status da carga em que a mesma foi gerada/atualizada, conforme imagem abaixo.

![Imagem 2: A partir da versão 1.9.0 no momento da geração/atualização das anomalias será gravado o status da carga no ato de sua…](https://ajuda.sankhya.com.br/hc/article_attachments/44011077534743)

- Foi disponibilizada a integração com a Demarco com objetivo de informar a Demarco se um determinado motorista está ou estava em viagem entre a Data X e a Data Y;

## Pequenas Melhorias

- Finalização automática de rota ao sair do raio da parada de destino;

  - Foi modificado um comportamento que faz com que a aplicação avalie se o veículo está dentro do raio apenas da coleta e não mais de destino, quando o veículo está executando o processo de pré-viagem, sendo assim mesmo recebendo posições neste raio, as mesmas serão desconsideradas. O comportamento antigo gerava inconsistências por que, durante a pré-viagem, quando o veículo mandava a primeira posição dentro do raio do destino (retornando de uma outra viagem) em vez do de coleta, gerava inconsistência na viagem impactando todos os demais processos, ocasionando assim a finalização da viagem de forma indevida.
- Erro ao exportar relatório apenas em Excel

  - Realizado tratamento nos componentes de filtro para atualizar a url de exportação do excel toda vez que um filtro é modificado.

Correções

- Corrigido pequenos bugs.

![Imagem 3: Corrigido pequenos bugs.](https://ajuda.sankhya.com.br/hc/article_attachments/44011052872215)
