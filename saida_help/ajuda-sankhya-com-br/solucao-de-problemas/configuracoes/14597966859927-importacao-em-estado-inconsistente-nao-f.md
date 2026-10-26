---
id: "14597966859927"
titulo: "Importação em estado inconsistente. Não foi possível carregar os produtos vinculados para o produto \"xxxxxxx\", unidade \"MIL\", referência \"SEM GTIN\" da empresa \"xxx\". Por favor, tente reimportar novamente o XML"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14597966859927-Importa%C3%A7%C3%A3o-em-estado-inconsistente-N%C3%A3o-foi-poss%C3%ADvel-carregar-os-produtos-vinculados-para-o-produto-xxxxxxx-unidade-MIL-refer%C3%AAncia-SEM-GTIN-da-empresa-xxx-Por-favor-tente-reimportar-novamente-o-XML"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:58:24Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "Parceiro", "XML", "Importação", "Problema na Importação de Produtos"]
---

# Importação em estado inconsistente. Não foi possível carregar os produtos vinculados para o produto "xxxxxxx", unidade "MIL", referência "SEM GTIN" da empresa "xxx". Por favor, tente reimportar novamente o XML

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16842157367959) MENSAGEM:**

"Erro interno: importação em estado inconsistente. Não foi possível carregar os produtos vinculados para o produto "xxxxxxx", unidade "MIL", referência "SEM GTIN" da empresa "xxx". Por favor, tente reimportar novamente o XML."

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16842199534871)SOLUÇÃO:**

![Imagem 3: Acesse a tela Parceiros - Configurações » Cadastros » Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/16842157375895) Acesse a tela **Parceiros** -Configurações » Cadastros » Parceiros

Aba: "**Fiscal**"

Campo: **"Unidade para considerar na importação"**

- Unidade Comercial
- Unidade Tributável

Caso o campo esteja diferente de **"Unidade Comercial",** o sistema não consegue identificar o produto.

Para o uso da rotina no sistema, configure o campo **"Unidade"** para considerar na importação:" Flegado para trabalhar com **"Unidade Comercial"** no cadastro do Parceiro, dessa forma, o sistema realiza a validação da importação sem apresentar a mensagem de erro.

 
![Imagem 4: Para o uso da rotina no sistema, configure o campo "Unidade" para considerar na importação:" Flegado para trabalhar com…](https://ajuda.sankhya.com.br/hc/article_attachments/14605483800087)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16842157378711)CAUSA:**

Ao clicar em **"Validar Importação"** após ter atribuídos os produtos na aba **"Produtos Por Parceiro"** na tela **"Portal de Importação de XML"** com a configuração do cadastro do Parceiro diferente de  Unidade Comercial.
