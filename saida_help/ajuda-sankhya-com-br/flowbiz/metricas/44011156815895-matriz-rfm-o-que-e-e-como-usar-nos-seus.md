---
id: "44011156815895"
titulo: "Matriz RFM: o que é e como usar nos seus fluxos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011156815895-Matriz-RFM-o-que-%C3%A9-e-como-usar-nos-seus-fluxos"
trilha: "Flowbiz > Métricas"
atualizado_em: "2026-10-05T18:57:35Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_1275", "sync_hash_53b87e733a38"]
---

# Matriz RFM: o que é e como usar nos seus fluxos

A Matriz RFM transforma o histórico de compras da sua audiência em respostas simples: quem tende a comprar de novo, quem precisa de atenção e quem já deveria ter voltado e ainda permite agir sobre cada grupo com campanhas e automações em poucos cliques.

**Disponibilidade:** recurso disponível nos planos **Flow, Prime, Premium e Corporativo**.

![Imagem 1: Disponibilidade: recurso disponível nos planos Flow, Prime, Premium e Corporativo .](https://ajuda.sankhya.com.br/hc/article_attachments/44011185937687)

## O que é RFM?

RFM é uma metodologia consolidada de segmentação de clientes baseada em três dimensões:

| Letra | Dimensão | O que mede |
| --- | --- | --- |
| **R** | Recência | Há quanto tempo o cliente fez o último pedido |
| **F** | Frequência | Quantos pedidos o cliente fez |
| **M** | Monetário | Quanto o cliente gastou |

A análise considera **apenas pedidos pagos dos últimos 12 meses**. Essa janela foi escolhida por capturar um ciclo completo de sazonalidade (Black Friday, Natal, Dia das Mães, volta às aulas) e uma amostra relevante do comportamento da sua base janelas curtas, de 30 ou 90 dias, classificariam como "perdidos" clientes cujo ciclo natural de recompra é mais longo.

## Como a classificação funciona

A Matriz RFM não usa regras fixas. Ela usa uma **distribuição** **estatística** por **quintis**: cada contato recebe uma nota de 1 a 5 em recência, frequência e valor monetário, sempre em comparação com o restante da sua própria base. Na prática, isso significa que a matriz se adapta ao seu negócio:

- Em uma loja em que a maioria dos clientes compra uma única vez ao ano, quem comprou duas vezes já pode ter frequência máxima.
- Em um negócio de reposição com recompra mensal, um "Campeão" pode precisar de dezenas de pedidos.

Por isso, não existe um critério universal do tipo "Campeão = 5 pedidos". A classificação reflete o comportamento real da sua base e é exatamente isso que a torna precisa.

**Visualmente, a matriz é uma grade 5x5**: o eixo horizontal representa a recência (quanto mais à direita, mais recente o último pedido) e o eixo vertical combina frequência e valor (quanto mais acima, mais e maiores compras). As 25 células são agrupadas em 11 segmentos fixos, como Campeões, Clientes Fiéis, Em Crescimento, Em Risco, Não Podemos Perdê-los, Perdidos e Prestes a Hibernar. Os Campeões são os melhores entre os clientes fiéis.

**Dica:** passe o mouse sobre qualquer segmento da matriz para ver a explicação daquele grupo.

- Atualização diária e posição dinâmica

**A matriz é recalculada uma vez por dia**, de madrugada. A posição de cada contato é definida pela data do seu pedido mais recente: um cliente em "Não Podemos Perdê-los" que compra hoje pode aparecer como "Campeão" no dia seguinte. Compras de hoje refletem no próximo recálculo a atualização não é em tempo real.

- **Posso editar ou ver a regra de um segmento?**

Os segmentos RFM são fixos e não editáveis — isso garante a integridade da metodologia estatística. E como a classificação é feita por pontuação comparativa (quintis), não existe uma "regra" isolada para exibir por segmento. Você pode ver todos os contatos de cada segmento e, se quiser critérios próprios, criar segmentos personalizados combinando os clusters RFM com outras regras.

## O dashboard da Matriz RFM

![Imagem 2: O dashboard da Matriz RFM](https://ajuda.sankhya.com.br/hc/article_attachments/44011157200663)

Ao acessar a Matriz RFM, você encontra para cada segmento:

- Número de clientes e de pedidos;
- Receita total do segmento;
- Ticket médio (receita ÷ pedidos) e LTV (receita ÷ clientes);
- Participação do segmento na base dos últimos 12 meses;
- Top 5 produtos e top 5 categorias mais comprados pelo grupo;
- Estatísticas de entrada e saída de contatos, dia a dia, em cada segmento.

**Observação:** se produtos ou categorias não aparecerem para a sua loja, normalmente é porque a sua plataforma de e-commerce não envia essas informações na integração. Nesse caso, fale com nosso suporte para confirmarmos.

## O campo RFM nas listas de contatos

Cada contato das suas listas agora possui o campo RFM, atualizado diariamente, com o segmento atual dele. Esse campo é global: funciona em qualquer lista inclusive na de assinantes, desde que o contato tenha histórico de pedido.

**Pontos importantes sobre esse campo:**

- **Contatos com o campo vazio** não possuem pedido pago nos últimos 12 meses (ou nunca compraram). Você pode filtrar "RFM está em branco" para alcançá-los.
- **Contatos "fora do intervalo"**: quem estava na matriz e completou mais de 12 meses sem comprar recebe um rótulo específico (Perdidos, Em Risco ou Não Podemos Perdê-los "fora do intervalo"). Ótimo para campanhas amplas de reativação: combine Perdidos + rótulos "fora do intervalo" + RFM em branco.
- **Os números da lista não batem com o dashboard — e isso é esperado.** A lista desconta descadastros, hard bounces e remoções manuais, enquanto o dashboard analisa o histórico completo de pedidos. A contagem da lista sempre será menor. A referência oficial é o dashboard da Matriz RFM.

**Recomendação importante:** use sempre os **segmentos RFM prontos** da plataforma. Não tente recriar os filtros manualmente — a classificação usa condições comparativas entre os grupos que não podem ser reproduzidas com filtros isolados (um Campeão, por exemplo, também pode ter pedidos de valor baixo).

## Como ativar os segmentos

Ver a matriz é só o começo. O valor real aparece quando você ativa cada segmento com comunicação direcionada. Há três caminhos:

- **Campanhas de e-mail:** Ao criar uma campanha de e-mail, na escolha dos destinatários você encontra os segmentos da Matriz RFM prontos para seleção. Escolha o segmento e dispare sem precisar montar filtros.
- **Campanhas de WhatsApp:** Na criação da campanha de WhatsApp, selecione diretamente o segmento RFM como destinatário. Ideal para ações rápidas: um cupom para "Em Risco", um lançamento para "Campeões".

**Observação:** o número final de destinatários pode ser menor que o total do segmento, pois somente contatos **com telefone cadastrado** recebem a campanha.

- **Fluxos de automação (jornadas):** Os segmentos RFM funcionam como **gatilhos de entrada** nos fluxos: assim que um contato **entra** em um segmento, a jornada correspondente é disparada automaticamente e quem sai do segmento pode parar de recebê-la. O processamento de entradas e saídas acontece uma vez ao dia.

Cada gatilho usa um segmento. Se quiser um fluxo que atenda vários clusters, crie um **segmento personalizado** combinando-os (ex.: "Em Risco OU Não Podemos Perdê-los") e use esse segmento no gatilho.

Você também pode **combinar RFM com qualquer outra regra de segmentação**, por exemplo: "Campeões **e** comprou a categoria X" e salvar como um novo público.

## Estratégias recomendadas para começar

Sugerimos estruturar fluxos automáticos para os segmentos de maior impacto:

| Segmento | Estratégia sugerida |
| --- | --- |
| **Campeões / Clientes Fiéis** | Reconhecimento, benefícios exclusivos, pré-lançamentos — mantenha seus melhores clientes engajados. |
| **Em Crescimento** | Incentivo à próxima compra para acelerar a fidelização. |
| **Em Risco** | Reengajamento com oferta ou conteúdo antes que deixem de comprar. |
| **Não Podemos Perdê-los** | Clientes de alto valor há muito tempo sem comprar — ação de recuperação com benefício relevante. |
| **Perdidos (+ fora do intervalo)** | Campanhas de reativação por e-mail e WhatsApp. |

Com fluxos ativos nos principais segmentos, a ferramenta passa a trabalhar sozinha: identifica quem precisa de atenção e dispara a ação certa, sem análise manual cliente a cliente.

## Perguntas frequentes

**Por que o total de um segmento na lista é menor que no dashboard?**

Porque a lista desconta descadastros, hard bounces e exclusões manuais. É o comportamento esperado — a referência é o dashboard.

**Por que um cliente com muitas compras não está em Campeões?**

A classificação considera apenas os últimos 12 meses e é comparativa com o restante da sua base. Compras antigas não entram no cálculo.

**Por que o campo RFM de um contato está vazio?**

Ele não tem pedido pago nos últimos 12 meses (ou nunca comprou).

**Posso mudar os critérios de um segmento?**

Não. Os segmentos são fixos por metodologia. Você pode criar segmentos personalizados combinando os clusters RFM com outras regras.

**Um assinante que nunca deveria ter RFM aparece classificado. É erro?**

Não. O campo RFM é global: se o contato tem histórico de pedido, ele recebe classificação em qualquer lista em que esteja.

**A campanha de WhatsApp saiu para menos gente que o tamanho do segmento. Por quê?**

Somente contatos com telefone cadastrado recebem a campanha.

Ficou com dúvidas? Fale com o nosso time de suporte e, se quiser ajuda para estruturar suas primeiras automações com RFM, o time de Sucesso do Cliente pode apoiar você.
