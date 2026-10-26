---
id: "360043101933"
titulo: "468 Rejeição: NF-e com Tipo Emissão = 4, sem EPEC correspondente.(NT2014/001)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043101933-468-Rejei%C3%A7%C3%A3o-NF-e-com-Tipo-Emiss%C3%A3o-4-sem-EPEC-correspondente-NT2014-001"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-10-20T17:51:35Z"
rotulos: ["ERRONF", "NF-e", "XML", "SEFAZ", "Contingência", "468", "Rejeição 468: EPEC Não Encontrado", "Erro", "468 Rejeição", "Rejeição 468", "Documentos Eletrônicos"]
---

# 468 Rejeição: NF-e com Tipo Emissão = 4, sem EPEC correspondente.(NT2014/001)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16510064470295) MENSAGEM:**

468 Rejeição: NF-e com Tipo Emissão = 4, sem EPEC correspondente. (NT2014/001)

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16510050686743) SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

![Imagem 3: Neste caso, aguarde a sincronização entre SEFAZ Nacional e Estadual, normalmente SEFAZ Nacional recepciona a nota,…](https://ajuda.sankhya.com.br/hc/article_attachments/16510064477463) Neste caso, aguarde a sincronização entre SEFAZ Nacional e Estadual, normalmente SEFAZ Nacional recepciona a nota, porém na Estadual ainda não houve integração desta nota, ou vice versa, primeiro SEFAZ Estadual recepciona e não sincroniza com SEFAZ Nacional.

![Imagem 4: Mesmo que hajam várias tentativas de envio e o erro persista, ainda assim é necessário aguardar. Porém, se passado um…](https://ajuda.sankhya.com.br/hc/article_attachments/16510064484375) Mesmo que hajam várias tentativas de envio e o erro persista, ainda assim é necessário aguardar. Porém, se passado um prazo considerável e não se conseguir realizar a transmissão, entre em contato com a SEFAZ com um chamado formal para averiguação da situação.

![Imagem 5: Vale ressaltar, que desde que a nota seja emitida na Contingência EPEC, se possui o prazo de até 7 dias corridos para a…](https://ajuda.sankhya.com.br/hc/article_attachments/16510050699671) Vale ressaltar, que desde que a nota seja emitida na Contingência EPEC, se possui o prazo de até 7 dias corridos para a regularização da mesma, ou seja, a geração de lote, saindo do StatusNFe = S - Enviada EPEC e transmissão para StatusNFe = A - Aprovada.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16510064491543) CAUSA:**

Uma NF-e emitida em Contingência EPEC precisa ser transmitida a Sefaz Estadual imediatamente após cessar os problemas técnicos no Ambiente Autorizador da Sefaz Estadual. Nesse tipo de Contingência, primeiro é enviado o Evento EPEC para a Sefaz Nacional, que compartilhará o mesmo com o Ambiente Estadual.

Quando uma NF-e em Contingência EPEC for recebida pela Sefaz Estadual e a Sefaz Nacional ainda não tiver feito o compartilhamento do Evento EPEC com a Sefaz Estadual, será retornado a rejeição.

Essa situação pode ocorrer tanto por uma falha na Sefaz Nacional ao compartilhar o Evento quanto por um falha na Sefaz Estadual ao receber o Evento EPEC.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16510050706199) OBSERVAÇÃO:**

**(1)** ([NT2014/001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=1m6MlHgr744=)) - Nota técnica

**(1)** Representação de Status da NF-e no sistema(TGFCAB.STATUSNFE)

'D' - DENEGADA
'A' - Aprovada
'E' - Aguardando Autoriz.
'R' - Aguardando Correção
'V' - Com erro de Validação
'P' - Pendente de Retorno
'N' - Não enviada
'I' - Enviada
'S'- Enviada DPEC
