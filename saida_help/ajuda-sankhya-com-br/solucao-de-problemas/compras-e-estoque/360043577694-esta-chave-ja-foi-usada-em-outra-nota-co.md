---
id: "360043577694"
titulo: "Esta chave já foi usada em outra nota com a mesma empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043577694-Esta-chave-j%C3%A1-foi-usada-em-outra-nota-com-a-mesma-empresa"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:01:54Z"
rotulos: ["DUVIDANF", "Portal de Compras", "NF-e", "XML", "Importação", "CORE_E01792", "Correção de Duplicatas", "Chave de Nota Fiscal", "Erro"]
---

# Esta chave já foi usada em outra nota com a mesma empresa

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16168848691351) MENSAGEM**:

[CORE\_E01792] Esta chave já foi usada em outra nota com a mesma empresa.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16168858242711) SOLUÇÃO**:

Para correção, siga os passos abaixo:

![Imagem 3: Acesse o " Portal de Compras " (Caminho de acesso: Comercial » Consulta » Portal de Compras).](https://ajuda.sankhya.com.br/hc/article_attachments/16168858247959) Acesse o **"[Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953)"** (Caminho de acesso: Comercial » Consulta » Portal de Compras).

![Imagem 4: Como sugestão, crie um filtro para pesquisar pela Chave da Nota:](https://ajuda.sankhya.com.br/hc/article_attachments/16168848695191) Como sugestão, crie um filtro para pesquisar pela Chave da Nota:

![Imagem 5: Como sugestão, crie um filtro para pesquisar pela Chave da Nota:](https://ajuda.sankhya.com.br/hc/article_attachments/14706658492695)

![Imagem 6: Como sugestão, crie um filtro para pesquisar pela Chave da Nota:](https://ajuda.sankhya.com.br/hc/article_attachments/12236270556183)

(1)** EXEMPLO:** 

CabecalhoNota.CHAVENFE = ?:{entidade=CabecalhoNota;campo=CHAVENFE}

![Imagem 7: Digite a chave e efetue a pesquisa, desta forma será encontrado a nota já importada.](https://ajuda.sankhya.com.br/hc/article_attachments/16168848699927) Digite a chave e efetue a pesquisa, desta forma será encontrado a nota já importada.

![Imagem 8: Com isso poderá escolher excluir e importar novamente ou apenas conferir a nota já importada.](https://ajuda.sankhya.com.br/hc/article_attachments/16168848701591) Com isso poderá escolher excluir e importar novamente ou apenas conferir a nota já importada.

**![Imagem 9: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16168848703255) CAUSA**:

Ocorre quando o XML da Nota de Compra já foi importado anteriormente, talvez por outro usuário.
