---
id: "360042578834"
titulo: "NF-e de devolução de mercadoria não possui documento fiscal referenciado.(NT2013/005)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042578834-NF-e-de-devolu%C3%A7%C3%A3o-de-mercadoria-n%C3%A3o-possui-documento-fiscal-referenciado-NT2013-005"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:07Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "TOP", "Devolução", "321", "Rejeição 321: NF-e de Devolução Sem Documento Referenciado", "Documentos Eletrônicos"]
---

# NF-e de devolução de mercadoria não possui documento fiscal referenciado.(NT2013/005)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16474865677719) MENSAGEM:**

[321 - Rejeição]: NF-e de devolução de mercadoria não possui documento fiscal referenciado.(NT2013/005).

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16474893523735) SITUAÇÃO:**

Ao realizar emissão de NF-e pela tela Central de Vendas no SankhyaW.

Acessando a opção (...)>>Ver Acompanhamento, é possível consultar o detalhe da Rejeição a seguir:

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16474865686039) SOLUÇÃO:**

Para 'Devolução de Compra' ou 'Devolução de Venda' de emissão própria:

![Imagem 4: Acesse: a tela "Tipos de Operação - TOP" (Caminho de acesso: Comercial » Arquivo » Cadastros ) » aba: " NF-e/NFC-e" :](https://ajuda.sankhya.com.br/hc/article_attachments/16474893530135) Acesse: a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) (Caminho de acesso: Comercial » Arquivo » Cadastros) » aba: "**NF-e/NFC-e"**:

- Campo **"Buscar NF de Origem p/ Referenciar na NF-e":**marque

![Imagem 5: Caso a marcação acima não tenha sido realizada, inutilize a numeração da devolução rejeitada, exclua. Realize a…](https://ajuda.sankhya.com.br/hc/article_attachments/16474893532823) Caso a marcação acima não tenha sido realizada, inutilize a numeração da devolução rejeitada, exclua. Realize a marcação da TOP e refaça o processo de devolução seguindo as orientações do próximo passo.

![Imagem 6: Selecione a NF-e de Origem(Venda/Compra), clique no botão "Devolv./Estor." , selecione os produtos que serão devolvidos…](https://ajuda.sankhya.com.br/hc/article_attachments/16474893537431) Selecione a NF-e de Origem(Venda/Compra), clique no botão **"Devolv./Estor."**, selecione os produtos que serão devolvidos ou toda a nota.

Desta forma, o sistema irá preencher na Nota o 'Grupo de Documentos Referenciados', que significa os dados na nota de origem (Chave NFe <refNFe>).

**Lançamento "Avulso/Manual":**

Caso não possua a nota de origem lançada no sistema, é necessário possuir a chave NF-e referente a mesma e seguir as orientações abaixo:

![Imagem 7: No configurador de layout da nota, para o respectivo tipo de movimento da nota de devolução, insira o campo "Chave NF-e…](https://ajuda.sankhya.com.br/hc/article_attachments/16474865694487) No configurador de layout da nota, para o respectivo tipo de movimento da nota de devolução, insira o campo **"Chave NF-e referenciada"**:

![Imagem 8: No configurador de layout da nota, para o respectivo tipo de movimento da nota de devolução, insira o campo "Chave NF-e…](https://ajuda.sankhya.com.br/hc/article_attachments/14500887416727)

![Imagem 9: Inserido o campo, ao realizar o lançamento da devolução é essencial que esse campo seja devidamente preenchido com a…](https://ajuda.sankhya.com.br/hc/article_attachments/16474865696407) Inserido o campo, ao realizar o lançamento da devolução é essencial que esse campo seja devidamente preenchido com a informação referente chave da NF-e de origem.

![Imagem 10: Confirme a NF-e gerada.](https://ajuda.sankhya.com.br/hc/article_attachments/16474893551127) Confirme a NF-e gerada.

Para os casos nos quais a nota de origem esteja lançada no sistema e a ligação será feita manualmente:

- Acesse no cabeçalho da nota a opção: (...)>>"**Ligar a Devolução com Notas"**, esta opção liga a Devolução com uma Nota de Origem mais recente.

**ou**

- Digite os itens que estão sendo devolvidos na grade de Itens e, posteriormente, ligue a nota de Origem na opção (...) da grade de Itens >>"**Documentos Relacionados"**. Clique para Incluir(+) e informar o "**Número Único"**, "**Sequência do Item"** e "**Quantidade Atendida"**, todos obrigatórios. Estas informações deverão ser devidamente anotadas antes da nota de origem, para a correta ligação entre a Devolução com a Nota de Origem (compra/venda).

![Imagem 11: Após o lançamento gere um novo lote da nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16474865703063) Após o lançamento gere um novo lote da nota.

**![Imagem 12: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16474893555095) CAUSA:**

Quando for emitida uma NF-e com finalidade igual à "4 - Devolução de mercadoria" e não for informado documento referenciado  que está sendo devolvido, será retornado a rejeição.

**![Imagem 13: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16474893557271) OBSERVAÇÕES:**

**(2)** ([NT2013/005](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=jLEf0c3bSBI=)) - Nota Técnica.

**(2)** **Parâmetros**:

**"TOPCONSIGC-TOP para consignação de compra"**

Altera a descrição da Opção: 'Ligar a Devolução com Notas' para 'Ligar a Devolução com Notas de Consignação' 

**(2)** Quando se tratar de uma devolução onde a Nota de Origem não é NF-e e não possui informações desta no sistema, use o campo "**ChaveNFeRef"** na nota de devolução para que seja gerado a devida tag, conforme abaixo:

`<``NFref``>`

`<``refNFe``>99999999999999999999999999999999999999999999</``refNFe``>`

`</``NFref``>`
