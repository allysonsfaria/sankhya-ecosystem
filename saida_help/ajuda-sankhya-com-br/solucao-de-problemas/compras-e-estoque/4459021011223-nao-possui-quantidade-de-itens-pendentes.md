---
id: "4459021011223"
titulo: "Não possui quantidade de itens pendentes para devolução, verifique em 'Outras Opções' no menu 'Documentos Relacionados'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4459021011223-N%C3%A3o-possui-quantidade-de-itens-pendentes-para-devolu%C3%A7%C3%A3o-verifique-em-Outras-Op%C3%A7%C3%B5es-no-menu-Documentos-Relacionados"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T15:19:09Z"
rotulos: ["CORE_E04678", "NF-e", "Estoque", "Devolução", "CORE_E06695", "Documentos Relacionados", "Falha na Devolução por Quantidade Insuficiente", "Erro"]
---

# Não possui quantidade de itens pendentes para devolução, verifique em 'Outras Opções' no menu 'Documentos Relacionados'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16314913799703) MENSAGEM:**

[CORE\_E04678] Não possui quantidade de itens pendentes para devolução, verifique em 'Outras Opções' no menu 'Documentos Relacionados'.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16314913803287) CAUSA:**

Ocorre quando ao tentar realizar a devolução de uma nota que não exista quantidade suficiente em estoque dos itens a serem devolvidos ou não existir quantidade pendente suficiente para esse processo.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16314941975319) SOLUÇÃO:**

**![Imagem 4: Verifique se já existe uma devolução vinculada à essa nota:](https://ajuda.sankhya.com.br/hc/article_attachments/16315014730775) Verifique se já existe uma devolução vinculada à essa nota:**

**(1)** Selecione a nota a ser devolvida no portal, dê um duplo clique e abra a mesma na Central de Notas.

**(1)** Com a nota aberta, selecione um item e no botão Outras Opções (...) >> **Documentos Relacionados**marque a opção **"Todos os Itens"**.

**(1)** Verifique se em "Documento de Destino" existe algum documento vinculado:

![Imagem 5: (1) Verifique se em "Documento de Destino" existe algum documento vinculado:](https://ajuda.sankhya.com.br/hc/article_attachments/15775251170839)

**Veja que essa nota já foi devolvida, impedindo assim uma nova devolução!**

**(1)** Dê um duplo clique nesse documento, o mesmo será aberto;

**(1)** Verifique se trata de uma devolução com os itens/quantidades que você esta tentando devolver;

**(1)** Em caso positivo, não será possível devolver duas vezes os mesmos itens;

**(1)** Será necessário entender o processo e verificar se a nota de devolução localizada é a que precisa, não sendo necessário refazer a devolução;

**(1)** Caso não exista nota de devolução vinculada, o item 2 também poderá ser analisado.

**![Imagem 6: Verifique se existe estoque suficiente para os itens a serem devolvidos:](https://ajuda.sankhya.com.br/hc/article_attachments/16315042744855) Verifique se existe estoque suficiente para os itens a serem devolvidos:**

No processo padrão de uma devolução de compra, que em sua maioria atualiza estoque como entrada, para que sua devolução de compra ocorra é necessário que a atualização de estoque ocorra como saída.

**(1)** Dessa forma, se estiver, por exemplo, tentando devolver 4 UN do produto X, é preciso ter em estoque essas 4 UN;

**(1)** Se esse estoque não existe, seu controle de estoque precisa ser revisto, para que seja compreendido internamente motivos pelos quais não existe estoque de um produto que será devolvido ao fornecedor;

**(1)** Após ajuste desse estoque, tente novamente realizar a devolução.
