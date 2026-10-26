---
id: "7117454111511"
titulo: "Como não gerar parcelas GNRE na tag ndup para Notas de Vendas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7117454111511-Como-n%C3%A3o-gerar-parcelas-GNRE-na-tag-ndup-para-Notas-de-Vendas"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:14:58Z"
rotulos: ["Configuração", "NF-e", "Cobrança", "XML", "Impostos", "Financeiro", "Natureza", "não apagar", "fatura", "duplicatas"]
---

# Como não gerar parcelas GNRE na tag ndup para Notas de Vendas

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16361291819543) MENSAGEM:**

 O valor da parcela do ICMS ST está sendo gerado no XML e não deveria.

<cobr>
<fat>
<nFat>0</nFat>
<vOrig>23.40</vOrig>
<vDesc>0.00</vDesc>
<vLiq>23.40</vLiq>
</fat>
<dup>
<nDup>001</nDup>
<dVenc>2022-06-29</dVenc>
<vDup>23.40</vDup>
</dup>
<dup>
<nDup>002</nDup>
<dVenc>2022-07-11</dVenc>
<vDup>3.40</vDup>
</dup>
</cobr>

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16361328194711)SOLUÇÃO:**

Realize a configuração no tipo de negociação conforme print abaixo, no campo **"Tipo de Financeiro"**, coloque **"Usar da natureza padrão".**

E no campo **"Natureza Padrão"**, insira uma natureza do tipo Receita

![Imagem 3: E no campo "Natureza Padrão" , insira uma natureza do tipo Receita](https://ajuda.sankhya.com.br/attachments/token/RUns6sYmCnSFKaNb0Q4Zfx9l8/?name=image.png)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16361291819799)CAUSA:**

Acontece quando não está parametrizado na preferência **"NATTITNAONOT"** as naturezas de títulos que serão não apresentados na nota.

Caso deseja colocar mais de uma natureza, estas devem ser separadas por virgulas conforme abaixo

![Imagem 5: Caso deseja colocar mais de uma natureza, estas devem ser separadas por virgulas conforme abaixo](https://ajuda.sankhya.com.br/hc/article_attachments/7118941424407)
