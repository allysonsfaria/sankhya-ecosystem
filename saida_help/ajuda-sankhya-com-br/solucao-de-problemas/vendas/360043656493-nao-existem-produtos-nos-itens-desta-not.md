---
id: "360043656493"
titulo: "Não existem produtos nos itens desta nota. Informe o valor de desconto no campo desconto de serviços"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043656493-N%C3%A3o-existem-produtos-nos-itens-desta-nota-Informe-o-valor-de-desconto-no-campo-desconto-de-servi%C3%A7os"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:33Z"
rotulos: ["Configuração", "Central de Vendas", "CORE_E02699", "NFS-e", "Verifique campo \"Total desc. serviços\"", "Use campo para descontos em NFS-e", "Adicione campo ao rodapé do Layout", "Erro"]
---

# Não existem produtos nos itens desta nota. Informe o valor de desconto no campo desconto de serviços

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16135440524951) MENSAGEM:**

[CORE\_E02699] Não existem produtos nos itens desta nota. Informe o valor de desconto no campo desconto de serviços.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16135417891607) SITUAÇÃO:**

Ao tentar inserir um desconto no total da nota(rodapé), para uma NFS-e, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16135440528279) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse ( Comercial » Configuração » Configurador de Layout da Nota) :](https://ajuda.sankhya.com.br/hc/article_attachments/16135440530583) Acesse (Comercial » Configuração » Configurador de Layout da Nota):

**(2)** Acesse o Layout que geralmente é usado para Notas de Serviço e na grade de **"Campos disponíveis"**, pesquise pelo campo **"Total desc. serviços"**. Disponibilize o campo no rodapé do Layout da Nota e salve a alteração.

![Imagem 5: Acesse ( Comercial » Rotinas » Central de Vendas) :](https://ajuda.sankhya.com.br/hc/article_attachments/16135417896343) Acesse (Comercial » Rotinas » Central de Vendas):

**(2)** Acesse novamente a Nota e no rodapé apresentará o campo Total desc. serviços que será usado para destacar desconto em NFS-e's. Este campo será considerado para trabalhar com desconto em notas de serviço.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16135440536215) CAUSA:**

Ocorre quando o desconto em uma NFS-e não está declarado no campo próprio que é Total desc. serviços, geralmente no rodapé da Nota.
