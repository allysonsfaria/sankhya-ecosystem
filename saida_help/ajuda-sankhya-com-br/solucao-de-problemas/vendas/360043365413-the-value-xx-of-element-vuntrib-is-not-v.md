---
id: "360043365413"
titulo: "The value '-XX' of element 'vUnTrib' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043365413-The-value-XX-of-element-vUnTrib-is-not-valid"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:11Z"
rotulos: ["Produtos", "NF-e", "Central de Vendas", "XML", "SEFAZ", "Valor '-XX' inválido para 'vUnTrib'", "Verifique valores negativos em itens; ajuste e gere novo lote", "Valores inconsistentes na tag <vUnCom> do XML", "Erro"]
---

# The value '-XX' of element 'vUnTrib' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16453508440343) MENSAGEM:**

cvc-pattern-valid: Value '-XX' is not facet-valid with respect to pattern '0|0\.[0-9]{1,10}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,10})?' for type 'TDec\_1110v'.
cvc-type.3.1.3: The value '-XX' of element 'vUnTrib' is not valid.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16453508444183) SITUAÇÃO:**

Ao realizar emissão de NF-e no **SankhyaW**, acessando o respectivo 'Portal' de emissão, na opção "**Outras Opções**" » "**Ver Acompanhamento"** é possível consultar a rejeição a seguir:

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16453508445207) SOLUÇÃO:**

Para correção siga os passos abaixo:

![Imagem 4: Identifique no lançamento da nota, se existe valor negativo para algum dos itens, no campo " Vlr.Unitário", conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/16453476051351) Identifique no lançamento da nota, se existe **valor negativo** para algum dos itens, no campo "**Vlr.Unitário",** conforme exemplo abaixo:

![Imagem 5: Identifique no lançamento da nota, se existe valor negativo para algum dos itens, no campo " Vlr.Unitário", conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/360060892793)

![Imagem 6: Para uma conferência mais efetiva, acesse o " Portal de Vendas " » " Botão NF-e" » "Gerar XML da NF-e" em arquivo para…](https://ajuda.sankhya.com.br/hc/article_attachments/16453508452119) Para uma conferência mais efetiva, acesse o "**[Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654)"** » "**Botão NF-e"** »**"Gerar XML da NF-e"** em arquivo para conferência', através do XML gerado, confira as tags abaixo para todos os itens, até localizar o item que possui valor negativo:

<prod>
     <cEAN/>
     <cProd>**8585**</cProd>
     <xProd>**PRODUTO TESTE LU**</xProd>
     <NCM>**64029990**</NCM>
     <CFOP>**5102**</CFOP>
     <uCom>**CX**</uCom>
     <qCom>**1**</qCom>
     <vUnCom>**-129.9**</vUnCom>
     <vProd>**-129.90**</vProd>
     <cEANTrib/>
     <uTrib>**CX**</uTrib>

![Imagem 7: Identificado o item com valores incoerentes, realize os devidos ajustes na " Central de Vendas ", redigite o cabeçalho…](https://ajuda.sankhya.com.br/hc/article_attachments/16453476053015) Identificado o item com valores incoerentes, realize os devidos ajustes na "**Central de Vendas**", redigite o cabeçalho da nota e gere um novo lote.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16453476055831) CAUSA:**

Mensagem apresentada ao gerar lote de uma nota fiscal eletrônica com valores inconsistentes na tag <vUnCom>.
