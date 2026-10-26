# Campos Calculados com HTML e JavaScript (#type.sql#)

Permite exibir botões de ação, status coloridos, badges e popups/tooltips ricos diretamente nas linhas das grades (grids) do Sankhya OM sem criar arquivos frontend dedicados.

---

## 1. Como Funciona no Dicionário de Dados

1. Abra a tela **Dicionário de Dados** (`TDDTAB` / `TDDCAM`).
2. Localize a tabela desejada (ex: `TGFCAB` ou `TGFPAR`).
3. Adicione um campo com tipo de dado **Expressão SQL** ou marque a opção correspondente.
4. Na expressão, inicie com a macro `#type.sql#` e retorne um bloco de HTML/CSS/JS concatenado pelo banco de dados (Oracle ou SQL Server).

---

## 2. Exemplo: Badge de Status com Cores Condicionais (Oracle / SQL Server)

```sql
#type.sql#
CASE 
    WHEN this.STATUSNOTA = 'L' THEN 
        '<span style="background-color: #28a745; color: white; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;">CONFIRMADA</span>'
    WHEN this.STATUSNOTA = 'A' THEN 
        '<span style="background-color: #ffc107; color: black; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;">PENDENTE</span>'
    ELSE 
        '<span style="background-color: #dc3545; color: white; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;">CANCELADA</span>'
END
```

---

## 3. Exemplo: Botão com Ação ou Tooltip / Popover Dinâmico

```sql
#type.sql#
'<button type="button" class="btn-grid-custom" style="cursor: pointer; background: #0066cc; color: #fff; border: none; border-radius: 3px; padding: 2px 6px;" onclick="window.open(''https://meusistema.com.br/rastreio?id=' || this.CODPARC || ''', ''_blank'')">Rastrear</button>'
```

---

## 4. Cuidados e Armadilhas Comuns
- **ORA-01489: result of string concatenation is too long**: Ocorre no Oracle ao usar `LISTAGG` com strings muito longas. Use `ON OVERFLOW TRUNCATE` no Oracle 12c+ ou subqueries controladas.
- **Escape de Aspas Simples**: No SQL, duplique as aspas simples dentro da string HTML (`''`).
- **Tag Script Crua**: Nunca injete scripts pesados que afetem o DOM global da tela do ERP para não quebrar a reatividade da grade.
