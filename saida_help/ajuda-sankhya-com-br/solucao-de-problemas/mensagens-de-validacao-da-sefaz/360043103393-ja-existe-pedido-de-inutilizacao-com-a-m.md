---
id: "360043103393"
titulo: "Já existe pedido de Inutilização com a mesma faixa de inutilização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043103393-J%C3%A1-existe-pedido-de-Inutiliza%C3%A7%C3%A3o-com-a-mesma-faixa-de-inutiliza%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:15Z"
rotulos: ["ERRONF", "NF-e", "SEFAZ", "563", "Rejeição por Faixa de Inutilização Duplicada", "Detalhe do erro", "Erro", "Documentos Eletrônicos"]
---

# Já existe pedido de Inutilização com a mesma faixa de inutilização

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16447631308951) MENSAGEM:**

[563-Rejeição]: Já existe pedido de Inutilização com a mesma faixa de inutilização.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16447624246167) SOLUÇÃO:**

**(2)** Considere o comportamento da aplicação, conforme abaixo:

**(2)** No sistema não há nenhuma orientação, configuração a ser feita.

**(2)** Aguarde que a Sefaz retorne a situação do processamento do primeiro envio da Inutilização. Se passado muito tempo e a Sefaz não retornar a situação do registro, acione a mesma para verificação.

[Consulta Inutilização](http://www.nfe.fazenda.gov.br/POrtal/consulta.aspx?tipoConsulta=inutilizacao&tipoConteudo=YG1QjUXR4PY=)

![Imagem 3: Consulta Inutilização](https://ajuda.sankhya.com.br/hc/article_attachments/14340516800791)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16447631319191) CAUSA:**

Quando for realizado um novo registro de Inutilização para uma mesmo CNPJ Emitente, Modelo, Série, Números Inicial e Final que já tenha sido registrado, mas ainda está em processamento pela Sefaz, será retornado a rejeição "563 - Já existe pedido de Inutilização com a mesma faixa de inutilização".

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16447624254487)OBSERVAÇÃO:**

[Manual de Orientação do Contribuinte](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=9hd38oni4Nc=http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=uvfnqOj%20spg=)
