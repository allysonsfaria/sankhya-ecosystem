# Relatórios Formatados e JasperReports (iReport 4.0.1)

O motor de impressão de relatórios formatados do Sankhya OM utiliza a biblioteca **JasperReports 4.0.1**.

---

## 1. Regra Inegociável de Compatibilidade

> **ATENÇÃO MÁXIMA:** Arquivos `.jrxml` criados com versões mais recentes do Jaspersoft Studio (ex: Jasper 6.x ou 7.x) **NÃO COMPILAM** no Sankhya OM.
> O compilador do ERP rejeita tags e atributos introduzidos após a versão 4.0.1 (como `uuid`, atributos de markup modernos ou novas fontes).

### Configuração Recomendada no iReport / Jaspersoft Studio:
- Defina a compatibilidade de saída do compilador para **JasperReports 4.0.1**.
- Evite atributos de tag `<reportElement uuid="..." />` gerados automaticamente por versões novas.

---

## 2. Parâmetros Nativos Injetados pelo Sankhya

Ao executar um relatório a partir do sistema, o Sankhya injeta automaticamente parâmetros de contexto:

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `$P{PDIR_MODELO}` | `java.lang.String` | Caminho físico absoluto da pasta onde o relatório está hospedado (usado para carregar sub-relatórios e imagens) |
| `$P{CODEMP}` | `java.math.BigDecimal` | Código da empresa selecionada |
| `$P{CODUSU}` | `java.math.BigDecimal` | Código do usuário logado |
| `$P{NUNOTA}` | `java.math.BigDecimal` | Número da nota selecionada na grade ao imprimir direto da Central de Vendas/Compras |
| `$P{PK_NOME_CAMPO}` | Conforme campo | Injetado automaticamente quando a impressão parte de uma grade com linha selecionada |

---

## 3. Padrão para Sub-relatórios

Para referenciar um sub-relatório de forma portável entre ambientes de homologação e produção:

```xml
<subreport>
    <reportElement x="0" y="0" width="555" height="40"/>
    <subreportParameter name="NUNOTA">
        <subreportParameterExpression><![CDATA[$F{NUNOTA}]]></subreportParameterExpression>
    </subreportParameter>
    <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
    <subreportExpression class="java.lang.String"><![CDATA[$P{PDIR_MODELO} + "sub_itens.jasper"]]></subreportExpression>
</subreport>
```

---

## 4. Deploy no Sankhya OM
1. Acesse a tela **Relatórios Formatados**.
2. Crie ou localize o relatório.
3. Faça o upload do arquivo `.jrxml` (e sub-relatórios compilados `.jasper` ou imagens necessárias).
4. O Sankhya compila o `.jrxml` no próprio servidor durante a importação.
