---
id: "360051314174"
titulo: "Como é realizado o cálculo do custo médio?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360051314174-Como-%C3%A9-realizado-o-c%C3%A1lculo-do-custo-m%C3%A9dio"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-10-15T16:02:05Z"
rotulos: ["Produtos", "Custos", "Configuração", "Estoque", "Financeiro", "#GuilhermeSilva", "Método de custeio", "Média ponderada móvel", "Cálculo do Custo Médio", "Artigo atualizado KCS", "CVE - KCS"]
---

# Como é realizado o cálculo do custo médio?

O **"Custo Médio"** é calculado automaticamente pelo sistema considerando o **"Estoque anterior"**, o **"Custo anterior"** e as novas movimentações de entrada. Quando ocorrem divergências nos valores apresentados, geralmente está relacionado a inconsistências no saldo de estoque ou na necessidade de reprocessamento dos custos.

Este artigo apresenta as principais causas de divergências no cálculo do custo médio e as soluções para corrigir essas inconsistências.

### Como o sistema calcula o custo médio

**(1)** Os custos médios são calculados seguindo o seguinte algoritmo:

((Custo médio anterior \* Estoque anterior) + (Custo atual \* Quantidade comprada)) / (Estoque anterior + Quantidade comprada)

Dessa forma, entende-se como custo médio, a média entre o estoque atual em valor antes da compra, somado ao valor de aquisição do produto dividido pelo estoque total.

Custo médio quando se trabalha com família: (Custo anterior + Custo da entrada) / (Estoque anterior + Estoque da entrada)

**Exemplo:**
Estoque anterior: 100 (saldo implantado no produto filho)
Estoque da entrada: 20 (10 para o filho e 10 para o pai)
Custo anterior: 0
Custo da entrada: 200 (100 para o filho e 100 para o pai)
Custo médio: (Custo anterior + Custo da entrada) / (Estoque anterior + Estoque da entrada)
ou seja:

Custo médio: (0 + 200) / (100 + 20) = 1,666667

**IMPORTANTE:**

Nosso sistema utiliza o método de custeio conhecido como “Média Ponderada Móvel”.

Este método calcula uma média dos custos de todos as entradas do dia (compra, devolução de compra, produção, etc.) para o item, resultando no custo médio diário. Portanto, não dispomos de um custeio por hora ou por minuto, uma vez que tal prática é atualmente inviável. De acordo com a literatura e as práticas contábeis vigentes, a apuração de custos não é realizada de forma cronológica considerando registros “por hora”. A cronologia adotada é baseada em períodos “diários”.

### Principais causas de divergências

As divergências no cálculo do custo médio geralmente ocorrem devido a:

- **Saldo de estoque inconsistente:** quando há diferenças entre o saldo físico e o saldo registrado no sistema.
- **Custo anterior zerado ou incorreto:** produtos com estoque anterior mas sem custo registrado.
- **Falta de reprocessamento:** após correções de movimentações, os custos não foram recalculados.
- **Movimentações retroativas:** lançamentos com datas anteriores que afetam o histórico de custos.
- **Parâmetro "CUSTOPORCONT":** o cálculo pode ser impactado pela transferência entre controles, caso esteja ativado na tela **"Atualização de Custos"** (Comercial >> Avançado), pois a apuração histórica considera o estoque atual menos a soma das movimentações anteriores.

### Solução para corrigir divergências

Para corrigir divergências no cálculo do custo médio, execute os seguintes procedimentos:

**(1)** Acesse a tela **"Verificação de Saldo de Estoque"** (Estoque >> Consultas) e realize a consulta.

**(2)** Localize o produto que apresenta divergência no custo médio.

**(3)** Execute a **"Reconstrução do Saldo Diário"** para o produto selecionado. Este processo irá recalcular todo o histórico de movimentações e saldos.

**(4)** Após a reconstrução do saldo, acesse a funcionalidade de **"Reprocessamento de Custos"** (Comercial >> Avançado).

**(5)** Execute o reprocessamento para o produto ou período desejado. Este processo irá recalcular o custo médio considerando os saldos corrigidos.

**(6)** Verifique se os valores do custo médio foram atualizados corretamente no cadastro do produto.

### Configurações que influenciam o cálculo

Algumas configurações do sistema podem influenciar o cálculo do custo médio:

- Parâmetro **"USACUSMEDICMPRO"**: define se o custo médio das matérias-primas será considerado no cálculo do custo de produtos acabados.
- Parâmetro **"USACUSTOMEDIOMPS"**: permite escolher entre usar o custo **"Gerencial"**, **"Reposição"**, **"Ambos"** ou **"Não considerar"**.
- Configuração **"USARPRECOCUSTO"**: configuração nos tipos de operação que define qual custo será utilizado (**"Último Custo Médio Gerencial"**, **"Com ICMS"** ou **"Sem ICMS"**).

Verifique estas configurações na tela **"Empresa Financeiro"** (Comercial >> Preferências) e nos **"Tipos de Operação"** (Comercial >> Arquivos) para garantir que estejam adequadas ao processo da empresa.
