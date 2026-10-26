---
id: "360043128053"
titulo: "NF-e já está inutilizada na base de dados da SEFAZ"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043128053-NF-e-j%C3%A1-est%C3%A1-inutilizada-na-base-de-dados-da-SEFAZ"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-10-22T20:26:28Z"
rotulos: ["ERRONF", "NF-e", "SEFAZ", "206", "Rejeição", "Rejeição 206: NF-e Inutilizada na SEFAZ", "Erro", "Documentos Eletrônicos"]
---

# NF-e já está inutilizada na base de dados da SEFAZ

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16504296279575) MENSAGEM:**

[206 - Rejeição]: NF-e já está inutilizada na Base de dados da SEFAZ.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16504310810647) SOLUÇÃO:**

![Imagem 3: Realize uma consulta de 'Inutilizadas' no site da SEFAZ, para confirmar se o número nota que está sendo enviado de fato…](https://ajuda.sankhya.com.br/hc/article_attachments/16504310813591) Realize uma consulta de 'Inutilizadas' no site da SEFAZ, para confirmar se o número nota que está sendo enviado de fato já foi inutilizado.

<http://www.nfe.fazenda.gov.br/portal/consulta.aspx?tipoConsulta=inutilizacao&tipoConteudo=YG1QjUXR4PY=>

![Imagem 4: http://www.nfe.fazenda.gov.br/portal/consulta.aspx?tipoConsulta=inutilizacao&tipoConteudo=YG1QjUXR4PY=](https://ajuda.sankhya.com.br/hc/article_attachments/360059969234)

![Imagem 5: Se a numeração for identificada na consulta acima, proceda com a exclusão dessa nota e a emissão de uma nova.](https://ajuda.sankhya.com.br/hc/article_attachments/16504310814871) Se a numeração for identificada na consulta acima, proceda com a exclusão dessa nota e a emissão de uma nova.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16504296289559) CAUSA:**

Quando emitida uma NF-e com uma numeração que já foi inutilizada será retornada a rejeição.

**![Imagem 7: IMPORTANTE :](https://ajuda.sankhya.com.br/hc/article_attachments/16504310820119) IMPORTANTE:**

- Certifique que a sequência de numeração está correta e que o próximo número a ser gerado de fato é o esperado para esse **Modelo/Série/Empresa;**
- Certifique que a exclusão da nota será realizada para notas **não recebidas pela SEFAZ**. (O sistema validará exclusão para Status NF-e que possam estar em processamento da SEFAZ, de toda forma a análise é recomendada).
- No SankhyaW é possível que as análises de numerações já inutilizadas sejam realizadas através do Dashboard. Esse pode ser baixado no Place Sankhya. <http://portal.sankhya.com.br/#/store/pacotes/904>
