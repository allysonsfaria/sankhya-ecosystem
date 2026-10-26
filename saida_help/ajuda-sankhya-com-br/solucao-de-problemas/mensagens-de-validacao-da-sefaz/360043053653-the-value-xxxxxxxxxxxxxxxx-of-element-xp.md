---
id: "360043053653"
titulo: "The value 'XXXXXXXXXXXXXXXX' of element 'xPed' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043053653-The-value-XXXXXXXXXXXXXXXX-of-element-xPed-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:37Z"
rotulos: ["ERRONF", "DUVIDANF", "#PUBLIFER", "Configuração", "NF-e", "XML", "SEFAZ", "Valor Inválido para Número do Pedido", "Erro"]
---

# The value 'XXXXXXXXXXXXXXXX' of element 'xPed' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16473977748503) MENSAGEM:**

Erro durante validação do XML do lote: cvc-maxLength-valid: Value 'XXXXXXXXXXXXXXXX' with length = '23' is not facet-valid with respect to maxLength '15' for type '#AnonType\_xPedproddetinfNFeTNFe'. cvc-type.3.1.3: The value 'XXXXXXXXXXXXXXXX' of element 'xPed' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16473993289751) SOLUÇÃO:**

![Imagem 3: Ajuste o campo 'Número Pedido', respeitando o limite de 15 caracteres aceitos pela SEFAZ.](https://ajuda.sankhya.com.br/hc/article_attachments/16473977751447) Ajuste o campo 'Número Pedido', respeitando o limite de 15 caracteres aceitos pela SEFAZ.

![Imagem 4: Ajuste o campo 'Número Pedido', respeitando o limite de 15 caracteres aceitos pela SEFAZ.](https://ajuda.sankhya.com.br/hc/article_attachments/14477492048919)

![Imagem 5: Caso não localize esse campo, acesse a tela " Configurador de Layout da Nota" (Caminho de acesso: Comercial »…](https://ajuda.sankhya.com.br/hc/article_attachments/16473977752727) Caso não localize esse campo, acesse a tela "[**Configurador de Layout da Nota"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634) (Caminho de acesso: Comercial » Configuração) e selecione o layout utilizado.

![Imagem 6: Para inserção do campo " Número pedido" no cabeçalho da nota, selecione em " Campos Disponíveis" o campo " Número…](https://ajuda.sankhya.com.br/hc/article_attachments/16473993296279) Para inserção do campo "**Número pedido"** no cabeçalho da nota, selecione em "**Campos Disponíveis"** o campo "**Número Pedido"** e arraste o mesmo para o quadrante cabeçalho.

**![Imagem 7: IMPORTANTE :](https://ajuda.sankhya.com.br/hc/article_attachments/16473977754519) IMPORTANTE:**

- Caso essa informação não esteja preenchida no cabeçalho da nota, considere esse mesmo campo na linha dos itens.
- Se não estiver preenchido no cabeçalho e nem nos itens, o sistema irá buscar o número do pedido de origem.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16473993301015) CAUSA:**

Mensagem apresentada quando a tag <xPed> é enviada com mais de 15 caracteres.
