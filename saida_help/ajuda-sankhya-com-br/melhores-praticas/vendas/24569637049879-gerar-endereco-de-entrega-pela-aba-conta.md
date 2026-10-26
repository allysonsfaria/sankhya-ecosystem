---
id: "24569637049879"
titulo: "Gerar endereço de entrega pela aba Contatos, usando o endereço principal para tributação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24569637049879-Gerar-endere%C3%A7o-de-entrega-pela-aba-Contatos-usando-o-endere%C3%A7o-principal-para-tributa%C3%A7%C3%A3o"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T14:46:39Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "XML", "Impostos"]
---

# Gerar endereço de entrega pela aba Contatos, usando o endereço principal para tributação

**![Imagem 1: SOLUÇÃO: Quando o usuário tem mais de um endereço de entrega pela aba de "Contatos" , mas precisa tributar no endereço…](https://ajuda.sankhya.com.br/hc/article_attachments/30091048424215) SOLUÇÃO:** Quando o usuário tem mais de um endereço de entrega pela aba de **"Contatos"**, mas precisa tributar no endereço principal do cadastro, pode-se executar as ações abaixo para que seja utilizado o endereço principal.

![Imagem 2: Insira nos campos parceiro remetente e parceiro destinatário a empresa e o parceiro respectivamente no lançamento feito…](https://ajuda.sankhya.com.br/hc/article_attachments/25168111147031) Insira nos campos parceiro remetente e parceiro destinatário a empresa e o parceiro respectivamente no lançamento feito na central;

![Imagem 3: Insira nos campos parceiro remetente e parceiro destinatário a empresa e o parceiro respectivamente no lançamento feito…](https://ajuda.sankhya.com.br/hc/article_attachments/25168139894679)

![Imagem 4: Mantenha o contato de entrega conforme necessário e o parâmetro ENDICMS igual a 0 e o tipo "Inteiro";](https://ajuda.sankhya.com.br/hc/article_attachments/25168139901975) Mantenha o contato de entrega conforme necessário e o parâmetro **ENDICMS** igual a 0 e o tipo **"Inteiro";**

![Imagem 5: Mantenha o contato de entrega conforme necessário e o parâmetro ENDICMS igual a 0 e o tipo "Inteiro";](https://ajuda.sankhya.com.br/hc/article_attachments/25168111168535)

![Imagem 6: Ligue o parâmetro "Usa endereço de entrega dos contatos - USENDENTREGA", a ssim, o sistema calculará o ICMS baseado nos…](https://ajuda.sankhya.com.br/hc/article_attachments/29588304758935) Ligue o parâmetro **"Usa endereço de entrega dos contatos - USENDENTREGA",** assim, o sistema calculará o ICMS baseado nos campos parceiro remetente e parceiro destinatário e a tag <entrega> será criada com o contato de entrega do parceiro conforme definido no campo do cabeçalho da nota.

Cenário atende a partir da norma técnica EC 87/2015 página 43.

Exemplo do XML abaixo.

![Imagem 7: Exemplo do XML abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/25168139927063)
