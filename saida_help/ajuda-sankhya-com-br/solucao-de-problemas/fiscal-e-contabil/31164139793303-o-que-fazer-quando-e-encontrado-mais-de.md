---
id: "31164139793303"
titulo: "O que fazer quando é encontrado mais de um parceiro com CNPJ ou CPF igual ao da empresa na busca da equivalência dos produtos?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31164139793303-O-que-fazer-quando-%C3%A9-encontrado-mais-de-um-parceiro-com-CNPJ-ou-CPF-igual-ao-da-empresa-na-busca-da-equival%C3%AAncia-dos-produtos"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:33:35Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "NF-e", "XML", "Importação", "Passos para resolver", "Razão do erro", "Detalhe do erro", "mais de um parceiro", "CNPJ ou CPF igual ao da empresa"]
---

# O que fazer quando é encontrado mais de um parceiro com CNPJ ou CPF igual ao da empresa na busca da equivalência dos produtos?

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31164157633559) **MENSAGEM:**

Foi encontrado mais de um parceiro com o mesmo CNPJ ou CPF igual ao da empresa, para buscar a equivalência dos produtos.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31164157634839)SOLUÇÃO:**

Na tela **"Portal de Importação de XML"**, clique no botão **"Outras opções"**, em seguida, selecione **"Preferência para importação de NF-e de Emissão Própria".**No pop up que irá abrir, marque o campo **"Considera Inscrição Estadual para seleção do parceiro da importação"**

![Imagem 3: Na tela "Portal de Importação de XML" , clique no botão "Outras opções" , em seguida, selecione "Preferência para…](https://ajuda.sankhya.com.br/hc/article_attachments/31929829708311)

Feito isso, clique em salvar e processe o arquivo novamente.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31164157635863)CAUSA:**

Problema acontece porque existe mais de um cadastro de parceiro e/ou empresa na base de dados com o mesmo CNPJ ou CPF e o sistema não consegue distinguir qual código a ser considerado para defini-lo na importação do arquivo.
