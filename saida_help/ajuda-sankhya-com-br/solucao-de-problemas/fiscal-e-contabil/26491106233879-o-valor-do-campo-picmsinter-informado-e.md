---
id: "26491106233879"
titulo: "O valor do campo pICMSInter informado é inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26491106233879-O-valor-do-campo-pICMSInter-informado-%C3%A9-inv%C3%A1lido"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-10-13T20:24:44Z"
rotulos: ["Produtos", "Alíquotas", "Configuração", "NF-e", "SEFAZ", "Impostos", "Passos para resolver", "Razão do erro", "Detalhe do erro", "interestadual para produtos importados", "destinado para os Estados do Norte e Nordeste ou ES", "informado não é válido", "CORE_04895", "O valor do campo pICMSInter", "7% para os Estados de origem do Sul e Sudeste"]
---

# O valor do campo pICMSInter informado é inválido

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26491106218647) **MENSAGEM:**

[CORE\_04895] O valor do campo pICMSInter (Aliquota interestadual das UF envolvidas - 4% aliquota interestadual para produtos importados, -7% para os Estados de origem do Sul e Sudeste (exceto ES) destinado para os Estados do Norte e Nordeste ou ES, -12% para os demais casos) informado não é válido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26491106222231)SOLUÇÃO:**

Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos), selecione o produto em questão e nele desmarque os campos **"Cacular DIFAL?**e **"Calcular ICMS"**

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26491106225815)CAUSA:**

Normalmente ocorre quando um produto bonificado está configurado para calcular ICMS e DIFAL. Sendo assim, o mesmo é levado para a nota fiscal com um CFOP de produto bonificado e alíquota de DIFAL 100. Com isso, ao tentar aprovar a nota, o sistema cria no XML a TAG 'pICMSInter' com o valor de alíquota do DIFAL, para o produto bonificado.
Com essa configuração, ao tentar enviar a nota, a SEFAZ rejeita a mesma com o seguinte erro.

**"O valor do campo pICMSInter (Alíquota interestadual das UF envolvidas: - 4% alíquota interestadual para produtos importados; - 7% para os Estados de origem do Sul e Sudeste (exceto ES), destinado para os Estados do Norte e Nordeste ou ES; - 12% para os demais casos.) informado não é valido."**
