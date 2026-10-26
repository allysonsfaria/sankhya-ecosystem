---
id: "12073041629719"
titulo: "NFS-e por Natureza"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/12073041629719-NFS-e-por-Natureza"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > NFS-e"
atualizado_em: "2026-09-15T17:00:12Z"
rotulos: ["Configuração", "Impostos", "Natureza de Receitas e Despesas", "TOP", "Construtor de Telas", "Natureza", "NFS-e por Natureza", "tela detalhe", "ID: br.com.sankhya.com.cad.tipooperacao", "Prefeituras", "NFS-e", "Campos: CODEMP CODNAT CODLST CNAE CODTRIBMUNISS CODNBS.", "Crie tela adicional para configuração de NFS-e por Natureza", "Configure e vincule nova tela ao cadastro de Natureza de Receitas e Despesas"]
---

# NFS-e por Natureza

Quando o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) da NFS-e estiver configurado por Natureza é necessário a criação de uma tela adicional para que o sistema pegue as configurações de CNAE, sendo elas o **"Cód.Trib.Mun. ISS"** e o **"Código da Lista de Serviços"**.

Esta tela será criada pelo [Construtor de telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773) do Sankhya Om, do tipo [Tela detalhe](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#teladetalhe) tendo como tela mestre, o cadastro de [Natureza de Receitas/Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774) que, terá uma nova aba, com a descrição da tela que foi criada (sugere-se para esta aba o nome **"NFS-e"**).

Os campos para esta tela deverão ser criados conforme abaixo:

- CODEMP - Deve ser importado da tabela TSIEMP;
- CODNAT - Que será criado automaticamente, visto que a tela mestre é TGFNAT;
- CODLST - Deve ser importado da tabela TGFLST;
- CNAE - Número inteiro;
- CODTRIBMUNISS - Tipo texto;
- CODNBS - Número inteiro.

Os outros atributos de campos devem ser deixados com o valor padrão.

Feitas estas configurações, na tela Natureza de Receitas e Despesas acesse a aba**"NFS-e"**, onde deverá ser informado por **"Empresa"**, o CNAE e os demais campos necessários para a prefeitura em questão.

Segue abaixo um exemplo de criação da tela para melhor entendimento:

Primeiramente, realize a formação da tela adicional, sendo esta uma tela do tipo Tela detalhe tendo como tela mestre a tela de cadastro de Natureza de Receitas e Despesas(tabela TGFNAT):

![Imagem 1: Primeiramente, realize a formação da tela adicional, sendo esta uma tela do tipo Tela detalhe tendo como tela mestre a…](https://ajuda.sankhya.com.br/hc/article_attachments/12074024474647)

Em seguida, informe os dados referentes a mesma:

![Imagem 2: Em seguida, informe os dados referentes a mesma:](https://ajuda.sankhya.com.br/hc/article_attachments/12074095618199)

Depois, efetue a criação dos campos pertinentes:

![Imagem 3: Depois, efetue a criação dos campos pertinentes:](https://ajuda.sankhya.com.br/hc/article_attachments/12074071430039)

E verifique a correta inclusão dos mesmos:

![Imagem 4: E verifique a correta inclusão dos mesmos:](https://ajuda.sankhya.com.br/hc/article_attachments/12074135931031)

Agora, vincule a nova tela com os demais cadastros. Neste exemplo, foi criada a ligação entre o campo **"Empresa"** com a tabela TSIEMP e o campo **"Cód. Lista Serviço"** com a tabela TGFLST:

![Imagem 5: Agora, vincule a nova tela com os demais cadastros. Neste exemplo, foi criada a ligação entre o campo "Empresa" com a…](https://ajuda.sankhya.com.br/hc/article_attachments/12074147095959)

Por fim, acesse o cadastro de Natureza de Receitas e Despesas para verificar a conclusão da aba **"NFS-e"**:

![Imagem 6: Por fim, acesse o cadastro de Natureza de Receitas e Despesas para verificar a conclusão da aba "NFS-e" :](https://ajuda.sankhya.com.br/hc/article_attachments/12074149249943)

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/12073041629719-NFS-e-por-Natureza#top)
