---
id: "21353079303703"
titulo: "vc-mnExcusive-valid: Value 0.00 is not facet-valid with respect to minExcustve '0.0' for type 'TS_vlrDedPenAlim."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/21353079303703-vc-mnExcusive-valid-Value-0-00-is-not-facet-valid-with-respect-to-minExcustve-0-0-for-type-TS-vlrDedPenAlim"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:31:49Z"
rotulos: ["Impostos", "eSocial", "Configuração Funcionários", "Erro", "S1210"]
---

# vc-mnExcusive-valid: Value 0.00 is not facet-valid with respect to minExcustve '0.0' for type 'TS_vlrDedPenAlim.

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/21353079297303) **MENSAGEM:**

vc-mnExcusive-valid: Value 0.00 is not facet-valid with respect to minExcustve '0.0' for type 'TS\_vlrDedPenAlim.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/21353079300631)CAUSA:**

Esta mensagem de erro ao tentar enviar S1210, é apresentada porque o funcionário tem dependente pensionista cadastrado, mas o percentual de repasse da pensão não esta devidamente preenchida.

**![Imagem 3: SOLUÇÃO: Se o funcionário possuir dois pensionistas ele tem que preencher este campo "Percentual de Repasse" igualmente…](https://ajuda.sankhya.com.br/hc/article_attachments/21353079299095)SOLUÇÃO:** 
Se o funcionário possuir dois pensionistas ele tem que preencher este campo **"Percentual de Repasse"** igualmente para os dois pensionista para que a **soma totalize 100%.**
Por exemplo: 50 em cada dependente pensionista.
 
Agora se o funcionário possui 3 pensionistas tem que preencher o campo:
Por exemplo: 33.3333333  em cada dependente pensionista.
 
![Imagem 4: SOLUÇÃO: Se o funcionário possuir dois pensionistas ele tem que preencher este campo "Percentual de Repasse" igualmente…](https://ajuda.sankhya.com.br/hc/article_attachments/21371122615703)

Após fazer o ajuste do campo, bloquear as folhas do funcionário e liberar novamente através da Rotina (Avançado/ Liberar envio de Folha para eSocial). Gerar os eventos e enviar o S1210.
