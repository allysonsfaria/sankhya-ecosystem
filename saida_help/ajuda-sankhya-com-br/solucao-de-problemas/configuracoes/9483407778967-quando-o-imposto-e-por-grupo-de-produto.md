---
id: "9483407778967"
titulo: "Quando o imposto é por Grupo de Produto, Produto ou Serviço e tiver o campo 'No Financeiro de Origem Estoque' = 'Subtrair' todos os registros devem ter a mesma alíquota e redução de base"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9483407778967-Quando-o-imposto-%C3%A9-por-Grupo-de-Produto-Produto-ou-Servi%C3%A7o-e-tiver-o-campo-No-Financeiro-de-Origem-Estoque-Subtrair-todos-os-registros-devem-ter-a-mesma-al%C3%ADquota-e-redu%C3%A7%C3%A3o-de-base"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-09-30T20:12:36Z"
rotulos: ["Configuração", "Movimentação Financeira", "Impostos", "Estoque", "Alíquotas de ISS", "CORE_E01887", "Padronização de Alíquota e Redução de Base"]
---

# Quando o imposto é por Grupo de Produto, Produto ou Serviço e tiver o campo 'No Financeiro de Origem Estoque' = 'Subtrair' todos os registros devem ter a mesma alíquota e redução de base

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18666415004055) MENSAGEM:**

[CORE\_E01887]  Quando o imposto é por Grupo de Produto, Produto ou Serviço e tiver o campo 'No Financeiro de Origem Estoque' = 'Subtrair' todos os registros devem ter a mesma alíquota e redução de base.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18666382115863) SITUAÇÃO:**

Ao tentar alterar o campo "No Financeiro de Origem Estoque" a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18666382127639) CAUSA:**

Ocorre quando existe divergência na % da alíquota dos serviços informados na tela de Impostos.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18666415042327) SOLUÇÃO:**

Acesse a tela **Impostos** (Configurações » Cadastros » Impostos) aba Serviço e verifique  se todos os serviços informados possuem a mesma alíquota.

Isso é necessário quando o campo "No Financeiro de Origem Estoque" estiver definido como Subtrair.

![Imagem 5: Isso é necessário quando o campo " No Financeiro de Origem Estoque " estiver definido como Subtrair.](https://ajuda.sankhya.com.br/hc/article_attachments/18666415052311)

**Importante:** Orientamos verificar com a contabilidade a necessidade de configurar uma alíquota diferente e caso realmente tenha a necessidade, será necessário que um consultor de implantação avalie este processo.
