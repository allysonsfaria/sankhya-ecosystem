---
id: "41481030236567"
titulo: "Não existe quantidade disponível para realizar o rastreamento. Produto X..."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41481030236567-N%C3%A3o-existe-quantidade-dispon%C3%ADvel-para-realizar-o-rastreamento-Produto-X"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T13:26:34Z"
rotulos: ["Produtos", "Relatórios", "WMS", "Movimentação Financeira", "Estoque", "Cópia de Estoque", "Erro", "Fiscal/Contábil - KCS", "Faturamento da empresa", "falta de estoque para o rastreamento de lote"]
---

# Não existe quantidade disponível para realizar o rastreamento. Produto X...

**MENSAGEM**

Não existe quantidade disponível para realizar o rastreamento. Produto X...

**SITUAÇÃO**

O erro é apresentado durante a confirmação de notas em movimentações internas (transferência de local), paralisando o faturamento da empresa. O sistema bloqueia a operação indicando falta de estoque para o rastreamento de lote, mesmo quando o saldo físico no Sankhya está correto e condizente com o WMS do cliente.

**SOLUÇÃO**

Para liberar o faturamento e corrigir o rastreamento de forma eficiente, realize o processo utilizando a **Cópia de Estoque** em vez de rastrear toda a vida útil do produto. Siga o passo a passo:

**(1)** Acesse a tela **''Cópia de Estoque''** (Inventário » Relatórios » Cópia de Estoque).

**(2)** Configure os filtros desejados (como o código do produto com erro ou grupo de produtos) para que a rotina considere apenas as informações relevantes.

**(3)** Clique em **''Executar Cópia''**.

**(4)** Acesse a tela **''Ativar/Reprocessar Rastreamento de Estoque/ST''** (Livros Fiscais » Avançado » Rastreamento de Estoque/ST » Ativar/Reprocessar Rastreamento de Estoque/ST).

**(5)** Clique na opção **''Filtros''** e informe os dados do produto que será corrigido.

**(6)** Acesse a opção **''Preferências''** e parametrize o rastreamento para utilizar os dados da cópia.

**(7)** É obrigatório informar no campo **''Data Cópia Estoque''** a mesma data utilizada no momento da execução da cópia de estoque (Passo 3).

**(8)** Clique em **''Aplicar''** e, em seguida, em **''Processar''**.

**(9)** Após o processamento, as tabelas de rastreamento (TGFITS) assumirão o saldo consolidado, e a movimentação de transferência poderá ser confirmada sem erros.

**CAUSA**

Ao utilizar o processamento padrão de "vida útil", o sistema exige a análise de todo o histórico de movimentações (entradas e saídas) desde o cadastro do item, o que pode travar caso haja alguma inconsistência histórica nas tabelas TGFITS e TGFVAS. A execução a partir de uma Cópia de Estoque cria uma nova "linha de base", desconsiderando o histórico passado e focando apenas no saldo atual disponível na TGFEST.
