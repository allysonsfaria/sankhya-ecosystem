---
id: "20127184136983"
titulo: "Quais produtos são visualizados na cópia de estoque?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/20127184136983-Quais-produtos-s%C3%A3o-visualizados-na-c%C3%B3pia-de-estoque"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-08-01T01:13:26Z"
rotulos: ["Produtos", "Configuração", "Movimentação Financeira", "Nota Fiscal", "Estoque", "Necessário ter movimentação ou linha na TGFEST", "Produto não aparece na cópia de estoque", "Estoque zerado também é considerado", "Artigo atualizado KCS", "CVE - KCS"]
---

# Quais produtos são visualizados na cópia de estoque?

É comum que usuários identifiquem situações em que os **"saldos de estoque"** não aparecem zerados no sistema, ou que produtos não sejam exibidos em relatórios como a **"Cópia de Estoque"**. Este comportamento pode ocorrer por diferentes motivos, dependendo do contexto da operação realizada.

Este artigo explica as principais situações que geram divergências ou ausência de registros de estoque e quais ações podem ser tomadas para corrigir ou compreender essas informações.

### Ausência na Cópia de Estoque

Para que um produto seja exibido na **"Cópia de Estoque"** (Inventário » Arquivo » Cópia de Estoque), é indispensável que ele possua ao menos uma movimentação de entrada registrada por meio de nota fiscal, a qual gera um lançamento na tabela TGFEST.

Caso o saldo do produto zere, o sistema remove automaticamente sua linha da TGFEST. Com isso, o item deixará de ser considerado na geração da **"Cópia de Estoque"**, já que essa rotina baseia-se na comparação entre o saldo existente na TGFEST e as movimentações registradas até a data informada.

### Comportamento após exclusão de notas fiscais

Quando uma **"Nota Fiscal"** é excluída, o sistema zera a quantidade do produto na tabela de estoque (TGFEST), mas não apaga o registro de controle. Por isso, a tela **"Verificação de Saldo de Estoque"** (Configurações » Avançado » Verificação de Saldo de Estoque) pode exibir linhas com saldo zerado.

Esse comportamento é normal e esperado para fins de auditoria e rastreabilidade.

### Divergências entre telas e relatórios

Em produtos com controle de lote e estoque em múltiplos locais, quando há saldo positivo em um local e negativo em outro, podem surgir divergências:

Tela **"Gerência de Produtos"** (Comercial » Gerente » Gerência de Produtos): consolida o saldo total, somando os valores positivos e negativos.
 Relatório **"Cópia de Estoque"**: ao aplicar o filtro "estoque maior que zero", exibe apenas os saldos positivos.

### Registros órfãos e Validação de Faturamento

Podem existir lançamentos sem cabeçalho (itens na TGFITE sem o correspondente na TGFCAB) que impactam o extrato de estoque. Além disso, durante o **"Faturamento"**, o sistema valida o saldo disponível: se o saldo estiver zerado, mas houver reserva vinculada ao pedido, o faturamento direto será bloqueado, sendo necessário utilizar o **"Botão Faturar"** no portal.

### Como corrigir saldos inconsistentes

Para corrigir saldos de estoque, siga as orientações abaixo:

Acesse a tela **"Verificação de Saldo de Estoque"** (Configurações » Avançado » Verificação de Saldo de Estoque) e identifique os produtos com divergências.
 Verifique se há registros órfãos; se necessário, solicite suporte técnico para correção via banco de dados.
 Realize um **"Inventário"** (WMS » Inventário » Inventários) dos produtos para identificar a quantidade real.
 Execute os ajustes de estoque necessários.
 Após as correções, execute novamente a **"Verificação de Saldo de Estoque"**.

Para mais informações, consulte: [Estoque - Processo de inventário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108953-Estoque-Processo-de-invent%C3%A1rio).
