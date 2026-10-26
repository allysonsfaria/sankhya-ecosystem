---
id: "4414497502103"
titulo: "Configurações para a realização de Baixa de Bens "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4414497502103-Configura%C3%A7%C3%B5es-para-a-realiza%C3%A7%C3%A3o-de-Baixa-de-Bens"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-09-08T18:33:28Z"
rotulos: ["Produtos", "Configuração", "Portal de Vendas", "TOP", "Estoque", "Configure TOP: Baixa/Venda", "Lance nota no Portal de Vendas", "Atualize depreciação do bem", "Controle Patrimonial"]
---

# Configurações para a realização de Baixa de Bens 

Confira as configurações necessárias para que o sistema proceda com a baixa de um bem no Controle Patrimonial da empresa.

Para que o sistema realize a baixa do bem, é necessário que exista uma TOP configurada para essa baixa, de forma que na aba **"Estoque"**,  no campo **"Atualização do Bem"** esteja como **"Baixa/Venda":**

![Imagem 1: Para que o sistema realize a baixa do bem, é necessário que exista uma TOP configurada para essa baixa, de forma que na…](https://ajuda.sankhya.com.br/hc/article_attachments/15745076134935)

**Observação:**

As demais configurações na TOP, como por exemplo a Atualização de Livro Fiscal e Emissão de NF-e ficarão a cargo de cada empresa, levando em consideração seus processos.

Em seguida, será necessário realizar o lançamento de uma nota no Portal de Vendas, informando a TOP configurada para a baixa e o bem a ser baixado.

Na grade de itens da nota, ao clicar em salvar, o sistema irá abrir a caixa 'Baixa de Bens', onde o usuário deverá vincular o código do bem a ser baixado:

![Imagem 2: Na grade de itens da nota, ao clicar em salvar, o sistema irá abrir a caixa 'Baixa de Bens', onde o usuário deverá…](https://ajuda.sankhya.com.br/hc/article_attachments/4414485476247)

Depois de confirmar a nota lançada, o sistema irá preencher os dados da baixa (Número da NF e Data de Baixa) dentro do cadastro do bem. tela Configurações » Cadastros » Produtos » Produtos', aba bens, sub-aba **"Bens".**

![Imagem 3: Depois de confirmar a nota lançada, o sistema irá preencher os dados da baixa (Número da NF e Data de Baixa) dentro do…](https://ajuda.sankhya.com.br/hc/article_attachments/15745080534807)

Em relação ao saldo de depreciação do bem que acabou de ser baixado, caso exista saldo a depreciar, o sistema irá calcular a diferença entre o total da depreciação do bem e a parte já depreciada no **SankhyaOm** e gravar este valor na tabela TCIMOV para que seja usado na contabilização da baixa do bem. Tela Imobilizado » Rotinas » Geração de Lote de Depreciação.
