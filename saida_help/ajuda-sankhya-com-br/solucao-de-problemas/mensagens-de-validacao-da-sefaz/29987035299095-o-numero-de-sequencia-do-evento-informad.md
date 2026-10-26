---
id: "29987035299095"
titulo: "O número de sequência do evento informado é maior que o permitido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29987035299095-O-n%C3%BAmero-de-sequ%C3%AAncia-do-evento-informado-%C3%A9-maior-que-o-permitido"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:36:41Z"
rotulos: ["Configuração", "Eventos", "NF-e", "XML", "SEFAZ", "Preferências", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Rejeição 594", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# O número de sequência do evento informado é maior que o permitido

**Mensagem**

O número de sequência do evento informado é maior que o permitido

**Situação**

Esta mensagem de rejeição pode ocorrer em dois cenários distintos:

1. Ao realizar uma **"Manifestação de documentos"** no **"Portal de Importação de XML"**, caso a nota já possua registros anteriores ou o parâmetro de sequência esteja configurado incorretamente.

2. Ao enviar eventos como **"Carta de Correção"** para a SEFAZ, quando o número de eventos excede o limite permitido.

**Solução**

A solução depende da origem do problema:

**Cenário 1: Manifestação do destinatário**

**(1)** Acesse a tela **"Preferências"** (Configurações >> Preferências).

**(2)** Localize o parâmetro **"Itera NSeqEvento para geração de MDe"** (ITNSEQEVENTOMDE).

**(3)** É necessário que o parâmetro "ITNSEQEVENTOMDE" esteja desligado.

**(4)** Tente realizar novamente a manifestação.

**Cenário 2: Carta de correção (CC-e)**

No **"Portal de Vendas"** (Comercial >> Consulta >> Portal de Vendas), na opção de **NF-e**, gere o XML por meio da opção **"Gerar Arquivo XML de NF-e"**.

Será gerado um arquivo **.ZIP** contendo o XML de aprovação da nota e o XML do evento da carta de correção. Após isso, verifique o campo **"nSeqEvento"** no XML.

A SEFAZ não permite mais de 20 eventos (correções) por NF-e. Caso o valor seja superior a 20, significa que o limite foi atingido.

![Imagem 1: A SEFAZ não permite mais de 20 eventos (correções) por NF-e. Caso o valor seja superior a 20, significa que o limite…](https://ajuda.sankhya.com.br/hc/article_attachments/39452416066711)

![Imagem 2: A SEFAZ não permite mais de 20 eventos (correções) por NF-e. Caso o valor seja superior a 20, significa que o limite…](https://ajuda.sankhya.com.br/hc/article_attachments/29987035295767)

**Causa**

O erro ocorre devido à duplicidade de registros na tabela **"TGFEMDE"** (relacionado ao parâmetro **"ITNSEQEVENTOMDE"**) ou ao atingimento do limite máximo de 20 eventos permitido pela SEFAZ para uma mesma chave de **NF-e**.

**Importante:** a SEFAZ valida a sequência dos eventos. Caso seja enviado, por exemplo, o evento 2 sem que o evento 1 tenha sido previamente recebido, o erro também será apresentado. Nessa situação, é necessário acionar o suporte da Sankhya.
