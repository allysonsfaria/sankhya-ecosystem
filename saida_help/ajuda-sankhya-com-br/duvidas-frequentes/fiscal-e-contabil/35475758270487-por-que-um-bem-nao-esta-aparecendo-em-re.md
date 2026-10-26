---
id: "35475758270487"
titulo: "Por que um bem não está aparecendo em relatórios contábeis do patrimonial?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35475758270487-Por-que-um-bem-n%C3%A3o-est%C3%A1-aparecendo-em-relat%C3%B3rios-cont%C3%A1beis-do-patrimonial"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-09-09T14:13:28Z"
rotulos: ["Configuração", "Relatórios", "Financeiro", "Razão do erro", "Relatório Contábeis do  Patrimonial", "bem não está aparecendo em relatórios contábeis do patrimonial", "Bem Baixado", "Entenda Por Que Um Bem Não Aparece", "Patrimonial"]
---

# Por que um bem não está aparecendo em relatórios contábeis do patrimonial?

**SITUAÇÃO:**

Se alguns bens não estão sendo evidenciados no relatório mesmo depois da depreciação, siga as verificações a baixo:

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/35475758261911)SOLUÇÃO:**

Se um bem (exemplo: Bem 429) não está sendo exibido em relatórios (referência 06/2025 por exemplo), o motivo mais comum é a aplicação de um filtro que o sistema interpreta como **"Bem Baixado"** antes do período de consulta.

Na maioria dos relatórios patrimoniais do Sankhya, o filtro principal é feito pela data de baixa, usando a função de banco de dados `SNK_Getdtbaixabem()`.

O relatório aplica uma condição lógica para garantir que apenas bens ativos ou baixados após o período de referência sejam incluídos. Para uma consulta com referência em **01/06/2025**, o filtro é resumidamente:

| Condição Exigida | Significado |
| --- | --- |
| `DATA_BAIXA > 01/06/2025` | O bem foi baixado após o mês de consulta. |
| `DATA_BAIXA IS NULL` | O bem não possui registro de baixa (está ativo). |

**O Bem 429 é excluído porque a função retorna 24/01/2024**. Como **24/01/2024** é anterior a **01/06/2025**, o bem é eliminado do resultado.

###

#### O Conceito de Baixa no Sankhya: SNK\_Getdtbaixabem()

É fundamental entender que o Sankhya não utiliza apenas o campo `DTBAIXA` da tabela `TCIBEM` (Bens Patrimoniais) para determinar se um bem foi baixado.

A função `SNK_Getdtbaixabem()` verifica outras fontes, mesmo que o campo `DTBAIXA` esteja vazio na tela:

Exemplo para consulta:

```
SELECT
    BEM.CODBEM,
    BEM.CODEMP,
    BEM.CODPROD,
    PRO.DESCRPROD AS DESCR_PRODUTO,
    BEM.DTCOMPRA,
    SNK_Getdtbaixabem(BEM.CODPROD, BEM.CODBEM, SNK_TRUNC_DATE('01/06/2025','MM')) AS DATA_BAIXA,
    BEM.NUNOTA,
    BEM.VLRDEP,
    BEM.VLRSALDO,

    /* --- regras principais --- */
    CASE
        WHEN SNK_TRUNC_DATE(SNK_Getdtbaixabem(BEM.CODPROD,BEM.CODBEM,SNK_TRUNC_DATE('01/06/2025','MM')),'MM') > SNK_TRUNC_DATE('01/06/2025','MM')
            OR SNK_Getdtbaixabem(BEM.CODPROD,BEM.CODBEM,SNK_TRUNC_DATE('01/06/2025','MM')) IS NULL
        THEN '✅ Passou - Não baixado até 06/2025'
        ELSE '❌ Excluído - Baixado antes de 07/2025'
    END AS REGRA_BAIXA,

    CASE
        WHEN SNK_TRUNC_DATE(BEM.DTCOMPRA,'MM') <= SNK_TRUNC_DATE('01/06/2025','MM')
        THEN '✅ Passou - Compra até 06/2025'
        ELSE '❌ Excluído - Compra após 06/2025'
    END AS REGRA_COMPRA,

    CASE
        WHEN (NVL('14',0)=0) OR (BEM.CODEMP='14')
        THEN '✅ Passou - Empresa = 14 ou sem filtro'
        ELSE '❌ Excluído - Empresa diferente de 14'
    END AS REGRA_EMPRESA,

    CASE
        WHEN NVL('0',0)=0 OR BEM.NUNOTA='0'
        THEN '✅ Passou - NUNOTA sem restrição'
        ELSE '❌ Excluído - NUNOTA diferente'
    END AS REGRA_NOTA

FROM TCIBEM BEM
JOIN TGFPRO PRO ON PRO.CODPROD = BEM.CODPROD
WHERE BEM.CODPROD = 9003
ORDER BY BEM.CODBEM
```

**Observação:** #troque o parâmetro 14 pelo código específico da empresa

Ao executar, será exibido algo assim:

![Imagem 2: Ao executar, será exibido algo assim:](https://ajuda.sankhya.com.br/hc/article_attachments/35475770560023)

###

- **Identifique o Saldo Zerado:**

  Acesse o DBE e consulte a tabela de saldos:

  SQL

  ```
  SELECT *
  FROM TCISAL
  WHERE CODBEM = '429'
  ORDER BY REFERENCIA DESC
  ```

- Verifique se há um registro com `REFERENCIA` próxima a **suposta data de baixa** onde o campo `VLRSALDO` está igual a zero (`0`).

  - Caso o bem **esteja ativo e não devesse estar baixado**, sugerimos que a equipe interna de TI junto com a fiscal ou a equipe de unidade avalie o saldo e os registros do bem para ajustar corretamente a contabilização no sistema.
- Se a baixa registrada está correta, **não há ação necessária**, pois o relatório reflete a situação real do sistema.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/35475758264599)CAUSA:**

A causa mais provável é que o sistema Sankhya está interpretando o bem como **"Baixado"** em uma data anterior à referência do relatório. Isso ocorre porque a função **SNK\_Getdtbaixabem()** encontra um registro na tabela de saldos (**TCISAL**) onde o campo **VLRSALDO** para o bem está **zerado (0)**, e utiliza a data desse saldo zerado como a data de baixa.

Se o bem realmente foi baixado antes da referência de geração do relatorio, o comportamento do relatório está correto e ele não deve ser exibido na referência atual.
