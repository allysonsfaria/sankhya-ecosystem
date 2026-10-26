---
id: "39358036748183"
titulo: "Tipo de NF-e não preparado para processamento no portal de importação de XML"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39358036748183-Tipo-de-NF-e-n%C3%A3o-preparado-para-processamento-no-portal-de-importa%C3%A7%C3%A3o-de-XML"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-09-28T19:05:54Z"
rotulos: ["Configuração", "NF-e", "XML", "Importação", "TOP", "Artigo criado KCS", "Docs Eletrônicos - KCS"]
---

# Tipo de NF-e não preparado para processamento no portal de importação de XML

**MENSAGEM**

Tipo de NF-e não preparado para processamento no portal de importação de XML

**SITUAÇÃO**

Ao tentar importar documentos fiscais eletrônicos por meio do **Portal de Importação de XML**, o sistema apresenta uma mensagem de erro e impede o processamento do documento.

Isso ocorre porque alguns tipos de documentos fiscais não possuem suporte para importação automática pelo Portal de Importação de XML. Entre eles, estão:

- **Modelo 65**: Nota Fiscal de Consumidor Eletrônica (NFC-e);
- **Modelo 66**: Nota Fiscal/Conta de Energia Elétrica Eletrônica (NF3e);
- **Modelo 62**: Nota Fiscal Fatura de Serviço de Comunicação Eletrônica (NFCom);
- **NFS-e**: Nota Fiscal de Serviço Eletrônica.

É importante destacar que a **NFS-e possui características, estruturas e padrões específicos**, diferentes dos utilizados em documentos fiscais eletrônicos, como a NF-e e o CT-e.

Por esse motivo, **o fato de um documento fiscal possuir um arquivo XML não significa, necessariamente, que ele seja compatível com o Portal de Importação de XML**. Para que a importação seja realizada automaticamente, o documento precisa estar entre os modelos e tipos fiscais suportados pelo portal.

Dessa forma, quando o documento não possui suporte para processamento, a importação pelo Portal de Importação de XML não poderá ser concluída.

**CAUSA**

O documento fiscal informado não possui suporte para processamento no **Portal de Importação de XML**. Embora o arquivo esteja disponível no formato XML, sua estrutura e seu modelo fiscal não são compatíveis com os padrões dos documentos atualmente suportados pelo portal.
