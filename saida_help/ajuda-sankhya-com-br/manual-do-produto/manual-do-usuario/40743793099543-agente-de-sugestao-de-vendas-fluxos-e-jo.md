---
id: "40743793099543"
titulo: "Agente de Sugestão de Vendas: fluxos e jornadas do usuário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40743793099543-Agente-de-Sugest%C3%A3o-de-Vendas-fluxos-e-jornadas-do-usu%C3%A1rio"
trilha: "Manual do Produto > Comercial e Vendas > Vendas > Agente de Sugestão de Vendas > Manual do Usuário"
atualizado_em: "2026-07-29T16:13:00Z"
rotulos: ["Produtos", "Central de Vendas", "BIA", "Venda Mais", "Fluxo de Vendas", "Jornada do Usuário"]
---

# Agente de Sugestão de Vendas: fluxos e jornadas do usuário

##### Visão geral do fluxo

Acompanhe o fluxo do Agente de Sugestão de Vendas desde a alteração do carrinho até a ação do vendedor.
Considere que a sugestão é exibida no bloco com título "Sugestões com base no pedido" e descrição "Quem compra os itens no seu pedido também costuma comprar:".

![Imagem 1: Acompanhe o fluxo do Agente de Sugestão de Vendas desde a alteração do carrinho até a ação do vendedor. Considere que a…](https://ajuda.sankhya.com.br/hc/article_attachments/40743752111511)

ℹ️ Nota: Todas as recomendações, mensagens e textos gerados pelo agente respeitam automaticamente o idioma configurado para o seu usuário no Sankhya Om.

##### Identificação de gatilhos

Use estes gatilhos para entender quando a consulta é disparada:

- Inclua um produto no carrinho da Central de Vendas para disparar o evento de seleção de produto.
- Altere o carrinho (inclusão ou remoção de item) para disparar nova verificação de recomendação.
- Se a cesta possuir produtos com recomendação calculada, a notificação será exibida e, a partir da mesma, é possível abrir o painel de detalhes.

Considere as regras de bloqueio automático:

- Não consulte quando o carrinho estiver vazio.
- Não consulte quando o tipo de movimento não for elegível.
- Não repita consulta para estado lógico idêntico do carrinho.
- Não repita consulta para estado marcado com falha temporária até o carrinho mudar.

##### Jornada do vendedor - inserção de item

**Nota Importante sobre o Visualizador:** o painel de sugestões da Bia IA é **reativo**. Ele não fica visível permanentemente, sendo ativado automaticamente sempre que houver uma **mudança no carrinho** (inclusão ou remoção de itens). \* **Atenção:** Se o sistema estiver configurado para o **Layout Flex**, o painel de sugestões não ficará disponível.

Siga o passo a passo operacional:

- Acesse a Central de Vendas.
- Adicione o primeiro item aos itens da nota ou ao carrinho.
- Aguarde o sistema processar a consulta.
- Valide o estado "Carregando sugestões..." durante o processamento.
- Aguarde a exibição de uma das saídas:
  - Lista de sugestões no bloco "Sugestões com base no pedido".
  - Mensagem "Nenhuma sugestão disponível" quando não houver retorno elegível.

![Imagem 2: Mensagem "Nenhuma sugestão disponível" quando não houver retorno elegível.](https://ajuda.sankhya.com.br/hc/article_attachments/40743793094039)

**Experiência Omnichannel com a Bia:** As recomendações na Central de Vendas são as mesmas oferecidas pela **Bia (Agente Conversacional)**. Caso prefira interagir via chat, você pode solicitar sugestões diretamente à Bia, mantendo a consistência dos produtos recomendados.

##### Jornada do vendedor - aparição de notificação

Use a notificação flutuante como sinal de oportunidade:

- Observe o título da notificação com mensagens como:
  - "Oportunidade para vender mais!"
  - "Mais oportunidades!"
  - "Aumente o total da venda!"
- Observe o subtítulo com a quantidade de sugestões disponíveis.
- Clique na notificação para abrir o painel lateral quando quiser revisar as sugestões.
- Clique em "Fechar" para dispensar a notificação quando não quiser agir naquele momento.

![Imagem 3: Clique em "Fechar" para dispensar a notificação quando não quiser agir naquele momento.](https://ajuda.sankhya.com.br/hc/article_attachments/40743793094679)

##### Jornada do vendedor - aceitar sugestão

Execute a ação de aceite com os rótulos reais da interface:

- Localize o card do item sugerido.
- Confira os campos "Código" e valor com prefixo "R$".
- Leia a argumentação de venda exibida junto ao card, gerada a partir das características do produto sugerido.
- Ajuste quantidade com os botões de menos e mais, se necessário.
- Clique em "Adicionar" para incluir o item sugerido no carrinho.
- Aguarde a remoção imediata do item da lista de sugestões após sucesso.

Valide o comportamento esperado:

- Atualize o contador de sugestões disponíveis.
- Exiba "Nenhuma sugestão disponível" quando a última sugestão for adicionada.

![Imagem 4: Exiba "Nenhuma sugestão disponível" quando a última sugestão for adicionada.](https://ajuda.sankhya.com.br/hc/article_attachments/40743752113431)

##### Jornada do vendedor - ignorar sugestão

Use duas formas de ignorar sem interromper a venda:

- Ignore a notificação e continue o atendimento normalmente.
- Feche o painel lateral no botão de fechar quando não quiser atuar agora.

Considere o efeito operacional:

- Mantenha o fluxo de venda sem bloqueio.
- Reavalie novas sugestões quando o carrinho mudar.

##### Agente em linguagem natural - Copiloto BIA

Além das sugestões exibidas diretamente na jornada de vendas, o Agente de Sugestão de Vendas também está disponível em formato conversacional no Copiloto BIA.

![Imagem 5: Além das sugestões exibidas diretamente na jornada de vendas, o Agente de Sugestão de Vendas também está disponível em…](https://ajuda.sankhya.com.br/hc/article_attachments/40743752113815)

Por meio de comandos em linguagem natural, o usuário pode solicitar recomendações de produtos complementares de forma rápida e contextual, utilizando códigos ou descrições dos itens de interesse.

O agente analisa o histórico de vendas e o comportamento de compra para identificar combinações frequentes de produtos, sugerindo oportunidades de venda complementar diretamente na conversa.

#### Exemplos de utilização

- “Me recomende produtos complementares ao item 1019”
- “Quais produtos costumam ser vendidos junto com ACM SIGNBOND?”
- “Sugira itens complementares para os produtos 1019 e 2050”

#### Comportamento esperado

Ao receber a solicitação, o agente:

- identifica os produtos mencionados;
- consulta as regras e relações de venda existentes;
- prioriza sugestões mais relevantes;
- apresenta os produtos recomendados junto de uma breve justificativa contextual.

![Imagem 6: apresenta os produtos recomendados junto de uma breve justificativa contextual.](https://ajuda.sankhya.com.br/hc/article_attachments/40743793096599)

Essa experiência permite que vendedores consultem oportunidades de cross-sell sem sair do fluxo de atendimento, tornando a venda mais ágil, assistida e inteligente.

Além do componente embarcado na jornada de vendas, o agente de sugestões de vendas também possui interface conversacional, disponível no copiloto da BIA.
