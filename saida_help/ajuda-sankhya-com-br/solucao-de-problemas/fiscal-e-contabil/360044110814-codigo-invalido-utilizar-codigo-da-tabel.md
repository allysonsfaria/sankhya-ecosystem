---
id: "360044110814"
titulo: "Código inválido. Utilizar código da \"Tabela de Códigos Situação Tributária do PIS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110814-C%C3%B3digo-inv%C3%A1lido-Utilizar-c%C3%B3digo-da-Tabela-de-C%C3%B3digos-Situa%C3%A7%C3%A3o-Tribut%C3%A1ria-do-PIS"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:03Z"
rotulos: ["#RevisadoJR", "Fiscal", "SEFAZ", "Impostos", "EFD", "CST PIS inválido", "Revise ajustes CST PIS", "Consulte a contabilidade", "Erro"]
---

# Código inválido. Utilizar código da "Tabela de Códigos Situação Tributária do PIS

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18610371100055) MENSAGEM:**

Código inválido. Utilizar código da "Tabela de Códigos Situação Tributária do PIS.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18610344503703) SITUAÇÃO:**

Mensagem retornada na validação da 'Escrituração Fiscal Digital', quando enviado código CST de PIS que diverge da Tabela de Códigos Situação Tributária do PIS registrada pela SEFAZ.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18610371116823) CAUSA:**

Ocorre quando enviado código CST de PIS que diverge da Tabela de Códigos Situação Tributária do PIS registrada pela SEFAZ.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18610344513431) SOLUÇÃO:**

![Imagem 5: Identifique através do registro rejeitado, qual o código produto e número documento responsáveis pela causa do erro.](https://ajuda.sankhya.com.br/hc/article_attachments/18610344529687) Identifique através do registro rejeitado, qual o código produto e número documento responsáveis pela causa do erro.

**Exemplo**

|C100|0|1|000004682|55|00|0|**7113**|31181013564754000116550000000071131032052930|24102018|24102018|100,00|0|17,00|0,00|117,00|1|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,02|0,09|0,00|0,00|

- REGISTRO C100 >> POSIÇÃO 8 >> NUM\_DOC = 7113

|C170|1|**11006**||3,00000|UN|117,00|17,00|0|000|1102|12|0,00|0,00|0,00|0,00|0,00|0,00|0|49||0,00|0,00|0,00|**00**|3,00|0,0000||0,6500|0,02|00|3,00|0,0000||3,0000|0,09||

- REGISTRO C170 >> POSIÇÃO 3 >> COD\_ITEM = 11006
- REGISTRO C170 >> POSIÇÃO 25 >> CST\_PIS = 00

![Imagem 6: Identificado o item, n° documento e CST enviado, é necessário realizar os devidos ajustes para o CST que se enquadre na…](https://ajuda.sankhya.com.br/hc/article_attachments/18610344535319) Identificado o item, n° documento e CST enviado, é necessário realizar os devidos ajustes para o CST que se enquadre na Tabela de Códigos Situação Tributária do PIS, conforme orientações de sua contabilidade.

**Importante:**

![Imagem 7: Identificado CST'S indevidos, avalie as configurações atuais de PIS, de forma a prevenir que o problema não volte a…](https://ajuda.sankhya.com.br/hc/article_attachments/18610344529687) Identificado CST'S indevidos, avalie as configurações atuais de PIS, de forma a prevenir que o problema não volte a ocorrer.

![Imagem 8: Para notas de saída, emissão própria, já aprovadas, necessário uma sintonia junto ao Contador da empresa, para avaliar…](https://ajuda.sankhya.com.br/hc/article_attachments/18610344535319) Para notas de saída, emissão própria, já aprovadas, necessário uma sintonia junto ao Contador da empresa, para avaliar a solução adequada.

![Imagem 9: Tabela de Códigos estabelecidos através da Instrução Normativa RFB nº 1.009:](https://ajuda.sankhya.com.br/hc/article_attachments/18610344537111) Tabela de Códigos estabelecidos através da Instrução Normativa RFB nº 1.009:
