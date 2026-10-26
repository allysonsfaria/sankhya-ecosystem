---
id: "34894940140055"
titulo: "CORE_E05076: O produto XXX - não possui lastro ou camadas informados para uma unidade alternativa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34894940140055-CORE-E05076-O-produto-XXX-n%C3%A3o-possui-lastro-ou-camadas-informados-para-uma-unidade-alternativa"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:26:27Z"
rotulos: ["Produtos", "Configuração", "WMS", "Estoque", "Unidade Alternativa", "CORE_E05076", "Exige Lastro e Camadas", "Unidades Alternativas", "O produto XXX não possui lastro ou camadas informados para uma unidade alternativa", "Norma de Paletização", "\"Lastro\" e \"Camadas\" da unidade"]
---

# CORE_E05076: O produto XXX - não possui lastro ou camadas informados para uma unidade alternativa

**MENSAGEM**

[CORE\_E05076] O produto XXX não possui lastro ou camadas informados para uma unidade alternativa

**SITUAÇÃO**

Esta mensagem aparece quando o usuário está realizando operações no **sistema WMS** com produtos que possuem **unidades alternativas** configuradas, mas que não têm os campos de **lastro e camadas** devidamente preenchidos para essas unidades.

**SOLUÇÃO**

**(1)** Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos).

**(2)** Filtre o **produto informado na mensagem de erro**.

**(3)** Acesse a aba **"WMS"** do produto.

**(4)** Na seção **"Norma de Paletização"**, verifique se o campo **"Exige Lastro e Camadas"** está marcado.

**(5)** Caso esteja marcado, configure o **lastro e camadas** para o produto principal nos campos correspondentes.

**(6)** Acesse a aba **"Unidades Alternativas"**.

**(7)** Caso o produto trabalhe com **unidade alternativa,** preencha os campos **"Lastro"** e **"Camadas"** da unidade.

**CAUSA**

Esta mensagem ocorre quando o produto está configurado para **exigir lastro e camadas** na norma de paletização, mas alguma **unidade alternativa** do produto não possui os campos **"Lastro"** e **"Camadas"** devidamente preenchidos.
