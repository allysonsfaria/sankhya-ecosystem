---
id: "32082804998679"
titulo: "Como gerar informações de endereço de retirada na emissão de NF-e?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32082804998679-Como-gerar-informa%C3%A7%C3%B5es-de-endere%C3%A7o-de-retirada-na-emiss%C3%A3o-de-NF-e"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:32:06Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "Central de Vendas", "XML", "Passos para resolver", "Razão do erro", "Detalhe do erro", "gerar informações", "endereço de retirada", "emissão de NF-e"]
---

# Como gerar informações de endereço de retirada na emissão de NF-e?

Em certas situações, pode ser necessário emitir uma NF-e que inclua o grupo de tags `<retirada>`, indicando o local onde o cliente ou comprador realizou a retirada da mercadoria. Para tal, siga os passos abaixo:

![Imagem 1: Acesse a tela de "Empresas" (Configurações » Cadastros » Empresas) , na aba "Local de Retirada" , insira o código do…](https://ajuda.sankhya.com.br/hc/article_attachments/32399275341335) Acesse a tela de **"Empresas"** **(Configurações » Cadastros » Empresas)**, na aba **"Local de Retirada"**, insira o código do parceiro onde será realizada a retirada e garanta que esse **cadastro está ativo.**

![Imagem 2: Acesse a tela de "Empresas" (Configurações » Cadastros » Empresas) , na aba "Local de Retirada" , insira o código do…](https://ajuda.sankhya.com.br/hc/article_attachments/32400100454167)

![Imagem 3: Na tela de "Central de Vendas" , no lançamento da NF-e, preencha o campo: " Cód. Parceiro Retirada " que. nesse caso,…](https://ajuda.sankhya.com.br/hc/article_attachments/32399304266135) Na tela de **"Central de Vendas"**, no lançamento da NF-e, preencha o campo:  "**Cód. Parceiro Retirada**" que. nesse caso, será o mesmo do campo: "**Parceiro**";

![Imagem 4: Na tela de "Central de Vendas" , no lançamento da NF-e, preencha o campo: " Cód. Parceiro Retirada " que. nesse caso,…](https://ajuda.sankhya.com.br/hc/article_attachments/32400100458135)

**Observação:**se o campo Cód. Parceiro Retirada não estiver aparecendo na Central de Vendas, acesse a tela **"Configurador de Layout da Nota"** (Comercial » Configuração » Configurador de Layout da Nota), busque o campo e insira no layout da nota.

![Imagem 5: Observação: se o campo Cód. Parceiro Retirada não estiver aparecendo na Central de Vendas , acesse a tela "Configurador…](https://ajuda.sankhya.com.br/hc/article_attachments/32400104893719)

Após realizar o lançamento mencionado, **confirme que a Nota Fiscal gerada no XML inclui o grupo <retirada>**, contendo os dados do parceiro responsável pela retirada da mercadoria na empresa.
