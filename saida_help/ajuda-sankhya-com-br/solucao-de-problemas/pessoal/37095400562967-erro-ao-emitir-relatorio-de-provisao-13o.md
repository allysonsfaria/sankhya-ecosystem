---
id: "37095400562967"
titulo: "Erro ao emitir relatório de provisão 13º e férias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37095400562967-Erro-ao-emitir-relat%C3%B3rio-de-provis%C3%A3o-13%C2%BA-e-f%C3%A9rias"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:06Z"
rotulos: ["Configuração", "Relatórios", "Financeiro", "Férias", "Erro", "13º", "Relatório de provisão", "VLRPARCELA"]
---

# Erro ao emitir relatório de provisão 13º e férias

**MENSAGEM:**

Falha

Não foi possível gerar o relatório solicitado.

Motivo: net.sf.jasperreports.engine.fill.JRExpressionEvalException: Error evaluating expression :
Source text : new DecimalFormat(",0.00”).format($F{VLRPARCELA})

![Imagem 1: Motivo: net.sf.jasperreports.engine.fill.JRExpressionEvalException: Error evaluating expression : Source text : new…](https://p23.zdusercontent.com/attachment/9618168/kYaEUyTO1VyEeqxvXEJNK02K0?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..3nfBahd1qwUcA-ECsxN7fA.Z2Qi6P-YS81-2W7jMm7Xd4xdil_LlMXMHTsD5LaWW-wT7ijJv-kGkFon4-kvE5xHga9Vxm0deF-h9vzp1P86852URYAEltoip-TKhDMWHYboaczpDc9Zc6pvU3muyd-1hyYzbQHjq49Lb9XeMbsxlS7U8y2Gy4yC65N4Jbxm_rfiQkyk8E5JnIhSa5oLa5pUQYWHKOWWRKoBiHsco7_JORyXI2lInFwrDjAlqw27covHFfcTmtdUaQa0Crhgjex-MXFKhC5Gwh1eVUltOSFrD2OsS8KN1iAwvLoFkojWJaY.Hpp--V5YzhtwLNHRGpjYsw)

**SITUAÇÃO:**

Ao tentar emitir o relatório de Provisão de 13º e Férias, é apresentada uma mensagem de erro.

**SOLUÇÃO:**

**(1)** Apague e calcule as provisões da referência em questão, garantindo que os campos sejam corretamente alimentados e permitindo a impressão do relatório.

**OBSERVAÇÃO:** Se houver provisões em referências futuras á que está sendo calculada, é necessário excluir essas provisões posteriores antes de recalcular.

**CAUSA:**

As provisões da referência em que o relatório está sendo impresso não possuem o campo **VLRPARCELA** preenchido.

![Imagem 2: As provisões da referência em que o relatório está sendo impresso não possuem o campo VLRPARCELA preenchido.](https://ajuda.sankhya.com.br/hc/article_attachments/37118350250263)
