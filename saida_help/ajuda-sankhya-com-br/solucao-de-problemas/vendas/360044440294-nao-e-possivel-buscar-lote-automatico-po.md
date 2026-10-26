---
id: "360044440294"
titulo: "Não é possível buscar lote automático, pois não há estoque suficiente para o produto."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044440294-N%C3%A3o-%C3%A9-poss%C3%ADvel-buscar-lote-autom%C3%A1tico-pois-n%C3%A3o-h%C3%A1-estoque-suficiente-para-o-produto"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-31T01:23:52Z"
rotulos: ["#criadoRoger", "Produtos", "Configuração", "Estoque", "Preferências", "CORE_E04646", "avulsa", "Sem estoque para lote automático", "Estoque insuficiente ou vencido", "Verifique estoque; ative parâmetro se necessário", "Erro", "Artigo atualizado KCS", "CVE - KCS"]
---

# Não é possível buscar lote automático, pois não há estoque suficiente para o produto.

**MENSAGEM**

[CORE\_E04646]: Não é possível buscar lote automático, pois não há estoque suficiente para o produto.

**CAUSA**

Esta mensagem é apresentada durante o processo de explosão automática de lotes, ao tentar faturar um pedido de venda ou realizar um orçamento, quando não há estoque suficiente (considerando data de validade fora do vencimento) ou devido a configurações divergentes de estoque. Para detalhes sobre o processo: [Explosão Automática de Lotes.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599374)

**SOLUÇÃO**

**(1)** Certifique-se que para os itens do respectivo faturamento, que são controlados por lote, existe estoque suficiente para a operação.

**(2)** Caso não exista estoque suficiente, considere ativar o parâmetro **"IGNORAVALESTLT"**, mas faça isso somente se estiver de acordo com as regras de validação de estoque de sua empresa:

- Tela **"Preferências"** (Configurações >> Avançado)
- Chave **"IGNORAVALESTLT"** - Ignorar validação estoque quando lote automático?

![Imagem 1: Chave "IGNORAVALESTLT" - Ignorar validação estoque quando lote automático?](https://ajuda.sankhya.com.br/hc/article_attachments/15439543571479)

Quando este parâmetro está habilitado, o sistema não realiza a validação de estoque correspondente ao produto relacionado à explosão automática de lotes, desconsiderando o produto controlado por lote no faturamento.

**Verificação adicional:** Caso o erro persista, valide as seguintes possibilidades:

**• Configuração do Grupo de Produtos:** Acesse a tela **"Grupos de Produtos"** (Configurações >> Cadastros >> Produtos >> Grupos de Produtos) e verifique o campo **"Validar Estoque"**. Se estiver como **"Nenhuma"**, altere para **"Local/Empresa"** se esta for a melhor opção para o seu processo.

**• Estoque Reservado em Outros Pedidos:** Consulte se existem pedidos pendentes comprometendo o saldo. Caso identifique pedidos que não serão faturados, selecione o **"Botão Outras Opções"** e em seguida a opção **"Marcar como Não Pendente"**.

**• Divergência de Local de Estoque:** Verifique se o local de estoque no pedido corresponde ao saldo disponível. No cadastro do produto, aba **"Medidas e Estoque"**, verifique a opção **"Usa Local"**.

**• Ausência Real de Estoque:** Consulte o saldo na tela de consulta de estoque (Estoque >> Consultas >> Consulta de Estoque) e, se necessário, realize um lançamento de ajuste de entrada para regularizar o saldo.
