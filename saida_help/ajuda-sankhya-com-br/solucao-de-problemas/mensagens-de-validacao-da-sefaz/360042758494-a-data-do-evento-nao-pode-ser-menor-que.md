---
id: "360042758494"
titulo: "A data do evento não pode ser menor que a data de autorização para NF-e não emitida em contingência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042758494-A-data-do-evento-n%C3%A3o-pode-ser-menor-que-a-data-de-autoriza%C3%A7%C3%A3o-para-NF-e-n%C3%A3o-emitida-em-conting%C3%AAncia"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:04Z"
rotulos: ["ERRONF", "Eventos", "Fiscal", "NF-e", "SEFAZ", "579", "Data de Evento", "Verificação de Hora", "Conferência de Data", "Erro", "Documentos Eletrônicos"]
---

# A data do evento não pode ser menor que a data de autorização para NF-e não emitida em contingência

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16453209205783) MENSAGEM:**

[579- Rejeição]: A data do evento não pode ser menor que a data de autorização para NF-e não emitida em contingencia.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16453209207575) SOLUÇÃO:**

![Imagem 3: Acesse o site da SEFAZ, busque pela chave NF-e da nota origem do evento enviado e verifique a Data/Hora registrada no…](https://ajuda.sankhya.com.br/hc/article_attachments/16453209212183) Acesse o site da SEFAZ, busque pela chave NF-e da nota origem do evento enviado e verifique a Data/Hora registrada no Campo 'Data Autorização' do Evento 'Autorização de Uso', conforme destacado abaixo:

**Link para consulta :** <http://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=completa&tipoConteudo=XbSeqxE8pl8=>

![Imagem 4: Link para consulta :…](https://ajuda.sankhya.com.br/hc/article_attachments/360059973214)

![Imagem 5: Para o evento que está sendo gerado, a data/hora de envio deve ser posterior a data registrada acima.](https://ajuda.sankhya.com.br/hc/article_attachments/16453177262487) Para o evento que está sendo gerado, a data/hora de envio deve ser posterior a data registrada acima.

![Imagem 6: Verifique se a hora do seu servidor encontra-se atualizada com a hora local, ou se tratar de algum evento lançado, se…](https://ajuda.sankhya.com.br/hc/article_attachments/16453177270551) Verifique se a hora do seu servidor encontra-se atualizada com a hora local, ou se tratar de algum evento lançado, se as informações de data foram preenchidas corretamente.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16453209217303) CAUSA:**

Ao emitir um evento (Exemplos: Carta de correção, Cancelamento ou Manifestação do destinatário) para ser vinculado a uma NF-e autorizada pela SEFAZ, seja esse evento qual for, se a data de emissão do evento for menor do que a data de autorização da NF-e, ocorrerá a rejeição.
