---
id: "360045039434"
titulo: "318 - Rejeição: Contranota de Produtor sem Nota Fiscal referenciada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045039434-318-Rejei%C3%A7%C3%A3o-Contranota-de-Produtor-sem-Nota-Fiscal-referenciada"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:33:18Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "XML", "SEFAZ", "TOP", "Erro"]
---

# 318 - Rejeição: Contranota de Produtor sem Nota Fiscal referenciada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18603591807895) MENSAGEM:**

Rejeição 318: Contranota de Produtor sem Nota Fiscal referenciada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18603626990487) SOLUÇÃO:**

![Imagem 3: Para lançamento da Contranota, a nota de origem deverá ser selecionada no respectivo 'Portal' e através do botão…](https://ajuda.sankhya.com.br/hc/article_attachments/18603591815191) Para lançamento da Contranota, a nota de origem deverá ser selecionada no respectivo 'Portal' e através do botão 'Devolver' selecionada a TOP para essa emissão. É essencial que o 'Tipo de Operação' utilizado obedeça a configuração abaixo:

- Tela 'Tipos de Operação - TOP' (Comercial » Arquivo » Cadastros)
  Aba 'NF-e/NFC-e'
  Campo '**Buscar NF de origem p/ referenciar na NFe**'

Após marcação acima, inutilize/exclua a nota rejeitada e realize o processo de "devolução" novamente.

**Importante:**

Para emissão de contranota, a SEFAZ identifica a tag <tpNF>, cujo 0 corresponde a Entrada e 1 Saída. Deste modo, para correta geração da **tag <refNFP>** - Informações da NF de produtor rural referenciada, seguir as orientações abaixo no que refere-se ao lançamento da **nota de ORIGEM**:

Tela 'Tipos de Operação - TOP' (Comercial » Arquivo » Cadastros)

O lançamento da nota de produtor rural no sistema deverá ser realizada utilizando um 'Tipo de Operação' que obedeça as seguintes configurações:

Aba Geral:

- Tipo de Movimento = C-Compra
- TOP p/Devolução = [Informar a TOP que será usada para geração da NFe própria

Aba NF-e/NFC-e:

- 'Modelo do Documento' = 04-Nota Fiscal de Produtor
- NF-e = Convencional (Não Usa NF-e

Aba Impressão:

- Base numeração = Manual (Informada pelo Usuário)

![Imagem 4: Confira as configurações mencionadas, a nota do Produtor Rural deverá ser lançada no sistema, atente-se ao…](https://ajuda.sankhya.com.br/hc/article_attachments/18603626994583) Confira as configurações mencionadas, a nota do Produtor Rural deverá ser lançada no sistema, atente-se ao preenchimento dos campos abaixo:

- Número da Nota
- Série da Nota
- Data de emissão dessa nota

Estes dados são importantes para correta geração da tag **<refNFP>** na nota própria.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18603626996887) CAUSA:**

A mensagem será apresentada quando emitida uma Contranota de Produtor sem Nota Fiscal referenciada:
- não informada NF de Produtor referenciada (tag:refNFP);
- e não informada Nota Fiscal referenciada (tag:refNFe).

**Observação 1:**
A Contranota de Produtor é identificada como uma Nota Fiscal de entrada (tag:tpNF=0) e remetente da mesma UF com IE de Produtor Rural.
**Observação 2:**
A utilização e controle da Contranota de Produtor é opcional, a critério da UF.

**Observações:**

Nota Técnica 2015.002 - v 1.40

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=yldA7bYcnVg=>
