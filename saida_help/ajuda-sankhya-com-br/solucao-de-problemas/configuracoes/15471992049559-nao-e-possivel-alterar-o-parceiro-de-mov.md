---
id: "15471992049559"
titulo: "Não é possível alterar o parceiro de movimentos originados do estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15471992049559-N%C3%A3o-%C3%A9-poss%C3%ADvel-alterar-o-parceiro-de-movimentos-originados-do-estoque"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:56:49Z"
rotulos: ["Configuração", "Parceiro", "Movimentação Financeira", "Estoque", "Financeiro", "CORE_E02420", "Restrição de Alteração de Parceiro em Movimentos de Estoque"]
---

# Não é possível alterar o parceiro de movimentos originados do estoque

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16538383562519) MENSAGEM:**

[CORE\_E02420]: Não é possível alterar o parceiro de movimentos originados do estoque.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16538411881751) CAUSA:**

Ocorre quando o parâmetro **"Proíbe a troca de parceiro em financeiro de nota? - PROIBTRCPARFIN"**está ligado e há tentativa de alterar o parceiro do lançamento.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16538411865751) SOLUÇÃO:**

Em algumas situações podem ser necessárias algumas modificações nos títulos na **"Movimentação Financeira",** mesmo que estes tenham sido originados das Centrais (campo Origem = Estoque); tal comportamento é controlado pelos parâmetros **"Qdo originado da Central não permitir alterar nada - ALTERAFIN"** e **"Proíbe a troca de parceiro em financeiro de nota? - PROIBTRCPARFIN"** da seguinte maneira:

![Imagem 4: Se o parâmetro Qdo originado da Central não permitir alterar nada - ALTERAFIN for habilitado, será feito o bloqueio de…](https://ajuda.sankhya.com.br/hc/article_attachments/16538383571863) Se o parâmetro Qdo originado da Central não permitir alterar nada - ALTERAFIN for habilitado, será feito o bloqueio de qualquer alteração nos títulos que tiveram origem nas Centrais;

![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16538383574807) **OBSERVAÇÃO:**

O parâmetro mencionado acima não será aplicado quando as funcionalidades do botão **"Baixar"** forem utilizadas (tela [**"Movimentação Financeira - Baixa de Títulos"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534)).

![Imagem 6: Caso o parâmetro Qdo originado da Central não permitir alterar nada -ALTERAFIN seja desabilitado e o parâmetro Proíbe a…](https://ajuda.sankhya.com.br/hc/article_attachments/16538383579287) Caso o parâmetro Qdo originado da Central não permitir alterar nada -ALTERAFIN seja desabilitado e o parâmetro Proíbe a troca de parceiro em financeiro de nota? - PROIBTRCPARFIN for habilitado, será feito o bloqueio de modificações nos títulos de origem nas Centrais, nos seguintes campos:

| Vlr do Desdobramento; | Tipo Operação; |
| --- | --- |
| Dt. Negociação; | Receita/Despesa; |
| Empresa; | Provisão; |
| Moeda; | Vlr Moeda; |
| Parceiro. |  |

![Imagem 7: Com ambos os parâmetros desligados, teremos o bloqueio de alterações nos títulos originados das Centrais , nos…](https://ajuda.sankhya.com.br/hc/article_attachments/16538411878551) Com ambos os parâmetros desligados, teremos o bloqueio de alterações nos títulos originados das Centrais, nos seguintes campos:

| Vlr do Desdobramento; | Tipo Operação; |
| --- | --- |
| Dt. Negociação; | Receita/Despesa; |
| Empresa; | Provisão; |
| Moeda; | Vlr Moeda. |
