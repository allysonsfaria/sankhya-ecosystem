---
id: "44010322514967"
titulo: "Como configurar Multi Origem do Mercado Livre"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010322514967-Como-configurar-Multi-Origem-do-Mercado-Livre"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:35:23Z"
rotulos: ["sync_hc", "magis5", "magis5_204055215213", "sync_hash_9a643909850a"]
---

# Como configurar Multi Origem do Mercado Livre

## Entenda nesse passo a passo como realizar a configuração de múltiplos depósitos do Mercado Livre dentro do Magis5 HUB para garantir o gerenciamento dos seus produtos corretamente.

---

Agora, no Mercado Livre, é possível cadastrar múltiplos depósitos **(localizações)** como endereços de coleta vinculados à sua conta.

![Imagem 1: Agora, no Mercado Livre, é possível cadastrar múltiplos depósitos (localizações) como endereços de coleta vinculados à…](https://ajuda.sankhya.com.br/hc/article_attachments/44010309328791)

![Imagem 2: Agora, no Mercado Livre, é possível cadastrar múltiplos depósitos (localizações) como endereços de coleta vinculados à…](https://ajuda.sankhya.com.br/hc/article_attachments/44010285127959)

Dentro do painel do Mercado Livre, você pode visualizar todas as suas localizações acessando a opção **"Preferencias de venda"** e depois**"Minhas Localizações".**

⚠️ **Atenção:** essa funcionalidade será liberada de forma gradual, inicialmente para um grupo selecionado de clientes pelo **Mercado Livre**.

Feito o login no Magis5, vá para **"Configurações"**, e por último clique em **"Marketplaces"**

![Imagem 3: Feito o login no Magis5, vá para "Configurações" , e por último clique em "Marketplaces"](https://ajuda.sankhya.com.br/hc/article_attachments/44010285227415)

Na tela de marketplace edite a integração do **Mercado Livre** que deseja realizar o ajuste de **"Multi origem"

![Imagem 4: Na tela de marketplace edite a integração do Mercado Livre que deseja realizar o ajuste de "Multi origem"](https://ajuda.sankhya.com.br/hc/article_attachments/44010309762199)**

Dentro da integração acesse a aba **"Deposito"**![Imagem 5: Dentro da integração acesse a aba "Deposito"](https://ajuda.sankhya.com.br/hc/article_attachments/44010309883415)

Na aba deposito você verá a listagem dos seus depósitos do BLING em **"Centro de distribuição"** e a opção para selecionar os depósitos do **Multi origem** do Mercado Livre.

![Imagem 6: Na aba deposito você verá a listagem dos seus depósitos do BLING em "Centro de distribuição" e a opção para selecionar…](https://ajuda.sankhya.com.br/hc/article_attachments/44010335494679)

Selecione a opção do depósito; em seguida, a **caixa de prioridade** será exibida. Defina nela a prioridade dos depósitos conforme configurado em seu ERP.

 **Exemplo de depósito configurado com prioridade preenchida:

![Imagem 7: Selecione a opção do depósito; em seguida, a caixa de prioridade será exibida. Defina nela a prioridade dos depósitos…](https://ajuda.sankhya.com.br/hc/article_attachments/44010335613847)**

**Como configurar a priorização de depósitos para baixa de estoque**Esta funcionalidade permite que o sistema faça a baixa de estoque em múltiplos depósitos **(multi-origem)** seguindo uma ordem de prioridade definida.

Defina a ordem de preferência utilizando um campo de prioridade nos cadastros dos depósitos.

1. **Tentativa de baixa no depósito prioritário:** o sistema verificará se há estoque disponível no depósito designado como prioritário (o que está alimentado o campo prioridade com o **valor 1**).
2. **Verificação de estoque insuficiente:** caso o depósito prioritário não possua estoque suficiente para atender ao pedido, o sistema avançará para o próximo depósito na lista de prioridades.
3. **Tentativa de baixa no depósito secundário (e subsequentes):** o sistema tentará baixar o estoque do próximo depósito na ordem de prioridade (o que está alimentado o campo prioridade com o **valor** 2).

⚠️ **Ponto de Atenção: É de extrema importância que a definição da ordem de prioridade do depósito esteja correta. Qualquer erro nesta definição impactará a funcionalidade de multi-origem e poderá resultar em baixas incorretas ou falhas no atendimento do pedido.**

Feito isso, clique em **"Vincular com depósito do canal de venda"** para associar o depósito do Mercado Livre.

![Imagem 8: Feito isso, clique em "Vincular com depósito do canal de venda" para associar o depósito do Mercado Livre.](https://ajuda.sankhya.com.br/hc/article_attachments/44010303381015)

![Imagem 9: Feito isso, clique em "Vincular com depósito do canal de venda" para associar o depósito do Mercado Livre.](https://ajuda.sankhya.com.br/hc/article_attachments/44010335820695)

Será exibida a lista de depósitos existentes no Mercado Livre. Após selecionar o depósito desejado, clique em **"Vincular".**

**Pronto! A configuração de Multi Origem no Mercado Livre foi concluída**

![Imagem 10: Pronto! A configuração de Multi Origem no Mercado Livre foi concluída](https://ajuda.sankhya.com.br/hc/article_attachments/44010319630487)

### Múltiplas Logísticas no Mercado Livre (Full, Flex e Cross)

Para vender o mesmo produto em diferentes canais de entrega (como **Full + Flex** ou **Full + Cross**) com estoques independentes, você precisa atender a três requisitos obrigatórios no Mercado Livre:

1. **Anúncio:** O anuncio deve  pertencer ao novo modelo de arquitetura de anúncios do **[Mercado Livre.](https://ajuda.sankhya.com.br/preco-por-variacao-e-multi-estoque-no-mercado-livre?hsLang=pt-br)**
2. **Conta Multi origem:** Sua conta de vendedor precisa ter permissão para gerenciar depósitos (seja um único depósito ou múltiplos depósitos).
3. **Serviço Liberado:** O tipo de envio desejado deve estar  disponível para o anúncio no Mercado Livre.

Exemplos de Uso:

- **Full + Cross:** Exige estoque físico no depósito do Mercado Livre e Full configurado.
- **Full + Flex:** Exige Full ativo, estoque no depósito físico e a opção **"controle de Flex por estoque"** habilitada.

⚠️ **Atenção:** Sem esses três requisitos, o estoque será unificado e você não conseguirá controlar as quantidades de forma independente para cada entrega.

![Universidade Magis5](https://ajuda.sankhya.com.br/hc/article_attachments/44010310608151)
