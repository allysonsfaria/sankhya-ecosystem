---
id: "36639280919575"
titulo: "NFCom - Valor do item difere de valor unitário x quantidade faturada [nItem: NNN]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36639280919575-NFCom-Valor-do-item-difere-de-valor-unit%C3%A1rio-x-quantidade-faturada-nItem-NNN"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:22:40Z"
rotulos: ["Central de Vendas", "Portal de Vendas", "XML", "SEFAZ", "Valor Unitário", "Passos para resolver", "Razão do erro", "Detalhe do erro", "NFCom", "Erro", "Rejeição 435", "Quantidade faturada", "XML da NFCom", "Documentos Eletrônicos"]
---

# NFCom - Valor do item difere de valor unitário x quantidade faturada [nItem: NNN]

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/36639233047191) **MENSAGEM:**

Rejeição 435: Valor do item difere de valor unitário x quantidade faturada [nItem: NNN]

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/36639233049751)SOLUÇÃO:**

**(1)** Acesse a tela [**''Portal de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas).

**(2)** Localize o documento que foi rejeitado.

**(3)** No campo **''NFcom''**, clique em **''Gerar XML da NFCom em arquivo para conferência''**.

![Imagem 3: (3) No campo ''NFcom'' , clique em ''Gerar XML da NFCom em arquivo para conferência'' .](https://ajuda.sankhya.com.br/hc/article_attachments/36687415376791)

**(4)** Abra o XML gerado e confira o cálculo:

- **vProd** (Valor do Item) deve ser igual a **vItem × qFaturada**.

**OBSERVAÇÃO:** considere uma tolerância de **± R$ 0,10**.

**(5)** Se houver divergência, abra a nota na [**''Central de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas) e redigite os valores corretamente.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/36639280917527)CAUSA:**

A **rejeição 435** ocorre quando uma **NFCom (modelo 66)** é emitida e o **Valor Total do Item (vProd)** é diferente do resultado da multiplicação do **Valor Unitário do Item (vItem)** pela **Quantidade Faturada (qFaturada)**.

**OBSERVAÇÕES:**

- Não há exceções para esta regra de validação.
- Considere uma tolerância de **± R$ 0,10** para mais ou para menos.
