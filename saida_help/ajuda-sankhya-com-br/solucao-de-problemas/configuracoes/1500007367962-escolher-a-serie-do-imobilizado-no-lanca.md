---
id: "1500007367962"
titulo: "Escolher a série do imobilizado no lançamento da Ordem de Serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007367962-Escolher-a-s%C3%A9rie-do-imobilizado-no-lan%C3%A7amento-da-Ordem-de-Servi%C3%A7o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:24:53Z"
rotulos: ["Configuração", "Contrato", "Imobilizado", "Ordem de Serviço", "Estoque", "não apagar", "Processo para Selecionar a Série do Imobilizado na Ordem de Serviço"]
---

# Escolher a série do imobilizado no lançamento da Ordem de Serviço

Confira abaixo o passo a passo para escolher a série do imobilizado no lançamento da Ordem de Serviço (lembrando que série não é o controle de estoque por serie (TGFSER) e sim o código da série informada no contrato):

![Imagem 1: Ligue os parâmetros " HABMULTSERCONT" e " SERVIMOBILI" ;](https://ajuda.sankhya.com.br/hc/article_attachments/16913684154135) Ligue os parâmetros **"HABMULTSERCONT"** e **"SERVIMOBILI"**;

![Imagem 2: Tendo realizado a nota de compra comum de um bem imobilizado, não informe nesse momento a série;](https://ajuda.sankhya.com.br/hc/article_attachments/16913700200855) Tendo realizado a nota de compra comum de um bem imobilizado, não informe nesse momento a série;

![Imagem 3: Em seguida, crie um contrato, mas não informe o produto, ele será inserido quando vincular a nota de remessa ao…](https://ajuda.sankhya.com.br/hc/article_attachments/16913684157719) Em seguida, crie um contrato, mas não informe o produto, ele será inserido quando vincular a nota de remessa ao contrato;

![Imagem 4: No "Cadastro de naturezas" , aba "Serviços autorizados" , adicione os serviços que serão usados no lançamento da Ordem…](https://ajuda.sankhya.com.br/hc/article_attachments/16913700203287) No **"Cadastro de naturezas"**, aba **"Serviços autorizados"**, adicione os serviços que serão usados no lançamento da Ordem de serviço;

![Imagem 5: Faça o lançamento da nota de remessa para o produto imobilizado com as configurações da top abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16913684159767) Faça o lançamento da nota de remessa para o produto imobilizado com as configurações da top abaixo:

**(1)** TOP de Venda, da baixa no estoque: XXX
**(1)** Atualiza imobilizado como Transf. Remessa
**(1)** **"Informar Contrato na Nota":** Obrigatório
(1)**"Integ. Série ao Contrato":** Entrada

**(1)Nota de vendas de Nro Unico:** XXX

**(2)** Empresa X

**(2)** Parceiro XX

**(2)** Contrato: XXXX

**(2)** TOP: XXX

**(1)** **Produto XX:** Qtd 2

Nesta nota, clique no botão **"Outras opções",** existente na grade de itens da nota, e escolha a opção: **"Transferência de bens"** para escolher os bens que farão parte do contrato, depois confirme a nota.

![Imagem 6: No cadastro do contrato XXXX utilize a opção "Selecionar produtos/serviços do pedido" existente no botão Outras opções…](https://ajuda.sankhya.com.br/hc/article_attachments/16913684161687) No cadastro do contrato XXXX utilize a opção **"Selecionar produtos/serviços do pedido"** existente no botão Outras opções. Escolha a nota de remessa lançada anteriormente e o produto informado nesta nota e clique no botão **"Confirmar"**.

![Imagem 7: No cadastro do contrato XXXX utilize a opção "Selecionar produtos/serviços do pedido" existente no botão Outras opções…](https://ajuda.sankhya.com.br/hc/article_attachments/16913684165143) Acesse o lançamento da ordem de serviço escolhendo o parceiro, contrato, produto e serviço definidos nos passos anteriores e escolha o executante e a a série do produto.
