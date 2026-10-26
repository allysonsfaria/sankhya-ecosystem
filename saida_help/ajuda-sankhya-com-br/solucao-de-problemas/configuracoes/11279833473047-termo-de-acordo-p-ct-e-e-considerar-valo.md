---
id: "11279833473047"
titulo: " \"Termo de Acordo p/ CT-e\" e \"Considerar valor total dos itens mais valor total tributado para tags vTprest e vRec\" - Cadastro de Parceiros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/11279833473047--Termo-de-Acordo-p-CT-e-e-Considerar-valor-total-dos-itens-mais-valor-total-tributado-para-tags-vTprest-e-vRec-Cadastro-de-Parceiros"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:01:55Z"
rotulos: ["CT-e", "Configuração", "Parceiro", "XML", "TOP", "Financeiro", "não apagar", "Configuração de Desconto para CT-e", "Estratégia para Desconto de ICMS em CT-e"]
---

#  "Termo de Acordo p/ CT-e" e "Considerar valor total dos itens mais valor total tributado para tags vTprest e vRec" - Cadastro de Parceiros

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16417653580183) MENSAGEM:**

"Termo de Acordo p/ CT-e" e "Considerar valor total dos itens mais valor total tributado para tags vTprest e vRec".

A marcação "Considerar valor total dos itens mais valor total tributado para tags vTprest e vRec?" definirá se o valor da tag vTotTib será somado nas tags vRec e vTprest. Algumas vezes o cliente precisa que a tag vRec saia o valor do total da nota menos o ICMS.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16417653584791) SOLUÇÃO:**

Para o cálculo do financeiro com o desconto do Termo de Acordo, além do campo "Tem Termo de Acordo p/ CT-e?" do parceiro estar marcado, também é necessário que a TOP esteja marcada com a opção "Permite financeiro menor que o valor total da nota". 
Este campo só aparece para configuração na TOP quando o parâmetro HABOPCFINMENNOT - Hab. opç. que perm. fin. menor que o vlr. da nota está ligado. Isso porque o termo de acordo pode fazer com que o financeiro fique com valor menor que o da nota, então é necessário essa configuração.

**![Imagem 3: OBSERVAÇÃO: É interessante realizar essa marcação em uma TOP especifica, ou seja, usar para aqueles clientes que…](https://ajuda.sankhya.com.br/hc/article_attachments/16417653586839) OBSERVAÇÃO:** É interessante realizar essa marcação em uma TOP especifica, ou seja, usar para aqueles clientes que possuem o desconto do ICMS (no financeiro), mas que o valor seja mencionado no XML.

Essas opções só funcionam para CT-e de saída.

![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16417674998295) **CAUSA:**

Se o parâmetro **"HABOPCFINMENNOT"** não estiver habilitado, o desconto realizado no financeiro do valor do ICMS será descontado também da tag vTprest do xml, não sendo justificável.
