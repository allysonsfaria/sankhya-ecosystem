---
id: "39359793066007"
titulo: "Produto não aparece na análise de giro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39359793066007-Produto-n%C3%A3o-aparece-na-an%C3%A1lise-de-giro"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-10-05T02:18:13Z"
rotulos: ["Produtos", "Custos", "Configuração", "Relatórios", "Análise de Giro", "TOP", "Artigo criado KCS", "CVE - KCS"]
---

# Produto não aparece na análise de giro

O item possui saídas registradas no sistema, mas não aparece na **"Análise de Giro"**.

### SITUAÇÃO

Ao gerar a **"Análise de Giro"** (Comercial Consulta Análise de Giro), o usuário identifica que um produto específico, mesmo possuindo várias saídas registradas no período analisado, não é apresentado na análise.

### SOLUÇÃO

Para resolver esta situação, execute os passos abaixo:

**(1)** Verifique se o **"Tipo de Operação (TOP)"** utilizado nas vendas está configurado corretamente para ser considerado na **"Análise de Giro"**. Acesse a tela **"Tipos de Operação"** (Comercial Arquivo Cadastros Tipos de Operação - TOP) e confirme se o campo **"Análise de Giro"** está marcado com o valor Venda(Saída).
**(2)** Verifique se o produto possui linha de custo cadastrada. Acesse a tela **"Variação de Custos"** (Comercial » Consulta » Variação de Custos de Produtos) e consulte se existe custo registrado para o item para o período que está sendo analisado. 
**(3)** Verifique se o produto está com a marcação para calcular giro, no cadastro de produtos (campo Calcular giro pelo agendador, na aba Medidas e Estoque, sub-aba Estoque). 
**(4)** Caso o produto não possua linha de custo, realize a limpeza da consolidação na tabela **"TGFGIR1"**. Após criar a linha de custo, execute novamente a consolidação da **"Análise de Giro"**.
**(5)** Retorne à tela **"Análise de Giro"** e verifique se o produto passou a apresentar o giro corretamente nos períodos analisados.

### CAUSA

As principais causas para o produto não aparecer na **"Análise de Giro"** são:

- **"TOP"** não configurada: o **"Tipo de Operação"** utilizado nas vendas não está marcado para ser considerado na **"Análise de Giro"**.
- Ausência de linha de custo: o produto não possui custo cadastrado, impedindo que as sugestões de giro sejam calculadas corretamente.
- Agendador inativo: o agendador de consolidação da **"Análise de Giro"** não está em funcionamento, impedindo a atualização dos dados.
- Consolidação desatualizada: a tabela de consolidação precisa ser limpa e reprocessada após correções nos cadastros.
