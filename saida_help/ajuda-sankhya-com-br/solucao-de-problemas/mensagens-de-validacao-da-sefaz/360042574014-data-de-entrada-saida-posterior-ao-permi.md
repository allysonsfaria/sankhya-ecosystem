---
id: "360042574014"
titulo: "Data de Entrada/Saida posterior ao permitido (Posterior a 30 dias)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042574014-Data-de-Entrada-Saida-posterior-ao-permitido-Posterior-a-30-dias"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:33Z"
rotulos: ["ERRONF", "#PUBLIFER", "NF-e", "Portal de Vendas", "XML", "SEFAZ", "504", "Data de Entrada/Saída ultrapassa 30 dias", "Verificar e ajustar data no XML", "Data posterior a 30 dias da emissão", "Erro", "Documentos Eletrônicos"]
---

# Data de Entrada/Saida posterior ao permitido (Posterior a 30 dias)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16459901887895) MENSAGEM:**

504 - Data de Entrada/Saída posterior ao permitido (Posterior a 30 dias)

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16459901898007) SOLUÇÃO:**

![Imagem 3: Para resolver a rejeição verifique no XML da NF-e a tag <dhSaiEnt> (Data de Entrada/Saída) e veja se ela é posterior a…](https://ajuda.sankhya.com.br/hc/article_attachments/16459901900567) Para resolver a rejeição verifique no XML da NF-e a tag <dhSaiEnt> (Data de Entrada/Saída) e veja se ela é posterior a 30 dias da data de autorização (<dhEmi>)

- Portal de Vendas » NF-e »**"Gerar XML em arquivo para conferência"**
- Abra o XML [Bloco de Notas e/ou Internet Explorer]
- Verifique a informação das tags abaixo:

**<dhEmi>**2019-12-26T16:05:58-03:00**</dhEmi>**
**<dhSaiEnt>**2020-01-30T23:59:59-03:00**</dhSaiEnt>**

Conforme exemplo acima, a data entrada/saída (30/01/2020) é mais do que 30 dias posterior a data de emissão (26/12/2019).

![Imagem 4: Na Central de Vendas, ajuste a informação inserida em 'Data Entrada/Saída' e gere um novo lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16459934009111) Na Central de Vendas, ajuste a informação inserida em 'Data Entrada/Saída' e gere um novo lote.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16459934010263) CAUSA:**

Se informado Data de Entrada / Saída (dhSaiEnt) e essa data for posterior a 30 dias da data de autorização, será apresentada a rejeição.
