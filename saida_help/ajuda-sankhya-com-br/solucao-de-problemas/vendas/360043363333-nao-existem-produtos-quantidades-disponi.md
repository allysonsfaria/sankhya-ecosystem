---
id: "360043363333"
titulo: "Não existem produtos/quantidades disponíveis para essa operação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043363333-N%C3%A3o-existem-produtos-quantidades-dispon%C3%ADveis-para-essa-opera%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-20T14:55:59Z"
rotulos: ["CORE_E04678", "Produtos", "NF-e", "Estoque", "Financeiro", "Verifique estoque disponível", "Confirme notas de destino vinculadas", "Cheque cortes que impedem faturamento", "Erro"]
---

# Não existem produtos/quantidades disponíveis para essa operação

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16115160583447) MENSAGEM:**

[CORE\_E04678] Não existem produtos/quantidades disponíveis para essa operação.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16115176057367) SOLUÇÃO:**

**![Imagem 3: Verifique se existe estoque suficiente para os itens a serem faturados/devolvidos:](https://ajuda.sankhya.com.br/hc/article_attachments/16115160593047) Verifique se existe estoque suficiente para os itens a serem faturados/devolvidos:**

**(2)** No processo padrão de uma devolução de compra, que em sua maioria atualiza estoque como entrada, para que sua devolução de compra ocorra é necessário que a atualização de estoque ocorra como saída;

**(2)** Dessa forma, se está, por exemplo, tentando devolver 4 UN do produto X, é necessário ter em estoque essas 4 UN;

**(2)** Se esse estoque não existe, seu controle de estoque precisa ser revisto, para que seja compreendido internamente motivos pelos quais não existe estoque de um produto que será devolvido ao fornecedor;

**(2)** Após ajuste desse estoque, tente novamente realizar a devolução.

**![Imagem 4: Verifique se já existe uma nota de destino vinculada à essa nota:](https://ajuda.sankhya.com.br/hc/article_attachments/16115160598039) Verifique se já existe uma nota de destino vinculada à essa nota:**

**(2)**Selecione a nota a ser faturada/devolvida no portal, dê um duplo clique e abra a mesma na Central de Notas;

**(2)** Com a nota aberta, selecione um item e no botão **"Outras Opções (...)"** » "**Documentos Relacionados"** marque a opção **"Todos os Itens"**;

**(2)** Verifique se em **"Documento de Destino"** existe algum documento vinculado.

**(2)** Dê um duplo clique nesse documento, o mesmo será aberto;

**(2)** Verifique se trata-se de uma nota com os itens/quantidades que você está tentando devolver/faturar;

**(2)** Em caso positivo, não será possível devolver/faturar duas vezes os mesmos itens.

**(2)** Será necessário entender o processo e verificar se a nota localizada é a que você necessita, não sendo necessário refazê-la.

**![Imagem 5: Outra análise a ser considerada é se foi realizado 'Corte' que impeça esse faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16115176067735) Outra análise a ser considerada é se foi realizado 'Corte' que impeça esse faturamento.**

No exemplo abaixo para um pedido com Qtde= 510 já havia sido feito o Corte de 510, não permitindo assim o faturamento. Nesse caso, entenda o processo e, se necessário, **Limpar o Corte:**

![Imagem 6: No exemplo abaixo para um pedido com Qtde= 510 já havia sido feito o Corte de 510, não permitindo assim o faturamento.…](https://ajuda.sankhya.com.br/hc/article_attachments/14599386670743)

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16115176070039) CAUSA:**

Ocorre quando ao tentar realizar o faturamento/devolução de uma nota que não exista quantidade suficiente em estoque dos itens ou não existir quantidade pendente suficiente para esse processo.
