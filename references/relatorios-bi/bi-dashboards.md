# Painéis e Construtor de Componentes de BI (Sankhya OM)

O Construtor de Componentes de BI permite criar dashboards visuais, relatórios analíticos, gráficos e indicadores executivos dentro do Sankhya OM.

---

## 1. Tipos de Gadgets Disponíveis

- **Gráfico de Barras / Colunas**: Comparações categóricas (vendas por vendedor, compras por grupo).
- **Gráfico de Linha / Área**: Evolução temporal de séries financeiras ou faturamento diário.
- **Gráfico de Pizza / Rosca**: Composição percentual (despesas por natureza, vendas por estado).
- **Tabela / Grade Analítica**: Exibição detalhada de linhas com totalizadores e filtros.
- **Cartão / KPI (Indicador Numérico)**: Destaque de métricas chave (Total Faturado no Mês, Ticket Médio).

---

## 2. Parâmetros Dinâmicos e Filtros Globais

Os dashboards suportam parâmetros no cabeçalho compartilhados entre múltiplos componentes:
- `:PERIODO` (Datas De/Até com calendário nativo)
- `:CODEMP` (Seleção múltipla de empresas)
- `:CODPARC` (Pesquisa de parceiro)

### Uso no SQL do Gadget:
```sql
SELECT 
    VEND.APELIDO AS VENDEDOR,
    SUM(CAB.VLRNOTA) AS TOTAL_FATURADO
FROM TGFCAB CAB
INNER JOIN TGFVEN VEND ON VEND.CODVEND = CAB.CODVEND
WHERE CAB.TIPMOV = 'V'
  AND CAB.STATUSNOTA = 'L'
  AND CAB.DTNEG BETWEEN :PERIODO.INI AND :PERIODO.FIN
  AND (:CODEMP IS NULL OR CAB.CODEMP = :CODEMP)
GROUP BY VEND.APELIDO
ORDER BY TOTAL_FATURADO DESC
```

---

## 3. Importação e Exportação de XML de BI
- Todo painel de BI pode ser exportado em formato XML pelo Construtor de Componentes de BI.
- Para implantar o dashboard em outro ambiente ou cliente, basta importar o XML na tela **Importação de Componentes de BI**.
