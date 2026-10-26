---
id: "34935638994071"
titulo: "Quantidade de provisões incorreta em contratos com faturamento diferente de mensal. Saiba como resolver"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34935638994071-Quantidade-de-provis%C3%B5es-incorreta-em-contratos-com-faturamento-diferente-de-mensal-Saiba-como-resolver"
trilha: "Solução de Problemas > Prestação de Serviços"
atualizado_em: "2026-07-22T14:26:23Z"
rotulos: ["Configuração", "Contratos", "Faturamento", "Contrato", "Financeiro", "Quantidade de provisões incorreta", "contratos com faturamento diferente de mensal", "periodicidade do contrato", "provisões", "Provisão"]
---

# Quantidade de provisões incorreta em contratos com faturamento diferente de mensal. Saiba como resolver

**SITUAÇÃO:**

Ao configurar contratos com periodicidade diferente de **mensal** (como trimestral, semestral ou anual), a quantidade de provisões exibida no sistema pode não corresponder ao número esperado, gerando dúvidas sobre o cálculo realizado.

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/34935638988823)SOLUÇÃO:**

**(1)** A quantidade de provisões geradas é definida de acordo com a **periodicidade do contrato,** na tela **"Contratos"** (Contratos e Serviços > Arquivos > Contratos), aba **"Propriedades",** campo **"Periodicidade do faturamento"**.

![Imagem 2: (1) A quantidade de provisões geradas é definida de acordo com a periodicidade do contrato, na tela "Contratos"…](https://ajuda.sankhya.com.br/hc/article_attachments/34935638988951)

(1)** Exemplo:** Contrato **Trimestral** com o campo **Qtd. Provisão = 4**.

O sistema interpreta que o período total é de **4 meses** (Janeiro, Fevereiro, Março e Abril).

Assim, cria **2 provisões**:

- **1ª provisão:** Janeiro, Fevereiro e Março.
- **2ª provisão:** Abril.

(2)** Como ajustar?**

Se a intenção é ter **4 títulos de provisões trimestrais ao longo do ano**, o campo "**Qtd. Provisão"** deve ser configurado como **12** (referente aos meses do ano).

![Imagem 3: Se a intenção é ter 4 títulos de provisões trimestrais ao longo do ano , o campo " Qtd. Provisão" deve ser configurado…](https://ajuda.sankhya.com.br/hc/article_attachments/34935638989079)

Nesse caso, o sistema criará:

- **1ª provisão:** Janeiro, Fevereiro e Março;
- **2ª provisão:** Abril, Maio e Junho;
- **3ª provisão:** Julho, Agosto e Setembro;
- **4ª provisão:** Outubro, Novembro e Dezembro.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/34935638989335)CAUSA:**

O sistema calcula a quantidade de provisões de acordo com a **periodicidade definida no contrato**.
Quando o campo **Qtd. Provisão** é informado com base no número de parcelas desejadas, mas sem considerar a periodicidade (mensal, trimestral, semestral etc.), ocorre a divergência entre a quantidade configurada e a quantidade realmente gerada.
