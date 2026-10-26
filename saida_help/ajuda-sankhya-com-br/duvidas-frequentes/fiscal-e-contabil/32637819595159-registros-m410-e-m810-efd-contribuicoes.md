---
id: "32637819595159"
titulo: "Registros M410 e M810 (EFD Contribuições) e suas respectivas contas contábeis"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32637819595159-Registros-M410-e-M810-EFD-Contribui%C3%A7%C3%B5es-e-suas-respectivas-contas-cont%C3%A1beis"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:30:48Z"
rotulos: ["Configuração", "SPED", "Fiscal", "Contas", "Impostos", "TOP", "EFD Contribuições", "Passos para resolver", "Razão do erro", "Detalhe do erro", "e suas respectivas contas contábeis", "M400", "M800", "Registros M410 e M810 (EFD Contribuições)"]
---

# Registros M410 e M810 (EFD Contribuições) e suas respectivas contas contábeis

Ao gerar o **EFD Contribuições**, utilizando os registros **M410 e M810**, pode ocorrer a seguinte situação: no SPED Contribuições, o sistema não está registrando corretamente as informações nos registros M410 e M810.

A configuração foi realizada na TOP, pois o mesmo produto possui registros distintos conforme a operação, entretanto, o sistema não está capturando as informações de forma adequada.

A conta contábil está sendo registrada apenas para uma operação, enquanto nas notas fiscais as contas estão corretamente atribuídas.

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32637790778263) SOLUÇÃO:**

**(1)** **Atualmente, o comportamento do sistema é o seguinte:**

É necessário considerar qual conta foi mais utilizada nos registros anteriores e gerar os dados nos registros M400 e M800 de acordo com essa conta.

Em outras palavras, não são consideradas todas as contas utilizadas nos lançamentos das notas fiscais.

Para ajustes adicionais, o processo deve ser realizado por meio do Validador.
