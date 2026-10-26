---
id: "360044617093"
titulo: "O parceiro deve ser diferente de zero na nota de Nro Único: 'X'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617093-O-parceiro-deve-ser-diferente-de-zero-na-nota-de-Nro-%C3%9Anico-X"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:28Z"
rotulos: ["#PUBLIFER", "Configuração", "Parceiro", "Estoque", "Preferências", "ORA-20101", "Parceiro deve ser diferente de zero na nota.", "Verifique campos \"Modelo Ajuste de Entrada/Saída\".", "Preencha o campo \"Parceiro\" nos modelos.", "Erro"]
---

# O parceiro deve ser diferente de zero na nota de Nro Único: 'X'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16592671254935) MENSAGEM:**

[ORA-20101]: O parceiro deve ser diferente de zero na nota de Nro Único:

[ORA-06512]: em "SANKHYA.TRG\_INC\_TGFCAB", line 443

[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG\_INC\_TGFCAB'

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16592671260567)SOLUÇÃO:**

![Imagem 3: Selecione a empresa utilizada no processo de inventário na tela " Empresa " (Caminho de acesso: Comercial »…](https://ajuda.sankhya.com.br/hc/article_attachments/16592695284503) Selecione a empresa utilizada no processo de inventário na tela "**Empresa**" (Caminho de acesso: Comercial » Preferências).

![Imagem 4: Na aba "Estoque/Preço" , verifique as informações apresentadas nos campos "Modelo Ajuste de Entrada de Estoque " e "…](https://ajuda.sankhya.com.br/hc/article_attachments/16592695288343) Na aba **"Estoque/Preço"**, verifique as informações apresentadas nos campos **"Modelo Ajuste de Entrada de Estoque**" e "**Modelo Ajuste de Saída de Estoque**":

![Imagem 5: Na aba "Estoque/Preço" , verifique as informações apresentadas nos campos "Modelo Ajuste de Entrada de Estoque " e "…](https://ajuda.sankhya.com.br/hc/article_attachments/15238735639447)

![Imagem 6: Busque pelos códigos de modelo localizados no item 2, através da tela " Modelo de Notas e Pedidos " (Comercial »…](https://ajuda.sankhya.com.br/hc/article_attachments/16592671268631) Busque pelos códigos de modelo localizados no item 2, através da tela "**Modelo de Notas e Pedidos**" (Comercial » Consulta).

![Imagem 7: Para ambos modelos, preencha o campo "Parceiro" :](https://ajuda.sankhya.com.br/hc/article_attachments/16592695293335) Para ambos modelos, preencha o campo **"Parceiro"**:

![Imagem 8: Para ambos modelos, preencha o campo "Parceiro" :](https://ajuda.sankhya.com.br/hc/article_attachments/15238828664855)

Aconselha-se ter o cadastro da empresa como parceiro e utilizá-lo para tal.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16592671275031) CAUSA:**

Ao tentar realizar ajuste de estoque, caso os modelos vinculados para esse ajuste não possuam o campo Parceiro informado, será apresentada a mensagem.
