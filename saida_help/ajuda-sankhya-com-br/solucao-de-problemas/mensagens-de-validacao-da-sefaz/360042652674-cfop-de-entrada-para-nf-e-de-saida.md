---
id: "360042652674"
titulo: "CFOP de entrada para NF-e de saída"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042652674-CFOP-de-entrada-para-NF-e-de-sa%C3%ADda"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-10-19T18:27:16Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "CFOP", "518", "CFOP entrada incorreto", "Tipo operação NF-e incompatível", "Ajustar CFOP na TOP"]
---

# CFOP de entrada para NF-e de saída

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16486055709207) MENSAGEM:**

[518 - Rejeição]: CFOP de entrada para NF-e de saída.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16486055710487) SOLUÇÃO:**

![Imagem 3: Acesse "Tipos de Operação - TOP" (Caminho de acesso: Comercial » Arquivo » Cadastros)](https://ajuda.sankhya.com.br/hc/article_attachments/16486097993751) Acesse **"Tipos de Operação - TOP"** (Caminho de acesso: Comercial » Arquivo » Cadastros)

![Imagem 4: Na aba "Livro Fiscal" , verifique as configurações abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16486097995543) Na aba **"Livro Fiscal"**, verifique as configurações abaixo:

- Campo **"Atualização de Livro ICMS":** deve ser preenchido com a respectiva finalidade da operação.
- CFOP para FORA do Estado.
- CFOP para DENTRO do Estado.

Insira a CFOP correspondente à Natureza da Operação (preenchimento da tag <natOp>):

- Se Movimentação de **Entrada**, CFOP's que iniciam com **1, 2 e 3**.
- Se Movimentação de **Saída**, CFOP's que iniciam com **5, 6 e 7**.

![Imagem 5: Após os ajustes, inutilize a numeração, exclua a nota e depois lance uma nova nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16486097996439) Após os ajustes, inutilize a numeração, exclua a nota e depois lance uma nova nota.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16486098000023) CAUSA:**

Quando for emitida uma NF-e com CFOP de Entrada (iniciado por 1, 2 ou 3) e o Tipo de Operação da NF-e for igual a "1 - Saída", ocorrerá a rejeição.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16486055726615) OBSERVAÇÃO:**

([NT2010/10](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=AtaVevRXCIQ=)) - Nota Técnica
