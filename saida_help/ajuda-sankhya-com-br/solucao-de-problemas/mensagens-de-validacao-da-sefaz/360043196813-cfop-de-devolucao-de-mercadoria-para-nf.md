---
id: "360043196813"
titulo: "CFOP de devolução de mercadoria para NF-e que não tem finalidade de devolução de mercadoria"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043196813-CFOP-de-devolu%C3%A7%C3%A3o-de-mercadoria-para-NF-e-que-n%C3%A3o-tem-finalidade-de-devolu%C3%A7%C3%A3o-de-mercadoria"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:46Z"
rotulos: ["ERRONF", "#criadoRoger", "Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "CFOP", "328", "Ajustar finalidade NF-e", "CFOP devolução incorreto", "Finalidade NF-e incompatível"]
---

# CFOP de devolução de mercadoria para NF-e que não tem finalidade de devolução de mercadoria

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16512580530839) MENSAGEM:**

[328 - Rejeição]: CFOP de devolução de mercadoria para NF-e que não tem finalidade de devolução de mercadoria.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16512580535831) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16512580540055) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

- Aba: **"NF-e/NFC-e"**
- Campo **"NF-e":** Devolução ou Complementar

![Imagem 4: Campo "NF-e": Devolução ou Complementar](https://ajuda.sankhya.com.br/hc/article_attachments/14626263946647)

A rejeição ocorre porque está sendo utilizada uma CFOP de DEVOLUÇÃO e no cadastro da TOP o campo "**NF-e"** da aba Impressão foi definido diferente de 'Devolução' ou 'Complementar'.

Após o ajuste, inutilize a numeração da nota e gere uma nova.

![Imagem 5: Caso a NF-e emitida não seja uma devolução, por exemplo, um retorno de remessa, revise o CFOP utilizado.](https://ajuda.sankhya.com.br/hc/article_attachments/16512580541463) Caso a NF-e emitida não seja uma devolução, por exemplo, um retorno de remessa, revise o CFOP utilizado.

Sintonize junto ao seu contador o CFOP correto e realize os devidos ajustes:

- Tela **"[Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** (Caminho de acesso: Comercial » Arquivo » Cadastros/Financeiro » Arquivos » Cadastros)
- Aba **"Livro Fiscal",** Campo **:**  **"CFOP'S"**;

![Imagem 6: Caso não se trate de uma NF-e de Estorno, o campo abaixo deve estar desmarcado.](https://ajuda.sankhya.com.br/hc/article_attachments/16512580543767) Caso não se trate de uma **NF-e de Estorno,** o campo abaixo deve estar desmarcado.

- Tela **"Tipo de Operação - TOP"**  » aba **"NF-e/NFC-e"**
  Campo **"NF-e de estorno":** desmarcado

![Imagem 7: Após ajustes na TOP, a nota deve ser inutilizada/excluída e um novo faturamento realizado.](https://ajuda.sankhya.com.br/hc/article_attachments/16512580545047) Após ajustes na TOP, a nota deve ser inutilizada/excluída e um novo faturamento realizado.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16512607708567) CAUSA:**

Quando for emitida uma NF-e com CFOP de Devolução de Mercadoria e a Finalidade da NF-e (finNFe) for diferente de 2 - "NF-e Complementar" ou 4 - "Devolução de Mercadoria", será retornada a rejeição "328 - CFOP de devolução de mercadoria para NF-e que não tem finalidade de devolução de mercadoria".

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16512580549655) OBSERVAÇÃO:**

([NT2015/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=VNyyxYte6T4=)) - Nota técnica
