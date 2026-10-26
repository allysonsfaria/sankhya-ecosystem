---
id: "44011175986711"
titulo: "[TMS] - Como Resolver o Problema de Nota de Devolução Aparecendo no Relatório de Provisão de Frete"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011175986711--TMS-Como-Resolver-o-Problema-de-Nota-de-Devolu%C3%A7%C3%A3o-Aparecendo-no-Relat%C3%B3rio-de-Provis%C3%A3o-de-Frete"
trilha: "Lincros > TMS > Relatórios - TMS"
atualizado_em: "2026-10-05T18:56:01Z"
rotulos: ["sync_hc", "lincros", "lincros_13439375", "sync_hash_08c644c9f991"]
---

# [TMS] - Como Resolver o Problema de Nota de Devolução Aparecendo no Relatório de Provisão de Frete

## 1 - Problema Relatado pelo Cliente:

O cliente relatou que, ao gerar um relatório de provisão de frete em Excel, uma nota de devolução apareceu na coluna "Nota Fiscal" de forma inesperada. O cliente havia configurado os filtros de extração da seguinte forma:

- **Data de emissão do CT-e**: de 01/01/2025 até 04/02/2025
- **Data de emissão da NF**: de 01/01/2025 até 31/01/2025
- **Tipo de operação**: "Saída"
- **Exibir total de não integrados**: "Sim"
- **Consistência prévia**: "Conhecimento s/cte"
- **Consistência de integração no período**: "Sim"

![Imagem 1: Consistência de integração no período : "Sim"](https://ajuda.sankhya.com.br/hc/article_attachments/44011176178839)

O cliente não entendeu o motivo de  aparecer uma devolução parcial na coluna "Nota Fiscal" do relatório, uma vez que não havia observado esse comportamento em extrações anteriores. A dúvida principal era sobre o motivo pelo qual apenas uma nota de devolução apareceu no relatório, enquanto outras notas de devolução parcial não estavam presentes, apesar de todas seguirem o mesmo padrão de "tipo de operação normal". O cliente também questionou o significado de "CT-e de entrada" e por que o CT-e 76569, com o mesmo padrão, não apareceu.

## 2 - Passo a Passo para Resolver o Problema:

**Passo 1: Verificar o Tipo de Operação no XML da Nota**

- Abra o XML da nota de devolução que apareceu no relatório.
- Verifique o campo **tpNF**(tipo de operação):

  - **tpNF = 1** indica uma operação de **saída**.
  - **tpNF = 0** indica uma operação de **entrada**.

A nota de devolução que apareceu no relatório tinha **tpNF = 1**, indicando uma operação de saída.

![Imagem 2: A nota de devolução que apareceu no relatório tinha tpNF = 1 , indicando uma operação de saída.](https://ajuda.sankhya.com.br/hc/article_attachments/44011144629911)

**Passo 2: Conferir a Modalidade de Frete**

- Verifique a modalidade de frete configurada na nota de devolução:

  - Se a modalidade de frete for **"Sem frete"** ou **"Por conta de terceiros"**, o tipo de operação será **"Saída"**.
  - Se a modalidade for **"Por conta do destinatário"** ou **"Frota própria por conta do destinatário"**, o tipo de operação será **"Entrada"**.

No caso da nota que apareceu, a modalidade de frete foi configurada como **"Sem frete"**, o que gerou a classificação da nota como **"Saída"**.

![Imagem 3: No caso da nota que apareceu, a modalidade de frete foi configurada como "Sem frete" , o que gerou a classificação da…](https://ajuda.sankhya.com.br/hc/article_attachments/44011098736791)

**Passo 3: Ajustar os Filtros do Relatório**

- O cliente havia configurado o filtro para **tipo de operação: "Saída"**. Como resultado, o relatório apenas exibiu as notas de operação de saída, excluindo as de entrada.
- Se desejar incluir também as notas de entrada, ajuste o filtro do relatório para cobrir **ambos os tipos de operação**(entrada e saída).

  - Alternativamente, gere dois relatórios separados: um para **"Saída"** e outro para **"Entrada"**.

**Passo 4: Entender o Caso do CT-e 76569**

- O CT-e 76569 foi classificado como **"Entrada"** devido à modalidade de frete **"Por conta do destinatário"**.
- Como o filtro foi configurado apenas para **"Saída"**, esse CT-e não apareceu no relatório. Para visualizar esse tipo de CT-e, o filtro deve ser ajustado ou um relatório separado deve ser gerado.

**Passo 5: Regerar o Relatório Após Ajustes**

- Após realizar os ajustes no filtro e garantir que as configurações estão corretas, regenere o relatório.
- Verifique se todas as notas de devolução, tanto de **entrada** quanto de **saída**, estão corretamente refletidas no relatório.
