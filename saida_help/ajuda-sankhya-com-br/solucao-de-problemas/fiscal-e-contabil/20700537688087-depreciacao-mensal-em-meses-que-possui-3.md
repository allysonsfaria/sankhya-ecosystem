---
id: "20700537688087"
titulo: "Depreciação mensal em meses que possui 31 dias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/20700537688087-Deprecia%C3%A7%C3%A3o-mensal-em-meses-que-possui-31-dias"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:50:46Z"
rotulos: ["Configuração", "Relatórios", "Impostos", "Financeiro", "Depreciação"]
---

# Depreciação mensal em meses que possui 31 dias

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/20700551548311) **MENSAGEM:**

Depreciação mensal em meses com 31 dias.

**SOLUÇÃO:**

Além das informações já disponíveis na documentação [''**Cálculo da Depreciação Mensal''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053497654-C%C3%A1lculo-da-Deprecia%C3%A7%C3%A3o-Mensal), no qual são apresentados alguns parâmetros que influenciam essa rotina, destaca-se um parâmetro específico que atua no cálculo da depreciação de ativos imobilizados em meses com 31 dias.

Esse parâmetro possibilita que o cálculo do percentual diário seja realizado considerando corretamente todos os dias do mês, garantindo maior aderência à regra contábil adotada pela empresa.

Trata-se do parâmetro:

- **"Depreciação pro rata considera todos os dias do mês - DEPPRORATDIAMES"**

**OBSERVAÇÃO:** Todos os parâmetros apresentados nesta rotina devem ser configurados conforme a necessidade específica de cada empresa, considerando suas políticas contábeis e critérios internos.

**CAUSA:**

Este cenário ocorre quando a empresa adota o processo de Depreciação Mensal de bens do ativo imobilizado e, ao emitir o relatório de Depreciação Mensal Analítica, observa-se que, ao informar a data de início da depreciação no dia 31, o sistema considera o valor total da depreciação mensal, em vez de calcular a depreciação proporcional ao dia informado.
