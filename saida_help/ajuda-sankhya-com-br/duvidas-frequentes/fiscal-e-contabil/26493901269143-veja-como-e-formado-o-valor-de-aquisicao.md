---
id: "26493901269143"
titulo: "Veja como é formado o valor de aquisição do bem na entrada da nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26493901269143-Veja-como-%C3%A9-formado-o-valor-de-aquisi%C3%A7%C3%A3o-do-bem-na-entrada-da-nota"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-09-14T12:28:50Z"
rotulos: ["Configuração", "NF-e", "SUBCREDICMSCIAP", "Impostos", "Estoque", "Preferências", "valor de aquisição do bem na entrada da nota", "AJUSBEMTOTNOTA", "VLRAQUISSEMIMP"]
---

# Veja como é formado o valor de aquisição do bem na entrada da nota

O valor de aquisição de um bem é o total gasto para comprá-lo, incluindo não apenas o preço de compra, mas também quaisquer custos adicionais relacionados à sua aquisição, como impostos, fretes e outros encargos.

Parâmetros que afetam a entrada do **Bem via portal de compras:**

- **"AJUSBEMTOTNOTA -Ajustar valor aquis. do bem pelo total da nota":** ligado
- **"VLRAQUISSEMIMP-Considerar valor de aquisição de BEM sem impostos?":**  desligado
- **"SUBCREDICMSCIAP - Subtrair Crédito de ICMS do CIAP do valor de aquis":** desligado

Na tela **"Empresa"** (Caminho: Comercial » Preferências ), de acordo com cada opção selecionada no campo **"Calcular o valor de aquisição do bem",** o sistema terá um comportamento diferente. Confira:

**1 - Seguindo as regras dos parâmetros:** esta opção obedece o comportamento dos parâmetros **SUBCREDICMSCIAP** e **VLRAQUISSEMIMP**;

**2 - Valor do bem:** selecionando esta opção, a depreciação será feita de acordo o cálculo;
Vlr. Aquisição (TCIBEM.VLRAQUISICAO)= Valor do bem + Frete Extra Nota
Vlr. Atual do bem (TCIBEM.VLRDEP)= Valor do bem + Frete Extra Nota - ICMS Op Própria - Icms Frete

**3 - Valor do bem sem ICMS operação própria:** esta opção segue o comportamento do parâmetro SUBCREDICMSCIAP desligado e VLRAQUISSEMIMP ligado;
Vlr. Aquisição (TCIBEM.VLRAQUISICAO)= Valor do bem - ICMS Op. Própria
Vlr. Atual do bem (TCIBEM.VLRDEP)= Valor do bem - ICMS Op. Própria

**4 - Valor do bem com ICMS diferencial de alíquotas:** esta opção obedece o comportamento do parâmetro SUBCREDICMSCIAP ligado e VLRAQUISSEMIMP desligado;
Vlr. Aquisição (TCIBEM.VLRAQUISICAO)= Valor do bem + Frete Extra Nota + ICMS Diferencial Alíquota + Diferencial Alíquota Frete
Vlr. Atual do bem (TCIBEM.VLRDEP)= Valor do bem + Frete Extra Nota - ICMS Diferencial Alíquota - ICMS Frete

**5 - Valor do bem com ICMS diferencial de alíquotas, sem ICMS CIAP:** esta opção seguirá o comportamento do parâmetro SUBCREDICMSCIAP e VLRAQUISSEMIMP desligados.
Vlr. Aquisição (TCIBEM.VLRAQUISICAO)= Valor do bem + Frete Extra Nota + ICMS Diferencial Alíquota - (ICMS CIAP + ICMS Frete)
Vlr. Atual do bem (TCIBEM.VLRDEP)= Valor do bem + Frete Extra Nota + ICMS Diferencial Alíquota - (ICMS CIAP + ICMS Frete)
