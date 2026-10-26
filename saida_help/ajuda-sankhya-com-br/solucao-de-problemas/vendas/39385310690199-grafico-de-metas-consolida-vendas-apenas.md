---
id: "39385310690199"
titulo: "Gráfico de Metas Consolida Vendas Apenas no Vendedor 'Gerente'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39385310690199-Gr%C3%A1fico-de-Metas-Consolida-Vendas-Apenas-no-Vendedor-Gerente"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-25T03:57:04Z"
rotulos: ["Configuração", "Relatórios", "Metas", "Atualização", "Vendas", "Artigo criado KCS", "CVE - KCS"]
---

# Gráfico de Metas Consolida Vendas Apenas no Vendedor 'Gerente'

**Mensagem**

O dashboard "Gráfico Metas" exibe todas as vendas agrupadas em um único vendedor (geralmente o gerente), em vez de separar por vendedor individual.

**Situação**

Ao acessar Comercial » Gráficos » Gráfico Metas, os valores aparecem consolidados em um único vendedor, mesmo com as Metas Simplificadas de Vendas configuradas corretamente e movimentações de venda existentes para cada vendedor no período. O esperado é ver o resultado detalhado por vendedor.

**Solução**

Para corrigir a consolidação incorreta das vendas, siga os passos abaixo:

**(1)** Acesse "Configuração de Estrutura de Metas/Orçamentos" (Metas e Orçamentos » Configuração de Estrutura de Metas/Orçamentos).

**(2)** Selecione a meta (deve ser do **Tipo Comercial,** em metas Financeiras esses campos não existem). Abra a aba **"Propriedades"**.

**(3)** Abra a aba **"Propriedades"**.

**(4)** No quadro de duas listas, arraste **"Vendedor/Comprador"** para a lista **"Campos Significativos"**. Se **"Gerente"** estiver nessa mesma lista e você não quiser o agrupamento por gerente, arraste-o de volta para **"Campos Disponíveis"**.

**(5)** Salve e volte em **Planejamento de Metas/Orçamentos**, localize a meta e clique em **"Atualização de Realizado"** para reprocessar.

**(6)** Confira no dashboard **"Gráfico de Metas"** se os valores passaram a aparecer por vendedor.

**Causa**

Esse comportamento ocorre pela forma como a meta foi configurada em "Configuração de Estrutura de Metas/Orçamentos" (Metas e Orçamentos):

- O campo **Vendedor** não está marcado para compor o agrupamento do realizado; e/ou
- O campo **Gerente** está marcado, fazendo o sistema agrupar pelo gerente em vez do vendedor; ou
- O cadastro de vendedores está com o campo **Gerente** preenchido igual para vários vendedores, o que faz o agrupamento por gerente "esconder" o detalhe por vendedor.
