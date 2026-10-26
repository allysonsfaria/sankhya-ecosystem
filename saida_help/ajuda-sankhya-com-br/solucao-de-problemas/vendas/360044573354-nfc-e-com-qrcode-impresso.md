---
id: "360044573354"
titulo: "NFC-e com QRCODE impresso"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044573354-NFC-e-com-QRCODE-impresso"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:51:35Z"
rotulos: ["Configuração", "Impressão", "XML", "SEFAZ", "NFC-e", "URLs diferentes para online e offline", "Novo Manual 5.0 altera layout e QR Code", "Ative GERARQRCODEXML e configure UFs para QR Code", "QR Code"]
---

# NFC-e com QRCODE impresso

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18589045342615) SITUAÇÃO:**

No dia 02 de Março foi lançada a [versão 5.0 do Manual de Especificações Técnicas do DANFE NFCe e QR Code](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=/xyXbAFZ71k=) que traz algumas mudanças no layout do documento impresso. Além de alterar a data de emissão da NFCe 4.0, o novo manual trouxe uma nova especificação do QR Code para o documento nesta versão.

No QR Code 2.0, a URL do código deverá ser composta de **duas maneiras diferentes**: uma para NFCe emitidas de forma **online**(sem contingência) e outra para as NFCe emitidas na **contingência offline**.

A Sefaz disponibilizou as novas URL a serem utilizadas nas versões online e offline no [portal do ENCAT](http://nfce.encat.org/). As URLs são as mesmas utilizadas pela consulta por chave de acesso e podem ser encontradas [aqui](http://nfce.encat.org/consumidor/consulte-nota/).

A alteração visa diminuir os dados quando a emissão já tiver sido autorizada pela Sefaz e passar mais informações sobre as notas que ainda não foram autorizadas, como **data de emissão, valor total e DigestValue** da NFCe. A Sefaz ainda disponibilizou um prazo para adequação à essa nova mudança:

- **09 de Julho de 2018** – início da produção da NFCe 4.0 e início da concomitância do QR Code 2.0 com a versão 1.0. Isto é, a NFCe 4.0 aceitará as versões 1.0 e 2.0 do QR Code;
- **1º de Outubro de 2018**– fim da concomitância com a versão 1.0 do QR Code. Ou seja, a NFCe aceitará somente o QR Code 2.0

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18589046343447) SOLUÇÃO:**

**Configurações para gerar o QRCode na impressão de NFC-e**

![Imagem 3: Ative o parâmetro GERARQRCODEXML-Gerar QRCODE no XML da NFC-e?](https://ajuda.sankhya.com.br/hc/article_attachments/18589046358679) Ative o parâmetro **GERARQRCODEXML-Gerar QRCODE no XML da NFC-e?**

   1.1- Via MGEConfigurações:  Menu>>Avançado>>Manutenção de Parâmetros

   1.2- Via SankhyaW : Configurações » Avançado » Preferências

![Imagem 4: Insira a UF do Estado, no parâmetro UFSQRCODEXML-UFs com QRCODE no XML da NFC-e?](https://ajuda.sankhya.com.br/hc/article_attachments/18589045365399) Insira a UF do Estado, no parâmetro **UFSQRCODEXML-UFs com QRCODE no XML da NFC-e?**

Use o mesmo passo  1.1 ou 1.2 para acessar o parâmetro.

**Observação**:

Parâmetro **UFSQRCODEXML (UFs com QRCODE no XML da NFC-e)** do tipo texto com default vazio, ele conterá as UFs que aceitam a tag **<qrCode>** dentro do XML. As UFs devem estar separadas por vírgula. Exemplo: AM,MT,PA,PR,RJ,RO.
