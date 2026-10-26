---
id: "26747322831255"
titulo: "CT-e ou NF-e não está sendo gerado nos livros fiscais (tela: Cadastro Livro ICMS/IPI)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26747322831255-CT-e-ou-NF-e-n%C3%A3o-est%C3%A1-sendo-gerado-nos-livros-fiscais-tela-Cadastro-Livro-ICMS-IPI"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:40:45Z"
rotulos: ["CT-e", "Configuração", "Fiscal", "NF-e", "TOP", "CT-e ou NF-e não está sendo gerado nos livros fiscais", "tela: Cadastro Livro ICMS/IPI", "Documentos Eletrônicos"]
---

# CT-e ou NF-e não está sendo gerado nos livros fiscais (tela: Cadastro Livro ICMS/IPI)

**![Imagem 1: SITUAÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/26891091589655) SITUAÇÃO**

Durante a geração dos livros fiscais, pode ocorrer o problema em que o CT-e ou NF-e não são gerados, deixando dúvidas sobre os motivos que levam a este cenário. Confira abaixo as configurações que podem causar este problema.

Quando é lançado um documento no sistema, principalmente documentos de entrada, não se pode configurar na TOP usada para no lançamento, informações contradizentes, ou seja, não pode haver configurações em uma mesma TOP para "NF-e" e, ao mesmo tempo, "CT-e".

Exemplo de configuração errada, ao configurar uma TOP **modelo 57** - CT-e.

![Imagem 2: Exemplo de configuração errada, ao configurar uma TOP modelo 57 - CT-e.](https://ajuda.sankhya.com.br/hc/article_attachments/26891106337175)

O mesmo vale para TOP'S **modelo 55,** em que na aba **"CT-e / MD-e",** o campo **"CT-e"** deve estar como **"convencional - não usa".**

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26891331434135)SOLUÇÃO:**

Se na TOP usada na operação existirem as configurações supracitadas, de fato o documento não será gerado nos livros. Assim, será preciso fazer a alteração na configuração da TOP e realizar um novo lançamento dos documentos com problema.
