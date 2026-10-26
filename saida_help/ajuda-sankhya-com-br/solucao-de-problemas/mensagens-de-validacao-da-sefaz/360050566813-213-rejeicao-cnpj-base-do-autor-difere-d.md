---
id: "360050566813"
titulo: "213-Rejeição: CNPJ-Base do Autor difere do CNPJ-Base do Certificado Digital"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360050566813-213-Rejei%C3%A7%C3%A3o-CNPJ-Base-do-Autor-difere-do-CNPJ-Base-do-Certificado-Digital"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:30:59Z"
rotulos: ["#criadoRoger", "CNPJ", "NF-e", "SEFAZ", "Certificado digital", "Rejeição 213", "CNPJ-Base", "Erro"]
---

# 213-Rejeição: CNPJ-Base do Autor difere do CNPJ-Base do Certificado Digital

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18604773314839) MENSAGEM**:

213-Rejeição: CNPJ-Base do Autor difere do CNPJ-Base do Certificado Digital. (NT2011/003)

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/18604746667415) SOLUÇÃO**:

Verifique se o CNPJ-Base do emitente foi informado corretamente na NF-e. Caso esteja correto o CNPJ-Base do emitente, confirme se o Certificado Digital usado para assinar a NF-e é realmente o certificado emitido para o CNPJ-Base do emitente.

**![Imagem 3: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/18604746669719) CAUSA**:

Quando uma NF-e for emitida com um CNPJ-Base (CNPJ do emitente) diferente do CNPJ-Base do Certificado Digital, será retornado a rejeição "213 - CNPJ-Base do Autor difere do CNPJ-Base do Certificado Digital".

 Há duas situações em que pode ocorrer essa situação:

![Imagem 4: Quando o CNPJ-Base do emitente for informado errado;](https://ajuda.sankhya.com.br/hc/article_attachments/18604773326231) Quando o CNPJ-Base do emitente for informado errado;

![Imagem 5: Quando a NF-e for assinada com um Certificado Digital errado.](https://ajuda.sankhya.com.br/hc/article_attachments/18604746681367) Quando a NF-e for assinada com um Certificado Digital errado.

**Observação:**

1-Nota Tecnica 2011/003
<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=tsiloeZ6vBw=>
