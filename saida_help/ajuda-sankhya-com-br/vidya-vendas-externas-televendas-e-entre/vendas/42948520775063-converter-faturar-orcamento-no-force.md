---
id: "42948520775063"
titulo: "Converter/Faturar Orçamento no Force"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42948520775063-Converter-Faturar-Or%C3%A7amento-no-Force"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Vendas"
atualizado_em: "2026-08-24T16:42:06Z"
rotulos: ["sync_hc", "vidya", "sync_hash_3fc120cc9e3b", "vidya_476115"]
---

# Converter/Faturar Orçamento no Force

1. Configuração
   Para ativar à opção de conversão de orçamento dentro do Force, o parâmetro “Permite Faturar pelo App” deve estar marcado dentro da TOP de orçamento.

   ![Imagem 1: Configuração Para ativar à opção de conversão de orçamento dentro do Force, o parâmetro “Permite Faturar pelo App” deve…](https://ajuda.sankhya.com.br/hc/article_attachments/42956886989463)

   E as TOP’s de Destino (TOP’s que serviram para a conversão do orçamento. Ex: Pedido de venda), devem estar informadas dentro da Opção de Restrições/Exceções contida na opção de três pontos (…), também na tela da TOP de Orçamento.

   ![Imagem 2: Configuração Para ativar à opção de conversão de orçamento dentro do Force, o parâmetro “Permite Faturar pelo App” deve…](https://ajuda.sankhya.com.br/hc/article_attachments/42956891109015)
2. Utilização
   Após realizar a criação do Orçamento dentro do Force e enviado, ao clicar nos três pontos ( ⁝ ) a opção de Conversão/Faturamento aparecerá, porém, não selecionável. Isso ocorre pois o Orçamento está com o status diferente de Confirmado dentro do Sankhya, não podendo assim realizar a conversão.

   ![Imagem 3: Utilização Após realizar a criação do Orçamento dentro do Force e enviado, ao clicar nos três pontos ( ⁝ ) a opção de…](https://ajuda.sankhya.com.br/hc/article_attachments/42956904242839)

   Após realizar a confirmação do Orçamento dentro do Sankhya, e atualizar a tela de pedidos dentro do Force, a opção estará liberada para seleção.
   Ao selecionar, iremos para a tela de Converter/Faturar, onde são mostradas as seguintes informações:

   ![Imagem 4: Utilização Após realizar a criação do Orçamento dentro do Force e enviado, ao clicar nos três pontos ( ⁝ ) a opção de…](https://ajuda.sankhya.com.br/hc/article_attachments/42956861547543)

   Tipo de Operação:
   TOP que será escolhida para converter o Orçamento, atualizando a top de orçamento para a escolhida nesse momento.

   Tipo de Conversão / Faturamento:
   Normal - Escolhe os itens e gera o próximo movimento sem estar confirmado (ou seja, precisará abrir pra confirmar, também dando a opção de editar nesse período)

   Direto - Escolhe os itens e gera o próximo movimento já confirmando automaticamente (ou seja, se não tiver nenhuma liberação necessária ele vai ser confirmado direto)

   Por estoque - NÃO escolhe os itens, eles são escolhidos baseado no que tem disponível no estoque. Também é confirmado automaticamente se possível. O orçamento não fica disponível para faturar o restante depois.

   Por estoque deixando pendente - Mesma situação do item anterior, só que o documento de origem (no caso o orçamento), continua disponível para faturar novamente o restante depois.

   mais informações sobre os Tipos de Conversão / Faturamento: <https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#faturamento>
3. Data da Saída
   Data informada para a saída dos itens do pedido.

   Após informar esses dados, e seguimos, iremos para a tela de Selecionar itens para faturamento.
   Onde poderemos validas os itens e escolher Todos, ou alguns dos itens contidos inicialmente no Orçamento.
   Após basta clicar em Concluir, e estará finalizada a conversão, transformando o Orçamento em um Pedido de venda.

![Imagem 5: Data da Saída Data informada para a saída dos itens do pedido. Após informar esses dados, e seguimos, iremos para a…](https://ajuda.sankhya.com.br/hc/article_attachments/42956904623767)

O Orçamento ainda ficará disponível para ser gerado um outro pedido a partir dele.
