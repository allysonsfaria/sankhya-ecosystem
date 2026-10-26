---
id: "360042564874"
titulo: "The value '0' of element 'cMun' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042564874-The-value-0-of-element-cMun-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:42Z"
rotulos: ["ERRONF", "CORE_E04895", "Configuração", "Parceiro", "NF-e", "Cidades", "XML", "SEFAZ", "Valor '0' no Campo 'cMun' Inválido", "Erro"]
---

# The value '0' of element 'cMun' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16482074639383) MENSAGEM:**

[CORE\_E04895] Value '0' is not facet-valid with rrespect to pattern '[0-9]{7}' for type 'TCodMunIBGE'. cvc-type.3.1.3: The value '0' of element 'cMun' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16482051762711) SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo.

![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16482074646039) Acesse a tela "**[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)**" (Caminho de acesso: Configurações » Cadastros), nas abas "**Endereço"** e "**Endereço de Entrega"**, verifique o **"Cód.Cidade**" inserido.

![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16482051765399) Realize essa verificação para todos os parceiros envolvidos no lançamento (Parceiro/Empresa/Parceiro Transportador).

![Imagem 5: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16482051767703) Acesse a tela "**[Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913)"** (Caminho de acesso: Configurações » Cadastros » Endereços), e para os cadastros de cidades localizados no item 1, verifique a informação contida no campo **"Mun. domicílio fiscal":**

![Imagem 6: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/14507759486231)

![Imagem 7: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16482051769495) Informe no campo citado anteriormente o "**Mun. domicílio fiscal**" conforme tabela do IBGE, disponível no link [https://cidades.ibge.gov.br/.](https://cidades.ibge.gov.br/)

Veja o exemplo abaixo, onde é realizada a busca por "Uberlândia" e apresentado o Cód. 3170206:

![Imagem 8: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/360059966134)

![Imagem 9: Realizados os ajustes, busque autorização, depois redigite o Parceiro ou Empresa no cabeçalho da nota e Gere o Lote…](https://ajuda.sankhya.com.br/hc/article_attachments/16482051770775) Realizados os ajustes, busque autorização, depois redigite o Parceiro ou Empresa no cabeçalho da nota e Gere o Lote novamente, nessa ordem.

![Imagem 10: Para parceiros residentes no exterior o Mun. domicilio fiscal deve ser "9999999".](https://ajuda.sankhya.com.br/hc/article_attachments/16482074653847) Para parceiros residentes no exterior o Mun. domicilio fiscal deve ser "9999999".

**![Imagem 11: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16482051775639) CAUSA:**

Esta mensagem é apresentada pois ao validar o campo "**Cidade**" no XML da nota, foi identificado que o valor inserido não é válido, a mensagem mostra que o campo inserido é "Zero", porém podemos ter este retorno se o campo estiver em branco ou com outros caracteres que não correspondem aos códigos validados pelo IBGE.

(1)** Exceção a Regra:**

Quando a operação envolver regiões administrativas (Ex. Cidades-satélites do DF), deve ser considerado o município sede como localidade da operação."
