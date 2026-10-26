---
id: "17990487527575"
titulo: "cvc-minExclusive-valid: Value '0.00' is not facet-valid with respect to minExclusive '0.0' for type TS_vrRubr"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17990487527575-cvc-minExclusive-valid-Value-0-00-is-not-facet-valid-with-respect-to-minExclusive-0-0-for-type-TS-vrRubr"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-08-18T20:03:31Z"
rotulos: ["Eventos", "Fiscal", "XML", "eSocial", "Exclua eventos sem valor do cálculo", "Erro ao enviar evento 1200", "Valor '0.00' em vrRubr não é válido", "Erro"]
---

# cvc-minExclusive-valid: Value '0.00' is not facet-valid with respect to minExclusive '0.0' for type TS_vrRubr

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17990487515031) MENSAGEM:**

Cvc-minExclusive-valid: Value '0.00' is not facet-valid with respect to minExclusive '0.0' for type TS\_vrRubr. cvc-type.3.1 .3: The value '0.00' of element 'vrRubr' is not valid. cvc-minExclusive-valid: Value '0.00' is not facet-valid with respect to minExclusive '0.0' for type TS\_vrRubr. cvc-type.3.1.3: The value '0.00' of element 'vrRubf is not valid.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17990448339223) SITUAÇÃO:**

Ao tentar enviar o evento 1200 a mensagem é apresentada.

O erro é apresentado quando o XML enviado não está respeitando as regras de schema definidos pelo governo, por exemplo, a tag "vrRubr"  passando como 0.00, então pode observar que no calculo o evento referente a esta rubrica esta com valor zerado.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17990454857879) SOLUÇÃO:**

Quando o funcionário não tiver valor no evento não precisa colocar o valor "0,00", pode excluir o evento do cálculo da folha.
