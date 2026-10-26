---
id: "16034061746071"
titulo: "SPED FISCAL - REGISTRO C170 - CAMPO 10 CST_ICMS valores diferentes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16034061746071-SPED-FISCAL-REGISTRO-C170-CAMPO-10-CST-ICMS-valores-diferentes"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-10-19T18:07:35Z"
rotulos: ["Parceiro", "NF-e", "XML", "Impostos", "EFD", "Situação: CST/CSOSN no registro C170 do EFD Fiscal.", "Causa: Erro quando parceiro é Simples Nacional e não informa CSOSN.", "Solução: Sistema usa hierarquia para preencher CST_ICMS; edite XML se necessário."]
---

# SPED FISCAL - REGISTRO C170 - CAMPO 10 CST_ICMS valores diferentes

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16108305665687)  SITUAÇÃO:**

Como o sistema gera a informação do CST e/ou CSOSN em notas de compra, para o C170 no EFD Fiscal.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16034077956631) CAUSA:**

Ocorre quando o parceiro (emissor da nota) é simples nacional e não informou o Cód CSOSN.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16034059131799) SOLUÇÃO:**

 O sistema segue uma hierarquia para levar as informações para o arquivo TXT do SPED no  registro C170 no campo 10 CST\_ICMS. 
Ao fazer a importação do XML pelo portal de uma nota onde o parceiro é simples nacional automaticamente leva o campo Cód. situação op. Simples nacional (CSON) preenchido, como exemplo levou para o campo o cód 102.

![Imagem 4: O sistema segue uma hierarquia para levar as informações para o arquivo TXT do SPED no registro C170 no campo 10…](https://ajuda.sankhya.com.br/hc/article_attachments/16108195314327)

Ao editar o campo deixando ele em branco a informação levada para o TXT do SPED no  registro C170 no campo 10 CST\_ICMS é a segunda hierarquia que é o campo tributação, no exemplo para o campo o cód 51.

![Imagem 5: Ao editar o campo deixando ele em branco a informação levada para o TXT do SPED no registro C170 no campo 10 CST_ICMS é…](https://ajuda.sankhya.com.br/hc/article_attachments/16108198903063)

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16108273168151) OBSERVAÇÃO:**

Esse comportamento ocorre quando parceiro (emissor da nota) é simples nacional, que tem por obrigação levar no XML da nota o Cód CSOSN. 
Em parceiros LUCRO REAL ou LUCRO PRESUMIDO não é informado esse código.
