---
id: "6978749917847"
titulo: "Não é permitido filtro por empresa quando o custo não é por empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6978749917847-N%C3%A3o-%C3%A9-permitido-filtro-por-empresa-quando-o-custo-n%C3%A3o-%C3%A9-por-empresa"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T15:15:33Z"
rotulos: ["Custos", "Kardex", "Configuração", "Relatórios", "Estoque", "Financeiro", "#validadoSilvio", "CORE_E03963", "Parâmetro \"CUSTOPOREMP\"", "Restrição no Filtro por Empresa em Custos não Individualizados"]
---

# Não é permitido filtro por empresa quando o custo não é por empresa

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16478149341335) MENSAGEM:**

[CORE\_E03963]Não é permitido filtro por empresa quando o custo não é por empresa.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16478149345687) SOLUÇÃO:**

O Kardex permite a visualização por empresas apenas nos casos em que o parâmetro **"CUSTOPOREMP"** esteja habilitado.

**Importante:** esse parâmetro **não deve ser ajustado** sem uma análise criteriosa dos responsáveis pelo gerenciamento de custos na empresa, visto impactos que essa mudança representa no processo de custo. 

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16478149349015)CAUSA:**

Caso o parâmetro esteja desabilitado, os custos gravados na tabela de custos ficam registrados com o CODEMP = 1, não fazendo sentido o filtro por empresas, justificando a mensagem apresentada.

Isso se faz necessário, pois como o relatório Kardex é um documento oficial, os custos apresentados devem coincidir com as movimentações da empresa. Caso não controle os custos por empresa, não existe a possibilidade de apresentar um estoque separado.
