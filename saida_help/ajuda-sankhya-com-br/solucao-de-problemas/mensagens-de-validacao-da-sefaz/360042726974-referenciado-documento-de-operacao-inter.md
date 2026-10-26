---
id: "360042726974"
titulo: "Referenciado documento de operação interna em operação interestadual ou com o exterior"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042726974-Referenciado-documento-de-opera%C3%A7%C3%A3o-interna-em-opera%C3%A7%C3%A3o-interestadual-ou-com-o-exterior"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:38Z"
rotulos: ["ERRONF", "#PUBLIFER", "Configuração", "Fiscal", "NF-e", "SEFAZ", "TOP", "923", "Rejeição por Referência a Documento Interno em Operação Interestadual", "Erro"]
---

# Referenciado documento de operação interna em operação interestadual ou com o exterior

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16512255482775) MENSAGEM:**

[923 - Rejeição]: Referenciado documento de operação interna em operação interestadual ou com o exterior.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16512230498199) SOLUÇÃO:**

- A nota de destino que está sendo rejeitada é uma nota de operação**FORA do Estado ou Exterior**, e a**nota que originou**essa nota trata-se de um Cupom Fiscal ou possui modelo de documento = 1 ou 2.
- Para solucionar essa rejeição primeiramente compreenda se a nota referenciada foi selecionada corretamente, em caso positivo, junto ao Contador reveja  o 'Modelo de Documento' utilizado.

(1)** Para correção siga os passos abaixo:**

![Imagem 3: Acesse a nota rejeitada através da " Central " (Caminho de acesso: Compras » Vendas » Mov.Interna ), na grade de itens…](https://ajuda.sankhya.com.br/hc/article_attachments/16512230500887) Acesse a nota rejeitada através da "**Central**" (Caminho de acesso: Compras » Vendas » Mov.Interna), na grade de itens » Outras Opções » Documentos Relacionados verifique o "**Documento de Origem**" vinculado:

![Imagem 4: Acesse a nota rejeitada através da " Central " (Caminho de acesso: Compras » Vendas » Mov.Interna ), na grade de itens…](https://ajuda.sankhya.com.br/hc/article_attachments/14612600095639)

![Imagem 5: Certifique que esse "Documento de Origem" é o correto, em caso negativo, inutilize/exclua a nota rejeitada e refaça o…](https://ajuda.sankhya.com.br/hc/article_attachments/16512230503703) Certifique que esse "Documento de Origem" é o correto, em caso negativo, inutilize/exclua a nota rejeitada e refaça o processo selecionando a nota correta.

![Imagem 6: Caso o "Documento de Origem" esteja correto, acesse o cadastro da TOP utilizada em seu lançamento e verifique os campos…](https://ajuda.sankhya.com.br/hc/article_attachments/16512230506775) Caso o "Documento de Origem" esteja correto, acesse o cadastro da TOP utilizada em seu lançamento e verifique os campos abaixo:

- Tela **"[Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** (Caminho de acesso: comercial » Arquivo » Cadastros) » **Aba** Livro Fiscal » Campo **"Modelo do Documento".**
- Tela Tipo de Operação - TOP (Caminho de acesso: Comercial » Arquivo » Cadastros) » **Aba** Geral » Campo **"TOP de Cupom Fiscal".**

Se Modelo do Documento = 1 ou 2 ou se a TOP de Cupom Fiscal = MARCADO, esse lançamento não será apropriado para ser referenciado em operações para fora do Estado/Exterior.

Lembre-se que caso trate-se de uma devolução de compra, sua **nota de COMPRA  origem deverá ser lançada com 'Modelo do Documento' = 55**. Caso tenha sido lançada com essa configuração na TOP = 01, essa poderá ser a causa da rejeição. Dessa forma, faça o ajuste na TOP, exclua os lançamentos atuais e lance a nota de compra novamente (caso trate-se de uma nota de terceiros), após isso refaça a devolução.

Dessa forma, selecione um documento válido e/ou corrija as configurações da TOP utilizada e refaça os respectivos lançamentos.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16512255497111) CAUSA:**

Se Informado Cupom Fiscal referenciado (tag: refECF) ou informado NF modelo 1 ou 2 referenciada (tag:refNF) em NFe de operação interestadual ou com o exterior (tag: idDest<>1), será apresentada a mensagem.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16512230511255) OBSERVAÇÃO:**

([NT2019/001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=RD1XRVxKLtI=)) - Nota técnica
