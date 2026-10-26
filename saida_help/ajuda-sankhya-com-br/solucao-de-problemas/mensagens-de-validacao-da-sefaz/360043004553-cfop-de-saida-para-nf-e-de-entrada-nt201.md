---
id: "360043004553"
titulo: "CFOP de saída para NF-e de entrada(NT2010/010)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004553-CFOP-de-sa%C3%ADda-para-NF-e-de-entrada-NT2010-010"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:10:21Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "XML", "SEFAZ", "TOP", "CFOP", "519", "Rejeição CFOP 519", "Ajuste CFOP na tela Tipo de Operação", "NF-e com CFOP de saída e tipo de operação de entrada"]
---

# CFOP de saída para NF-e de entrada(NT2010/010)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16455448450583) MENSAGEM:**

[519- Rejeição]: CFOP de saída para NF-e de entrada"

**![Imagem 2: SOLUÇÃO: Para correção, siga os passos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16455432085655) SOLUÇÃO:**
Para correção, siga os passos abaixo:

![Imagem 3: Acesse a tela: " Tipo de Operação " : (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)](https://ajuda.sankhya.com.br/hc/article_attachments/16455432092183) Acesse a tela: "**[Tipo de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"**: (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)

 Aba: "**Livro Fiscal"**

 - Campo "**Atualização de Livro ICMS"**: preencha com a respectiva finalidade da operação.

Campos:

- "**CFOP para FORA do Estado".**

- "**CFOP para DENTRO do Estado**".

![Imagem 4: Insira a CFOP correspondente a Natureza da Operação (preenchimento da tag <natOp>):](https://ajuda.sankhya.com.br/hc/article_attachments/16455448461719) Insira a CFOP correspondente a Natureza da Operação (preenchimento da tag <natOp>):

**(2)** Se Movimentação de Entrada, CFOP's que inicia com 1, 2 e 3.
**(2)** Se movimentação de Saída, CFOP's que inicia com 5, 6 e 7.

![Imagem 5: Preencha a informação de 'Atualização de Livro ICMS' dentro do XML a tag <tpNF>, onde 0 = Entrada e 1 = Saída. Dessa…](https://ajuda.sankhya.com.br/hc/article_attachments/16455448474647) Preencha a informação de 'Atualização de Livro ICMS' dentro do XML a tag <tpNF>, onde 0 = Entrada e 1 = Saída. Dessa forma, a SEFAZ realiza verificação da tag <tpNF> com <CFOP>.

![Imagem 6: Após os ajustes, faz-se necessário a inutilização de numeração e exclusão da nota para posterior lançamento de uma nova…](https://ajuda.sankhya.com.br/hc/article_attachments/16455432112535) Após os ajustes, faz-se necessário a inutilização de numeração e exclusão da nota para posterior lançamento de uma nova nota.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16455448486039) CAUSA:**

Quando for emitida uma NF-e com CFOP de Saída (iniciado por 5, 6 ou 7) e o Tipo de Operação da NF-e for igual a "0 - Entrada", ocorrerá a rejeição.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16455432119703) OBSERVAÇÃO:**

([**NT2010/010**](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=AtaVevRXCIQ=)) - Nota Técnica.
