---
id: "4404722929303"
titulo: " A soma dos valores dos fatos contábeis (somatório do campo 04 dos registros J215 filhos) deve ser igual ao saldo final do código de aglutinação (campo 07 do registro J210) menos o saldo inicial do código de aglutinação (campo 05 do registro J210)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4404722929303--A-soma-dos-valores-dos-fatos-cont%C3%A1beis-somat%C3%B3rio-do-campo-04-dos-registros-J215-filhos-deve-ser-igual-ao-saldo-final-do-c%C3%B3digo-de-aglutina%C3%A7%C3%A3o-campo-07-do-registro-J210-menos-o-saldo-inicial-do-c%C3%B3digo-de-aglutina%C3%A7%C3%A3o-campo-05-do-registro-J210"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:22:59Z"
rotulos: ["Configuração", "ECD", "Fiscal", "Financeiro", "DLPA", "DMPL", "#publicadoHyago", "Conciliação de Saldo na DMPL", "Resolução de Discrepância nos Registros J210 e J215"]
---

#  A soma dos valores dos fatos contábeis (somatório do campo 04 dos registros J215 filhos) deve ser igual ao saldo final do código de aglutinação (campo 07 do registro J210) menos o saldo inicial do código de aglutinação (campo 05 do registro J210)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16369123233175) MENSAGEM:**

 A soma dos valores dos fatos contábeis (somatório do campo 04 dos registros J215 filhos) deve ser igual ao saldo final do código de aglutinação (campo 07 do registro J210) menos o saldo inicial do código de aglutinação (campo 05 do registro J210).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16369123235223) SOLUÇÃO:**

Para a resolução do incidente, siga os passos abaixo:

![Imagem 3: Na estrutura da DMPL gerada na ECD, deverá ter os registros J210 e J215.](https://ajuda.sankhya.com.br/hc/article_attachments/16369123237143) Na estrutura da DMPL gerada na ECD, deverá ter os registros J210 e J215.

O J210 é gerado a partir das configurações na tela **"Demonstrativos ECD"**, aba **"DMPL/DLPA"**.

**Exemplo:**

![Imagem 4: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/15694701404439)

**![Imagem 5: IMPORTANTE: No Grid debaixo da estrutura deve ser vinculada as contas que são usadas nos lançamentos que alteram o PL.](https://ajuda.sankhya.com.br/hc/article_attachments/16369154507671) IMPORTANTE:** No Grid debaixo da estrutura deve ser vinculada as contas que são usadas nos lançamentos que alteram o PL.

![Imagem 6: Fatos Contábeis são as ocorrências que alteram, qualitativa e/ou quantitativamente o Patrimônio. para mais informações,…](https://ajuda.sankhya.com.br/hc/article_attachments/16369123240471) Fatos Contábeis são as ocorrências que alteram, qualitativa e/ou quantitativamente o Patrimônio. 
para mais informações, acessar o Artigo ( [Demonstrativos ECD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjo0MDg1NjIyMjcwMTQsInRpY2tldF9pZCI6MTA5NDc0LCJjaGFubmVsX2lkIjo2MywidHlwZSI6IlNFQVJDSCIsImV4cCI6MTYyOTQ4NjAzM30.Hz1HdpCIE4sGiC_ufQlFZnwPuccTtV5gIiWmDR_2LpU)).

- O J215 é gerado com base nas configurações na tela Demonstrativos ECD, aba Fatos DMPL/DLPA

**Exemplo:**

![Imagem 7: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/15694736996503)

**![Imagem 8: IMPORTANTE: deverá ter o fato contábil vinculado ao histórico contábil e este histórico no lançamento contábil. O…](https://ajuda.sankhya.com.br/hc/article_attachments/16369154507671) IMPORTANTE:** deverá ter o fato contábil vinculado ao histórico contábil e este histórico no lançamento contábil. O histórico aqui vinculado, é o mesmo usado nos lançamento que alteram o PL.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16369123248023) CAUSA:**

No J210 deverá ser informada a Demonstração de Lucros ou Prejuízos Acumulados (DLPA) ou a Demonstração de Mutações do Patrimônio Líquido (DMPL). Ao gerar o J210 deve ser gerado também o J215 . Neste registro deverão ser informados os fatos contábeis que alteram a conta “Lucros Acumulados” ou a conta “Prejuízos Acumulados” ou quaisquer outras contas do Patrimônio Líquido. Quando gera o J210 e não gera o J215, o erro é apresentado.
