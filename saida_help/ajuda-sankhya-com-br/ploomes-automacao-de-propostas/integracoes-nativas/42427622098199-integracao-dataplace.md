---
id: "42427622098199"
titulo: "Integração Dataplace"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427622098199-Integra%C3%A7%C3%A3o-Dataplace"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:06:26Z"
rotulos: ["sync_hc", "ploomes", "ploomes_8124896", "sync_hash_00993bfc2fc2"]
---

# Integração Dataplace

O Dataplace é um ERP com mais de 30 anos de mercado e com centenas de clientes dentro e fora do Brasil. Com ele você integra e controla o seu departamento de compras, financeiro, a manufatura dos seus produtos (mesmo em terceiros), faz controle por lotes, gera orçamentos e pedidos de vendas, gerencia o faturamento e as notas fiscais, integra meios de pagamento, marketplaces e automatiza a sua força de vendas.

Através da integração entre o Dataplace ERP e o Ploomes, seus clientes, contatos, produtos, orçamentos e pedidos de venda são sincronizados.

## Escopo da integração

Importante!

O e-mail é um campo obrigatório no cadastro de usuários do Ploomes. Caso esta informação não esteja preenchida no cadastro do usuário no Dataplace, um e-mail fictício será criado para este usuário no Ploomes. Para evitar custos não previstos para o cliente, todos os usuários criados automaticamente via integração serão categorizados como “Usuários de integração”, porém não permite acesso ao sistema e será usado apenas para vincular os clientes, orçamentos e pedidos aos respectivos vendedores. Caso seja desejável liberar um acesso real para o vendedor em questão, o time de parcerias da Ploomes poderá alterar a configuração do usuário para permitir acesso ao CRM, o que resultará no custo de uma licença adicional do Ploomes para o cliente final.

- ### Clientes

**Comportamento:**

**Do Dataplace para o Ploomes:** sempre que há uma criação ou atualização de clientes no Dataplace, seus dados cadastrais são enviados ao Ploomes. Clientes já sincronizados, quando atualizados no Ploomes, são enviados ao Dataplace.

![Imagem 1: Do Dataplace para o Ploomes: sempre que há uma criação ou atualização de clientes no Dataplace, seus dados cadastrais…](https://downloads.intercomcdn.com/i/o/784591984/4716acf69b3c371f7e28e41a/image.png?expires=1786536000&signature=07f9e430f7062fa90a61b3c9333180fca16cbb2ebb7455d72ab9de104c18a377&req=cygjE8B%2FlIlbFb4V1XW4gSTd0qOpQVnf%2By753yHiBixsgYcjdOVg47fMHsHc%0AzrEweC%2BxxJolduPrIbhtL5hFHg%3D%3D%0A)

**Do Ploomes para o Dataplace:** quando um cliente do Ploomes estiver com o campo “Enviar para o Dataplace” (booleano) marcado como “True”, o cliente será enviado para o Dataplace (por enquanto apenas cria no Dataplace, mas não atualiza). Desta forma, é possível utilizar o recurso de Automações para escolher quando o cliente deve ser enviado, por ex.: quando chegar em determinada fase do funil ou quando tiver todos os dados principais preenchidos.

![Imagem 2: Do Ploomes para o Dataplace: quando um cliente do Ploomes estiver com o campo “Enviar para o Dataplace” (booleano)…](https://downloads.intercomcdn.com/i/o/784592877/952b3bab45d5fe9b6f9bbd26/image.png?expires=1786536000&signature=46ecfbb96b0f14dfce0a1c79ca0c474a081d1af82e3963e6dc2b5efcacc20b3c&req=cygjE8B8lYZYFb4V1XW4gZLJvzlwY%2BO15cR%2BKMPsX7Q5EN%2Ff4TgQs3vMs9X1%0Ah8%2Bp2UKiwsP%2BMKle3GfnWh4a%2Bw%3D%3D%0A)

**Dados sincronizados:** Código Dataplace, Nome, Razão Social, CNPJ, Telefone, E-mail, Site, Endereço (entrega e faturamento), Inscrição Estadual e Vendedor.

- ### Produtos:

**Comportamento:** sempre que um produto é criado ou atualizado no Dataplace ocorre a sincronização com o Ploomes.

![Imagem 3: Comportamento: sempre que um produto é criado ou atualizado no Dataplace ocorre a sincronização com o Ploomes.](https://downloads.intercomcdn.com/i/o/784593802/ead67ba5ae4b207ea19e70a3/image.png?expires=1786536000&signature=1a3157a8678d5b821810794bae464f0678693611bf6f306ca4c12ace42112998&req=cygjE8B9lYFdFb4V1XW4gSz3HxXGktgnoy90cCAZ0idsQxKUEPFY%2FmM60hUs%0AuuN7eki9%2BZQuG3P0vU9CHhhydw%3D%3D%0A)

**Dados sincronizados:**

- Nome
- Código
- Grupo (Categoria)
- NCM
- Peso líquido
- Peso bruto
- Unidade de peso
- Altura
- Largura
- Comprimento
- Descrição de compra
- Descrição de venda
- Observações
- Custo

- ### Orçamentos:

**Comportamento:** sempre que um orçamento é criado no Dataplace, uma cópia é enviada ao Ploomes e uma negociação é criada em um estágio e funil pré-determinados. Quando o orçamento é atualizado no Dataplace, este é Revisado no Ploomes, para que uma nova versão seja criada e se mantenha o histórico de modificações do orçamento, para melhor acompanhamento comercial.

![Imagem 4: Comportamento: sempre que um orçamento é criado no Dataplace, uma cópia é enviada ao Ploomes e uma negociação é criada…](https://downloads.intercomcdn.com/i/o/784597590/b1c559ba9640a30c8fae5e8d/image.png?expires=1786536000&signature=bb6728307d9789f98fbc8ce5212700cffcbbab33bfc50ae9b39e1c1b3c2f8a52&req=cygjE8B5mIhfFb4V1XW4gZVc%2BSZk1Zk6BEcj9gqFymbvOa9eeCPLAePcmuZD%0AvrDMs1p1fndvP8feI5z7Qx42hw%3D%3D%0A)

**Dados sincronizados:** todos os campos que estão visíveis no orçamento do Dataplace e são relevantes para consulta e compartilhamento com o cliente são sincronizados. Os principais são:

- Empresa de faturamento
- Condição de pagamento
- Vendedor
- Cliente
- Detalhamento dos itens: nome, código, observações, NCM, % ICMS, % IPI, valor do IPI, ST, total com e sem impostos.
- Total dos itens
- Total de impostos
- Valor do frete
- Tipo de frete
- Data de validade
- Status (pendente ou fechado)
- Data de fechamento
- Detalhamento das parcelas: sequência, número do lançamento, valor, vencimento e documento de quitação.
- Valor final
- Observações

**Carga inicial:** ao habilitar a integração, serão sincronizados os orçamentos criados até 30 dias atrás.

- ### Pedidos (de venda e faturamento):

**Comportamento:** sempre que um pedido é criado no Dataplace, ele é enviado ao Ploomes. Quando o pedido é atualizado no Dataplace, as mudanças são refletidas no Ploomes.

![Imagem 5: Comportamento: sempre que um pedido é criado no Dataplace, ele é enviado ao Ploomes. Quando o pedido é atualizado no…](https://downloads.intercomcdn.com/i/o/784598372/4c236690387eb99208ed81b4/image.png?expires=1786536000&signature=eb99788f257d6634572a6b905557707d62c2fa2d9e8a02a5debb5c30fc8fc221&req=cygjE8B2noZdFb4V1XW4gV3mnUg6cbcpAW68y9eyDbxNIDAIce2YrCZmY2H6%0AuOgBcTTj2Za3u%2B5OzdugINrx0Q%3D%3D%0A)

**Dados sincronizados:** todos os campos que estão visíveis no pedido do Dataplace e são relevantes para consulta e compartilhamento com o cliente são sincronizados. Os principais são:

- Empresa de faturamento
- Condição de pagamento
- Vendedor
- Cliente
- Detalhamento dos itens: nome, código, observações, NCM, % ICMS, % IPI, valor do IPI, ST, total com e sem impostos.
- Total dos itens
- Total de impostos
- Frete
- Tipo de frete
- Data de validade
- Detalhamento das parcelas: sequência, número do lançamento, valor, vencimento e documento de quitação.
- Valor final
- Observações
- Data de faturamento

**Carga inicial:** ao habilitar a integração, serão sincronizados os pedidos criados até 90 dias atrás.

**Observação:** os layouts do orçamento e do pedido do venda podem ser alterados no Ploomes, sem afetar a integração. Isso permite que o cliente Ploomes/Dataplace possa utilizar as facilidades de edição dos modelos de documentos do Ploomes. Exemplos do que pode ser realizado: incluir capa, apresentação institucional, alterar a estrutura e/ou as cores das tabelas de produtos e parcelas, incluir imagens da sua empresa, produtos ou serviços, entre outros.

## Carga inicial de dados

Na carga inicial de dados, todos os Cliente e Produtos são puxados do Dataplace para o Ploomes, bem como os orçamentos e pedidos gerados no Dataplace nos últimos 3 meses. Este é o período padrão, mas pode ser estendido caso necessário. Quanto maior o período, maior será o tempo de processamento, que pode levar até dezenas de horas (alguns dias) caso o período e o volume de dados sejam grandes. Caso isso seja uma preocupação, deve-se alinhar com o time da Ploomes e Dataplace qual é este volume para que seja estimado o tempo da carga inicial.

## Como é realizado o vínculo entre o Vendedor do Dataplace e do Ploomes

Quando um orçamento, por exemplo, é trazido do Dataplace ao Ploomes, a aplicação verifica se existe algum usuário no Ploomes com o campo “ID Dataplace” preenchido com o mesmo código do vendedor no Dataplace. Caso não encontre, verifica se existe algum usuário com o mesmo e-mail do vendedor no Dataplace (caso esta info esteja preenchida). CAso não encontre, será criado um usuário de integração no Ploomes para representar o vendedor do Dataplace e vincular os dados corretamente.

## Limitações

O Dataplace possui um recurso de Campos de tempo de execução. Estes campos não ficam armazenados no banco de dados, apenas são calculados na hora para serem exibidos no formulário para o usuário ou em um orçamento ou pedido, por exemplo. Justamente por não ficar gravado no banco de dados, não é possível trazer este tipo de campo, que pode ser criado pelo time de implementação da Dataplace ou seus parceiros autorizados.

---

Esse artigo te ajudou? Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

Ficou com alguma dúvida? Não hesite em chamar o Suporte pelo chat.
