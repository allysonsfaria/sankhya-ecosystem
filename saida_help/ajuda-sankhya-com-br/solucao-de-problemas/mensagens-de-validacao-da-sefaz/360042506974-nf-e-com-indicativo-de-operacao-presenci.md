---
id: "360042506974"
titulo: "NF-e com indicativo de Operação Presencial, fora do estabelecimento e não informada NF referenciada.(NT2016/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042506974-NF-e-com-indicativo-de-Opera%C3%A7%C3%A3o-Presencial-fora-do-estabelecimento-e-n%C3%A3o-informada-NF-referenciada-NT2016-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:10:23Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "TOP", "864", "Rejeição 864: Operação Presencial Fora do Estabelecimento", "Erro", "Documentos Eletrônicos"]
---

# NF-e com indicativo de Operação Presencial, fora do estabelecimento e não informada NF referenciada.(NT2016/002)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19258916958871) MENSAGEM:**

864- Rejeição: NF-e com indicativo de Operação Presencial, fora do estabelecimento e não informada NF referenciada.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19258956722711) CAUSA:**

Quando for emitida uma NF-e (modelo 55) com operação presencial fora do estabelecimento **(Campo: indPres = 5)**e não for informado os campos referente a NF referenciada, haverá a rejeição pelo motivo '864 - NF-e com indicativo de Operação presencial, fora do estabelecimento e não informada NF-e referenciada'.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19258916970135) SOLUÇÃO:**

![Imagem 4: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP / Aba: NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/article_attachments/19258956740631) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP / Aba: NF-e/NFC-e

Campo '**Indicador de Presença para NF-e/NFC-e'**: Se estiver informado valor 5, neste campo, considere Informar a Chave NFe Referenciada, na nota;

![Imagem 5: Verifique na TOP / Aba: NF-e/NFC-e, se o campo ' Buscar NF de origem p/ referenciar na NFe' está marcado e observe o…](https://ajuda.sankhya.com.br/hc/article_attachments/19258956746135) Verifique na TOP / Aba: NF-e/NFC-e, se o campo '**Buscar NF de origem p/ referenciar na NFe'** está marcado e observe o campo '**Chave NF-e referenciada':**insira a chave da NF-e conforme está solicitando na mensagem de rejeição.

A SEFAZ considera que por ser uma Operação Presencial fora do estabelecimento, tenha-se uma Nota simbolizando a transferência para um local móvel(carro) em trânsito, efetuando a venda,  por isso exige-se a Nota de Referência.

![Imagem 6: Caso a operação não esteja simbolizando uma Operação Presencial fora do estabelecimento, efetue o ajuste na TOP, no…](https://ajuda.sankhya.com.br/hc/article_attachments/19258956749975) Caso a operação não esteja simbolizando uma Operação Presencial fora do estabelecimento, efetue o ajuste na TOP, no campo '**Indicador de Presença para NF-e/NFC-e**' (Consulte o contador para a correta informação).

Após o ajuste, gere nova nota ou fature novamente e gere o Lote.

Para essa Regra de Validação não há exceções. Quando uma nota fiscal for emitida com indicador de presença 5, deverá ser informada a nota referenciada a essa NFe.

**Observação:**

1-(NT2016/002)

Nota Técnica:

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=>
