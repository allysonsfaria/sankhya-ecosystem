---
id: "42948429214999"
titulo: "Incluindo Dashboard personalizado no Vidya Force"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42948429214999-Incluindo-Dashboard-personalizado-no-Vidya-Force"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Performance"
atualizado_em: "2026-08-24T16:38:29Z"
rotulos: ["sync_hc", "vidya", "vidya_459874", "sync_hash_e41fcab1b78e"]
---

# Incluindo Dashboard personalizado no Vidya Force

1 - Ao acessar a tela: Construtor de Componentes de BI, selecione um Dashboard, marque como Card Inteligente.

![Imagem 1: 1 - Ao acessar a tela: Construtor de Componentes de BI, selecione um Dashboard, marque como Card Inteligente.](https://ajuda.sankhya.com.br/hc/article_attachments/42956782626583)

Para validação, entre com o Usuário do Vendedor no SankhyaOm e valide se o Dashboard (Card) aparece na tela inicial.

na tela: Construção do Dashboad:

O nome das colunas precisam ser COLUMN1, COLUMN2... até o máximo de COLUMN10, e para formatação dos campos de valor, usar a função TO\_CHAR.

ex: TO\_CHAR(NVL(CAB.VLRNOTA, 0), 'FM999G999G999D90', 'nls\_numeric\_characters='',.''') AS COLUMN2

Se desejar adicionar o cifrão pode fazer da seguinte forma:

'R$' || TO\_CHAR(NVL(CAB.VLRNOTA, 0), 'FM999G999G999D90', 'nls\_numeric\_characters='',.''') AS COLUMN2

**Obs: Atualmente é possível carregar no aplicativo apenas Dashboards nos modelos de Tabela e Valor.**
