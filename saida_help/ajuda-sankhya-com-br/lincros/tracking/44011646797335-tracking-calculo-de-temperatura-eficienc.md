---
id: "44011646797335"
titulo: "[Tracking] Cálculo de Temperatura - Eficiência de Frio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011646797335--Tracking-C%C3%A1lculo-de-Temperatura-Efici%C3%AAncia-de-Frio"
trilha: "Lincros > Tracking"
atualizado_em: "2026-10-05T19:07:25Z"
rotulos: ["sync_hc", "lincros", "lincros_13438079", "sync_hash_d5f509991ebb"]
---

# [Tracking] Cálculo de Temperatura - Eficiência de Frio

## Objetivo

Este artigo lhe auxiliará na dinâmica de cálculo e configuração da Eficiência de Frio (Temperatura) disponível no Lincros Tracking

## Pré-requisito

Primeiramente, cadastre os tipos de produto aos quais a sua operação trabalha: congelado, resfriado, quente, etc.

## Caminho

Menu > Cadastros > Tipo de Produto:

![Imagem 1: Menu > Cadastros > Tipo de Produto:](https://ajuda.sankhya.com.br/hc/article_attachments/44011615625879)

Informe as temperaturas **mínima** e **máxima** do tipo de produto cadastrado, conforme imagem abaixo demonstra. Elas serão consideradas no cálculo de eficiência:

![Imagem 2: Informe as temperaturas mínima e máxima do tipo de produto cadastrado, conforme imagem abaixo demonstra. Elas serão…](https://ajuda.sankhya.com.br/hc/article_attachments/44011630863639)

Caso haja outro tipo de produto cadastrado, repita o mesmo procedimento acima.

## Conceito

Quando o motorista inicia uma viagem, o sistema verifica os tipos do produto de cada entrega e cria a meta do frio. Essa meta é criada baseada nas informações de Tipos de Produto cadastrados no sistema, conforme demonstrado anteriormente:

![Imagem 3: Quando o motorista inicia uma viagem, o sistema verifica os tipos do produto de cada entrega e cria a meta do frio.…](https://ajuda.sankhya.com.br/hc/article_attachments/44011631058071)

Com a meta criada, o sistema irá receber as temperaturas via integração entre **Rastreador** e **Lincros Tracking** e verificar se a mesma está dentro da meta.

Na imagem abaixo, temos uma rota com entrega de produtos congelados (de 0º a -45ºC). A meta pode ser identificada pela área demarcada em azul. A temperatura enviada pelo rastreador é demarcado pelo tracejo de cor vermelho:

![Imagem 4: Na imagem abaixo, temos uma rota com entrega de produtos congelados (de 0º a -45ºC). A meta pode ser identificada pela…](https://ajuda.sankhya.com.br/hc/article_attachments/44011616136215)

**Importante!** Caso a rota possua entregas com tipos de produto misto (CONGELADO e RESFRIADO), será considerado prioritariamente a meta do primeiro produto cadastrado. No nosso caso, **CONGELADO**. Assim que for realizada a entrega de todos os produtos congelados e, ainda assim, houver produtos resfriados pendentes de entrega, a meta passa a considerar as temperaturas mínima e máxima do produto **RESFRIADO**.

No gráfico aparece somente quando há mudança de temperatura. Verificar os horários apresentados para a temperatura no Gráfico.

Para verificar os registros completos de temperatura que geraram a porcentagem. Isto pode ser visto no relatório Temperaturas Registradas na Rota.

O monitoramento do frio é inicializado a partir do horário de início de rota e permanece enquanto houver mercadoria no caminhão, ou seja, até que a última entrega seja apontada via smartphone. O cálculo da porcentagem do frio considera o tempo total da rota dentro da meta dividido pelo tempo total que o sistema recebeu a temperatura.

**OBS**: Caso haja apontamento de devolução, o cálculo de eficiência do frio permanecerá até que a rota seja finalizada

## Gráfico de Temperaturas

![Imagem 5: Gráfico de Temperaturas](https://ajuda.sankhya.com.br/hc/article_attachments/44011608707223)

- Para acessar o gráfico de temperaturas, clique no ícone representado por um "termômetro" no painel de entregas na tela de monitoramento;
- Para acompanhar a porcentagem de eficiência obtida em cada rota até o momento, basta localizar a coluna "% Eficiência". Lembrando que, enquanto houver entregas pendentes na viagem, a porcentagem poderá ser alterada.

**Dica**: Não deixe de conferir com nossa equipe quais tecnologias de rastreador o **Lincros Tracking** já possui integração para o envio de temperaturas.
